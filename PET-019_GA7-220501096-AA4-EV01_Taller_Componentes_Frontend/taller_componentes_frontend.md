# Taller Técnico: Componentes Front-end con React y JSX
## Evidencia de Conocimiento: GA7-220501096-AA4-EV01

---

### 🏛️ Identificación Institucional y Formativa
- **Institución:** Servicio Nacional de Aprendizaje (SENA)
- **Centro de Formación:** Centro de Teleinformática y Producción Industrial (CTPI) - Regional Cauca
- **Programa:** Análisis y Desarrollo de Software (ADSO) - Modalidad 100% Virtual
- **Ficha de Caracterización:** 228118
- **Aprendiz:** Karen Yuliana Campo
- **Ubicación:** Popayán, Cauca, Colombia
- **Actividad de Proyecto:** AP7 - Codificar los módulos del software
- **Actividad de Aprendizaje:** GA7-220501096-AA4: Codificar el front-end utilizando framework, de acuerdo con el diseño.
- **Instrumento de Evaluación:** IE-GA7-220501096-AA4-EV01
- **Fecha de Entrega:** Noviembre de 2026

---

### 1. Introducción y Objetivos

En la ingeniería de software actual, el desarrollo de interfaces de usuario (Frontend) ha experimentado una evolución paradigmática: se abandonó la manipulación directa e imperativa del Document Object Model (DOM) mediante JavaScript puro o bibliotecas tradicionales, dando paso a arquitecturas declarativas basadas en componentes reutilizables y reactivos.

En este contexto, **React** —desarrollada originalmente por Meta (Facebook) y mantenida por una comunidad global de código abierto— se ha consolidado como la tecnología dominante para la construcción de Single Page Applications (SPA), interfaces web dinámicas y aplicaciones móviles multiplataforma.

La presente evidencia da cumplimiento a **GA7-220501096-AA4-EV01**, desarrollando un taller formativo exhaustivo que profundiza en los fundamentos conceptuales de React: la naturaleza sintáctica de **JSX**, el rol histórico y contemporáneo de las **Clases en React** frente a los **Componentes Funcionales con Hooks**, el sistema unificado de **Eventos Sintéticos (`SyntheticEvent`)** y la representación estructural mediante un **Mapa Conceptual** integral.

#### Objetivos del Taller:
1. Analizar las diferencias técnicas, conceptuales y de procesamiento entre la biblioteca React y la extensión sintáctica JSX.
2. Examinar el concepto de clases en React, su ciclo de vida y contrastarlo con la evolución hacia componentes funcionales impulsada por los Hooks.
3. Describir el funcionamiento del sistema de eventos en React, su sintaxis `camelCase`, la delegación de eventos y el objeto unificado `SyntheticEvent`.
4. Diseñar un mapa conceptual representativo de la arquitectura de React, explicando el funcionamiento del Virtual DOM y la reconciliación.
5. Sintetizar las características clave que posicionan a React como el framework líder en la industria de desarrollo de software.

---

### 2. Diferencia entre React y JSX

Uno de los errores más comunes al iniciar en el ecosistema es confundir **React** con **JSX**, considerándolos términos intercambiables. En realidad, corresponden a dos conceptos distintos y complementarios:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       REACT (Biblioteca / Motor Núcleo)                     │
│  - Algoritmo de Reconciliación (Fiber)                                      │
│  - Gestión del Virtual DOM y ciclo de vida de componentes                   │
│  - Métodos API: React.createElement(), useState(), useEffect()              │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       ▲ Transpilación (Babel / Vite / SWC)
                                       │ transforma etiquetas en llamadas JS
┌──────────────────────────────────────┴──────────────────────────────────────┐
│                  JSX (JavaScript XML - Extensión Sintáctica)                │
│  - Azúcar sintáctico (Syntactic Sugar) para escribir HTML dentro de JS      │
│  - Declarativo, seguro contra XSS y validado en tiempo de compilación       │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### 2.1. ¿Qué es React?
React es una **biblioteca de JavaScript** creada para construir interfaces de usuario interactivas y declarativas. Su principio fundamental radica en dividir la pantalla en piezas independientes y aisladas llamadas **componentes**. React administra un árbol en memoria conocido como el **Virtual DOM**, calculando de manera eficiente las diferencias mínimas (*diffing*) necesarias para sincronizar la interfaz visual con el DOM real del navegador.

