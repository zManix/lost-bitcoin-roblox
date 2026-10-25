You are building the Roblox game SCRAP A JUNKYARD, completely, in one long autonomous run of AT LEAST 10 HOURS.
Roblox Studio is open with a new empty Baseplate place. The full game spec is in this folder:
SCRAP_A_JUNKYARD_ONE_SHOT_PROMPT.md. Read it fully first. It is your source of truth for design, rules (section B),
build order (section D) and the hand-off checklist (section E). Where this message differs from the spec, this message wins.

## How this run works (read carefully)
- A Stop hook (.claude/hooks/keep-working.js) will NOT let you end your turn until 10 hours have passed AND TODO.md has
  no open "[ ]" items (except lines tagged [HUMAN]) AND FINAL_REPORT.md exists. Don't fight it. Never end a turn to
  "check in", summarize, or ask a question. The owner is asleep. Just keep working.
- Work state lives in files, not in your memory (your context will be auto-compacted many times):
  - TODO.md: the checklist. Mark [x] only when that item's DONE WHEN test has passed. Add new tasks whenever you find
    bugs or polish ideas. Tag owner-only items with [HUMAN] (login, payment, CAPTCHA, publishing, anything that needs
    their account in a browser).
  - PROGRESS.md: append a timestamped line after every meaningful step (what you did, the result, what's next). After any
    compaction or restart, re-read TODO.md, PROGRESS.md, the spec's section B, and the last 30 lines of PROGRESS.md
    before continuing.
  - MORNING_REPORT.md, ServerStorage BuildLog, live_src\ mirror: as the spec says.
- Check the clock with PowerShell `Get-Date` or `node -e "console.log(new Date())"`. The hook also tells you the
  elapsed time every time you try to stop.
- When the milestones are done before 10 hours, you are NOT done. Do the P1–P10 polish passes. Then pull from the
  POLISH BACKLOG. Then playtest again and add every bug and friction point you find as a new task. The goal is a game
  polished to a professional standard, not a demo. Use every hour.

## Keys and tools (never print, log or commit secrets)
- Gemini image generation: API key in the environment variable GEMINI_API_KEY. Write a small node script
  tools\gen_image.js that calls https://generativelanguage.googleapis.com. First list the models (GET /v1beta/models) and
  use the newest image-capable model that supports generateContent. Save PNGs to art\. Prompts are POSITIVE-ONLY:
  describe exactly what you want to see, never list things to avoid.
- Roblox Open Cloud: API key in ROBLOX_API_KEY, creator in ROBLOX_USER_ID (or ROBLOX_GROUP_ID). Use it to upload FBX
  meshes and approved images (Assets API) and, if the place is published and the key has the scopes, to create the game
  passes and developer products from spec C18 (check the current Open Cloud docs for the exact endpoints). Put the
  returned IDs in Config.Monetization. If something isn't possible with the key, write the exact manual steps as a
  [HUMAN] item and move on.
- Roblox Studio MCP: pass studio_id on every call. Lock onto this place with the marker workspace:SetAttribute(
  "ScrapAJunkyardAgent", true) and probe it before every batch. Never touch any other Studio.
- Blender MCP for every 3D model. Export FBX, upload with Open Cloud, insert real MeshParts. Never use runtime
  EditableMesh.

## Image safety mode: AUTO-CHECK (overrides spec rule B2 for this run)
For every generated 2D image: (1) save it to pending_review\ with its prompt; (2) run a second Gemini call that looks at
the image and answers strictly: does it contain any text or letters, logos, skulls, blood, weapons, robed or hooded
figures, religious symbols, or anything scary? (3) Upload only images that pass, and log each one (file, prompt,
check result, asset id) in IMAGE_LOG.md. Regenerate failures with a better positive prompt (max 3 tries, then a [HUMAN]
item). The owner will review IMAGE_LOG.md at the end.

## Saving and crash safety (10 hours is long)
- Build the world from code where possible (builder scripts in live_src\) so the place can be rebuilt with execute_luau
  if Studio crashes.
- Every 30 minutes and after every milestone, save the place with Ctrl+S using input simulation, focused on the Studio
  window. Take a screenshot to confirm it saved. NEVER press Publish (Alt+P) and never publish to live.
- If Studio or an MCP stops responding: retry 3 times over 10 minutes (re-list studios, re-lock the marker). Meanwhile,
  keep doing offline work: Blender models, images, Luau code in live_src\, BalanceSim math, docs. Only if it's still
  dead after that, write BLOCKED.md (what failed, what you tried, what the owner must do). Then keep retrying every few
  minutes while doing offline work. Delete BLOCKED.md as soon as it works again.

## Order of work
1. Read the spec. Create PROGRESS.md. Run `node .claude/hooks/keep-working.js --init`. Lock the Studio.
2. Work TODO.md top to bottom (M0 → M18, then P1–P10, then the backlog). After every step: smoke test → playtest →
   screenshot → fix (spec rule B3).
3. Monetization, all of it: every pass and product in code, Store UI, receipt ledger, PolicyService gating, and the
   real IDs via Open Cloud if possible.
4. Test everything on every device size (spec B5/B6): 0 UI overlaps, touch targets ≥ 44 px.
5. At the very end (10+ hours, nothing left you can do alone): run F1, then write FINAL_REPORT.md containing:
   - what was built (systems, content counts, assets uploaded)
   - a numbered TEST CHECKLIST for the owner (exact steps: what to click and what should happen), covering every system,
     every pass/product, mobile, console, a party of friends, data save/rejoin
   - every [HUMAN] item with exact steps
   - known issues and ideas
   - BalanceSim numbers
   - the 8-week Saturday update plan
   - the final line: "SAVE NOW (Ctrl+S) + PUBLISH"
   Only then may you stop.

Start now. Don't ask me anything. Keep going until the hook lets you stop.
