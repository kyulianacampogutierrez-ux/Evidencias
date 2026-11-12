# MANUAL TÉCNICO DE INTEGRACIÓN DE MÓDULOS DE SOFTWARE
## Sistema de Gestión, Carta y Pedidos - Pizzería Gourmet Bella Italia Popayán
### Evidencia GA8-220501096-AA1-EV01

---

**Aprendiz:** Karen Yuliana Campo  
**Ficha:** 3186681  
**Programa:** Tecnología en Análisis y Desarrollo de Software (ADSO)  
**Centro:** Centro de Teleinformática y Producción Industrial (CTPI Popayán) - Regional Cauca  
**Servicio Nacional de Aprendizaje (SENA)**  

---

## 1. Introducción y Propósito del Sistema

El proyecto formativo **Pizzería Gourmet Bella Italia Popayán** tiene como objetivo dotar al establecimiento gastronómico de una plataforma tecnológica integral y de alto rendimiento que digitalice los procesos comerciales y operativos:
* Publicación dinámica de la carta gastronómica horneada a 380°C.
* Configuración de pizzas personalizadas por tamaño y adiciones.
* Carrito de compras con motor inteligente de cupones de descuento.
* Pasarela de pagos multicanal (Nequi, Daviplata, PSE, Tarjetas y Efectivo contraentrega).
* Sistema de seguimiento en vivo (*tracking*) en 5 estados operativos.
* Consola de administración y analítica en tiempo real para el control de inventario y facturación.

Para alcanzar una arquitectura desacoplada, mantenible y escalable, el sistema adopta una **Arquitectura en Tres Capas (Three-Tier Architecture)** enriquecida con principios de microservicios y contenedores Docker.

---

## 2. Arquitectura Multicapa Integrada

```
+-----------------------------------------------------------------------------------+
|                           CAPA 1: PRESENTACIÓN (FRONTEND)                         |
|  +-------------------------------------+   +------------------------------------+ |
|  |     Aplicación Web SPA (React 18)   |   |   Aplicación Móvil (React Native)  | |
|  | Vite + Tailwind CSS + Lucide Icons  |   | Expo SDK 51 + NativeWind + SafeZone| |
|  | Puerto: 5173                        |   | Puerto: 8081 / Expo Go             | |
|  +-------------------------------------+   +------------------------------------+ |
+------------------------------------------+----------------------------------------+
                                           | HTTP / RESTful (JSON + Bearer JWT)
                                           v
+-----------------------------------------------------------------------------------+
|                        CAPA 2: SERVICIOS Y LÓGICA DE NEGOCIO                      |
|  +-----------------------------------------------------------------------------+  |
|  |                 Microservicio Principal (Go 1.22 + Fiber v2)                |  |
|  |  - AuthHandler & RBAC Security Middleware (Bcrypt + JWT)                    |  |
|  |  - PizzaHandler (Catálogo, Categorías, Filtros dinámicos)                   |  |
|  |  - CuponHandler (Motor de reglas de descuento porcentual)                   |  |
|  |  - PedidoHandler (Checkout, estados de preparación y tracking en vivo)      |  |
|  |  - PagoHandler (Broker de simulación bancaria Nequi/PSE/Tarjetas)           |  |
|  |  - AdminHandler (Dashboard analítico de métricas financieras)               |  |
|  | Puerto: 8085                                                                |  |
|  +-----------------------------------------------------------------------------+  |
|  +-------------------------------------+   +------------------------------------+ |
|  |  Microservicio Spring Boot 3 (Java) |   | Microservicio Auth Node.js Express | |
|  |  CRUD Relacional & Auditoría (8082) |   | Autenticación de Contingencia(8083)| |
|  +-------------------------------------+   +------------------------------------+ |
+------------------------------------------+----------------------------------------+
                                           | Driver Oficial Mongo-Go / JDBC
                                           v
+-----------------------------------------------------------------------------------+
|                       CAPA 3: PERSISTENCIA Y ALMACENAMIENTO                       |
|  +-------------------------------------+   +------------------------------------+ |
|  |       MongoDB 6 Community NoSQL     |   |          MariaDB 10.5 SQL          | |
|  | Motor WiredTiger, BSON Documental   |   | Motor InnoDB, Integridad Relacional| |
|  | Colecciones: usuarios, pizzas,      |   | Tablas: clientes, ordenes_auditoria| |
|  | categorias, cupones, pedidos.       |   | Puerto: 3306                       | |
|  | Puerto: 27017                       |   |                                    | |
|  +-------------------------------------+   +------------------------------------+ |
+-----------------------------------------------------------------------------------+
```

---

## 3. Módulos del Sistema y Responsabilidades

