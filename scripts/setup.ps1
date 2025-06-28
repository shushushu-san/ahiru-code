# AHIRU-CODE Setup Script (PowerShell)
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "AHIRU-CODE Setup Script" -ForegroundColor Cyan
Write-Host ""

# 現在のディレクトリを取得
$ahiruDir = $PSScriptRoot
Write-Host "Adding current directory to PATH: $ahiruDir" -ForegroundColor Yellow
Write-Host ""

try {
    # ユーザー環境変数のPATHを取得
    $currentPath = [Environment]::GetEnvironmentVariable('PATH', 'User')
    if ($currentPath -eq $null) { $currentPath = '' }
    
    # PATHに追加（重複チェック）
    if (-not $currentPath.Split(';').Contains($ahiruDir)) {
        [Environment]::SetEnvironmentVariable('PATH', $currentPath + ';' + $ahiruDir, 'User')
        Write-Host "PATH setup completed!" -ForegroundColor Green
    } else {
        Write-Host "PATH is already configured." -ForegroundColor Green
    }
    
    # PATHEXT環境変数を設定
    $pathext = [Environment]::GetEnvironmentVariable('PATHEXT', 'User')
    if ($pathext -eq $null) { 
        $pathext = [Environment]::GetEnvironmentVariable('PATHEXT', 'Machine') 
    }
    if ($pathext -eq $null) { 
        $pathext = '.COM;.EXE;.BAT;.CMD;.PS1' 
    }
    
    # .CMD、.BAT、.PS1を適切な順序で追加
    $needsUpdate = $false
    
    # 既存のPATHEXTから.PS1、.CMD、.BATを一旦削除
    $pathext = $pathext -replace '\.PS1;?', '' -replace '\.CMD;?', '' -replace '\.BAT;?', ''
    $pathext = $pathext -replace ';;+', ';'  # 重複セミコロンを削除
    $pathext = $pathext.Trim(';')  # 先頭末尾のセミコロンを削除
    
    # 正しい順序で追加（.COM .EXE .BAT .CMD .PS1 ...）
    $pathext = '.COM;.EXE;.BAT;.CMD;.PS1;' + $pathext
    [Environment]::SetEnvironmentVariable('PATHEXT', $pathext, 'User')
    Write-Host "PATHEXT setup completed! (.CMD prioritized over .PS1)" -ForegroundColor Green
    $needsUpdate = $true
    
    if ($needsUpdate) {
        [Environment]::SetEnvironmentVariable('PATHEXT', $pathext, 'User')
        Write-Host "PATHEXT setup completed! (.CMD prioritized)" -ForegroundColor Green
    }
    
    Write-Host ""
    Write-Host "Setup completed! Open a new terminal and use 'ahiru' command from anywhere." -ForegroundColor Green
    Write-Host ""
    Write-Host "Usage:" -ForegroundColor Cyan
    Write-Host "  PowerShell: ahiru (after restart)" -ForegroundColor White
    Write-Host "  Command Prompt: ahiru" -ForegroundColor White
    Write-Host "  PowerShell (immediate): . .\ahiru_profile.ps1; ahiru" -ForegroundColor Yellow
    Write-Host ""
    
    # PowerShellプロファイル設定の提案
    Write-Host "Optional: To enable 'ahiru' in PowerShell immediately, run:" -ForegroundColor Cyan
    Write-Host ". .\ahiru_profile.ps1" -ForegroundColor Yellow
    Write-Host ""
    
    # テスト実行
    Write-Host "Test execution..." -ForegroundColor Yellow
    Write-Host ""
    $projectRoot = Split-Path $ahiruDir -Parent
    & "$projectRoot\ahiru.cmd"
    
} catch {
    Write-Host "Setup failed: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host ""
    Write-Host "Manual setup method:" -ForegroundColor Yellow
    Write-Host "1. Win+R -> sysdm.cpl -> Advanced -> Environment Variables" -ForegroundColor White
    Write-Host "2. Add to user PATH: $ahiruDir" -ForegroundColor White
}

Write-Host ""
Read-Host "Press any key to continue"
