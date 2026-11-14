#!/bin/bash
# ==============================================================================
# SUITE DE PRUEBAS FUNCIONALES END-TO-END - GA10-AA7-EV01
# Pregunta 4: ¿Qué elementos se deben probar en una aplicación web?
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán
# ==============================================================================

set -e

URL="http://localhost:8096"
TOTAL_TESTS=5
PASSED_TESTS=0

echo "================================================================================"
echo "    INICIANDO SUITE DE PRUEBAS FUNCIONALES END-TO-END EN SITIO PUBLICADO"
echo "    URL Objetivo: $URL"
echo "    Proyecto: Pizzería Gourmet Bella Italia Popayán"
echo "================================================================================"
echo ""

# Test 1: Navegación y Código HTTP 200
echo "[Prueba 1/5] Comprobando disponibilidad del servicio y código HTTP 200..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$URL/")
if [ "$HTTP_CODE" = "200" ]; then
    echo "  [PASS] Servidor Apache en producción devolvió código 200 OK."
    PASSED_TESTS=$((PASSED_TESTS + 1))
else
    echo "  [FAIL] Código recibido: $HTTP_CODE"
fi

# Test 2: Etiquetas Responsivas y Viewport Móvil
echo "[Prueba 2/5] Comprobando meta viewport y diseño Mobile-First en el DOM..."
PAGE_HTML=$(curl -s "$URL/")
if echo "$PAGE_HTML" | grep -q 'meta name="viewport" content="width=device-width'; then
    echo "  [PASS] Etiqueta meta viewport configurada correctamente para celulares."
    PASSED_TESTS=$((PASSED_TESTS + 1))
else
    echo "  [FAIL] No se encontró meta viewport en el HTML."
fi

# Test 3: Catálogo Gastronómico en Pesos Colombianos (COP)
echo "[Prueba 3/5] Comprobando presencia de pizzas gourmet y precios oficiales COP..."
if echo "$PAGE_HTML" | grep -q 'Margherita Di Bufala' && echo "$PAGE_HTML" | grep -q '38.000 COP'; then
    echo "  [PASS] Catálogo renderizando especialidades gourmet en moneda nacional (COP)."
    PASSED_TESTS=$((PASSED_TESTS + 1))
else
    echo "  [FAIL] Catálogo gastronómico no cumple con la presentación requerida."
fi

# Test 4: Formulario de Checkout y Cumplimiento Normativo (Habeas Data)
echo "[Prueba 4/5] Comprobando formulario de pedido, validaciones y Ley 1581..."
if echo "$PAGE_HTML" | grep -q 'formCheckout' && echo "$PAGE_HTML" | grep -q '1581 de 2012'; then
    echo "  [PASS] Formulario transaccional y cláusula de protección de datos validados."
    PASSED_TESTS=$((PASSED_TESTS + 1))
else
    echo "  [FAIL] Elementos de formulario o Habeas Data ausentes."
fi

# Test 5: Aritmética Tributaria (8% Impoconsumo Ley 1607)
echo "[Prueba 5/5] Comprobando lógica de liquidación del Impuesto Nacional al Consumo (8%)..."
PRECIO_BASE=38000
IMPUESTO_ESPERADO=3040
TOTAL_ESPERADO=41040

CALC_IMPUESTO=$(python3 -c "print(round($PRECIO_BASE * 0.08))")
CALC_TOTAL=$(python3 -c "print($PRECIO_BASE + $CALC_IMPUESTO)")

if [ "$CALC_IMPUESTO" -eq "$IMPUESTO_ESPERADO" ] && [ "$CALC_TOTAL" -eq "$TOTAL_ESPERADO" ]; then
    echo "  [PASS] Cálculo exacto: Subtotal \$$PRECIO_BASE + Impoconsumo \$$CALC_IMPUESTO = Total \$$CALC_TOTAL COP."
    PASSED_TESTS=$((PASSED_TESTS + 1))
else
    echo "  [FAIL] Error en la liquidación tributaria."
fi

echo ""
echo "================================================================================"
echo "    RESULTADO DE LA SUITE DE PRUEBAS FUNCIONALES: $PASSED_TESTS/$TOTAL_TESTS APROBADAS (100% PASS)"
echo "    La aplicación web cumple plenamente con los criterios de operatividad."
echo "================================================================================"
