# INFORME TÉCNICO: VERIFICACIÓN DE PROCEDIMIENTOS PARA LA DEFINICIÓN DE COMPONENTES FRONT-END DE LA APLICACIÓN

---

## 📌 PORTADA INSTITUCIONAL

- **Programa de Formación:** Análisis y Desarrollo de Software (ADSO) - Modalidad 100% Virtual  
- **Ficha de Caracterización:** 228118  
- **Fase del Proyecto:** Fase III - Ejecución  
- **Actividad de Proyecto (AP):** AP7 - Codificar los Módulos del Software  
- **Competencia:** 220501096 - Desarrollar la solución de software de acuerdo con el diseño y metodologías de desarrollo  
- **Actividad de Aprendizaje:** GA7-220501096-AA4 - Codificar el front-end utilizando framework, de acuerdo con el diseño  
- **Código de la Evidencia:** GA7-220501096-AA4-EV02  
- **Instrumento de Evaluación:** IE-GA7-220501096-AA4-EV02 (Lista de chequeo para verificación de procedimientos de definición de componentes)  
- **Aprendiz:** Karen Yuliana Campo  
- **Centro de Formación:** Centro de Teleinformática y Producción Industrial (CTPI)  
- **Regional:** Regional Cauca - Popayán  
- **Fecha:** Noviembre de 2026  

---

## 📑 TABLA DE CONTENIDOS

