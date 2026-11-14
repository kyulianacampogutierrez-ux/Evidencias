#!/bin/bash
# ==============================================================================
# SCRIPT BASH DE VALIDACIÓN Y AUDITORÍA DE HARDWARE EN SERVIDOR LINUX
# Evidencia: GA10-220501097-AA2-EV01 - Elaborar plan de validación de hardware
# Caso: Servidor Web PHP (250 usuarios no concurrentes, ~30 concurrentes pico)
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán - Regional Cauca
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AUDIT_DIR="${SCRIPT_DIR}/../auditoria"
mkdir -p "${AUDIT_DIR}"
OUT_FILE="${AUDIT_DIR}/diagnostico_comandos_linux.txt"

echo "================================================================================" > "${OUT_FILE}"
echo "AUDITORÍA TÉCNICA DE INFRAESTRUCTURA Y HARDWARE PARA DESPLIEGUE PHP" >> "${OUT_FILE}"
echo "Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán - Regional Cauca" >> "${OUT_FILE}"
echo "Fecha de Ejecución: $(date)" >> "${OUT_FILE}"
echo "================================================================================" >> "${OUT_FILE}"

echo "" >> "${OUT_FILE}"
echo "--------------------------------------------------------------------------------" >> "${OUT_FILE}"
echo "1. VERIFICACIÓN DE PROCESADOR (CPU): lscpu / nproc" >> "${OUT_FILE}"
echo "--------------------------------------------------------------------------------" >> "${OUT_FILE}"
echo "Total de núcleos (nproc): $(nproc 2>/dev/null || echo 'N/A')" >> "${OUT_FILE}"
if command -v lscpu &> /dev/null; then
    lscpu | grep -E "Model name|Architecture|CPU\(s\):|Thread|Socket|MHz" >> "${OUT_FILE}" || true
else
    cat /proc/cpuinfo | grep -E "model name|cpu MHz|processor" | head -n 10 >> "${OUT_FILE}" || true
fi

echo "" >> "${OUT_FILE}"
echo "--------------------------------------------------------------------------------" >> "${OUT_FILE}"
echo "2. VERIFICACIÓN DE MEMORIA RAM Y SWAP: free -h" >> "${OUT_FILE}"
echo "--------------------------------------------------------------------------------" >> "${OUT_FILE}"
free -h >> "${OUT_FILE}" 2>/dev/null || cat /proc/meminfo | head -n 6 >> "${OUT_FILE}"

echo "" >> "${OUT_FILE}"
echo "--------------------------------------------------------------------------------" >> "${OUT_FILE}"
echo "3. VERIFICACIÓN DE ALMACENAMIENTO Y SISTEMAS DE ARCHIVOS: df -h / lsblk" >> "${OUT_FILE}"
echo "--------------------------------------------------------------------------------" >> "${OUT_FILE}"
df -hT -x tmpfs -x devtmpfs >> "${OUT_FILE}" 2>/dev/null || df -h >> "${OUT_FILE}"
echo "" >> "${OUT_FILE}"
if command -v lsblk &> /dev/null; then
    lsblk -o NAME,SIZE,FSTYPE,TYPE,MOUNTPOINT >> "${OUT_FILE}" || true
fi

echo "" >> "${OUT_FILE}"
echo "--------------------------------------------------------------------------------" >> "${OUT_FILE}"
echo "4. VERIFICACIÓN DE ADAPTADORES DE RED Y DIRECCIONAMIENTO IP: ip addr" >> "${OUT_FILE}"
echo "--------------------------------------------------------------------------------" >> "${OUT_FILE}"
ip -br addr >> "${OUT_FILE}" 2>/dev/null || ifconfig -a >> "${OUT_FILE}" 2>/dev/null || true

echo "" >> "${OUT_FILE}"
echo "--------------------------------------------------------------------------------" >> "${OUT_FILE}"
echo "5. VERIFICACIÓN DEL SISTEMA OPERATIVO Y KERNEL: uname -a / os-release" >> "${OUT_FILE}"
echo "--------------------------------------------------------------------------------" >> "${OUT_FILE}"
uname -a >> "${OUT_FILE}"
if [ -f /etc/os-release ]; then
    cat /etc/os-release | grep -E "PRETTY_NAME|VERSION_ID|ID" >> "${OUT_FILE}"
fi

echo "" >> "${OUT_FILE}"
echo "================================================================================" >> "${OUT_FILE}"
echo "DIAGNÓSTICO FINALIZADO CORRECTAMENTE. ARCHIVO CONSOLIDADO EN:" >> "${OUT_FILE}"
echo "${OUT_FILE}" >> "${OUT_FILE}"
echo "================================================================================" >> "${OUT_FILE}"

cat "${OUT_FILE}"
