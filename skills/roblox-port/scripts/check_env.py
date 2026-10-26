#!/usr/bin/env python3
"""Preflight check for the roblox-port pipeline. Prints OK/MISSING per item and the fix. Never prints secret values.

Usage: python check_env.py
Checks: python, git, node, ffmpeg, ffprobe, yt-dlp, claude CLI, MCP servers (Roblox Studio + Blender),
and the keys GEMINI_API_KEY, ROBLOX_API_KEY, ROBLOX_USER_ID (process env OR Windows user env in the registry).
Exit code 0 always; read the table.
"""
import os, platform, shutil, subprocess, sys

KEYS = ["GEMINI_API_KEY", "ROBLOX_API_KEY", "ROBLOX_USER_ID"]
FIX = {
    "git": "winget install Git.Git",
    "node": "winget install OpenJS.NodeJS.LTS",
    "ffmpeg": "winget install Gyan.FFmpeg",
    "ffprobe": "comes with ffmpeg (winget install Gyan.FFmpeg)",
    "yt-dlp": "pip install -U yt-dlp",
    "claude": "npm install -g @anthropic-ai/claude-code (or the native installer)",
}


def user_env(name):
    v = os.environ.get(name)
    if v:
        return v
    if platform.system() == "Windows":
        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as k:
                return winreg.QueryValueEx(k, name)[0]
        except OSError:
            return None
    return None


def main():
    rows = [("python", sys.version.split()[0], "")]
    for tool in ["git", "node", "ffmpeg", "ffprobe", "yt-dlp", "claude"]:
        p = shutil.which(tool)
        rows.append((tool, "OK" if p else "MISSING", "" if p else FIX[tool]))
    mcp = ""
    if shutil.which("claude"):
        try:
            mcp = subprocess.run(["claude", "mcp", "list"], capture_output=True, text=True, timeout=90).stdout.lower()
        except Exception:  # noqa: BLE001
            mcp = ""
    rows.append(("MCP: Roblox Studio", "OK" if "roblox" in mcp else "CHECK", "" if "roblox" in mcp else
                 "Studio → enable the built-in MCP server; then: claude mcp add Roblox_Studio -- cmd.exe /c %LOCALAPPDATA%\\Roblox\\mcp.bat"))
    rows.append(("MCP: Blender", "OK" if "blender" in mcp else "CHECK", "" if "blender" in mcp else
                 "claude mcp add blender -s user -- uvx mcp-for-blender  (and enable the add-on inside Blender)"))
    for k in KEYS:
        v = user_env(k)
        rows.append((k, "SET" if v else "MISSING", "" if v else f'setx {k} "<value>"  (then reopen the shell)'))
    w = max(len(r[0]) for r in rows)
    for name, status, fix in rows:
        print(f"{name:<{w}}  {status:<8} {fix}")


if __name__ == "__main__":
    main()
