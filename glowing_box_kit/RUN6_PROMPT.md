Run 6: real-phone fixes from the owner's first phone test. Small run (~1 hour max). Only these 3 fixes.

The owner played on a real phone (landscape, about 2000×923 px screenshot). Problems:
1. The level bar + spell slots float in the MIDDLE of the screen (their top is at about 57% of the height). They must
   sit at the bottom.
2. The top-right menu button (≡) overlaps the FLARE readiness pill under it.
3. You CAN'T LOOK AROUND WHILE HOLDING PUNCH. On a phone the right thumb does both, so this makes the game almost
   unplayable.

Setup: rename FINAL_REPORT.md to FINAL_REPORT_run5.md, run `node .claude/hooks/keep-working.js --init`, add the
"## Run 6" items below to TODO.md as "- [ ]" lines, lock the Studio as before.

## Run 6 items (each needs its DONE WHEN, with proof in PROGRESS.md)
- R6-1 PUNCH = DRAG TO LOOK (mobile-shooter style).
  - A touch that STARTS on PUNCH starts punching. While that same finger stays down: keep punching, and its drag
    turns the camera (yaw + pitch, pitch clamped, the same look-sensitivity setting as normal touch look). Lifting the
    finger anywhere stops punching.
  - How: track that touch's InputObject (UserInputService InputBegan/InputChanged/InputEnded, Touch type, started
    inside PUNCH's bounds) and apply its Delta to the camera. If the game uses the default camera, rotate it in a
    BindToRenderStep after Enum.RenderPriority.Camera and prove the rotation sticks (doesn't snap back). If the game
    has its own camera, feed the delta into it.
  - Keep: a second finger dragging elsewhere still looks; the thumbstick still moves; a drag that starts on empty
    screen still never punches; UI taps never punch through.
  - DONE WHEN: a touch test holds PUNCH and drags right 300 px: the camera turns (log the yaw change), blocks break the
    whole time, and the camera stays turned after release. The thumbstick + PUNCH-drag work at the same time.
- R6-2 HOTBAR AT THE BOTTOM (phones + tablets).
  - Spell slots: AnchorPoint (0.5, 1), bottom = bottom safe-area inset + 10 px, centered.
  - The level bar sits directly above the slots (6 px gap).
  - On the screenshot's shape (2000×923 → test at 868×400 and 667×375) the slots must not overlap the thumbstick zone
    (left ~30%), PUNCH or jump. If they would, shrink the slots (min 44 px) before moving them up.
  - The crosshair stays clear (the Run 5 fix still holds).
  - DONE WHEN: screenshots on the 3 phone sizes + tablet show the slots at the bottom edge, and OverlapCheck = 0.
- R6-3 TOP-RIGHT GAP. Keep the menu button where it is and move the FLARE readiness pill so it's ≥ 8 px below it (or
  beside it if there's room). Nothing may touch Roblox's top bar.
  DONE WHEN: screenshots on all 6 devices show the gap, and OverlapCheck = 0.
- R6-4 Re-run the tests + TouchTest + OverlapCheck, Ctrl+S, then write FINAL_REPORT.md (max 20 lines): what changed,
  before/after phone screenshots, "the owner re-tests on the phone: hold PUNCH and drag to look", last line
  "SAVE NOW (Ctrl+S) + PUBLISH (private) → re-test on the phone".

Rules: only these items, no other changes. Never print keys. Never Publish. Ctrl+S after each item.

Start now. Don't ask me anything.
