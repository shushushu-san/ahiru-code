@echo off
echo Cleaning up conflicting ahiru files...
echo.

if exist ahiru.bat (
    echo Deleting ahiru.bat to avoid conflicts...
    del ahiru.bat
)

if exist ahiru_cmd.bat (
    echo Deleting ahiru_cmd.bat to avoid conflicts...
    del ahiru_cmd.bat
)

echo.
echo Remaining ahiru files:
dir ahiru.* /b
echo.
echo Cleanup completed!
pause
