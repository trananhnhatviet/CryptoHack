# demo_create_file.ps1
# Demo PowerShell cơ bản – KHÔNG PHẢI malware

$path = "C:\Temp\hacked.txt"
$content = "Da bi hack (demo PowerShell)"

# Tạo thư mục nếu chưa tồn tại
if (!(Test-Path "C:\Temp")) {
    New-Item -ItemType Directory -Path "C:\Temp"
}

# Ghi nội dung vào file
Set-Content -Path $path -Value $content

Write-Host "Da tao file hacked.txt tai C:\Temp"