#### 2.2. ¿Qué es JSX?
**JSX (JavaScript XML)** es una **extensión de la sintaxis estándar de JavaScript (ECMAScript)**. Permite a los desarrolladores describir la apariencia y estructura de la interfaz utilizando una sintaxis casi idéntica a HTML directamente dentro del código JavaScript. 

Es fundamental recalcar que **JSX no es código HTML real ni es interpretado nativamente por los navegadores web**. Se trata de azúcar sintáctico (*syntactic sugar*): durante el proceso de empaquetado (*build time*), herramientas como **Babel**, **SWC** o **esbuild** transforman cada etiqueta JSX en invocaciones a funciones puras de JavaScript mediante `React.createElement()`.

#### 2.3. Demostración Técnica: Código JSX vs. Transpilación a JavaScript Puro

A continuación se contrasta la declaración de una tarjeta de pizza del proyecto formativo:

**Sintaxis con JSX (Código fuente del desarrollador):**
```jsx
const TarjetaPizza = ({ nombre, precio, tamano }) => (
  <div className="card-pizza">
    <h3 className="pizza-titulo">{nombre}</h3>
    <span className="pizza-tamano">{tamano}</span>
    <p className="pizza-precio">${precio} COP</p>
    <button onClick={() => agregarAlPedido(nombre)} className="btn-ordenar">
      Ordenar Ahora
    </button>
  </div>
);
```

**Resultado de Transpilación por Babel (JavaScript puro ejecutado por el navegador):**
```javascript
const TarjetaPizza = ({ nombre, precio, tamano }) => {
  return React.createElement(
    "div",
    { className: "card-pizza" },
    React.createElement("h3", { className: "pizza-titulo" }, nombre),
    React.createElement("span", { className: "pizza-tamano" }, tamano),
    React.createElement("p", { className: "pizza-precio" }, "$" + precio + " COP"),
    React.createElement(
      "button",
      {
        onClick: () => agregarAlPedido(nombre),
        className: "btn-ordenar"
      },
      "Ordenar Ahora"
    )
  );
};
```

#### 2.4. Matriz Comparativa: React vs. JSX

| Criterio | React | JSX |
|---|---|---|
| **Definición** | Biblioteca de JavaScript para construir interfaces de usuario. | Extensión sintáctica de ECMAScript para escribir marcas declarativas. |
| **Rol en el Sistema** | Motor de reconciliación, gestión de estado, renderizado y ciclo de vida. | Notación visual para describir árboles de elementos de forma legible. |
| **Ejecución en Navegador** | Código JS ejecutable en tiempo de ejecución (*Runtime*). | Requiere transpilación previa con Babel/Vite; no se ejecuta directamente. |
| **Seguridad XSS** | Implementa escape automático de variables antes de inyectar en el DOM. | Evita ataques de inyección al convertir strings en texto plano antes de renderizar. |
| **Obligatoriedad** | Obligatorio para construir la aplicación. | Opcional (se puede programar con `React.createElement`, aunque es impráctico). |

---

### 3. ¿Qué son Clases en React y su Evolución con Hooks?

#### 3.1. Definición y Estructura de Componentes de Clase
En las primeras versiones estables de React (anteriores a la versión 16.8), la única forma de crear componentes que tuvieran **estado propio (*state*)** o que pudieran reaccionar a las etapas del **ciclo de vida (*lifecycle*)** era mediante **Clases de JavaScript (ES6)** que heredaban de la clase base `React.Component`:

```jsx
import React, { Component } from 'react';

class ContadorPedidos extends Component {
  constructor(props) {
    super(props);
    // Estado inicial en el constructor
    this.state = {
      cantidad: 1,
      precioUnitario: 28000
    };
    // Enlace explícito del contexto 'this'
    this.incrementar = this.incrementar.bind(this);
  }

  componentDidMount() {
    console.log("Componente montado en el DOM real");
  }

  componentWillUnmount() {
    console.log("Limpieza de recursos antes de desmontar");
  }

  incrementar() {
    this.setState(prevState => ({ cantidad: prevState.cantidad + 1 }));
  }

  // Método obligatorio de renderizado
  render() {
    const total = this.state.cantidad * this.state.precioUnitario;
    return (
      <div className="card-pedido">
        <p>Pizzas seleccionadas: {this.state.cantidad}</p>
        <p>Subtotal: ${total} COP</p>
        <button onClick={this.incrementar}>+ Añadir Otra</button>
      </div>
    );
  }
}
```

