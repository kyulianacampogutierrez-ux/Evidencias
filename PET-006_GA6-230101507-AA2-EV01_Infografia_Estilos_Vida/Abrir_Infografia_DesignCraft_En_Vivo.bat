@echo off
chcp 65001 >nul
title Reproducir Infografia en DesignCraft - SENA ADSO Ficha 228118
echo ======================================================================
echo   SENA - ADSO Ficha 228118 - Karen Yuliana Campo
echo   Evidencia: GA6-230101507-AA2-EV01: Infografia Estilos de Vida Saludable
echo ======================================================================
echo.
echo [1/2] Enviando 177 comandos de trazado y maquetacion a DesignCraft...
echo (Si tienes abierto DesignCraft en segundo plano, veras como se dibuja en vivo)
echo.

"C:\Program Files\ArtCraft\DesignCraft\designcraft-cli.exe" script "%~dp0infografia_estilos_vida.script" --connect 7979 --keep-going

echo.
echo [2/2] Abriendo el diseno editable y la imagen de alta resolucion...
start "" "%~dp0infografia_estilos_vida.png"

echo.
echo ======================================================================
echo   Proceso completado con exito en DesignCraft CLI!
echo   Archivo editable: %~dp0infografia_estilos_vida.designcraft
echo   Imagen PNG HD:    %~dp0infografia_estilos_vida.png
echo ======================================================================
pause
