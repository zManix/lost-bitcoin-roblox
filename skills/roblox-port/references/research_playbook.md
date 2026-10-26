# Phase 1 playbook: study the source game until you could rebuild it from memory

The goal is to understand WHAT the player does second to second, WHY it feels good, and EXACTLY how it looks:
- UI layout
- palette
- lighting
- animation timing
- juice

Claude can't watch video, so turn every video into frames and read them. Shallow research produced an ugly, boring
build once (771 tests passed, the owner hated it). Depth here is what prevents that.

## 1. Store data (scripts/steam_fetch.py)
`python scripts/steam_fetch.py "<url|appid|name>" --out <ws>/research/steam`
- Run everything from the workspace and call scripts by absolute path (`python "<skill-dir>/scripts/x.py"`; on
  Linux/macOS use `python3`).
- The reviews API often returns HTML (a region redirect). That's normal: read REVIEW_PAGES.txt with WebFetch instead.
- extras/ may contain promos or other games (Discord banners, cross-promotion): skim before deep study.
- Read summary.md and description.txt fully. Note the release date (unreleased = no reviews: use the ancestors' and
  similar games' reviews instead), price, the AI-content note, modes, numbers (cube sizes, counts of
  spells/perks/levels, playtime claims).
- Not on Steam (itch, mobile, console, website)? Use WebFetch on the page plus WebSearch, and download any trailer you
  can legitimately reach (ffmpeg on direct mp4/m3u8 links). Skip anything behind a login.

## 2. Look at EVERYTHING (scripts/frames.py)
- Screenshots: `frames.py images <ws>/research/steam/screenshots --out <ws>/research/frames`. Read every sheet.
- Each trailer: `frames.py sheets <trailer> --out <ws>/research/frames --fps 1 --dedupe` (long videos auto-cap at 90
  frames; --dedupe drops static holds). Read every sheet in order and write down what happens at each second. Skim
  logo/end cards; when several trailers share shots, read the longest gameplay one fully and skim the others.
- Store clips (extras/): `frames.py sheets` with --fps 2 (they're short).
- Then go deeper on the moments that matter, at full resolution:
  - `frames.py key <video> --times a,b,c --out <ws>/research/hi` for: every menu/UI screen (level-up, shop,
    collection, leaderboard, settings), the HUD (crop mentally: bottom bar, corners), tooltips/hint text, a
    representative scene per area/biome/depth, the title card.
  - `frames.py strip <video> --start S --dur 1.2 --fps 10 --out ...` for animation timing: the core action (punch,
    swing, shot), a level-up, a reward/pickup, a big moment (boss, find, win).
- Small sprites or HUD details: add `--crop x,y,w,h` to `strip`, or use `key` and read the PNG.
- Palette hexes: `frames.py palette <image> [--crop x,y,w,h]` on one representative frame per area.
- Write down exact UI text you see (button labels, stat lines, flavor lines). It tells you the systems (e.g. "Banish
  removes it for the rest of the run", "DEPTH II", "RISKS" tabs). We copy the SYSTEMS, never the names/text.

## 3. Gameplay videos (scripts/yt_study.py) — run on the user's PC
- `python "<skill-dir>/scripts/yt_study.py" search "<exact game title> gameplay" --n 15 --json <ws>/research/videos.jsonl` (also try the title alone, the title +
  "steam", the developer name, the title in Japanese/Korean if it's popular there). Pick 3–6 videos: the longest
  playthroughs, the most viewed, and the developer's own channel.
- `python scripts/yt_study.py get ID1 ID2 ... --out <ws>/research/videos --every 20`. Then read the frame sheets and
  `ID.transcript.txt` (what the YouTuber reacts to = what's fun; what they complain about = what to fix).
- If YouTube shows a bot check (common on servers, rare on home PCs): stop downloads, note it, never work around it.
  Instead:
  (a) keep the search list (videos.jsonl) as the build agent's R0 watch list (it runs on the user's PC and can
      usually download)
  (b) lean harder on review text and the trailers' 10-fps strips
  (c) mark animation timings as [ESTIMATE]
  (d) optionally tell the user they can drop video files into <ws>/research/videos and you'll study them.

## 4. Reviews and community
- WebFetch the URLs in REVIEW_PAGES.txt (top-rated negative AND positive). Pull the top 5 loves and top 5 hates, with
  short quotes.
- WebSearch: "<title> review", "<title> reddit", "<developer> devlog", press coverage, sales/wishlist signals.
- Unreleased game: use the closest ancestors' reviews (the games it's clearly based on), and say so.

## 5. Comparable games (one subagent, in parallel)
If no subagent tool is available, do this yourself after §4 (same brief). Spawn a general-purpose subagent: "Find the 10–15 closest games to <title> on Steam/mobile/console. For each: sales or
review count + score (source), core loop in 8 words, top 3 loves/hates with quotes, and what made it sell." This
gives the evidence for "proven loop" claims.

## 6. Write STUDY.md (the build agent reads this; make it concrete)
Sections:
1. What the game is (facts, modes, numbers, release, team)
2. Why it works (6–10 design lessons; each one names the moment in the footage that proves it)
3. Visual language:
   - post-process look
   - materials and texture style
   - character/viewmodel style
   - colors with sampled hexes per area
   - lighting sources
   - VFX
   - UI fonts, panel colors and accents
4. UI inventory: every screen and HUD element with its layout and the exact labels seen
5. Systems observed: progression, upgrades/cards/skills (names as reference only), currencies, modes, events,
   specials/secrets, leaderboards, saves
6. Animation & juice timings (from the 10-fps strips)
7. Loves / hates (quotes)
8. Roblox translation decisions: keep / change / add
9. Videos for the build agent (IDs, titles, lengths), so it can study them itself on the user's PC

Also pick 15–30 reference images for `style_refs/` (store screenshots + full-res UI keyframes + 1–2 animation strips).
Name them by what they show (ui_cards.jpg, hud_full.jpg, area_rose_tunnel.jpg, anim_punch_10fps.jpg).
