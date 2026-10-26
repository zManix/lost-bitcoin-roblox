You are building the Roblox game FIND THE GLOWING BOX, completely, in one long autonomous run of AT LEAST 10 HOURS.
Roblox Studio is open with a new place (published privately). Everything you need is in this folder:
- FIND_THE_GLOWING_BOX_SPEC.md: the design, the source of truth.
- style_refs\: reference images for the LOOK. Study every one before any visual work.
- TODO.md: your checklist.
Read the spec fully first.

## The lesson from the last build (read this twice)
The last 10-hour build passed 771 tests and the owner called it "ugly and boring". Tests are not the goal.
LOOKS and FUN come first:
- Spec §9 VISUAL QA: screenshot after every visual change, score it against style_refs, and fix anything below 8/10
  before moving on. Log the scores in VISUAL_QA.md.
- Spec §10 FUN QA: play 3 real minutes at every milestone and fix the dullest moments. Log in FUN_QA.md.
- Don't rebuild what already works. Reuse the backend modules from %USERPROFILE%\Desktop\ScrapAJunkyard\live_src
  (spec §15), so your hours go into the cube engine, the look and the feel.

## How this run works
- A Stop hook (.claude/hooks/keep-working.js) will NOT let you end your turn until 10 hours have passed AND TODO.md has
  no open "[ ]" items (except lines tagged [HUMAN]) AND FINAL_REPORT.md exists. Never end a turn to check in,
  summarize, or ask a question. The owner is asleep.
- State lives in files: TODO.md (mark [x] only when DONE WHEN passes; add every bug and polish idea you find),
  PROGRESS.md (a timestamped line after every step), VISUAL_QA.md, FUN_QA.md, MORNING_REPORT.md, the ServerStorage
  BuildLog, and the live_src\ mirror of every script. After any context compaction or restart, re-read TODO.md, the
  last 30 lines of PROGRESS.md, spec §9–§10 and STYLE_NOTES.md before continuing.
- If the milestones are done before 10 hours, you are NOT done: polish passes, then the backlog, then playtest again
  and add everything you find. Use every hour.

## Keys and tools (never print, log or commit secrets)
- Gemini (images): env var GEMINI_API_KEY. Write tools\gen_image.js against generativelanguage.googleapis.com and use
  the newest image model (gemini-3.1-flash-image was confirmed available). Positive-only prompts.
- Roblox Open Cloud: env vars ROBLOX_API_KEY + ROBLOX_USER_ID. Upload meshes and images (Assets API). Create the game
  passes and developer products from spec §14 (the key can create them) and put the IDs in Config.
- Studio MCP: studio_id on every call; lock with workspace:SetAttribute("GlowingBoxAgent", true) and probe before
  every batch; never touch other Studios.
- Blender MCP for every 3D model → FBX → Open Cloud → real MeshParts. Never use runtime EditableMesh. The cube itself
  is plain Parts from the greedy mesher.
- Images: AUTO-CHECK mode. Save to pending_review\, run a second Gemini check (text/letters, logos, skulls, blood,
  weapons, robed/hooded figures, religious symbols, anything scary), upload only passes, and log everything in
  IMAGE_LOG.md.

## Saving and crash safety
- Ctrl+S via input simulation every 30 minutes and after every milestone; confirm with a screenshot. Never Publish.
- Keep builders in live_src\ so the place can be rebuilt with execute_luau after a Studio crash.
- If Studio or an MCP dies: retry 3 times over 10 minutes and do offline work in the meantime (Blender, images, Luau in
  live_src, BalanceSim, docs). Write BLOCKED.md only if it's still dead, keep retrying, and delete BLOCKED.md when it
  works again.

## Order
1. `node .claude/hooks/keep-working.js --init`, create PROGRESS.md, lock the Studio.
2. TODO.md top to bottom. M2 (the cube engine) is the biggest risk: prove it with CubeTest + PerfTest before building
   on it.
3. At the very end (10+ hours, nothing left you can do alone): F1, then FINAL_REPORT.md with:
   - what was built
   - a numbered TEST CHECKLIST for the owner (what to click and what should happen; phone, controller, party,
     rejoin, every pass)
   - [HUMAN] items with exact steps
   - known issues
   - the VISUAL_QA and FUN_QA summary
   - the BalanceSim numbers
   - the 8-week update plan
   - the last line "SAVE NOW (Ctrl+S) + PUBLISH"

Start now. Don't ask me anything. Keep going until the hook lets you stop.
