# Catálogo Técnico y Especificación de Endpoints REST API
## Sistema de Gestión y Pedidos - Pizzería Bella Italia Popayán
**Evidencia:** GA7-220501096-AA5-EV03 (Diseño y desarrollo de servicios web – proyecto)  
**Programa:** Tecnología en Análisis y Desarrollo de Software (ADSO) - Modalidad Virtual  
**Ficha:** 228118  
**Centro de Formación:** Centro de Teleinformática y Producción Industrial (CTPI Popayán) - Regional Cauca  
**Aprendiz:** Karen Yuliana Campo  
**Stack Tecnológico:** MongoDB 6 NoSQL + Go 1.22 (Fiber v2 + JWT) + Docker Compose  
**URL Base de la API:** `http://localhost:8085` (o `http://192.168.20.21:8085` en red local Wi-Fi)

---

## 1. Resumen General de Endpoints RESTful

| Módulo | Método | Ruta (Endpoint) | Autenticación / Rol | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| **Sistema** | `GET` | `/health` | Público | Verificación del estado del microservicio y base de datos |
| **Sistema** | `GET` | `/api/health` | Público | Metadatos institucionales y versión de la API |
| **Auth** | `POST` | `/api/auth/register` | Público | Registro de nuevos clientes con encriptación Bcrypt |
| **Auth** | `POST` | `/api/auth/login` | Público | Autenticación y generación de token firmado JWT Bearer |
| **Auth** | `GET` | `/api/auth/profile` | Bearer (Cualquier Rol) | Consulta del perfil del usuario autenticado |
| **Carta** | `GET` | `/api/categorias` | Público | Lista de categorías disponibles (Tradicionales, Especiales, etc.) |
| **Carta** | `GET` | `/api/pizzas` | Público | Catálogo completo de pizzas con precios por tamaño |
| **Carta** | `GET` | `/api/pizzas/:codigo` | Público | Detalle de una pizza específica según su código BSON |
| **Cupones** | `POST` | `/api/cupones/validar` | Público | Validación y aplicación de cupón promocional (ej. SENA2026) |
| **Pedidos** | `GET` | `/api/pedidos/:numero` | Público | Consulta y seguimiento (tracking) de orden por número |
| **Pedidos** | `POST` | `/api/pedidos` | Bearer (CLIENTE / ADMIN) | Creación de orden con cálculo de subtotales, cupón y envío |
| **Pedidos** | `GET` | `/api/pedidos/mis-pedidos`| Bearer (CLIENTE / ADMIN) | Historial de pedidos realizados por el usuario en sesión |
| **Pagos** | `POST` | `/api/pagos/procesar` | Público | Simulación de pasarela de pago (Nequi, Daviplata, Tarjeta) |
| **Admin** | `GET` | `/api/admin/dashboard` | Bearer (ADMIN) | Métricas ejecutivas (ventas totales, órdenes activas, usuarios) |
| **Admin** | `GET` | `/api/admin/pedidos` | Bearer (ADMIN) | Lista completa de pedidos de la pizzería con filtros |
| **Admin** | `PUT` | `/api/admin/pedidos/:numero/estado` | Bearer (ADMIN) | Transición de estado en vivo (Recibido → Horno → Entregado) |
| **Admin** | `POST` | `/api/admin/pizzas` | Bearer (ADMIN) | Creación de nuevo producto en el catálogo NoSQL |
| **Admin** | `PUT` | `/api/admin/pizzas/:codigo` | Bearer (ADMIN) | Actualización de ingredientes, descripción o precios |
| **Admin** | `DELETE`| `/api/admin/pizzas/:codigo` | Bearer (ADMIN) | Eliminación lógica/física de pizza del catálogo |
| **Admin** | `GET` | `/api/admin/usuarios` | Bearer (ADMIN) | Lista de usuarios registrados en el sistema |

---

## 2. Detalle de Endpoints por Módulo

### 2.1 Módulo de Autenticación (`/api/auth`)

#### `POST /api/auth/register`
Permite el autoregistro de un nuevo cliente en el sistema. Valida duplicidad de correo o nombre de usuario y almacena la contraseña protegida con Bcrypt.

* **Headers:** `Content-Type: application/json`
* **Request Body:**
```json
{
  "usuario": "karencampo",
  "email": "karen.campo@misena.edu.co",
  "password": "PasswordSena2026*",
  "nombre": "Karen Yuliana Campo",
  "telefono": "+57 312 456 7890",
  "direccion": {
    "alias": "Residencia Popayán",
    "direccion": "Calle 5 # 4-22, Centro Histórico",
    "ciudad": "Popayán",
    "principal": true
  }
}
```
* **Respuesta Exitosa (HTTP 201 Created):**
```json
{
  "mensaje": "Usuario registrado exitosamente",
  "usuario": {
    "id": "67303f8a9b1c2d001e3f4a5b",
    "usuario": "karencampo",
    "email": "karen.campo@misena.edu.co",
    "nombre": "Karen Yuliana Campo",
    "rol": "CLIENTE",
    "activo": true
  }
}
```

