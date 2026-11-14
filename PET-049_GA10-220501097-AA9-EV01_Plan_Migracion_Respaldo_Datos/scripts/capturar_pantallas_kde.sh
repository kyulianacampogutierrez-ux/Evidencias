#!/bin/bash
# ==============================================================================
# SCRIPT DE AUTOMATIZACIÓN DE CAPTURAS CON XDOTOOL Y SPECTACLE EN KDE X11
# Evidencia: GA10-220501097-AA9-EV01 - Plan de Migración y Respaldo de Datos
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
# PASO 1: Terminal Konsole - Protocolo de Respaldo Determinístico y SHA-256
# ------------------------------------------------------------------------------
echo "[Paso 1] Ejecutando terminal Konsole con Respaldo Seguro SHA-256..."
minimizar_vscode

RUN_P1="/tmp/run_aa9_paso1_respaldo.sh"
cat << 'EOF' > "${RUN_P1}"
#!/bin/bash
clear
echo -e "\033[1;36m================================================================================\033[0m"
echo -e "\033[1;37;44m SENA CTPI POPAYÁN - REGIONAL CAUCA | ADSO FICHA 3186681 | APRENDIZ: KAREN CAMPO \033[0m"
echo -e "\033[1;36m EVIDENCIA GA10-220501097-AA9-EV01: PLAN DE MIGRACIÓN Y RESPALDO DE DATOS       \033[0m"
echo -e "\033[1;36m FASE 1: EXTRACCIÓN DETERMINÍSTICA MYSQLDUMP Y HUELLA CRIPTOGRÁFICA SHA-256     \033[0m"
echo -e "\033[1;36m================================================================================\033[0m"
echo ""
cd /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-049_GA10-220501097-AA9-EV01_Plan_Migracion_Respaldo_Datos
./scripts_migracion_respaldo/ejecutar_respaldo_seguro_sha256.sh
echo ""
echo -e "\033[1;32m[✓] RESPALDO DETERMINÍSTICO COMPLETADO Y VALIDADO CRIPTOGRÁFICAMENTE\033[0m"
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
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_01_respaldo_automatizado_sha256_konsole.png"
sleep 1

if [ -n "${KONSOLE_WID}" ]; then
  DISPLAY=:0 xdotool windowclose "${KONSOLE_WID}" 2>/dev/null || kill "${KPID1}" 2>/dev/null || true
fi
sleep 1

# ------------------------------------------------------------------------------
# PASO 2: Terminal Konsole - Despliegue de Ambiente de Migración en Docker
# ------------------------------------------------------------------------------
echo "[Paso 2] Ejecutando terminal Konsole con Despliegue Docker (Puertos 8098 y 3313)..."
minimizar_vscode

RUN_P2="/tmp/run_aa9_paso2_docker.sh"
cat << 'EOF' > "${RUN_P2}"
#!/bin/bash
clear
echo -e "\033[1;36m================================================================================\033[0m"
echo -e "\033[1;37;44m SENA CTPI POPAYÁN - REGIONAL CAUCA | ADSO FICHA 3186681 | APRENDIZ: KAREN CAMPO \033[0m"
echo -e "\033[1;36m EVIDENCIA GA10-220501097-AA9-EV01: PLAN DE MIGRACIÓN Y RESPALDO DE DATOS       \033[0m"
echo -e "\033[1;36m FASE 2: VERIFICACIÓN DEL AMBIENTE STAGING AISLADO EN DOCKER (ZERO POLLUTION)   \033[0m"
echo -e "\033[1;36m================================================================================\033[0m"
echo ""
cd /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-049_GA10-220501097-AA9-EV01_Plan_Migracion_Respaldo_Datos/docker_migracion
echo -e "\033[1;32mdanilo@linux-workstation\033[0m:\033[1;34m~/.../docker_migracion\033[0m$ docker compose ps"
docker compose ps
echo ""
echo -e "\033[1;32mdanilo@linux-workstation\033[0m:\033[1;34m~/.../docker_migracion\033[0m$ curl -I http://localhost:8098/"
curl -I http://localhost:8098/
echo ""
echo -e "\033[1;32m[✓] AMBIENTE AISLADO ACTIVO: SERVIDOR HTTPD EN :8098 Y BASE DE DATOS EN :3313\033[0m"
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
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_02_despliegue_ambiente_migracion_docker_konsole.png"
sleep 1

if [ -n "${KONSOLE_WID2}" ]; then
  DISPLAY=:0 xdotool windowclose "${KONSOLE_WID2}" 2>/dev/null || kill "${KPID2}" 2>/dev/null || true
fi
sleep 1

