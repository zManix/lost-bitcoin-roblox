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
Get 10–20 videos, at least one of each type (search each type separately):
- **first hour** of a new player ("<title> first time", "part 1"): onboarding, tutorial text, the first unlocks
- **full playthrough / longplay**: the whole progression and pacing
- **endgame / 100% / final boss**: late systems, max upgrades, what "done" looks like
- **speedrun / high skill** (speedrun.com links): the movement ceiling, tech, exact timings
- **guides / tips / "everything you need to know"**: the hidden rules, best builds, numbers people quote
- **reviews / critiques**: what's loved and hated
- **devlogs, trailers, GDC/interviews**: the intent behind the design
Per video, note timestamps for every system, screen and moment. Read captions for numbers and terms.
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

## 3b. Wikis and written sources (the exact numbers live here)
WebSearch + WebFetch, and save what you read to <ws>/research/wiki/ (source URL at the top of each file):
- the game's wiki: "<title> wiki" (wiki.gg, Fandom, an official wiki). Read EVERY page on mechanics, items/upgrades,
  abilities, enemies/obstacles, levels/worlds, currencies, shops, achievements and patch history.
- Steam: the community guides (steamcommunity.com/app/<appid>/guides, highest rated first), the achievements list
  (steamcommunity.com/stats/<appid>/achievements: it lists every system and goal), the news/patch notes
  (balance numbers change there), the discussions (FAQ threads, "how does X work").
- Reddit (r/<game>): "how does … work", tips, tier lists, datamined numbers.
- speedrun.com (categories, rules, tech notes), dev interviews, GDC talks, the press kit.
Record every number with its source. When sources disagree, prefer: patch notes > datamine > wiki > guides > videos.

## 3c. Measure what nobody wrote down
From the 10-fps strips, measure in frames (1 frame = 0.1 s) and in body heights / known object sizes:
- movement: run speed, sprint/boost speed, acceleration time to top speed, air control, fall speed
- jumps: height, airtime, double jump, coyote time if visible
- the core action: wind-up, active, recovery; cooldowns
- camera: FOV feel, shake on impact, follow distance
- UI: transition durations, popup timings
Convert to Roblox units (1 body height ≈ 5 studs) and mark [MEASURED]. Anything you can't measure or find is
[ESTIMATE] and goes on the build agent's R0 list to measure from the videos itself.

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
9. Videos for the build agent (IDs, titles, lengths, type, the timestamps that matter), so it can study them on the
   user's PC
10. Sources: every wiki/guide/patch page used, with URLs

## 7. Write MECHANICS_BIBLE.md (the contract for an exact copy)
One table per system (movement, core action, progression, economy, levels/runs, enemies/obstacles, UI flow, saves).
Every row: mechanic | exact behavior | number(s) in source units and studs/seconds | source (wiki URL, video ID @
timestamp, patch note) | [WIKI] / [MEASURED] / [ESTIMATE].
Then:
- a SCREEN FLOW: every screen from boot to the end of a run, in order, with what each button does
- a FIRST 10 MINUTES script: second by second, what the original shows and teaches
- an ORIGINAL-EXPRESSION list: every name, character, text and asset we must replace, with our replacement
The build agent copies the bible's numbers into Config and must not change them without a playtest reason logged in
FIDELITY_AUDIT.md.

Also pick 15–30 reference images for `style_refs/` (store screenshots + full-res UI keyframes + 1–2 animation strips).
Name them by what they show (ui_cards.jpg, hud_full.jpg, area_rose_tunnel.jpg, anim_punch_10fps.jpg).