#### 3.2. Las Tres Fases del Ciclo de Vida en Clases
1. **Fase de Montaje (*Mounting*):**
   - `constructor()`: Inicialización del estado y binding de métodos.
   - `render()`: Retorna la representación visual del Virtual DOM.
   - `componentDidMount()`: Se ejecuta inmediatamente después de que el elemento entra en el DOM. Ideal para llamados a APIs REST o suscripciones.
2. **Fase de Actualización (*Updating*):**
   - `shouldComponentUpdate()`: Optimización de rendimiento para autorizar o denegar el re-renderizado.
   - `componentDidUpdate()`: Invocado tras actualizarse el estado o los props.
3. **Fase de Desmontaje (*Unmounting*):**
   - `componentWillUnmount()`: Limpieza de temporizadores, cancelaciones de peticiones o desconexión de websockets.

#### 3.3. La Evolución Moderna: Componentes Funcionales y Hooks
A partir de **React 16.8 (2019)**, el equipo de React introdujo los **Hooks**. Los Hooks permiten utilizar estado y características de ciclo de vida en **funciones puras de JavaScript**, sin necesidad de escribir clases:

```jsx
import React, { useState, useEffect } from 'react';

const ContadorPedidosFuncional = () => {
  const [cantidad, setCantidad] = useState(1);
  const precioUnitario = 28000;

  useEffect(() => {
    console.log("Efecto ejecutado (reemplaza componentDidMount/Update)");
    return () => console.log("Limpieza (reemplaza componentWillUnmount)");
  }, [cantidad]);

  return (
    <div className="card-pedido">
      <p>Pizzas seleccionadas: {cantidad}</p>
      <p>Subtotal: ${cantidad * precioUnitario} COP</p>
      <button onClick={() => setCantidad(c => c + 1)}>+ Añadir Otra</button>
    </div>
  );
};
```

#### 3.4. Tabla Comparativa: Clases vs. Componentes Funcionales con Hooks

| Característica | Componentes de Clase (`React.Component`) | Componentes Funcionales Modernos con Hooks |
|---|---|---|
| **Sintaxis** | Clases ES6 con herencia y método `render()`. | Funciones JavaScript estándar (`function` o arrow `=>`). |
| **Manejo de Estado** | Objeto `this.state` y llamada a `this.setState()`. | Hook `useState()` desestructurado en variable y función mutadora. |
| **Ciclo de Vida** | Métodos dispersos (`componentDidMount`, `Update`, `Unmount`). | Unificado y declarativo mediante el Hook `useEffect()`. |
| **Manejo del `this`** | Requiere enlaces explícitos (`.bind(this)`) en constructor. | No existe el problema de contexto `this`; ámbito léxico puro. |
| **Reutilización de Lógica** | Patrones complejos: High-Order Components (HOC) y Render Props. | Sencilla y elegante mediante **Custom Hooks** personalizados. |
| **Estado en la Industria** | En modo mantenimiento / código legado. | **Estándar oficial y recomendado por React**. |

---

### 4. Principales Eventos en React y Sistema SyntheticEvent

El manejo de interacciones del usuario en React se realiza mediante un sistema propio de eventos diseñado para garantizar rendimiento y consistencia multiplataforma.

#### 4.1. ¿Qué es `SyntheticEvent`?
React no vincula directamente manejadores de eventos nativos en cada nodo del DOM real. En su lugar, implementa un objeto contenedor envolvente denominado **`SyntheticEvent`**. 

Este objeto normaliza las inconsistencias entre diferentes navegadores (Chrome, Firefox, Safari, Edge), asegurando que las propiedades y métodos del evento (como `e.target`, `e.preventDefault()`, `e.stopPropagation()`) sigan estrictamente la especificación W3C en cualquier entorno.

#### 4.2. Diferencias Fundamentales con el DOM HTML Nativo:
1. **Nomenclatura camelCase:** Los eventos en React usan sintaxis camelCase (`onClick`, `onChange`, `onSubmit`, `onKeyDown`) en lugar de minúsculas nativas (`onclick`, `onchange`).
2. **Paso de Funciones como Handlers:** En HTML se pasa una cadena (`onclick="guardar()"`), mientras que en React se pasa una **referencia a la función** entre llaves (`onClick={guardar}`).
3. **Prevención de Comportamientos por Defecto:** En HTML se podía retornar `false` dentro de la etiqueta. En React es mandatorio llamar explícitamente a `e.preventDefault()`.

