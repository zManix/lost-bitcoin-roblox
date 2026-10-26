# TODO: {{GAME_NAME}} ({{HOURS}}+ hour build)
Rules:
- Check an item off ([x]) only when its DONE WHEN passes. Visual items also need VISUAL_QA avg ≥ 8.
- Tag owner-only items [HUMAN].
- The stop hook won't let you stop while any untagged "[ ]" remains, or before {{HOURS}} hours.

## Research first
- [ ] R0 Video study: yt-dlp the videos in STUDY.md (720p, private reference). Extract frames every 3–20 s plus
  10-fps strips of key moments, and read the captions. Write VIDEO_STUDY.md (systems, UI flows, timings, best
  moments, complaints). If blocked, note it and continue.
- [ ] R1 STYLE_NOTES.md from every image in style_refs\ + STUDY.md (before any visual work)

## Milestones (customize per game; risk order; each has a DONE WHEN)
- [ ] M0 Setup:
  - lock Studio (marker "{{MARKER}}"), folders, Config, Remotes, DataService (TEST store), BuildLog, live_src mirror,
    PROGRESS.md
  - {{REUSE_LINE}}
- [ ] M1 Blender scale/orientation test + upload script + one templated test mesh (ASSET_LOG.md)
- [ ] M2 THE HARDEST SYSTEM (from TECH_NOTES), with its tests passing on an emulated phone
- [ ] M3 Core action feel (input → animation → feedback → reward); FUN_QA: the core action alone feels good
- [ ] M4 Look pass 1 for the main play area; VISUAL_QA ≥ 8
- [ ] M5 Hub/lobby look pass; VISUAL_QA ≥ 8
- [ ] M6 … (game systems from SPEC, one per line, each with DONE WHEN)
- [ ] M? Social layer (SPEC §2) with 2-client and 8-client tests
- [ ] M? Persistence (exact resume) + session lock
- [ ] M? Leaderboards / events (if any)
- [ ] M? Meta progression, collection, daily, quests, group reward, codes
- [ ] M? Real assets: everything in BLENDER_PIPELINE §H; VISUAL_QA ≥ 8 everywhere
- [ ] M? HUD + every UI screen + all input types; OverlapCheck 0 on 6 devices; touch ≥ 44 px
- [ ] M? Onboarding (SPEC first-60-seconds) + funnel analytics
- [ ] M? BalanceSim: all SPEC targets
- [ ] M? Monetization: passes/products (Open Cloud + IDs in Config), Store UI, receipts, PolicyService, ranked ignores boosts
- [ ] M? Audio: every SFX/ambience in the SPEC juice list (free Creator Store audio)
- [ ] M? Performance: 8–10-client stress: heartbeat ≥ 55, FPS ≥ 40 on Low
- [ ] M? Final QA: every test, exploit fuzz, data kill-test

## Polish passes (all required)
- [ ] P1 A full session on emulated phone as a new player: fix every friction; FUN_QA log
- [ ] P2 An alternate mode/difficulty playthrough
- [ ] P3 A multi-client session: the social layer feels alive, nothing interferes
- [ ] P4 Juice pass on every action; the big moment polished until it gives goosebumps
- [ ] P5 Visual pass: re-score every area vs style_refs, raise anything < 8
- [ ] P6 Thumbnails + icon: 3 variants, auto-checked
- [ ] P7 Gamepad-only first 10 minutes
- [ ] P8 Exploit + data pass (kill the server mid-session, rejoin, progress intact)
- [ ] P9 Text pass: our own short lines, no typos
- [ ] P10 Second balance pass + BalanceSim

## POLISH BACKLOG (pull from here when the lists are empty and time remains)
more content · more cosmetics · hub decoration · accessibility (colorblind-safe, reduced motion) · settings
persistence · achievements/badges · week-1 update content behind a disabled LiveEvent

## Final
- [ ] F1 Re-run every test + OverlapCheck + a final VISUAL_QA sweep; all pass
- [ ] F2 FINAL_REPORT.md (see START_PROMPT), last line "SAVE NOW (Ctrl+S) + PUBLISH"
