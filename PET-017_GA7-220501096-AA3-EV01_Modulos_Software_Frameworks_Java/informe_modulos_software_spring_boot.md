# Informe Técnico: Codificación de Módulos del Software con Frameworks de Java
## Evidencia: GA7-220501096-AA3-EV01

---

### 🏛️ Identificación Institucional y Formativa
- **Institución:** Servicio Nacional de Aprendizaje (SENA)
- **Centro de Formación:** Centro de Teleinformática y Producción Industrial (CTPI) - Regional Cauca
- **Programa:** Análisis y Desarrollo de Software (ADSO) - Modalidad 100% Virtual
- **Ficha de Caracterización:** 228118
- **Aprendiz:** Karen Yuliana Campo
- **Ubicación:** Popayán, Cauca, Colombia
- **Actividad de Aprendizaje:** GA7-220501096-AA3: Codificar los módulos del software stand-alone, web y móvil, de acuerdo con el diseño.
- **Instrumento de Evaluación:** IE-GA7-220501096-AA3-EV01
- **Fecha de Entrega:** Noviembre 2026

---

### 1. Introducción y Objetivos

En el ecosistema tecnológico moderno, los frameworks de desarrollo ágil son pilares indispensables para la construcción de sistemas empresariales escalables, seguros y mantenibles. Dentro de la plataforma Java, **Spring Boot** se posiciona como el estándar de facto en la industria para la creación de APIs REST y microservicios, eliminando la configuración manual compleja (*convention over configuration*) e integrando servidores web embebidos, gestores de dependencias y potentes herramientas de mapeo objeto-relacional (ORM) mediante **Spring Data JPA** y **Hibernate**.

La presente evidencia da cumplimiento a **GA7-220501096-AA3-EV01**, desarrollando la capa backend moderna para el sistema de información de la **Pizzería Bella Italia**, implementando una arquitectura de microservicio basada en Spring Boot, validaciones automáticas de datos, operaciones CRUD transaccionales y orquestación contenerizada con Docker.

#### Objetivos Específicos:
1. Codificar la capa de persistencia relacional con **Spring Data JPA** y **Hibernate**, modelando entidades relacionales (`Cliente`, `Pizza`, `Pedido`, `DetallePedido`) con llaves primarias, foráneas y restricciones de integridad.
2. Desarrollar la capa de lógica de negocio (`Service`) implementando reglas de validación, cálculos automáticos de subtotales y gestión de transacciones atómicas con la anotación `@Transactional`.
3. Exponer endpoints HTTP estructurados mediante **Controladores REST (`@RestController`)** respetando las convenciones semánticas del protocolo HTTP (`GET`, `POST`, `PUT`, `DELETE`, `PATCH`).
4. Aplicar validación declarativa de datos mediante **Jakarta Bean Validation** (`@NotBlank`, `@Min`, `@Pattern`, `@Size`) y captura centralizada de errores con `@RestControllerAdvice`.
5. Ejecutar la solución bajo un entorno 100% portable y contenerizado mediante Docker Compose conectado a una base de datos MariaDB.

---

### 2. Arquitectura de Software: Capas del Microservicio Spring Boot

El diseño del backend `PizzeriaSpringBoot` implementa una arquitectura desacoplada en cuatro capas principales:

```
┌────────────────────────────────────────────────────────┐
│             CLIENTES HTTP (Web, Móvil, Postman)        │
└───────────────────────────┬────────────────────────────┘
             Peticiones JSON│ ▲ Respuestas HTTP / Códigos de Estado
                            ▼ │
┌────────────────────────────────────────────────────────┐
│ 1. CAPA CONTROLADOR REST (@RestController)             │
│    - ClienteRestController (/api/clientes)             │
│    - PizzaRestController   (/api/pizzas)               │
│    - PedidoRestController  (/api/pedidos)              │
│    - GlobalExceptionHandler (@RestControllerAdvice)    │
└───────────────────────────┬────────────────────────────┘
                            │ DTOs / Entidades
                            ▼
┌────────────────────────────────────────────────────────┐
│ 2. CAPA DE SERVICIO (@Service & @Transactional)        │
│    - ClienteService (Reglas de negocio y directorio)   │
│    - PizzaService   (Catálogo gastronómico y precios)  │
│    - PedidoService  (Cálculo de ítems y transacciones) │
└───────────────────────────┬────────────────────────────┘
                            │ Invocación de Operaciones
                            ▼
┌────────────────────────────────────────────────────────┐
│ 3. CAPA DE PERSISTENCIA (Spring Data JPA)              │
│    - ClienteRepository extends JpaRepository           │
│    - PizzaRepository extends JpaRepository             │
│    - PedidoRepository extends JpaRepository            │
│    - DetallePedidoRepository extends JpaRepository     │
└───────────────────────────┬────────────────────────────┘
                            │ Mapeo ORM (Hibernate)
                            ▼
┌────────────────────────────────────────────────────────┐
│ 4. CAPA DE DOMINIO / BASE DE DATOS (MariaDB en Docker) │
│    - Entidades: Cliente, Pizza, Pedido, DetallePedido  │
│    - Tablas: CLIENTES, PIZZAS, PEDIDOS, DETALLE_PEDIDO │
└────────────────────────────────────────────────────────┘
```

---

### 3. Componentes y Módulos Desarrollados

