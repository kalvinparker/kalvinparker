<#
. SYNOPSIS
    Add or update the AUTOMATION_PAT repository secret for the kalvinparker repo.

. DESCRIPTION
    This helper attempts to set the secret using the GitHub CLI (`gh`). If `gh` is not
    available it prints clear manual instructions for adding the secret via the GitHub
    web UI or using the REST API.

    Note: This script does NOT store or transmit the token anywhere except to the
    GitHub CLI (which will send it to GitHub). Always create tokens with least privilege.

. EXAMPLES
    # Prompt for the token securely and set secret using gh
    .\add_automation_pat.ps1

    # Provide token on the command line (be careful with shell history)
    .\add_automation_pat.ps1 -Token 'ghp_xxx'
#>
param(
    [Parameter(Mandatory=$false)]
    [string]$Token
)

function Prompt-ForToken {
    $sec = Read-Host -AsSecureString "public_repo"
    $ptr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($sec)
    try { [Runtime.InteropServices.Marshal]::PtrToStringAuto($ptr) } finally { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($ptr) }
}

if (-not $Token) {
    $Token = Prompt-ForToken
}

Write-Host "Setting AUTOMATION_PAT for repository 'kalvinparker/kalvinparker'..." -ForegroundColor Cyan

# Check for gh CLI
$gh = Get-Command gh -ErrorAction SilentlyContinue
if ($gh) {
    # gh exists - check auth status
    try {
        gh auth status --hostname github.com > $null 2>&1
        Write-Host "gh is installed and authenticated. Creating/updating secret via gh..." -ForegroundColor Green
        # gh will prompt if not authenticated. Use --repo to target the repo explicitly.
        gh secret set AUTOMATION_PAT --repo kalvinparker/kalvinparker --body "$Token"
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Secret AUTOMATION_PAT set successfully." -ForegroundColor Green
        } else {
            Write-Host "gh secret command exited with code $LASTEXITCODE. If gh is not authenticated, run 'gh auth login' and re-run this script." -ForegroundColor Yellow
        }
        return
    } catch {
        Write-Host "gh exists but failed to set secret: $_" -ForegroundColor Yellow
        # fall through to manual instructions
    }
} else {
    Write-Host "gh CLI not found on PATH." -ForegroundColor Yellow
}

Write-Host "\nManual instructions to add AUTOMATION_PAT to the repository secrets:" -ForegroundColor Cyan
Write-Host "1) Create a PAT with the required scopes:\n   - Classic PAT: 'repo' and 'workflow' scopes; OR\n   - Fine-grained PAT: give access to 'kalvinparker/kalvinparker' and 'kalvinparker/kalvinparker' with Actions: Read & write and Contents: Read & write." -ForegroundColor White
Write-Host "2) Add the secret via GitHub UI:\n   - Go to: https://github.com/kalvinparker/kalvinparker/settings/secrets/actions\n   - Click 'New repository secret'\n   - Name: AUTOMATION_PAT\n   - Value: <paste your PAT>\n   - Save." -ForegroundColor White

Write-Host "\nOptional: Use the GitHub CLI (install: https://cli.github.com/) and then run:" -ForegroundColor Cyan
Write-Host "  gh auth login" -ForegroundColor White
Write-Host "  gh secret set AUTOMATION_PAT --repo kalvinparker/kalvinparker --body '<your_pat>'" -ForegroundColor White

Write-Host "\nAfter adding the secret, re-run your dispatch helper or the workflow." -ForegroundColor Cyan

