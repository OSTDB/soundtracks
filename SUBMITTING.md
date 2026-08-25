# Submitting a soundtrack via pull request

You can submit a soundtrack link — or a correction to an existing one — by opening a pull request instead of using [ostdb.net](https://ostdb.net) directly.

## How it works

1. Copy [`submissions/TEMPLATE.json`](submissions/TEMPLATE.json) to a new file under `submissions/`, e.g. `submissions/1234-example-game.json`.
2. Fill in the fields (see below).
3. Open a pull request.
4. Once merged, the file is picked up automatically and added to the review queue on ostdb.net — it is **not** published immediately. An admin still reviews and approves it before it appears on the site, same as a submission made through the website.
5. After processing, the bot removes your file from `submissions/` in a follow-up commit.

## Fields

| Field | Required | Description |
|---|---|---|
| `igdb_id` | yes | The game's numeric [IGDB](https://www.igdb.com) ID — see below for how to find it |
| `game_name` | yes | Game name |
| `album_name` | yes | Soundtrack/album name |
| `spotify_url` | one of these three | Spotify album URL |
| `apple_music_url` | one of these three | Apple Music album URL |
| `album_link_url` | one of these three | [album.link](https://album.link) URL |
| `cover_url` | no | Game cover art URL |
| `album_cover_url` | yes | Album cover art URL |

At least one of `spotify_url`, `apple_music_url`, or `album_link_url` must be filled in.

### Finding the IGDB ID

ostdb.net URLs use a name-based slug (e.g. `ostdb.net/games/genshin-impact`), not the numeric IGDB ID, so you won't find it there directly. Instead:

1. Find the game on [ostdb.net](https://ostdb.net) (search, or browse) and open its page.
2. Click **"Submit soundtrack for `<game>`"** on that page — it links to `ostdb.net/submit?igdb=<ID>`.
3. The number after `?igdb=` in that URL is the `igdb_id` you need.

If the game isn't on ostdb.net at all yet, use the [website submit form](https://ostdb.net/submit) instead — it looks the game up on IGDB for you by name and resolves the ID automatically. If you're unsure, just fill in the game name and open the PR anyway; an admin can resolve the correct ID during review.

### Adding a soundtrack to a game that already has one

You don't need to look up or set any internal ID to add another soundtrack, or to correct an existing one. Just submit with the same `igdb_id` and the exact `album_name` of the entry you're correcting:

- **Same `igdb_id`, new `album_name`** → adds a new soundtrack entry alongside the existing one(s).
- **Same `igdb_id` and `album_name` matching an existing approved soundtrack** → treated as a correction to that entry (its links get updated instead of creating a duplicate).

This matches how it works on the website: pick a game, and you either add a new soundtrack or edit one that's already there.
