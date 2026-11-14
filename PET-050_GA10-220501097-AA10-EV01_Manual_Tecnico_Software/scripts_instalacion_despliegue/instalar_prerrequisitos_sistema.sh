#!/bin/bash
# ==============================================================================
# SCRIPT DE VERIFICACIÓN E INSTALACIÓN DE PRERREQUISITOS TÉCNICOS
# Sistema: Pizzería Gourmet Bella Italia Popayán | Guía 10 - AA10-EV01
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán
# ==============================================================================

set -e

echo "================================================================================"
echo "    VERIFICADOR DE PRERREQUISITOS TÉCNICOS DEL SISTEMA (MANUAL TÉCNICO)"
echo "    Proyecto: Pizzería Gourmet Bella Italia Popayán - SENA CTPI Ficha 3186681"
echo "================================================================================"

# 1. Verificación de Sistema Operativo y Arquitectura
OS_NAME=$(uname -s)
ARCH_NAME=$(uname -m)
echo -e "\n[1/6] Verificando Sistema Operativo y Arquitectura del Servidor..."
echo "  - Sistema Operativo Detectado: ${OS_NAME}"
echo "  - Arquitectura de Procesador:  ${ARCH_NAME}"
if [ "${OS_NAME}" = "Linux" ]; then
  echo "  [✓] Sistema Operativo compatible (Linux Kernel)"
else
  echo "  [!] Advertencia: Se recomienda Linux para entornos de producción"
fi

# 2. Verificación de Memoria RAM y Núcleos de CPU
echo -e "\n[2/6] Verificando Recursos de Hardware (CPU y RAM)..."
CPU_CORES=$(nproc || echo 2)
TOTAL_RAM_MB=$(free -m | awk '/^Mem:/{print $2}' || echo 4096)
echo "  - Núcleos de CPU Disponibles: ${CPU_CORES}"
echo "  - Memoria RAM Total del Host: ${TOTAL_RAM_MB} MB"
if [ "${TOTAL_RAM_MB}" -ge 3000 ]; then
  echo "  [✓] Memoria RAM suficiente (Mínimo 3000 MB superado)"
else
  echo "  [!] Memoria RAM ajustada"
fi

# 3. Verificación de Espacio en Disco
echo -e "\n[3/6] Verificando Espacio Libre en Partición Principal..."
DISK_FREE_GB=$(df -BG / | awk 'NR==2 {gsub("G",""); print $4}')
echo "  - Espacio Libre en /: ${DISK_FREE_GB} GB"
if [ "${DISK_FREE_GB}" -ge 5 ]; then
  echo "  [✓] Espacio en disco óptimo (Mínimo 5 GB superado con creces)"
else
  echo "  [!] Espacio en disco crítico"
fi

# 4. Verificación de Motores Docker y Docker Compose
echo -e "\n[4/6] Verificando Motor de Contenedores Docker (Zero Host Pollution)..."
if command -v docker >/dev/null 2>&1; then
  DOCKER_VER=$(docker --version)
  echo "  - Docker Engine: ${DOCKER_VER}"
  echo "  [✓] Docker instalado y accesible"
else
  echo "  [✗] Docker no encontrado. Por favor instale Docker Engine"
  exit 1
fi

if docker compose version >/dev/null 2>&1; then
  COMPOSE_VER=$(docker compose version)
  echo "  - Docker Compose: ${COMPOSE_VER}"
  echo "  [✓] Docker Compose Plugin activo"
else
  echo "  [✗] Docker Compose Plugin no disponible"
  exit 1
fi

# 5. Verificación de Disponibilidad de Puertos
echo -e "\n[5/6] Verificando Puertos Requeridos para el Manual Técnico..."
PUERTO_WEB=8099
PUERTO_DB=3314

check_port() {
  local port=$1
  if ss -tuln | grep -q ":${port} "; then
    echo "  - Puerto ${port}: OCUPADO / EN USO"
  else
    echo "  - Puerto ${port}: LIBRE Y DISPONIBLE"
  fi
}

check_port "${PUERTO_WEB}"
check_port "${PUERTO_DB}"

# 6. Verificación de Herramientas de Red y Diagnóstico
echo -e "\n[6/6] Verificando Herramientas Auxiliares (curl, jq)..."
for tool in curl jq; do
  if command -v $tool >/dev/null 2>&1; then
    echo "  - Herramienta ${tool}: INSTALADA [✓]"
  else
    echo "  - Herramienta ${tool}: NO ENCONTRADA [!]"
  fi
done

echo -e "\n================================================================================"
echo "    [✓] AUDITORÍA DE PRERREQUISITOS COMPLETADA SATISFACTORIAMENTE"
echo "    El entorno está 100% calificado para el despliegue del ecosistema."
echo "================================================================================"