#### 4.3. Catálogo de los Principales Eventos en React

A continuación se presentan los eventos más relevantes del framework, clasificados por categoría y ejemplificados en el contexto de la **Pizzería Bella Italia**:

| Categoría | Evento React | Descripción | Ejemplo de Uso en Pizzería Bella Italia |
|---|---|---|---|
| **Mouse (Ratón)** | `onClick` | Se dispara al pulsar y soltar un botón del ratón. | Pulsar el botón para agregar pizza al carrito. |
| | `onMouseEnter` / `onMouseLeave` | Detección de cursor sobre un elemento. | Efecto visual de zoom o destaque de especialidad. |
| | `onDoubleClick` | Doble clic rápido sobre un elemento. | Abrir ficha técnica detallada de ingredientes. |
| **Formularios** | `onChange` | Disparado cuando el valor de un `<input>`, `<select>` o `<textarea>` cambia. | Componente controlado: captura del nombre, teléfono o dirección en tiempo real. |
| | `onSubmit` | Disparado al enviar un `<form>`. | Validación de comanda antes de invocar la API REST. |
| | `onFocus` / `onBlur` | Elemento gana o pierde el foco. | Mostrar advertencia visual si el teléfono no tiene 10 dígitos al salir del input. |
| **Teclado** | `onKeyDown` | Disparado al presionar una tecla. | Detectar tecla `Enter` para filtrar catálogo o `Esc` para cerrar modal. |
| | `onKeyUp` | Disparado al soltar una tecla. | Actualización de contador de caracteres en la dirección. |
| **Portapapeles** | `onCopy` / `onPaste` | Detección de copiado o pegado. | Validar que el cupón de descuento pegado sea alfanumérico. |
| **Táctiles (Mobile)** | `onTouchStart` / `onTouchEnd` | Interacciones en pantallas móviles táctiles. | Deslizar lateralmente (*swipe*) el catálogo de pizzas en teléfonos. |

#### 4.4. Ejemplo Práctico: Formulario de Pedido con Control de Eventos
```jsx
const FormularioCliente = () => {
  const [formData, setFormData] = useState({ nombre: '', telefono: '' });

  const handleChange = (e) => {
    // SyntheticEvent normalizado
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault(); // Evita que la página se refresque
    console.log("Enviando cliente a la API Spring Boot:", formData);
  };

  return (
    <form onSubmit={handleSubmit} className="formulario-pizzeria">
      <input
        type="text"
        name="nombre"
        placeholder="Nombre Completo"
        value={formData.nombre}
        onChange={handleChange}
      />
      <input
        type="tel"
        name="telefono"
        placeholder="Teléfono"
        value={formData.telefono}
        onChange={handleChange}
      />
      <button type="submit">Guardar Cliente</button>
    </form>
  );
};
```

---

### 5. Mapa Conceptual de la Arquitectura de React

A continuación se estructura el mapa conceptual que sintetiza las relaciones, flujo de datos y piezas arquitectónicas de React:

```
                               ┌─────────────────────────────────┐
                               │       REACT ECOSYSTEM (SPA)     │
                               └────────────────┬────────────────┘
                                                │
         ┌──────────────────────────────────────┼──────────────────────────────────────┐
         ▼                                      ▼                                      ▼
┌──────────────────┐                  ┌──────────────────┐                   ┌──────────────────┐
│  PARADIGMA BASE  │                  │ VIRTUAL DOM (VDOM│                   │ GESTIÓN DE DATOS │
└────────┬─────────┘                  └────────┬─────────┘                   └────────┬─────────┘
         │                                     │                                      │
 ┌───────┴───────┐                    ┌────────┴────────┐                    ┌────────┴────────┐
 │ - Declarativo │                    │ - Copia Ligera  │                    │ - Props: Inmut. │
 │ - Componentes │                    │ - Reconciliación│                    │   (Padre a Hijo)│
 │ - Sintaxis JSX│                    │   (Diffing)     │                    │ - State: Mutable│
 │   (Babel)     │                    │ - Algoritmo     │                    │   (useState)    │
 └───────────────┘                    │   React Fiber   │                    │ - Unidirectional│
                                      │ - Batch Updates │                    │   Data Flow     │
                                      └────────┬────────┘                    └─────────────────┘
                                               │ Modifica de forma eficiente
                                               ▼
                                      ┌──────────────────┐
                                      │  DOM REAL (HTML) │
                                      │  (Navegador Web) │
                                      └──────────────────┘
                                               ▲
                                               │ Dispara eventos
                                      ┌────────┴────────┐
                                      │  SyntheticEvent │
                                      │ - onClick       │
                                      │ - onChange      │
                                      │ - onSubmit      │
                                      └─────────────────┘
```

