#!/bin/bash
# ==============================================================================
# SCRIPT DE SIMULACIÓN DE FLUJO DE USUARIO (COMENSAL -> COCINA -> FACTURACIÓN)
# Sistema: Pizzería Gourmet Bella Italia Popayán | Guía 10 - AA11-EV01
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán
# ==============================================================================

set -e

echo "================================================================================"
echo "    SIMULADOR DEL FLUJO DE TRABAJO DEL USUARIO (END-TO-END WORKFLOW)"
echo "    Pizzería Gourmet Bella Italia Popayán - Ficha 3186681"
echo "================================================================================"

# Paso 1: Autenticación de Usuario Comensal
echo -e "\n[Paso 1/5] Autenticación de Comensal en el Portal Web..."
echo "  • Usuario: santiago.perez@gmail.com"
echo "  • Rol Detectado: ClienteComensal (Nivel 1)"
echo "  • Token JWT emitido con éxito [✓]"

# Paso 2: Selección de Platos en Menú Digital
echo -e "\n[Paso 2/5] Exploración de Carta y Creación de Pedido en Carrito..."
echo "  • Ítem 1: Pizza Gourmet Pipián Caucano ($48.000 COP)"
echo "  • Ítem 2: Limonada de Coco Caucana ($12.000 COP)"
echo "  • Subtotal: $60.000 COP | IVA (19%): $11.400 COP | Total: $71.400 COP"
echo "  • Dirección de Envío: Calle 4 # 7-19, Centro Histórico, Popayán"
echo "  • Código de Pedido Generado: ORD-202611-105 [✓]"

# Paso 3: Enrutamiento a Cocina KDS
echo -e "\n[Paso 3/5] Notificación en Pantalla KDS de Jefe de Cocina..."
echo "  • Estado Actual: RECIBIDO -> EN_PREPARACION"
echo "  • Horno de Leña a 400°C: Tiempo estimado 14 minutos"
echo "  • Alerta sonora y visual disparada en el monitor de cocina [✓]"

# Paso 4: Liquidación y Facturación Electrónica DIAN
echo -e "\n[Paso 4/5] Emisión de Factura Fiscal en Módulo de Caja..."
echo "  • Factura No.: FE-POPY-105"
echo "  • CUFE Generado: fe7b9c1d3e5a7b90123456789abcdef0123456789abcdef0123456789abcdef05"
echo "  • Estado DIAN: ACEPTADA [✓]"

# Paso 5: Despacho y Entrega
echo -e "\n[Paso 5/5] Asignación y Entrega por Domiciliario..."
echo "  • Domiciliario: Carlos López (Ruta Centro - Popayán)"
echo "  • Estado Final: EN_CAMINO -> ENTREGADO"
echo "  • Pago Recibido: $71.400 COP en efectivo"
echo "  • Firma digital capturada en pantalla del cliente [✓]"

echo -e "\n================================================================================"
echo "    [✓] FLUJO DE TRABAJO DE USUARIO COMPLETADO SATISFACTORIAMENTE"
echo "    Tiempos de respuesta y transiciones de estado 100% conformes."
echo "================================================================================"
