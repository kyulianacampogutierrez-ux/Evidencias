# Guion Técnico de Sustentación en Video (MP4)
## Evidencia: GA7-220501096-AA3-EV02 - Módulos de Software Codificados y Probados
**Aprendiz:** Karen Yuliana Campo  
**Ficha:** 228118  
**Programa:** Análisis y Desarrollo de Software (ADSO) - Modalidad Virtual  
**Centro:** Centro de Teleinformática y Producción Industrial (CTPI) - Regional Cauca (Popayán)  
**Duración Estimada:** 4 a 6 minutos  

---

### ⏱️ Estructura del Video de Demostración

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 00:00 - 00:45 │ BLOQUE 1: Saludo Institucional, Portada y Presentación     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 00:45 - 01:45 │ BLOQUE 2: Arquitectura Spring Boot, JPA y Docker Compose   │
├─────────────────────────────────────────────────────────────────────────────┤
│ 01:45 - 03:00 │ BLOQUE 3: Demostración de Historias de Usuario (HU-01 a 04)│
├─────────────────────────────────────────────────────────────────────────────┤
│ 03:00 - 04:30 │ BLOQUE 4: Validaciones de Datos (Bean Validation & HTTP 400)│
├─────────────────────────────────────────────────────────────────────────────┤
│ 04:30 - 05:15 │ BLOQUE 5: Suite JUnit 5 (10/10) y Conclusiones Finales      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 🎙️ Guion Locutado Paso a Paso

#### Bloque 1: Saludo Institucional y Presentación (00:00 - 00:45)
> *"Un cordial saludo para los instructores y evaluadores del Servicio Nacional de Aprendizaje (SENA). Mi nombre es **Karen Yuliana Campo**, aprendiz de la ficha **228118** del programa **Análisis y Desarrollo de Software (ADSO)**, perteneciente al **Centro de Teleinformática y Producción Industrial (CTPI) de la Regional Cauca**, Popayán.*
>
> *En este video presento la evidencia **GA7-220501096-AA3-EV02**, correspondiente a los módulos de software codificados y probados para el sistema de información de la **Pizzería Bella Italia**, demostrando la ejecución de las pruebas basadas en Historias de Usuario, Casos de Uso y validaciones de datos en servidor."*

---

#### Bloque 2: Arquitectura del Microservicio Spring Boot (00:45 - 01:45)
> *(Mostrar en pantalla el diagrama de arquitectura y el código en el IDE / terminal)*  
> *"La solución fue construida utilizando **Spring Boot 3.2.5** y **Spring Data JPA** con motor Hibernate ORM, orquestada en un contenedor Docker conectado a una base de datos relacional MariaDB.
>
> La arquitectura se organiza en 4 capas limpias:
> 1. **Capa Entidades:** `Cliente`, `Pizza`, `Pedido` y `DetallePedido` con llaves primarias autonuméricas y relaciones referenciales.
> 2. **Capa Repositorios:** Interfaces que extienden `JpaRepository` para consultas DML automáticas.
> 3. **Capa Servicios:** Servicios de negocio anotados con `@Transactional` para garantizar transacciones ACID atómicas.
> 4. **Capa Controladores REST:** Controladores que exponen endpoints HTTP en el contexto `/api` con validaciones automáticas y respuestas JSON."*

---

#### Bloque 3: Demostración de Requisitos e Historias de Usuario (01:45 - 03:00)
> *(Mostrar en pantalla las peticiones HTTP y respuestas)*  
> *"A continuación demostramos el cumplimiento de los requisitos del sistema:
> - **HU-01 (Gestión de Clientes):** Mediante una petición `GET` a `/api/clientes`, recuperamos la lista de clientes registrados desde la base de datos.
> - **HU-02 (Catálogo de Pizzas):** Accedemos a `/api/pizzas` y aplicamos filtros dinámicos por tamaño y precio máximo con `/api/pizzas/precio-maximo?precio=35000`.
> - **HU-03 (Pedido Transaccional):** Al enviar una petición `POST` a `/api/pedidos` con el cliente y los ítems solicitados, el servicio `PedidoService` consulta las tarifas de cada pizza, calcula automáticamente los subtotales unitarios y consolida el gran total de la factura, persistiendo cabecera y detalle de forma atómica.
> - **HU-04 (Transición de Estados):** Con el método `PATCH` en `/api/pedidos/{id}/estado`, actualizamos el estado del pedido de 'En Preparación' a 'En Horno', manteniendo trazabilidad de la orden."*

---

#### Bloque 4: Pruebas de Validación de Datos (03:00 - 04:30)
> *(Mostrar en pantalla los intentos fallidos y la respuesta HTTP 400 Bad Request)*  
> *"Uno de los puntos clave exigidos por la Guía 7 son las pruebas de validación de datos en servidor:
> 1. **Longitudes y campos obligatorios:** Si intentamos crear un cliente con nombre vacío o menor a 3 caracteres, Jakarta Bean Validation activa la regla `@NotBlank` y `@Size`.
> 2. **Expresiones regulares en teléfonos:** Si enviamos un teléfono con letras o caracteres especiales, la restricción `@Pattern` rechaza la solicitud.
> 3. **Validación de precios numéricos:** Para las especialidades de pizza, `@DecimalMin` exige un valor mínimo de $5.000 COP, impidiendo tarifas negativas o irrisorias.
> 4. **Manejo Centralizado de Excepciones:** Todas las violaciones son capturadas por nuestra clase `GlobalExceptionHandler` (`@RestControllerAdvice`), devolviendo un JSON limpio con código HTTP 400 y el detalle exacto de cada campo erróneo."*

---

#### Bloque 5: Suite JUnit 5 y Conclusiones (04:30 - 05:15)
> *(Mostrar la terminal ejecutando `mvn test` con 10/10 pruebas en verde)*  
> *"Finalmente, ejecutamos la suite automatizada de pruebas unitarias con JUnit 5 y Mockito dentro del contenedor Docker. Como observamos en consola:
> **10 de 10 pruebas aprobadas exitosamente**, verificando la capa de persistencia, la lógica de cálculo y los validadores.
>
> Con esto damos cabal cumplimiento a todos los criterios de la evidencia **GA7-220501096-AA3-EV02**. Muchas gracias por su atención."*