### 3.1 Módulo de Seguridad y Autenticación (`/api/auth`)
* **Protocolo:** JSON Web Token (JWT) con estándar HMAC-SHA256 (`HS256`).
* **Control de Acceso:** Rol-Based Access Control (RBAC) con dos niveles de privilegio:
  * `CLIENTE`: Acceso a consulta de carta, aplicación de cupones, realización de pedidos y seguimiento de órdenes propias.
  * `ADMIN`: Acceso irrestricto al dashboard de analítica comercial, actualización de estados de pedidos en cocina y gestión de usuarios.
* **Seguridad de Credenciales:** Hashing criptográfico mediante Bcrypt con salt rounds de factor 10.

### 3.2 Módulo de Carta Gastronómica y Catálogo (`/api/pizzas`, `/api/categorias`)
* **Modelo de Datos:** Cada especialidad cuenta con atributos de nombre, ingredientes, descripción, categoría, estado destacado y estructura polimórfica de precios según el formato:
  * Personal (4 porciones)
  * Mediana (8 porciones)
  * Familiar (12 porciones)
* **Búsqueda y Filtros:** Búsqueda full-text insensible a mayúsculas/minúsculas mediante operadores `$regex` de MongoDB y ordenamiento por relevancia culinaria.

### 3.3 Módulo de Cupones y Promociones (`/api/cupones/validar`)
* **Reglas de Negocio:**
  * Validación de existencia y estado activo en la base de datos.
  * Comprobación estricta de fecha de vigencia (`expiracion > NOW()`).
  * Cálculo dinámico de descuento porcentual sobre el subtotal de la compra.
  * Límite de descuento máximo (`maxDescuento`) para proteger el margen de contribución de la pizzería.

### 3.4 Módulo de Pedidos y Trazabilidad (`/api/pedidos`)
* **Ciclo de Vida del Pedido en 5 Estados:**
  1. `RECIBIDO`: Orden registrada en el sistema tras el checkout del cliente.
  2. `EN_PREPARACION`: Masa estirada a mano y montaje de ingredientes frescos.
  3. `EN_HORNO`: Cocción artesanal a la piedra a 380°C.
  4. `EN_CAMINO`: Domiciliario asignado en tránsito hacia la dirección en Popayán.
  5. `ENTREGADO`: Pedido recibido a satisfacción por el cliente final.
* **Regla de Domicilio:** Envío gratuito para compras superiores a \$70.000 COP; tarifa plana de \$4.000 COP para pedidos inferiores.

### 3.5 Módulo de Pasarela de Pagos (`/api/pagos/procesar`)
* Simulación bancaria con generación de recibos digitales autorizados (`PAY-<MEDIO>-<TIMESTAMP>`).
* Transición atómica del estado de pago a `APROBADO` y del estado del pedido a `EN_PREPARACION`.
* Soporte nativo para billeteras electrónicas (Nequi, Daviplata), pasarela bancaria PSE, tarjetas de crédito (Visa, Mastercard) y recaudo en efectivo contraentrega.

### 3.6 Módulo de Administración y Analítica (`/api/admin/dashboard`)
* Consolidación en tiempo real de ingresos brutos acumulados, pedidos pendientes en cola de cocina, pedidos despachados, volumen del catálogo y usuarios registrados.

---

## 4. Patrones de Diseño Aplicados

1. **Patrón Arquitectónico en Capas (Layered Architecture):** Clara separación entre controladores HTTP (Handlers), lógica de dominio (Services/Models) y conectores de datos (Database Config).
2. **Patrón Middleware / Interceptor:** Validación perimetral de cabeceras `Authorization: Bearer <token>`, descifrado de claims y verificación de roles antes de acceder a rutas protegidas.
3. **Patrón Singleton:** Gestor de conexión único a la base de datos MongoDB para reutilización eficiente de pools de sockets TCP.
4. **Patrón Data Transfer Object (DTO):** Estructuras especializadas (`CrearPedidoRequest`, `ProcesarPagoRequest`, `ValidarCuponResponse`) que protegen el modelo interno frente a mutaciones del cliente.

---

## 5. Ambientes y Despliegue con Docker

El sistema se orquesta íntegramente en contenedores Docker mediante red puente aislada (`sena-network`):
* `sena-mongodb`: Puerto `27017` (MongoDB 6 Jammy).
* `sena-backend-go`: Puerto `8085` (Go 1.22 Alpine).
* `sena-frontend-vite`: Puerto `5173` (Node 20 Alpine).
* `sena-rn-dev`: Puerto `8081` (Node 22 Alpine para React Native Metro Bundler).
* `sena-auth-service`: Puerto `8083` (Node 20 Alpine para auth microservice).
* `sena-springboot-pizzeria`: Puerto `8082` (Java 17 Spring Boot 3).
* `sena-pizzeria-db`: Puerto `3306` (MariaDB 10.5).
