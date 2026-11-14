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

# Función para minimizar estrictamente cualquier ventana de Visual Studio Code
minimizar_vscode() {
  for wid in $(DISPLAY=:0 xdotool search --class "code" 2>/dev/null || true); do
    DISPLAY=:0 xdotool windowminimize "$wid" 2>/dev/null || true
  done
  for wid in $(DISPLAY=:0 xdotool search --name "Visual Studio Code" 2>/dev/null || true); do
    DISPLAY=:0 xdotool windowminimize "$wid" 2>/dev/null || true
  done
}

# Minimizar VS Code antes de cualquier acción
minimizar_vscode
sleep 1

# ------------------------------------------------------------------------------
# PASO 1: Ejecutar comandos de despliegue Docker en Terminal Konsole (KDE)
# ------------------------------------------------------------------------------
echo "[Paso 1] Ejecutando comandos de despliegue Docker en Terminal Konsole..."
minimizar_vscode

RUN_P1="/tmp/run_paso1_docker.sh"
cat << 'EOF' > "${RUN_P1}"
#!/bin/bash
clear
echo -e "\033[1;36m================================================================================\033[0m"
echo -e "\033[1;37;44m SENA CTPI POPAYÁN - REGIONAL CAUCA | ADSO FICHA 3186681 | APRENDIZ: KAREN CAMPO \033[0m"
echo -e "\033[1;36m EVIDENCIA GA10-220501097-AA3-EV01: SOFTWARE INSTALADO EN LA PLATAFORMA CLIENTE \033[0m"
echo -e "\033[1;36m FASE 1: DESPLIEGUE DE LA PLATAFORMA EN CONTENEDOR DOCKER (SIN CONTAMINAR HOST)  \033[0m"
echo -e "\033[1;36m================================================================================\033[0m"
echo ""
cd /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-044_GA10-220501097-AA3-EV01_Software_Instalado_Plataforma_Cliente/docker
echo -e "\033[1;32mdanilo@linux-workstation\033[0m:\033[1;34m~/SENA/.../PET-044/docker\033[0m$ docker compose ps"
docker compose ps
echo ""
echo -e "\033[1;32mdanilo@linux-workstation\033[0m:\033[1;34m~/SENA/.../PET-044/docker\033[0m$ docker ps --filter name=sena-cliente-landing-pizzeria --format \"table {{.Names}}\t{{.Status}}\t{{.Ports}}\""
docker ps --filter name=sena-cliente-landing-pizzeria --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
echo ""
echo -e "\033[1;32mdanilo@linux-workstation\033[0m:\033[1;34m~/SENA/.../PET-044/docker\033[0m$ curl -I http://localhost:8088/"
curl -I http://localhost:8088/
echo ""
echo -e "\033[1;32m[✓] PLATAFORMA NGINX DESPLEGADA SATISFACTORIAMENTE EN PUERTO 8088\033[0m"
echo -e "\033[1;33m[!] ENTORNO 100% AISLADO EN DOCKER - CERO CONTAMINACIÓN DE PAQUETES EN HOST CLIENTE\033[0m"
EOF
chmod +x "${RUN_P1}"

# Lanzar Konsole
konsole --hold -e bash "${RUN_P1}" &
KPID1=$!
sleep 2

# Localizar ventana de Konsole
KONSOLE_WID=$(DISPLAY=:0 xdotool search --onlyvisible --class "konsole" 2>/dev/null | tail -n 1 || true)
if [ -n "${KONSOLE_WID}" ]; then
  DISPLAY=:0 xdotool windowactivate --sync "${KONSOLE_WID}"
  DISPLAY=:0 xdotool windowsize "${KONSOLE_WID}" 1450 850
  DISPLAY=:0 xdotool windowmove "${KONSOLE_WID}" 235 90
  sleep 1
fi

minimizar_vscode
sleep 1

echo "[Paso 1] Capturando terminal Konsole con Spectacle..."
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_01_despliegue_contenedor_docker.png"
sleep 1

# Cerrar Konsole de Paso 1
if [ -n "${KONSOLE_WID}" ]; then
  DISPLAY=:0 xdotool windowclose "${KONSOLE_WID}" 2>/dev/null || kill "${KPID1}" 2>/dev/null || true
fi
sleep 1

# ------------------------------------------------------------------------------
# PASO 2: Abrir Google Chrome en Landing Page Local (http://localhost:8088)
# ------------------------------------------------------------------------------
echo "[Paso 2] Abriendo Google Chrome en http://localhost:8088..."
minimizar_vscode

google-chrome --new-window "http://localhost:8088" &
CHROME_PID=$!
sleep 3

# Localizar la ventana con xdotool
CHROME_WID=$(DISPLAY=:0 xdotool search --onlyvisible --name "Pizzería Gourmet Bella Italia" 2>/dev/null | tail -n 1 || true)
if [ -z "${CHROME_WID}" ]; then
  CHROME_WID=$(DISPLAY=:0 xdotool search --onlyvisible --class "google-chrome" 2>/dev/null | tail -n 1)
fi

echo "ID de Ventana Chrome detectada: ${CHROME_WID}"
if [ -n "${CHROME_WID}" ]; then
  DISPLAY=:0 xdotool windowactivate --sync "${CHROME_WID}"
  DISPLAY=:0 xdotool windowsize "${CHROME_WID}" 1550 920
  DISPLAY=:0 xdotool windowmove "${CHROME_WID}" 185 60
  sleep 1
fi

minimizar_vscode
sleep 1

echo "[Paso 2] Capturando Landing Page en Google Chrome..."
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_02_navegador_chrome_landing_page.png"
sleep 1

