param(
    [string]$WorkflowFile = 'sync-readmes.yml',
    [string]$Ref = 'main'
)

function Get-Pat() {
    if ($env:GITHUB_PAT) { return $env:GITHUB_PAT }
    if ($env:AUTOMATION_PAT) { return $env:AUTOMATION_PAT }
    Write-Host "Enter a PAT with workflow_dispatch permissions for this repo (input hidden):"
    $sec = Read-Host -AsSecureString
    return [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($sec))
}

$pat = Get-Pat
if (-not $pat) { Write-Error "No PAT provided"; exit 2 }

$owner = 'kalvinparker'
$repo = 'profile-template'

$url = "https://api.github.com/repos/$owner/$repo/actions/workflows/$WorkflowFile/dispatches"

$body = @{ ref = $Ref } | ConvertTo-Json

Write-Host "Dispatching workflow $WorkflowFile on $owner/$repo (ref: $Ref)"

try {
    $resp = Invoke-RestMethod -Uri $url -Method Post -Headers @{ Authorization = "token $pat"; 'User-Agent' = 'dispatch-script' } -Body $body -ContentType 'application/json'
    Write-Host "Workflow dispatch requested. Response: $resp"
} catch {
    Write-Error "Failed to dispatch workflow: $_"
    exit 1
}

Write-Host "Dispatch request sent. Check Actions console for run status."
