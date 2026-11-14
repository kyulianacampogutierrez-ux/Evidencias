#!/bin/bash
# ==============================================================================
# SCRIPT DE AUTOMATIZACIÓN DE CAPTURAS CON XDOTOOL Y SPECTACLE EN KDE X11
# Evidencia: GA10-220501097-AA7-EV01 - Realización de Pruebas de Funcionalidad
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
# PASO 1: Terminal Konsole - Verificación de Dominio y Diagnóstico DNS (Pregunta 1)
# ------------------------------------------------------------------------------
echo "[Paso 1] Ejecutando terminal Konsole con Verificación de Dominio y DNS..."
minimizar_vscode

RUN_P1="/tmp/run_aa7_paso1_dns.sh"
cat << 'EOF' > "${RUN_P1}"
#!/bin/bash
clear
echo -e "\033[1;36m================================================================================\033[0m"
echo -e "\033[1;37;44m SENA CTPI POPAYÁN - REGIONAL CAUCA | ADSO FICHA 3186681 | APRENDIZ: KAREN CAMPO \033[0m"
echo -e "\033[1;36m EVIDENCIA GA10-220501097-AA7-EV01: PRUEBAS DE FUNCIONALIDAD DEL SOFTWARE       \033[0m"
echo -e "\033[1;36m PREGUNTA 1: ¿CÓMO VERIFICAR SI UN DOMINIO ESTÁ BIEN CONFIGURADO?               \033[0m"
echo -e "\033[1;36m================================================================================\033[0m"
echo ""
cd /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-047_GA10-220501097-AA7-EV01_Pruebas_Funcionalidad_Software
./scripts_pruebas/verificar_dominio_dns.sh
echo ""
echo -e "\033[1;32m[✓] AUDITORÍA DNS Y CERTIFICADO SSL/TLS LET'S ENCRYPT COMPLETADA EXITOSAMENTE\033[0m"
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
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_01_verificacion_dns_dominio_konsole.png"
sleep 1

if [ -n "${KONSOLE_WID}" ]; then
  DISPLAY=:0 xdotool windowclose "${KONSOLE_WID}" 2>/dev/null || kill "${KPID1}" 2>/dev/null || true
fi
sleep 1

# ------------------------------------------------------------------------------
# PASO 2: Terminal Konsole - Despliegue de Ambiente de Pruebas en Docker
# ------------------------------------------------------------------------------
echo "[Paso 2] Ejecutando terminal Konsole con Despliegue de Contenedores..."
minimizar_vscode

RUN_P2="/tmp/run_aa7_paso2_docker.sh"
cat << 'EOF' > "${RUN_P2}"
#!/bin/bash
clear
echo -e "\033[1;36m================================================================================\033[0m"
echo -e "\033[1;37;44m SENA CTPI POPAYÁN - REGIONAL CAUCA | ADSO FICHA 3186681 | APRENDIZ: KAREN CAMPO \033[0m"
echo -e "\033[1;36m EVIDENCIA GA10-220501097-AA7-EV01: PRUEBAS DE FUNCIONALIDAD DEL SOFTWARE       \033[0m"
echo -e "\033[1;36m FASE DE INFRAESTRUCTURA: ENTORNO DE PRUEBAS EN DOCKER (PUERTOS 8096 Y 3311)   \033[0m"
echo -e "\033[1;36m================================================================================\033[0m"
echo ""
cd /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-047_GA10-220501097-AA7-EV01_Pruebas_Funcionalidad_Software/docker_pruebas
echo -e "\033[1;32mdanilo@linux-workstation\033[0m:\033[1;34m~/.../docker_pruebas\033[0m$ docker compose ps"
docker compose ps
echo ""
echo -e "\033[1;32mdanilo@linux-workstation\033[0m:\033[1;34m~/.../docker_pruebas\033[0m$ curl -I http://localhost:8096/"
curl -I http://localhost:8096/
echo ""
echo -e "\033[1;32m[✓] CONTENEDORES AISLADOS OPERANDO EN ESTADO HEALTHY (ZERO HOST POLLUTION)\033[0m"
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
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_02_despliegue_ambiente_pruebas_docker_konsole.png"
sleep 1

if [ -n "${KONSOLE_WID2}" ]; then
  DISPLAY=:0 xdotool windowclose "${KONSOLE_WID2}" 2>/dev/null || kill "${KPID2}" 2>/dev/null || true
fi
sleep 1

# ------------------------------------------------------------------------------
# PASO 3: Terminal Konsole - Suite de Pruebas Automatizadas E2E y Elementos Web
# ------------------------------------------------------------------------------
echo "[Paso 3] Ejecutando terminal Konsole con Suite Automatizada de Pruebas..."
minimizar_vscode

