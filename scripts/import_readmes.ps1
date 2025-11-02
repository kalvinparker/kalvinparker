param(
    [string[]]$Repos = @('Windows-help','Security-Tools','WSL','CET','trivy','SAST','Prompt_Engineering','docker-cheat-sheet'),
    [switch]$FullCloneIfMissing,
    [string]$OutputPath
)

$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
$root = Resolve-Path "$root\.." | Select-Object -ExpandProperty Path
$profile = $root
# If OutputPath is supplied use it (relative paths resolved against script root), otherwise default to profile/docs
if ($OutputPath) {
    if (-not (Split-Path -Path $OutputPath -IsAbsolute)) {
        $docsDir = Join-Path $root $OutputPath
    } else {
        $docsDir = $OutputPath
    }
} else {
    $docsDir = Join-Path $profile 'docs'
}
$tmp = Join-Path $profile 'tmp_imports'

if (Test-Path $tmp) { Remove-Item -Recurse -Force $tmp }
New-Item -ItemType Directory -Path $tmp | Out-Null

# Ensure output docs directory exists
if (-not (Test-Path $docsDir)) {
    New-Item -ItemType Directory -Path $docsDir -Force | Out-Null
}

$report = @()

foreach ($r in $Repos) {
    $repoUrl = "https://github.com/kalvinparker/$r.git"
    $dest = Join-Path $tmp $r
    $snapshotPath = Join-Path $docsDir ("$r.md")
    try {
        git clone --depth 1 $repoUrl $dest 2>$null
        $report += "Cloned $r"

        $candidates = Get-ChildItem -Path $dest -Recurse -File -Include README*,readme*,index* -ErrorAction SilentlyContinue | Sort-Object FullName
        if (-not $candidates -and $FullCloneIfMissing) {
            Remove-Item -Recurse -Force $dest
            git clone $repoUrl $dest 2>$null
            $candidates = Get-ChildItem -Path $dest -Recurse -File -Include README*,readme*,index* -ErrorAction SilentlyContinue | Sort-Object FullName
        }

        $commitHash = ''
        $author = ''
        $lic = $null
        if (Test-Path $dest) {
            Push-Location $dest
            try {
                $commitHash = (git rev-parse --short HEAD) -join ''
                $author = (git log -1 --pretty=format:"%an <%ae>") -join ''
            } catch { }
            Pop-Location

            $lic = Get-ChildItem -Path $dest -File -Include LICENSE,LICENSE.md,LICENSE.txt -ErrorAction SilentlyContinue | Select-Object -First 1
        }

        if ($candidates -and $candidates.Count -gt 0) {
            $first = $candidates[0]
            $content = Get-Content -Raw -Path $first.FullName -ErrorAction Stop
            $rel = $first.FullName.Replace($dest,'')
            $licenseSnippet = ''
            if ($lic) { $licenseSnippet = Get-Content -Raw -Path $lic.FullName -ErrorAction SilentlyContinue }
            $header = "<!-- Imported from $repoUrl`nCommit: $commitHash`nAuthor: $author`nLicense-Name: $($lic.Name -as [string])`nLicense-Text: `n$licenseSnippet`nImported-on: $(Get-Date -Format o) -->`r`n`r`n"
            $header + $content | Out-File -FilePath $snapshotPath -Encoding utf8
            $report += "Imported README for $r (path: $rel)"
        } else {
            $listing = Get-ChildItem -Path $dest -File -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Name
            $body = "# $r`n`nNo README found. Repository file listing:`n`n" + ($listing -join "`n")
            $licenseSnippet = ''
            if ($lic) { $licenseSnippet = Get-Content -Raw -Path $lic.FullName -ErrorAction SilentlyContinue }
            $meta = "<!-- Imported from $repoUrl`nCommit: $commitHash`nAuthor: $author`nLicense-Name: $($lic.Name -as [string])`nLicense-Text: `n$licenseSnippet`nImported-on: $(Get-Date -Format o) -->`r`n`r`n"
            $meta + $body | Out-File -FilePath $snapshotPath -Encoding utf8
            $report += "No README; wrote listing for $r"
        }
    } catch {
        $report += ("Failed to clone/import {0}: {1}" -f $r, $_.Exception.Message)
    }
}

# cleanup: try removing .git folders first (reduces locked handles), retry deletion
if (Test-Path $tmp) {
    try {
        Get-ChildItem -Path $tmp -Recurse -Directory -Force -ErrorAction SilentlyContinue | Where-Object { $_.Name -eq '.git' } | ForEach-Object { Remove-Item -Recurse -Force -LiteralPath $_.FullName -ErrorAction SilentlyContinue }
    } catch { }
    for ($i=0;$i -lt 6;$i++) {
        try {
            Remove-Item -Recurse -Force $tmp -ErrorAction Stop
            break
        } catch { Start-Sleep -Seconds (2*$i) }
    }
}

Write-Output "--- REPORT ---"
$report | ForEach-Object { Write-Output $_ }
