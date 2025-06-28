#!/usr/bin/env pwsh
# 現在のディレクトリを保存
$originalLocation = Get-Location
try {
    # ahiru-codeディレクトリに移動してPythonスクリプトを実行
    Set-Location $PSScriptRoot
    python ahiru.py @args
} finally {
    # 確実に元のディレクトリに戻る
    Set-Location $originalLocation
}
