# TODO: Find the Glowing Box 10-hour build
Rules: check items off ([x]) only when their DONE WHEN passes. Visual items also need VISUAL_QA avg ≥ 8 (spec §9).
Tag owner-only items [HUMAN]. The stop hook won't let you stop while any untagged "[ ]" line remains, or before 10 hours.

## Milestones
- [ ] M0 Setup: lock Studio (marker "GlowingBoxAgent"), folders, Config, Remotes, copy + adapt the reused modules from ..\ScrapAJunkyard\live_src (DataService TEST store, Monetization, AntiExploit, Social, Leaderboard, LiveEvent, OverlapCheck, QualityController, SmokeTest harness), BuildLog, live_src mirror, PROGRESS.md
- [ ] M1 STYLE_NOTES.md written from every image in style_refs\ (do this before any visual work)
- [ ] M2 Cube engine: buffer grid, chunks, greedy mesher, client renderer + pool, server dig validation, CubeTest + PerfTest pass (FPS ≥ 45 emulated phone, parts ≤ 6,000)
- [ ] M3 Fists viewmodel + punch feel (crack, chips, sound, hit stop, kick); FUN_QA: punching alone feels good
- [ ] M4 Look pass 1: block texture with seams + veins, embedded candle lights, Hall greybox → art, band colors; VISUAL_QA ≥ 8 on hub + B1 tunnel
- [ ] M5 Generation: seeded box + box room, Specials, bands; hints closer/further + special distance; Hard mode
- [ ] M6 Box find sequence + Box Buddy reveal + timer stop + gems
- [ ] M7 Tokens + levels + card pick UI (3 cards, reroll, banish, skip, auto-pick); VISUAL_QA ≥ 8 on cards
- [ ] M8 Spells (12) + hotbar + cooldowns; perks (40); companions (4); movement perks
- [ ] M9 Modes: sizes, Normal/Hard, Upgrades on/off/Pure, Boxless, Daily Cube, seeds; mode panel
- [ ] M10 Persistence: resume a dug cube exactly (RLE bitset), timer pause/resume
- [ ] M11 Leaderboards: every board key + period, Daily board, Hall wall UI; ranked ignores paid boosts
- [ ] M12 Party cubes (up to 4): invite/join, shared digs, per-player cards, party boards
- [ ] M13 Meta: gems, unlocks (card pool, movement, decor), Box Buddy shelf, Index, daily streak, quests, group reward, codes
- [ ] M14 Real assets: Blender (fists, glowing box, 10 shrine props, 30 Box Buddies, 4 companions, Hall props, candles); textures via Gemini + auto-check; VISUAL_QA ≥ 8 everywhere
- [ ] M15 UI: every screen, all input types, OverlapCheck 0 on 6 devices, touch ≥ 44 px (punch ≥ 90 px)
- [ ] M16 Onboarding (spec §16) + funnel analytics
- [ ] M17 BalanceSim: all spec §17 targets
- [ ] M18 Monetization: passes/products in code, ranked-safe flag, Store UI, receipts, PolicyService; create real IDs via Open Cloud
- [ ] M19 Performance: 8-client stress (4 cubes, spells spamming): heartbeat ≥ 55, FPS ≥ 40 on Low
- [ ] M20 Final QA (spec checklist): smoke, CubeTest, PerfTest, OddsTest, OverlapCheck, exploit fuzz

## Polish passes (all required after the milestones)
- [ ] P1 Full Standard run solo, Normal, upgrades ON, on emulated phone: fix every bug/friction; FUN_QA log
- [ ] P2 Pure + Hard run: is it still relaxing and readable without hints?
- [ ] P3 3-client party run: desync, fairness, juice for everyone
- [ ] P4 Juice pass on every action (spec §11); find-the-box moment polished until it gives goosebumps
- [ ] P5 Visual pass: re-score every area vs style_refs, raise anything < 8
- [ ] P6 Thumbnails + icon: 3 variants (giant cube in the candle hall; a tunnel in rose light with fists punching; the glowing box reveal), auto-checked
- [ ] P7 Console gamepad-only first 10 minutes
- [ ] P8 Exploit + data pass (kill server mid-run, rejoin, cube intact)
- [ ] P9 Text pass: short, lowercase cozy lines, no typos, all our own words
- [ ] P10 Second balance pass + re-run BalanceSim

## POLISH BACKLOG (pull from here when the lists are empty and time remains)
more Specials · more Box Buddies · more perks · hall decoration · ambient sound beds per band · candle flicker shader feel ·
leaderboard animations · glove skins art · seed share UI · Daily Cube countdown · accessibility (colorblind-safe bands,
reduced motion) · settings persistence · Humongous size behind a flag · week-1 update content behind a disabled LiveEvent

## Final
- [ ] F1 Re-run every test + OverlapCheck + a final VISUAL_QA sweep; all pass
- [ ] F2 Write FINAL_REPORT.md (built, owner TEST CHECKLIST, [HUMAN] items with steps, known issues, VISUAL_QA + FUN_QA summary, BalanceSim, 8-week update plan, last line "SAVE NOW (Ctrl+S) + PUBLISH")
