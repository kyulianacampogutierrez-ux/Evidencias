@echo off
chcp 65001 > nul
title Presentador de Diapositivas - GA6-240202501-AA1-EV02
echo ===================================================================
echo     PRESENTADOR DE DIAPOSITIVAS INTERACTIVO (SENA ADSO)
echo     Evidencia: GA6-240202501-AA1-EV02 Video Presentacion Oral
echo     Aprendiz: Karen Yuliana Campo - Ficha 228118
echo     Ubicacion: Popayan, Cauca (Modalidad 100%% Virtual)
echo ===================================================================
echo.
echo Abriendo presentador interactivo en el navegador...
echo - Puedes alternar entre DesignCraft y FigCraft con 1 clic.
echo - Usa las flechas (<- y ->) para cambiar de diapositiva.
echo - Presiona F11 para ponerlo en Pantalla Completa y grabar con Loom / OBS.
echo - Incluye teleprompter con el guion en ingles y guia de pronunciacion.
echo.
start "" "%~dp0diapositivas_presentacion.html"
exit
