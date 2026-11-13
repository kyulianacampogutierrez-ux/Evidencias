# MATRIZ DE TRAZABILIDAD DE REQUISITOS (REQUIREMENTS TRACEABILITY MATRIX - RTM)
## PROYECTO: PIZZERÍA GOURMET BELLA ITALIA POPAYÁN
**Ficha ADSO:** 3186681 | **Aprendiz:** Karen Yuliana Campo | **Estándar:** IEEE 829

| ID REQUISITO | DESCRIPCIÓN DEL REQUISITO FUNCIONAL | HISTORIA DE USUARIO | ID CASO DE PRUEBA | TIPO DE PRUEBA | ESTADO DE COBERTURA |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **RF-01** | Catálogo digital de pizzas gourmet y bebidas | `HU-01: Catálogo` | `CP-CAT-001` | Funcional / Integración | Cubierto (100%) |
| **RF-02** | Carrito de compras con adiciones y tamaños | `HU-02: Carrito` | `CP-CAR-001` | Funcional / UI | Cubierto (100%) |
| **RF-03** | Liquidación de Impoconsumo (8%) y Domicilios | `HU-07: Checkout` | `CP-ORD-001` | Unitaria / Negocio | Cubierto (100%) |
| **RF-04** | Exoneración de envío para compras &ge; $60.000 | `HU-08: Promo Envío`| `CP-ORD-002` | Unitaria / Regla | Cubierto (100%) |
| **RF-05** | Aplicación de cupones gourmet (ej. 10% OFF) | `HU-09: Cupones` | `CP-ORD-003` | Unitaria / Negocio | Cubierto (100%) |
| **RF-06** | Validación de canasta no vacía en checkout | `HU-10: Validación`| `CP-ORD-004` | Unitaria / Excepción | Cubierto (100%) |
| **RF-07** | Políticas de contraseñas robustas (&ge;8 chars) | `HU-11: Registro` | `CP-SEC-001` | Seguridad / Auth | Cubierto (100%) |
| **RF-08** | Autenticación JWT y control de acceso RBAC | `HU-12: Login/Roles`| `CP-SEC-002` | Seguridad / API | Cubierto (100%) |
| **RF-09** | Validación de teléfonos móviles en Colombia | `HU-13: Datos Envío`| `CP-CUS-001` | Integración / Datos | Cubierto (100%) |
| **RF-10** | Saneamiento XSS y NoSQL Injection | `HU-14: Seguridad Web`| `CP-SEC-003` | Seguridad / OWASP | Cubierto (100%) |
| **RF-11** | Reserva transaccional de stock de bodega | `HU-15: KDS Cocina` | `CP-INV-001` | Integración / Datos | Cubierto (100%) |
| **RF-12** | Control de desabastecimiento de insumos | `HU-16: Bloqueo Stock`| `CP-INV-002` | Unitaria / Excepción | Cubierto (100%) |
| **RNF-01** | Tiempo de respuesta de endpoints &lt; 200 ms | `HU-17: Rendimiento` | `CP-PRF-001` | Rendimiento / k6 | Cubierto (100%) |
| **RNF-02** | Disponibilidad del servicio 99.9% en Docker | `HU-18: Operación` | `CP-ENV-001` | Infraestructura / Docker | Cubierto (100%) |
