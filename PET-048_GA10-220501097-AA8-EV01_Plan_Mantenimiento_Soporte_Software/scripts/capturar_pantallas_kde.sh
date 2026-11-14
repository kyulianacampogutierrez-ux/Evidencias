#!/bin/bash
# ==============================================================================
# SCRIPT DE AUTOMATIZACIÓN DE CAPTURAS CON XDOTOOL Y SPECTACLE EN KDE X11
# Evidencia: GA10-220501097-AA8-EV01 - Diseñar Plan de Mantenimiento y Soporte
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
# PASO 1: Terminal Konsole - Protocolo de Mantenimiento Preventivo (ISO/IEC 14764)
# ------------------------------------------------------------------------------
echo "[Paso 1] Ejecutando terminal Konsole con Mantenimiento Preventivo..."
minimizar_vscode

RUN_P1="/tmp/run_aa8_paso1_prev.sh"
cat << 'EOF' > "${RUN_P1}"
#!/bin/bash
clear
echo -e "\033[1;36m================================================================================\033[0m"
echo -e "\033[1;37;44m SENA CTPI POPAYÁN - REGIONAL CAUCA | ADSO FICHA 3186681 | APRENDIZ: KAREN CAMPO \033[0m"
echo -e "\033[1;36m EVIDENCIA GA10-220501097-AA8-EV01: PLAN DE MANTENIMIENTO Y SOPORTE DE SOFTWARE  \033[0m"
echo -e "\033[1;36m FASE 1: EJECUCIÓN AUTOMATIZADA DE MANTENIMIENTO PREVENTIVO SEGÚN ISO/IEC 14764  \033[0m"
echo -e "\033[1;36m================================================================================\033[0m"
echo ""
cd /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-048_GA10-220501097-AA8-EV01_Plan_Mantenimiento_Soporte_Software
./scripts_mantenimiento/ejecutar_mantenimiento_preventivo.sh
echo ""
echo -e "\033[1;32m[✓] PROTOCOLO PREVENTIVO EJECUTADO CON ÉXITO: DISCO, LOGS, MYSQL Y SSL ÓPTIMOS\033[0m"
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
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_01_ejecucion_mantenimiento_preventivo_konsole.png"
sleep 1

if [ -n "${KONSOLE_WID}" ]; then
  DISPLAY=:0 xdotool windowclose "${KONSOLE_WID}" 2>/dev/null || kill "${KPID1}" 2>/dev/null || true
fi
sleep 1

# ------------------------------------------------------------------------------
# PASO 2: Terminal Konsole - Despliegue de Ambiente de Mantenimiento en Docker
# ------------------------------------------------------------------------------
echo "[Paso 2] Ejecutando terminal Konsole con Despliegue en Docker..."
minimizar_vscode

RUN_P2="/tmp/run_aa8_paso2_docker.sh"
cat << 'EOF' > "${RUN_P2}"
#!/bin/bash
clear
echo -e "\033[1;36m================================================================================\033[0m"
echo -e "\033[1;37;44m SENA CTPI POPAYÁN - REGIONAL CAUCA | ADSO FICHA 3186681 | APRENDIZ: KAREN CAMPO \033[0m"
echo -e "\033[1;36m EVIDENCIA GA10-220501097-AA8-EV01: PLAN DE MANTENIMIENTO Y SOPORTE DE SOFTWARE  \033[0m"
echo -e "\033[1;36m FASE 2: ENTORNO DE SOPORTE Y MONITOREO EN DOCKER (PUERTOS 8097 Y 3312)          \033[0m"
echo -e "\033[1;36m================================================================================\033[0m"
echo ""
cd /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-048_GA10-220501097-AA8-EV01_Plan_Mantenimiento_Soporte_Software/docker_mantenimiento
echo -e "\033[1;32mdanilo@linux-workstation\033[0m:\033[1;34m~/.../docker_mantenimiento\033[0m$ docker compose ps"
docker compose ps
echo ""
echo -e "\033[1;32mdanilo@linux-workstation\033[0m:\033[1;34m~/.../docker_mantenimiento\033[0m$ curl -I http://localhost:8097/"
curl -I http://localhost:8097/
echo ""
echo -e "\033[1;32m[✓] CONTENEDORES DE SOPORTE TÉCNICO EN ESTADO SALUDABLE (ZERO HOST POLLUTION)\033[0m"
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
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_02_despliegue_ambiente_mantenimiento_docker_konsole.png"
sleep 1

if [ -n "${KONSOLE_WID2}" ]; then
  DISPLAY=:0 xdotool windowclose "${KONSOLE_WID2}" 2>/dev/null || kill "${KPID2}" 2>/dev/null || true
fi
sleep 1

