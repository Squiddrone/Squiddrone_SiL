$currentPath = Get-Location
$check_styleguide = Join-Path -Path $currentPath ".\scripts\check_styleguide.ps1"
$check_tests = Join-Path -Path $currentPath ".\scripts\check_tests.ps1"
$check_coverage = Join-Path -Path $currentPath ".\scripts\check_coverage.ps1"

$styleguide = Start-Process powershell -ArgumentList $check_styleguide -Wait -PassThru -NoNewWindow
$tests = Start-Process powershell -ArgumentList $check_tests -Wait -PassThru -NoNewWindow
$coverage = Start-Process powershell -ArgumentList $check_coverage -Wait -PassThru -NoNewWindow

$results = @($styleguide, $tests, $coverage)
$description = @("StyleGuide", "Tests", "Coverage")

$results | ForEach-Object {
    if ($_.ExitCode -ne 0) {
        Write-Host $description[$results.IndexOf($_)] " FAILED!" -fore Red
        $exit = $true
    }
    else {
        Write-Host $description[$results.IndexOf($_)] " PASSED!" -fore Green
    }
}

if ($exit) {
    exit 1
}