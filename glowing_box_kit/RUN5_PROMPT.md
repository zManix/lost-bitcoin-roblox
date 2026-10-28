Run 5: MOBILE + DEVICE QA before the owner tests on a real phone. Small run (~3 hours max). No new features.

80% of Roblox players are on phones. Earlier runs had a 5 px Collection text and a cards pill that overlapped on
phones. This run makes every screen work on every device and input, and prepares the owner's real-phone test.

Setup (do this first, yourself):
- Rename FINAL_REPORT.md to FINAL_REPORT_run4.md.
- Run `node .claude/hooks/keep-working.js --init`.
- Add the "## Run 5" items below to TODO.md as "- [ ]" lines.
- Re-read spec §6 (HUD), §13 (controls), §16 (Visual QA), the last 30 lines of PROGRESS.md. Lock the Studio as before.
- Press Ctrl+S and screenshot the tab's save stamp. If it doesn't update, write "SAVE NOT CONFIRMED" at the top of
  PROGRESS.md and in the final report. Keep going.

## Devices (use all of them, landscape)
| Name | Size | Why |
|---|---|---|
| Small phone | 667×375 | the hardest fit (iPhone SE class) |
| Notch phone | 852×393 | safe areas, notch/island |
| Big Android | 915×412 | most common shape |
| Tablet | 1024×768 | 4:3, lots of empty space |
| PC low | 1366×768 | small laptop |
| Console / TV | 1920×1080, 10-foot | gamepad only, text read from a sofa |

Use the Studio Device Emulator if the MCP can switch it; otherwise use the OverlapCheck harness at each size. Lock the
game to landscape (ScreenOrientation LandscapeSensor) unless something already handles portrait properly.

## Run 5 items (each needs its DONE WHEN, with proof in PROGRESS.md)
- R5-1 SCREEN SWEEP. On all 6 devices, screenshot every screen and state:
  - HUD mid-run: hint chip, depth pill, timer, level bar, spell slots, cards ×N pill, tooltip pill
  - the card screen with 3 cards + "N more" + later/reroll/skip/banish
  - Collection (every tab), leaderboard, store, mode panel, settings, the box-found screen, onboarding chips, a
    Special claim pop
  Save them to visual_qa\run5\<device>\. Fix:
  - any overlap, clipping, or anything off-screen
  - any text under 14 px on phones (TextScaled + UITextSizeConstraint min 14)
  - anything under the notch: use ScreenInsets / SafeAreaCompatibility, and respect GuiService.TopbarInset (the
    Roblox top bar)
  - anything under Roblox's own chat (top-left) or the jump button and thumbstick zones
  DONE WHEN: OverlapCheck 0 issues on all 6 devices, and every screenshot is scored in VISUAL_QA.md (avg ≥ 8, none < 7).
- R5-2 TOUCH. Check with real touch input simulation where possible:
  - PUNCH ≥ 96 px, every other button ≥ 44 px, with ≥ 8 px between them
  - you can move (thumbstick) + look (drag) + punch (hold) at the same time
  - a camera drag never fires a punch, a tap on UI never punches through it
  - spell slots, the cards pill and the card screen are all tappable with a thumb
  - a camera sensitivity slider exists in settings (phones need it)
  DONE WHEN: a touch test script logs all checks as PASS.
- R5-3 GAMEPAD + SWITCHING.
  - Gamepad only: every button reachable with selection (GuiService.SelectedObject), a visible selection ring,
    Y opens cards, B closes any menu, no dead ends.
  - Switch input mid-run (touch → keyboard → gamepad): prompts and button icons update (LastInputTypeChanged).
  DONE WHEN: a full gamepad-only path (spawn → dig → open cards → pick → Collection → back → find box) is logged PASS.
- R5-4 PHONE PERFORMANCE. On the emulated small phone with QualityController at Low:
  - a 10-minute bot run at a high break rate (a late-game build, spells + companions on)
  - log FPS, client memory, part count, particle count, and network receive per second
  - targets: FPS ≥ 40 (min ≥ 30), client memory ≤ 1,200 MB, parts ≤ 3,000, network ≤ 50 KB/s
  - fix anything over target (cap debris and particles on Low, pool more, lower the token spray)
  DONE WHEN: the numbers in PROGRESS.md all hit target.
- R5-5 PROMPTS + POLICY on mobile. Every pass/product prompt opens and closes cleanly on a phone layout and the game
  resumes. PolicyService hides paid random items where required. Nothing is reachable that isn't allowed.
  DONE WHEN: logged PASS per product (test purchases in Studio only).
- R5-6 PHONE_TEST.md for the owner, max 1 page, plain words:
  - Step 1: in Studio, File → Publish to Roblox (the experience stays PRIVATE, only the owner can join).
  - Step 2: open Roblox on the phone → Create/your experiences → join.
  - Then a 10-minute checklist with a checkbox per line: punch feel, hint chip readable, depth pill readable, the
    cards pill + card screen, a shrine claim, the store, the box-found screen, rejoin (cube still dug), FPS feel,
    battery/heat after 10 min.
  - Plus "what to send back": screenshots of anything wrong.
  DONE WHEN: the file exists and is under 60 lines.
- R5-7 LAUNCH_CHECKLIST.md: every remaining [HUMAN] item with exact click paths, in order:
  - Studio API access ON (for saves)
  - devices enabled: Phone, Tablet, Computer, Console; VR off
  - the maturity questionnaire
  - badges, thumbnails (3) + icon, pass descriptions, the test leaderboard wipe, Gemini credits
  - go public on a Thu/Fri
  DONE WHEN: the file exists; each item has its click path.
- R5-8 Re-run the tests + OverlapCheck, Ctrl+S, then write FINAL_REPORT.md. Keep it short:
  - what changed
  - the device table with PASS/FAIL
  - the perf numbers
  - whether the save was confirmed
  - last line: "SAVE NOW (Ctrl+S) + PUBLISH (private) → run PHONE_TEST.md"

Rules:
- Only these items. Fix what breaks; no new features, no redesigns.
- If you pass 3 hours, finish the current item, move the rest to the POLISH BACKLOG (plain text, no checkbox), write
  the report and stop.
- Never print keys. Never Publish (the owner does it). Ctrl+S after each item.

Start now. Don't ask me anything.
