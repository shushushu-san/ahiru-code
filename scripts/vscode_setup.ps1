# VS Code用 ahiru セットアップスクリプト
# VS CodeのPowerShellターミナルでahiruコマンドを使えるようにします

Write-Host "=== VS Code ahiru Setup ===" -ForegroundColor Cyan
Write-Host "VS CodeのPowerShellターミナル用にahiru関数を設定します" -ForegroundColor Yellow
Write-Host ""

# プロジェクトルートディレクトリを取得
$projectRoot = Split-Path $PSScriptRoot -Parent
Write-Host "Project root: $projectRoot" -ForegroundColor Gray

# PowerShellプロファイルパスを取得
$profilePath = $PROFILE.CurrentUserCurrentHost
$profileDir = Split-Path $profilePath -Parent

Write-Host "PowerShell profile: $profilePath" -ForegroundColor Gray
Write-Host ""

# プロファイルディレクトリが存在しない場合は作成
if (-not (Test-Path $profileDir)) {
    Write-Host "Creating profile directory..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Path $profileDir -Force | Out-Null
}

# ahiru関数の定義
$ahiruFunction = @"

# ahiru AI launcher function (VS Code用)
function ahiru {
    param([Parameter(ValueFromRemainingArguments)]`$args)
    `$ahiruPath = "$projectRoot"
    `$originalLocation = Get-Location
    try {
        Set-Location `$ahiruPath
        python scripts\ahiru.py @args
    } finally {
        Set-Location `$originalLocation
    }
}

Write-Host "ahiru function loaded! Use 'ahiru' command in VS Code terminal." -ForegroundColor Green
"@

# 既存のプロファイルをチェック
if (Test-Path $profilePath) {
    $profileContent = Get-Content $profilePath -Raw -ErrorAction SilentlyContinue
    if ($profileContent -and $profileContent -match "function ahiru") {
        Write-Host "ahiru function already exists in PowerShell profile" -ForegroundColor Yellow
        Write-Host "Updating to current project path..." -ForegroundColor Yellow
        
        # 既存のahiru関数を更新
        $profileContent = $profileContent -replace '(?s)# ahiru AI launcher function.*?^}', $ahiruFunction.Trim()
        Set-Content -Path $profilePath -Value $profileContent -Encoding UTF8
    } else {
        # 新しく関数を追加
        Add-Content -Path $profilePath -Value $ahiruFunction -Encoding UTF8
        Write-Host "ahiru function added to PowerShell profile" -ForegroundColor Green
    }
} else {
    # 新しいプロファイルを作成
    Set-Content -Path $profilePath -Value $ahiruFunction.TrimStart() -Encoding UTF8
    Write-Host "Created PowerShell profile with ahiru function" -ForegroundColor Green
}

Write-Host ""
Write-Host "Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Usage in VS Code:" -ForegroundColor Cyan
Write-Host "1. Restart VS Code (recommended)" -ForegroundColor White
Write-Host "2. または現在のターミナルで: . `$PROFILE" -ForegroundColor White
Write-Host "3. Then use: ahiru" -ForegroundColor White
Write-Host ""

# 現在のセッションに関数を読み込み
try {
    . $profilePath
    Write-Host "ahiru function loaded in current session!" -ForegroundColor Green
    Write-Host "You can now use 'ahiru' command in this terminal." -ForegroundColor Green
} catch {
    Write-Host "Note: Restart VS Code to use the ahiru command." -ForegroundColor Yellow
}

Write-Host ""
Read-Host "Press Enter to continue"
