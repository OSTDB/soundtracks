# Submitting a soundtrack via pull request

You can submit a soundtrack link — or correct an existing one — by opening a pull request. You don't need to install Git or use the command line; this can all be done in the browser.

## Step by step (browser only)

1. Open [`submissions/TEMPLATE.json`](submissions/TEMPLATE.json) in this repo.
2. Click the **pencil (✎) icon** in the top right of the file view to edit a copy of it.
3. GitHub will ask you to name the new file — change the filename at the top from `submissions/TEMPLATE.json` to something like `submissions/1234-example-game.json` (use the game's IGDB ID and a short name).
4. Replace the example values with your game's info (see **Fields** below). Delete the `_readme` line — it's just a note, not a real field.
5. Scroll down, and under "Commit changes" choose **"Create a new branch and start a pull request."** Click **Propose changes**, then **Create pull request** on the next screen.
6. That's it — a maintainer will review it from here.

Once your pull request is merged, the file is picked up automatically and added to the review queue on ostdb.net. It is **not published immediately** — an admin still approves it before it goes live, the same as a submission made through the website. After it's processed, a bot removes your file from `submissions/` in a follow-up commit — that's expected, not an error.

## Fields

| Field | Required | Description |
|---|---|---|
| `igdb_id` | yes | The game's numeric IGDB ID — see below for how to find it |
| `game_name` | yes | Game name |
| `album_name` | yes | Soundtrack/album name |
| `spotify_url` | at least one of these three | Spotify album URL |
| `apple_music_url` | at least one of these three | Apple Music album URL |
| `album_link_url` | at least one of these three | [album.link](https://album.link) URL |
| `cover_url` | no | Game cover art URL |
| `album_cover_url` | yes | Album cover art URL |

Leave a field as `""` (empty string) if it doesn't apply — don't delete it from the file.

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
