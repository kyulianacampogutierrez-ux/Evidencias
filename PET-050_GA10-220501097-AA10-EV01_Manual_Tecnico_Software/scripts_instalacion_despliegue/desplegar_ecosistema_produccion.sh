#!/bin/bash
# ==============================================================================
# SCRIPT DE DESPLIEGUE AUTOMATIZADO DEL ECOSISTEMA (DOCKER COMPOSE)
# Sistema: Pizzería Gourmet Bella Italia Popayán | Guía 10 - AA10-EV01
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="${SCRIPT_DIR}/.."
DOCKER_DIR="${BASE_DIR}/docker_manual_tecnico"

echo "================================================================================"
echo "    INICIANDO DESPLIEGUE DEL MANUAL TÉCNICO Y AMBIENTE EN DOCKER"
echo "    Directorio Docker: ${DOCKER_DIR}"
echo "================================================================================"

cd "${DOCKER_DIR}"

echo -e "\n[1/3] Levantando contenedores orquestados con Docker Compose..."
docker compose up -d

echo -e "\n[2/3] Esperando estabilización e inicialización de servicios (Healthchecks)..."
sleep 5

for i in {1..12}; do
  WEB_HEALTH=$(docker inspect --format='{{.State.Health.Status}}' sena-manual-tecnico-web 2>/dev/null || echo "starting")
  DB_HEALTH=$(docker inspect --format='{{.State.Health.Status}}' sena-manual-tecnico-db 2>/dev/null || echo "starting")
  echo "  Intento $i: Web=[${WEB_HEALTH}] | DB=[${DB_HEALTH}]"
  if [ "${WEB_HEALTH}" = "healthy" ] && [ "${DB_HEALTH}" = "healthy" ]; then
    echo -e "\n[✓] Ambos servicios han alcanzado el estado HEALTHY!"
    break
  fi
  sleep 3
done

echo -e "\n[3/3] Resumen de contenedores activos:"
docker compose ps

echo -e "\n================================================================================"
echo "    [✓] DESPLIEGUE FINALIZADO EXITOSAMENTE"
echo "    - Portal Web Manual Técnico: http://localhost:8099/"
echo "    - Base de Datos MySQL 8.0:   localhost:3314 (DB: pizzeria_manual_tecnico_db)"
echo "================================================================================"
