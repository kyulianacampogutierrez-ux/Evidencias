# Evidencia: GA6-220501096-AA4-EV03
## Diseño front-end que cumpla con los requerimientos del proyecto

> **Programa:** Análisis y Desarrollo de Software (ADSO)  
> **Ficha:** 228118  
> **Aprendiz:** Karen Yuliana Campo  
> **Competencia:** 220501096 - Desarrollar la solución de software de acuerdo con el diseño y metodologías de desarrollo.  
> **Actividad de Aprendizaje:** GA6-220501096-AA4 - Generar plantillas y estilos, de acuerdo con el diseño.  
> **Producto entregable:** Archivo comprimido ZIP con todos los archivos del diseño front-end (`index.html`, `styles.css`, `app.js`) + Informe Técnico en PDF.

---

## 🎯 1. Descripción de la Evidencia

Según la Guía de Aprendizaje 6 (páginas 13 y 14):
> *"Teniendo en cuenta las características del software a desarrollar, realice el diseño front-end cumpliendo con los requisitos del proyecto, aplicando lo visto en el componente formativo. Elementos para tener en cuenta en el documento: El diseño front-end debe aplicar los conceptos de usabilidad y diseño propuesto en las anteriores evidencias. Se debe aplicar HTML, CSS y JS para el diseño front-end. Producto a entregar: archivo ZIP con todos los archivos del diseño front-end."*

---

## 🍕 2. Funcionalidades del Sistema Frontend de la Pizzería

La solución web implementada para la **Pizzería Bella Italia** comprende:

1. **Autenticación con Control de Acceso Basado en Roles (RBAC):**
   - **Cliente (Carlos Mendoza):** Explora menú, arma pedido, verifica dirección y hace seguimiento a sus compras en `🛍️ Mis Pedidos`.
   - **Administradora (Karen Campo):** Acceso al panel de control `📊 Gestión de Órdenes` con indicadores en vivo (KPIs de órdenes totales, en cocina, en ruta, facturación acumulada) y botones para avanzar el estado (*En Preparación* ➔ *En Camino* ➔ *Entregado*).
2. **Catálogo Gastronómico Interactivo:**
   - 6 variedades de pizzas artesanales con selector de tamaño (Personal, Mediana, Familiar) y cálculo reactivo de precios.
   - Filtros instantáneos por categorías (Tradicionales, Especiales, Gourmet) y barra de búsqueda en tiempo real.
3. **Carrito de Compras y Regla de Negocio de Despacho:**
   - Sumatoria dinámica de cantidades, subtotal y valor del domicilio ($4.000 COP).
   - **Envío GRATIS:** Si el subtotal supera los **$80.000 COP**, el costo de envío se reduce automáticamente a $0 y se emite un mensaje de felicitación.
4. **Formulario de Checkout con Validaciones:**
   - Validación de número de teléfono celular colombiano (exactamente 10 dígitos numéricos).
   - Verificación obligatoria de dirección física de entrega y selección de medio de pago.
5. **Persistencia Local y Resiliencia:**
   - Las órdenes y estados persisten en el navegador mediante `localStorage`.
   - Estilos embebidos de respaldo para que la página abra perfectamente incluso desde un visor comprimido de Windows ZIP.

---

## 📐 3. Normas de Diseño Aplicadas (Componente Formativo CF16)

- **Retícula Modular de 8dp:** Espaciados uniformes en múltiplos de 8 píxeles (8px, 16px, 24px, 32px, 48px).
- **Márgenes Perimetrales de 16dp:** Zonas de respiro para diseño adaptable a teléfonos inteligentes.
- **Ley de Fitts:** Altura mínima de 48px en botones táctiles principales para operabilidad óptima con el pulgar.
- **Código Cromático Semiótico:**
  - Rojo (`#ef4444`): Error, eliminación y peligro.
  - Amarillo (`#f59e0b`): Alerta y estado de preparación en horno.
  - Verde (`#10b981`): Confirmación, éxito y entrega de pedidos.
  - Azul (`#0284c7`): Color señalético de interacción y enlaces.

---

## 🧪 4. Validación TDD (Test-Driven Development)

Suite en `test/diseno_frontend_proyecto.test.js` con **7 de 7 pruebas unitarias aprobadas al 100%** (37 pruebas totales de la suite en verde con `pnpm test`):
- `TC01`: Existencia física de archivos fuente (`index.html`, `styles.css`, `app.js`).
- `TC02`: Estructura semántica HTML5 completa y accesible.
- `TC03`: Estilos CSS3 conforme a la retícula 8dp y Ley de Fitts.
- `TC04`: Lógica de carrito y umbral de envío gratis ($80.000 COP).
- `TC05`: Validación de celular de 10 dígitos y dirección de entrega.
- `TC06`: Adaptación visual de vistas y métricas de KPI por rol de usuario.
- `TC07`: Flujo de estados operativos en cocina y despacho.

Registro de auditoría: `test/evidencias/test_pass_GA6-220501096-AA4-EV03.txt`.

---

## 📦 5. Archivos de la Evidencia

- [`index.html`](file:///C:/Users/Karen%20Campo/Desktop/SENA/CDE/Evidencias/PET-005_GA6-220501096-AA4-EV03_Diseno_Frontend_Proyecto/index.html): Maquetación web accesible.
- [`styles.css`](file:///C:/Users/Karen%20Campo/Desktop/SENA/CDE/Evidencias/PET-005_GA6-220501096-AA4-EV03_Diseno_Frontend_Proyecto/styles.css): Hoja de estilos con retícula modular de 8dp.
- [`app.js`](file:///C:/Users/Karen%20Campo/Desktop/SENA/CDE/Evidencias/PET-005_GA6-220501096-AA4-EV03_Diseno_Frontend_Proyecto/app.js): Lógica reactiva de compras, pedidos y roles.
- `GA6-220501096-AA4-EV03.zip`: Archivo comprimido para entrega en Zajuna.
- `GA6-220501096-AA4-EV03_Informe_Tecnico.pdf`: Informe técnico formal con portada y rúbrica.
