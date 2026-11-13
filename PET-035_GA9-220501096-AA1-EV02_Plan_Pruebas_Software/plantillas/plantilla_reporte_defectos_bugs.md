# FORMATO OFICIAL DE REPORTE Y SEGUIMIENTO DE DEFECTOS (BUG TRACKING REPORT)
## PROYECTO: PIZZERÍA GOURMET BELLA ITALIA POPAYÁN

| CAMPO | ESPECIFICACIÓN DEL DEFECTO / INCIDENCIA |
| :--- | :--- |
| **Identificador del Bug:** | `BUG-2026-004` |
| **Título del Defecto:** | Excepción no controlada al enviar lista vacía de items en endpoint de checkout |
| **Caso de Prueba Origen:** | `CP-ORD-004` |
| **Módulo Afectado:** | Microservicio de Órdenes (`/api/v1/pedidos`) |
| **Severidad:** | Alta (Bloquea la transacción sin mensaje amigable) |
| **Prioridad:** | Alta (Debe corregirse antes del paso a producción) |
| **Estado:** | Resuelto / Verificado (Closed) |
| **Ambiente de Reproducción:** | Docker Test Environment - Node.js 20 / Go REST API |
| **Reportado por:** | Karen Yuliana Campo (Tester / Aprendiz ADSO) |
| **Asignado a:** | Equipo de Desarrollo Backend |
| **Fecha de Reporte:** | Noviembre 2026 |

---

### DESCRIPCIÓN DETALLADA DEL DEFECTO
Al invocar la función `processOrder` o enviar un `POST /api/v1/pedidos` con un cuerpo JSON cuyo arreglo de items está vacío (`"items": []`), el servicio generaba un error interno no controlado `TypeError: cannot read property 'price' of undefined` en lugar de retornar una excepción de validación formal `400 Bad Request`.

---

### PASOS PARA REPRODUCIR EL ERROR (STEPS TO REPRODUCE)
1. Abrir terminal de pruebas o cliente Postman.
2. Construir petición `POST /api/v1/pedidos/checkout` con payload:
   ```json
   {
     "items": [],
     "deliveryZone": "CENTRO"
   }
   ```
3. Enviar la petición.
4. **Comportamiento Observado:** Error no controlado 500 con volcado de pila en consola.
5. **Comportamiento Esperado:** Mensaje de validación: `"El pedido debe contener al menos un producto"` con código HTTP 400.

---

### SOLUCIÓN APLICADA Y VERIFICACIÓN (FIX & RE-TEST)
* Se implementó una guarda condicional estricta al inicio de `OrderCalculator.processOrder`:
  ```javascript
  if (!Array.isArray(items) || items.length === 0) {
    throw new Error('El pedido debe contener al menos un producto');
  }
  ```
* Se ejecutó el caso `CP04` de la suite automatizada, confirmando la captura limpia de la excepción y el paso de la prueba en 0.6 ms.
