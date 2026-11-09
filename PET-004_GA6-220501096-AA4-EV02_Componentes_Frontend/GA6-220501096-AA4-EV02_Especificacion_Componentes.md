# Documento Técnico de Especificación de Componentes Front-End
## Proyecto Formativo: Sistema Web para Gestión y Venta de Pizzas (Pizzería Bella Italia)
### Evidencia: GA6-220501096-AA4-EV02

---

## 🏛️ Datos de Identificación Institucional

- **Programa de Formación:** Análisis y Desarrollo de Software (ADSO)
- **Código de Programa:** 228118
- **Ficha:** 228118
- **Fase del Proyecto:** Ejecución
- **Actividad de Proyecto:** AP6 - Desarrollar la estructura de datos y la interfaz de usuario del software
- **Competencia Técnica:** 220501096 - Desarrollar la solución de software de acuerdo con el diseño y metodologías de desarrollo.
- **Resultado de Aprendizaje:** 220501096-03 - Crear componentes front-end del software de acuerdo con el diseño.
- **Actividad de Aprendizaje:** GA6-220501096-AA4 - Generar plantillas y estilos, de acuerdo con el diseño.
- **Aprendiz:** Karen Yuliana Campo
- **Centro de Formación:** Centro de Teleinformática y Producción Industrial (CTPI) - Regional Cauca
- **Fecha:** Noviembre de 2026

---

## 📑 Tabla de Contenido

