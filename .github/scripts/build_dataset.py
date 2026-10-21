"""Build the downloadable OSTDB dataset from all-games.json.

Writes to dist/:
  ostdb.json    every game with its albums (same shape as all-games.json)
  ostdb.csv     one row per album
  ostdb.sqlite  tables `games` and `albums`, plus a `meta` table with the license
  README.md     dataset card (also used for the Hugging Face mirror)

Streaming links are filed by their domain, so a link stored in the wrong
field still lands in the right column.
"""

import csv
import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "dist"


def platform_of(url):
    host = (urlparse(url).hostname or "").lower()
    if host.endswith("spotify.com"):
        return "spotify_url"
    if host.endswith("music.apple.com") or host.endswith("itunes.apple.com"):
        return "apple_music_url"
    if host.endswith("album.link") or host.endswith("song.link") or host.endswith("odesli.co"):
        return "album_link_url"
    return None


def normalise_links(album):
    links = {"spotify_url": None, "apple_music_url": None, "album_link_url": None}
    for field in links:
        url = album.get(field)
        if not url:
            continue
        target = platform_of(url) or field
        links[target] = links[target] or url
    return links


def main():
    source = json.loads((ROOT / "all-games.json").read_text(encoding="utf-8"))
    DIST.mkdir(exist_ok=True)
    built_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    games = []
    rows = []
    for game in source["games"]:
        albums = []
        for album in game["albums"]:
            entry = {"album_name": album["album_name"], **normalise_links(album)}
            albums.append(entry)
            rows.append(
                {
                    "igdb_id": game["igdb_id"],
                    "game_name": game["game_name"],
                    "game_url": game["game_url"],
                    **entry,
                }
            )
        games.append({**game, "albums": albums})

    meta = {k: source[k] for k in ("license", "license_url", "attribution", "notice") if k in source}
    meta["built_at"] = built_at
    meta["source_generated_at"] = source.get("generated_at")
    meta["total_games"] = len(games)
    meta["total_albums"] = len(rows)

    (DIST / "ostdb.json").write_text(
        json.dumps({**meta, "games": games}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    fields = ["igdb_id", "game_name", "game_url", "album_name", "spotify_url", "apple_music_url", "album_link_url"]
    with (DIST / "ostdb.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    database = DIST / "ostdb.sqlite"
    database.unlink(missing_ok=True)
    with sqlite3.connect(database) as db:
        db.executescript(
            """
            CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT);
            CREATE TABLE games (
              igdb_id INTEGER PRIMARY KEY,
              game_name TEXT NOT NULL,
              game_url TEXT NOT NULL,
              cover_url TEXT
            );
            CREATE TABLE albums (
              id INTEGER PRIMARY KEY,
              igdb_id INTEGER NOT NULL REFERENCES games(igdb_id),
              album_name TEXT NOT NULL,
              spotify_url TEXT,
              apple_music_url TEXT,
              album_link_url TEXT
            );
            CREATE INDEX albums_by_game ON albums(igdb_id);
            """
        )
        db.executemany("INSERT INTO meta VALUES (?, ?)", [(k, str(v)) for k, v in meta.items()])
        db.executemany(
            "INSERT OR IGNORE INTO games VALUES (?, ?, ?, ?)",
            [(g["igdb_id"], g["game_name"], g["game_url"], g.get("cover_url")) for g in games],
        )
        db.executemany(
            "INSERT INTO albums (igdb_id, album_name, spotify_url, apple_music_url, album_link_url) VALUES (?, ?, ?, ?, ?)",
            [
                (r["igdb_id"], r["album_name"], r["spotify_url"], r["apple_music_url"], r["album_link_url"])
                for r in rows
            ],
        )

    card = (ROOT / ".github" / "scripts" / "dataset_card.md").read_text(encoding="utf-8")
    (DIST / "README.md").write_text(
        card.replace("{{games}}", f"{len(games):,}").replace("{{albums}}", f"{len(rows):,}").replace("{{built_at}}", built_at),
        encoding="utf-8",
    )
    print(f"{len(games)} games, {len(rows)} albums -> {DIST}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
