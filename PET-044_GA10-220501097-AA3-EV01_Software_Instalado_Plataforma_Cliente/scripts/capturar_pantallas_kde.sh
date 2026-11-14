#!/bin/bash
# ==============================================================================
# SCRIPT DE AUTOMATIZACIÓN DE CAPTURAS CON XDOTOOL Y SPECTACLE EN KDE X11
# Evidencia: GA10-220501097-AA3-EV01 - Software Instalado en la Plataforma del Cliente
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán - Regional Cauca
# ==============================================================================

set -e

export DISPLAY="${DISPLAY:-:0}"
export XAUTHORITY="${XAUTHORITY:-$HOME/.Xauthority}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="${SCRIPT_DIR}/.."
CAPTURAS_DIR="${BASE_DIR}/capturas"
mkdir -p "${CAPTURAS_DIR}"

echo "================================================================================"
echo "INICIANDO CAPTURA DE PANTALLAS CON XDOTOOL Y SPECTACLE EN ENTORNO KDE X11"
echo "Usuario: $(whoami) | DISPLAY: ${DISPLAY}"
echo "Directorio de destino: ${CAPTURAS_DIR}"
echo "================================================================================"

# 1. CAPTURA 1: Terminal con Despliegue de Contenedores Docker
echo "[Paso 1] Capturando estado del contenedor de despliegue Docker..."
spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_01_despliegue_contenedor_docker.png"
sleep 1

# 2. ABRIR GOOGLE CHROME EN EL DESPLIEGUE LOCAL (http://localhost:8088)
echo "[Paso 2] Abriendo Google Chrome en http://localhost:8088..."
google-chrome --new-window "http://localhost:8088" &
CHROME_PID=$!
sleep 3

# Localizar la ventana con xdotool
CHROME_WID=$(xdotool search --onlyvisible --name "Pizzería Gourmet Bella Italia" | tail -n 1 || true)
if [ -z "${CHROME_WID}" ]; then
  CHROME_WID=$(xdotool search --onlyvisible --class "google-chrome" | tail -n 1)
fi

echo "ID de Ventana Chrome detectada: ${CHROME_WID}"
if [ -n "${CHROME_WID}" ]; then
  xdotool windowactivate --sync "${CHROME_WID}"
  xdotool windowsize "${CHROME_WID}" 1280 800
  xdotool windowmove "${CHROME_WID}" 50 50
  sleep 1
fi

# Captura 2: Landing Page Hero Banner
echo "[Paso 2] Capturando Landing Page en Google Chrome..."
spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_02_navegador_chrome_landing_page.png"
sleep 1

# Captura 3: Menú Gourmet Interactivo (Scroll con xdotool)
echo "[Paso 3] Navegando hacia la sección de Menú Gourmet con xdotool..."
if [ -n "${CHROME_WID}" ]; then
  xdotool windowactivate --sync "${CHROME_WID}"
  xdotool key Page_Down
  sleep 1.5
fi
spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_03_chrome_menu_gourmet_interactivo.png"
sleep 1

# Captura 4: Formulario de Checkout y Registro de Pedidos
echo "[Paso 4] Desplazando hacia Formulario de Pedidos..."
if [ -n "${CHROME_WID}" ]; then
  xdotool windowactivate --sync "${CHROME_WID}"
  xdotool key Page_Down
  sleep 1
fi
spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_04_chrome_formulario_checkout_pedido.png"
sleep 1

# Captura 5: Inspección DevTools con F12
echo "[Paso 5] Abriendo DevTools en Google Chrome (F12)..."
if [ -n "${CHROME_WID}" ]; then
  xdotool windowactivate --sync "${CHROME_WID}"
  xdotool key F12
  sleep 2
fi
spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_05_chrome_devtools_inspeccion_red.png"
sleep 1

# Cerrar DevTools
if [ -n "${CHROME_WID}" ]; then
  xdotool key F12
  sleep 0.5
fi

# Captura 6: Terminal con Ejecución de Respaldo y Migración
echo "[Paso 6] Generando captura del Plan de Respaldo y Migración de Datos..."
spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_06_plan_respaldo_migracion_datos.png"
sleep 1

echo "================================================================================"
echo "CAPTURA DE PANTALLAS FINALIZADA EXITOSAMENTE CON SPECTACLE"
ls -lh "${CAPTURAS_DIR}"
echo "================================================================================"
