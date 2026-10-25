# TODO: Scrap a Junkyard 10-hour build
Rules: check items off ([x]) only when their DONE WHEN test passes. Tag anything that truly needs the owner with [HUMAN]
(login, payment, CAPTCHA, image approval if queue mode, publishing). The stop hook reads this file:
you cannot stop while any untagged "[ ]" line remains or before 10 hours.

## Build milestones (spec: SCRAP_A_JUNKYARD_ONE_SHOT_PROMPT.md, section D)
- [ ] M0 Setup: Studio lock, folders, Config, Remotes, DataService (TEST store), BuildLog, live_src mirror, SmokeTest, OddsTest
- [ ] M1 Greybox Z1 loop: hub, START A RUN, 3 towers, grab/throw, furnace, coins, Appraiser + Carry Strength (first upgrade < 30 s)
- [ ] M2 Stack collapse: StackGraph, support highlight, tweened topple, zone progress, StackTest
- [ ] M3 Tools: backpack pack/tip-out, vacuum tank + blow, magnet cluster shot, winch, weight gates, hover card
- [ ] M4 Vehicles: wagon, pickup, dump truck, bed stacking, DUMP at furnace
- [ ] M5 Boss: Junk Golem Z1 (plates, telegraphed attacks, core, victory, gate)
- [ ] M6 Gems, classes, 5-min global restock, permanent upgrades + vehicles
- [ ] M7 Night + raccoon bandits + Peaceful mode
- [ ] M8 Mystery Sticks + Reader roll, capsules, fire hatch, Scrapkins, Index
- [ ] M9 Zones 2–5, run save/resume, run complete, Run Level
- [ ] M10 Parties: invite/join run (max 4), friend boost, boss scaling, party slot saves
- [ ] M11 Real assets: Blender models uploaded, all greybox replaced
- [ ] M12 UI: every screen, all input types, OverlapCheck 0 on 6 devices, touch targets ≥ 44 px
- [ ] M13 Onboarding funnel (first 60 s targets)
- [ ] M14 BalanceSim: all pacing targets hit, Config tuned
- [ ] M15 Monetization: passes + products in code, receipt ledger, PolicyService gating, Store UI
- [ ] M15b Create the real game passes + developer products via Open Cloud (if the place is published and the key has the scopes), put IDs in Config; otherwise move this to [HUMAN] with exact steps
- [ ] M16 Retention + live ops: daily, quests, gem drip, codes, group reward, leaderboards, LiveEventService, Golden Junk Rain
- [ ] M17 Performance: 12-client stress test within budgets
- [ ] M18 Final QA: full hand-off checklist (spec section E)

## Polish passes (do all, after the milestones)
- [ ] P1 Full playthrough solo Z1→Z5 on emulated phone; fix every bug and friction point found
- [ ] P2 Full playthrough as a 3-client party; fix desync and UX issues
- [ ] P3 Juice pass: every action has sound + particles + feedback; furnace, collapse and hatch feel great
- [ ] P4 Console pass: gamepad-only playthrough of the first 15 minutes
- [ ] P5 Exploit pass: spam, bad args, far grabs, fake furnace drops, speed checks
- [ ] P6 Data pass: kill the server mid-run, rejoin, verify nothing is lost
- [ ] P7 Performance pass on the Low preset with a full night and a boss
- [ ] P8 Thumbnails/icon: 3 variants generated and checked
- [ ] P9 Text pass: every string short, clear and kid-readable; no typos
- [ ] P10 Second balance pass after playtests; re-run BalanceSim

## POLISH BACKLOG (pull from here when the list above is empty and time remains)
- more tower shapes and junk variety per zone · better golem attack telegraphs · more Scrapkin idle animations ·
  hub decoration and lighting · leaderboard visuals · tutorial clarity tweaks · accessibility (colorblind-safe rarity
  labels, reduced-motion) · sound mix levels · loading screen · settings persistence · more quests · codes system test ·
  error-proof every remote · retest OverlapCheck after every UI change · retest DataStore edge cases ·
  write week-1 and week-2 update content (Zone 6 "Toy Mountain") behind a disabled LiveEvent flag

## Final (last steps, in this order)
- [ ] F1 Re-run SmokeTest, OddsTest, StackTest, OverlapCheck; all pass
- [ ] F2 Write FINAL_REPORT.md (what was built, test checklist for the owner, everything tagged [HUMAN], known issues, 8-week update plan, the line "SAVE NOW (Ctrl+S) + PUBLISH")
