# Evidencia: GA6-220501096-AA4-EV02
## Establecer los componentes front-end de la aplicación web

> **Programa:** Análisis y Desarrollo de Software (ADSO)  
> **Ficha:** 228118  
> **Aprendiz:** Karen Yuliana Campo  
> **Competencia:** 220501096 - Desarrollar la solución de software de acuerdo con el diseño y metodologías de desarrollo.  
> **Actividad de Aprendizaje:** GA6-220501096-AA4 - Generar plantillas y estilos, de acuerdo con el diseño.  
> **Producto entregable:** Archivo comprimido ZIP con el documento técnico de especificación de componentes y plantillas HTML.

---

## 🎯 1. Descripción de la Evidencia

Según la Guía de Aprendizaje 6 (página 13):
> *"Con base en las características del software a desarrollar, realice un documento donde especifique la estructura de componentes que se van a utilizar para cumplir con las necesidades del software a desarrollar. Se deben seguir las normas básicas de presentación de un documento escrito, es decir, el documento debe tener como mínimo una portada, introducción, objetivo, definición de elementos HTML a utilizar en el diseño frontend del software a desarrollar. Formato: ZIP."*

---

## 🏛️ 2. Arquitectura de Componentes (Pizzería Bella Italia)

La aplicación web se estructura en un árbol jerárquico de **8 componentes desacoplados**:

1. **`NavbarComponent` (`<header>`, `<nav>`):** Barra superior sticky con logotipo, menú de navegación, badge interactivo del carrito y estado de sesión.
2. **`AuthModalComponent` (`role="dialog"`, `<form>`):** Modal de autenticación accesible con control de acceso por roles (Cliente vs Administrador).
3. **`MenuCatalogComponent` & `PizzaCardComponent` (`<section>`, `<article>`, `<figure>`):** Catálogo en rejilla con selector de tamaño de pizza y cálculo de precio en tiempo real.
4. **`CartDrawerComponent` & `CartItemComponent` (`<aside>`, `<article>`):** Carrito lateral con controles de cantidad (+/-), cálculo de subtotal, envío gratis por compras mayores a $80.000 COP y botón de checkout.
5. **`CheckoutFormComponent` (`<form>`, `<fieldset>`, `<legend>`):** Formulario con validación de celular colombiano (10 dígitos), dirección de entrega y método de pago.
6. **`OrdersDashboardComponent` (`<section>`, `<article>`):** Gestión de pedidos diferenciada: histórico para Cliente (`🛍️ Mis Pedidos`) y panel de KPIs con botones de despacho para Admin (`📊 Gestión de Órdenes`).
7. **`ToastNotificationComponent` (`aria-live="assertive"`):** Notificaciones dinámicas accesibles con colores reservados (éxito verde, error rojo).
8. **`FooterComponent` (`<footer>`):** Cierre semántico con créditos del aprendiz, ficha 228118 y enlaces de contacto.

---

## 📐 3. Tokens de Diseño y Normas del Componente CF16

- **Retícula Modular de 8dp:** Espaciados internos y externos en múltiplos de 8px (8px, 16px, 24px, 32px).
- **Márgenes Laterales de 16dp:** Seguridad perimetral en pantallas móviles.
- **Ley de Fitts:** Altura mínima de 48px para todos los botones táctiles interactivos.
- **Colores Reservados:** Rojo (`#ef4444`) para peligro/error, Amarillo (`#f59e0b`) para alertas, Verde (`#10b981`) para éxito.

---

## 🧪 4. Validación TDD (Test-Driven Development)

Suite en `test/componentes_frontend.test.js` con **7 de 7 pruebas unitarias aprobadas al 100%**:
- Portada, introducción y objetivos formales.
- Árbol de arquitectura de componentes.
- Elementos semánticos HTML5 por componente.
- Atributos de accesibilidad WCAG y WAI-ARIA.
- Principios de diseño del CF16.
- Integridad de las plantillas en `templates/components.html`.

Registro de auditoría: `test/evidencias/test_pass_GA6-220501096-AA4-EV02.txt`.

---

## 📦 5. Archivos de la Evidencia

- [`GA6-220501096-AA4-EV02_Especificacion_Componentes.md`](file:///C:/Users/Karen%20Campo/Desktop/SENA/CDE/Evidencias/PET-004_GA6-220501096-AA4-EV02_Componentes_Frontend/GA6-220501096-AA4-EV02_Especificacion_Componentes.md): Documento técnico completo en Markdown.
- [`GA6-220501096-AA4-EV02_Especificacion_Componentes_Frontend.pdf`](file:///C:/Users/Karen%20Campo/Desktop/SENA/CDE/Evidencias/PET-004_GA6-220501096-AA4-EV02_Componentes_Frontend/GA6-220501096-AA4-EV02_Especificacion_Componentes_Frontend.pdf): Documento formal de alta resolución para Zajuna.
- [`templates/components.html`](file:///C:/Users/Karen%20Campo/Desktop/SENA/CDE/Evidencias/PET-004_GA6-220501096-AA4-EV02_Componentes_Frontend/templates/components.html): Plantillas modulares en código HTML5.
- `GA6-220501096-AA4-EV02.zip`: Archivo comprimido para entrega en Zajuna.
