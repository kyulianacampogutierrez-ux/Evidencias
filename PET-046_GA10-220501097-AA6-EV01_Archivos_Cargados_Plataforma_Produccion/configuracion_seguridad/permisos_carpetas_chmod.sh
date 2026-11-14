#!/bin/bash
# ==============================================================================
# SCRIPT DE APLICACIÓN DE PERMISOS DE SEGURIDAD UNIX EN HOSTING (CPANEL / APACHE)
# Evidencia: GA10-220501097-AA6-EV01 - Archivos Cargados en Plataforma Producción
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | SENA CTPI Popayán
# ==============================================================================

set -e

TARGET_DIR="${1:-../sitio_web_produccion}"

echo "================================================================================"
echo "APLICANDO MATRIZ DE PERMISOS DE SEGURIDAD EN CARPETA DE PRODUCCIÓN"
echo "Directorio objetivo: ${TARGET_DIR}"
echo "================================================================================"

# 1. Aplicar 0755 a directorios (Lectura, escritura y ejecución para propietario; lectura y ejecución para grupo y otros)
find "${TARGET_DIR}" -type d -exec chmod 755 {} \;
echo "✔ Permisos 0755 (drwxr-xr-x) aplicados a todos los directorios."

# 2. Aplicar 0644 a archivos regulares (Lectura y escritura para propietario; solo lectura para grupo y otros)
find "${TARGET_DIR}" -type f -exec chmod 644 {} \;
echo "✔ Permisos 0644 (-rw-r--r--) aplicados a archivos web (HTML, CSS, JS, SQL)."

# 3. Restricción estricta a archivos de configuración sensible
if [ -f "${TARGET_DIR}/config_produccion.json" ]; then
  chmod 640 "${TARGET_DIR}/config_produccion.json"
  echo "✔ Permiso restringido 0640 (-rw-r-----) aplicado a config_produccion.json."
fi

echo "================================================================================"
echo "VERIFICACIÓN DE PERMISOS DE ARCHIVOS:"
ls -la "${TARGET_DIR}"
echo "================================================================================"
