# ACTA FORMAL DE APROBACIÓN DE REQUERIMIENTOS DE SOFTWARE
## Proyecto: Sistema de Gestión, Carta y Pedidos - Pizzería Gourmet Bella Italia Popayán
### Evidencia GA8-220501096-AA1-EV02: Módulos Integrados

---

**Fecha de Aprobación:** 10 de Noviembre de 2026  
**Lugar:** Popayán, Cauca — Sede Centro Histórico  
**Entidad Evaluadora:** Servicio Nacional de Aprendizaje (SENA) — CTPI Popayán  
**Programa:** Tecnología en Análisis y Desarrollo de Software (ADSO) — Ficha: 3186681  
**Aprendiz Responsable:** Karen Yuliana Campo  
**Interesado / Stakeholder del Negocio:** Gerencia General y Dirección de Operaciones — Pizzería Gourmet Bella Italia  

---

## 1. Declaración de Conformidad y Aprobación

Por medio del presente documento, los interesados del proyecto formativo y el equipo técnico certifican que los **Requerimientos Funcionales (RF)** y **Requerimientos No Funcionales (RNF)** especificados en las fases de análisis han sido desarrollados, integrados y validados a satisfacción mediante prototipos funcionales, microservicios RESTful, interfaces web reactivas y aplicativos móviles.

---

## 2. Matriz de Trazabilidad de Requerimientos Funcionales (RF)

| Código | Descripción del Requerimiento Funcional | Módulo Asociado | Estado de Entrega | Mecanismo de Verificación |
|---|---|---|---|---|
| **RF-01** | Autenticación perimetral mediante credenciales seguras y generación de tokens JWT. | Módulo de Seguridad | **APROBADO (100%)** | `POST /api/auth/login` con bcrypt hash |
| **RF-02** | Control de acceso basado en roles (RBAC) para perfiles `CLIENTE` y `ADMIN`. | Módulo de Seguridad | **APROBADO (100%)** | Middlewares `JWTMiddleware` y `AdminRequired` |
| **RF-03** | Consulta pública de catálogo gastronómico con pizzas artesanales a 380°C. | Módulo de Carta | **APROBADO (100%)** | `GET /api/pizzas` y componente `CartaMenu.jsx` |
| **RF-04** | Filtrado dinámico por categoría (Clásicas, Gourmet, Vegetarianas, Especiales). | Módulo de Carta | **APROBADO (100%)** | Query params `?categoria=` y tabs interactivos |
| **RF-05** | Selección y tarificación polimórfica por tamaño (Personal, Mediana, Familiar). | Módulo de Carta | **APROBADO (100%)** | Selector en modal y cálculo en modelo `Pizza` |
| **RF-06** | Validación en tiempo real de cupones de descuento porcentuales vigentes. | Módulo de Cupones | **APROBADO (100%)** | `POST /api/cupones/validar` (Cupón `SENA2026`) |
| **RF-07** | Límite máximo de descuento en pesos para protección del margen de ganancia. | Módulo de Cupones | **APROBADO (100%)** | Atributo `maxDescuento` en MongoDB |
| **RF-08** | Carrito de compras persistente con cálculo automático de subtotales y adiciones. | Módulo de Checkout | **APROBADO (100%)** | React `CartContext` y Drawer lateral interactivo |
| **RF-09** | Regla de negocio de domicilio gratuito por compras superiores a \$70.000 COP. | Módulo de Pedidos | **APROBADO (100%)** | Lógica de envío en `handlers.CrearPedido` |
| **RF-10** | Creación y despacho de pedidos con dirección georreferenciada en Popayán. | Módulo de Pedidos | **APROBADO (100%)** | `POST /api/pedidos` con código autogenerado |
| **RF-11** | Trazabilidad del pedido en 5 estados operativos (`RECIBIDO` a `ENTREGADO`). | Módulo de Tracking | **APROBADO (100%)** | `GET /api/pedidos/:numero` y timeline visual |
| **RF-12** | Simulación de pasarela de pagos con recibo digital autorizado. | Módulo de Pagos | **APROBADO (100%)** | `POST /api/pagos/procesar` (Nequi, Daviplata, PSE) |
| **RF-13** | Transición atómica de estados: Pago Aprobado &rarr; Cocina Inicia Preparación. | Módulo de Pagos | **APROBADO (100%)** | Actualización `$set` y `$push` en MongoDB |
| **RF-14** | Dashboard directivo con analítica de ventas totales y pedidos en cola. | Módulo Admin | **APROBADO (100%)** | `GET /api/admin/dashboard` y panel gráfico |
| **RF-15** | Actualización administrativa del ciclo de vida del pedido por el pizzero. | Módulo Admin | **APROBADO (100%)** | `PUT /api/admin/pedidos/:numero/estado` |

---

## 3. Matriz de Requerimientos No Funcionales (RNF)

| Código | Requerimiento No Funcional | Estándar / Métrica Alcanzada | Validación Técnica |
|---|---|---|---|
| **RNF-01** | **Rendimiento:** Tiempos de respuesta de servicios web inferiores a 100 ms. | Promedio alcanzado: **19 ms** (min: 2 ms, max: 64 ms). | Benchmark Newman / Postman Runner |
| **RNF-02** | **Seguridad:** Cifrado de contraseñas y firma digital de tokens. | Bcrypt factor 10 + JWT HMAC-SHA256 con clave de 256 bits. | Pruebas de autenticación y profile |
| **RNF-03** | **Portabilidad y Despliegue:** Ejecución sin fricción en cualquier SO con Docker. | 6 contenedores en `docker-compose.yml` (`sena-network`). | Pruebas de contenedores en Linux/Windows |
| **RNF-04** | **Usabilidad y Responsive:** Experiencia fluida en móviles y escritorio. | React SPA (Vite + Tailwind) y React Native (Expo SDK 51). | Pruebas en Chrome y emuladores Android |
| **RNF-05** | **Concurrencia:** Alta capacidad de atención simultánea de órdenes. | Go Fiber v2 sobre motor Fasthttp con goroutines asíncronas. | 100% de aserciones sin bloqueos de red |

---

## 4. Firmas de Aprobación

```
_____________________________________          _____________________________________
        KAREN YULIANA CAMPO                              GERENCIA GENERAL
           Aprendiz ADSO                          Pizzería Gourmet Bella Italia Popayán
         Ficha SENA: 3186681                               Interesado del Negocio
```
