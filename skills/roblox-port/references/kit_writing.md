# Phase 6 playbook: write the build kit (everything the 10-hour agent needs, self-contained)

The build agent has NEVER seen this conversation. Every file must stand alone, with concrete numbers, names, layouts
and "DONE WHEN" tests. Vague specs produce generic, ugly games.

## Kit folder layout (<ws>/kit/)
```
kit/
├── START_PROMPT.md        (from assets/kit/START_PROMPT.md; fill the {{placeholders}})
├── SPEC.md                (the master game spec, template below)
├── STUDY.md               (from Phase 1)
├── VERDICT.md             (from Phase 3–4, so the agent knows what to protect)
├── TECH_NOTES.md          (engine/networking/saves/leaderboards for THIS game)
├── BLENDER_PIPELINE.md    (copy references/blender_pipeline.md + §H asset list for THIS game)
├── TODO.md                (from assets/kit/TODO.template.md, customized milestones)
├── style_refs/            (15–30 images from Phase 1)
└── .claude/ settings.json + hooks/keep-working.js   (copy assets/kit/.claude as-is)
```

## SPEC.md template (fill every section; numbers everywhere; our own names and text)
0. **Why this game + what to protect:** the evidence, our edge, the lesson that LOOK + FEEL are graded first.
1. **Pitch:** 2–3 sentences a kid understands.
2. **The Roblox layer:** how friends/other players fit, without breaking the source's core feel. Examples:
   - shared space with ghosts for a solo game
   - co-op parties
   - live events/races
   - show-off cosmetics others can see

   State what is shared and what is private, and why nothing interferes.
3. **Core loop:** seconds / minutes / session / week.
4. **Modes:** a table.
5. **Look:**
   - camera
   - viewmodel/character style (OUR design, matching the mood)
   - materials and textures
   - area/biome palette table with hexes
   - lighting values (LightingStyle, bloom, color correction)
   - VFX
   - UI style (panel colors, fonts, accents)
6. **HUD:** exact placement of every element on PC and mobile.
7. **Progression systems:** cards/skills/upgrades with FULL lists (names, categories, effect per level, cooldowns,
   costs, odds), currencies and curves ([ESTIMATE] where guessed; BalanceSim tunes).
8. **Content:** specials/secrets/bosses/events with our own names and lines.
9. **Meta progression:** permanent currency, unlocks, collection, daily, quests.
10. **Leaderboards / social.**
11. **Hub & flow:** spawn → first action in 2 taps.
12. **Onboarding:** first 60 s, second by second.
13. **Controls:** PC / mobile / console.
14. **Juice checklist:** every action's sound + particles + motion + timing.
15. **Monetization table:** proven prices from MARKET.md; ranked modes ignore boosts; no paid random items; cosmetics
    others can see.
16. **VISUAL QA loop** (copy the block below).
17. **FUN QA loop** (copy the block below).
18. **Balance targets** (BalanceSim proves them).
19. **Safety:** no skulls, blood, gore, robed/hooded figures, religious symbols, weapons aimed at people/creatures,
    text in images, real brands.
20. Pointers to TECH_NOTES.md and BLENDER_PIPELINE.md.

### VISUAL QA block (paste into SPEC §16)
- Before any visual work: study every image in style_refs\ and STUDY.md §3–§4; write STYLE_NOTES.md in your own words.
- After every visual change: screen_capture the same view types as the refs and save them to visual_qa\<step>\.
  Score each 1–10 vs the refs on: palette, light mood, materials/textures, characters/viewmodel, UI/HUD, glow + juice.
  Log in VISUAL_QA.md.
- DONE only at an average ≥ 8 AND when it would look good as a Roblox thumbnail. Below 8: list what's off, fix it,
  re-shoot. Never mark visual work done on "it works".
- The refs are for mood and layout only: never upload, trace or copy their pixels, names or text.

### FUN QA block (paste into SPEC §17)
At every milestone, play 3 real minutes (input simulation). Log in FUN_QA.md:
- Feedback on EVERY core action (visual + audio)? (must be yes)
- Seconds to the first action / reward / level / choice (state targets).
- A new choice or surprise at least every 60 s in the first 10 minutes? (must be yes)
- The 3 best and 3 dullest moments; fix the dullest before moving on.
- With 2+ clients: does the social layer feel alive without distracting?

## TECH_NOTES.md
Design the hardest system FIRST and write it as a numbered architecture with tests (the build proves it in an early
milestone). Use references/roblox_platform_facts.md "Tech facts". For anything uncertain, spawn a research subagent
(docs + DevForum + GitHub) before writing. Always include:
- server authority
- remotes + rate limits
- data saves (session lock, TEST store in Studio)
- persistence format
- leaderboard key design (if any)
- performance budgets
- anti-exploit checks
- the test list with numeric pass bars

Known patterns:
- **Voxel/destructible worlds:** server `buffer` grid + client-only greedy-BOX-merged anchored Parts in 20³ chunks
  (an untouched 100³ cube ≈ 125 parts), client DDA aim, batched digs, server validation, anti-noclip against the
  per-player grid, a zstd bitset save, MaterialVariant textures with baked seams (StudsPerTile = tile size).
- **Shared space, private worlds:** same world position; CollisionGroups (Players don't collide with each other,
  Ghosts collide with nothing); other characters shown with LocalTransparencyModifier + one Highlight each; big
  moments re-broadcast over UnreliableRemoteEvent; client-only geometry; `CharacterAutoLoads = false` until the
  client has built its spawn surface.
- **Plots/tycoons:** server-owned plot state, pooled props, offline earnings capped.

## REUSE
Look for earlier builds on this PC (e.g. `%USERPROFILE%\Desktop\*\live_src\` containing DataService, Monetization,
AntiExploit, OverlapCheck, QualityController, SmokeTest). If found, the kit's M0 says "copy and adapt these modules"
with their paths, so the 10 hours go to the game itself.

## TODO.md
Start from assets/kit/TODO.template.md. Customize:
- R0/R1 (video study list + style notes)
- M-milestones in risk order: the hardest tech first, proven with tests, then the core feel, then the look, then
  systems, then the social layer, then meta, then assets, then UI, then onboarding, then balance, then monetization,
  then audio, then performance, then QA
- P polish passes, the backlog, F1/F2

Each milestone gets a "DONE WHEN". The stop hook reads lines starting with "- [ ]" (multi-line items are fine; only
the first line needs the checkbox).

## style_refs
15–30 images, named by content. Include: the hero scene, each area/biome, every UI screen, the HUD, 1–2 animation
strips. Total < 10 MB.

## Validate the kit before launch
- Every file in the layout exists.
- `echo {} | node .claude/hooks/keep-working.js` prints `"decision":"block"`; then delete `.claude/run_state.json`.
- Read SPEC.md once as if you were the build agent: any section that says "TBD", "etc." or "similar" gets fixed.
