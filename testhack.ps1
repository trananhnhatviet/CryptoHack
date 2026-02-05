$path = "C:\Temp\hacked.txt"
$content = "Da bi hack (demo PowerShell)"

if (!(Test-Path "C:\Temp")) {
    New-Item -ItemType Directory -Path "C:\Temp"
}

Set-Content -Path $path -Value $content

Write-Host "Da tao file hacked.txt tai C:\Temp"
