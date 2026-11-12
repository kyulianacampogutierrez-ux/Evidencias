# MANUAL TÉCNICO DE ARQUITECTURA Y DESPLIEGUE MÓVIL
## EVIDENCIA GA8-220501096-AA2-EV02: APK (DESARROLLAR MÓDULOS MÓVILES SEGÚN REQUERIMIENTOS DEL PROYECTO)
**Proyecto Formativo:** Pizzería Gourmet Bella Italia Popayán  
**Aprendiz:** Karen Yuliana Campo | **Ficha:** 228118  
**Centro:** Centro de Teleinformática y Producción Industrial (CTPI Popayán) - Regional Cauca  

---

### 1. INTRODUCCIÓN Y ALCANCE
El presente manual documenta la arquitectura técnica, diseño de componentes, flujo de navegación y proceso de compilación de la solución móvil para la **Pizzería Gourmet Bella Italia Popayán**, desarrollada en el marco de la Guía de Aprendizaje 8 del programa ADSO.

La solución aborda la necesidad de ofrecer a los comensales y al personal operativo una experiencia móvil rápida, intuitiva y robusta para la consulta del menú artesanal, personalización de pizzas, aplicación de descuentos institucionales, pago electrónico y trazabilidad en tiempo real de los pedidos.

---

### 2. ARQUITECTURA DE SOFTWARE POR CAPAS (3-TIER MOBILE ARCHITECTURE)
La aplicación móvil se estructura bajo el patrón de arquitectura desacoplada por capas:

1. **Capa 1: Presentación e Interfaz de Usuario (UI/UX):**
   - Vistas móviles construidas con React Native y StyleSheet optimizado.
   - Componentes desacoplados y reutilizables: `PizzaCard`, `CartDrawer`, `SizeSelector`, `OrderTimeline`, `StatusBadge`.
   - Navegación basada en Bottom Tabs (Inicio, Carrito, Pedidos, Perfil) con modales superpuestos para detalle de producto y pago.

2. **Capa 2: Lógica de Negocio y Gestión de Estado:**
   - React Context API con Hooks personalizados (`CartContext`, `AuthContext`).
   - Reglas de negocio: Cálculo de subtotales, límites de descuento de cupones, recargo de envío ($4.000 COP a cualquier sector de Popayán) y transiciones de estados del pedido.
   - Motor de ejecución nativa **Hermes** con compilación anticipada (AOT) a bytecode para arranque instantáneo y bajo consumo de memoria RAM.

3. **Capa 3: Acceso a Datos y Persistencia:**
   - Cliente HTTP `ApiService` para comunicación asíncrona mediante protocolo RESTful y formato JSON con el backend Go Fiber.
   - `AsyncStorage` para almacenamiento persistente local del carrito de compras y estado de sesión.
   - Manejo seguro de autenticación mediante cabeceras `Authorization: Bearer <JWT>`.

4. **Capa 4: Servidores y Base de Datos (Infraestructura de Soporte):**
   - **Backend RESTful:** Go Fiber v2 escuchando en el puerto `8085` (contenedor Docker `sena-backend-go`).
   - **Base de Datos NoSQL:** MongoDB 6 en el puerto `27017` (contenedor Docker `sena-mongodb`).

---

### 3. MAPA DE NAVEGACIÓN Y FLUJO DE USUARIO (MOBILE UX)
El flujo de interacción de la aplicación garantiza una navegación ágil y libre de fricciones:

```text
[SplashScreen] ──► [Menú Principal (HomeScreen)]
                         │
                         ├──► [Modal Detalle Pizza] (Tamaño, adiciones, notas)
                         │          │
                         │          ▼
                         ├──► [Carrito de Compras (CartScreen)]
                         │          │  (Cupón SENA2026, cálculo total)
                         │          ▼
                         ├──► [Checkout & Pasarela] (Nequi, Daviplata, PSE)
                         │          │
                         │          ▼
                         ├──► [Confirmación y Tracking en Vivo]
                         │      (Línea de tiempo: Recibido -> Preparación -> Horno -> Camino -> Entregado)
                         │
                         ├──► [Mi Perfil / Historial] (Datos del cliente, pedidos previos)
                         │
                         └──► [Panel Administrador] (Métricas de ventas y control de cocina)
```

---

### 4. AMBIENTE DE CONSTRUCCIÓN Y OBSERVACIÓN INSTITUCIONAL
Con el fin de mantener la máxima eficiencia en el uso de los recursos de cómputo del aprendiz y garantizar la portabilidad absoluta del pipeline de construcción:

> **OBSERVACIÓN INSTITUCIONAL IMPORTANTE:**  
> Se prescindió formalmente de la instalación de **Android Studio** y sus emuladores en la máquina anfitriona debido a su excesivo tamaño en disco (>15 GB) y alto consumo de memoria RAM.  
> Se utilizó **Visual Studio Code** como entorno de desarrollo integrado (IDE) y un contenedor **Docker aislado (`pizzeria-android-builder:34`)** que aloja OpenJDK 17, Gradle 8.5/9.4.1 y el Android SDK CLI oficial.  
> Para la entrega de la evidencia se generaron y adjuntan dos binarios APK:
> 1. **APK Nativa Java (`pizzeria-bella-italia-nativa.apk`):** Desarrollada con POO y Android SDK API 34 para dar cumplimiento a los lineamientos teóricos de la guía.
> 2. **APK Release Standalone (`pizzeria-bella-italia-rn.apk`):** Compilada para el proyecto formativo en React Native con bundle JS offline embebido, lista para ejecutarse en cualquier dispositivo Android 14+ sin depender de servidores de desarrollo.

---

### 5. ESPECIFICACIONES TÉCNICAS DE LOS BINARIOS MÓVILES (APKs)

| Atributo | APK Nativa Android | APK React Native Release |
|---|---|---|
| **Nombre de Archivo** | `pizzeria-bella-italia-nativa.apk` | `pizzeria-bella-italia-rn.apk` |
| **Tamaño del Archivo** | 12 MB (11.692.872 bytes) | 61 MB (63.214.493 bytes) |
| **Package Name** | `co.edu.sena.pizzerianativa.debug` | `co.edu.sena.pizzeriabellaitalia` |
| **Versión de Android Mínima** | Android 14+ (`minSdkVersion = 34`) | Android 14+ (`minSdkVersion = 34`) |
| **Versión Objetivo (Target)** | Android 14+ (`targetSdkVersion = 34`) | Android 14+ (`targetSdkVersion = 34`) |
| **Versión de Compilación** | `compileSdkVersion = 34` | `compileSdkVersion = 36` |
| **Motor de Ejecución** | Java JVM / ART Nativo | Hermes Bytecode Engine C++ |
| **Empaquetado de Código** | Clases DEX nativas | Bytecode Hermes en `assets/index.android.bundle` (1.28 MB) |
| **Dependencia de Metro** | Ninguna (Autónoma) | **Ninguna (Standalone Offline)** |
| **Seguridad Multi-UID** | Sandbox Linux nativo por aplicación | Sandbox Linux nativo por aplicación |
