You are building the Roblox game {{GAME_NAME}} completely, in one long autonomous run of AT LEAST {{HOURS}} HOURS.
Roblox Studio has a new place open (published privately as "{{GAME_NAME}}"). Everything you need is in this folder.
Read these in order before doing anything else:

1. SPEC.md: the design (source of truth)
2. STUDY.md: a deep study of the original game (why it works, its UI, look, animations, videos to watch)
3. VERDICT.md: why this concept, what to protect, what the reviews found
4. TECH_NOTES.md: the architecture for the hardest systems, limits, tests
5. BLENDER_PIPELINE.md: Blender → Roblox rules, upload steps, the FULL asset list
6. style_refs\: reference images (open every one)
7. TODO.md: your checklist (start with R0)

## Lessons from earlier builds (read this twice)
A previous 10-hour build passed 771 tests and the owner called it "ugly and boring". Tests are not the goal:
- LOOKS: SPEC Visual QA. Screenshot after every visual change, score it against style_refs, and fix anything below
  8/10 before moving on (VISUAL_QA.md).
- FEEL: SPEC Fun QA. Play 3 real minutes at every milestone and fix the dullest moments (FUN_QA.md).
- REUSE: {{REUSE_LINE}}

## How this run works
- A Stop hook (.claude/hooks/keep-working.js) will NOT let you end your turn until {{HOURS}} hours have passed AND
  TODO.md has no open "[ ]" items (except lines tagged [HUMAN]) AND FINAL_REPORT.md exists. Never end a turn to check
  in, summarize or ask a question. The owner is asleep.
- State lives in files:
  - TODO.md: mark [x] only when DONE WHEN passes; add every bug and polish idea you find.
  - PROGRESS.md: a timestamped line after every step.
  - VISUAL_QA.md, FUN_QA.md, ASSET_LOG.md, IMAGE_LOG.md, MORNING_REPORT.md.
  - The ServerStorage BuildLog and the live_src\ mirror of every script.
- After any context compaction or restart: re-read TODO.md, the last 30 lines of PROGRESS.md, the SPEC QA sections,
  STYLE_NOTES.md and TECH_NOTES.md before continuing.
- If the milestones are done early, you are NOT done: polish passes, then the backlog, then playtest again and add
  everything you find. Use every hour.

## Keys and tools (never print, log or commit secrets)
- Gemini images: env var GEMINI_API_KEY → write tools\gen_image.js against generativelanguage.googleapis.com, using
  the newest image-capable model (list the models first; {{GEMINI_MODEL_NOTE}}). Positive-only prompts: describe
  exactly what you want to see; never list things to avoid.
- Roblox Open Cloud: ROBLOX_API_KEY + ROBLOX_USER_ID (or ROBLOX_GROUP_ID). Upload meshes and images
  (BLENDER_PIPELINE §E). Create the game passes and developer products from SPEC's monetization table and put their
  IDs in Config. If the key can't, write exact manual steps as a [HUMAN] item.
- Roblox Studio MCP: studio_id on every call. Lock with workspace:SetAttribute("{{MARKER}}", true) and probe it before
  every batch; never touch other Studios.
- Blender MCP: every 3D model (BLENDER_PIPELINE). Use its `look` tool to check models visually. Never use runtime
  EditableMesh for core geometry.
- Videos (R0): use yt-dlp on this PC (pip install -U yt-dlp) to study the videos listed in STUDY.md, for private
  reference only. If YouTube shows a bot check, don't work around it; note it and continue. Never upload or reuse
  their footage, art or text.
- Images: AUTO-CHECK mode. Save to pending_review\, run a second Gemini check (any text/letters, logos, skulls,
  blood, weapons, robed/hooded figures, religious symbols, anything scary), upload only passes, and log everything in
  IMAGE_LOG.md.

## Hard rules
- No skulls, blood, gore, robed/hooded figures, religious symbols, weapons aimed at people/creatures, text inside
  images, real brands. Never copy the original game's names, text, art or logo.
- Data: DataStore with session locking + retries; in Studio ALWAYS the TEST store; never touch live data.
- Server authority for currency, items, progress, purchases; remotes type-checked and rate-limited.
- UI: OverlapCheck 0 on Phone 20:9, Phone 16:9, Tablet, Console, PC 1080p, PC 768p; touch targets ≥ 44 px.
- Performance: smooth on 2 GB Android phones (TECH_NOTES budgets); an adaptive QualityController.
- Mirror every script to live_src\. Keep the BuildLog + PROGRESS.md.
- Never Publish. Save with Ctrl+S via input simulation every 30 minutes and after every milestone (confirm with a
  screenshot).
- If Studio or an MCP dies: retry 3 times over 10 minutes and do offline work in the meantime. Write BLOCKED.md only if
  it's still dead; keep retrying; delete BLOCKED.md when it works again.

## Order
1. `node .claude/hooks/keep-working.js --init`, create PROGRESS.md, lock the Studio.
2. TODO.md top to bottom. The early tech milestone (the hardest system) must pass its tests before you build on it.
3. At the very end ({{HOURS}}+ hours, nothing left you can do alone): run every test + a final VISUAL_QA sweep, then
   FINAL_REPORT.md containing:
   - what was built
   - a numbered owner TEST CHECKLIST (phone, controller, friends/party, save + rejoin, every pass)
   - [HUMAN] items with exact steps
   - known issues
   - the VISUAL_QA + FUN_QA summary
   - the BalanceSim numbers
   - an 8-week Saturday update plan
   - the last line "SAVE NOW (Ctrl+S) + PUBLISH"

Start now. Don't ask me anything. Keep going until the hook lets you stop.
