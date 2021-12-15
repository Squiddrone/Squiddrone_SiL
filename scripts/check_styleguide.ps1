$currentPath = Get-Location
$sil_framework = Join-Path -Path $currentPath "sil_framework"

$flake_program = Join-Path -Path $currentPath "venv\Scripts\flake8.exe"
$flake_config_file = Join-Path -Path $currentPath -ChildPath ".flake8"

$pylint_program = Join-Path -Path $currentPath "venv\Scripts\pylint.exe"
$pylint_config_file = Join-Path -Path $currentPath -ChildPath ".pylintrc"

$flake = Start-Process $flake_program -ArgumentList "$sil_framework --config=$flake_config_file" -Wait -PassThru -NoNewWindow
$pylint = Start-Process $pylint_program -ArgumentList "$sil_framework --rcfile=$pylint_config_file" -Wait -PassThru -NoNewWindow

if (($flake.ExitCode -ne 0) -or ($pylint.ExitCode -ne 0))
{
    exit 1
}