@echo off
echo ファイル整理を開始します...
echo.

:: scriptsフォルダにファイルを移動
echo scripts フォルダに移動中...
move ahiru.py scripts\ 2>nul
move ahiru_ps.ps1 scripts\ 2>nul
move ahiru_profile.ps1 scripts\ 2>nul
move setup.bat scripts\ 2>nul
move setup.ps1 scripts\ 2>nul
move check_path.bat scripts\ 2>nul

:: toolsフォルダにファイルを移動
echo tools フォルダに移動中...
move test_ahiru.ps1 tools\ 2>nul
move debug_pathext.bat tools\ 2>nul
move cleanup.bat tools\ 2>nul

:: 不要になったファイルを削除
echo 不要ファイルを削除中...
if exist ahiru.bat del ahiru.bat

echo.
echo ファイル整理が完了しました！
echo.
echo 現在のメインファイル:
dir *.cmd *.py *.md /b
echo.
echo scriptsフォルダ:
dir scripts /b
echo.
echo toolsフォルダ:
dir tools /b
echo.
pause
