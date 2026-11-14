#!/bin/bash
# ==============================================================================
# SCRIPT DE DESPLIEGUE DEL AMBIENTE DEL MANUAL DE USUARIO EN DOCKER
# Sistema: Pizzería Gourmet Bella Italia Popayán | Guía 10 - AA11-EV01
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="${SCRIPT_DIR}/.."
DOCKER_DIR="${BASE_DIR}/docker_manual_usuario"

echo "================================================================================"
echo "    INICIANDO AMBIENTE DEL MANUAL DE USUARIO EN DOCKER (ZERO POLLUTION)"
echo "    Puertos: 8100 (Web Apache) y 3315 (MySQL 8.0)"
echo "================================================================================"

cd "${DOCKER_DIR}"

echo -e "\n[1/3] Levantando contenedores orquestados con Docker Compose..."
docker compose up -d

echo -e "\n[2/3] Esperando inicialización y comprobación de salud (Healthchecks)..."
sleep 5

for i in {1..12}; do
  WEB_HEALTH=$(docker inspect --format='{{.State.Health.Status}}' sena-manual-usuario-web 2>/dev/null || echo "starting")
  DB_HEALTH=$(docker inspect --format='{{.State.Health.Status}}' sena-manual-usuario-db 2>/dev/null || echo "starting")
  echo "  Intento $i: Web=[${WEB_HEALTH}] | DB=[${DB_HEALTH}]"
  if [ "${WEB_HEALTH}" = "healthy" ] && [ "${DB_HEALTH}" = "healthy" ]; then
    echo -e "\n[✓] Contenedores en estado HEALTHY!"
    break
  fi
  sleep 3
done

echo -e "\n[3/3] Resumen de contenedores activos:"
docker compose ps

echo -e "\n================================================================================"
echo "    [✓] ENTORNO DEL MANUAL DE USUARIO DISPONIBLE"
echo "    - Portal Web Manual de Usuario: http://localhost:8100/"
echo "    - Base de Datos MySQL 8.0:      localhost:3315"
echo "================================================================================"
