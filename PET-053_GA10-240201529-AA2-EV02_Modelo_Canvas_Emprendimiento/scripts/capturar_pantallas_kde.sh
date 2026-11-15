#!/usr/bin/env bash
# ==============================================================================
# SCRIPT DE CAPTURA DE PANTALLA EN KDE X11 CON SPECTACLE, KONSOLE Y CHROME
# Evidencia: GA10-240201529-AA2-EV02 - Modelo Canvas del emprendimiento
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán - Regional Cauca
# ==============================================================================

set -e

export DISPLAY="${DISPLAY:-:0}"
export XAUTHORITY="${XAUTHORITY:-$HOME/.Xauthority}"

BASE_DIR="/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-053_GA10-240201529-AA2-EV02_Modelo_Canvas_Emprendimiento"
CAPTURAS_DIR="${BASE_DIR}/capturas"
URL_PORTAL="http://localhost:8101/"

mkdir -p "${CAPTURAS_DIR}"

echo "[INFO] Iniciando protocolo de capturas reales en KDE Plasma X11..."

# Función obligatoria: Minimizar ventanas de Visual Studio Code
minimizar_vscode() {
    echo "[INFO] Minimizando ventanas de Visual Studio Code..."
    for wid in $(DISPLAY=:0 xdotool search --class "code" 2>/dev/null || true); do
        DISPLAY=:0 xdotool windowminimize "$wid" 2>/dev/null || true
    done
    for wid in $(DISPLAY=:0 xdotool search --name "Visual Studio Code" 2>/dev/null || true); do
        DISPLAY=:0 xdotool windowminimize "$wid" 2>/dev/null || true
    done
    sleep 1
}

minimizar_vscode

# ------------------------------------------------------------------------------
# PASO 1: Despliegue de Contenedores Docker en Konsole
# ------------------------------------------------------------------------------
echo "[INFO] Paso 1: Ejecución de despliegue Docker en Konsole..."
konsole --geometry 1200x750+100+100 -e bash -c "
    echo '=== DESPLIEGUE DEL PORTAL MODELO CANVAS EN DOCKER (PUERTO 8101) ===';
    echo 'Evidencia: GA10-240201529-AA2-EV02 | Aprendiz: Karen Campo (Ficha 3186681)';
    cd '${BASE_DIR}/docker_lean_canvas';
    docker compose ps;
    echo '';
    echo '=== ESTRUCTURA DE COMPONENTES DEL MODELO CANVAS ===';
    ls -la '${BASE_DIR}/sitio_lean_canvas/';
    sleep 12
" &
KONSOLE_PID=$!
sleep 4
minimizar_vscode

KONSOLE_WIN=$(DISPLAY=:0 xdotool search --pid $KONSOLE_PID 2>/dev/null | tail -n 1 || true)
if [ -n "$KONSOLE_WIN" ]; then
    DISPLAY=:0 xdotool windowactivate "$KONSOLE_WIN" 2>/dev/null || true
    DISPLAY=:0 xdotool windowraise "$KONSOLE_WIN" 2>/dev/null || true
fi
sleep 2

DISPLAY=:0 spectacle -b -n -o "${CAPTURAS_DIR}/paso_01_despliegue_docker_lean_canvas_konsole.png"
echo "[OK] Captura 1 guardada: paso_01_despliegue_docker_lean_canvas_konsole.png"

kill $KONSOLE_PID 2>/dev/null || true
sleep 2

# ------------------------------------------------------------------------------
# PASO 2: Verificación de Salud de Servicios y JSON en Konsole
# ------------------------------------------------------------------------------
echo "[INFO] Paso 2: Verificación de salud y parsing JSON en Konsole..."
konsole --geometry 1200x750+100+100 -e bash -c "
    echo '=== HEALTHCHECK Y VERIFICACIÓN DE API JSON DEL MODELO CANVAS ===';
    curl -I http://localhost:8101/;
    echo '';
    echo '=== RESUMEN DE LOS 9 BLOQUES MODELO CANVAS (JSON) ===';
    curl -s http://localhost:8101/modelo_lean_canvas.json | grep -E '\"nombre\":|\"proyecto\":|\"lema_principal\":';
    sleep 12
" &
KONSOLE_PID2=$!
sleep 4
minimizar_vscode

KONSOLE_WIN2=$(DISPLAY=:0 xdotool search --pid $KONSOLE_PID2 2>/dev/null | tail -n 1 || true)
if [ -n "$KONSOLE_WIN2" ]; then
    DISPLAY=:0 xdotool windowactivate "$KONSOLE_WIN2" 2>/dev/null || true
    DISPLAY=:0 xdotool windowraise "$KONSOLE_WIN2" 2>/dev/null || true
fi
sleep 2

DISPLAY=:0 spectacle -b -n -o "${CAPTURAS_DIR}/paso_02_verificacion_salud_servicios_konsole.png"
echo "[OK] Captura 2 guardada: paso_02_verificacion_salud_servicios_konsole.png"

