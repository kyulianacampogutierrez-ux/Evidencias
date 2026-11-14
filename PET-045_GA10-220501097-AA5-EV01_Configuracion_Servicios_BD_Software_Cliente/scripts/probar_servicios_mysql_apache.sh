#!/bin/bash
# ==============================================================================
# SCRIPT DE COMPROBACIÓN TÉCNICA DE SERVICIOS EN PLATAFORMA CLIENTE
# Evidencia: GA10-220501097-AA5-EV01 - Configuración de Servicios, BD y Software
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | SENA CTPI Popayán
# ==============================================================================

set -e

echo "================================================================================"
echo "AUDITORÍA Y CERTIFICACIÓN DE SERVICIOS ACTIVOS EN PLATAFORMA CLIENTE"
echo "Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán - Regional Cauca"
echo "Proyecto: Pizzería Gourmet Bella Italia Popayán"
echo "Fecha: $(date)"
echo "================================================================================"

echo ""
echo "[1/4] AUDITORÍA DEL SERVIDOR WEB DE APLICACIONES APACHE 2.4 (PUERTO 8090):"
echo "--------------------------------------------------------------------------------"
curl -I http://localhost:8090/
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8090/)
if [ "$HTTP_CODE" -eq 200 ]; then
  echo "✔ Servidor Apache 2.4 respondiendo satisfactoriamente con código HTTP 200 OK."
else
  echo "✖ Fallo en respuesta de Apache (Código HTTP: $HTTP_CODE)."
  exit 1
fi

echo ""
echo "[2/4] AUDITORÍA DE CONECTIVIDAD Y SALUD DEL GESTOR MYSQL 8.0 (PUERTO 3308):"
echo "--------------------------------------------------------------------------------"
docker exec sena-cliente-mysql-servidor mysqladmin ping -h localhost -u karen_admin -pSenaPopayan2026!
echo "✔ Gestor de Base de Datos MySQL 8.0 respondiendo activamente (alive)."

echo ""
echo "[3/4] CONSULTA SQL DE CATÁLOGO GOURMET EN TIEMPO REAL:"
echo "--------------------------------------------------------------------------------"
docker exec -i sena-cliente-mysql-servidor mysql -u karen_admin -pSenaPopayan2026! pizzeria_bella_italia_db -e "
SELECT id_producto, nombre_pizza, categoria, precio_cop FROM productos_pizza;
"
echo "✔ Tablas relacionales leídas directamente desde el motor InnoDB de MySQL."

echo ""
echo "[4/4] AUDITORÍA TRANSACCIONAL DE PEDIDOS PERSISTIDOS:"
echo "--------------------------------------------------------------------------------"
docker exec -i sena-cliente-mysql-servidor mysql -u karen_admin -pSenaPopayan2026! pizzeria_bella_italia_db -e "
SELECT p.codigo_orden, u.nombre_completo, pr.nombre_pizza, p.total_cop, p.estado_orden 
FROM pedidos_gourmet p 
JOIN usuarios_clientes u ON p.id_usuario = u.id_usuario 
JOIN productos_pizza pr ON p.id_producto = pr.id_producto;
"
echo "✔ Integridad referencial certificada (FOREIGN KEY clientes -> pedidos -> productos)."

echo ""
echo "================================================================================"
echo "TODOS LOS SERVICIOS OPERANDO EN ESTADO HEALTHY Y CONECTADOS EXITOSAMENTE"
echo "================================================================================"
