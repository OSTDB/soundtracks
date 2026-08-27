# Submitting a soundtrack via pull request

You can submit a soundtrack link — or correct an existing one — by opening a pull request. You don't need to install Git or use the command line; this can all be done in the browser.

## Step by step (browser only)

1. Check the [`missing/`](missing/) folder for a file named `missing/<igdb_id>-<name>.json` matching your game — the `igdb_id` and `game_name` are already filled in for you. Browse or use GitHub's file search to find it.
   - **Found it?** Click the **pencil (✎) icon** in the top right of that file to edit it, fill in the fields below, and skip to step 3.
   - **Not there?** Your game hasn't been scanned into `missing/` yet (or already has a soundtrack). Open [`submissions/TEMPLATE.json`](submissions/TEMPLATE.json) instead, click the pencil icon to edit a copy, and rename the file at the top to something like `submissions/1234-example-game.json` (use the game's IGDB ID and a short name).
2. Fill in your game's info (see **Fields** below). Delete the `_readme` line — it's just a note, not a real field.
3. Scroll down, and under "Commit changes" choose **"Create a new branch and start a pull request."** Click **Propose changes**, then **Create pull request** on the next screen.
4. That's it — a maintainer will review it from here.

Once your pull request is merged, the file is picked up automatically and added to the review queue on ostdb.net. It is **not published immediately** — an admin still approves it before it goes live, the same as a submission made through the website. Only after an admin approves it does a bot remove the file from `missing/` or `submissions/` in a follow-up commit — until then, the file stays put. That's expected, not an error.

## Fields

| Field | Required | Description |
|---|---|---|
| `igdb_id` | yes | The game's numeric IGDB ID — see below for how to find it |
| `game_name` | yes | Game name |
| `album_name` | yes | Soundtrack/album name |
| `spotify_url` | at least one of these three | Spotify album URL |
| `apple_music_url` | at least one of these three | Apple Music album URL |
| `album_link_url` | at least one of these three | [album.link](https://album.link) URL |
| `album_cover_url` | yes | Album cover art URL |

Leave a field as `""` (empty string) if it doesn't apply — don't delete it from the file.

### Finding the IGDB ID

If you're editing a file from `missing/`, the `igdb_id` is already filled in — skip this section.

ostdb.net URLs use a name-based slug (e.g. `ostdb.net/games/genshin-impact`), not the numeric IGDB ID, so you won't find it there directly. Instead:

1. Find the game on [ostdb.net](https://ostdb.net) (search, or browse) and open its page.
2. Click **"Submit soundtrack for `<game>`"** on that page — it links to `ostdb.net/submit?igdb=<ID>`.
3. The number after `?igdb=` in that URL is the `igdb_id` you need.

If the game isn't on ostdb.net at all yet, use the [website submit form](https://ostdb.net/submit) instead — it looks the game up on IGDB for you by name and resolves the ID automatically. If you're unsure, just fill in the game name and open the PR anyway; an admin can resolve the correct ID during review.

### Adding a soundtrack to a game that already has one

You don't need to look up or set any internal ID to add another soundtrack, or to correct an existing one. Just submit with the same `igdb_id` and the exact `album_name` of the entry you're correcting:

- **Same `igdb_id`, new `album_name`** → adds a new soundtrack entry alongside the existing one(s).
- **Same `igdb_id` and `album_name` matching an existing approved soundtrack** → treated as a correction to that entry (its links get updated instead of creating a duplicate).

This matches how it works on the website: pick a game, and you either add a new soundtrack or edit one that's already there. Note that a game with an existing soundtrack won't have a file in `missing/` — use `submissions/TEMPLATE.json` for this instead.

### How to actually do this via PR

You always create a **new** JSON file in `submissions/` for this — never edit an already-merged submission file, since those get deleted by the bot right after they're processed.

**To add another soundtrack (e.g. a second volume, or a DLC OST) to a game already on ostdb.net:**

1. Same as a fresh submission: copy `submissions/TEMPLATE.json`, name the new file `submissions/<igdb_id>-<name>-vol2.json` (or similar — the filename itself doesn't matter, only the fields inside do).
2. Use the **same `igdb_id`** as the existing game.
3. Use a **different `album_name`** than any existing soundtrack for that game (e.g. `"Crimson Desert (Original Soundtrack Volume 2)"` instead of `"...Volume 1"`).
4. Fill in `spotify_url` / `apple_music_url` / `album_link_url` and `album_cover_url` for this new album — its own cover, not the game's.
5. Open the PR as usual.

**To correct an existing soundtrack's links, name, or cover:**

1. Same as above — new file in `submissions/`, same `igdb_id`.
2. Use the **exact same `album_name`** (character-for-character) as the entry you're correcting — check the game's page on ostdb.net if you're not sure of the exact wording.
3. Fill in the corrected fields. This gets treated as an edit request, not a duplicate — the admin will see it as an update to the existing entry, not a new one.

In both cases the game's own cover art is **not** part of this file — it's fetched automatically from IGDB using `igdb_id`. `album_cover_url` here is only the cover of the soundtrack/album itself.
