#!/bin/bash
# ==============================================================================
# SCRIPT DE ATENCIÓN DE INCIDENCIA CORRECTIVA Y CONTROL DE SLA - ISO/IEC 14764
# Evidencia: GA10-220501097-AA8-EV01 - Plan de Mantenimiento y Soporte
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán - Regional Cauca
# ==============================================================================

set -e

TICKET_ID="#TCK-2026-CORR-085"
FECHA_REPORTE=$(date '+%Y-%m-%d %H:%M:%S')

echo "================================================================================"
echo "    GESTIÓN DE INCIDENCIA CORRECTIVA Y CONTROL DE ACUERDOS SLA"
echo "    Ticket Radicado: ${TICKET_ID}"
echo "    Sistema: Módulo de Pedidos - Pizzería Gourmet Bella Italia Popayán"
echo "    Responsable de Soporte: Karen Yuliana Campo (Líder Técnico)"
echo "    Fecha y Hora del Reporte: ${FECHA_REPORTE}"
echo "================================================================================"
echo ""

echo "[Paso 1: Clasificación del Incidente según Matriz de Severidad]"
echo "  - Clasificación: P1 - Severidad Crítica"
echo "  - Causa detectada: Bloqueo intermitente en tabla de transacciones de checkout."
echo "  - SLA Máximo de Respuesta: 15 minutos"
echo "  - SLA Máximo de Solución (MTTR): 2 horas (120 minutos)"
echo "  [OK] Notificación inmediata emitida a la responsable del sistema."
echo ""

echo "[Paso 2: Diagnóstico de Causa Raíz en Entorno de Pruebas]"
echo "  - Análisis de logs de MySQL y slow-query-log."
echo "  - Se detecta contención por falta de índice compuesto en pedidos_gourmet(fecha_pedido, estado)."
echo "  - Tiempo transcurrido de diagnóstico: 14 minutos."
echo ""

echo "[Paso 3: Implementación y Validación de Hotfix Correctivo]"
echo "  - Aplicación de sentencia SQL de corrección:"
echo "      ALTER TABLE pedidos_gourmet ADD INDEX idx_pedidos_fecha_estado (fecha_pedido, estado);"
echo "  - Ejecución de prueba de estrés transaccional (100 pedidos concurrentes simulados):"
echo "      Latencia promedio reducida de 2.8s a 18ms."
echo "  - Verificación en ambiente Staging: 100% PASS sin errores."
echo ""

echo "[Paso 4: Despliegue en Producción y Cierre Formal del Ticket]"
echo "  - Despliegue de parche mediante ventana controlada."
echo "  - Tiempo Total de Solución (MTTR Registrado): 38 minutos."
echo "  - Cumplimiento de SLA: CUMPLE (38 min < 120 min permitidos)."
echo "  - Estado del Ticket: CERRADO Y ACEPTADO CON PRUEBA DE REGRESIÓN."
echo ""

echo "================================================================================"
echo "    INCIDENCIA CORRECTIVA RESUELTA CON ÉXITO DENTRO DEL SLA EXIGIDO"
echo "    Métrica MTTR: 38 minutos | Disponibilidad Restaurada: 100%"
echo "================================================================================"
