$currentPath = Get-Location
$pytest = Join-Path -Path $currentPath "venv\Scripts\pytest.exe"
$process = Start-Process $pytest -Wait -PassThru -NoNewWindow

if ($process.ExitCode -ne 0)
{
    exit 1
}