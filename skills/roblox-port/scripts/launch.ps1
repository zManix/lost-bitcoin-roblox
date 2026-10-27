# Launches the long autonomous build in a NEW window, inside the kit folder (so the project Stop hook loads).
# Usage: powershell -ExecutionPolicy Bypass -File launch.ps1 -KitDir "C:\Users\me\Desktop\RobloxPorts\my-game\kit" [-MaxHours 8]
param(
  [Parameter(Mandatory = $true)][string]$KitDir,
  [int]$MaxHours = 8
)
$ErrorActionPreference = "Stop"
if (-not (Test-Path (Join-Path $KitDir "START_PROMPT.md"))) { throw "START_PROMPT.md not found in $KitDir" }
if (-not (Test-Path (Join-Path $KitDir ".claude\hooks\keep-working.js"))) { throw "Stop hook missing in $KitDir\.claude\hooks" }

# Keys set with setx live in the User registry; this process may predate them, so load them explicitly.
foreach ($k in @("GEMINI_API_KEY", "ROBLOX_API_KEY", "ROBLOX_USER_ID", "ROBLOX_GROUP_ID")) {
  $v = [Environment]::GetEnvironmentVariable($k, "User")
  if ($v) { Set-Item -Path "Env:$k" -Value $v }
}
# The kit's settings.json sets MIN_HOURS/MAX_HOURS; this overrides MAX_HOURS for this run. Do NOT raise
# CLAUDE_CODE_STOP_HOOK_BLOCK_CAP: the default (8 idle blocks) prevents endless loops that burn usage.
$env:MAX_HOURS = "$MaxHours"

# Fresh clock for the hook.
$state = Join-Path $KitDir ".claude\run_state.json"
if (Test-Path $state) { Remove-Item $state -Force }

# Keep the PC awake while plugged in.
powercfg /change standby-timeout-ac 0 | Out-Null

$prompt = "Read START_PROMPT.md in this folder and follow it exactly, starting now."
Start-Process cmd -WorkingDirectory $KitDir -ArgumentList '/k', "claude --dangerously-skip-permissions `"$prompt`""
Write-Output "Launched in a new window: $KitDir (cap $MaxHours h). In that window answer YES to 'trust this folder' and pick 'Yes, I accept' on the bypass warning."
