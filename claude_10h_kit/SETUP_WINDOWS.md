# 10-hour build: setup (about 5 minutes, Windows cmd)

## 1. Get the files
```
cd %USERPROFILE%\Desktop
git clone -b claude/lost-bitcoin-roblox-port-eye41g https://github.com/zmanix/lost-bitcoin-roblox.git
mkdir ScrapAJunkyard
xcopy /E /I /H lost-bitcoin-roblox\claude_10h_kit ScrapAJunkyard
copy lost-bitcoin-roblox\SCRAP_A_JUNKYARD_ONE_SHOT_PROMPT.md ScrapAJunkyard\
```

## 2. Keys (type your real keys; never paste them into the chat or the prompt)
```
setx GEMINI_API_KEY "your-gemini-key"
setx ROBLOX_API_KEY "your-open-cloud-key"
setx ROBLOX_USER_ID "your-roblox-user-id"
```
Close cmd and open a new one, so the keys load.
For the Open Cloud key (create.roblox.com → Open Cloud → API Keys), give it:
- Assets read + write
- Game passes + developer products write (if offered)
- Access to your experience

## 3. Studio + PC prep
- In Studio, with the empty Baseplate: **File → Publish to Roblox → new experience "Scrap a Junkyard", keep it PRIVATE.**
  It needs to exist so game passes can be created and Ctrl+S can save it. It stays private, so nobody can play it.
- Make sure the Roblox Studio MCP is connected, and Blender is open with its MCP add-on running.
- Stop the PC from sleeping (a sleeping PC kills the run):
  ```
  powercfg /change standby-timeout-ac 0
  powercfg /change monitor-timeout-ac 0
  ```
  Keep it plugged in.

## 4. Launch
```
cd %USERPROFILE%\Desktop\ScrapAJunkyard
set CLAUDE_CODE_STOP_HOOK_BLOCK_CAP=1000
claude --dangerously-skip-permissions
```
Paste the whole of `START_PROMPT.md` and press Enter. Walk away.

## Controls
- **Stop it early:** create an empty file named `STOP_NOW` in the ScrapAJunkyard folder. It stops at its next stop
  attempt. Or press Esc in the terminal.
- **Check progress:** open `PROGRESS.md` and `TODO.md`.
- **It ends by itself** when 10 h have passed, TODO.md has nothing left that it can do alone, and FINAL_REPORT.md is
  written. Hard cap: 14 h.

## Be aware
- `--dangerously-skip-permissions` lets Claude run any command without asking. That's needed for 10 unattended hours.
  Only run it in this folder, and don't keep other important stuff open.
- **Usage limits:** 10 hours non-stop uses a LOT. On Pro you'll hit the limit; Max (20x) or API billing is the realistic
  option. If a limit hits, Claude Code pauses. Type `continue` after the reset; the hook and TODO.md pick it back up.
- Images are auto-checked by a second Gemini pass before upload, and logged in `IMAGE_LOG.md`. Review it in the morning.
