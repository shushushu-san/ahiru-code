@echo off
chcp 65001 >nul
echo AHIRU-CODE セットアップスクリプト
echo.

:: 現在のディレクトリを取得
set "AHIRU_DIR=%~dp0"
set "AHIRU_DIR=%AHIRU_DIR:~0,-1%"

echo 現在のディレクトリをPATHに追加します: %AHIRU_DIR%
echo.

:: ユーザー環境変数のPATHに追加
echo PATH環境変数を設定中...
powershell -Command "try { $currentPath = [Environment]::GetEnvironmentVariable('PATH', 'User'); if ($currentPath -eq $null) { $currentPath = '' }; [Environment]::SetEnvironmentVariable('PATH', $currentPath + ';%AHIRU_DIR%', 'User'); exit 0 } catch { exit 1 }"
set PATH_RESULT=%ERRORLEVEL%

echo PATHEXT環境変数を設定中...
powershell -Command "try { $pathext = [Environment]::GetEnvironmentVariable('PATHEXT', 'User'); if ($pathext -eq $null) { $pathext = [Environment]::GetEnvironmentVariable('PATHEXT', 'Machine') }; if ($pathext -eq $null) { $pathext = '.COM;.EXE;.BAT;.CMD' }; if (-not $pathext.ToUpper().Contains('.BAT')) { [Environment]::SetEnvironmentVariable('PATHEXT', $pathext + ';.BAT', 'User') }; exit 0 } catch { exit 1 }"
set PATHEXT_RESULT=%ERRORLEVEL%

if %PATH_RESULT% EQU 0 if %PATHEXT_RESULT% EQU 0 (
    echo ✓ PATH設定が完了しました！
    echo ✓ 新しいターミナルを開いて、どこからでもahiruコマンドが使用できます。
    echo.
    echo 実行方法:
    echo   PowerShell: .\ahiru
    echo   コマンドプロンプト: ahiru
    echo.
    echo テスト実行中...
    echo.
    call "%AHIRU_DIR%\ahiru.bat"
) else (
    echo ✗ PATH設定に失敗しました。手動で設定してください。
    echo.
    echo 手動設定方法:
    echo 1. Win+R → sysdm.cpl → 詳細設定 → 環境変数
    echo 2. ユーザー環境変数のPathに以下を追加: %AHIRU_DIR%
)

echo.
pause
