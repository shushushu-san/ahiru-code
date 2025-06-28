@echo off
echo === PATHEXT and Command Priority Check ===
echo.

echo Current PATHEXT (User):
powershell -Command "[Environment]::GetEnvironmentVariable('PATHEXT', 'User')"
echo.

echo Current PATHEXT (System):
powershell -Command "[Environment]::GetEnvironmentVariable('PATHEXT', 'Machine')"
echo.

echo Current combined PATHEXT:
echo %PATHEXT%
echo.

echo Files found for 'ahiru':
where ahiru* 2>nul
echo.

echo Testing command resolution:
where ahiru 2>nul
echo.

pause
