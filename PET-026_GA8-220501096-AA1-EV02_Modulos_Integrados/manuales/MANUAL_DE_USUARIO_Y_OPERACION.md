# MANUAL DE USUARIO Y GUÍA DE OPERACIÓN
## Sistema de Gestión, Carta y Pedidos - Pizzería Gourmet Bella Italia Popayán
### Evidencia GA8-220501096-AA1-EV02: Módulos Integrados

---

**Aprendiz:** Karen Yuliana Campo  
**Ficha:** 228118 — ADSO  
**CTPI Popayán — SENA Regional Cauca**  

---

## 1. Perfiles de Usuario y Credenciales Semilla

El sistema cuenta con dos roles diferenciados mediante control de acceso RBAC:

| Rol | Usuario | Contraseña | Capacidades y Privilegios en el Sistema |
|---|---|---|---|
| **CLIENTE** | `carlos_cliente` | `Cliente123*` | Explorar carta, personalizar pizzas, aplicar cupones, realizar pedidos y seguimiento en vivo. |
| **ADMIN** | `karencampo` | `Admin123*` | Monitoreo del dashboard de ventas, cambio de estados en cocina, gestión de carta y usuarios. |

---

## 2. Flujo Operativo para el Cliente (Experiencia de Compra)

### 2.1 Inicio de Sesión
1. Ingrese a la aplicación web (`http://localhost:5173`) o móvil (`http://localhost:8081`).
2. Haga clic en el botón superior derecho **"Iniciar Sesión"**.
3. Ingrese sus credenciales. El sistema validará su identidad contra la colección de usuarios de MongoDB y emitirá un token JWT seguro.

### 2.2 Exploración de la Carta Gastronómica
* Utilice los filtros superiores para navegar entre categorías: **Clásicas**, **Gourmet**, **Vegetarianas** y **Especiales**.
* Puede realizar búsquedas inmediatas ingresando palabras clave en el buscador (ej. *"Margherita"*, *"Prosciutto"*, *"Cuatro Quesos"*).
* Cada tarjeta muestra la fotografía, ingredientes, cocción a 380°C y selector de tamaño:
  * **Personal (4 Porciones):** Ideal para una persona.
  * **Mediana (8 Porciones):** Para compartir en pareja.
  * **Familiar (12 Porciones):** Para reuniones familiares.

### 2.3 Carrito de Compras y Aplicación de Cupones
1. Al hacer clic en **"Agregar al Carrito"**, se despliega el Drawer lateral interactivo.
2. En la sección **"Cupón de Descuento"**, ingrese el código promocional institucional:
   * **Código:** `SENA2026`
   * **Beneficio:** 15% de descuento inmediato sobre el subtotal.
3. El sistema valida contra el microservicio Go (`POST /api/cupones/validar`) y recalcula la orden en pantalla.

### 2.4 Checkout y Selección de Medio de Pago
1. Haga clic en **"Confirmar Pedido"**.
2. Ingrese la dirección exacta de entrega en Popayán (ej. *"Calle 5 # 4-22, Centro Histórico"*).
3. Seleccione su medio de pago preferido:
   * **PSE / Nequi / Daviplata:** Transacción electrónica inmediata con comprobante digital.
   * **Tarjeta de Crédito:** Pasarela simulada con confirmación instantánea.
   * **Efectivo contraentrega:** Pago directo al domiciliario.
4. Al pulsar **"Pagar y Enviar Orden"**, se genera el número de orden único (ej. `PED-2026-4821`).

### 2.5 Seguimiento en Vivo (Timeline de 5 Fases)
El cliente puede observar la barra de progreso en tiempo real:
* **Fase 1: RECIBIDO:** Pedido ingresado y confirmado.
* **Fase 2: EN PREPARACIÓN:** Pizzero artesanal estirando la masa madre.
* **Fase 3: EN HORNO:** Cocción a la piedra a 380°C durante 90 segundos.
* **Fase 4: EN CAMINO:** Domiciliario en ruta por las calles de Popayán.
* **Fase 5: ENTREGADO:** ¡Disfrute su auténtica pizza italiana!

---

## 3. Flujo Operativo para el Administrador

### 3.1 Acceso al Dashboard Directivo
1. Inicie sesión con el usuario administrador `karencampo`.
2. Acceda a la pestaña **"Panel Administrativo"**.
3. El dashboard consulta `GET /api/admin/dashboard` y despliega:
   * **Total Ventas Acumuladas ($ COP):** Liquidación financiera en tiempo real.
   * **Pedidos Activos:** Órdenes en cola que requieren atención de la cocina.
   * **Pizzas en Catálogo:** Inventario de especialidades activas.
   * **Clientes Registrados:** Volumen de usuarios en la plataforma.

### 3.2 Gestión de Estados de Pedido
El administrador o jefe de cocina puede cambiar el estado de cualquier orden con un solo clic:
* `RECIBIDO` &rarr; `EN_PREPARACION` &rarr; `EN_HORNO` &rarr; `EN_CAMINO` &rarr; `ENTREGADO`.
* Al cambiar el estado, se genera un registro inmutable con fecha y nota en el historial del pedido en MongoDB.
