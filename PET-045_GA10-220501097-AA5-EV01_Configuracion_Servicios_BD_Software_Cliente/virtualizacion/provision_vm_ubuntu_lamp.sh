#!/bin/bash
# ==============================================================================
# SCRIPT DE APROVISIONAMIENTO: MÁQUINA VIRTUAL UBUNTU SERVER 22.04 LTS (LAMP)
# Evidencia: GA10-220501097-AA5-EV01 - Configuración de Servicios en Cliente
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | SENA CTPI Popayán
# ==============================================================================

set -e

export DEBIAN_FRONTEND=noninteractive

echo "================================================================================"
echo "APROVISIONANDO MÁQUINA VIRTUAL UBUNTU SERVER - PILA LAMP"
echo "================================================================================"

# 1. Actualización de repositorios
apt-get update -y
apt-get upgrade -y

# 2. Instalación del Servidor Web Apache2
echo "[1/4] Instalando Apache 2..."
apt-get install -y apache2 apache2-utils
systemctl enable apache2
systemctl start apache2

# 3. Instalación del Gestor de Base de Datos MySQL Server
echo "[2/4] Instalando MySQL Server 8.0..."
apt-get install -y mysql-server
systemctl enable mysql
systemctl start mysql

# 4. Configuración Segura de Base de Datos y Creación de Esquema
echo "[3/4] Configurando Base de Datos pizzeria_bella_italia_db..."
mysql -u root << 'EOSQL'
CREATE DATABASE IF NOT EXISTS pizzeria_bella_italia_db CHARACTER SET utf8mb4;
CREATE USER IF NOT EXISTS 'karen_admin'@'%' IDENTIFIED BY 'SenaPopayan2026!';
GRANT ALL PRIVILEGES ON pizzeria_bella_italia_db.* TO 'karen_admin'@'%';
FLUSH PRIVILEGES;
EOSQL

# 5. Instalación de PHP y Módulos de Conexión
echo "[4/4] Instalando PHP y módulos Apache/MySQL..."
apt-get install -y php php-cli php-mysql php-mbstring libapache2-mod-php
a2enmod rewrite
systemctl restart apache2

echo "================================================================================"
echo "APROVISIONAMIENTO DE MÁQUINA VIRTUAL COMPLETADO EXITOSAMENTE"
echo "Servicios activos: Apache2 ($(apache2 -v | head -n 1)), MySQL ($(mysql --version))"
echo "================================================================================"
