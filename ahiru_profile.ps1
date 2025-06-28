# PowerShell Profile function for ahiru command
# Add this to your PowerShell profile for permanent ahiru command access

function ahiru {
    param([Parameter(ValueFromRemainingArguments)]$args)
    $ahiruPath = "C:\Users\gents\1.University\Projects\Yukari_tech\ahiruAI\ahiru-code"
    $originalLocation = Get-Location
    try {
        Set-Location $ahiruPath
        python ahiru.py @args
    } finally {
        Set-Location $originalLocation
    }
}

Write-Host "ahiru function loaded! Use 'ahiru' command anywhere in PowerShell." -ForegroundColor Green
