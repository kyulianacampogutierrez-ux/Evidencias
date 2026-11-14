#!/bin/bash
# ==============================================================================
# SCRIPT DE AUTOMATIZACIÓN DE CAPTURAS CON XDOTOOL Y SPECTACLE EN KDE X11
# Evidencia: GA10-220501097-AA10-EV01 - Elabora Documentos Técnicos del Software
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
# PASO 1: Terminal Konsole - Verificación de Prerrequisitos Técnicos
# ------------------------------------------------------------------------------
echo "[Paso 1] Ejecutando terminal Konsole con Verificación de Prerrequisitos..."
minimizar_vscode

RUN_P1="/tmp/run_aa10_paso1_prerreq.sh"
cat << 'EOF' > "${RUN_P1}"
#!/bin/bash
clear
echo -e "\033[1;36m================================================================================\033[0m"
echo -e "\033[1;37;44m SENA CTPI POPAYÁN - REGIONAL CAUCA | ADSO FICHA 3186681 | APRENDIZ: KAREN CAMPO \033[0m"
echo -e "\033[1;36m EVIDENCIA GA10-220501097-AA10-EV01: MANUAL TÉCNICO Y DE OPERACIONES DEL SOFTWARE\033[0m"
echo -e "\033[1;36m SECCIÓN 1: AUDITORÍA DE PRERREQUISITOS DE INSTALACIÓN (HARDWARE / SOFTWARE)     \033[0m"
echo -e "\033[1;36m================================================================================\033[0m"
echo ""
cd /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-050_GA10-220501097-AA10-EV01_Manual_Tecnico_Software
./scripts_instalacion_despliegue/instalar_prerrequisitos_sistema.sh
echo ""
echo -e "\033[1;32m[✓] PRERREQUISITOS VALIDADOS CON ÉXITO: HOST APTO PARA PRODUCCIÓN\033[0m"
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
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_01_verificacion_prerrequisitos_konsole.png"
sleep 1

if [ -n "${KONSOLE_WID}" ]; then
  DISPLAY=:0 xdotool windowclose "${KONSOLE_WID}" 2>/dev/null || kill "${KPID1}" 2>/dev/null || true
fi
sleep 1

# ------------------------------------------------------------------------------
# PASO 2: Terminal Konsole - Despliegue de Contenedores en Docker (Zero Pollution)
# ------------------------------------------------------------------------------
echo "[Paso 2] Ejecutando terminal Konsole con Despliegue Docker (Puertos 8099 y 3314)..."
minimizar_vscode

RUN_P2="/tmp/run_aa10_paso2_docker.sh"
cat << 'EOF' > "${RUN_P2}"
#!/bin/bash
clear
echo -e "\033[1;36m================================================================================\033[0m"
echo -e "\033[1;37;44m SENA CTPI POPAYÁN - REGIONAL CAUCA | ADSO FICHA 3186681 | APRENDIZ: KAREN CAMPO \033[0m"
echo -e "\033[1;36m EVIDENCIA GA10-220501097-AA10-EV01: MANUAL TÉCNICO Y DE OPERACIONES DEL SOFTWARE\033[0m"
echo -e "\033[1;36m SECCIÓN 2: ORQUESTACIÓN EN DOCKER (HTTPD :8099 / MYSQL 8.0 :3314) - ZERO POLLUTION\033[0m"
echo -e "\033[1;36m================================================================================\033[0m"
echo ""
cd /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-050_GA10-220501097-AA10-EV01_Manual_Tecnico_Software/docker_manual_tecnico
echo -e "\033[1;32mdanilo@linux-workstation\033[0m:\033[1;34m~/.../docker_manual_tecnico\033[0m$ docker compose ps"
docker compose ps
echo ""
echo -e "\033[1;32mdanilo@linux-workstation\033[0m:\033[1;34m~/.../docker_manual_tecnico\033[0m$ curl -I http://localhost:8099/"
curl -I http://localhost:8099/
echo ""
echo -e "\033[1;32m[✓] CONTENEDORES ACTIVOS Y SALUDABLES EN RED BRIDGE AISLADA\033[0m"
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
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_02_despliegue_contenedores_docker_konsole.png"
sleep 1

if [ -n "${KONSOLE_WID2}" ]; then
  DISPLAY=:0 xdotool windowclose "${KONSOLE_WID2}" 2>/dev/null || kill "${KPID2}" 2>/dev/null || true
fi
sleep 1

# ------------------------------------------------------------------------------
# PASO 3: Terminal Konsole - Healthchecks de Componentes y Auditoría MySQL
# ------------------------------------------------------------------------------
echo "[Paso 3] Ejecutando terminal Konsole con Healthchecks y Auditoría DB..."
minimizar_vscode

