@echo off
cd /d "%~dp0"

echo Menambahkan semua perubahan ke Git...
git add .

echo Membuat commit dengan pesan otomatis...
git commit -m "update otomatis"

echo Mengirim ke GitHub...
git push

echo.
echo ✅ Selesai! Perubahan sudah dikirim ke GitHub.
pause
