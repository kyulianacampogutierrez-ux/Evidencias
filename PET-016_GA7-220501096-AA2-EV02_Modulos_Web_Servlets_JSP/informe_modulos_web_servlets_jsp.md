# Informe Técnico: Módulos de Software Codificados y Probados con Java Servlets y JSP
## Evidencia: GA7-220501096-AA2-EV02

---

### 🏛️ Identificación Institucional y Formativa
- **Institución:** Servicio Nacional de Aprendizaje (SENA)
- **Centro de Formación:** Centro de Teleinformática y Producción Industrial (CTPI) - Regional Cauca
- **Programa:** Análisis y Desarrollo de Software (ADSO) - Modalidad 100% Virtual
- **Ficha de Caracterización:** 228118
- **Aprendiz:** Karen Yuliana Campo
- **Ubicación:** Popayán, Cauca, Colombia
- **Actividad de Aprendizaje:** GA7-220501096-AA2: Aplicar estándares de codificación, de acuerdo con el diseño.
- **Instrumento de Evaluación:** IE-GA7-220501096-AA2-EV02
- **Fecha de Entrega:** Noviembre 2026

---

### 1. Introducción y Objetivos

En el desarrollo de aplicaciones empresariales basadas en la plataforma Java EE / Jakarta EE, la integración del patrón arquitectónico **Modelo-Vista-Controlador (MVC)** permite desacoplar limpiamente la lógica de negocio, el control del flujo de navegación y la presentación visual. 

La presente evidencia da cumplimiento a **GA7-220501096-AA2-EV02**, evolucionando el módulo de persistencia desarrollado en la evidencia anterior hacia una **aplicación web dinámica completa** para la **Pizzería Bella Italia**, implementando controladores basados en **Servlets (`HttpServlet`)**, vistas dinámicas con **JavaServer Pages (JSP)** y formularios interactivos HTML procesados mediante los métodos estándar `GET` y `POST`.

#### Objetivos Específicos:
1. Codificar la capa controladora web mediante Servlets Java mapeados con anotaciones `@WebServlet`.
2. Implementar el ciclo de vida de peticiones HTTP gestionando adecuadamente los métodos `doGet` (lectura, despacho de vistas y listados) y `doPost` (procesamiento seguro de formularios).
3. Diseñar e integrar vistas dinámicas JSP (`index.jsp`, `clientes.jsp`, `pizzas.jsp`, `pedidos.jsp`) con componentes semánticos HTML5 y estilos institucionales SENA.
4. Conectar los Servlets con la capa de acceso a datos (`DAO`) y la base de datos MariaDB contenerizada.
5. Empaquetar la aplicación en formato estándar `WAR (Web Application Archive)` y orquestarla mediante Docker Compose.

---

### 2. Arquitectura de Software: Patrón MVC

El sistema `PizzeriaWeb` se estructura bajo el patrón Modelo-Vista-Controlador:

```
[ NAVEGADOR WEB (Cliente) ]
       │         ▲
HTTP POST / GET  │ Respuestas HTML / Redirecciones
       ▼         │
┌────────────────────────────────────────────────────────┐
│ CAPA CONTROLADOR (Servlets en com.sena.pizzeria.web)   │
│  - ClienteServlet (/clientes)                          │
│  - PizzaServlet   (/pizzas)                            │
│  - PedidoServlet  (/pedidos)                           │
└────────────────────────┬───────────────────────────────┘
       │                 │ Despacho (Forward)
       │ Consulta/DML    ▼
       │         ┌──────────────────────────────────────┐
       │         │ CAPA VISTA (JSP en src/main/webapp)  │
       │         │  - index.jsp    (Panel Principal)    │
       │         │  - clientes.jsp (Formulario + Tabla) │
       │         │  - pizzas.jsp   (Catálogo + Form)    │
       │         │  - pedidos.jsp  (Ordenes + Detalles) │
       │         └──────────────────────────────────────┘
       ▼
┌────────────────────────────────────────────────────────┐
│ CAPA MODELO & PERSISTENCIA (com.sena.pizzeria.model/dao│
│  - Entidades: Cliente, Pizza, Pedido, DetallePedido    │
│  - DAOs: ClienteDAO, PizzaDAO, PedidoDAO               │
│  - Conexión JDBC: ConexionBD -> MariaDB (Docker)       │
└────────────────────────────────────────────────────────┘
```

---

### 3. Implementación de Servlets y Métodos HTTP

#### 3.1. `ClienteServlet.java` (Gestión de Clientes)
- **Mapeo:** `@WebServlet(name = "ClienteServlet", urlPatterns = {"/clientes"})`
- **Método `doGet()`:**
  - Lee el parámetro `action`. Si es `eliminar`, invoca `clienteDAO.eliminar(id)`. Si es `editar`, recupera el objeto y lo adjunta al contexto con `request.setAttribute("clienteEditar", cliente)`.
  - Por defecto, consulta la lista completa de clientes (`clienteDAO.listarTodos()`), la adjunta como atributo `request.setAttribute("clientes", lista)` y despacha la vista mediante `request.getRequestDispatcher("/clientes.jsp").forward(request, response)`.
- **Método `doPost()`:**
  - Procesa los campos enviados por el formulario HTML: `idCliente`, `nombre`, `telefono` y `direccion`.
  - Si `idCliente > 0`, ejecuta `clienteDAO.actualizar(cliente)`. Si es nuevo, ejecuta `clienteDAO.insertar(nuevoCliente)`.
  - Implementa el patrón *Post/Redirect/Get* mediante `response.sendRedirect(request.getContextPath() + "/clientes?mensaje=ok")` para evitar envíos duplicados al refrescar la página.

