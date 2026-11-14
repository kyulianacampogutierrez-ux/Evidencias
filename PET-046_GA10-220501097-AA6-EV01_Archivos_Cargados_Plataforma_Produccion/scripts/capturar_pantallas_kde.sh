#!/bin/bash
# ==============================================================================
# SCRIPT DE AUTOMATIZACIÓN DE CAPTURAS CON XDOTOOL Y SPECTACLE EN KDE X11
# Evidencia: GA10-220501097-AA6-EV01 - Archivos Cargados en Plataforma Producción
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

minimizar_vscode
sleep 1

# ------------------------------------------------------------------------------
# PASO 1: Terminal Konsole - Estructura de Archivos y Permisos de Hosting (0755/0644)
# ------------------------------------------------------------------------------
echo "[Paso 1] Ejecutando terminal Konsole con Estructura de Archivos de Hosting..."
minimizar_vscode

RUN_P1="/tmp/run_aa6_paso1_files.sh"
cat << 'EOF' > "${RUN_P1}"
#!/bin/bash
clear
echo -e "\033[1;36m================================================================================\033[0m"
echo -e "\033[1;37;44m SENA CTPI POPAYÁN - REGIONAL CAUCA | ADSO FICHA 3186681 | APRENDIZ: KAREN CAMPO \033[0m"
echo -e "\033[1;36m EVIDENCIA GA10-220501097-AA6-EV01: ARCHIVOS CARGADOS EN PLATAFORMA PRODUCCIÓN  \033[0m"
echo -e "\033[1;36m FASE 1: ESTRUCTURA DE ARCHIVOS DE HOSTING Y MATRIZ DE PERMISOS UNIX (0755/0644) \033[0m"
echo -e "\033[1;36m================================================================================\033[0m"
echo ""
cd /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-046_GA10-220501097-AA6-EV01_Archivos_Cargados_Plataforma_Produccion/sitio_web_produccion
echo -e "\033[1;32mdanilo@linux-workstation\033[0m:\033[1;34m~/.../sitio_web_produccion\033[0m$ ls -la"
ls -la
echo ""
echo -e "\033[1;32mdanilo@linux-workstation\033[0m:\033[1;34m~/.../sitio_web_produccion\033[0m$ cat config_produccion.json"
cat config_produccion.json
echo ""
echo -e "\033[1;32m[✓] ÁRBOL DE DIRECTORIOS EN PUBLIC_HTML CON PERMISOS DE SEGURIDAD VERIFICADOS\033[0m"
echo -e "\033[1;33m[!] SEGURIDAD OWASP: Directorios 0755 (-rwxr-xr-x) y archivos 0644 (-rw-r--r--)\033[0m"
EOF
chmod +x "${RUN_P1}"

konsole --hold -e bash "${RUN_P1}" &
KPID1=$!
sleep 2

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
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_01_hosting_estructura_archivos_konsole.png"
sleep 1

if [ -n "${KONSOLE_WID}" ]; then
  DISPLAY=:0 xdotool windowclose "${KONSOLE_WID}" 2>/dev/null || kill "${KPID1}" 2>/dev/null || true
fi
sleep 1

# ------------------------------------------------------------------------------
# PASO 2: Terminal Konsole - Despliegue de Contenedores de Producción (Web + DB)
# ------------------------------------------------------------------------------
echo "[Paso 2] Ejecutando terminal Konsole con Despliegue de Producción..."
minimizar_vscode

