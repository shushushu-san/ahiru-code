@echo off
:: ahiru launcher for Command Prompt and PowerShell
:: Detects environment and executes appropriate script

:: Check if we're in PowerShell by testing for PowerShell-specific variable
powershell -Command "if ($PSVersionTable) { exit 100 } else { exit 200 }" >nul 2>&1

if %ERRORLEVEL% EQU 100 (
    :: Running in PowerShell context - use PowerShell script
    powershell -ExecutionPolicy Bypass -File "%~dp0scripts\ahiru_ps.ps1" %*
) else (
    :: Running in CMD - use Python script directly
    :: Save current directory
    pushd "%~dp0"
    python scripts\ahiru.py %*
    :: Return to original directory
    popd
)
