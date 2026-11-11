# MATRIZ DE INTEGRACIÓN DE COMPONENTES Y MÓDULOS DE SOFTWARE
## Pizzería Gourmet Bella Italia Popayán - Guía 8 (GA8-220501096-AA1-EV01)

| Módulo Funcional | Componente de Presentación (Frontend) | Controlador / Handler (Backend) | Modelo de Dominio / DTO | Capa de Persistencia (MongoDB) | Endpoint REST Integrado |
|---|---|---|---|---|---|
| **Seguridad & Sesión** | `LoginModal.jsx`, `AuthContext.jsx` (Web)<br>`LoginModal.js` (Móvil) | `handlers.Login`, `handlers.GetProfile` | `models.Usuario`, `models.LoginRequest` | Colección `usuarios` | `POST /api/auth/login`<br>`GET /api/auth/profile` |
| **Carta & Catálogo** | `CatalogoPizzas.jsx`, `PizzaCard.jsx` (Web)<br>`MenuScreen.js` (Móvil) | `handlers.GetPizzas`, `handlers.GetCategorias` | `models.Pizza`, `models.Categoria` | Colección `pizzas`, `categorias` | `GET /api/pizzas`<br>`GET /api/categorias` |
| **Cupones de Descuento** | `CarritoDrawer.jsx`, `CuponInput.jsx` (Web)<br>`CartScreen.js` (Móvil) | `handlers.ValidarCupon` | `models.Cupon`, `models.ValidarCuponRequest` | Colección `cupones` | `POST /api/cupones/validar` |
| **Pedidos & Checkout** | `CheckoutModal.jsx`, `CartContext.jsx` (Web)<br>`CheckoutScreen.js` (Móvil) | `handlers.CrearPedido`, `handlers.GetMisPedidos` | `models.Pedido`, `models.ItemPedido`, `models.CrearPedidoRequest` | Colección `pedidos` | `POST /api/pedidos`<br>`GET /api/pedidos/mis-pedidos` |
| **Tracking en 5 Fases** | `OrderTracking.jsx`, `TimelineEstado.jsx` (Web)<br>`TrackingScreen.js` (Móvil) | `handlers.GetPedidoByNumero` | `models.HistorialEstado`, `models.Pedido` | Colección `pedidos` | `GET /api/pedidos/:numero` |
| **Pasarela de Pagos** | `PagoModal.jsx`, `BilleteraDigital.jsx` (Web)<br>`PaymentScreen.js` (Móvil) | `handlers.ProcesarPago` | `models.ProcesarPagoRequest`, `models.ComprobantePago` | Colección `pedidos` (update estadoPago) | `POST /api/pagos/procesar` |
| **Dashboard y Control** | `AdminDashboard.jsx`, `TablaOrdenes.jsx` (Web)<br>`AdminScreen.js` (Móvil) | `handlers.GetDashboardStats`, `handlers.ActualizarEstadoPedido` | `models.ActualizarEstadoRequest` | Colección `pedidos`, `usuarios`, `pizzas` | `GET /api/admin/dashboard`<br>`PUT /api/admin/pedidos/:numero/estado` |

---

### Resumen de Pruebas Unitarias y de Integración:
* **Pruebas de Integración Postman:** 10 peticiones secuenciales, 20 aserciones automatizadas (100% aprobadas).
* **Pruebas Automatizadas TDD:** Suite completa de 180 pruebas unitarias en Node.js Test Runner ejecutadas en contenedor.
