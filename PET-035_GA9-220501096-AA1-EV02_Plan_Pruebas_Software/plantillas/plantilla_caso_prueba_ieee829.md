# FORMATO OFICIAL DE ESPECIFICACIÓN DE CASO DE PRUEBA (ESTÁNDAR IEEE 829)
## PROYECTO: PIZZERÍA GOURMET BELLA ITALIA POPAYÁN

| CAMPO | ESPECIFICACIÓN TÉCNICA DEL CASO DE PRUEBA |
| :--- | :--- |
| **Identificador del Caso:** | `CP-ORD-001` |
| **Nombre del Caso de Prueba:** | Cálculo automatizado de subtotal, Impoconsumo (8%) y tarifa de envío en Popayán Centro |
| **Módulo del Sistema:** | Módulo de Facturación y Procesamiento de Órdenes (`OrderCalculator`) |
| **Requisito Asociado (RTM):** | `RF-03`: Liquidación tributaria de Impoconsumo y cálculo de recargos de envío |
| **Historia de Usuario:** | `HU-07`: Como cliente en Popayán, deseo visualizar el desglose exacto de mi comanda con impuestos y costo de domicilio antes de pagar |
| **Nivel de Prueba:** | Prueba Unitaria / Prueba de Integración |
| **Tipo de Prueba:** | Funcional / Caja Negra y Caja Blanca |
| **Prioridad:** | Alta (Crítica para la operación financiera) |
| **Ambiente de Ejecución:** | Contenedor Docker Node.js 20 LTS / REST API Go Fiber |
| **Responsable / Diseñador:** | Karen Yuliana Campo (Aprendiz ADSO - Ficha 3186681) |
| **Fecha de Diseño:** | Noviembre 2026 |

---

### CONDICIONES PREVIAS (PRE-CONDICIONES)
1. El catálogo de productos gourmet se encuentra disponible en la base de datos MongoDB.
2. El cliente ha seleccionado productos válidos:
   - 1 Pizza Margherita Gourmet Familiar ($42.000 COP)
   - 2 Gaseosas Italianas 400ml ($6.000 COP c/u = $12.000 COP)
3. La dirección de entrega seleccionada pertenece a la comuna "Centro" de Popayán.

---

### PASOS DE EJECUCIÓN PASO A PASO
1. Instanciar el objeto de orden con el listado de items, precios y cantidades.
2. Invocar la función de cálculo `OrderCalculator.processOrder(items, 'CENTRO')`.
3. Validar el subtotal bruto generado por la suma de items.
4. Aplicar el 8% de Impuesto Nacional al Consumo sobre el subtotal neto.
5. Determinar la tarifa de envío para Popayán Centro ($3.000 COP).
6. Totalizar: `Subtotal + Impoconsumo + Envío`.

---

### DATOS DE ENTRADA (TEST DATA)
```json
{
  "items": [
    { "id": "PZ-MARG-01", "name": "Pizza Margherita Gourmet Familiar", "price": 42000, "quantity": 1 },
    { "id": "BEB-ITA-02", "name": "Gaseosa Italiana 400ml", "price": 6000, "quantity": 2 }
  ],
  "deliveryZone": "CENTRO",
  "couponCode": null
}
```

---

### RESULTADOS ESPERADOS (EXPECTED RESULTS)
* Subtotal Bruto: **$54.000 COP**
* Descuento: **$0 COP**
* Impoconsumo (8%): **$4.320 COP**
* Costo Domicilio Popayán Centro: **$3.000 COP**
* **Total Liquidado a Pagar:** **$61.320 COP**
* Código de Estado HTTP (en API): **`200 OK`**

---

### CRITERIOS DE ACEPTACIÓN / POST-CONDICIONES
* El total calculado coincide exactamente al peso con el valor esperado.
* La comanda queda en estado `PENDIENTE` lista para confirmación por pasarela de pago o efectivo contra entrega.
