// keep-working.js v2 — "don't quit early or sloppy", NOT "burn hours".
//
// Claude may stop when ANY of these is true:
//   1. DONE: TODO.md has no open "- [ ]" lines (except ones tagged [HUMAN]) AND FINAL_REPORT.md exists
//      AND at least MIN_HOURS have passed (default 0.5; stops "2 hours and sloppy" via strict TODO DONE WHENs, not via a clock).
//   2. The owner asks: a file named STOP_NOW or PAUSE exists in the project folder.
//   3. Safety cap: MAX_HOURS passed (default 8).
//   4. Stalled: 3 blocked stops in a row with no change to PROGRESS.md / TODO.md (it's idling or waiting for a human),
//      so it never loops forever burning usage.
//   5. Real blocker: BLOCKED.md exists for 3+ stop attempts over 15+ minutes.
// Otherwise it blocks the stop and tells Claude the next open TODO item. It NEVER asks Claude to invent filler work.
// Run with --init (SessionStart) to record the start time once.
const fs = require("fs");
const path = require("path");

const root = process.env.CLAUDE_PROJECT_DIR || process.cwd();
const stateFile = path.join(root, ".claude", "run_state.json");
const MIN_HOURS = Number(process.env.MIN_HOURS || 0.5);
const MAX_HOURS = Number(process.env.MAX_HOURS || process.env.RUN_HOURS || 8);

const p = (f) => path.join(root, f);
const exists = (f) => fs.existsSync(p(f));
const read = (f) => { try { return fs.readFileSync(p(f), "utf8"); } catch { return ""; } };
const mtime = (f) => { try { return fs.statSync(p(f)).mtimeMs; } catch { return 0; } };
let state = {};
try { state = JSON.parse(fs.readFileSync(stateFile, "utf8")); } catch {}
const save = () => { try { fs.writeFileSync(stateFile, JSON.stringify(state, null, 2)); } catch {} };

if (process.argv.includes("--init")) {
  if (!state.start) { state.start = Date.now(); save(); }
  const hrs = (Date.now() - state.start) / 3600000;
  process.stdout.write(`Build session: ${hrs.toFixed(2)} h elapsed (cap ${MAX_HOURS} h). You may stop only when every TODO.md item is truly done (its DONE WHEN passes) and FINAL_REPORT.md is written. Read TODO.md and PROGRESS.md, then continue.`);
  process.exit(0);
}

let raw = "";
process.stdin.on("data", (d) => (raw += d));
process.stdin.on("end", () => {
  const now = Date.now();
  if (!state.start) state.start = now;
  const hrs = (now - state.start) / 3600000;
  const allow = (why) => { state.stoppedBecause = why; state.stoppedAt = now; state.blocksInRow = 0; save(); process.exit(0); };

  if (exists("STOP_NOW") || exists("PAUSE")) allow("owner asked (STOP_NOW/PAUSE)");
  if (hrs >= MAX_HOURS) allow(`safety cap ${MAX_HOURS} h`);

  const open = read("TODO.md").split(/\r?\n/)
    .filter((l) => /^\s*[-*]\s*\[ \]/.test(l) && !/\[HUMAN\]/i.test(l))
    .map((l) => l.replace(/^\s*[-*]\s*\[ \]\s*/, "").trim());
  const report = exists("FINAL_REPORT.md");
  if (open.length === 0 && report && hrs >= MIN_HOURS) allow("done");

  // Stall detection: no progress since the last blocked stop -> don't loop.
  const progressStamp = Math.max(mtime("PROGRESS.md"), mtime("TODO.md"));
  if (state.lastStamp === progressStamp) state.blocksInRow = (state.blocksInRow || 0) + 1;
  else state.blocksInRow = 1;
  state.lastStamp = progressStamp;
  if (state.blocksInRow >= 3) allow("stalled: no progress across 3 stop attempts");

  if (exists("BLOCKED.md")) {
    state.blockedHits = (state.blockedHits || 0) + 1;
    state.blockedSince = state.blockedSince || now;
    if (state.blockedHits >= 3 && now - state.blockedSince >= 15 * 60000) allow("real blocker: " + read("BLOCKED.md").slice(0, 200));
  } else { state.blockedHits = 0; state.blockedSince = null; }
  save();

  let reason = `Not done yet (${hrs.toFixed(1)} h in, cap ${MAX_HOURS} h). `;
  if (open.length) reason += `${open.length} open TODO item(s). Next: ${open.slice(0, 2).join(" | ")}. Finish it properly (its DONE WHEN must pass, with evidence in PROGRESS.md), then continue. `;
  else if (!report) reason += "All TODO items are checked: run the final checks and write FINAL_REPORT.md, then you may stop. ";
  else reason += `Everything is done; you can stop after ${MIN_HOURS} h total. `;
  if (exists("BLOCKED.md")) reason += "BLOCKED.md exists: retry the blocker; keep doing work that doesn't need it. ";
  reason += "Don't invent filler work. Update PROGRESS.md as you go. If you are only waiting for the owner, say so once and stop.";
  process.stdout.write(JSON.stringify({ decision: "block", reason }));
  process.exit(0);
});
