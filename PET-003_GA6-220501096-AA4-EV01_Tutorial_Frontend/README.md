# Evidencia: GA6-220501096-AA4-EV01
## Fundamentos en la implementación de componentes front-end, HTML, CSS, JS

> **Programa:** Análisis y Desarrollo de Software (ADSO)  
> **Ficha:** 228118  
> **Aprendiz:** Karen Yuliana Campo  
> **Competencia:** 220501096 - Desarrollar la solución de software de acuerdo con el diseño y metodologías de desarrollo.  
> **Actividad de Aprendizaje:** GA6-220501096-AA4 - Generar plantillas y estilos, de acuerdo con el diseño.  
> **Producto entregable:** Archivo comprimido ZIP con los archivos del tutorial web (`index.html`, `styles.css`, `tutorial.js`) + Informe Técnico en PDF.

---

## 🎯 1. Descripción de la Evidencia

Según la Guía de Aprendizaje 6 (páginas 12 y 13):
> *"Con base en el siguiente contexto, aplique los principales componentes de HTML y CSS: elabore una página que enseñe un pequeño tutorial seleccionando un tema de su gusto. Establezca un título y emplee una lista ordenada para indicar los distintos conceptos que contiene el tutorial con enlaces a los temas propiamente dichos. Cada tema debe tener su título, imagen y la descripción del tema. Debe incluir los elementos vistos en el componente y utilizar estilos CSS."*

### Tema Seleccionado:
**"Tutorial Didáctico: Fundamentos de Componentes Frontend (HTML5 Semántico, CSS3 y JavaScript Interactivo) para Aplicaciones Web y Móviles"**, alineado al proyecto formativo de la pizzería y al componente formativo institucional **CF16** (*"Herramientas para el diseño y desarrollo móvil híbrido"*).

---

## 📋 2. Temario Desarrollado en la Página

La página web implementa de forma obligatoria una **lista ordenada (`<ol>`)** con enlaces internos que llevan al usuario directamente a cada tema:

1. **Tema 01 - Anatomía y Estructura Semántica con HTML5:**  
   Uso de `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<figure>`, y `<footer>`. Analogía con el esqueleto humano.
2. **Tema 02 - Tipografía, Escala y Jerarquía Visual:**  
   Fuentes Sans-serif para evitar fatiga visual en pantallas, escala tipográfica desde 16px hasta 34px y line-height de 1.6.
3. **Tema 03 - Retícula Espacial (Grid de 8dp) y Margen de 16dp:**  
   Regla matemática de múltiplos de 8dp de Material Design / SENA CF16 para orden y consistencia.
4. **Tema 04 - Teoría del Color, Contraste y Significado Semiótico:**  
   Colores reservados (Rojo peligro, Amarillo alerta, Verde éxito) y colores señaléticos (Blanco, Negro, Azul). Contraste accesible WCAG AA.
5. **Tema 05 - Iconografía, Semiótica y Ley de Fitts:**  
   Botones ergonómicos con área táctil mínima de 48px y las tres dimensiones del ícono (semiótica, semántica y funcional).
6. **Tema 06 - Estructura de Navegación y DCU (ISO 13407):**  
   Navegación lineal, jerárquica y aleatoria, junto con las 4 fases del ciclo de Diseño Centrado en el Usuario.

---

## 💻 3. Características Técnicas de la Aplicación

- **HTML5 Semántico:** Sin abusos de `<div>`, estructura accesible con atributos ARIA y meta etiquetas responsivas.
- **CSS3 Moderno:** Variables CSS en `:root`, sistema Flexbox y Grid, efectos de elevación con sombreados suaves y diseño adaptable (`@media`).
- **Modo Oscuro / Claro:** Alternador interactivo con persistencia local en `localStorage`.
- **Barra de Progreso de Lectura:** Indicador dinámico en la parte superior que mide el scroll.
- **Buscador en Tiempo Real:** Filtro instantáneo de temas mediante JavaScript.
- **Copiador de Código:** Botón en cada bloque de código que copia el snippet al portapapeles con confirmación visual.
- **Botón Flotante:** Acceso rápido para regresar a la parte superior.

---

## 🧪 4. Validación TDD (Test-Driven Development)

Se elaboró una suite de pruebas automatizadas con Node.js Test Runner (`test/tutorial_frontend.test.js`) que verifica:
- Existencia de los archivos fuente requeridos.
- Estructura semántica HTML5 completa.
- Presencia de la lista ordenada `<ol>` con enlaces internos `#tema-X`.
- Integridad de cada una de las tarjetas de temas con título, imagen vectorial SVG y descripción.
- Alineación teórica con el componente formativo SENA CF16 (Ley de Fitts, retícula 8dp, DCU, colores).
- Variables CSS y adaptabilidad responsive.
- Interactividad JavaScript (buscador, modo oscuro, scroll progress).

**Resultado:** **7 de 7 pruebas unitarias aprobadas (100% Green)** en ~30 ms.  
Registro de auditoría: `test/evidencias/test_pass_GA6-220501096-AA4-EV01.txt`.

---

## 📦 5. Archivos de la Evidencia

- [`index.html`](file:///C:/Users/Karen%20Campo/Desktop/SENA/CDE/Evidencias/PET-003_GA6-220501096-AA4-EV01_Tutorial_Frontend/index.html): Documento principal interactivo.
- [`styles.css`](file:///C:/Users/Karen%20Campo/Desktop/SENA/CDE/Evidencias/PET-003_GA6-220501096-AA4-EV01_Tutorial_Frontend/styles.css): Hoja de estilos con variables y retícula de 8dp.
- [`tutorial.js`](file:///C:/Users/Karen%20Campo/Desktop/SENA/CDE/Evidencias/PET-003_GA6-220501096-AA4-EV01_Tutorial_Frontend/tutorial.js): Lógica de interacción y búsqueda.
- `GA6-220501096-AA4-EV01.zip`: Paquete comprimido para subir a la plataforma Zajuna.
- `GA6-220501096-AA4-EV01_Informe_Tecnico.pdf`: Informe técnico formal con evidencias y rúbrica.
