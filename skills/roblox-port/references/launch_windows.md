# Phase 0 + 7 playbook: preflight, keys, Studio prep, launch, troubleshooting (Windows, Claude Code)

## Preflight (Phase 0)
1. `python <skill>/scripts/check_env.py`. Fix anything MISSING with the listed command (winget/pip), then rerun.
   Tools: git, node (the stop hook runs on node), ffmpeg/ffprobe (frames), yt-dlp (video study), claude CLI, Roblox
   Studio MCP, Blender MCP.
2. MCP gotcha: an MCP added with the default scope only exists in the folder it was added in. The build runs in a NEW
   folder, so the Roblox Studio and Blender MCPs must be user-scope. Check with `claude mcp list` FROM the kit folder.
   To move one: `claude mcp get <name>` → `claude mcp add-json <name> '<json>' -s user`.
3. Workspace: `%USERPROFILE%\Desktop\RobloxPorts\<game-slug>\` with `research\` (raw) and `kit\` (the build folder).

## Keys (ask ONCE, only for what's missing)
- Needed:
  - GEMINI_API_KEY (images; aistudio.google.com/apikey; normal keys start with "AIza")
  - ROBLOX_API_KEY: create.roblox.com/dashboard/credentials → Create API Key. Permissions: Assets read+write, game
    passes + developer products write (if listed), add the experience. Accepted IP addresses: 0.0.0.0/0 or it fails
    from home PCs.
  - ROBLOX_USER_ID: the number in roblox.com/users/<ID>/profile. Use ROBLOX_GROUP_ID instead if the game is owned by
    a group.
- check_env.py shows which are SET (process env or the Windows user registry). Ask the user only for the MISSING ones,
  in ONE message, with where to get each. If they paste them in chat, that's their choice; never echo them back.
- Store them with `setx NAME "value"` (user scope, persists). Values set with setx aren't visible to already-running
  processes; scripts/launch.ps1 loads them from the registry.
- Never write keys into any file, log, prompt or commit.
- Verify (no secrets printed):
  - Gemini: GET https://generativelanguage.googleapis.com/v1beta/models?key=… → list the image-capable models and note
    the newest.
  - Roblox: any read-only Open Cloud call with x-api-key (e.g. universe info for the place) → OK/FAIL.
  - Write KEY_CHECK.md with OK/FAIL only.

## Studio prep (the user must click; ask and wait)
"In Roblox Studio: File → New → Baseplate. Then File → Publish to Roblox → new experience '<NAME>', keep it PRIVATE.
Close other places. Tell me when done."
- Publishing privately is safe (only the owner can join) and is required to create game passes and to save with
  Ctrl+S.
- Then confirm with the Studio MCP (list studios) that the place is open; note the place/universe id in KEY_CHECK.md.

## Launch (Phase 7)
`powershell -ExecutionPolicy Bypass -File <skill>/scripts/launch.ps1 -KitDir "<ws>\kit" -Hours 10`
- Opens a new cmd window in the kit folder running `claude --dangerously-skip-permissions` with "Read START_PROMPT.md
  …". It loads the keys from the registry, sets CLAUDE_CODE_STOP_HOOK_BLOCK_CAP=1000, and disables sleep on AC.
- Tell the user, in plain words:
  1. In the NEW window: "trust this folder?" → Yes. The bypass warning → arrow keys to "Yes, I accept" (the default
     is No).
  2. Watch the first 10 minutes: it should read the files and start R0. If it writes BLOCKED.md, paste it back here.
  3. Stop early: create an empty file named STOP_NOW in the kit folder (or press Esc in that window).
  4. Progress: PROGRESS.md, TODO.md, VISUAL_QA.md, FUN_QA.md in the kit folder.
  5. Usage limits: a 10-hour run needs Max-tier or API billing; if it pauses on a limit, type "continue" after the
     reset.

## Why things failed before (don't repeat)
- Claude was started in the home folder: no spec, no hook, no keys → it (correctly) refused. Always launch IN the kit
  folder.
- The trust prompt silently blocked the new window: always tell the user to switch to it and accept.
- Keys set after the session started weren't visible: load them from the registry (launch.ps1 does).
- The run looked fine on tests but was "ugly and boring": the Visual QA + Fun QA loops and style_refs exist because
  of this.

## After the run (when the user comes back)
- Read FINAL_REPORT.md, VISUAL_QA.md and FUN_QA.md. Give the user an honest summary: what's good, what's weak, the
  top 5 things to test on a real phone, the [HUMAN] steps (Studio API access, badges, group id, thumbnails, the
  maturity questionnaire, publish).
- Before going public: real-phone test, save/rejoin test with Studio API access ON, the maturity questionnaire,
  thumbnails (3 variants), then launch on a Thu/Fri and update every Saturday.
