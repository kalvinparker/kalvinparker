<#
. SYNOPSIS
    Diagnose GitHub Actions workflow dispatch problems for this repo.

. DESCRIPTION
    Prompts for a PAT (or reads $env:AUTOMATION_PAT), then runs several checks:
      - Repo access check (GET /repos/:owner/:repo)
      - List workflows (GET /repos/:owner/:repo/actions/workflows)
      - Check that .github/workflows/<workflowFile> exists at the given ref
      - Optionally attempt to dispatch the workflow (POST) if -Dispatch is supplied

. USAGE
    .\diagnose_workflow.ps1 -WorkflowFile 'sync-readmes.yml' -Ref 'chore/auto-readme-sync-20251101-224716'

    To actually perform a dispatch add -Dispatch
#>

param(
    [Parameter(Mandatory=$true)]
    [string]$WorkflowFile,

    [Parameter(Mandatory=$true)]
    [string]$Ref,

    [switch]$Dispatch
)

function Get-Token {
    if ($env:AUTOMATION_PAT) { return $env:AUTOMATION_PAT }
    $sec = Read-Host -AsSecureString "Enter a PAT with repo+workflow permissions for this repo (input hidden)"
    $ptr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($sec)
    try { [Runtime.InteropServices.Marshal]::PtrToStringAuto($ptr) } finally { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($ptr) }
}

function Invoke-GithubApi {
    param($Method, $Uri, $Body=$null)
    $headers = @{ Authorization = "token $token"; "User-Agent" = "diag" }
    if ($Body) {
        Invoke-RestMethod -Method $Method -Uri $Uri -Headers $headers -ContentType 'application/json' -Body ($Body | ConvertTo-Json -Depth 10) -ErrorAction Stop
    } else {
        Invoke-RestMethod -Method $Method -Uri $Uri -Headers $headers -ErrorAction Stop
    }
}

Write-Host "Running diagnostic for workflow file '$WorkflowFile' on ref '$Ref'...`n" -ForegroundColor Cyan
try {
    $token = Get-Token
} catch {
    Write-Error "Failed to read token: $_"
    exit 2
}

$owner = 'kalvinparker'
$repo = 'kalvinparker'

try {
    Write-Host "1) Checking repository access..." -ForegroundColor White
    $repoInfo = Invoke-GithubApi -Method Get -Uri "https://api.github.com/repos/$owner/$repo"
    Write-Host "  OK: Repo accessible. Full name: $($repoInfo.full_name)" -ForegroundColor Green
} catch {
    Write-Host "  ERROR: Cannot access repository. HTTP: $($_.Exception.Response.StatusCode)" -ForegroundColor Red
    Write-Host "  Message: $($_.Exception.Message)\n" -ForegroundColor Red
    exit 3
}

try {
    Write-Host "2) Listing workflows (repository level)..." -ForegroundColor White
    $wfList = Invoke-GithubApi -Method Get -Uri "https://api.github.com/repos/$owner/$repo/actions/workflows"
    $count = $wfList.workflows.Count
    Write-Host "  OK: $count workflows found." -ForegroundColor Green
    $wfList.workflows | ForEach-Object { Write-Host "    - $($_.name) (id: $($_.id), path: $($_.path))" }
} catch {
    Write-Host "  ERROR: Failed to list workflows. HTTP: $($_.Exception.Response.StatusCode)" -ForegroundColor Red
    Write-Host "  Message: $($_.Exception.Message)\n" -ForegroundColor Red
}

try {
    Write-Host "3) Checking that the workflow file exists on the given ref..." -ForegroundColor White
    $contentsUri = "https://api.github.com/repos/$owner/$repo/contents/.github/workflows/$WorkflowFile?ref=$Ref"
    $fileInfo = Invoke-GithubApi -Method Get -Uri $contentsUri
    if ($fileInfo -and $fileInfo.type -eq 'file') {
        Write-Host "  OK: Workflow file exists on ref '$Ref' (path: $($fileInfo.path), sha: $($fileInfo.sha))." -ForegroundColor Green
    } else {
        Write-Host "  WARNING: File exists but response isn't a file object." -ForegroundColor Yellow
    }
} catch {
    Write-Host "  ERROR: Workflow file not found at .github/workflows/$WorkflowFile on ref '$Ref'." -ForegroundColor Red
    Write-Host "  HTTP/Message: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "  Suggestion: Ensure the workflow file is committed to that branch and pushed to origin." -ForegroundColor Yellow
}

if ($Dispatch) {
    try {
        Write-Host "4) Attempting to dispatch the workflow now..." -ForegroundColor White
        $dispatchUri = "https://api.github.com/repos/$owner/$repo/actions/workflows/$WorkflowFile/dispatches"
        $body = @{ ref = $Ref }
        Invoke-GithubApi -Method Post -Uri $dispatchUri -Body $body
        Write-Host "  Dispatch sent — if accepted you'll see HTTP 204 and an Actions run." -ForegroundColor Green
    } catch {
        Write-Host "  ERROR: Failed to dispatch workflow. HTTP/Message: $($_.Exception.Message)" -ForegroundColor Red
        if ($_.Exception.Response) { Write-Host "  StatusCode: $($_.Exception.Response.StatusCode)" -ForegroundColor Red }
    }
}

Write-Host "\nDiagnostic complete." -ForegroundColor Cyan

