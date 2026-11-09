@echo off
chcp 65001 > nul
echo ================================================================================
echo   REPRODUCTOR EN VIVO DE DESIGNCRAFT STUDIO - SENA ADSO
echo   Evidencia: GA6-240202501-AA1-EV01 - Personal Statement (English B1.2+)
echo   Aprendiz: Karen Yuliana Campo - Ficha: 228118
echo ================================================================================
echo.
echo Iniciando servidor en vivo en el puerto 7979...
"C:\Program Files\ArtCraft\DesignCraft\designcraft-cli.exe" serve --source "personal_statement.script" --port 7979 --open
pause
