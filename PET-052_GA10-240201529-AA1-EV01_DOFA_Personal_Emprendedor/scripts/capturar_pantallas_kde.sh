#!/usr/bin/env bash
# ==============================================================================
# SCRIPT DE CAPTURA DE PANTALLA EN KDE X11 CON SPECTACLE Y XDOTOOL
# Evidencia: GA10-240201529-AA1-EV01 - DOFA personal en Hoja de Cálculo
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán - Regional Cauca
# ==============================================================================

set -e

export DISPLAY=:0
export XAUTHORITY=/home/danilo/.Xauthority

BASE_DIR="/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-052_GA10-240201529-AA1-EV01_DOFA_Personal_Emprendedor"
CAPTURAS_DIR="${BASE_DIR}/capturas"
HOJA_ODS="${BASE_DIR}/hoja_de_calculo/GA10-240201529-AA1-EV01_DOFA_Personal_Emprendedor.ods"

mkdir -p "${CAPTURAS_DIR}"

echo "[INFO] Iniciando protocolo de capturas reales en KDE Plasma X11..."

# Función obligatoria: Minimizar cualquier ventana de Visual Studio Code
minimizar_vscode() {
    echo "[INFO] Minimizando ventanas de Visual Studio Code..."
    for win in $(xdotool search --class "code" 2>/dev/null || true); do
        xdotool windowminimize "$win" 2>/dev/null || true
    done
    for win in $(xdotool search --name "Visual Studio Code" 2>/dev/null || true); do
        xdotool windowminimize "$win" 2>/dev/null || true
    done
    sleep 1
}

minimizar_vscode

# ------------------------------------------------------------------------------
# PASO 1: Generación y Validación de la Hoja de Cálculo en Konsole
# ------------------------------------------------------------------------------
echo "[INFO] Paso 1: Ejecución en Konsole..."
konsole --geometry 1200x750+100+100 -e bash -c "
    echo '=== GENERACIÓN DE HOJA DE CÁLCULO DOFA PERSONAL EMPRENDEDOR ===';
    echo 'Evidencia: GA10-240201529-AA1-EV01 | Aprendiz: Karen Campo (Ficha 3186681)';
    cd '${BASE_DIR}';
    python3 scripts/generar_hoja_calculo_dofa.py;
    echo '';
    echo '=== RESUMEN DE ARCHIVOS GENERADOS ===';
    ls -lh hoja_de_calculo/;
    sleep 15
" &
KONSOLE_PID=$!
sleep 4
minimizar_vscode

# Activar ventana Konsole
KONSOLE_WIN=$(xdotool search --pid $KONSOLE_PID 2>/dev/null | tail -n 1 || true)
if [ -n "$KONSOLE_WIN" ]; then
    xdotool windowactivate "$KONSOLE_WIN" 2>/dev/null || true
    xdotool windowraise "$KONSOLE_WIN" 2>/dev/null || true
fi
sleep 2

spectacle -b -n -o "${CAPTURAS_DIR}/paso_01_generacion_hoja_calculo_konsole.png"
echo "[OK] Captura 1 guardada: paso_01_generacion_hoja_calculo_konsole.png"

# Cerrar Konsole del paso 1
kill $KONSOLE_PID 2>/dev/null || true
sleep 2

# ------------------------------------------------------------------------------
# PASO 2: Apertura de LibreOffice Calc - Hoja 1: Portada_Institucional
# ------------------------------------------------------------------------------
echo "[INFO] Paso 2: Abriendo LibreOffice Calc con Hoja 1 (Portada)..."
localc "${HOJA_ODS}" &
CALC_PID=$!
sleep 6
minimizar_vscode

# Buscar ventana de LibreOffice Calc y maximizarla
CALC_WIN=$(xdotool search --class "soffice" 2>/dev/null | tail -n 1 || true)
if [ -n "$CALC_WIN" ]; then
    xdotool windowactivate "$CALC_WIN" 2>/dev/null || true
    xdotool windowraise "$CALC_WIN" 2>/dev/null || true
    xdotool windowsize "$CALC_WIN" 1400 900 2>/dev/null || true
    xdotool windowmove "$CALC_WIN" 50 50 2>/dev/null || true
