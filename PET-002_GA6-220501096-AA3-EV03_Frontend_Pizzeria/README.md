# INFORME TÉCNICO: INTERFACES GRÁFICAS SEGÚN REQUERIMIENTOS DEL PROYECTO

> **Programa de Formación:** Análisis y Desarrollo de Software (ADSO)  
> **Código del Programa:** 228118  
> **Fase del Proyecto:** Ejecución  
> **Actividad de Proyecto:** AP6 - Desarrollar la estructura de datos y la interfaz de usuario del software  
> **Competencia:** 220501096 - Desarrollar la solución de software de acuerdo con el diseño y metodologías de desarrollo  
> **Resultado de Aprendizaje (RAP):** 220501096-03 - Crear componentes front-end del software de acuerdo con el diseño  
> **Evidencia:** **GA6-220501096-AA3-EV03: Interfaces gráficas según requerimientos del proyecto**  
> **Aprendiz:** Karen Yuliana Campo  
> **Fecha:** Noviembre de 2026  

---

## 1. INTRODUCCIÓN

El presente documento e implementación técnica consolidan el desarrollo de la interfaz gráfica de usuario para el sistema web de **Gestión y Venta de la Pizzería Bella Italia**. Partiendo de los mockups y esquemas de navegación estructurados en la evidencia previa (*GA6-220501096-AA3-EV02*), se materializó una aplicación frontend completamente interactiva y funcional construida bajo estándares modernos de la web (HTML5 semántico, CSS3 modular y JavaScript ES6+), aplicando rigurosamente los principios de usabilidad, diseño centrado en el usuario (norma ISO 13407) y desarrollo guiado por pruebas (**TDD**).

---

## 2. OBJETIVOS

### Objetivo General
Desarrollar e implementar la interfaz gráfica de usuario frontend para el sistema de pedidos y ventas de la pizzería, cumpliendo los requerimientos funcionales, directrices ergonómicas y estándares de usabilidad web establecidos por el SENA.

### Objetivos Específicos
1. Traducir los mockups diseñados en *DesignCraft* a código frontend limpio, responsive y accesible.
2. Aplicar los principios de diseño visual del componente formativo del SENA: retícula de 8dp/16dp, contraste cromático WCAG, jerarquía tipográfica y la Ley de Fitts para optimización táctil.
3. Garantizar la robustez del software mediante una suite de pruebas automatizadas **TDD** ejecutada con `pnpm test`.
4. Empaquetar el producto final en formato comprimido ZIP (`GA6-220501096-AA3-EV03.zip`) con su respectiva documentación para la plataforma de aprendizaje.

---

## 3. FUNDAMENTACIÓN DE USABILIDAD Y DISEÑO VISUAL

En concordancia con el material formativo *"Herramientas para el diseño y desarrollo móvil híbrido"* y *"Desarrollo web con HTML, CSS y JavaScript"*, se incorporaron los siguientes fundamentos:

### 3.1. Códigos Visuales y Paleta Cromática
Se estructuró una paleta basada en colores señaléticos y reservados con alto nivel de contraste:
- **Rojo Artesanal (`#E11D48`):** Color reservado institucional que estimula el apetito y destaca las acciones primarias (*Agregar al Pedido*, *Confirmar Orden*).
- **Amarillo Dorado (`#F59E0B`):** Color de alerta y calidez artesanal, utilizado en insignias de masa tradicional y alertas de envío gratis.
- **Verde Éxito (`#10B981`):** Color señalético para retroalimentación positiva de acciones completadas y confirmación de pagos.
- **Azul y Gris Oscuro (`#0F172A` / `#1E293B`):** Fondo moderno y relajante que reduce la fatiga visual del usuario.
- **Blanco (`#FFFFFF`):** Superficie de tarjetas de contenido que garantiza una legibilidad óptima para personas con dificultades visuales.

### 3.2. Retícula y Espaciado Modular
Se implementó un sistema de espaciado basado en el módulo estándar de **8dp / 16dp** (márgenes laterales de 16px, padding de tarjetas de 24px y separaciones entre secciones de 32px y 48px), asegurando simetría visual y balance armónico en cualquier resolución.

### 3.3. Ley de Fitts y Ergonomía de Interacción
La Ley de Fitts postula que el tiempo necesario para alcanzar un objetivo depende del tamaño del objetivo y de la distancia al mismo:
- Todos los botones principales (*Call-to-Action*) poseen un tamaño vertical superior a **48px**, superando el umbral táctil ergonómico recomendado para pantallas táctiles y dispositivos móviles.
- Los controles de cantidad (`+` y `−`) y el botón del carrito están estratégicamente ubicados para minimizar la distancia de recorrido del cursor o del pulgar del usuario.