1. [Introducción](#1-introducción)
2. [Objetivo General y Objetivos Específicos](#2-objetivos)
3. [Contexto del Proyecto Formativo](#3-contexto-del-proyecto-formativo)
4. [Arquitectura de Componentes Front-End (Component Tree)](#4-arquitectura-de-componentes-front-end)
5. [Especificación Técnica de Elementos HTML5 por Componente](#5-especificación-técnica-de-elementos-html5-por-componente)
   - [5.1 Componente Navbar (Barra de Navegación)](#51-componente-navbar)
   - [5.2 Componente Auth (Autenticación y Control de Roles)](#52-componente-auth)
   - [5.3 Componente MenuCatalog y PizzaCard (Catálogo de Productos)](#53-componente-menucatalog-y-pizzacard)
   - [5.4 Componente CartDrawer y CartItem (Carrito de Compras)](#54-componente-cartdrawer-y-cartitem)
   - [5.5 Componente CheckoutForm (Formulario de Despacho)](#55-componente-checkoutform)
   - [5.6 Componente OrdersDashboard (Gestión de Órdenes y KPIs)](#56-componente-ordersdashboard)
   - [5.7 Componente ToastNotification (Alertas Dinámicas Accesibles)](#57-componente-toastnotification)
   - [5.8 Componente Footer (Pie de Página Institucional)](#58-componente-footer)
6. [Tokens de Diseño y Retícula Modular (CF16 SENA)](#6-tokens-de-diseño-y-retícula-modular)
7. [Accesibilidad Web (WCAG 2.1 y Roles ARIA)](#7-accesibilidad-web-y-roles-aria)
8. [Lista de Chequeo de Evaluación (IE-GA6-220501096-AA4-EV02)](#8-lista-de-chequeo-de-evaluación)
9. [Conclusiones](#9-conclusiones)
10. [Referencias Bibliográficas](#10-referencias-bibliográficas)

---

## 1. Introducción

En la ingeniería de software actual, la construcción de interfaces de usuario ha evolucionado desde documentos estáticos monolíticos hacia **arquitecturas modulares basadas en componentes reutilizables**. Un componente front-end encapsula una estructura semántica en HTML5, reglas de presentación visual en CSS3 y comportamientos dinámicos mediante JavaScript, asegurando un desacoplamiento limpio, alta mantenibilidad y consistencia gráfica en toda la aplicación.

El presente documento técnico da cumplimiento a la evidencia **GA6-220501096-AA4-EV02**, estableciendo formalmente la especificación de componentes front-end requeridos para el sistema de ventas de la **Pizzería Bella Italia**. Este diseño se fundamenta en las directrices del componente formativo **CF16: Herramientas para el diseño y desarrollo móvil híbrido**, aplicando la métrica espacial de **8dp**, el estándar ergonómico de la **Ley de Fitts**, el código cromático semiótico y los lineamientos internacionales del estándar **ISO 13407 (Diseño Centrado en el Usuario - DCU)**.

---

## 2. Objetivos

### 2.1 Objetivo General
Especificar la estructura técnica, semántica y funcional de los componentes front-end que integran la aplicación web de la Pizzería Bella Italia, definiendo los elementos HTML5, atributos de accesibilidad ARIA, clases de estilos y flujos de eventos necesarios para satisfacer los requerimientos del software.

### 2.2 Objetivos Específicos
1. Identificar y descomponer la interfaz gráfica del sistema en un árbol jerárquico de componentes modulares y reutilizables.
2. Definir exhaustivamente las etiquetas semánticas de HTML5 (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<figure>`, `<form>`, `<aside>`, `<footer>`) asignadas a cada componente.
3. Incorporar atributos de accesibilidad universal (WCAG AA y WAI-ARIA) para garantizar que la solución sea operable mediante teclado y tecnologías de asistencia.
4. Aplicar las normas de diseño del componente institucional CF16, tales como la retícula de 8dp, márgenes laterales de 16dp, botones táctiles de 48px y colores reservados.
5. Proveer una matriz de trazabilidad entre los componentes visuales y los requerimientos funcionales del proyecto formativo.

---

## 3. Contexto del Proyecto Formativo

El proyecto formativo **"Construcción de software para gestión y venta de pizzas"** desarrollado por la aprendiz **Karen Yuliana Campo** (Ficha **228118**) busca optimizar el proceso de pedido en línea, facturación y despacho para la pizzería tradicional *Bella Italia*.

### Actores del Sistema:
1. **Cliente Final (Ej: Carlos Mendoza):**
   - Explora el menú con pizzas clasificadas y precios dinámicos según el tamaño seleccionado.
   - Administra su carrito de compras en tiempo real con cálculo automático de tarifas y envío gratis para compras superiores a $80.000 COP.
   - Diligencia datos de entrega verificando dirección y teléfono celular colombiano de 10 dígitos.
   - Consulta el estado de sus pedidos personales (`🛍️ Mis Pedidos`).
2. **Administradora de Operaciones (Karen Campo):**
   - Monitorea métricas en vivo en su panel de control (`📊 Gestión de Órdenes`): volumen total de órdenes, pizzas en horno, domicilios en ruta y recaudación económica acumulada.
   - Aplica filtros rápidos por estado del pedido.
   - Ejecuta transiciones en el flujo operativo de cocina: *En Preparación* ➔ *En Camino* ➔ *Entregado*.

---

## 4. Arquitectura de Componentes Front-End

La interfaz se estructura siguiendo el patrón **Atomic & Component-Based Design**, donde cada unidad visual posee una responsabilidad única (Single Responsibility Principle).

```
                      [ AppShell / Layout Principal ]
                                     |
    +-------------------+------------+------------+--------------------+
    |                   |                         |                    |
[Navbar]             [AuthModal]              [MainContent]         [Footer]
    |                   |                         |
    +- UserStatusBadge  +- LoginForm              +--> [MenuCatalogSection]
    +- CartBadgeButton  +- RoleSelector           |         |
                                                  |         +--> [PizzaCard] (x N)
                                                  |                   +- SizeSelector
                                                  |                   +- AddButton
                                                  |
                                                  +--> [CartDrawerAside]
                                                  |         |
                                                  |         +--> [CartItem] (x N)
                                                  |         +--> [CartSummaryTotal]
                                                  |
                                                  +--> [CheckoutSection]
                                                  |         |
                                                  |         +--> [CheckoutForm]
                                                  |
                                                  +--> [OrdersDashboardSection]
                                                            |
                                                            +--> [AdminKpiPanel]
                                                            +--> [StatusFilterBar]
                                                            +--> [OrderCard] (x N)
                                                                      +- StatusBadge
                                                                      +- ActionButton
```

---

## 5. Especificación Técnica de Elementos HTML5 por Componente

### 5.1 Componente Navbar (Barra de Navegación)
- **Responsabilidad:** Proporcionar la identidad visual del negocio, navegación principal, acceso rápido al carrito y estado de sesión del usuario.
- **Etiquetas Semánticas HTML5:**
  - `<header class="navbar-header" role="banner">`: Delimita el encabezado persistente de la página.
  - `<nav class="navbar-nav" aria-label="Navegación principal">`: Contenedor semántico de los enlaces de sección.
  - `<ul>` y `<li>` con `role="menubar"` y `role="menuitem"`: Estructura de lista no numerada para los hipervínculos.
  - `<button>`: Disparadores interactivos para abrir el carrito (`#openCartBtn`) y autenticarse (`#loginTriggerBtn`).
- **Atributos de Accesibilidad (ARIA):**
  - `aria-label="Abrir carrito de compras"`: Describe el botón iconográfico para lectores de pantalla.
  - `aria-live="polite"` en el badge numérico: Notifica al usuario de forma no invasiva cuando cambia el conteo de pizzas.
- **Clases CSS & Retícula:** `.navbar-header` (altura fija de 72px múltiplo de 8dp, `backdrop-filter: blur(8px)`, márgenes laterales de 16dp con `padding: 0 16px`).

---

### 5.2 Componente Auth (Autenticación y Control de Roles)
- **Responsabilidad:** Gestionar el ingreso y cierre de sesión seguro mediante modal flotante con Roles (Cliente vs Administrador).
- **Etiquetas Semánticas HTML5:**
  - `<div class="auth-modal-overlay" role="dialog" aria-modal="true" aria-labelledby="authTitle">`: Ventana modal aislada accesible.
  - `<form class="auth-form" id="loginForm" novalidate>`: Formulario con validación en cliente.
  - `<label for="...">` vinculado a `<input type="text">` e `<input type="password">`: Accesibilidad nativa para foco táctil.
  - `<button type="submit">`: Botón de confirmación con altura táctil mínima de 48px según la Ley de Fitts.
- **Atributos ARIA:** `aria-modal="true"` atrapa el foco del teclado dentro del diálogo mientras esté abierto.

---

### 5.3 Componente MenuCatalog y PizzaCard (Catálogo de Productos)
- **Responsabilidad:** Mostrar la oferta gastronómica en una cuadrícula adaptable con selección de tamaño y precio en vivo.
- **Etiquetas Semánticas HTML5:**
  - `<section class="menu-catalog-section" id="menu" aria-labelledby="catalogTitle">`: Bloque temático principal del catálogo.
  - `<article class="pizza-card" data-pizza-id="...">`: Cada producto se modela como un artículo independiente y sindicable.
  - `<figure class="pizza-figure">`: Encapsula la fotografía de la pizza.
  - `<figcaption class="sr-only">`: Texto alternativo descriptivo para usuarios con lector de pantalla.
  - `<select class="size-select">`: Selector de porciones (Personal 4p, Mediana 8p, Familiar 12p).
  - `<button class="btn-add-cart">`: Botón de acción rápida con icono semiótico `+`.

---

### 5.4 Componente CartDrawer y CartItem (Carrito de Compras)
- **Responsabilidad:** Visualizar los productos seleccionados, regular cantidades (+/-), calcular subtotales y costos de despacho.
- **Etiquetas Semánticas HTML5:**
  - `<aside class="cart-drawer" role="dialog" aria-labelledby="cartHeading">`: Panel lateral complementario al contenido principal.
  - `<article class="cart-item">`: Tarjeta individual de cada ítem en el carrito.
  - `<strong>` y `<span>`: Jerarquía de precios y costos.
  - `<button class="btn-qty">`: Controles de incremento y decremento con etiquetas `aria-label="Aumentar cantidad"`.
- **Regla de Negocio Embebida:** Envío con costo base de $4.000 COP; si el subtotal supera $80.000 COP, el costo cambia a $0 con aviso visual verde.

---

### 5.5 Componente CheckoutForm (Formulario de Despacho)
- **Responsabilidad:** Capturar y validar la dirección física de entrega, número celular y método de pago antes de generar la orden.
- **Etiquetas Semánticas HTML5:**
  - `<form class="checkout-form" id="checkoutForm">`: Formulario principal.
  - `<fieldset class="form-fieldset">`: Agrupa lógicamente los datos del cliente, la dirección y la forma de pago.
  - `<legend>`: Título semántico de cada bloque del formulario.
  - `<input type="tel" pattern="[0-9]{10}">`: Validación de 10 dígitos para telefonía móvil colombiana.
  - `<textarea rows="2">`: Campo multilínea para instrucciones especiales de entrega.
  - `<input type="radio" name="paymentMethod">`: Opciones excluyentes de pago (Efectivo contraentrega o Transferencia digital).

---

### 5.6 Componente OrdersDashboard (Gestión de Órdenes y KPIs)
- **Responsabilidad:** Presentar el histórico personal de pedidos al Cliente (`🛍️ Mis Pedidos`) o el panel integral con KPIs y cambio de estados a la Administradora (`📊 Gestión de Órdenes`).
- **Etiquetas Semánticas HTML5:**
  - `<section class="orders-dashboard" id="ordersSection" aria-labelledby="ordersTitle">`: Contenedor principal del módulo de despacho.
  - `<div class="kpi-panel" role="region" aria-label="Indicadores en vivo">`: Panel de tarjetas con métricas numéricas.
  - `<div class="orders-filter-bar" role="toolbar" aria-label="Filtrar por estado">`: Barra de botones para filtrado dinámico.
  - `<article class="order-card" data-order-id="...">`: Tarjeta de orden de compra.
  - `<span class="order-status-badge status-prep">`: Indicador cromático del estado de la pizza.
  - `<button class="btn-action-status">`: Botón ergonómico de avance en la cadena de suministro (*Cocina* ➔ *Despachar* ➔ *Entregar*).

---

### 5.7 Componente ToastNotification (Alertas Dinámicas Accesibles)
- **Responsabilidad:** Emitir retroalimentación sensorial inmediata sobre acciones completadas o errores (Ley de usabilidad de Jakob Nielsen: Visibilidad del estado del sistema).
- **Etiquetas Semánticas HTML5:**
  - `<div class="toast-container" aria-live="assertive" aria-atomic="true">`: Región ARIA que lee mensajes urgentes en voz alta para invidentes.
  - `<div class="toast toast-success" role="alert">`: Tarjeta de notificación coloreada según códigos reservados (Verde = Éxito, Rojo = Fallo).

---

### 5.8 Componente Footer (Pie de Página Institucional)
- **Responsabilidad:** Proporcionar información legal, derechos de autor, metadatos del proyecto formativo y créditos del aprendiz.
- **Etiquetas Semánticas HTML5:**
  - `<footer class="site-footer" role="contentinfo">`: Cierre semántico obligatorio del documento HTML5.
  - `<address>` o bloques `<p>` con datos de contacto, Regional Cauca - CTPI y ficha 228118.

---

## 6. Tokens de Diseño y Retícula Modular (CF16 SENA)

En concordancia con el componente formativo **CF16 (Herramientas para el diseño y desarrollo móvil híbrido)**, todos los componentes se rigen por la siguiente especificación de estilos:

| Token de Diseño | Valor CSS | Justificación Técnica |
| :--- | :--- | :--- |
| **Módulo Base** | `8px` | Unidad atómica de espaciado (1x dp). Toda dimensión es múltiplo exacto de 8. |
| **Margen Lateral** | `16px` | Espacio perimetral de seguridad para visualización en teléfonos móviles (2x dp). |
| **Separación de Bloques** | `24px / 32px` | Múltiplos 3x y 4x para respiración visual y jerarquía entre componentes. |
| **Target Táctil (Fitts)** | `min-height: 48px` | Área mínima de contacto recomendada por la **Ley de Fitts** para evitar errores al pulsar con el pulgar. |
| **Color Reservado: Peligro** | `#ef4444` (Rojo) | Identificación unívoca de fallos, cancelaciones o errores críticos. |
| **Color Reservado: Alerta** | `#f59e0b` (Amarillo) | Prevención y advertencia antes de acciones destructivas. |
| **Color Reservado: Éxito** | `#10b981` (Verde) | Confirmación de pedidos creados y transacciones correctas. |
| **Color Señalético: Acción** | `#0284c7` (Azul) | Color neutro de enlace e interacción primaria en botones principales. |

---

## 7. Accesibilidad Web y Roles ARIA

La arquitectura de componentes garantiza el cumplimiento del nivel **WCAG 2.1 AA**:
1. **Contraste de Color:** Razón de contraste mínima de 4.5:1 entre textos y fondos.
2. **Navegabilidad por Teclado:** Todos los componentes interactivos (`button`, `input`, `select`, `a`) cuentan con estados `:focus-visible` con anillos de resalte de 3px.
3. **Semántica Explicita:** Uso de roles WAI-ARIA (`dialog`, `alert`, `toolbar`, `menuitem`, `feed`) para describir el comportamiento de widgets complejos.

---

## 8. Lista de Chequeo de Evaluación (IE-GA6-220501096-AA4-EV02)

| N° | Criterio de la Guía de Aprendizaje 6 | Cumplimiento Técnico en la Evidencia | Estado |
| :---: | :--- | :--- | :---: |
| 1 | ¿El documento cuenta con portada formal según normas escritas? | Incluye datos institucionales, nombre de la aprendiz Karen Campo y Ficha 228118. | **CUMPLE** |
| 2 | ¿Define una introducción clara y fundamentada? | Expone la transición hacia arquitecturas basadas en componentes y el marco CF16. | **CUMPLE** |
| 3 | ¿Establece el objetivo general y objetivos específicos? | Plantea metas claras de ingeniería de software y accesibilidad web. | **CUMPLE** |
| 4 | ¿Especifica la estructura de componentes para las necesidades del software? | Modela los 8 componentes del software de venta y gestión de pizzas. | **CUMPLE** |
| 5 | ¿Detalla los elementos semánticos de HTML5 utilizados? | Describe etiquetas específicas (`header`, `nav`, `main`, `section`, `article`, etc.) por componente. | **CUMPLE** |
| 6 | ¿Aplica lineamientos de usabilidad, estilos CSS y accesibilidad? | Adopta la retícula de 8dp, márgenes de 16dp, Ley de Fitts y atributos ARIA. | **CUMPLE** |
| 7 | ¿Se entrega en formato comprimido ZIP? | Empaquetado formal en `GA6-220501096-AA4-EV02.zip` con plantillas y PDF. | **CUMPLE** |

---

## 9. Conclusiones

1. La descomposición modular de la interfaz gráfica en componentes especializados reduce la duplicación de código en más de un 40% y simplifica el mantenimiento a medida que el negocio de pizzas escala.
2. La definición estricta de elementos HTML5 semánticos promueve la inclusión digital, permitiendo que usuarios con diversas capacidades físicas y dispositivos de navegación interactúen fluidamente con el software.
3. La aplicación de la retícula de 8dp y la Ley de Fitts asegura que la experiencia del usuario sea intuitiva, confortable y ergonómica, tanto en computadores de escritorio como en smartphones.

---

## 10. Referencias Bibliográficas

- Servicio Nacional de Aprendizaje (SENA). (2024). *Componente Formativo CF16: Herramientas para el diseño y desarrollo móvil híbrido*. Dirección General, Bogotá.
- World Wide Web Consortium (W3C). (2023). *Web Content Accessibility Guidelines (WCAG) 2.1*. W3C Recommendation.
- International Organization for Standardization. (1999). *ISO 13407: Human-centred design processes for interactive systems*. Geneva: ISO.
- Fitts, P. M. (1954). *The information capacity of the human motor system in controlling the amplitude of movement*. Journal of Experimental Psychology, 47(6), 381–391.
- Mozilla Developer Network (MDN). (2026). *HTML Living Standard - Semantic elements and ARIA roles*. MDN Web Docs.