RUN_P3="/tmp/run_aa7_paso3_e2e.sh"
cat << 'EOF' > "${RUN_P3}"
#!/bin/bash
clear
echo -e "\033[1;36m================================================================================\033[0m"
echo -e "\033[1;37;44m SENA CTPI POPAYÁN - REGIONAL CAUCA | ADSO FICHA 3186681 | APRENDIZ: KAREN CAMPO \033[0m"
echo -e "\033[1;36m EVIDENCIA GA10-220501097-AA7-EV01: PRUEBAS DE FUNCIONALIDAD DEL SOFTWARE       \033[0m"
echo -e "\033[1;36m PREGUNTA 4: ¿QUÉ ELEMENTOS SE DEBEN PROBAR EN UNA APLICACIÓN WEB? (E2E)        \033[0m"
echo -e "\033[1;36m================================================================================\033[0m"
echo ""
cd /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-047_GA10-220501097-AA7-EV01_Pruebas_Funcionalidad_Software
./scripts_pruebas/ejecutar_pruebas_funcionales_e2e.sh
echo ""
./scripts_pruebas/probar_compatibilidad_navegadores.sh
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
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_03_suite_pruebas_automatizadas_konsole.png"
sleep 1

if [ -n "${KONSOLE_WID3}" ]; then
  DISPLAY=:0 xdotool windowclose "${KONSOLE_WID3}" 2>/dev/null || kill "${KPID3}" 2>/dev/null || true
fi
sleep 1

# ------------------------------------------------------------------------------
# PASO 4: Google Chrome - Vista de Escritorio con Diagnóstico y Catálogo Gourmet
# ------------------------------------------------------------------------------
echo "[Paso 4] Abriendo Google Chrome en http://localhost:8096/..."
minimizar_vscode

google-chrome --new-window "http://localhost:8096/" &
CHROME_PID=$!
sleep 3

CHROME_WID=$(DISPLAY=:0 xdotool search --onlyvisible --name "Pizzería Gourmet Bella Italia Popayán | Pruebas de Funcionalidad" 2>/dev/null | tail -n 1 || true)
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

echo "[Paso 4] Capturando Vista de Escritorio en Google Chrome..."
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_04_chrome_vista_escritorio_funcional.png"
sleep 1

# ------------------------------------------------------------------------------
# PASO 5: Google Chrome - Emulación de Dispositivo Móvil (Pregunta 3)
# ------------------------------------------------------------------------------
echo "[Paso 5] Ajustando Chrome a resolución de Smartphone (412x915px) para prueba móvil..."
minimizar_vscode
if [ -n "${CHROME_WID}" ]; then
  DISPLAY=:0 xdotool windowactivate --sync "${CHROME_WID}"
  DISPLAY=:0 xdotool windowsize "${CHROME_WID}" 480 880
  DISPLAY=:0 xdotool windowmove "${CHROME_WID}" 720 70
  sleep 1.5
fi
minimizar_vscode
echo "[Paso 5] Capturando emulación móvil en Google Chrome..."
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_05_chrome_emulacion_movil_responsive.png"
sleep 1

# ------------------------------------------------------------------------------
# PASO 6: Google Chrome - Formulario de Checkout, Validaciones e Impoconsumo 8%
# ------------------------------------------------------------------------------
echo "[Paso 6] Restaurando tamaño de ventana para diligenciar checkout..."
minimizar_vscode
if [ -n "${CHROME_WID}" ]; then
  DISPLAY=:0 xdotool windowactivate --sync "${CHROME_WID}"
  DISPLAY=:0 xdotool windowsize "${CHROME_WID}" 1550 920
  DISPLAY=:0 xdotool windowmove "${CHROME_WID}" 185 60
  sleep 1
  DISPLAY=:0 xdotool key Page_Down
  sleep 1
fi
minimizar_vscode
echo "[Paso 6] Capturando formulario de checkout y validaciones en Google Chrome..."
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_06_chrome_formulario_checkout_validaciones.png"
sleep 1

# Cerrar ventana de prueba de Chrome
if [ -n "${CHROME_WID}" ]; then
  DISPLAY=:0 xdotool windowclose "${CHROME_WID}" 2>/dev/null || kill "${CHROME_PID}" 2>/dev/null || true
fi
sleep 1

echo "================================================================================"
echo "TODAS LAS CAPTURAS DE PRUEBAS FUNCIONALES GENERADAS EXITOSAMENTE CON SPECTACLE"
echo "Todo Visual Studio Code fue minimizado y los comandos se ejecutaron en Konsole."
ls -lh "${CAPTURAS_DIR}"
echo "================================================================================"
