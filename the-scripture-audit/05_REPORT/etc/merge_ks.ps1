$content = Get-Content -Path .\ks_part1.md, .\ks_part2.md, .\ks_part3.md, .\ks_part4.md, .\ks_part5.md -Raw
Set-Content -Path .\ks.md -Value $content -Encoding UTF8
Remove-Item .\ks_part1.md, .\ks_part2.md, .\ks_part3.md, .\ks_part4.md, .\ks_part5.md
Write-Host "Successfully merged ks_part files into ks.md and deleted the parts."
