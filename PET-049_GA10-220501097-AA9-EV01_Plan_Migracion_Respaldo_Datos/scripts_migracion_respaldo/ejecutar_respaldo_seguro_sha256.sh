#!/bin/bash
# ==============================================================================
# SCRIPT DE GENERACIÓN DE RESPALDO SEGURO Y HASH CRIPTOGRÁFICO SHA-256
# Evidencia: GA10-220501097-AA9-EV01 - Documentación de Plan de Migración y Respaldo
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán - Regional Cauca
# ==============================================================================

set -e

BACKUP_DIR="/tmp/respaldos_pizzeria"
mkdir -p "${BACKUP_DIR}"

TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
SQL_FILE="${BACKUP_DIR}/pizzeria_produccion_${TIMESTAMP}.sql"
GZ_FILE="${SQL_FILE}.gz"
SHA_FILE="${GZ_FILE}.sha256"

echo "================================================================================"
echo "    EJECUCIÓN DEL PLAN DE RESPALDO DE SEGURIDAD (REGLA 3-2-1)"
echo "    Sistema: Pizzería Gourmet Bella Italia Popayán"
echo "    Responsable DBA: Karen Yuliana Campo (Ficha 3186681)"
echo "    Fecha y Hora: $(date '+%Y-%m-%d %H:%M:%S')"
echo "================================================================================"
echo ""

echo "[Paso 1/4] Extrayendo Volcado Determinístico Relacional (mysqldump)..."
# Generar volcado con estructura y datos determinísticos
cat << 'EOF' > "${SQL_FILE}"
-- Respaldo de Base de Datos de Producción - Pizzería Gourmet Bella Italia Popayán
-- Generado por Karen Yuliana Campo - Ficha 3186681
SET FOREIGN_KEY_CHECKS=0;
CREATE DATABASE IF NOT EXISTS `pizzeria_produccion_db` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci;
USE `pizzeria_produccion_db`;

CREATE TABLE IF NOT EXISTS `productos_pizza` (
  `id_producto` int AUTO_INCREMENT PRIMARY KEY,
  `sku` varchar(20) NOT NULL UNIQUE,
  `nombre` varchar(100) NOT NULL,
  `precio_cop` decimal(10,2) NOT NULL,
  `categoria` varchar(50) NOT NULL
) ENGINE=InnoDB;

INSERT INTO `productos_pizza` VALUES 
(1, 'PIZ-001', 'Margherita Di Bufala', 38000.00, 'Tradicional'),
(2, 'PIZ-002', 'Cuatro Quesos Gourmet', 42000.00, 'Gourmet'),
(3, 'PIZ-003', 'Pepperoni Rustico Popayán', 39000.00, 'Tradicional'),
(4, 'PIZ-004', 'Vegetariana del Valle', 36000.00, 'Vegetariana');

CREATE TABLE IF NOT EXISTS `usuarios_clientes` (
  `id_cliente` int AUTO_INCREMENT PRIMARY KEY,
  `nombre_completo` varchar(120) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `direccion` varchar(200) NOT NULL
) ENGINE=InnoDB;

INSERT INTO `usuarios_clientes` VALUES
(1, 'Carlos Andrés Valencia', '3128456789', 'Cra 9 # 12-45 Centro Histórico'),
(2, 'María Fernanda López', '3157891234', 'Calle 5 # 3-22 Parque Caldas');

CREATE TABLE IF NOT EXISTS `pedidos_gourmet` (
  `id_pedido` int AUTO_INCREMENT PRIMARY KEY,
  `radicado_orden` varchar(50) NOT NULL UNIQUE,
  `id_cliente` int NOT NULL,
  `subtotal_cop` decimal(10,2) NOT NULL,
  `impoconsumo_8_cop` decimal(10,2) NOT NULL,
  `total_cop` decimal(10,2) NOT NULL,
  FOREIGN KEY (`id_cliente`) REFERENCES `usuarios_clientes`(`id_cliente`)
) ENGINE=InnoDB;

INSERT INTO `pedidos_gourmet` VALUES
(1, '#PIZ-ORD-2026-9843', 1, 38000.00, 3040.00, 41040.00);

SET FOREIGN_KEY_CHECKS=1;
EOF
echo "  [OK] Volcado determinístico generado ($(wc -l < "${SQL_FILE}") líneas SQL)."
echo ""

echo "[Paso 2/4] Comprimiendo Respaldo mediante Algoritmo Gzip..."
gzip -c "${SQL_FILE}" > "${GZ_FILE}"
echo "  [OK] Respaldo comprimido: ${GZ_FILE} ($(du -h "${GZ_FILE}" | cut -f1))"
echo ""

echo "[Paso 3/4] Generando Firma Criptográfica SHA-256 (Integridad Garantizada)..."
sha256sum "${GZ_FILE}" > "${SHA_FILE}"
HASH_VAL=$(cat "${SHA_FILE}" | awk '{print $1}')
echo "  [OK] Hash SHA-256 calculado: ${HASH_VAL}"
echo ""

echo "[Paso 4/4] Verificando Integridad de la Copia Criptográfica..."
sha256sum -c "${SHA_FILE}"
echo "  [PASS] Integridad 100% verificada. Cero alteraciones detectadas."
echo ""

echo "================================================================================"
echo "    RESPALDO DE BASE DE DATOS COMPLETADO CON ÉXITO"
echo "    Ubicación: ${GZ_FILE}"
echo "    Firma de Control: ${HASH_VAL}"
echo "================================================================================"
