<#
set-secret-and-dispatch.ps1

Prompts for a PAT, saves it as AUTOMATION_PAT in the repo kalvinparker/profile-template,
dispatches the workflow sync-readmes.yml on the chosen branch/ref, then shows the latest run.

Usage:
  pwsh .\set-secret-and-dispatch.ps1
#>

# Configuration - adjust if you need different values
$Owner = 'kalvinparker'
$Repo = 'profile-template'
$RepoSpec = "$Owner/$Repo"               # repository to set secret and dispatch workflow in
$WorkflowFile = 'sync-readmes.yml'       # workflow filename (in .github/workflows/)
$Ref = 'clean/readme-sync'               # branch/ref that contains the workflow (adjust if needed)
$ShowLogs = $true                        # set to $false to skip printing logs

function AbortWith($msg) {
    Write-Host $msg -ForegroundColor Red
    exit 1
}

# Check gh availability
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    AbortWith "gh CLI not found. Install from https://cli.github.com/ and authenticate (gh auth login) before running this script."
}

# Check gh auth status
$authOut = gh auth status --hostname github.com 2>&1
if ($LASTEXITCODE -ne 0 -or $authOut -match "You are not logged into any GitHub hosts") {
    Write-Host $authOut
    Write-Host ""
    Write-Host "gh is not authenticated. Run: gh auth login"
    AbortWith "Authenticate gh and re-run this script."
}

Write-Host "gh is installed and authenticated."

# Prompt for the PAT (secure)
$securePAT = Read-Host -Prompt "Paste the PAT to store as AUTOMATION_PAT (it will only be used in this session)" -AsSecureString
if (-not $securePAT) { AbortWith "No PAT provided; aborting." }

# Convert SecureString to plain string in-memory (temporary)
$ptr = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($securePAT)
$plainPAT = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($ptr)

# Set secret using gh
Write-Host "Setting secret AUTOMATION_PAT in repository $RepoSpec ..."
$ghSetResult = gh secret set AUTOMATION_PAT --repo $RepoSpec --body $plainPAT 2>&1
$ghExit = $LASTEXITCODE

# Clear sensitive variables ASAP
Remove-Variable ptr, securePAT -ErrorAction SilentlyContinue
# Note: plainPAT exists until we remove it; we'll remove it below after the call
if ($ghExit -ne 0) {
    Write-Host $ghSetResult
    Remove-Variable plainPAT -ErrorAction SilentlyContinue
    AbortWith "Failed to set repository secret AUTOMATION_PAT. Ensure you have permission to create secrets in $RepoSpec."
}

Write-Host "Secret set successfully."

# Dispatch the workflow
Write-Host "Dispatching workflow '$WorkflowFile' on ref '$Ref' ..."
$dispatchOut = gh workflow run $WorkflowFile --repo $RepoSpec --ref $Ref 2>&1
$dispatchExit = $LASTEXITCODE

if ($dispatchExit -ne 0) {
    Write-Host $dispatchOut
    Remove-Variable plainPAT -ErrorAction SilentlyContinue
    AbortWith "Workflow dispatch failed. Check that the workflow file exists on ref $Ref and that the token scopes are correct."
}

Write-Host "Workflow dispatch requested. Listing recent runs..."

# Give GitHub a few seconds to register the run
Start-Sleep -Seconds 4

# Show the most recent run for this workflow
# Get latest run as JSON
$json = gh run list --workflow $WorkflowFile --repo $RepoSpec --limit 5 --json databaseId,status,conclusion,createdAt 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host $json
    Remove-Variable plainPAT -ErrorAction SilentlyContinue
    AbortWith "Failed to list workflow runs."
}

# Parse
$runs = $json | ConvertFrom-Json
if (-not $runs -or $runs.Count -eq 0) {
    Remove-Variable plainPAT -ErrorAction SilentlyContinue
    AbortWith "No workflow runs found for $WorkflowFile in $RepoSpec."
}

$latest = $runs[0]
Write-Host "Latest run:"
Write-Host ("  id: {0}`n  status: {1}`n  conclusion: {2}`n  createdAt: {3}" -f $latest.databaseId, $latest.status, $latest.conclusion, $latest.createdAt)

if ($ShowLogs) {
    Write-Host "Fetching logs for run id $($latest.databaseId) ..."
    # Stream logs to console
    gh run view $latest.databaseId --repo $RepoSpec --log
}

# Clean sensitive variable
Remove-Variable plainPAT -ErrorAction SilentlyContinue

Write-Host "Done. If the workflow step that creates PRs uses the stored AUTOMATION_PAT it should run in the workflow and open a PR (check Actions run logs for the create-pull-request step)."
Write-Host "To see open PRs (in this repo): gh pr list --repo $RepoSpec --state open --limit 20"
Write-Host "If the workflow creates a PR in another repo (e.g. 'kalvinparker/kalvinparker'), run:" 
Write-Host "  gh pr list --repo kalvinparker/kalvinparker --state open --limit 20"