#### Explicación de los Nodos del Mapa Conceptual:
1. **Componentes y JSX:** La interfaz se descompone en módulos autónomos que retornan JSX. Babel los compila a JavaScript ejecutable.
2. **Virtual DOM y Reconciliación:** Cada mutación de estado crea una nueva versión del árbol virtual. El algoritmo **React Fiber** compara el árbol previo con el nuevo (*Diffing*), calcula la diferencia mínima y aplica un único lote de actualizaciones al DOM real (*Batch Rendering*), eliminando repintados costosos.
3. **Flujo Unidireccional de Datos (*One-Way Data Flow*):** Los datos descienden desde componentes padres hacia hijos mediante **Props** (inmutables). Las modificaciones del estado se encapsulan mediante **State** (`useState`) y se comunican hacia arriba mediante funciones callbacks.
4. **SyntheticEvent:** Canaliza las interacciones del usuario hacia la lógica de negocio asegurando portabilidad cross-browser.

---

### 6. Características Principales de React

1. **Arquitectura Basada en Componentes (*Component-Based*):** Permite encapsular estructura, estilos y comportamiento en piezas autocontenidas y reutilizables a lo largo de toda la aplicación.
2. **Enfoque Declarativo (*Declarative UI*):** El desarrollador describe *qué* debe mostrarse en la pantalla en función del estado actual, y React se encarga de determinar *cómo* alterar el DOM del navegador.
3. **Virtual DOM de Alto Rendimiento:** Reduce al mínimo indispensable los costosos accesos de lectura/escritura en el DOM real mediante su algoritmo de reconciliación.
4. **Flujo Unidireccional de Datos:** Facilita la depuración, el rastreo de errores y la predictibilidad del estado al garantizar que los datos fluyan exclusivamente en un solo sentido.
5. **Ecosistema Amplio y Estandarizado:** Cuenta con el mayor soporte de herramientas comunitarias (Vite, Next.js, Redux, React Router, TailwindCSS) y versatilidad para reutilizar conocimientos en aplicaciones nativas con **React Native**.

---

### 7. Matriz de Cumplimiento de la Rúbrica SENA (IE-GA7-220501096-AA4-EV01)

| Criterio Evaluado en la Guía 7 | Estado | Evidencia Aportada |
|---|:---:|---|
| 1. El documento sigue las normas de presentación (portada, introducción, objetivo). | **CUMPLE** | Informe técnico estructurado con diseño formal SENA de 8 páginas en PDF. |
| 2. Presenta la diferencia conceptual y técnica entre React y JSX. | **CUMPLE** | Análisis profundo, rol de Babel y comparación de código lado a lado. |
| 3. Explica qué son las clases en React, su ciclo de vida y contraste con Hooks. | **CUMPLE** | Explicación de `React.Component`, 3 fases del ciclo de vida y migración a Hooks. |
| 4. Detalla los principales eventos de React y el sistema `SyntheticEvent`. | **CUMPLE** | Tabla clasificatoria, sintaxis camelCase y ejemplos prácticos en la Pizzería. |
| 5. Incluye un mapa conceptual completo y representativo de React. | **CUMPLE** | Diagrama arquitectónico del Virtual DOM, Fiber, Props, State y Eventos. |
| 6. Describe las principales características del framework/biblioteca. | **CUMPLE** | Síntesis de los 5 pilares arquitectónicos del ecosistema React. |

---

### 8. Conclusiones
1. React y JSX forman una simbiosis técnica donde React provee el motor de reconciliación y estado, mientras que JSX actúa como azúcar sintáctico declarativo que Babel traduce a JavaScript estándar.
2. La evolución desde componentes de clase hacia componentes funcionales con Hooks ha simplificado la estructura del código, eliminando la complejidad del contexto `this` y facilitando la reutilización de lógica mediante Custom Hooks.
3. El sistema `SyntheticEvent` y el Virtual DOM garantizan una experiencia de usuario ágil y altamente optimizada, permitiendo que interfaces complejas como la Pizzería Bella Italia respondan fluidamente a cada interacción.
4. El presente documento técnico en formato PDF oficial queda listo en la carpeta de entrega para su calificación en la plataforma Zajuna.
