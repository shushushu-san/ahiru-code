#!/usr/bin/env pwsh
# 現在のディレクトリを保存
$originalLocation = Get-Location
try {
    # プロジェクトルートディレクトリに移動してPythonスクリプトを実行
    $projectRoot = Split-Path $PSScriptRoot -Parent
    Set-Location $projectRoot
    python scripts\ahiru.py @args
} finally {
    # 確実に元のディレクトリに戻る
    Set-Location $originalLocation
}
