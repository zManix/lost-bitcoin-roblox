// Keeps Claude Code working for RUN_HOURS (default 10).
// Stop hook: blocks stopping until the time target is met AND TODO.md has no open agent tasks AND FINAL_REPORT.md exists.
// Escape hatches: create a file named STOP_NOW in the project folder (you), a hard cap of RUN_HOURS + 4,
// or a real blocker (BLOCKED.md that stays for 4+ stop attempts over 20+ minutes).
// Run with --init (SessionStart) to record the start time once.
const fs = require("fs");
const path = require("path");

const root = process.env.CLAUDE_PROJECT_DIR || process.cwd();
const stateFile = path.join(root, ".claude", "run_state.json");
const TARGET = Number(process.env.RUN_HOURS || 10);
const HARD_CAP = TARGET + 4;

const exists = (f) => fs.existsSync(path.join(root, f));
const read = (f) => { try { return fs.readFileSync(path.join(root, f), "utf8"); } catch { return ""; } };
let state = {};
try { state = JSON.parse(fs.readFileSync(stateFile, "utf8")); } catch {}
const save = () => fs.writeFileSync(stateFile, JSON.stringify(state, null, 2));

if (process.argv.includes("--init")) {
  if (!state.start) { state.start = Date.now(); save(); }
  const hrs = (Date.now() - state.start) / 3600000;
  process.stdout.write(`Long run active: ${hrs.toFixed(2)} h of ${TARGET} h elapsed. Read TODO.md and PROGRESS.md, then continue.`);
  process.exit(0);
}

let raw = "";
process.stdin.on("data", (d) => (raw += d));
process.stdin.on("end", () => {
  const now = Date.now();
  if (!state.start) state.start = now;
  const hrs = (now - state.start) / 3600000;

  const allow = (why) => { state.stoppedBecause = why; state.stoppedAt = now; save(); process.exit(0); };

  if (exists("STOP_NOW")) allow("user STOP_NOW");
  if (hrs >= HARD_CAP) allow("hard cap");

  const open = read("TODO.md").split(/\r?\n/)
    .filter((l) => /^\s*[-*]\s*\[ \]/.test(l) && !/\[HUMAN\]/i.test(l))
    .map((l) => l.replace(/^\s*[-*]\s*\[ \]\s*/, "").trim());
  const finalReport = exists("FINAL_REPORT.md");

  if (hrs >= TARGET && open.length === 0 && finalReport) allow("done");

  if (exists("BLOCKED.md")) {
    state.blockedHits = (state.blockedHits || 0) + 1;
    state.blockedSince = state.blockedSince || now;
    if (state.blockedHits >= 4 && now - state.blockedSince >= 20 * 60000) allow("real blocker: " + read("BLOCKED.md").slice(0, 200));
  } else {
    state.blockedHits = 0;
    state.blockedSince = null;
  }

  state.blocks = (state.blocks || 0) + 1;
  save();

  const left = Math.max(0, TARGET - hrs).toFixed(1);
  let reason = `KEEP WORKING. ${hrs.toFixed(2)} h of ${TARGET} h done, ${left} h left. `;
  if (open.length) {
    reason += `Open TODO items (${open.length}), next: ${open.slice(0, 3).join(" | ")}. `;
  } else if (hrs < TARGET) {
    reason += "TODO.md has no open items but time remains: add at least 10 new tasks from the POLISH BACKLOG in TODO.md (or better ones you find by playtesting), then continue. ";
  } else if (!finalReport) {
    reason += "All tasks done and time is up: write FINAL_REPORT.md now (what to test, what needs a human, SAVE NOW + PUBLISH). ";
  }
  if (exists("BLOCKED.md")) reason += "BLOCKED.md exists: retry the blocker now (re-list studios, re-lock the marker, restart the MCP call). Keep doing any work that does not need it. Delete BLOCKED.md once it works. ";
  reason += "If your context was compacted, re-read TODO.md, PROGRESS.md and the spec first. Do not ask the user anything. Do not end your turn.";

  process.stdout.write(JSON.stringify({ decision: "block", reason }));
  process.exit(0);
});