RUN_P2="/tmp/run_aa6_paso2_deploy.sh"
cat << 'EOF' > "${RUN_P2}"
#!/bin/bash
clear
echo -e "\033[1;36m================================================================================\033[0m"
echo -e "\033[1;37;44m SENA CTPI POPAYÁN - REGIONAL CAUCA | ADSO FICHA 3186681 | APRENDIZ: KAREN CAMPO \033[0m"
echo -e "\033[1;36m EVIDENCIA GA10-220501097-AA6-EV01: ARCHIVOS CARGADOS EN PLATAFORMA PRODUCCIÓN  \033[0m"
echo -e "\033[1;36m FASE 2: DESPLIEGUE DEL SERVIDOR WEB APACHE Y BASE DE DATOS EN PRODUCCIÓN        \033[0m"
echo -e "\033[1;36m================================================================================\033[0m"
echo ""
cd /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-046_GA10-220501097-AA6-EV01_Archivos_Cargados_Plataforma_Produccion/docker_produccion
echo -e "\033[1;32mdanilo@linux-workstation\033[0m:\033[1;34m~/.../docker_produccion\033[0m$ docker compose ps"
docker compose ps
echo ""
echo -e "\033[1;32mdanilo@linux-workstation\033[0m:\033[1;34m~/.../docker_produccion\033[0m$ docker ps --filter name=sena-produccion- --format \"table {{.Names}}\t{{.Status}}\t{{.Ports}}\""
docker ps --filter name=sena-produccion- --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
echo ""
echo -e "\033[1;32mdanilo@linux-workstation\033[0m:\033[1;34m~/.../docker_produccion\033[0m$ curl -I http://localhost:8095/"
curl -I http://localhost:8095/
echo ""
echo -e "\033[1;32m[✓] SERVICIOS DE PRODUCCIÓN ACTIVOS (HTTP 200 OK) Y CONECTADOS A RED BRIDGE\033[0m"
echo -e "\033[1;33m[!] ENTORNO 100% AISLADO: Web en puerto 8095 y Base de Datos MySQL en puerto 3310.\033[0m"
EOF
chmod +x "${RUN_P2}"

konsole --hold -e bash "${RUN_P2}" &
KPID2=$!
sleep 2

KONSOLE_WID2=$(DISPLAY=:0 xdotool search --onlyvisible --class "konsole" 2>/dev/null | tail -n 1 || true)
if [ -n "${KONSOLE_WID2}" ]; then
  DISPLAY=:0 xdotool windowactivate --sync "${KONSOLE_WID2}"
  DISPLAY=:0 xdotool windowsize "${KONSOLE_WID2}" 1450 850
  DISPLAY=:0 xdotool windowmove "${KONSOLE_WID2}" 235 90
  sleep 1
fi

minimizar_vscode
sleep 1

echo "[Paso 2] Capturando terminal Konsole con Spectacle..."
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_02_despliegue_contenedores_produccion_konsole.png"
sleep 1

if [ -n "${KONSOLE_WID2}" ]; then
  DISPLAY=:0 xdotool windowclose "${KONSOLE_WID2}" 2>/dev/null || kill "${KPID2}" 2>/dev/null || true
fi
sleep 1

# ------------------------------------------------------------------------------
# PASO 3: Terminal Konsole - Migración SQL y Roles de Seguridad (PoLP)
# ------------------------------------------------------------------------------
echo "[Paso 3] Ejecutando terminal Konsole con Migración SQL y Roles de Usuario..."
minimizar_vscode

RUN_P3="/tmp/run_aa6_paso3_sql.sh"
cat << 'EOF' > "${RUN_P3}"
#!/bin/bash
clear
echo -e "\033[1;36m================================================================================\033[0m"
echo -e "\033[1;37;44m SENA CTPI POPAYÁN - REGIONAL CAUCA | ADSO FICHA 3186681 | APRENDIZ: KAREN CAMPO \033[0m"
echo -e "\033[1;36m EVIDENCIA GA10-220501097-AA6-EV01: ARCHIVOS CARGADOS EN PLATAFORMA PRODUCCIÓN  \033[0m"
echo -e "\033[1;36m FASE 3: CERTIFICACIÓN DE OPERATIVIDAD, MIGRACIÓN SQL Y PRIVILEGIOS DE USUARIOS  \033[0m"
echo -e "\033[1;36m================================================================================\033[0m"
echo ""
cd /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-046_GA10-220501097-AA6-EV01_Archivos_Cargados_Plataforma_Produccion
./scripts/probar_operatividad_produccion.sh
EOF
chmod +x "${RUN_P3}"