### 3.4. Arquitectura de Navegación (ISO 13407)
La navegación de la aplicación es **bidireccional y reversible**:
- El usuario puede moverse fluidamente entre el Login, el Menú interactivo y la Confirmación del Carrito sin perder su estado de compra.
- Permite deshacer o modificar cantidades de pizzas en cualquier momento antes de confirmar.

---

## 4. ESTRUCTURA Y COMPONENTES DEL FRONTEND

La aplicación se compone de tres módulos centrales:

```
FrontEnd_Pizzeria/
├── index.html        # Estructura semántica HTML5 y vistas interactivas (Login, Menú, Checkout, Modal)
├── styles.css        # Hoja de estilos CSS3 moderna con variables CSS, Flexbox, CSS Grid y Media Queries
└── app.js            # Lógica cliente: autenticación, filtrado en vivo, carrito, persistencia y modal
```

### Pantallas Desarrolladas:
1. **Módulo de Autenticación (Login):** Formulario con validación en tiempo real, campos de correo y contraseña, y selector rápido de cuentas demo para el evaluador.
2. **Catálogo de Pizzas (Menú):** Cuadrícula responsiva que exhibe las pizzas reales del proyecto (*Hawaiana Familiar $45.000*, *Pepperoni Mediana $32.000*, *Pollo & Champiñón $38.000*, *Cuatro Quesos $22.000*), con filtros por categoría y buscador instantáneo.
3. **Módulo de Checkout y Despacho:** Resumen de compra con cálculo automático de subtotal, tarifa de envío ($4.000 COP o ¡Envío Gratis si supera $80.000 COP!), formulario de datos de entrega del cliente y selección de métodos de pago.
4. **Modal de Éxito:** Notificación con código de orden generado (`ORD-XXXXXX`), tiempo estimado de entrega (30 a 45 min) y registro automático en el historial de pedidos.
5. **Control de Acceso Basado en Roles (RBAC):**
   - **Vista Cliente (`Carlos Mendoza`):** La pestaña se titula **`🛍️ Mis Pedidos`**, filtrando única y exclusivamente sus compras con indicador visual del estado de despacho.
   - **Vista Administrador (`Karen Campo`):** La pestaña se titula **`📊 Gestión de Órdenes`**, mostrando un **Dashboard KPI con métricas en vivo** (Ingresos Totales, Órdenes en Cocina, En Camino y Entregadas), filtros avanzados y **botones de control de estado en tiempo real** (`👨‍🍳 Cocina` ➔ `🛵 Despachar` ➔ `✅ Entregar`).

---

## 5. VALIDACIÓN MEDIANTE METODOLOGÍA TDD (TEST-DRIVEN DEVELOPMENT)

En estricto cumplimiento del enfoque de calidad de software, la lógica central de negocio fue validada mediante una suite automatizada de **16 pruebas unitarias** ejecutadas con `pnpm test`:

- **Archivo de Pruebas:** [`test/frontend_pizzeria.test.js`](file:///C:/Users/Karen%20Campo/Desktop/SENA/CDE/test/frontend_pizzeria.test.js)
- **Módulo de Lógica:** [`src/pizzeria_logic.js`](file:///C:/Users/Karen%20Campo/Desktop/SENA/CDE/src/pizzeria_logic.js)
- **Registro Oficial de Pruebas Aprobadas:** [`test/evidencias/test_pass_GA6-220501096-AA3-EV03.txt`](file:///C:/Users/Karen%20Campo/Desktop/SENA/CDE/test/evidencias/test_pass_GA6-220501096-AA3-EV03.txt)

### Resultados de la Suite TDD:
- **Pruebas Evaluadas:** 16
- **Suites Evaluadas:** 7
- **Pruebas Aprobadas (Pass):** 16 (100% efectivas)
- **Fallos (Fail):** 0
- **Tiempo de Ejecución:** 15.4 ms

---

## 6. ENTREGABLES DE LA EVIDENCIA

- 📦 **Archivo ZIP Oficial para la Plataforma SENA:**  
  [`GA6-220501096-AA3-EV03.zip`](file:///C:/Users/Karen%20Campo/Desktop/SENA/CDE/Evidencias/PET-002_GA6-220501096-AA3-EV03_Frontend_Pizzeria/GA6-220501096-AA3-EV03.zip)
- 📁 **Código Fuente Listo para Abrir:**  
  [C:\Users\Karen Campo\Desktop\SENA\FrontEnd_Pizzeria](file:///C:/Users/Karen%20Campo/Desktop/SENA/FrontEnd_Pizzeria)
- 🧪 **Registro Test Pass:**  
  [test/evidencias/test_pass_GA6-220501096-AA3-EV03.txt](file:///C:/Users/Karen%20Campo/Desktop/SENA/CDE/test/evidencias/test_pass_GA6-220501096-AA3-EV03.txt)
