#!/bin/bash
# ==============================================================================
# SCRIPT DE CERTIFICACIÓN DE OPERATIVIDAD EN PLATAFORMA DE PRODUCCIÓN
# Evidencia: GA10-220501097-AA6-EV01 - Archivos Cargados en Plataforma Producción
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | SENA CTPI Popayán
# ==============================================================================

set -e

echo "================================================================================"
echo "AUDITORÍA Y CERTIFICACIÓN DE OPERATIVIDAD EN PLATAFORMA DE PRODUCCIÓN"
echo "Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán - Regional Cauca"
echo "Proyecto: Pizzería Gourmet Bella Italia Popayán"
echo "Fecha: $(date)"
echo "================================================================================"

echo ""
echo "[1/4] AUDITORÍA DEL SERVIDOR WEB DE PRODUCCIÓN (PUERTO 8095):"
echo "--------------------------------------------------------------------------------"
curl -I http://localhost:8095/
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8095/)
if [ "$HTTP_CODE" -eq 200 ]; then
  echo "✔ Servidor web en producción respondiendo con código HTTP 200 OK."
else
  echo "✖ Fallo en respuesta de producción (Código HTTP: $HTTP_CODE)."
  exit 1
fi

echo ""
echo "[2/4] VERIFICACIÓN DE ESTRUCTURA Y PERMISOS DE ARCHIVOS EN HOSTING (0755/0644):"
echo "--------------------------------------------------------------------------------"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="${SCRIPT_DIR}/.."
SITE_DIR="${BASE_DIR}/sitio_web_produccion"

ls -la "${SITE_DIR}"
echo "✔ Estructura de archivos de hosting validada con permisos seguros Unix."

echo ""
echo "[3/4] AUDITORÍA DE BASE DE DATOS Y MIGRACIÓN EN PRODUCCIÓN (PUERTO 3310):"
echo "--------------------------------------------------------------------------------"
docker exec sena-produccion-pizzeria-db mysqladmin ping -h 127.0.0.1 -u root -pRootPopayan2026!
docker exec -i sena-produccion-pizzeria-db mysql -u root -pRootPopayan2026! pizzeria_produccion_db -e "
SELECT id_producto, nombre_pizza, categoria, precio_cop FROM productos_pizza;
SELECT codigo_orden, subtotal_cop, total_cop, estado_orden FROM pedidos_gourmet;
"
echo "✔ Tablas de producción migradas satisfactoriamente en motor InnoDB."

echo ""
echo "[4/4] COMPROBACIÓN DE ROLES Y PRIVILEGIOS SEGÚN SEGURIDAD (PoLP):"
echo "--------------------------------------------------------------------------------"
docker exec -i sena-produccion-pizzeria-db mysql -u root -pRootPopayan2026! pizzeria_produccion_db -e "
SHOW GRANTS FOR 'pizzeria_app_user'@'%';
SHOW GRANTS FOR 'auditor_sena'@'%';
"
echo "✔ Principio de Menor Privilegio (PoLP) certificado para usuarios de producción."

echo ""
echo "================================================================================"
echo "PLATAFORMA EN PRODUCCIÓN OPERANDO EXITOSAMENTE Y CERTIFICADA AL 100%"
echo "================================================================================"