kill $KONSOLE_PID2 2>/dev/null || true
sleep 2

# ------------------------------------------------------------------------------
# PASO 3: Google Chrome - Portal Modelo Canvas y Diagrama Oficial
# ------------------------------------------------------------------------------
echo "[INFO] Paso 3: Abriendo Google Chrome con Diagrama Oficial Modelo Canvas..."
google-chrome --new-window "${URL_PORTAL}#tab-diagrama" &
CHROME_PID=$!
sleep 5
minimizar_vscode

CHROME_WIN=$(DISPLAY=:0 xdotool search --onlyvisible --class "google-chrome" 2>/dev/null | tail -n 1 || true)
if [ -n "$CHROME_WIN" ]; then
    DISPLAY=:0 xdotool windowactivate "$CHROME_WIN" 2>/dev/null || true
    DISPLAY=:0 xdotool windowraise "$CHROME_WIN" 2>/dev/null || true
    DISPLAY=:0 xdotool windowsize "$CHROME_WIN" 1400 900 2>/dev/null || true
    DISPLAY=:0 xdotool windowmove "$CHROME_WIN" 50 50 2>/dev/null || true
fi
sleep 3
minimizar_vscode

DISPLAY=:0 spectacle -b -n -o "${CAPTURAS_DIR}/paso_03_chrome_lean_canvas_portada_canvas.png"
echo "[OK] Captura 3 guardada: paso_03_chrome_lean_canvas_portada_canvas.png"

# ------------------------------------------------------------------------------
# PASO 4: Google Chrome - Cuadrícula Interactiva de los 9 Bloques
# ------------------------------------------------------------------------------
echo "[INFO] Paso 4: Navegando a Cuadrícula Interactiva de los 9 Bloques..."
if [ -n "$CHROME_WIN" ]; then
    DISPLAY=:0 xdotool windowactivate "$CHROME_WIN" 2>/dev/null || true
    DISPLAY=:0 xdotool key ctrl+l
    sleep 0.5
    DISPLAY=:0 xdotool type "${URL_PORTAL}#tab-canvas"
    DISPLAY=:0 xdotool key Return
fi
sleep 4
minimizar_vscode

DISPLAY=:0 spectacle -b -n -o "${CAPTURAS_DIR}/paso_04_chrome_lean_canvas_bloques_problema_solucion.png"
echo "[OK] Captura 4 guardada: paso_04_chrome_lean_canvas_bloques_problema_solucion.png"

# ------------------------------------------------------------------------------
# PASO 5: Google Chrome - Pestaña de las 4 Áreas Estratégicas
# ------------------------------------------------------------------------------
echo "[INFO] Paso 5: Navegando a pestaña de las 4 Áreas Estratégicas..."
if [ -n "$CHROME_WIN" ]; then
    DISPLAY=:0 xdotool windowactivate "$CHROME_WIN" 2>/dev/null || true
    DISPLAY=:0 xdotool key ctrl+l
    sleep 0.5
    DISPLAY=:0 xdotool type "${URL_PORTAL}#tab-areas"
    DISPLAY=:0 xdotool key Return
fi
sleep 4
minimizar_vscode

DISPLAY=:0 spectacle -b -n -o "${CAPTURAS_DIR}/paso_05_chrome_lean_canvas_propuesta_valor_ventaja.png"
echo "[OK] Captura 5 guardada: paso_05_chrome_lean_canvas_propuesta_valor_ventaja.png"

# ------------------------------------------------------------------------------
# PASO 6: Google Chrome - Simulador Financiero y Punto de Equilibrio
# ------------------------------------------------------------------------------
echo "[INFO] Paso 6: Captura del Simulador Financiero y Costos..."
if [ -n "$CHROME_WIN" ]; then
    DISPLAY=:0 xdotool windowactivate "$CHROME_WIN" 2>/dev/null || true
    DISPLAY=:0 xdotool key ctrl+l
    sleep 0.5
    DISPLAY=:0 xdotool type "${URL_PORTAL}#tab-simulador"
    DISPLAY=:0 xdotool key Return
fi
sleep 4
minimizar_vscode

DISPLAY=:0 spectacle -b -n -o "${CAPTURAS_DIR}/paso_06_chrome_lean_canvas_costos_ingresos_metricas.png"
echo "[OK] Captura 6 guardada: paso_06_chrome_lean_canvas_costos_ingresos_metricas.png"

# Cerrar ventana de Chrome limpia
echo "[INFO] Cerrando sesión de Chrome..."
if [ -n "$CHROME_WIN" ]; then
    DISPLAY=:0 xdotool windowclose "$CHROME_WIN" 2>/dev/null || true
fi
sleep 2

echo "=== PROTOCOLO DE CAPTURAS FINALIZADO CON ÉXITO ==="