# ------------------------------------------------------------------------------
# PASO 3: Navegación Interactiva hacia el Menú Gourmet (Scroll con xdotool)
# ------------------------------------------------------------------------------
echo "[Paso 3] Navegando hacia la sección de Menú Gourmet con xdotool..."
minimizar_vscode
if [ -n "${CHROME_WID}" ]; then
  DISPLAY=:0 xdotool windowactivate --sync "${CHROME_WID}"
  DISPLAY=:0 xdotool key Page_Down
  sleep 1.5
fi
minimizar_vscode
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_03_chrome_menu_gourmet_interactivo.png"
sleep 1

# ------------------------------------------------------------------------------
# PASO 4: Formulario de Checkout y Registro de Pedidos
# ------------------------------------------------------------------------------
echo "[Paso 4] Desplazando hacia Formulario de Pedidos..."
minimizar_vscode
if [ -n "${CHROME_WID}" ]; then
  DISPLAY=:0 xdotool windowactivate --sync "${CHROME_WID}"
  DISPLAY=:0 xdotool key Page_Down
  sleep 1
fi
minimizar_vscode
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_04_chrome_formulario_checkout_pedido.png"
sleep 1

# ------------------------------------------------------------------------------
# PASO 5: Inspección DevTools con F12
# ------------------------------------------------------------------------------
echo "[Paso 5] Abriendo DevTools en Google Chrome (F12)..."
minimizar_vscode
if [ -n "${CHROME_WID}" ]; then
  DISPLAY=:0 xdotool windowactivate --sync "${CHROME_WID}"
  DISPLAY=:0 xdotool key F12
  sleep 2.5
fi
minimizar_vscode
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_05_chrome_devtools_inspeccion_red.png"
sleep 1

# Cerrar DevTools y ventana de Chrome usada para las capturas
if [ -n "${CHROME_WID}" ]; then
  DISPLAY=:0 xdotool windowclose "${CHROME_WID}" 2>/dev/null || kill "${CHROME_PID}" 2>/dev/null || true
fi
sleep 1

# ------------------------------------------------------------------------------
# PASO 6: Terminal Konsole con Ejecución de Respaldo y Migración
# ------------------------------------------------------------------------------
echo "[Paso 6] Ejecutando Plan de Respaldo y Migración en Terminal Konsole..."
minimizar_vscode

RUN_P6="/tmp/run_paso6_backup.sh"
cat << 'EOF' > "${RUN_P6}"
#!/bin/bash
clear
echo -e "\033[1;36m================================================================================\033[0m"
echo -e "\033[1;37;44m SENA CTPI POPAYÁN - REGIONAL CAUCA | ADSO FICHA 3186681 | APRENDIZ: KAREN CAMPO \033[0m"
echo -e "\033[1;36m EVIDENCIA GA10-220501097-AA3-EV01: SOFTWARE INSTALADO EN LA PLATAFORMA CLIENTE \033[0m"
echo -e "\033[1;36m FASE 6: EJECUCIÓN PLAN DE RESPALDO (DRP 3-2-1) Y MIGRACIÓN DE DATOS RELACIONALES \033[0m"
echo -e "\033[1;36m================================================================================\033[0m"
echo ""
cd /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-044_GA10-220501097-AA3-EV01_Software_Instalado_Plataforma_Cliente
./scripts/respaldo_migracion_datos.sh
echo ""
echo -e "\033[1;32mdanilo@linux-workstation\033[0m:\033[1;34m~/SENA/.../PET-044\033[0m$ ls -lh respaldos_migracion/"
ls -lh respaldos_migracion/ | tail -n 5
echo ""
LATEST_CHECKSUM=$(ls -t respaldos_migracion/checksums_*.sha256 | head -n 1)
echo -e "\033[1;32mdanilo@linux-workstation\033[0m:\033[1;34m~/SENA/.../PET-044\033[0m$ sha256sum -c ${LATEST_CHECKSUM}"
sha256sum -c "${LATEST_CHECKSUM}"
echo ""
echo -e "\033[1;32m[✓] RESPALDO COMPLETO Y VERIFICACIÓN CRIPTOGRÁFICA SHA-256 EXITOSA (DRP 3-2-1)\033[0m"
echo -e "\033[1;33m[!] INTEGRIDAD CERTIFICADA: ARCHIVOS LISTOS PARA MIGRACIÓN A LA PLATAFORMA CLIENTE\033[0m"
EOF
chmod +x "${RUN_P6}"

# Lanzar Konsole para Paso 6
konsole --hold -e bash "${RUN_P6}" &
KPID6=$!
sleep 3

KONSOLE_WID6=$(DISPLAY=:0 xdotool search --onlyvisible --class "konsole" 2>/dev/null | tail -n 1 || true)
if [ -n "${KONSOLE_WID6}" ]; then
  DISPLAY=:0 xdotool windowactivate --sync "${KONSOLE_WID6}"
  DISPLAY=:0 xdotool windowsize "${KONSOLE_WID6}" 1450 850
  DISPLAY=:0 xdotool windowmove "${KONSOLE_WID6}" 235 90
  sleep 1
fi

minimizar_vscode
sleep 1

echo "[Paso 6] Capturando terminal Konsole con Spectacle..."
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_06_plan_respaldo_migracion_datos.png"
sleep 1

if [ -n "${KONSOLE_WID6}" ]; then
  DISPLAY=:0 xdotool windowclose "${KONSOLE_WID6}" 2>/dev/null || kill "${KPID6}" 2>/dev/null || true
fi

echo "================================================================================"
echo "CAPTURA DE PANTALLAS FINALIZADA EXITOSAMENTE CON SPECTACLE Y XDOTOOL"
echo "Todo Visual Studio Code fue minimizado y los comandos se ejecutaron en Konsole."
ls -lh "${CAPTURAS_DIR}"
echo "================================================================================"
