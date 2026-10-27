You are building the Roblox game FIND THE GLOWING BOX (first person), completely, thoroughly, in one long autonomous run
(safety cap 8 hours). Roblox Studio has a new place open (published privately as "Find the Glowing Box"). Everything you
need is in this folder. Read these in order before doing anything else:

1. FIND_THE_GLOWING_BOX_SPEC.md: the design (source of truth)
2. FTB_STUDY.md: a deep study of the original game (why it works, the UI, the look, the animations)
3. TECH_NOTES.md: the cube engine, the shared space with ghosts, networking, saves, leaderboards
4. BLENDER_PIPELINE.md: Blender → Roblox rules, upload steps, the FULL asset list
5. style_refs\: 28 reference images (open every one)
6. TODO.md: your checklist (start with R0)

## The lesson from the last build (read this twice)
The last 10-hour build passed 771 tests and the owner called it "ugly and boring". Tests are not the goal:
- LOOKS: spec §16 Visual QA. Screenshot after every visual change, score it against style_refs, and fix anything
  below 8/10 before moving on (VISUAL_QA.md).
- FEEL: spec §17 Fun QA. Play 3 real minutes at every milestone and fix the dullest moments (FUN_QA.md).
- REUSE: the backend modules from %USERPROFILE%\Desktop\ScrapAJunkyard\live_src (spec §15 / TODO M0), so your
  hours go into the cube engine, the look and the feel.

## How this run works
- A Stop hook (.claude/hooks/keep-working.js) won't let you end your turn while TODO.md has open "[ ]" items (except
  [HUMAN]) or FINAL_REPORT.md is missing. The point is THOROUGHNESS, not hours: do every item properly, with its DONE WHEN
  proven (evidence in PROGRESS.md), instead of stopping early and sloppy. Never invent filler work to fill time. Safety
  cap: 8 hours. If you are only waiting for the owner, say so once and stop (the hook allows it after 3 idle tries).
  Never end a turn just to check in or ask a question: the owner is away.
- State lives in files:
  - TODO.md: mark [x] only when DONE WHEN passes; add every bug and polish idea you find.
  - PROGRESS.md: a timestamped line after every step.
  - VISUAL_QA.md, FUN_QA.md, ASSET_LOG.md, IMAGE_LOG.md, MORNING_REPORT.md.
  - The ServerStorage BuildLog and the live_src\ mirror of every script.
- After any context compaction or restart: re-read TODO.md, the last 30 lines of PROGRESS.md, spec §16–§17,
  STYLE_NOTES.md and TECH_NOTES.md §1 before continuing.
- Finishing the milestones isn't "done": do the polish passes and fix everything they find. Backlog items are
  optional: do them only if they clearly improve the game. Finishing early with quality is a success.

## Keys and tools (never print, log or commit secrets)
- Gemini images: env var GEMINI_API_KEY → tools\gen_image.js against generativelanguage.googleapis.com, using the
  newest image model (gemini-3.1-flash-image was confirmed available). Positive-only prompts.
- Roblox Open Cloud: ROBLOX_API_KEY + ROBLOX_USER_ID. Upload meshes and images (BLENDER_PIPELINE §E). Create the game
  passes and developer products from spec §15 and put their IDs in Config.
- Studio MCP: studio_id on every call; lock with workspace:SetAttribute("GlowingBoxAgent", true) and probe it before
  every batch; never touch other Studios.
- Blender MCP: every 3D model (BLENDER_PIPELINE). Use its `look` tool to check models visually. Never use runtime
  EditableMesh.
- Videos (R0): use yt-dlp on this PC (pip install yt-dlp if missing) to study the videos listed in FTB_STUDY.md §7,
  for private reference only. Never upload or reuse their footage, art or text.
- Images: AUTO-CHECK mode. Save to pending_review\, run a second Gemini check (text/letters, logos, skulls, blood,
  weapons, robed/hooded figures, religious symbols, anything scary), upload only passes, and log everything in
  IMAGE_LOG.md.

## Saving and crash safety
- Ctrl+S via input simulation every 30 minutes and after every milestone; confirm with a screenshot. Never Publish.
- Keep builders in live_src\ so the place can be rebuilt with execute_luau after a crash.
- If Studio or an MCP dies: retry 3 times over 10 minutes and do offline work in the meantime (Blender, images, Luau,
  BalanceSim, docs). Write BLOCKED.md only if it's still dead; keep retrying; delete BLOCKED.md when it works.

## Order
1. `node .claude/hooks/keep-working.js --init`, create PROGRESS.md, lock the Studio.
2. TODO.md top to bottom: R0 → R1 → M0 … M24 → P1–P10 → backlog. M2 (the cube engine) is the biggest risk: prove it
   with CubeTest + PerfTest before building on it.
3. At the end (every TODO item done, nothing left you can do alone): F1, then FINAL_REPORT.md (see TODO F2), whose last line
   is "SAVE NOW (Ctrl+S) + PUBLISH".

Start now. Don't ask me anything. Keep going until the hook lets you stop.
