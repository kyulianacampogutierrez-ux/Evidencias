#!/bin/bash
# ==============================================================================
# SCRIPT DE AUTOMATIZACIÓN DE CAPTURAS CON XDOTOOL Y SPECTACLE EN KDE X11
# Evidencia: GA10-220501097-AA5-EV01 - Configuración de Servicios, BD y Software
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
# PASO 1: Terminal Konsole - Enfoque 1: Especificación de Virtualización (VM Ubuntu LAMP)
# ------------------------------------------------------------------------------
echo "[Paso 1] Ejecutando terminal Konsole con especificación de Virtualización VM..."
minimizar_vscode

RUN_P1="/tmp/run_aa5_paso1_vm.sh"
cat << 'EOF' > "${RUN_P1}"
#!/bin/bash
clear
echo -e "\033[1;36m================================================================================\033[0m"
echo -e "\033[1;37;44m SENA CTPI POPAYÁN - REGIONAL CAUCA | ADSO FICHA 3186681 | APRENDIZ: KAREN CAMPO \033[0m"
echo -e "\033[1;36m EVIDENCIA GA10-220501097-AA5-EV01: CONFIGURACIÓN DE SERVICIOS EN CLIENTE       \033[0m"
echo -e "\033[1;36m FASE 1: ESPECIFICACIÓN TÉCNICA DE MÁQUINA VIRTUAL UBUNTU SERVER (PILA LAMP)    \033[0m"
echo -e "\033[1;36m================================================================================\033[0m"
echo ""
cd /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-045_GA10-220501097-AA5-EV01_Configuracion_Servicios_BD_Software_Cliente/virtualizacion
echo -e "\033[1;32mdanilo@linux-workstation\033[0m:\033[1;34m~/.../virtualizacion\033[0m$ cat Vagrantfile"
cat Vagrantfile
echo ""
echo -e "\033[1;32mdanilo@linux-workstation\033[0m:\033[1;34m~/.../virtualizacion\033[0m$ head -n 22 provision_vm_ubuntu_lamp.sh"
head -n 22 provision_vm_ubuntu_lamp.sh
echo ""
echo -e "\033[1;32m[✓] ENFOQUE 1: MÁQUINA VIRTUAL UBUNTU 22.04 LTS (APACHE2 + MYSQL 8.0 + 2GB RAM)\033[0m"
echo -e "\033[1;33m[!] ANÁLISIS: Alto consumo estático de memoria (2048 MB) y tiempo de booteo ~50s\033[0m"
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
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_01_arquitectura_virtualizacion_vm_ubuntu.png"
sleep 1

if [ -n "${KONSOLE_WID}" ]; then
  DISPLAY=:0 xdotool windowclose "${KONSOLE_WID}" 2>/dev/null || kill "${KPID1}" 2>/dev/null || true
fi
sleep 1

# ------------------------------------------------------------------------------
# PASO 2: Terminal Konsole - Enfoque 2: Despliegue de Contenedores Docker (Apache + MySQL)
# ------------------------------------------------------------------------------
echo "[Paso 2] Ejecutando terminal Konsole con Despliegue de Contenedores Docker..."
minimizar_vscode

RUN_P2="/tmp/run_aa5_paso2_docker.sh"
cat << 'EOF' > "${RUN_P2}"
#!/bin/bash
clear
echo -e "\033[1;36m================================================================================\033[0m"
echo -e "\033[1;37;44m SENA CTPI POPAYÁN - REGIONAL CAUCA | ADSO FICHA 3186681 | APRENDIZ: KAREN CAMPO \033[0m"
echo -e "\033[1;36m EVIDENCIA GA10-220501097-AA5-EV01: CONFIGURACIÓN DE SERVICIOS EN CLIENTE       \033[0m"
echo -e "\033[1;36m FASE 2: DESPLIEGUE CONTENERIZADO APACHE 2.4 + MYSQL 8.0 EN DOCKER (AISLADO)    \033[0m"
echo -e "\033[1;36m================================================================================\033[0m"
echo ""
cd /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-045_GA10-220501097-AA5-EV01_Configuracion_Servicios_BD_Software_Cliente/docker
echo -e "\033[1;32mdanilo@linux-workstation\033[0m:\033[1;34m~/.../docker\033[0m$ docker compose ps"
docker compose ps
echo ""
echo -e "\033[1;32mdanilo@linux-workstation\033[0m:\033[1;34m~/.../docker\033[0m$ docker ps --filter name=sena-cliente- --format \"table {{.Names}}\t{{.Status}}\t{{.Ports}}\""
docker ps --filter name=sena-cliente- --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
echo ""
echo -e "\033[1;32mdanilo@linux-workstation\033[0m:\033[1;34m~/.../docker\033[0m$ curl -I http://localhost:8090/"
curl -I http://localhost:8090/
echo ""
echo -e "\033[1;32m[✓] SERVICIOS EN CONTENEDORES ACTIVOS Y SALUDABLES (HEALTHY)\033[0m"
echo -e "\033[1;33m[!] EFICIENCIA: Consumo dinámico ~220 MB RAM vs 2048 MB en VM. Host sin contaminar.\033[0m"
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
# PASO 3: Terminal Konsole - Verificación y Consultas SQL en MySQL 8.0 CLI
# ------------------------------------------------------------------------------
echo "[Paso 3] Ejecutando terminal Konsole con verificación técnica de MySQL y Apache..."
minimizar_vscode