---

#### `POST /api/auth/login`
Autentica credenciales de usuario y expide un Token JWT firmado con HMAC-SHA256 que codifica la identidad, correo y rol del usuario.

* **Headers:** `Content-Type: application/json`
* **Request Body:**
```json
{
  "usuario": "karencampo",
  "password": "PasswordSena2026*"
}
```
* **Respuesta Exitosa (HTTP 200 OK):**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "tipo": "Bearer",
  "expiraEn": 86400,
  "usuario": {
    "usuario": "karencampo",
    "email": "karen.campo@misena.edu.co",
    "nombre": "Karen Yuliana Campo",
    "rol": "CLIENTE"
  }
}
```

---

### 2.2 Módulo de Carta y Catálogo (`/api/pizzas`)

#### `GET /api/pizzas`
Retorna el catálogo completo de pizzas napolitanas horneadas a 380°C.

* **Respuesta Exitosa (HTTP 200 OK):**
```json
[
  {
    "id": "673041239b1c2d001e3f4a5c",
    "codigo": "PIZ-MARG-01",
    "nombre": "Margherita Bella Italia",
    "descripcion": "Pomodoro San Marzano, mozzarella fior di latte, albahaca fresca del Huerto de Popayán y aceite de oliva virgen extra.",
    "categoria": "TRADICIONAL",
    "precios": {
      "personal": 22000.0,
      "mediana": 36000.0,
      "familiar": 48000.0
    },
    "disponible": true,
    "imagenUrl": "/assets/pizzas/margherita.jpg"
  }
]
```

---

### 2.3 Módulo de Pedidos y Tracking (`/api/pedidos`)

#### `POST /api/pedidos`
Crea una orden de compra validando los ítems, calculando subtotales, aplicando descuento si existe cupón y calculando el flete de envío en Popayán.

* **Headers:**  
  `Content-Type: application/json`  
  `Authorization: Bearer <jwt_token>`
* **Request Body:**
```json
{
  "items": [
    {
      "pizzaCodigo": "PIZ-MARG-01",
      "tamano": "familiar",
      "precioUnitario": 48000.0,
      "cantidad": 2
    }
  ],
  "cuponCodigo": "SENA2026",
  "direccionEnvio": "Calle 5 # 4-22, Centro Histórico, Popayán",
  "metodoPago": "NEQUI",
  "notas": "Tocar el timbre de la reja blanca."
}
```
* **Respuesta Exitosa (HTTP 201 Created):**
```json
{
  "mensaje": "Pedido creado exitosamente",
  "pedido": {
    "numeroPedido": "PED-2026-003",
    "usuarioCliente": "karencampo",
    "subtotal": 96000.0,
    "descuento": 14400.0,
    "costoEnvio": 4000.0,
    "total": 85600.0,
    "estado": "RECIBIDO",
    "tiempoEstimadoMinutos": 35,
    "historialTracking": [
      {
        "estado": "RECIBIDO",
        "fechaHora": "2026-11-10T21:00:00Z",
        "nota": "Pedido ingresado al sistema central de cocina.",
        "operador": "Sistema Automático"
      }
    ]
  }
}
```

---

#### `GET /api/pedidos/:numero`
Consulta pública de seguimiento en tiempo real de una orden mediante su identificador.

* **Respuesta Exitosa (HTTP 200 OK):**
```json
{
  "numeroPedido": "PED-2026-003",
  "estadoActual": "EN_HORNO",
  "tiempoRestanteMinutos": 18,
  "historial": [
    { "estado": "RECIBIDO", "fechaHora": "2026-11-10T21:00:00Z", "nota": "Orden confirmada" },
    { "estado": "EN_PREPARACION", "fechaHora": "2026-11-10T21:06:00Z", "nota": "Masa fermentada estirada y condimentada" },
    { "estado": "EN_HORNO", "fechaHora": "2026-11-10T21:14:00Z", "nota": "Cocción napolitana a 380°C con leña" }
  ]
}
```

---

### 2.4 Módulo de Administración (`/api/admin`)

#### `PUT /api/admin/pedidos/:numero/estado`
Permite al administrador o jefe de cocina avanzar el estado del pedido en el flujo de 5 fases.

* **Headers:** `Authorization: Bearer <jwt_token_admin>`
* **Request Body:**
```json
{
  "nuevoEstado": "EN_CAMINO",
  "nota": "Repartidor en motocicleta despachado hacia el Centro Histórico de Popayán.",
  "operador": "Administrador Karen"
}
```
* **Respuesta Exitosa (HTTP 200 OK):**
```json
{
  "mensaje": "Estado de pedido actualizado correctamente",
  "numeroPedido": "PED-2026-003",
  "estado": "EN_CAMINO"
}
```