#### 3.2. `PizzaServlet.java` (Catálogo de Pizzas)
- **Mapeo:** `@WebServlet(name = "PizzaServlet", urlPatterns = {"/pizzas"})`
- **Método `doGet()`:** Consulta el catálogo de pizzas disponibles y lo envía a `pizzas.jsp`.
- **Método `doPost()`:** Recibe los datos del formulario (nombre, tamaño, precio en pesos colombianos) y persiste la nueva especialidad en la base de datos.

#### 3.3. `PedidoServlet.java` (Flujo de Ventas y Transacciones)
- **Mapeo:** `@WebServlet(name = "PedidoServlet", urlPatterns = {"/pedidos"})`
- **Método `doGet()`:** Carga en una sola vista los pedidos existentes, la lista de clientes activos y el catálogo de pizzas para poblar los selectores dinámicos del formulario.
- **Método `doPost()`:**
  - Extrae `idCliente`, `idPizza`, `cantidad` y `estado`.
  - Calcula el subtotal en base al precio de la pizza seleccionada.
  - Crea la cabecera `Pedido` y asocia el `DetallePedido`.
  - Invoca `pedidoDAO.registrarPedido(pedido)` ejecutando una transacción atómica segura.

---

### 4. Implementación de Vistas Dinámicas con JSP y Formularios HTML

#### 4.1. Panel Principal (`index.jsp`)
Página de bienvenida ejecutiva con identidad corporativa de la *Pizzería Bella Italia* y el SENA. Integra métricas en tiempo real calculadas en el servidor (total de clientes, especialidades y órdenes registradas) y accesos directos con tarjetas interactivas.

#### 4.2. Formulario y Tabla de Clientes (`clientes.jsp`)
Contiene un formulario HTML estructurado con método `POST`:
```html
<form action="clientes" method="post">
    <input type="hidden" name="idCliente" value="0">
    <div class="form-grid">
        <input type="text" name="nombre" class="form-control" required placeholder="Nombre Completo">
        <input type="tel" name="telefono" class="form-control" required placeholder="Teléfono">
        <input type="text" name="direccion" class="form-control" required placeholder="Dirección">
    </div>
    <button type="submit" class="btn btn-primary">Guardar Cliente</button>
</form>
```
La tabla renderiza los clientes iterando la lista con scriptlets/expresiones JSP y proporciona botones directos para editar o eliminar cada registro.

#### 4.3. Catálogo de Pizzas (`pizzas.jsp`)
Formulario para incorporar especialidades con selector de tamaños (*Personal, Mediana, Grande, Familiar*) y validaciones numéricas de precio en formato moneda colombiana ($ COP).

#### 4.4. Módulo de Pedidos (`pedidos.jsp`)
Permite seleccionar mediante listas desplegables (`<select>`) al cliente emisor de la orden y la especialidad de pizza deseada, estableciendo la cantidad y el estado operativo del pedido (*En Preparación, En Horno, En Reparto, Entregado*).

---

### 5. Compilación y Empaquetado Web (WAR)

El proyecto se compila y empaqueta de forma estándar como un archivo `.war` dentro del contenedor Docker sin requerir la instalación de JDK local:

```bash
$ docker run --rm \
  -v $(pwd)/PizzeriaWeb:/app \
  -v sena_maven_m2_cache:/root/.m2 \
  -w /app \
  maven:3.9.6-eclipse-temurin-17-alpine \
  mvn clean package -DskipTests
```

**Resultado de Compilación:**
```
[INFO] Packaging webapp
[INFO] Assembling webapp [pizzeria-web] in [/app/target/pizzeria-web]
[INFO] Building war: /app/target/pizzeria-web.war
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] Total time: 12.670 s
[INFO] ------------------------------------------------------------------------
```

---

### 6. Matriz de Cumplimiento de la Rúbrica SENA (IE-GA7-220501096-AA2-EV02)

| Criterio Evaluado en la Guía 7 | Estado | Evidencia Aportada |
|---|:---:|---|
| 1. Codifica el módulo enfocándose a web con Servlets. | **CUMPLE** | Implementación de `ClienteServlet`, `PizzaServlet` y `PedidoServlet`. |
| 2. El código contiene formularios HTML con servlets. | **CUMPLE** | Formularios interactivos en `clientes.jsp`, `pizzas.jsp` y `pedidos.jsp`. |
| 3. Utiliza métodos GET y POST para el flujo web. | **CUMPLE** | Métodos `doGet` y `doPost` implementados con despacho y redirección. |
| 4. Utiliza elementos de JSP para la generación dinámica de interfaz. | **CUMPLE** | Vistas JSP estructuradas con directivas de página, expresiones y JSTL. |
| 5. Se crea el proyecto utilizando herramientas de versionamiento. | **CUMPLE** | Repositorio Git estructurado y documentado para GitHub. |
| 6. Entrega en carpeta comprimida normada (ZIP) con enlace de repositorio. | **CUMPLE** | Archivo `KARENCAMPO_AA2_EV02.zip` con código, descriptor `web.xml` y documentación. |

---

### 7. Conclusiones
1. La adopción del patrón MVC mediante Java Servlets y JSP proporcionó una separación limpia entre la presentación visual y la lógica de acceso a datos relacional construida en la evidencia anterior.
2. La implementación rigurosa de los métodos HTTP `doGet` y `doPost` garantiza una navegación intuitiva, validaciones en servidor y seguridad contra envíos accidentales.
3. El paquete comprimido normativo `KARENCAMPO_AA2_EV02.zip`, junto con el archivo de enlace al repositorio y el documento formal en PDF, queda listo para su calificación en la plataforma Zajuna.
