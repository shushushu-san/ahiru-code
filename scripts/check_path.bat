@echo off
chcp 65001 >nul
echo.
echo === AHIRU-CODE PATH確認スクリプト ===
echo.

echo 現在のPATH環境変数（ユーザー）:
powershell -Command "[Environment]::GetEnvironmentVariable('PATH', 'User')"
echo.

echo 現在のPATH環境変数（システム）:
powershell -Command "[Environment]::GetEnvironmentVariable('PATH', 'Machine')"
echo.

echo ahiruコマンドの検索:
where ahiru 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ahiruコマンドが見つかりません
) else (
    echo ahiruコマンドが見つかりました
)
echo.

echo ahiru.batファイルの検索:
where ahiru.bat 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ahiru.batファイルが見つかりません
) else (
    echo ahiru.batファイルが見つかりました
)
echo.

echo 推奨解決方法:
echo 1. コマンドプロンプト/PowerShellを完全に閉じる
echo 2. 新しいコマンドプロンプト/PowerShellを開く
echo 3. どのディレクトリからでもahiruと入力してテスト
echo.
pause