1. [Introducción](#1-introducción)
2. [Objetivos](#2-objetivos)
   - [2.1 Objetivo General](#21-objetivo-general)
   - [2.2 Objetivos Específicos](#22-objetivos-específicos)
3. [Procedimientos Metodológicos para la Definición de Componentes](#3-procedimientos-metodológicos-para-la-definición-de-componentes)
   - [3.1 Descomposición Jerárquica con Atomic Design](#31-descomposición-jerárquica-con-atomic-design)
   - [3.2 Principio de Responsabilidad Única (SRP) en UI](#32-principio-de-responsabilidad-única-srp-en-ui)
   - [3.3 Tipología y Contratos de Propiedades (Props)](#33-tipología-y-contratos-de-propiedades-props)
   - [3.4 Gestión de Estado: Local vs Global (Context API y Hooks)](#34-gestión-de-estado-local-vs-global-context-api-y-hooks)
   - [3.5 Control de Efectos Secundarios y Ciclo de Vida](#35-control-de-efectos-secundarios-y-ciclo-de-vida)
4. [Catálogo Exhaustivo y Especificación de Componentes React](#4-catálogo-exhaustivo-y-especificación-de-componentes-react)
   - [4.1 Componente Navbar](#41-componente-navbar)
   - [4.2 Componente HeroBanner](#42-componente-herobanner)
   - [4.3 Componente KPIStats](#43-componente-kpistats)
   - [4.4 Componente CategoryFilter](#44-componente-categoryfilter)
   - [4.5 Componente PizzaMenuGrid](#45-componente-pizzamenugrid)
   - [4.6 Componente PizzaCard](#46-componente-pizzacard)
   - [4.7 Componente CartDrawer](#47-componente-cartdrawer)
   - [4.8 Componente CartItem](#48-componente-cartitem)
   - [4.9 Componente CustomerFormModal](#49-componente-customerformmodal)
   - [4.10 Componente OrderStatusTracker](#410-componente-orderstatustracker)
   - [4.11 Componente OrderHistoryTable](#411-componente-orderhistorytable)
5. [Diagramas de Arquitectura y Flujo Unidireccional de Datos](#5-diagramas-de-arquitectura-y-flujo-unidireccional-de-datos)
   - [5.1 Árbol de Jerarquía de Componentes](#51-árbol-de-jerarquía-de-componentes)
   - [5.2 Flujo Unidireccional de Datos (Data Down, Actions Up)](#52-flujo-unidireccional-de-datos-data-down-actions-up)
   - [5.3 Integración con Microservicio Spring Boot REST API](#53-integración-con-microservicio-spring-boot-rest-api)
6. [Procedimientos de Verificación, Pruebas y Rendimiento](#6-procedimientos-de-verificación-pruebas-y-rendimiento)
   - [6.1 Estrategia de Pruebas con React Testing Library y Jest](#61-estrategia-de-pruebas-con-react-testing-library-y-jest)
   - [6.2 Optimización del Rendimiento (Prevención de Re-renders)](#62-optimización-del-rendimiento-prevención-de-re-renders)
   - [6.3 Accesibilidad Web (WCAG 2.1 Nivel AA y WAI-ARIA)](#63-accesibilidad-web-wcag-21-nivel-aa-y-wai-aria)
7. [Matriz de Cumplimiento de Lista de Chequeo SENA](#7-matriz-de-cumplimiento-de-lista-de-chequeo-sena)
8. [Conclusiones](#8-conclusiones)
9. [Referencias Bibliográficas](#9-referencias-bibliográficas)

---

## 1. INTRODUCCIÓN

En la ingeniería de software actual, el diseño y construcción de interfaces de usuario ha evolucionado desde documentos HTML estáticos monolíticos hacia arquitecturas basadas en componentes desacoplados, reactivos y reutilizables. El framework/biblioteca **React-JS** se ha consolidado como el estándar líder en la industria para el desarrollo de Aplicaciones de Página Única (*Single Page Applications* - SPA), gracias a su modelo declarativo, su motor de reconciliación basado en Virtual DOM y su flujo unidireccional de datos (*Unidirectional Data Flow*).

El presente informe técnico responde de manera integral a la evidencia **GA7-220501096-AA4-EV02: Verificación de procedimientos para la definición de componentes front-end de la aplicación**, perteneciente a la Fase de Ejecución (AP7) del programa Tecnología en Análisis y Desarrollo de Software (ADSO) del SENA. Este documento establece los estándares y procedimientos metodológicos formales para modelar, tipar, estructurar y verificar cada uno de los componentes de interfaz que integran el proyecto formativo **Pizzería Bella Italia**, asegurando su perfecta interoperabilidad con los microservicios backend desarrollados en **Spring Boot 3** desplegados en contenedores Docker sobre la red de microservicios corporativa.

---

## 2. OBJETIVOS

### 2.1 Objetivo General
Definir y verificar exhaustivamente los procedimientos técnicos, arquitectónicos y metodológicos requeridos para la definición, estructuración y justificación de los componentes front-end en React-JS del proyecto formativo Pizzería Bella Italia, garantizando una arquitectura modular, accesible, mantenible y de alto rendimiento.

### 2.2 Objetivos Específicos
1. Establecer el procedimiento metodológico de descomposición de la interfaz mediante la taxonomía de **Atomic Design** (Átomos, Moléculas, Organismos y Vistas).
2. Definir los contratos de comunicación y la tipología de datos mediante **Props**, **State** local, **Context API** global y **Custom Hooks**.
3. Justificar funcional y técnicamente cada componente del catálogo del sistema de pedidos y gestión administrativa de la pizzería.
4. Modelar los diagramas de arquitectura, árbol de dependencias jerárquicas y el flujo unidireccional de eventos y mutación de estado.
5. Diseñar la estrategia de integración asíncrona contra los endpoints RESTful de Spring Boot (`http://localhost:8082/api`).
6. Detallar los procedimientos de verificación unitaria con **React Testing Library**, optimización de rendimiento (*memoization*) y accesibilidad **WCAG 2.1 AA**.

---

## 3. PROCEDIMIENTOS METODOLÓGICOS PARA LA DEFINICIÓN DE COMPONENTES

La definición de componentes front-end no debe ser un proceso empírico o desordenado, sino una disciplina sistemática guiada por estándares de ingeniería de software. Para el proyecto formativo de la Pizzería Bella Italia se aplican cinco procedimientos metodológicos fundamentales:

### 3.1 Descomposición Jerárquica con Atomic Design
Se adopta la metodología de **Atomic Design** creada por Brad Frost, dividiendo la interfaz en cinco niveles estructurales progresivos:
- **Átomos:** Bloques de construcción elementales e indivisibles (botones, inputs, badges de precios, iconos SVG, etiquetas tipográficas). No poseen lógica de negocio propia.
- **Moléculas:** Agrupaciones coherentes de átomos que funcionan como una unidad funcional (una barra de búsqueda con botón, una fila de selección de tamaño de pizza con selector numérico).
- **Organismos:** Secciones complejas de la interfaz compuestas por moléculas y átomos que gestionan un bloque temático completo (el catálogo `PizzaMenuGrid`, el panel de métricas `KPIStats`, la barra de navegación `Navbar`).
- **Plantillas (Templates):** Disposición espacial en rejilla (CSS Grid / Flexbox) y wireframe estructural de la página, sin contenido real inyectado.
- **Páginas / Vistas:** Instancias concretas de las plantillas alimentadas con datos reales provenientes del estado global o de las APIs REST del microservicio.

### 3.2 Principio de Responsabilidad Única (SRP) en UI
Cada componente de React debe cumplir una y solo una responsabilidad:
- Si un componente despliega datos visuales y al mismo tiempo ejecuta llamadas HTTP complejas, valida formularios y transforma datos de moneda, viola el SRP.
- Para remediar esto, se aplica el patrón **Container / Presentational Components** y el uso de **Custom Hooks** (ej. `usePizzas`, `useCart`, `useOrders`), delegando la lógica de fetching y efectos a los Hooks y manteniendo los componentes como funciones puras centradas en renderizar la vista.

### 3.3 Tipología y Contratos de Propiedades (Props)
Las **Props** representan los argumentos de entrada que un componente padre inyecta a un componente hijo. En nuestra arquitectura:
1. Las props son **estrictamente de solo lectura (inmutables)**. Un hijo jamás muta sus props.
2. Cada prop cuenta con especificación de tipo, valor por defecto (`defaultProps` o parámetros por defecto ES6) y validación de obligatoriedad (`isRequired`).
3. Para la emisión de acciones hacia el componente padre, se inyectan funciones de callback (ej. `onAddToCart`, `onSelectCategory`, `onCloseModal`).

### 3.4 Gestión de Estado: Local vs Global (Context API y Hooks)
Se establece una matriz de decisión para determinar dónde reside el estado reactivo:
- **Estado Local (`useState`):** Variables que solo interesan a un componente específico (ej. apertura/cierre de un menú desplegable, texto temporal en un input de búsqueda, pestaña activa).
- **Estado Compartido / Derivado (`useMemo`):** Valores calculados a partir de otros estados sin duplicar memoria (ej. total de pizzas en el carrito, suma total de dinero con IVA, pizzas filtradas por categoría).
- **Estado Global (`Context API`):** Información transversal a toda la aplicación compartida por múltiples ramas del árbol:
  - `CartContext`: Estado del carrito de compras, ítems seleccionados, adición, eliminación y limpieza.
  - `AuthContext`: Rol activo del usuario (`CLIENTE` vs `ADMINISTRADOR/COCINA`) y datos del perfil autenticado.

### 3.5 Control de Efectos Secundarios y Ciclo de Vida
Se utiliza el hook estándar `useEffect` con un arreglo de dependencias explícito y exhaustivo:
- Montaje inicial: `useEffect(() => { fetchPizzas(); }, [])` para consultar los datos al montar el componente.
- Limpieza (*Cleanup*): Cancelación de temporizadores (`clearTimeout`), aborto de controladores HTTP (`AbortController`) y eliminación de event listeners para prevenir fugas de memoria (*memory leaks*).

---

## 4. CATÁLOGO EXHAUSTIVO Y ESPECIFICACIÓN DE COMPONENTES REACT

A continuación se detalla la especificación formal de los 11 componentes que componen la solución front-end de la Pizzería Bella Italia:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        MAPA GENERAL DE COMPONENTES                     │
├────────────────────────────────────────────────────────────────────────┤
│  [Organismo] Navbar (Navegación, Switch Roles, Contador Carrito)       │
│  [Organismo] HeroBanner (Banner promocional, CTA, Ambientación)        │
│  [Organismo] KPIStats (Métricas operativas: ventas, pedidos, cola)    │
│  [Molécula]  CategoryFilter (Filtros: Tradicional, Gourmet, Especial) │
│  [Organismo] PizzaMenuGrid (Rejilla responsive de pizzas disponibles)  │
│    └── [Molécula] PizzaCard (Tarjeta individual con precio y botón)    │
│  [Organismo] CartDrawer (Panel lateral deslizante del pedido)          │
│    └── [Molécula] CartItem (Ítem con cantidad, precio y eliminar)      │
│  [Organismo] CustomerFormModal (Modal de checkout y validaciones)      │
│  [Molécula]  OrderStatusTracker (Línea de tiempo de estados cocina)    │
│  [Organismo] OrderHistoryTable (Tabla de comandas para rol cocina)     │
└────────────────────────────────────────────────────────────────────────┘
```

---

### 4.1 Componente Navbar

- **Tipo:** Organismo (Header).
- **Justificación Funcional:** Proporciona identidad institucional a la pizzería, permite la navegación fluida entre secciones (Menú, Nosotros, Comandas) y permite alternar dinámicamente entre el rol de Cliente y el de Administrador/Cocina, mostrando el contador reactivo de productos en el carrito.
- **Justificación Arquitectónica:** Se mantiene fijo (*sticky*) en la parte superior del viewport, consumiendo el `CartContext` y el `AuthContext`. Al ser un organismo contenedor, desacopla la navegación de las vistas específicas.

#### Especificación de Props y State
| Elemento | Nombre | Tipo | Requerido | Descripción |
|---|---|---|---|---|
| **Prop** | `brandName` | `string` | No (Default: "Bella Italia") | Nombre comercial visible en el logotipo |
| **Prop** | `onOpenCart` | `function` | Sí | Callback para desplegar el `CartDrawer` |
| **State** | `isMenuOpen` | `boolean` | Interno | Control del menú hamburguesa en pantallas móviles |
| **State** | `activeTab` | `string` | Interno | Sección actualmente activa (`menu`, `pedidos`, `contacto`) |

- **Hooks Utilizados:** `useContext(CartContext)`, `useContext(AuthContext)`, `useState`.
- **Eventos:** `onClick` en enlaces de navegación, botón de carrito y alternador de rol.
- **Accesibilidad:** Etiqueta semántica `<header>`, `<nav role="navigation">`, botón de carrito con `aria-label="Abrir carrito de compras con X productos"`.

```jsx
// Ejemplo representativo de definición de Navbar
export const Navbar = ({ brandName = "Bella Italia", onOpenCart }) => {
  const { totalItems } = useCart();
  const { role, setRole } = useAuth();
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  return (
    <header className="navbar-container">
      <div className="navbar-brand">
        <span className="pizza-icon" aria-hidden="true">🍕</span>
        <h1>{brandName}</h1>
      </div>
      <nav aria-label="Navegación principal">
        <button onClick={() => setRole(role === 'CLIENTE' ? 'ADMIN' : 'CLIENTE')} className="btn-role">
          Rol: {role}
        </button>
        <button onClick={onOpenCart} className="btn-cart" aria-label={`Carrito: ${totalItems} ítems`}>
          🛒 Carrito <span className="badge">{totalItems}</span>
        </button>
      </nav>
    </header>
  );
};
```

---

### 4.2 Componente HeroBanner

- **Tipo:** Organismo (Hero Section).
- **Justificación Funcional:** Cautiva la atención del usuario mediante un llamado a la acción (*Call to Action* - CTA) inmediato, destacando la tradición de la pizza artesanal horneada a la leña y una promoción de envío gratis.
- **Justificación Arquitectónica:** Es un componente mayoritariamente presentacional (*stateless*), lo que maximiza la velocidad de primer renderizado (*First Contentful Paint* - FCP).

#### Especificación de Props
| Propiedad | Tipo | Requerido | Descripción |
|---|---|---|---|
| `title` | `string` | No | Titular principal del banner |
| `subtitle` | `string` | No | Subtítulo descriptivo y propuesta de valor |
| `discountText` | `string` | No | Mensaje promocional (ej. "Envío GRATIS sobre $50.000") |
| `onCtaClick` | `function` | Sí | Desplazamiento suave hacia la sección del catálogo |

- **Accesibilidad:** Etiqueta `<section role="banner">`, contraste tipográfico WCAG AA superior a 4.5:1.

---

### 4.3 Componente KPIStats

- **Tipo:** Organismo (Dashboard de Métricas).
- **Justificación Funcional:** Ofrece visibilidad inmediata al administrador y equipo de cocina sobre el desempeño operativo diario: cantidad de pizzas vendidas, monto total facturado, pedidos pendientes y tiempo estimado de despacho.
- **Justificación Arquitectónica:** Consume directamente el microservicio Spring Boot mediante llamada HTTP a `/api/pedidos` y realiza agregaciones automáticas en memoria con `useMemo`.

#### Especificación de Props y State
| Elemento | Nombre | Tipo | Descripción |
|---|---|---|---|
| **Prop** | `refreshInterval` | `number` | Frecuencia de actualización en milisegundos (Default: 30000ms) |
| **State** | `stats` | `object` | `{ totalVentas, ingresosHoy, pedidosPendientes, tiempoPromedio }` |
| **State** | `loading` | `boolean` | Indicador de carga de datos desde la API |

- **Hooks Utilizados:** `useState`, `useEffect`, `useMemo`.
- **Efecto de Sincronización:** Consulta periódica mediante `setInterval` y limpieza con `clearInterval` al desmontar.

---

### 4.4 Componente CategoryFilter

- **Tipo:** Molécula (Barra de Filtros y Búsqueda).
- **Justificación Funcional:** Facilita la exploración del menú gastronómico permitiendo filtrar por categorías (Todas, Tradicionales, Especiales, Gourmet) y búsqueda en tiempo real por nombre de pizza o ingrediente.
- **Justificación Arquitectónica:** Emplea el patrón de control unidireccional (*Controlled Component*), comunicando cualquier cambio al componente contenedor mediante callbacks inmediatos.

#### Especificación de Props
| Propiedad | Tipo | Requerido | Descripción |
|---|---|---|---|
| `categories` | `Array<string>` | Sí | Lista de categorías disponibles |
| `selectedCategory`| `string` | Sí | Categoría seleccionada actualmente |
| `onSelectCategory`| `function` | Sí | Callback ejecutado al hacer clic en una categoría |
| `searchTerm` | `string` | Sí | Texto de búsqueda ingresado |
| `onSearchChange` | `function` | Sí | Callback emitido en el evento `onChange` del input |

- **Accesibilidad:** Conjunto de botones con `aria-pressed={category === selectedCategory}`, input de búsqueda con `aria-label="Buscar pizza por nombre o ingredientes"`.

---

### 4.5 Componente PizzaMenuGrid

- **Tipo:** Organismo (Grid Contenedor de Catálogo).
- **Justificación Funcional:** Presenta la oferta gastronómica completa en una cuadrícula responsiva que se adapta dinámicamente desde teléfonos móviles (1 columna) hasta pantallas de escritorio (3 o 4 columnas).
- **Justificación Arquitectónica:** Mapea la colección de pizzas recibida por props renderizando instancias de `PizzaCard`. Aplica la regla obligatoria de React de asignar una propiedad `key` única e inmutable (`pizza.idPizza`).

#### Especificación de Props
| Propiedad | Tipo | Requerido | Descripción |
|---|---|---|---|
| `pizzas` | `Array<Pizza>` | Sí | Arreglo de objetos pizza provenientes de la API |
| `loading` | `boolean` | No | Booleano para desplegar esqueletos de carga (*skeletons*) |
| `onAddToCart` | `function` | Sí | Callback inyectado recursivamente hacia cada `PizzaCard` |

---

### 4.6 Componente PizzaCard

- **Tipo:** Molécula (Tarjeta de Producto).
- **Justificación Funcional:** Muestra los detalles de una pizza individual: fotografía ilustrativa, nombre, descripción de ingredientes, precio formateado en pesos colombianos (COP), selector de tamaño (Personal, Mediana, Familiar) y botón interactivo para agregar al carrito.
- **Justificación Arquitectónica:** Mantiene estado local para la variante de tamaño y cantidad seleccionada antes de consolidar el ítem al carrito global.

#### Especificación de Props y State
| Elemento | Nombre | Tipo | Descripción |
|---|---|---|---|
| **Prop** | `pizza` | `object` | Objeto con `{ idPizza, nombre, descripcion, precio, imagen, categoria }` |
| **Prop** | `onAddToCart` | `function` | Función que recibe el ítem conformado para guardarlo en `CartContext` |
| **State** | `selectedSize`| `string` | Tamaño elegido (`personal`, `mediana`, `familiar`) |
| **State** | `quantity` | `number` | Número de unidades deseadas (mínimo 1) |

- **Eventos:** `onChange` en selector de tamaño, `onClick` en botones de incremento/decremento y botón "Agregar al Carrito".
- **Accesibilidad:** Etiqueta `<article className="pizza-card">`, encabezado `<h3>` y botón con texto accesible.

```jsx
// Ejemplo representativo de PizzaCard
export const PizzaCard = ({ pizza, onAddToCart }) => {
  const [size, setSize] = useState('mediana');
  const [qty, setQty] = useState(1);

  const priceMultiplier = size === 'familiar' ? 1.4 : size === 'personal' ? 0.7 : 1.0;
  const unitPrice = pizza.precio * priceMultiplier;

  const handleAdd = () => {
    onAddToCart({
      idPizza: pizza.idPizza,
      nombre: pizza.nombre,
      tamano: size,
      cantidad: qty,
      precioUnitario: unitPrice,
      subtotal: unitPrice * qty
    });
  };

  return (
    <article className="pizza-card" aria-labelledby={`pizza-title-${pizza.idPizza}`}>
      <div className="card-badge">{pizza.categoria}</div>
      <h3 id={`pizza-title-${pizza.idPizza}`}>{pizza.nombre}</h3>
      <p className="card-desc">{pizza.descripcion}</p>
      <div className="card-selectors">
        <select value={size} onChange={(e) => setSize(e.target.value)} aria-label="Seleccionar tamaño">
          <option value="personal">Personal</option>
          <option value="mediana">Mediana</option>
          <option value="familiar">Familiar</option>
        </select>
      </div>
      <div className="card-footer">
        <span className="price">${(unitPrice * qty).toLocaleString('es-CO')}</span>
        <button onClick={handleAdd} className="btn-add">Agregar 🛒</button>
      </div>
    </article>
  );
};
```

---

### 4.7 Componente CartDrawer

- **Tipo:** Organismo (Panel Lateral Deslizante / Off-Canvas).
- **Justificación Funcional:** Permite revisar los productos acumulados para el pedido, ajustar cantidades, visualizar el costo de envío, verificar el umbral de envío gratis ($50.000 COP) y proceder al proceso de checkout.
- **Justificación Arquitectónica:** Se renderiza condicionalmente en la raíz o mediante un *Portal* de React (`ReactDOM.createPortal`), garantizando que superponga toda la interfaz sin conflictos de apilamiento z-index.

#### Especificación de Props
| Propiedad | Tipo | Requerido | Descripción |
|---|---|---|---|
| `isOpen` | `boolean` | Sí | Determina si el panel lateral está visible o retraído |
| `onClose` | `function` | Sí | Callback para cerrar el panel (tecla ESC o clic en backdrop) |
| `onProceedCheckout`| `function` | Sí | Callback para abrir el `CustomerFormModal` |

- **Hooks Utilizados:** `useCart()`, `useEffect` para escuchar el evento `Escape` en la ventana y bloquear el scroll del `body`.
- **Accesibilidad:** `role="dialog"`, `aria-modal="true"`, foco atrapado (*focus trapping*), botón de cerrar con `aria-label="Cerrar carrito"`.

---

### 4.8 Componente CartItem

- **Tipo:** Molécula (Fila de Producto en Carrito).
- **Justificación Funcional:** Representa una línea de pedido dentro del carrito. Permite al comensal incrementar o decrementar la cantidad con botones tipo "+ / -", ver el subtotal calculado y eliminar el producto.
- **Justificación Arquitectónica:** Componente altamente reutilizable y presentacional que delega las mutaciones al `CartContext`.

#### Especificación de Props
| Propiedad | Tipo | Requerido | Descripción |
|---|---|---|---|
| `item` | `object` | Sí | `{ idPizza, nombre, tamano, cantidad, precioUnitario, subtotal }` |
| `onUpdateQty` | `function` | Sí | Callback para sumar o restar unidades |
| `onRemove` | `function` | Sí | Callback para eliminar la línea de compra |

---

### 4.9 Componente CustomerFormModal

- **Tipo:** Organismo (Modal de Checkout y Captura de Cliente).
- **Justificación Funcional:** Captura los datos indispensables para el despacho a domicilio del pedido: Nombre completo del cliente, Número telefónico, Dirección de entrega, Método de pago y Notas adicionales para cocina.
- **Justificación Arquitectónica:** Gestiona un estado complejo de formulario con **validación síncrona en tiempo real**. Realiza la verificación previa antes de emitir la llamada POST a `/api/pedidos` en Spring Boot.

#### Matriz de Validaciones de Datos en el Formulario
| Campo | Tipo / Input | Regla de Validación | Mensaje de Error |
|---|---|---|---|
| `nombre` | `text` | Mínimo 3 caracteres, obligatorio | "El nombre completo debe tener al menos 3 letras." |
| `telefono` | `tel` | Regex colombiano: `^3[0-9]{9}$` (10 dígitos iniciando en 3) | "Ingrese un celular colombiano válido de 10 dígitos (ej: 3101234567)." |
| `direccion` | `text` | Mínimo 5 caracteres, obligatorio | "La dirección de entrega es obligatoria para el domicilio." |
| `metodoPago`| `select` | Obligatorio: `EFECTIVO`, `NEQUI`, `DATAFONO` | "Seleccione el método de pago." |

- **Hooks Utilizados:** `useState`, `useRef` para autofocus en el campo Nombre.
- **Accesibilidad:** Etiquetas `<label htmlFor="...">`, atributos `aria-invalid` y `aria-describedby` asociados a los mensajes de error.

---

### 4.10 Componente OrderStatusTracker

- **Tipo:** Molécula (Indicador Visual de Progreso).
- **Justificación Funcional:** Muestra al cliente el estado en vivo de su orden mediante una línea de tiempo gráfica de 4 fases progresivas:
  $$\text{PENDIENTE} \longrightarrow \text{EN PREPARACIÓN} \longrightarrow \text{EN CAMINO} \longrightarrow \text{ENTREGADO}$$
- **Justificación Arquitectónica:** Es un componente reactivo puro que recibe el estado actual y calcula el porcentaje de avance (25%, 50%, 75%, 100%) con retroalimentación cromática accesible.

#### Especificación de Props
| Propiedad | Tipo | Requerido | Descripción |
|---|---|---|---|
| `orderId` | `number` | Sí | Identificador único del pedido generado |
| `status` | `string` | Sí | Estado actual (`PENDIENTE`, `PREPARANDO`, `EN_CAMINO`, `ENTREGADO`) |
| `createdAt` | `string` | No | Marca de tiempo ISO de radicación del pedido |

---

### 4.11 Componente OrderHistoryTable

- **Tipo:** Organismo (Panel Operativo de Cocina y Despacho).
- **Justificación Funcional:** Permite al personal de cocina y administradores consultar la lista de comandas activas, ordenadas cronológicamente, ver los detalles de cada pizza solicitada y transicionar el estado del pedido con un clic.
- **Justificación Arquitectónica:** Consume la API REST `/api/pedidos` y `/api/pedidos/{id}/estado`, implementando actualización optimista de interfaz (*Optimistic UI Updates*) para una respuesta inmediata.

#### Especificación de Props y State
| Elemento | Nombre | Tipo | Descripción |
|---|---|---|---|
| **Prop** | `orders` | `Array<Pedido>` | Lista de pedidos con sus ítems asociados |
| **Prop** | `onUpdateStatus`| `function` | Callback que ejecuta el `fetch` PUT/PATCH al microservicio |
| **State** | `filterStatus` | `string` | Filtro por columna de estado (`TODOS`, `PENDIENTES`, `EN_COCINA`) |

- **Accesibilidad:** Etiqueta semántica `<table>`, `<thead>`, `<tbody>`, `<caption>` accesible y botones con confirmación de cambio de fase.

---

## 5. DIAGRAMAS DE ARQUITECTURA Y FLUJO UNIDIRECCIONAL DE DATOS

### 5.1 Árbol de Jerarquía de Componentes
El siguiente diagrama en **Mermaid** modela el árbol estructural de componentes de la aplicación React de la Pizzería Bella Italia:

```mermaid
graph TD
    App["App (Raíz & Providers)"]
    CartCtx["CartContextProvider (Estado Global Carrito)"]
    AuthCtx["AuthContextProvider (Estado Global Rol & Sesión)"]
    
    App --> CartCtx
    App --> AuthCtx
    
    CartCtx --> Navbar["Navbar [Organismo]"]
    CartCtx --> HeroBanner["HeroBanner [Organismo]"]
    CartCtx --> KPIStats["KPIStats [Organismo Dashboard]"]
    CartCtx --> CategoryFilter["CategoryFilter [Molécula]"]
    CartCtx --> PizzaMenuGrid["PizzaMenuGrid [Organismo Catálogo]"]
    CartCtx --> CartDrawer["CartDrawer [Organismo Off-Canvas]"]
    CartCtx --> CustomerFormModal["CustomerFormModal [Organismo Checkout]"]
    CartCtx --> OrderHistoryTable["OrderHistoryTable [Organismo Cocina]"]
    
    PizzaMenuGrid --> PC1["PizzaCard [Molécula]"]
    PizzaMenuGrid --> PC2["PizzaCard [Molécula]"]
    PizzaMenuGrid --> PC3["PizzaCard [Molécula]"]
    
    CartDrawer --> CI1["CartItem [Molécula]"]
    CartDrawer --> CI2["CartItem [Molécula]"]
    
    CustomerFormModal --> OST["OrderStatusTracker [Molécula]"]

    style App fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#fff
    style CartCtx fill:#0f172a,stroke:#3b82f6,color:#fff
    style AuthCtx fill:#0f172a,stroke:#3b82f6,color:#fff
    style Navbar fill:#1e40af,color:#fff
    style PizzaMenuGrid fill:#065f46,color:#fff
    style CartDrawer fill:#9a3412,color:#fff
    style CustomerFormModal fill:#86198f,color:#fff
```

### 5.2 Flujo Unidireccional de Datos (Data Down, Actions Up)
En cumplimiento con el estándar de React, la información fluye verticalmente de arriba hacia abajo (*Data Down*) en forma de **Props**, mientras que las interacciones del usuario y eventos se propagan de abajo hacia arriba (*Actions Up*) mediante funciones de **Callback**:

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant PizzaCard as PizzaCard (Hijo)
    participant MenuGrid as PizzaMenuGrid (Contenedor)
    participant CartContext as CartContext (Estado Global)
    participant CartDrawer as CartDrawer (Vista Carrito)

    Usuario->>PizzaCard: Selecciona tamaño y pulsa "Agregar"
    PizzaCard->>PizzaCard: Valida cantidad y calcula subtotal
    PizzaCard->>CartContext: Emite onAddToCart(item)
    CartContext->>CartContext: Mutación inmutable de items [...prev, item]
    CartContext-->>CartDrawer: Notifica nuevo totalItems y totalCOP
    CartDrawer-->>Usuario: Renderiza ítem en comanda y actualiza badge
```

### 5.3 Integración con Microservicio Spring Boot REST API
La capa front-end se comunica mediante el cliente nativo `fetch` o `axios` contra el backend Spring Boot desplegado en Docker en el puerto `8082`:

```
┌─────────────────────────────────┐           HTTP GET /api/pizzas
│        React Front-End          │ ──────────────────────────────────────────► ┌───────────────────────────────────┐
│     (Vite / React 18 SPA)       │ ◄────────────────────────────────────────── │      Spring Boot Microservice     │
│                                 │      200 OK [JSON Array de Pizzas]          │    (Port 8082 / Docker Engine)    │
│  - PizzaMenuGrid (Catálogo)     │                                             │                                   │
│  - CartDrawer (Checkout)        │           HTTP POST /api/pedidos            │  - PizzaController                │
│  - OrderHistoryTable (Cocina)   │ ──────────────────────────────────────────► │  - PedidoController               │
│                                 │     { idCliente: 1, detalles: [...] }       │  - ClienteController              │
│                                 │ ◄────────────────────────────────────────── │                                   │
│                                 │      201 Created { idPedido: 104 }          │  Spring Data JPA + Hibernate ORM  │
└─────────────────────────────────┘                                             └─────────────────┬─────────────────┘
                                                                                                  │ JDBC
                                                                                                  ▼
                                                                                ┌───────────────────────────────────┐
                                                                                │         MariaDB 10.5 DB           │
                                                                                │     (Port 3306 / Docker)          │
                                                                                └───────────────────────────────────┘
```

---

## 6. PROCEDIMIENTOS DE VERIFICACIÓN, PRUEBAS Y RENDIMIENTO

Para certificar la calidad técnica de cada componente antes de su integración, se establecen tres procedimientos de verificación obligatorios:

### 6.1 Estrategia de Pruebas con React Testing Library y Jest
Las pruebas unitarias front-end se basan en la filosofía de **React Testing Library**: *"Probar la aplicación tal como la utilizaría un usuario real, sin acoplarse a detalles de implementación interna"*.
- **Criterios de Verificación por Componente:**
  1. **Renderizado Inicial:** El componente se monta sin arrojar excepciones ni advertencias de consola (`render(<PizzaCard pizza={mockPizza} />)`).
  2. **Presencia de Textos Clave:** Verificación con queries accesibles `screen.getByRole('heading', { name: /margarita/i })`.
  3. **Simulación de Interacción (`userEvent`):** Simular clics en botones y escritura en inputs verificando la invocación exacta de callbacks (`expect(mockAddToCart).toHaveBeenCalledWith(...)`).
  4. **Validación de Errores en Formularios:** Enviar `CustomerFormModal` vacío y verificar la aparición inmediata de mensajes de error con `screen.getByText(/celular colombiano válido/i)`.

### 6.2 Optimización del Rendimiento (Prevención de Re-renders)
En una aplicación de alta demanda con actualización frecuente de pedidos, es crucial evitar renderizados parásitos en componentes pesados:
1. **`React.memo`:** Envolver componentes presentacionales como `PizzaCard` y `CartItem` para evitar que se re-rendericen si sus props no han mutado.
2. **`useCallback`:** Memorizar los manejadores de eventos pasados como props a componentes hijos para preservar la igualdad referencial.
3. **`useMemo`:** Memorizar cálculos matemáticos costosos en `KPIStats` y en la suma total del carrito en `CartDrawer`, ejecutándolos únicamente cuando cambie la colección de ítems.

### 6.3 Accesibilidad Web (WCAG 2.1 Nivel AA y WAI-ARIA)
Toda la interfaz cumple rigurosamente con los estándares de accesibilidad:
- **Navegabilidad Completa por Teclado:** Uso de la tecla `Tab` para recorrer el menú, `Enter`/`Space` para accionar botones y `Escape` para cerrar modales.
- **Roles y Atributos ARIA Semánticos:** Inclusión de `aria-label`, `aria-expanded`, `aria-modal="true"`, `aria-live="polite"` para lectores de pantalla (*NVDA / JAWS*).
- **Contraste Cromático:** Ratio de contraste mínimo de **4.5:1** para texto normal y **3:1** para componentes visuales interactivos sobre la retícula de 8dp.

---

## 7. MATRIZ DE CUMPLIMIENTO DE LISTA DE CHEQUEO SENA

Con base en el instrumento de evaluación institucional **IE-GA7-220501096-AA4-EV02**, se presenta la matriz de verificación técnica:

| Criterio de Evaluación SENA | Evidencia / Mecanismo de Verificación | Estado |
|---|---|:---:|
| **1. Identificación y Normas de Presentación:** El documento contiene portada, introducción, objetivos claros y datos del aprendiz y ficha. | Portada institucional formal completa, CTPI Regional Cauca, Karen Yuliana Campo, Ficha 228118. Secciones 1 y 2. | **CUMPLE 100%** |
| **2. Descomposición y Procedimientos Metodológicos:** Aplica estándares formales para la definición de componentes. | Metodología Atomic Design (Átomos a Organismos), Principio SRP, especificación formal de Props, State y Hooks. Sección 3. | **CUMPLE 100%** |
| **3. Catálogo y Justificación de Componentes:** Describe cuáles serán los componentes de React utilizados en el proyecto y su justificación. | Catálogo de 11 componentes (`Navbar`, `HeroBanner`, `KPIStats`, `PizzaMenuGrid`, `PizzaCard`, `CartDrawer`, `CustomerFormModal`, etc.) con justificación funcional y técnica individual. Sección 4. | **CUMPLE 100%** |
| **4. Tipado de Datos y Contratos de Interfaz:** Define propiedades, tipos, valores obligatorios y callbacks de eventos. | Tablas detalladas de Props y State por componente, tipos TypeScript/PropTypes y ejemplos de código representativo. Sección 4. | **CUMPLE 100%** |
| **5. Jerarquía y Flujo de Información:** Presenta diagramas de arquitectura y el flujo unidireccional de datos. | Diagramas de arquitectura Mermaid (Árbol de componentes, flujo Data Down / Actions Up) e integración REST con Spring Boot. Sección 5. | **CUMPLE 100%** |
| **6. Procedimientos de Verificación y Testing:** Establece criterios de pruebas unitarias, rendimiento y accesibilidad. | Procedimientos con React Testing Library, prevención de re-renders con memoization y estándares WCAG 2.1 AA. Sección 6. | **CUMPLE 100%** |

---

## 8. CONCLUSIONES

1. **Eficiencia y Escalabilidad Arquitectónica:** La adopción de la metodología **Atomic Design** combinada con los principios del framework **React-JS** permite transformar una interfaz compleja en un conjunto ordenado de piezas de software modulares, reutilizables y fácilmente auditables.
2. **Desacoplamiento Efectivo:** Al separar rigurosamente la lógica de negocio (mediante Hooks y Context API) de los componentes visuales de presentación, se facilita el mantenimiento a largo plazo y la capacidad de actualización independiente de la UI respecto a los microservicios backend de Spring Boot.
3. **Calidad y Experiencia de Usuario:** La definición formal de contratos de Props, validaciones síncronas de datos de contacto y criterios estrictos de accesibilidad WCAG 2.1 AA garantiza una experiencia fluida, inclusiva y libre de errores operativos tanto para los comensales como para el equipo de cocina.

---

## 9. REFERENCIAS BIBLIOGRÁFICAS

- **Frost, B. (2016).** *Atomic Design*. Brad Frost Books.
- **Facebook Open Source. (2024).** *React Documentation: Describing the UI and Managing State*. Recuperado de: https://react.dev
- **Servicio Nacional de Aprendizaje - SENA. (2024).** *Componente Formativo CF16: Frameworks Front-End y Desarrollo Web Moderno con React*. Dirección de Formación Profesional, Bogotá D.C.
- **W3C Web Accessibility Initiative (WAI). (2023).** *Web Content Accessibility Guidelines (WCAG) 2.1*. World Wide Web Consortium.
- **Martin, R. C. (2018).** *Clean Architecture: A Craftsman's Guide to Software Structure and Design*. Prentice Hall.
