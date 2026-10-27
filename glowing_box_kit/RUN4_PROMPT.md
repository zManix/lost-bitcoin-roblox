Run 4: make the hunt FINDABLE and the pace calm. Small run (~3 hours max). No filler.

The owner played 21+ minutes on Normal and never found the box. They say the game is genuinely fun, but:
1. Specials (rubber boots shrine, mushroom shrine) "can't be broken" and they don't know what they're for.
2. Level-ups come every ~5 seconds, so the card screen pops up constantly. They want upgrades to bank up.
3. The search feels random. They dug straight down, kept hitting the cube floor and had no plan. "closer / further"
   alone didn't get them anywhere.

Setup (do this first, yourself):
- Rename FINAL_REPORT.md to FINAL_REPORT_run3.md (or _run2 if no Run 3 report exists).
- Run `node .claude/hooks/keep-working.js --init`.
- Add the "## Run 4" items below to TODO.md as "- [ ]" lines. If any Run 3 item (R3-x) is still open, keep it.
- Re-read FIDELITY_AUDIT.md, spec §7–§8, the last 30 lines of PROGRESS.md. Lock the Studio as before.

## Run 4 items (each needs its DONE WHEN, with proof in PROGRESS.md)
- R4-0 VIDEO STUDY FIRST. Use yt-dlp on this PC (720p max, private reference only) to get these Find The Box videos:
  xHYT7ybiSwY, r28z2gU6tVU, RdlnEbMLS98, aUM3xPa7DS8, HLcefgt8pQk, fMhTnfhv9Sg. Grab frames every 3 s plus the
  auto-captions. Answer these questions in VIDEO_STUDY.md, with timestamps:
  a) the closer/further hint: when does it update (timer or movement)? Is there a "same" state? Any sound?
  b) how do players search? Layer by layer from the top, straight tunnels, or something else? How long do runs take?
  c) how are Specials used? Punch? Walk in? What do they give, and how is that shown?
  d) leveling at high levels: does the card screen open every time? Does it pause, queue or bank?
  e) can you see the cube's edges/floor? Any position or depth readout?
  DONE WHEN: VIDEO_STUDY.md answers a–e. If yt-dlp hits a bot check, write that down and continue. Never work around
  bot checks.
- R4-1 SPECIALS WORK. Each Special has a verb, a prompt and a reward:
  - Shrine: punch the prop. Tooltip pill: "<name> · punch to claim". On claim: the prop lights up, its line types out,
    a pop "+N tokens · free card" appears, then it stays lit (claimed).
  - Geode: breaks with punches. Cache: punch to open.
  - DONE WHEN: in a Studio playtest you claim one of each type, with a screenshot of each pop.
- R4-2 CARD BANK + PACE.
  - Level-ups never open the card screen by themselves. A pulsing pill "cards ×N" sits above the level bar. Open it
    with Tab, tapping the pill, or gamepad Y. After a pick, if more are banked, the next 3 cards rise at once with
    "2 more". Add a "later" button. Remove the 25 s auto-pick.
  - Retune need(L) so mid-run levels come every 30–90 s at a normal build's break rate.
  - DONE WHEN: a 15-min bot run logs the level gaps (median gap after minute 3 is 30–90 s), and the screen never
    opens unasked.
- R4-3 THE HINT YOU CAN USE. Follow VIDEO_STUDY (a) where it differs.
  - Update on MOVEMENT: compare against your last reference point once you've moved ≥ 2 blocks. Show CLOSER (warm
    chime) or FURTHER (low tone). If you haven't moved, keep the last state, dimmed.
  - Teach it once, at the first hint: "dig straight. when it says further, turn."
  - Hard mode stays hint-free.
  - DONE WHEN: a bot that ONLY plays this method finds the box (tunnel along one axis until "further", step back,
    turn 90°, repeat for each axis incl. up/down; it never knows where the box is). Over 10 Normal Standard runs:
    median 8–18 min, none over 30.
- R4-4 KNOW WHERE YOU ARE (our addition; must not reveal the box).
  - A small "depth 34" readout (layers from the top) next to the timer.
  - The cube's outer layer (walls + floor) gets a slightly darker, smoother block, so you can see an edge coming.
  - The first time you reach the floor, one line: "the box is never near the edges."
  - Log it in FIDELITY_AUDIT.md as INVENTED-GOOD with the reason. If VIDEO_STUDY (e) shows the original already
    does this differently, copy the original instead.
  - DONE WHEN: screenshots show the readout and the edge layer. It gives zero box info.
- R4-5 RE-CHECK. Pure must take longer than Normal with upgrades. The box glow must be visible through about 3
  blocks, as you close in. Never stuck: an unstuck button exists. Skip any of these already done in Run 3.
  DONE WHEN: numbers in PROGRESS.md.
- R4-6 Re-run the tests + OverlapCheck, then write FINAL_REPORT.md. Keep it short:
  - what changed
  - 3 things the owner should test
  - the bot numbers
  - last line: "SAVE NOW (Ctrl+S) + PUBLISH"

Rules:
- Only these items. No new features beyond them.
- If you pass 3 hours, finish the current item, move the rest to the POLISH BACKLOG (plain text, no checkbox), write
  the report and stop.
- Never print keys. Never Publish. Ctrl+S after each item.

Start now. Don't ask me anything.
