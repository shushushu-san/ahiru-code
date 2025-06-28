# PowerShellでahiruコマンドの実行テスト
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "=== ahiru command test ===" -ForegroundColor Cyan
Write-Host ""

# 現在のディレクトリを表示
Write-Host "Current directory: $PWD" -ForegroundColor Yellow

# ahiruコマンドの場所を確認
Write-Host "ahiru command search result:" -ForegroundColor Green
$ahiruCmd = Get-Command ahiru -ErrorAction SilentlyContinue
if ($ahiruCmd) {
    $ahiruCmd | Select-Object Name, Source, CommandType
} else {
    Write-Host "ahiru command not found" -ForegroundColor Red
}

# PATHEXT環境変数を確認
Write-Host ""
Write-Host "PATHEXT environment variable:" -ForegroundColor Green
$env:PATHEXT

# 実行ポリシーを確認
Write-Host ""
Write-Host "PowerShell execution policy:" -ForegroundColor Green
Get-ExecutionPolicy

# 手動でファイル検索
Write-Host ""
Write-Host "Manual file search:" -ForegroundColor Green
$ahiruFiles = Get-ChildItem -Path $env:PATH.Split(';') -Filter "ahiru*" -ErrorAction SilentlyContinue
$ahiruFiles | Select-Object Name, FullName

Write-Host ""
Read-Host "Press any key to continue"