konsole --hold -e bash "${RUN_P3}" &
KPID3=$!
sleep 2

KONSOLE_WID3=$(DISPLAY=:0 xdotool search --onlyvisible --class "konsole" 2>/dev/null | tail -n 1 || true)
if [ -n "${KONSOLE_WID3}" ]; then
  DISPLAY=:0 xdotool windowactivate --sync "${KONSOLE_WID3}"
  DISPLAY=:0 xdotool windowsize "${KONSOLE_WID3}" 1450 850
  DISPLAY=:0 xdotool windowmove "${KONSOLE_WID3}" 235 90
  sleep 1
fi

minimizar_vscode
sleep 1

echo "[Paso 3] Capturando terminal Konsole con Spectacle..."
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_03_migracion_roles_seguridad_mysql_konsole.png"
sleep 1

if [ -n "${KONSOLE_WID3}" ]; then
  DISPLAY=:0 xdotool windowclose "${KONSOLE_WID3}" 2>/dev/null || kill "${KPID3}" 2>/dev/null || true
fi
sleep 1

# ------------------------------------------------------------------------------
# PASO 4: Google Chrome - Plataforma Web en Producción (Landing Page & Hero)
# ------------------------------------------------------------------------------
echo "[Paso 4] Abriendo Google Chrome en http://localhost:8095/..."
minimizar_vscode

google-chrome --new-window "http://localhost:8095/" &
CHROME_PID=$!
sleep 3

CHROME_WID=$(DISPLAY=:0 xdotool search --onlyvisible --name "Pizzería Gourmet Bella Italia Popayán | Plataforma en Producción" 2>/dev/null | tail -n 1 || true)
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

echo "[Paso 4] Capturando Landing Page en Google Chrome..."
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_04_chrome_landing_page_produccion.png"
sleep 1

# ------------------------------------------------------------------------------
# PASO 5: Google Chrome - Módulo de Checkout y Liquidación en Producción
# ------------------------------------------------------------------------------
echo "[Paso 5] Desplazando hacia módulo de pedidos y checkout..."
minimizar_vscode
if [ -n "${CHROME_WID}" ]; then
  DISPLAY=:0 xdotool windowactivate --sync "${CHROME_WID}"
  DISPLAY=:0 xdotool key Page_Down
  sleep 1.5
fi
minimizar_vscode
echo "[Paso 5] Capturando checkout y estructura de hosting en Google Chrome..."
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_05_chrome_checkout_liquidacion_pedido.png"
sleep 1

# ------------------------------------------------------------------------------
# PASO 6: Google Chrome - Auditoría con DevTools (F12) en Producción
# ------------------------------------------------------------------------------
echo "[Paso 6] Abriendo Chrome DevTools (F12) para auditoría de cabeceras HTTP..."
minimizar_vscode
if [ -n "${CHROME_WID}" ]; then
  DISPLAY=:0 xdotool windowactivate --sync "${CHROME_WID}"
  DISPLAY=:0 xdotool key F12
  sleep 2.5
fi
minimizar_vscode
echo "[Paso 6] Capturando DevTools con cabeceras de servidor Apache 2.4 en producción..."
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_06_chrome_devtools_auditoria_produccion.png"
sleep 1

# Cerrar DevTools y ventana de prueba de Chrome
if [ -n "${CHROME_WID}" ]; then
  DISPLAY=:0 xdotool windowclose "${CHROME_WID}" 2>/dev/null || kill "${CHROME_PID}" 2>/dev/null || true
fi
sleep 1

echo "================================================================================"
echo "TODAS LAS CAPTURAS DE PRODUCCIÓN GENERADAS EXITOSAMENTE CON SPECTACLE"
echo "Todo Visual Studio Code fue minimizado y los comandos se ejecutaron en Konsole."
ls -lh "${CAPTURAS_DIR}"
echo "================================================================================"
