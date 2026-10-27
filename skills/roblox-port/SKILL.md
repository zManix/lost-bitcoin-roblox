---
name: roblox-port
description: >-
  Turn any game (Steam link, store page or name) into a researched Roblox game and launch a long, thorough autonomous build
  in Roblox Studio. Studies the source deeply (store data, screenshots, trailers frame by frame, gameplay videos,
  reviews), checks the live Roblox market via Roblox's APIs (rising charts, 40+ clone searches, peaks, like ratios,
  proven pass prices), gives an honest verdict, runs adversarial reviewers and pivots if the idea is dead, then writes
  a full build kit (spec, study, tech notes, Blender pipeline + assets, style refs, TODO, start prompt, a stop hook
  that keeps Claude working for hours), asks once for missing keys and launches it. Use whenever the user wants to
  port, copy, clone, remake or "make a Roblox version of" a game, pastes a game link and mentions Roblox, asks if a
  game would work on Roblox, wants a one-shot/master build prompt for a Roblox game, or types /roblox-port.
---

# roblox-port: game → research → verdict → build kit → thorough autonomous Roblox build

You run the whole pipeline the user would otherwise do over a long conversation:
1. Study the source game.
2. Check the Roblox market.
3. Decide honestly.
4. Get attacked by reviewers and fix.
5. Write a self-contained build kit.
6. Launch a long autonomous build on the user's Windows PC (Claude Code + Roblox Studio MCP + Blender MCP).

**Input:** `$ARGUMENTS` = a Steam URL, a store/itch/website URL, an app id, or a game name. Optional extras the user may
add: a different hour count ("12h"), "research only" (stop after the verdict), "no launch" (write the kit but don't
start it), a concept idea of their own.

## How to work with the user
- Keep messages short and plain. Lead with the answer, then the reason. No jargon without a 3-word explanation.
- Be brutally honest. If the idea is weak on Roblox, say so and say why, with numbers. Never promise a 10/10: say what
  would make it real (shipping fast, weekly updates, juice, thumbnails).
- Ask only for what you can't get yourself: missing keys (once, all together), the Studio prep click, the go/no-go
  before a long build launch. Everything else, decide with sensible defaults and mark guesses as [ESTIMATE] /
  [ASSUMPTION].
- Post a one-line status when a phase finishes, so the user can follow along.

## Ground rules (why they exist)
- **Mechanics, not assets.** Copy systems, layouts and mood. Never names, text, art, logos or story from the source.
  This keeps the user safe from takedowns and moderation.
- **Content safety.** No skulls, blood, gore, robed/hooded figures, religious symbols, weapons aimed at
  people/creatures, text inside images, real brands. Roblox moderation is strict and strikes hit the user's account.
- **No bot-check circumvention.** If YouTube or any site asks to "confirm you're not a bot", stop that source, say so,
  and use other material. Don't try mirrors or tricks.
- **Secrets.** Never print, store in files, or commit API keys.
- **Freshness claims need evidence.** On Roblox, small versions of almost every idea exist. Earlier runs had three
  concepts killed because the clone check was shallow. Do at least 40 searches yourself, and let the reviewer do 40+
  more.
- **Looks and feel are graded.** A past 10-hour build passed 771 tests and was "ugly and boring". That's why every kit
  carries style reference images plus Visual QA and Fun QA loops.

