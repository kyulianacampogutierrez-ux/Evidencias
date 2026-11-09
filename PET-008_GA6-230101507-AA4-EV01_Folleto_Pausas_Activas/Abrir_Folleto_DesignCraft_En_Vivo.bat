@echo off
chcp 65001 >nul
title Reproducir Folleto en DesignCraft - SENA ADSO Ficha 228118
echo ======================================================================
echo   SENA - ADSO Ficha 228118 - Karen Yuliana Campo
echo   Evidencia: GA6-230101507-AA4-EV01: Folleto de Lesiones y Pausas Activas
echo ======================================================================
echo.
echo [1/3] Enviando Cara Exterior (206 comandos) a DesignCraft en vivo...
"C:\Program Files\ArtCraft\DesignCraft\designcraft-cli.exe" script "%~dp0folleto_cara_exterior.script" --connect 7979 --keep-going
echo.
echo [2/3] Enviando Cara Interior (269 comandos) a DesignCraft en vivo...
"C:\Program Files\ArtCraft\DesignCraft\designcraft-cli.exe" script "%~dp0folleto_cara_interior.script" --connect 7979 --keep-going
echo.
echo [3/3] Abriendo imagenes de alta resolucion del folleto...
start "" "%~dp0folleto_cara_exterior.png"
start "" "%~dp0folleto_cara_interior.png"

echo.
echo ======================================================================
echo   Proceso completado con exito en DesignCraft CLI!
echo   Archivo editable: %~dp0folleto_lesiones_pausas.designcraft
echo   Exterior PNG:     %~dp0folleto_cara_exterior.png
echo   Interior PNG:     %~dp0folleto_cara_interior.png
echo ======================================================================
pause
