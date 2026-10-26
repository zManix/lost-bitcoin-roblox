# TODO: Find the Glowing Box (10+ hour build)
Rules:
- Check an item off ([x]) only when its DONE WHEN passes. Visual items also need VISUAL_QA avg ≥ 8 (spec §16).
- Tag owner-only items [HUMAN].
- The stop hook won't let you stop while any untagged "[ ]" remains, or before 10 hours.

## Research first
- [ ] R0 Video study: download the videos listed in FTB_STUDY.md §7 with yt-dlp (720p max, for private reference
  only), extract frames every 3 s plus 10-fps strips around punches, level-ups, specials and the box find, and read
  their auto-captions. Write VIDEO_STUDY.md: every card/spell/perk/risk name seen (as reference only; we use our own
  names), HUD/menu flows, animation timings, sounds described, what YouTubers react to most (best moments), and what
  they complain about. If yt-dlp is blocked, write that in VIDEO_STUDY.md and continue with FTB_STUDY.md.
- [ ] R1 STYLE_NOTES.md from every image in style_refs\ + FTB_STUDY.md §3–§4 (before any visual work)

## Milestones
- [ ] M0 Setup:
  - lock Studio (marker "GlowingBoxAgent"), folders, Config, Remotes
  - copy + adapt the reused modules from ..\ScrapAJunkyard\live_src (DataService TEST store, Monetization,
    AntiExploit, Social, LiveEvent, OverlapCheck, QualityController, SmokeTest harness)
  - BuildLog, live_src mirror, PROGRESS.md
- [ ] M1 Blender scale/orientation test (BLENDER_PIPELINE A3) + an upload script + one test mesh uploaded and
  templated (ASSET_LOG.md)
- [ ] M2 CUBE ENGINE (TECH_NOTES §1, items 1–4, 7–8, 11):
  - buffer grid, seeded gen, 20³ chunks, greedy box mesher, pool + BulkMoveTo
  - client DDA aim, batched digs, server validation + corrections, anti-noclip
  - CubeTest + PerfTest pass: ≤ 4 ms per chunk on emulated phone, ≤ 3,000 parts, 8 bots at 30 digs/s OK
- [ ] M3 Fists viewmodel (greybox first) + punch feel: alternating jabs, crack, block pop-out debris, tock + combo
  pitch, hit stop, camera kick. FUN_QA: punching alone feels good
- [ ] M4 Block look:
  - band MaterialVariants (4×4 tile with seams + variation), embedded lamps, band color system
  - VISUAL_QA ≥ 8 on B1 and B2 tunnels
- [ ] M5 Hall greybox → art pass 1 (candles, uplights, plinth, pool, stations); VISUAL_QA ≥ 8 on the Hall
- [ ] M6 Generation extras: box + box room, Specials (shrines, geodes, caches, gold veins), hints, Hard mode
- [ ] M7 Box found sequence (spec §8) + Box Buddy reveal + timer + gems + the shared column for others
- [ ] M8 Tokens + levels + LEVEL-UP CARD screen (anatomy, rarity glow, reroll/banish/skip, depth tiers); VISUAL_QA ≥ 8
- [ ] M9 Spells (12) + hotbar/cooldowns/charges; Perks (48); Risks (6); Companions (4); movement perks
- [ ] M10 SHARED SPACE: collision groups, ghost rendering (Highlight + transparency + tags), shared moments, emotes;
  2-client and 8-client tests
- [ ] M11 Party cubes (shared grid for up to 4)
- [ ] M12 Modes: sizes, Normal/Hard, On/Pure, Boxless, Daily, Seeds, Casual flag; mode panel
- [ ] M13 Persistence: resume a dug cube exactly (zstd bitset), timer pause/resume, session lock
- [ ] M14 Leaderboards: ODS naming scheme + MemoryStore live boards, cached refresh, wall + menu UI; ranked ignores boosts
- [ ] M15 LIVE RACE event: hourly schedule, gate + countdown, same seed, race sidebar, winner beam, rewards
- [ ] M16 Meta: gems, unlocks, Collection menu (tabs + filters), Box Buddy shelves + shoulder buddy, daily streak,
  quests, group reward, codes
- [ ] M17 Real assets: every item in BLENDER_PIPELINE §H (meshes + textures), templated, cloned;
  VISUAL_QA ≥ 8 everywhere
- [ ] M18 HUD + all UI screens, all input types, OverlapCheck 0 on 6 devices, touch ≥ 44 px (PUNCH ≥ 96 px)
- [ ] M19 Onboarding (spec §12) + funnel analytics
- [ ] M20 BalanceSim: spec §18 targets
- [ ] M21 Monetization: passes/products (Open Cloud create + IDs in Config), casual-only flags, Store UI, receipts,
  PolicyService
- [ ] M22 Audio: band ambiences, the Hall bed, every SFX in spec §14 (free Creator Store audio)
- [ ] M23 Performance: 10-client stress (ghosts, spells, a race): heartbeat ≥ 55, FPS ≥ 40 on Low
- [ ] M24 Final QA: smoke, CubeTest, PerfTest, OddsTest, OverlapCheck, exploit fuzz, data kill-test

## Polish passes (all required after the milestones)
- [ ] P1 A full Standard run, solo, Normal, upgrades ON, on emulated phone. Fix every friction; FUN_QA log
- [ ] P2 Pure + Hard run: relaxing and readable without hints?
- [ ] P3 A 3-client party run + a 6-client Live Race: ghosts readable, shared moments delightful, not distracting
- [ ] P4 Juice pass on every action; the box-find moment polished until it gives goosebumps
- [ ] P5 Visual pass: re-score every area vs style_refs, raise anything < 8
- [ ] P6 Thumbnails + icon: 3 variants (the giant cube in the candle hall with ghosts; fists punching in a rose
  tunnel with tokens flying; the glowing box reveal), auto-checked
- [ ] P7 Console gamepad-only first 10 minutes
- [ ] P8 Exploit + data pass (kill the server mid-run, rejoin, cube intact)
- [ ] P9 Text pass: our own short lowercase lines, no typos
- [ ] P10 Second balance pass + BalanceSim

## POLISH BACKLOG (pull from here when the lists are empty and time remains)
more Specials · more Box Buddies · more perks/spells · Hall decoration · ghost aura variety · leaderboard animations ·
glove skin art · seed share UI · Daily countdown · accessibility (colorblind-safe bands, reduced motion) ·
achievements/badges · Humongous size behind a flag · week-1 update content behind a disabled LiveEvent

## Final
- [ ] F1 Re-run every test + OverlapCheck + a final VISUAL_QA sweep; all pass
- [ ] F2 FINAL_REPORT.md with:
  - what was built
  - an owner TEST CHECKLIST
  - [HUMAN] items with steps
  - known issues
  - the VISUAL_QA + FUN_QA summary
  - the BalanceSim numbers
  - the 8-week update plan
  - the last line "SAVE NOW (Ctrl+S) + PUBLISH"