#### 3.1. Entidades del Dominio JPA
- **`Cliente.java`**: Mapeada a la tabla `CLIENTES`. Incorpora validaciones declarativas: nombre obligatorio (`@NotBlank`), teléfono validado con expresión regular (`^[0-9]{7,15}$`) y dirección estructurada.
- **`Pizza.java`**: Mapeada a la tabla `PIZZAS`. Define nombre, tamaño estandarizado (*Personal, Mediana, Grande, Familiar*) y precio validado con monto mínimo de $5.000 COP (`@DecimalMin`).
- **`Pedido.java`**: Cabecera de órdenes de compra con relación `@ManyToOne` hacia `Cliente` y `@OneToMany` hacia `DetallePedido` con propagación en cascada (`CascadeType.ALL`) y ciclo de vida `@PrePersist` para marca temporal automática.
- **`DetallePedido.java`**: Detalle del pedido con relación referencial hacia `Pizza`, cantidad unitaria y cálculo de subtotales.

#### 3.2. Repositorios Spring Data JPA
Los repositorios extienden la interfaz `JpaRepository<T, ID>`, obteniendo métodos nativos como `save()`, `findById()`, `findAll()`, `deleteById()` y `existsById()` sin necesidad de escribir código SQL manual, aprovechando además consultas derivadas (*derived query methods*):
- `findByTelefono(String telefono)`
- `findByNombreContainingIgnoreCase(String nombre)`
- `findByTamano(String tamano)`
- `findByPrecioLessThanEqual(BigDecimal precioMax)`
- `findByEstado(String estado)`

#### 3.3. Capa de Servicios y Transaccionalidad
- **`ClienteService.java`**: Administra el ciclo de vida de clientes, garantizando lectura limpia (`@Transactional(readOnly = true)`) y confirmación atómica en mutaciones.
- **`PizzaService.java`**: Gestiona las especialidades y tarifas gastronómicas.
- **`PedidoService.java`**: Núcleo transaccional. Al recibir un `PedidoRequestDTO`, verifica en tiempo real la existencia del cliente y de cada especialidad solicitada, calcula matemáticamente los subtotales de cada ítem, consolida el gran total de la factura y persiste la orden completa de forma atómica.

#### 3.4. Controladores REST y Manejo Global de Excepciones
- **`ClienteRestController`**: Expone endpoints para listar clientes, buscar por nombre, consultar por identificador, registrar nuevos usuarios con código HTTP `201 Created` y eliminar con `204 No Content`.
- **`PizzaRestController`**: Endpoints para exploración de menú y filtros de precio.
- **`PedidoRestController`**: Endpoint de creación de comandas y actualización de estados mediante método HTTP `PATCH`.
- **`GlobalExceptionHandler`**: Captura errores de validación (`MethodArgumentNotValidException`) e inconsistencias de negocio (`IllegalArgumentException`), devolviendo respuestas JSON legibles con sellos de tiempo y códigos de error estándar (HTTP 400 Bad Request).

---

### 4. Pruebas Unitarias con JUnit 5 y Mockito

Se implementó una suite completa de pruebas unitarias (`PizzeriaSpringBootTests.java`) que verifica el comportamiento aislado de cada servicio de negocio simulando la capa de datos:
1. **UT01:** Guardado y listado de clientes mediante `ClienteService`.
2. **UT02:** Consulta por ID y filtros de catálogo de especialidades con `PizzaService`.
3. **UT03:** Cálculo matemático atómico de subtotales y gran total de comanda con `PedidoService`.
4. **UT04:** Verificación de borrado y control de integridad referencial.

---

### 5. Matriz de Cumplimiento de la Rúbrica SENA (IE-GA7-220501096-AA3-EV01)

| Criterio Evaluado en la Guía 7 | Estado | Evidencia Aportada |
|---|:---:|---|
| 1. Codifica el módulo del proyecto aplicando frameworks vistos en el componente formativo. | **CUMPLE** | Framework Spring Boot 3.2.5 con Spring Data JPA y Hibernate. |
| 2. Para la codificación tiene en cuenta artefactos de diseño previos (clases, casos de uso). | **CUMPLE** | Modelo relacional y POO de la Pizzería Bella Italia con entidades estructuradas. |
| 3. El código contiene comentarios técnicos y documentación descriptiva. | **CUMPLE** | Clases comentadas con Javadoc formal y especificaciones de parámetros. |
| 4. El código cumple con estándares de codificación (nomenclatura, buenas prácticas). | **CUMPLE** | CamelCase, PascalCase, inyección de dependencias por constructor e inmutabilidad. |
| 5. Se crea el proyecto utilizando herramientas de versionamiento. | **CUMPLE** | Repositorio Git estructurado y documentado en `enlace_repositorio.txt`. |
| 6. Entrega en archivo comprimido normado `NOMBRE_APELLIDO_AA3_EV01.zip`. | **CUMPLE** | Archivo `KARENCAMPO_AA3_EV01.zip` en la carpeta oficial de entrega Zajuna. |

---

### 6. Conclusiones
1. La adopción de **Spring Boot** acelera significativamente los tiempos de desarrollo al proveer configuraciones automáticas y un contenedor de inyección de dependencias maduro y altamente desacoplado.
2. El uso de **Spring Data JPA** simplifica la interacción con la base de datos MariaDB, abstrayendo la complejidad de las sentencias SQL manuales mediante repositorios tipificados y transacciones declarativas seguras.
3. El proyecto se entrega completamente empaquetado, verificado por pruebas automatizadas y respaldado por la carpeta oficial en el Escritorio para su calificación directa en la plataforma Zajuna.
