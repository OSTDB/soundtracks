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
| `igdb_id` | yes | The game's IGDB ID (find it in the ostdb.net URL, e.g. `ostdb.net/games/1234`) |
| `game_name` | yes | Game name |
| `album_name` | yes | Soundtrack/album name |
| `spotify_url` | one of these three | Spotify album URL |
| `apple_music_url` | one of these three | Apple Music album URL |
| `album_link_url` | one of these three | [album.link](https://album.link) URL |
| `cover_url` | no | Game cover art URL |
| `album_cover_url` | yes | Album cover art URL |
| `edit_target_id` | no | Set this to correct an **existing** soundtrack entry instead of adding a new one — use the soundtrack's `id` as shown on ostdb.net |

At least one of `spotify_url`, `apple_music_url`, or `album_link_url` must be filled in.
