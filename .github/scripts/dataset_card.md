---
license: cc-by-nc-sa-4.0
pretty_name: OSTDB - Video Game Soundtracks
language:
  - en
tags:
  - music
  - video-games
  - soundtracks
  - spotify
  - apple-music
size_categories:
  - 1K<n<10K
configs:
  - config_name: default
    data_files: ostdb.csv
---

# OSTDB: official video game soundtracks

The open database of official video game soundtracks from [ostdb.net](https://ostdb.net): **{{games}} games** and **{{albums}} soundtrack albums**, each with Spotify, Apple Music and/or album.link URLs.

Built {{built_at}} from [OSTDB/soundtracks](https://github.com/OSTDB/soundtracks), where the community adds and reviews every entry.

## Files

| File | Contents |
|---|---|
| `ostdb.csv` | One row per album: `igdb_id`, `game_name`, `game_url`, `album_name`, `spotify_url`, `apple_music_url`, `album_link_url` |
| `ostdb.json` | Every game with its albums and cover art URL |
| `ostdb.sqlite` | Tables `games`, `albums` and `meta` |

`igdb_id` is the game's [IGDB](https://www.igdb.com) id, so the data joins easily with IGDB.

## License

Data licensed **[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)**: non-commercial use, share alike, and credit with a link:

> Data from [OSTDB (ostdb.net)](https://ostdb.net)

Album art, game art and IGDB metadata are not covered and belong to their owners. OSTDB is a non-commercial fan project, not affiliated with Spotify, Apple, IGDB or any game company. Commercial use: [support@ostdb.net](mailto:support@ostdb.net).