fi
sleep 2
minimizar_vscode

spectacle -b -n -o "${CAPTURAS_DIR}/paso_02_libreoffice_calc_hoja1_portada.png"
echo "[OK] Captura 2 guardada: paso_02_libreoffice_calc_hoja1_portada.png"

# ------------------------------------------------------------------------------
# PASO 3: LibreOffice Calc - Hoja 2: Matriz_DOFA_Personal
# ------------------------------------------------------------------------------
echo "[INFO] Paso 3: Navegando a Hoja 2 (Matriz DOFA Personal)..."
if [ -n "$CALC_WIN" ]; then
    xdotool windowactivate "$CALC_WIN" 2>/dev/null || true
    xdotool key Ctrl+Next  # Next sheet (Ctrl+Page_Down)
fi
sleep 3
minimizar_vscode

spectacle -b -n -o "${CAPTURAS_DIR}/paso_03_libreoffice_calc_hoja2_matriz_dofa.png"
echo "[OK] Captura 3 guardada: paso_03_libreoffice_calc_hoja2_matriz_dofa.png"

# ------------------------------------------------------------------------------
# PASO 4: LibreOffice Calc - Hoja 3: Cruce_Estrategico_FODA
# ------------------------------------------------------------------------------
echo "[INFO] Paso 4: Navegando a Hoja 3 (Cruce Estratégico FODA)..."
if [ -n "$CALC_WIN" ]; then
    xdotool windowactivate "$CALC_WIN" 2>/dev/null || true
    xdotool key Ctrl+Next  # Next sheet
fi
sleep 3
minimizar_vscode

spectacle -b -n -o "${CAPTURAS_DIR}/paso_04_libreoffice_calc_hoja3_cruce_foda.png"
echo "[OK] Captura 4 guardada: paso_04_libreoffice_calc_hoja3_cruce_foda.png"

# ------------------------------------------------------------------------------
# PASO 5: LibreOffice Calc - Hoja 5: Plan_Accion_SMART
# ------------------------------------------------------------------------------
echo "[INFO] Paso 5: Navegando a Hoja 5 (Plan de Acción SMART)..."
if [ -n "$CALC_WIN" ]; then
    xdotool windowactivate "$CALC_WIN" 2>/dev/null || true
    xdotool key Ctrl+Next  # A Hoja 4 (Diagnostico)
    sleep 1
    xdotool key Ctrl+Next  # A Hoja 5 (Plan SMART)
fi
sleep 3
minimizar_vscode

spectacle -b -n -o "${CAPTURAS_DIR}/paso_05_libreoffice_calc_hoja5_plan_smart.png"
echo "[OK] Captura 5 guardada: paso_05_libreoffice_calc_hoja5_plan_smart.png"

# ------------------------------------------------------------------------------
# PASO 6: LibreOffice Calc - Hoja 6: Dashboard_Metricas
# ------------------------------------------------------------------------------
echo "[INFO] Paso 6: Navegando a Hoja 6 (Dashboard Métricas IPE)..."
if [ -n "$CALC_WIN" ]; then
    xdotool windowactivate "$CALC_WIN" 2>/dev/null || true
    xdotool key Ctrl+Next  # A Hoja 6 (Dashboard)
fi
sleep 3
minimizar_vscode

spectacle -b -n -o "${CAPTURAS_DIR}/paso_06_libreoffice_calc_hoja6_dashboard_ipe.png"
echo "[OK] Captura 6 guardada: paso_06_libreoffice_calc_hoja6_dashboard_ipe.png"

# Cerrar LibreOffice Calc de manera limpia
echo "[INFO] Cerrando sesión de LibreOffice Calc..."
if [ -n "$CALC_WIN" ]; then
    xdotool key Ctrl+q 2>/dev/null || true
fi
sleep 2
kill $CALC_PID 2>/dev/null || true
killall soffice.bin 2>/dev/null || true

echo "=== PROTOCOLO DE CAPTURAS FINALIZADO CON ÉXITO ==="