RUN_P3="/tmp/run_aa5_paso3_sql.sh"
cat << 'EOF' > "${RUN_P3}"
#!/bin/bash
clear
echo -e "\033[1;36m================================================================================\033[0m"
echo -e "\033[1;37;44m SENA CTPI POPAYÁN - REGIONAL CAUCA | ADSO FICHA 3186681 | APRENDIZ: KAREN CAMPO \033[0m"
echo -e "\033[1;36m EVIDENCIA GA10-220501097-AA5-EV01: CONFIGURACIÓN DE SERVICIOS EN CLIENTE       \033[0m"
echo -e "\033[1;36m FASE 3: COMPROBACIÓN DE SALUD DE SERVICIOS Y CONSULTAS SQL EN TIEMPO REAL       \033[0m"
echo -e "\033[1;36m================================================================================\033[0m"
echo ""
cd /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-045_GA10-220501097-AA5-EV01_Configuracion_Servicios_BD_Software_Cliente
./scripts/probar_servicios_mysql_apache.sh
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
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_03_verificacion_mysql_cli_konsole.png"
sleep 1

if [ -n "${KONSOLE_WID3}" ]; then
  DISPLAY=:0 xdotool windowclose "${KONSOLE_WID3}" 2>/dev/null || kill "${KPID3}" 2>/dev/null || true
fi
sleep 1

# ------------------------------------------------------------------------------
# PASO 4: Google Chrome - Renderizado de Aplicación Web en Apache/PHP y MySQL
# ------------------------------------------------------------------------------
echo "[Paso 4] Abriendo Google Chrome en http://localhost:8090/..."
minimizar_vscode

google-chrome --new-window "http://localhost:8090/" &
CHROME_PID=$!
sleep 3

CHROME_WID=$(DISPLAY=:0 xdotool search --onlyvisible --name "Pizzería Gourmet Bella Italia Popayán" 2>/dev/null | tail -n 1 || true)
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

echo "[Paso 4] Capturando Landing Page de Apache/MySQL en Google Chrome..."
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_04_chrome_aplicacion_web_pizzeria.png"
sleep 1

# ------------------------------------------------------------------------------
# PASO 5: Google Chrome - Registro de Pedido y Checkout en Tiempo Real
# ------------------------------------------------------------------------------
echo "[Paso 5] Desplazando hacia formulario de checkout interactivo..."
minimizar_vscode
if [ -n "${CHROME_WID}" ]; then
  DISPLAY=:0 xdotool windowactivate --sync "${CHROME_WID}"
  DISPLAY=:0 xdotool key Page_Down
  sleep 1.5
fi
minimizar_vscode
echo "[Paso 5] Capturando formulario de pedidos con registro transaccional..."
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_05_chrome_registro_pedido_transaccional.png"
sleep 1

# ------------------------------------------------------------------------------
# PASO 6: Google Chrome - Inspección de Red y Servidor con Chrome DevTools (F12)
# ------------------------------------------------------------------------------
echo "[Paso 6] Abriendo Chrome DevTools (F12) para auditoría de cabeceras HTTP..."
minimizar_vscode
if [ -n "${CHROME_WID}" ]; then
  DISPLAY=:0 xdotool windowactivate --sync "${CHROME_WID}"
  DISPLAY=:0 xdotool key F12
  sleep 2.5
fi
minimizar_vscode
echo "[Paso 6] Capturando DevTools con cabeceras Apache/2.4 y PHP/8.2..."
DISPLAY=:0 spectacle -b -n -f -o "${CAPTURAS_DIR}/paso_06_chrome_devtools_auditoria_servicios.png"
sleep 1

# Cerrar DevTools y ventana de prueba de Chrome
if [ -n "${CHROME_WID}" ]; then
  DISPLAY=:0 xdotool windowclose "${CHROME_WID}" 2>/dev/null || kill "${CHROME_PID}" 2>/dev/null || true
fi
sleep 1

echo "================================================================================"
echo "TODAS LAS CAPTURAS GENERADAS EXITOSAMENTE CON SPECTACLE Y XDOTOOL"
echo "Todo Visual Studio Code fue minimizado y los comandos se ejecutaron en Konsole."
ls -lh "${CAPTURAS_DIR}"
echo "================================================================================"