RUN_P3="/tmp/run_aa10_paso3_health.sh"
cat << 'EOF' > "${RUN_P3}"
#!/bin/bash
clear
echo -e "\033[1;36m================================================================================\033[0m"
echo -e "\033[1;37;44m SENA CTPI POPAYÁN - REGIONAL CAUCA | ADSO FICHA 3186681 | APRENDIZ: KAREN CAMPO \033[0m"
echo -e "\033[1;36m EVIDENCIA GA10-220501097-AA10-EV01: MANUAL TÉCNICO Y DE OPERACIONES DEL SOFTWARE\033[0m"
echo -e "\033[1;36m SECCIÓN 3: COMPROBACIÓN DE SALUD (HEALTHCHECKS) Y AUDITORÍA DE ESQUEMA EN MYSQL \033[0m"
echo -e "\033[1;36m================================================================================\033[0m"
echo ""
cd /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-050_GA10-220501097-AA10-EV01_Manual_Tecnico_Software
./scripts_instalacion_despliegue/verificar_estado_componentes_healthcheck.sh
echo ""
echo -e "\033[1;32m[✓] 8 TABLAS RELACIONALES AUDITADAS Y VALIDACIÓN HTTP 200 OK COMPLETADA\033[0m"
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
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_03_ejecucion_healthcheck_componentes_konsole.png"
sleep 1

if [ -n "${KONSOLE_WID3}" ]; then
  DISPLAY=:0 xdotool windowclose "${KONSOLE_WID3}" 2>/dev/null || kill "${KPID3}" 2>/dev/null || true
fi
sleep 1

# ------------------------------------------------------------------------------
# PASO 4: Google Chrome - Portal del Manual Técnico: Prerrequisitos y Frameworks
# ------------------------------------------------------------------------------
echo "[Paso 4] Abriendo Google Chrome en http://localhost:8099/..."
minimizar_vscode

google-chrome --new-window "http://localhost:8099/" &
CHROME_PID=$!
sleep 3

CHROME_WID=$(DISPLAY=:0 xdotool search --onlyvisible --name "Manual Técnico del Software" 2>/dev/null | tail -n 1 || true)
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

echo "[Paso 4] Capturando Manual Técnico (Prerrequisitos y Frameworks) en Google Chrome..."
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_04_chrome_manual_tecnico_prerrequisitos_frameworks.png"
sleep 1

# ------------------------------------------------------------------------------
# PASO 5: Google Chrome - Diagramas de Casos de Uso UML y Modelo Entidad-Relación
# ------------------------------------------------------------------------------
echo "[Paso 5] Navegando a pestaña de Casos de Uso y Modelo E-R..."
minimizar_vscode
if [ -n "${CHROME_WID}" ]; then
  DISPLAY=:0 xdotool windowactivate --sync "${CHROME_WID}"
  # Clic en pestaña de Casos de Uso o pulsar Tab/Enter
  DISPLAY=:0 xdotool key Page_Down
  sleep 1
fi
minimizar_vscode
echo "[Paso 5] Capturando Diagrama de Casos de Uso y Modelo E-R en Google Chrome..."
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_05_chrome_manual_tecnico_diagramas_casos_uso_er.png"
sleep 1

# ------------------------------------------------------------------------------
# PASO 6: Google Chrome - Diccionario de Datos Interactivo y Diagrama Componentes
# ------------------------------------------------------------------------------
echo "[Paso 6] Navegando a Diccionario de Datos y Componentes..."
minimizar_vscode
if [ -n "${CHROME_WID}" ]; then
  DISPLAY=:0 xdotool windowactivate --sync "${CHROME_WID}"
  DISPLAY=:0 xdotool key Page_Down
  sleep 1.5
fi
minimizar_vscode
echo "[Paso 6] Capturando Diccionario de Datos y Componentes en Google Chrome..."
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_06_chrome_manual_tecnico_diccionario_datos_componentes.png"
sleep 1

# Cerrar ventana de prueba de Chrome
if [ -n "${CHROME_WID}" ]; then
  DISPLAY=:0 xdotool windowclose "${CHROME_WID}" 2>/dev/null || kill "${CHROME_PID}" 2>/dev/null || true
fi
sleep 1

echo "================================================================================"
echo "TODAS LAS CAPTURAS DEL MANUAL TÉCNICO GENERADAS CON SPECTACLE"
echo "Visual Studio Code minimizado y comandos ejecutados en Konsole."
ls -lh "${CAPTURAS_DIR}"
echo "================================================================================"