## Workspace
`%USERPROFILE%\Desktop\RobloxPorts\<game-slug>\` with:
- `research\` (raw data, frames, videos)
- the research docs at the root (STUDY.md, MARKET.md, VERDICT.md)
- `kit\` (the build folder that gets launched)

On non-Windows or when unsure, use `~/RobloxPorts/<slug>/`. Slug = the game's name in lowercase, with hyphens
and no symbols (e.g. "find-the-box").

Run commands from the workspace and call scripts by absolute path: `python "<skill-dir>/scripts/<name>.py" ...` (on
Linux/macOS use `python3`). In the playbooks, `scripts/x.py` means that absolute path.

**Subagents:** Phases 1, 4 and 6 spawn subagents (Agent/Task tool) for independent research and review. If no subagent
tool is available, do the work yourself, and run the review as a separate hostile pass labeled "self-review (not
independent)" (verdict_and_review.md §3).

---

## Phase 0: Preflight (≈2 min)
1. `python scripts/check_env.py`. Install anything MISSING with the printed command (winget/pip), rerun.
2. Make sure the Roblox Studio and Blender MCPs are user-scope (references/launch_windows.md "MCP gotcha"). Fix it if
   not.
3. Create the workspace. Note today's date (you'll stamp research with it).
4. Keys: don't ask yet unless the user only wants a build. Ask in Phase 5, together with the Studio prep, so the
   user is interrupted once.

## Phase 1: Study the source game (deep; the longest phase)
Follow **references/research_playbook.md** exactly. In short:
1. `scripts/steam_fetch.py "<input>" --out research/steam` (store data, screenshots, trailers, store clips, review
   pages).
2. `scripts/frames.py` to turn every screenshot and trailer into sheets you READ. Then full-res keyframes of every UI
   screen + HUD, and 10-fps strips of the core action, the level-up/reward and the big moment.
3. `scripts/yt_study.py search` + `get` for 3–6 gameplay videos (frames + captions). Bot check = skip.
4. Reviews (WebFetch the review pages) and web/press/devlog search.
5. In parallel, spawn ONE general-purpose subagent for comparable games (sales, loves/hates, why they sold).
6. Write **STUDY.md** (template in the playbook) and choose **15–30 style_refs**.

Status line: "Studied <game>: <N> trailers, <N> frames read, <N> videos. The core loop is …".

## Phase 2: Roblox market check
Follow **references/market_playbook.md**:
1. `scripts/roblox_market.py charts`: what's rising (note event-week skew).
2. 40+ searches in 6 families (`search ... --enrich --json research/market_search.json`). Family 6
   (shelter/base nouns + trending character names) catches what the others miss.
3. `details`, `votes`, `passes` on close matches and lane leaders; RoWatcher pages for peaks/trends.
4. Write **MARKET.md**.

Use **references/roblox_platform_facts.md** for the ranking signals, audience, proven patterns, failure patterns,
prices and policy. If it's more than about 60 days old, refresh the items marked ⟳ quickly.

## Phase 3: Concept + verdict
Follow **references/verdict_and_review.md** §1–2 and §4–5:
- Choose: straight port, port + Roblox layer (most common), or pivot onto a rising formula.
- Design the Roblox layer on purpose. Examples that worked in planning:
  - a solo game → a shared space where everyone digs their own private world in the same spot and sees the others
    as ghosts, plus shared big moments and an hourly live race
  - parties that share one world
  - cosmetics others can see
- Score it with the rubric (show the table). Name it (5 options, pick one).
- Write **VERDICT.md**.

## Phase 4: Adversarial review (always)
Spawn a fresh reviewer subagent with the brief in verdict_and_review.md §3. **Verify its top claims yourself** with
`roblox_market.py details`. If the concept is already shipped and dead, or a clearly better lane exists, pivot and run
one more review round. Apply surviving fixes. Update VERDICT.md "Review rounds".

## Phase 5: Checkpoint with the user (one message)
**Research-only runs:** show only the verdict block (pitch, score table, total, risks, name, Roblox layer), list the
files written, and stop. No keys, no Studio prep.

Show:
- the verdict (pitch, score table, honest total, the top 3 risks)
- the name
- what the Roblox layer is

Then ask in ONE message:
1. "Go / change something?"
2. Only the MISSING keys (from check_env.py), with where to get each (references/launch_windows.md "Keys").
3. The Studio prep: "File → New → Baseplate, then File → Publish to Roblox → '<NAME>', Private. Tell me when done."

When they answer:
- store the keys with `setx` (never echo them)
- verify the keys (Gemini model list; one read-only Open Cloud call)
- confirm the place via the Studio MCP
- write KEY_CHECK.md (OK/FAIL only)

## Phase 6: Write the build kit
Follow **references/kit_writing.md**. Create `kit\` with:
- SPEC.md (full template; numbers and our own names everywhere; the Visual QA + Fun QA blocks)
- STUDY.md, VERDICT.md (copies)
- TECH_NOTES.md (design the hardest system first; spawn a research subagent for anything uncertain)
- BLENDER_PIPELINE.md (copy references/blender_pipeline.md and fill §H with this game's asset list)
- TODO.md (from assets/kit/TODO.template.md, customized; R0 lists the video IDs)
- START_PROMPT.md (from assets/kit/START_PROMPT.md; fill {{GAME_NAME}}, {{HOURS}}, {{MARKER}} (e.g.
  "<GameName>Agent"), {{GEMINI_MODEL_NOTE}} (e.g. "gemini-3.1-flash-image was confirmed available"), {{REUSE_LINE}}
  (paths of earlier builds' live_src modules to copy, or "none found: build fresh"))
- style_refs\ (copy the chosen images)
- `.claude\` (copy assets/kit/.claude as-is: settings.json + hooks/keep-working.js)

Then validate:
- all files exist
- `echo {} | node .claude/hooks/keep-working.js` prints `"decision":"block"`; then delete `.claude/run_state.json`
- re-read SPEC.md as the build agent would and fix any vague spot

If the user said "no launch", stop here and tell them how to launch later (the launch command below).

## Phase 7: Launch
`powershell -ExecutionPolicy Bypass -File scripts/launch.ps1 -KitDir "<ws>\kit" -MaxHours <H>` (default cap 8). The hook keeps the build going until every TODO item is
truly done (thoroughness), stops on its own after 3 idle attempts, and never asks for filler work.

Then tell the user exactly what to click in the new window, how to watch it, and how to stop it
(references/launch_windows.md "Launch"). Keep this message under 10 lines.

## Phase 8: When the user comes back after the run
Read FINAL_REPORT.md, VISUAL_QA.md and FUN_QA.md. Give an honest summary:
- what's good and what's weak
- the top 5 things to test on a real phone
- the [HUMAN] steps
- the pre-launch list (Studio API access + save/rejoin test, maturity questionnaire, 3 thumbnails, Thu/Fri launch,
  Saturday updates)

If they say it's ugly or boring: diagnose with them (ugly = fixable with refs and assets; boring = a core-loop
problem), and offer a targeted follow-up run with a narrower TODO.

---

## Reference files (read when you reach that phase)
| File | Use in |
|---|---|
| references/research_playbook.md | Phase 1: every step and the STUDY.md template |
| references/market_playbook.md | Phase 2: search families, reading the numbers, MARKET.md |
| references/verdict_and_review.md | Phases 3–4: concept choice, rubric, reviewer brief, naming, VERDICT.md |
| references/roblox_platform_facts.md | Phases 2–6: ranking, audience, patterns, prices, policy, tech limits (dated) |
| references/kit_writing.md | Phase 6: kit layout, SPEC template, QA blocks, tech patterns, validation |
| references/blender_pipeline.md | Phase 6: copy into the kit; fill §H |
| references/launch_windows.md | Phases 0, 5, 7, 8: preflight, keys, Studio prep, launch, troubleshooting |
| assets/kit/ | START_PROMPT.md, TODO.template.md, .claude/ stop hook + settings |
| references/examples/ | a gold-standard SPEC + TECH_NOTES (Find the Glowing Box) and an honest VERDICT (Dome Keeper) |

## Scripts (tested)
| Script | Does |
|---|---|
| scripts/check_env.py | tool/MCP/key preflight (never prints secrets) |
| scripts/steam_fetch.py | store data, screenshots, trailers (ffmpeg), store clips, review page list |
| scripts/frames.py | sheets / key / strip / images: turn video and images into frames Claude can read |
| scripts/yt_study.py | YouTube search + download + captions + frame sheets (stops on bot checks) |
| scripts/roblox_market.py | search / details / votes / passes / charts from Roblox's public APIs |
| scripts/launch.ps1 | starts the long build in a new window inside the kit folder, keys loaded, sleep off |

## Time and cost
Phases 1–6 take roughly 30–90 minutes and spawn 2–4 subagents. The build itself runs for the chosen hours and needs a
plan that allows long sessions (Max tier or API billing). Say this once in Phase 5 so the user isn't surprised.