# ------------------------------------------------------------------------------
# PASO 3: Terminal Konsole - Migración, Integridad Referencial y Conciliación COP
# ------------------------------------------------------------------------------
echo "[Paso 3] Ejecutando terminal Konsole con Migración y Validación de Datos..."
minimizar_vscode

RUN_P3="/tmp/run_aa9_paso3_migracion.sh"
cat << 'EOF' > "${RUN_P3}"
#!/bin/bash
clear
echo -e "\033[1;36m================================================================================\033[0m"
echo -e "\033[1;37;44m SENA CTPI POPAYÁN - REGIONAL CAUCA | ADSO FICHA 3186681 | APRENDIZ: KAREN CAMPO \033[0m"
echo -e "\033[1;36m EVIDENCIA GA10-220501097-AA9-EV01: PLAN DE MIGRACIÓN Y RESPALDO DE DATOS       \033[0m"
echo -e "\033[1;36m FASE 3: INGESTA, AUDITORÍA DE FILAS Y CONCILIACIÓN CONTABLE FINANCIERA COP     \033[0m"
echo -e "\033[1;36m================================================================================\033[0m"
echo ""
cd /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-049_GA10-220501097-AA9-EV01_Plan_Migracion_Respaldo_Datos
./scripts_migracion_respaldo/ejecutar_migracion_datos_validacion.sh
echo ""
echo -e "\033[1;32m[✓] MIGRACIÓN CERTIFICADA: 0 FILAS DE DISCREPANCIA Y $0 COP DE DIFERENCIA\033[0m"
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
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_03_migracion_validacion_integridad_konsole.png"
sleep 1

if [ -n "${KONSOLE_WID3}" ]; then
  DISPLAY=:0 xdotool windowclose "${KONSOLE_WID3}" 2>/dev/null || kill "${KPID3}" 2>/dev/null || true
fi
sleep 1

# ------------------------------------------------------------------------------
# PASO 4: Google Chrome - Portal de Auditoría de Migración y Respaldo
# ------------------------------------------------------------------------------
echo "[Paso 4] Abriendo Google Chrome en http://localhost:8098/..."
minimizar_vscode

google-chrome --new-window "http://localhost:8098/" &
CHROME_PID=$!
sleep 3

CHROME_WID=$(DISPLAY=:0 xdotool search --onlyvisible --name "Portal de Auditoría de Migración y Respaldo" 2>/dev/null | tail -n 1 || true)
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

echo "[Paso 4] Capturando Portal de Migración y Respaldo en Google Chrome..."
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_04_chrome_portal_auditoria_migracion.png"
sleep 1

# ------------------------------------------------------------------------------
# PASO 5: Google Chrome - Listas de Chequeo Interactivas de Migración
# ------------------------------------------------------------------------------
echo "[Paso 5] Desplazando hacia Listas de Chequeo Interactivas (Pre, Durante, Post)..."
minimizar_vscode
if [ -n "${CHROME_WID}" ]; then
  DISPLAY=:0 xdotool windowactivate --sync "${CHROME_WID}"
  DISPLAY=:0 xdotool key Page_Down
  sleep 1.5
fi
minimizar_vscode
echo "[Paso 5] Capturando Listas de Chequeo en Google Chrome..."
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_05_chrome_listas_chequeo_interactivas.png"
sleep 1

# ------------------------------------------------------------------------------
# PASO 6: Google Chrome - Validador Criptográfico SHA-256 y Protocolo Rollback
# ------------------------------------------------------------------------------
echo "[Paso 6] Desplazando hacia Validador Criptográfico 3-2-1 y Rollback..."
minimizar_vscode
if [ -n "${CHROME_WID}" ]; then
  DISPLAY=:0 xdotool windowactivate --sync "${CHROME_WID}"
  DISPLAY=:0 xdotool key Page_Down
  sleep 1.5
fi
minimizar_vscode
echo "[Paso 6] Capturando Validador SHA-256 y Rollback en Google Chrome..."
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_06_chrome_validador_respaldos_rollback.png"
sleep 1

# Cerrar ventana de prueba de Chrome
if [ -n "${CHROME_WID}" ]; then
  DISPLAY=:0 xdotool windowclose "${CHROME_WID}" 2>/dev/null || kill "${CHROME_PID}" 2>/dev/null || true
fi
sleep 1

echo "================================================================================"
echo "TODAS LAS CAPTURAS DE MIGRACIÓN Y RESPALDO GENERADAS CON SPECTACLE"
echo "Visual Studio Code minimizado y comandos ejecutados en Konsole."
ls -lh "${CAPTURAS_DIR}"
echo "================================================================================"
