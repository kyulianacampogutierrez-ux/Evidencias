# MATRIZ DE REQUERIMIENTOS VS. MÓDULOS MÓVILES
## EVIDENCIA GA8-220501096-AA2-EV02: APK (DESARROLLAR MÓDULOS MÓVILES SEGÚN REQUERIMIENTOS DEL PROYECTO)
**Proyecto Formativo:** Pizzería Gourmet Bella Italia Popayán  
**Aprendiz:** Karen Yuliana Campo | **Ficha:** 228118  
**Centro:** Centro de Teleinformática y Producción Industrial (CTPI Popayán) - Regional Cauca  

---

### 1. MATRIZ DE REQUERIMIENTOS FUNCIONALES (RF) EN LA APLICACIÓN MÓVIL

| ID Requerimiento | Descripción del Requerimiento | Módulo Móvil Implementador | Componente / Pantalla React Native | Estado |
|---|---|---|---|:---:|
| **RF-01** | Catálogo digital de pizzas artesanales categorizado (Clásicas, Gourmet, Especiales, Postres, Bebidas). | Módulo Carta / Menú | `CartaMenu.jsx`, `CategoryTabs.jsx`, `PizzaCard.jsx` | **100% CUMPLIDO** |
| **RF-02** | Selección de tamaños de pizza (Personal, Mediana, Familiar) con actualización dinámica de precios. | Módulo Detalle y Configuración | `PizzaModal.jsx`, `SizeSelector.jsx` | **100% CUMPLIDO** |
| **RF-03** | Personalización de ingredientes y adiciones especiales (Borde de queso, champiñones extras, etc.). | Módulo Detalle de Producto | `ToppingsSelector.jsx`, `CustomNotesInput.jsx` | **100% CUMPLIDO** |
| **RF-04** | Carrito de compras interactivo con cálculo automático de subtotales por ítem y total general. | Módulo Carrito de Compras | `CartDrawer.jsx`, `CartItemCard.jsx`, `CartContext.jsx` | **100% CUMPLIDO** |
| **RF-05** | Validación en tiempo real de cupones promocionales (ej. `SENA2026` con 15% de descuento). | Módulo Cupones y Promociones | `CuponInput.jsx`, `useCuponDiscount.js` | **100% CUMPLIDO** |
| **RF-06** | Formulario de checkout con captura de dirección de entrega en Popayán y teléfono de contacto. | Módulo Checkout | `CheckoutModal.jsx`, `AddressInput.jsx` | **100% CUMPLIDO** |
| **RF-07** | Integración de pasarela de pagos móviles simulada (Nequi, Daviplata, PSE, Tarjeta, Efectivo). | Módulo Medios de Pago | `PaymentMethodSelector.jsx`, `PaymentGateway.js` | **100% CUMPLIDO** |
| **RF-08** | Asignación automática de número de orden consecutivo (`PED-2026-XXXX`) tras confirmación. | Módulo Órdenes | `OrderService.js`, `CheckoutModal.jsx` | **100% CUMPLIDO** |
| **RF-09** | Trazabilidad y seguimiento de pedidos en tiempo real con línea de tiempo visual de 5 etapas. | Módulo Tracking en Vivo | `OrderTrackingView.jsx`, `OrderTimeline.jsx` | **100% CUMPLIDO** |
| **RF-10** | Autenticación de clientes y persistencia de sesión segura mediante tokens Bearer JWT. | Módulo Autenticación | `AuthModal.jsx`, `AuthContext.jsx`, `SecureStorage.js` | **100% CUMPLIDO** |
| **RF-11** | Registro de nuevos clientes con validación de datos en Popayán. | Módulo Clientes | `RegisterForm.jsx`, `AuthService.js` | **100% CUMPLIDO** |
| **RF-12** | Consulta de historial de pedidos previos del usuario autenticado. | Módulo Perfil de Usuario | `ClientProfile.jsx`, `OrderHistoryList.jsx` | **100% CUMPLIDO** |
| **RF-13** | Panel de administración móvil con métricas financieras (Ventas totales, pedidos activos). | Módulo Administrador | `AdminDashboard.jsx`, `MetricCard.jsx` | **100% CUMPLIDO** |
| **RF-14** | Actualización de estados de pedidos en cocina por parte del administrador. | Módulo Operaciones | `StatusPicker.jsx`, `AdminOrderRow.jsx` | **100% CUMPLIDO** |
| **RF-15** | Búsqueda predictiva y filtrado de pizzas por texto e ingredientes en tiempo real. | Módulo Búsqueda | `SearchBar.jsx`, `usePizzasCatalog.js` | **100% CUMPLIDO** |

---

### 2. MATRIZ DE REQUERIMIENTOS NO FUNCIONALES (RNF)

| ID | Requerimiento No Funcional | Criterio de Aceptación | Verificación Técnica en la Solución Móvil |
|---|---|---|---|
| **RNF-01** | **Compatibilidad y Plataforma** | Soporte para Android 14+ (`minSdkVersion = 34`). | Verificado mediante `aapt dump badging`: `sdkVersion:'34'`, `targetSdkVersion:'34'`. |
| **RNF-02** | **Rendimiento y Arranque Offline** | Ejecución standalone sin requerir servidor de desarrollo Metro en runtime. | Bytecode JavaScript precompilado con motor Hermes embebido en `assets/index.android.bundle` (1.28 MB). |
| **RNF-03** | **Seguridad y Aislamiento** | Sandboxing multiusuario Linux (UID/GID), almacenamiento seguro y HTTPS/Cleartext restringido. | Permisos acotados en `AndroidManifest.xml` bajo principio de mínimo privilegio. |
| **RNF-04** | **Usabilidad y Accesibilidad** | Interfaz táctil ergonómica con estándares Material Design 3 y tiempos de respuesta < 100 ms. | Botones táctiles de min 48dp, contrastes WCAG AA, animaciones suaves y feedback táctil inmediato. |
| **RNF-05** | **Portabilidad y Despliegue Limpio** | Construcción reproducible en Docker sin instalar Android Studio ni emuladores en la máquina anfitriona. | Contenedor `pizzeria-android-builder:34` con OpenJDK 17 y Gradle 8.5/9.4.1. |

---

### 3. DUALIDAD DE EJECUTABLES MÓVILES (APKs) ENTREGADOS

1. **`pizzeria-bella-italia-rn.apk` (61 MB - Release Standalone):**
   - Aplicación móvil principal del proyecto formativo construida con React Native 0.76+ y Expo.
   - Contiene la totalidad de los 15 Requerimientos Funcionales y la interfaz completa de usuario.
   - Ejecutable optimizado en modo `Release` con bundle offline precompilado que opera de manera autónoma en cualquier dispositivo Android 14+.

2. **`pizzeria-bella-italia-nativa.apk` (12 MB - Nativa Java):**
   - Aplicación móvil nativa en Java POO para Android 14+ (`compileSdk 34`, `targetSdk 34`).
   - Implementa componentes nativos del SDK de Android: `RecyclerView`, `CardView`, ciclo de vida de `Activity` y consumo en memoria.
   - Desarrollada como demostración de dominio de la plataforma nativa Java solicitada en los puntos teóricos del componente formativo.