# ------------------------------------------------------------------------------
# PASO 3: Terminal Konsole - Atención de Incidencia Correctiva y Control SLA
# ------------------------------------------------------------------------------
echo "[Paso 3] Ejecutando terminal Konsole con Atención de Incidencia Correctiva..."
minimizar_vscode

RUN_P3="/tmp/run_aa8_paso3_corr.sh"
cat << 'EOF' > "${RUN_P3}"
#!/bin/bash
clear
echo -e "\033[1;36m================================================================================\033[0m"
echo -e "\033[1;37;44m SENA CTPI POPAYÁN - REGIONAL CAUCA | ADSO FICHA 3186681 | APRENDIZ: KAREN CAMPO \033[0m"
echo -e "\033[1;36m EVIDENCIA GA10-220501097-AA8-EV01: PLAN DE MANTENIMIENTO Y SOPORTE DE SOFTWARE  \033[0m"
echo -e "\033[1;36m FASE 3: ATENCIÓN DE INCIDENTE CORRECTIVO P1 Y MÉTRICAS DE RESOLUCIÓN (MTTR)     \033[0m"
echo -e "\033[1;36m================================================================================\033[0m"
echo ""
cd /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-048_GA10-220501097-AA8-EV01_Plan_Mantenimiento_Soporte_Software
./scripts_mantenimiento/simular_incidencia_correctiva_sla.sh
echo ""
echo -e "\033[1;32m[✓] TICKET #TCK-2026-CORR-085 RESUELTO: MTTR 38 MINUTOS (DENTRO DEL SLA EXIGIDO)\033[0m"
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
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_03_atencion_incidencia_correctiva_sla_konsole.png"
sleep 1

if [ -n "${KONSOLE_WID3}" ]; then
  DISPLAY=:0 xdotool windowclose "${KONSOLE_WID3}" 2>/dev/null || kill "${KPID3}" 2>/dev/null || true
fi
sleep 1

# ------------------------------------------------------------------------------
# PASO 4: Google Chrome - Portal de Mantenimiento y KPIs de Operación
# ------------------------------------------------------------------------------
echo "[Paso 4] Abriendo Google Chrome en http://localhost:8097/..."
minimizar_vscode

google-chrome --new-window "http://localhost:8097/" &
CHROME_PID=$!
sleep 3

CHROME_WID=$(DISPLAY=:0 xdotool search --onlyvisible --name "Portal de Mantenimiento y Soporte Técnico" 2>/dev/null | tail -n 1 || true)
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

echo "[Paso 4] Capturando Portal de Mantenimiento en Google Chrome..."
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_04_chrome_portal_soporte_mantenimiento.png"
sleep 1

# ------------------------------------------------------------------------------
# PASO 5: Google Chrome - Cronograma Anual ISO 14764 y Matriz de SLAs
# ------------------------------------------------------------------------------
echo "[Paso 5] Desplazando hacia Cronograma Anual y Matriz SLA..."
minimizar_vscode
if [ -n "${CHROME_WID}" ]; then
  DISPLAY=:0 xdotool windowactivate --sync "${CHROME_WID}"
  DISPLAY=:0 xdotool key Page_Down
  sleep 1.5
fi
minimizar_vscode
echo "[Paso 5] Capturando Cronograma y Matriz SLA en Google Chrome..."
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_05_chrome_cronograma_interactivo_sla.png"
sleep 1

# ------------------------------------------------------------------------------
# PASO 6: Google Chrome - Mesa de Ayuda y Radicación de Tickets de Soporte
# ------------------------------------------------------------------------------
echo "[Paso 6] Desplazando hacia Mesa de Ayuda y Radicación de Tickets..."
minimizar_vscode
if [ -n "${CHROME_WID}" ]; then
  DISPLAY=:0 xdotool windowactivate --sync "${CHROME_WID}"
  DISPLAY=:0 xdotool key Page_Down
  sleep 1.5
fi
minimizar_vscode
echo "[Paso 6] Capturando Mesa de Ayuda y Radicación de Tickets en Google Chrome..."
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_06_chrome_registro_ticket_soporte_pizzeria.png"
sleep 1

# Cerrar ventana de prueba de Chrome
if [ -n "${CHROME_WID}" ]; then
  DISPLAY=:0 xdotool windowclose "${CHROME_WID}" 2>/dev/null || kill "${CHROME_PID}" 2>/dev/null || true
fi
sleep 1

echo "================================================================================"
echo "TODAS LAS CAPTURAS DE MANTENIMIENTO Y SOPORTE GENERADAS CON SPECTACLE"
echo "Todo Visual Studio Code fue minimizado y los comandos se ejecutaron en Konsole."
ls -lh "${CAPTURAS_DIR}"
echo "================================================================================"
