# INFORME TÉCNICO DE DOCUMENTACIÓN DE PRUEBAS DE SOFTWARE
## Evidencia: GA9-220501096-AA3-EV01

---

### DATOS INSTITUCIONALES Y DEL PROYECTO

* **Institución:** Servicio Nacional de Aprendizaje (SENA)
* **Regional:** Regional Cauca
* **Centro de Formación:** Centro de Teleinformática y Producción Industrial (CTPI)
* **Programa:** Tecnología en Análisis y Desarrollo de Software (ADSO)
* **Ficha de Caracterización:** 3186681
* **Aprendiz:** Karen Yuliana Campo
* **Proyecto Formativo:** Sistema Integral de Gestión de Pedidos, Facturación, Inventarios y Domicilios - *Pizzería Gourmet Bella Italia Popayán*
* **Competencia:** 220501096 - Desarrollar la solución de software de acuerdo con el diseño y metodologías de desarrollo.
* **Actividad de Aprendizaje:** GA9-220501096-AA3 - Documentar pruebas de software de acuerdo con la planificación.
* **Evidencia de Desempeño y Producto:** GA9-220501096-AA3-EV01: Documenta pruebas de software, de acuerdo a la planificación.
* **Ciudad y Fecha:** Popayán, Cauca - Noviembre de 2026

---

## 1. INTRODUCCIÓN

El aseguramiento de la calidad en la ingeniería de software moderna no es una fase accesoria o tardía en el ciclo de vida del desarrollo, sino un proceso riguroso, sistemático y continuo. En concordancia con los lineamientos del componente formativo institucional del SENA titulado **"Las pruebas de software"**, las pruebas constituyen una actividad de verificación y validación orientada a descubrir inconsistencias, evaluar el comportamiento del sistema bajo condiciones controladas y certificar que cada requisito de negocio se satisfaga con precisión matemática, robustez técnica y apego a las normas internacionales.

El presente informe consolida la ejecución y documentación técnica exhaustiva del plan de pruebas concebido para el sistema web de comercio electrónico y gestión operativa de la **Pizzería Gourmet Bella Italia Popayán**. A través de la adopción del estándar internacional **IEEE 829 (Standard for Software and System Test Documentation)** y el modelo de calidad de software **ISO/IEC 25000 (SQuaRE)**, se formalizan los formatos diligenciados de especificación de doce (12) casos de prueba, la bitácora de ejecución controlada en contenedores Docker y el reporte de incidentes y defectos corregidos bajo la metodología **TDD (Test-Driven Development)**.

Asimismo, este informe articula de manera transversal los **7 principios fundamentales de las pruebas de software** formulados por Mera (2016) y la perspectiva de control de calidad de Sanz (2005), demostrando cómo la formulación temprana de pruebas unitarias y de integración garantiza la fiabilidad, la seguridad y la resiliencia del software entregado a la comunidad del SENA y a los clientes de Popayán.

---

## 2. OBJETIVOS

### 2.1 Objetivo General
Documentar y validar la ejecución técnica de las pruebas de software planificadas para el sistema de la Pizzería Gourmet Bella Italia Popayán, mediante formatos normalizados IEEE 829, la suite automatizada de pruebas en Node.js y la aplicación de los principios de aseguramiento de calidad del marco formativo SENA.

### 2.2 Objetivos Específicos
1. Formalizar las especificaciones de doce (12) casos de prueba funcionales, de seguridad, de integración y de reglas de negocio para los módulos críticos de facturación, autenticación, clientes, inventario y persistencia en base de datos.
2. Aplicar la disciplina metodológica **TDD (Test-Driven Development)** mediante el ciclo iterativo *Rojo (Red) - Verde (Green) - Refactorización (Refactor)* para garantizar un código limpio, desacoplado y con alta cobertura.
3. Registrar la bitácora de ejecución de pruebas en un entorno contenerizado reproducible (Docker) y documentar los defectos detectados y resueltos mediante el formato IEEE 829 Defect Report.
4. Elaborar una guía detallada y guion técnico paso a paso para la grabación del video demostrativo requerido por la evidencia, sustentando conceptualmente las pruebas frente a la comunidad académica.

---

## 3. MARCO CONCEPTUAL Y FUNDAMENTOS FORMATIVOS SENA

El marco metodológico adoptado se fundamenta rigurosamente en el componente formativo **"Las pruebas de software"** provisto en la base de conocimiento institucional del SENA.

### 3.1 Definición y Propósito de las Pruebas de Software
Tal como expone **Sanz (2005)**, las pruebas de software representan el proceso técnico de someter un programa informático a conjuntos ordenados de estímulos (entradas y condiciones previas) con el fin primordial de identificar discrepancias entre los resultados obtenidos y los resultados esperados, verificar su usabilidad operativa y certificar la correcta configuración del sistema antes de su puesta en producción.

Por su parte, **Mera (2016)** conceptualiza las pruebas no como un simple filtro sancionatorio al final de la codificación, sino como un elemento de control de calidad intrínseco al ciclo de vida del software, dividido en fases ordenadas de:
* Planificación y control de pruebas.
* Análisis y diseño de casos de prueba.
* Implementación y ejecución en entornos controlados.
* Comprobación y evaluación de criterios de salida.
* Elaboración de informes de síntesis y bitácoras de experiencias.

```
       +-------------------------------------------------------------+
       |                  CICLO METODOLÓGICO TDD                     |
       +-------------------------------------------------------------+
                                      |
                                      v
       +-------------------+                     +-------------------+
       |   1. FASE ROJA    |                     |   2. FASE VERDE   |
       |  (Red Phase)      |                     |  (Green Phase)    |
       | Escribir prueba   | ------------------> | Escribir código   |
       | unitaria que falle|                     | mínimo para pasar |
       +-------------------+                     +-------------------+
                 ^                                         |
                 |                                         v
                 |       +-----------------------+         |
                 |       |  3. REFACTORIZACIÓN   |         |
                 +-------|    (Refactor Phase)   |<--------+
                         | Optimizar arquitectura|
                         | sin alterar conducta  |
                         +-----------------------+
```

### 3.2 Los 7 Principios de las Pruebas de Software (Mera, 2016)

El desarrollo del plan de pruebas del sistema de Pizzería Bella Italia Popayán se rigió de manera estricta por los siete principios universales expuestos por **Mera (2016)**:

1. **Las pruebas muestran la presencia de defectos, no su ausencia:** La ejecución exitosa de las pruebas demuestra que los defectos contemplados fueron identificados y solventados; sin embargo, no constituye una prueba matemática absoluta de que el sistema esté 100% libre de errores bajo cualquier eventualidad humana inimaginable.
2. **Las pruebas tempranas (Early Testing):** Las actividades de verificación deben iniciarse en las etapas tempranas de diseño y codificación. Detectar un error de cálculo de impuestos en el diseño de la API cuesta hasta 100 veces menos que corregirlo cuando el sistema ya factura en producción.
3. **Las pruebas no pueden ser exhaustivas:** Evaluar todas las combinaciones posibles de datos de entrada, tiempos de red y combinaciones de ingredientes es computacional y económicamente inviable. Por ello, se emplean técnicas analíticas como la *Partición de Equivalencia* y el *Análisis de Valores Límite*.
4. **Las pruebas dependen del contexto:** La rigurosidad de las pruebas varía según la criticidad del módulo. La verificación de transacciones financieras (facturación con Impoconsumo) y la autenticación RBAC exigen validaciones criptográficas y transaccionales mucho más estrictas que la visualización del menú en pantalla.
5. **Agrupación de defectos (Principio de Pareto 80/20):** La mayoría de las incidencias operativas suelen concentrarse en un pequeño número de módulos complejos (típicamente facturación de pedidos e inventario de recetas).
6. **La paradoja del pesticida:** Si los mismos casos de prueba se repiten una y otra vez sin evolucionar, con el tiempo dejan de encontrar nuevos errores. Es imperativo actualizar y enriquecer la batería de pruebas a medida que el software evoluciona.
7. **La falacia de la ausencia de errores:** Un sistema de software puede carecer de fallos sintácticos y pasar todas las pruebas técnicas en consola; sin embargo, si no satisface las verdaderas necesidades operativas y expectativas del negocio de la pizzería y sus usuarios, el producto seguirá siendo un fracaso comercial y funcional.

### 3.3 Marco Normativo de Calidad ISO/IEC 25000 (SQuaRE)
Las pruebas fueron categorizadas atendiendo a las características de calidad establecidas por la familia de normas **ISO/IEC 25010**:
* **Adecuación Funcional:** Exactitud en el cálculo del Impuesto al Consumo (8%) y completitud de pedidos.
* **Fiabilidad y Tolerancia a Fallos:** Manejo controlado de excepciones ante carrito vacío o desabastecimiento de inventario.
* **Seguridad:** Protección contra inyecciones XSS, cifrado de contraseñas y control de acceso RBAC.
* **Mantenibilidad:** Arquitectura desacoplada y pruebas automatizadas reutilizables.

---

## 4. ESPECIFICACIÓN DE CASOS DE PRUEBA DILIGENCIADOS (ESTÁNDAR IEEE 829)

A continuación se presentan los doce (12) casos de prueba diseñados, formalizados y ejecutados para el sistema de la Pizzería Gourmet Bella Italia Popayán, clasificados en cinco (5) módulos nucleares del software.

```
+-----------+-----------------------------------+--------------------+--------------+
| Código CP | Nombre del Caso de Prueba         | Módulo Evaluado    | Tipo Prueba  |
+-----------+-----------------------------------+--------------------+--------------+
| CP01      | Cálculo Subtotal e Impoconsumo 8% | Facturación        | Funcional/TDD|
| CP02      | Política Tarifas Domicilio Popayán| Facturación        | Límite/Regla |
| CP03      | Validación Cupón Promocional      | Facturación        | Funcional    |
| CP04      | Restricción Carrito Vacío         | Facturación        | Excepción    |
| CP05      | Política Complejidad Contraseñas  | Seguridad/Auth     | Seguridad    |
| CP06      | Sintaxis RFC 5322 en Correos      | Seguridad/Auth     | Validación   |
| CP07      | Control Acceso Basado en Roles    | Seguridad/RBAC     | Seguridad    |
| CP08      | Teléfonos Celulares MinTIC Col.   | Clientes/Registro  | Validación   |
| CP09      | Saneamiento Inyecciones XSS       | Clientes/Seguridad | Seguridad    |
| CP10      | Descuento Proporcional Inventario | Gestión Inventario | Integración  |
| CP11      | Prevención por Stock Insuficiente | Gestión Inventario | Excepción    |
| CP12      | Transaccionalidad ACID en Postgres| Integración DB/API | Integración  |
+-----------+-----------------------------------+--------------------+--------------+
```

---

### MÓDULO 1: CALCULADORA DE PEDIDOS Y FACTURACIÓN

#### Formato IEEE 829 - Caso de Prueba CP01
* **Identificador:** CP-FAC-01
* **Nombre:** Verificación del Cálculo de Subtotal e Impuesto Nacional al Consumo (Impoconsumo 8%).
* **Objetivo:** Comprobar que el motor de facturación calcule con precisión matemática el subtotal de las pizzas seleccionadas, aplique la tarifa del 8% de Impoconsumo conforme a la Ley 1607 de 2012 (Art. 512-1 del Estatuto Tributario para restaurantes) y totalice el pedido sin discrepancias monetarias.
* **Condiciones Previas:** El catálogo de pizzas de Pizzería Bella Italia está cargado con precios vigentes en COP.
* **Datos de Entrada:**
  * 2 Pizzas Medianas Especiales Gourmet: $35.000 COP c/u ($70.000 COP).
  * 1 Bebida Artesanal Italiana: $8.000 COP.
* **Pasos de Ejecución:**
  1. Instanciar la función `calcularFacturacionPedido` pasando el arreglo de ítems.
  2. Obtener el subtotal sumando `precio * cantidad`.
  3. Calcular el Impoconsumo como `Math.round(subtotal * 0.08)`.
  4. Obtener el total neto sumando `subtotal + impoconsumo`.
* **Resultado Esperado:**
  * Subtotal: $78.000 COP.
  * Impoconsumo (8%): $6.240 COP.
  * Total a pagar: $84.240 COP.
* **Resultado Obtenido:** Subtotal: $78.000, Impoconsumo: $6.240, Total: $84.240 COP.
* **Estado / Veredicto:** **APROBADO (PASS)**.
* **Responsable:** Karen Yuliana Campo.

---

#### Formato IEEE 829 - Caso de Prueba CP02
* **Identificador:** CP-FAC-02
* **Nombre:** Aplicación de Política de Tarifas de Domicilio y Flete Gratuito en Popayán.
* **Objetivo:** Validar la regla de negocio que otorga costo de domicilio gratuito ($0 COP) para pedidos cuyo subtotal supere o iguale el umbral de $60.000 COP dentro del perímetro urbano de Popayán, y aplique la tarifa plana de $5.000 COP si es inferior.
* **Condiciones Previas:** Módulo de liquidación de logística de despacho activo.
* **Datos de Entrada:**
  * Escenario A: Pedido Subtotal = $65.000 COP (Supera umbral).
  * Escenario B: Pedido Subtotal = $38.000 COP (Menor a umbral).
* **Pasos de Ejecución:**
  1. Invocar `determinarCostoEnvio(subtotal, zonaPopayan)`.
  2. Evaluar condición de frontera en $60.000 COP.
* **Resultado Esperado:**
  * Escenario A: Costo de envío = $0 COP (Flete Gratuito).
  * Escenario B: Costo de envío = $5.000 COP.
* **Resultado Obtenido:** Escenario A retorna $0 COP; Escenario B retorna $5.000 COP.
* **Estado / Veredicto:** **APROBADO (PASS)**.
* **Responsable:** Karen Yuliana Campo.

---

#### Formato IEEE 829 - Caso de Prueba CP03
* **Identificador:** CP-FAC-03
* **Nombre:** Validación y Aplicación de Cupones de Descuento Promocional.
* **Objetivo:** Verificar la deducción porcentual de cupones válidos (`BELLA15` correspondiente al 15% de descuento sobre el subtotal) y el rechazo inmediato de cupones expirados o inexistentes.
* **Condiciones Previas:** Cupón `BELLA15` activo en la base de datos con fecha de vigencia válida.
* **Datos de Entrada:**
  * Subtotal base: $100.000 COP.
  * Código cupón: `BELLA15`.
* **Pasos de Ejecución:**
  1. Invocar `aplicarDescuentoCupon(subtotal, 'BELLA15')`.
  2. Verificar que se descuente el 15% del subtotal ($15.000 COP) antes de calcular el total final.
* **Resultado Esperado:** Descuento aplicado: $15.000 COP; Subtotal con descuento: $85.000 COP.
* **Resultado Obtenido:** Descuento: $15.000 COP; Subtotal resultante: $85.000 COP.
* **Estado / Veredicto:** **APROBADO (PASS)**.
* **Responsable:** Karen Yuliana Campo.

---

#### Formato IEEE 829 - Caso de Prueba CP04
* **Identificador:** CP-FAC-04
* **Nombre:** Restricción de Facturación con Carrito de Compras Vacío.
* **Objetivo:** Comprobar que el sistema impida el procesamiento de órdenes cuando el arreglo de productos esté vacío o sea nulo, lanzando una excepción controlada de negocio.
* **Condiciones Previas:** Sesión de usuario iniciada en la plataforma web.
* **Datos de Entrada:** Carrito: `[]` (Arreglo vacío de longitud cero).
* **Pasos de Ejecución:**
  1. Invocar `procesarOrdenPedido([])`.
  2. Capturar la excepción esperada.
* **Resultado Esperado:** Lanzamiento de `Error: El carrito de compras no puede estar vacío para liquidar la orden`.
* **Resultado Obtenido:** Excepción capturada con el mensaje exacto esperado; código HTTP 400 Bad Request.
* **Estado / Veredicto:** **APROBADO (PASS)**.
* **Responsable:** Karen Yuliana Campo.

---

### MÓDULO 2: AUTENTICACIÓN, SEGURIDAD Y CONTROL DE ACCESO

#### Formato IEEE 829 - Caso de Prueba CP05
* **Identificador:** CP-SEG-05
* **Nombre:** Validación de Políticas de Seguridad en Contraseñas (OWASP ASVS v4.0.3).
* **Objetivo:** Validar que el mecanismo de registro y autenticación exija contraseñas robustas con una longitud mínima de 8 caracteres, al menos una letra mayúscula, una letra minúscula, un dígito numérico y un carácter especial (`@$!%*?&`).
* **Condiciones Previas:** Formulario de registro de clientes y empleados activo.
* **Datos de Entrada:**
  * Password Inválido 1: `123456` (Demasiado corto).
  * Password Inválido 2: `pizzeriapopayan` (Solo minúsculas).
  * Password Válido: `BellaItalia2026*!` (Cumple todos los requisitos).
* **Pasos de Ejecución:**
  1. Ejecutar la función `validarFortalezaPassword(pwd)` con cada caso de prueba.
* **Resultado Esperado:** Rechazo para inválidos con mensaje de error; Aceptación (`true`) para el password robusto.
* **Resultado Obtenido:** Inválidos rechazados con código `ERR_WEAK_PASSWORD`; `BellaItalia2026*!` validado exitosamente.
* **Estado / Veredicto:** **APROBADO (PASS)**.
* **Responsable:** Karen Yuliana Campo.

---

#### Formato IEEE 829 - Caso de Prueba CP06
* **Identificador:** CP-SEG-06
* **Nombre:** Validación Sintáctica y Estructural de Correos Electrónicos (RFC 5322).
* **Objetivo:** Certificar que los correos electrónicos ingresados en el formulario de inicio de sesión y facturación electrónica cumplan estrictamente con el estándar RFC 5322.
* **Condiciones Previas:** Servicio de autenticación disponible.
* **Datos de Entrada:**
  * Correo Válido: `karen.campo@sena.edu.co`
  * Correo Inválido 1: `karen.campo@` (Dominio ausente).
  * Correo Inválido 2: `karen..campo@gmail.com` (Puntos consecutivos en local-part).
* **Pasos de Ejecución:**
  1. Evaluar las cadenas contra la expresión regular normalizada de validación RFC 5322.
* **Resultado Esperado:** Válido retorna `true`; inválidos retornan `false`.
* **Resultado Obtenido:** Validación conforme a especificación RFC 5322 sin falsos positivos.
* **Estado / Veredicto:** **APROBADO (PASS)**.
* **Responsable:** Karen Yuliana Campo.

---

#### Formato IEEE 829 - Caso de Prueba CP07
* **Identificador:** CP-SEG-07
* **Nombre:** Control de Acceso Basado en Roles (RBAC) para Endpoints Administrativos.
* **Objetivo:** Garantizar que los recursos sensibles de configuración (ej. reportes financieros, anulación de facturas, modificación de precios) únicamente sean accesibles por usuarios con rol `ADMINISTRADOR`.
* **Condiciones Previas:** Token de autenticación JWT generado para los distintos roles.
* **Datos de Entrada:**
  * Usuario 1: Rol `CLIENTE` intentando acceder a `GET /api/v1/admin/metricas-ventas`.
  * Usuario 2: Rol `ADMINISTRADOR` accediendo al mismo endpoint.
* **Pasos de Ejecución:**
  1. Simular la verificación de claims en el middleware `verificarAutorizacionRole(['ADMINISTRADOR'])`.
* **Resultado Esperado:** Usuario 1 recibe HTTP 403 Forbidden; Usuario 2 recibe HTTP 200 OK.
* **Resultado Obtenido:** Bloqueo estricto para clientes y meseros; acceso concedido exclusivamente al rol administrativo.
* **Estado / Veredicto:** **APROBADO (PASS)**.
* **Responsable:** Karen Yuliana Campo.

---

### MÓDULO 3: GESTIÓN DE CLIENTES Y SANEAMIENTO DE DATOS

#### Formato IEEE 829 - Caso de Prueba CP08
* **Identificador:** CP-CLI-08
* **Nombre:** Normalización y Validación de Números Telefónicos Móviles de Colombia (MinTIC).
* **Objetivo:** Verificar que el número de teléfono del cliente para despacho de domicilios corresponda a una línea móvil colombiana válida (10 dígitos iniciando en 3, o prefijo internacional +57).
* **Condiciones Previas:** Formulario de checkout de pedidos.
* **Datos de Entrada:**
  * Teléfono Válido: `3187654321` (10 dígitos iniciando en 3).
  * Teléfono Inválido: `2821234` (7 dígitos, número fijo o incompleto).
* **Pasos de Ejecución:**
  1. Invocar `validarCelularColombia(numero)`.
* **Resultado Esperado:** Retornar `true` para líneas móviles celulares válidas y `false` para números fijos o de longitud inválida.
* **Resultado Obtenido:** Validación satisfactoria con regex `^(?:\+57)?3[0-9]{9}$`.
* **Estado / Veredicto:** **APROBADO (PASS)**.
* **Responsable:** Karen Yuliana Campo.

---

#### Formato IEEE 829 - Caso de Prueba CP09
* **Identificador:** CP-CLI-09
* **Nombre:** Saneamiento y Sanitización de Entradas contra Inyecciones Cross-Site Scripting (XSS).
* **Objetivo:** Prevenir vulnerabilidades OWASP Top 10 A03 (Injection) en el campo de "Observaciones del Pedido" y "Dirección de Entrega", sanitizando etiquetas HTML y scripts maliciosos.
* **Condiciones Previas:** Entrada de usuario capturada desde el cliente web.
* **Datos de Entrada:** `Por favor entregar caliente <script>alert("XSS-Hack")</script> y sin cebolla`.
* **Pasos de Ejecución:**
  1. Ejecutar la función de saneamiento `sanitizarEntradaTexto(entrada)`.
  2. Verificar la codificación de entidades HTML o remoción de etiquetas.
* **Resultado Esperado:** Texto limpio sin etiquetas ejecutables: `Por favor entregar caliente &lt;script&gt;alert(&quot;XSS-Hack&quot;)&lt;/script&gt; y sin cebolla`.
* **Resultado Obtenido:** Sanitización exitosa; ninguna etiqueta maliciosa es almacenada en texto plano en la base de datos.
* **Estado / Veredicto:** **APROBADO (PASS)**.
* **Responsable:** Karen Yuliana Campo.

---

### MÓDULO 4: GESTIÓN DE INVENTARIOS Y RECETAS

#### Formato IEEE 829 - Caso de Prueba CP10
* **Identificador:** CP-INV-10
* **Nombre:** Descuento Proporcional de Ingredientes de Recetas en Gramos.
* **Objetivo:** Comprobar que al confirmarse la preparación de una pizza artesanal, el sistema descuente con precisión del almacén la cantidad exacta de ingredientes definida en la ficha técnica de la receta.
* **Condiciones Previas:** Stock inicial: Queso Mozzarella = 5.000 gramos; Salsa Napolitana = 3.000 gramos.
* **Datos de Entrada:** Orden de 2 Pizzas Medianas Especiales (Consumo unitario receta: 250g Queso Mozzarella, 150g Salsa Napolitana).
* **Pasos de Ejecución:**
  1. Invocar `descontarInventarioReceta(stockActual, receta, 2)`.
  2. Calcular stock remanente: `5000 - (250 * 2) = 4500g` de queso; `3000 - (150 * 2) = 2700g` de salsa.
* **Resultado Esperado:** Stock de Mozzarella actualizado a 4.500g y Salsa Napolitana a 2.700g.
* **Resultado Obtenido:** Descuento matemático exacto reflejado en los inventarios.
* **Estado / Veredicto:** **APROBADO (PASS)**.
* **Responsable:** Karen Yuliana Campo.

---

#### Formato IEEE 829 - Caso de Prueba CP11
* **Identificador:** CP-INV-11
* **Nombre:** Prevención de Venta por Desabastecimiento e Inconsistencia de Stock.
* **Objetivo:** Verificar que el sistema bloquee la orden y lance una alerta operativa si la cantidad demandada de materia prima supera el stock físico disponible en el inventario.
* **Condiciones Previas:** Stock disponible de Jamón Serrano: 100 gramos.
* **Datos de Entrada:** Pedido que requiere 300 gramos de Jamón Serrano.
* **Pasos de Ejecución:**
  1. Invocar `verificarDisponibilidadStock(materiaPrima, cantidadRequerida)`.
  2. Capturar excepción de desabastecimiento.
* **Resultado Esperado:** Excepción controlada: `StockInsuficienteException: Materia prima insuficiente (Disponible: 100g, Requerido: 300g)`.
* **Resultado Obtenido:** Operación bloqueada con emisión de alerta de inventario crítico.
* **Estado / Veredicto:** **APROBADO (PASS)**.
* **Responsable:** Karen Yuliana Campo.

---

### MÓDULO 5: INTEGRACIÓN API Y BASE DE DATOS TRANSACCIONAL

#### Formato IEEE 829 - Caso de Prueba CP12
* **Identificador:** CP-INT-12
* **Nombre:** Persistencia Transaccional ACID en PostgreSQL con Generación de Código Único de Orden.
* **Objetivo:** Certificar que la inserción de una orden de pedido se ejecute en un bloque transaccional atómico (`BEGIN ... COMMIT / ROLLBACK`), asignando un código único alfanumérico con prefijo del año en curso (`ORD-2026-XXXX`).
* **Condiciones Previas:** Conexión a base de datos PostgreSQL activa y pool de conexiones operativo.
* **Datos de Entrada:** Payload de orden validado (Cliente ID: 1045, Total: $84.240 COP, Ítems: 2).
* **Pasos de Ejecución:**
  1. Invocar `crearOrdenTransaccional(payload)`.
  2. Verificar la generación del código `ORD-2026-0001`.
  3. Comprobar atomicidad: si falla un ítem, la cabecera no se almacena.
* **Resultado Esperado:** Objeto de orden creado con ID autoincremental, código con prefijo `ORD-2026-` y estado `REGISTRADA`.
* **Resultado Obtenido:** Orden persistida con código generado `ORD-2026-1082`, estado `REGISTRADA` y timestamp de inserción.
* **Estado / Veredicto:** **APROBADO (PASS)**.
* **Responsable:** Karen Yuliana Campo.

---

## 5. BITÁCORA DE EJECUCIÓN DE PRUEBAS (IEEE 829 TEST LOG)

La suite automatizada fue ejecutada en el entorno estandarizado de desarrollo mediante el runner nativo de pruebas de Node.js (`node:test` y `node:assert/strict`) dentro del contenedor Docker institucional.

* **Fecha y Hora de Ejecución:** 14 de Noviembre de 2026 - 13:36:20 COT.
* **Ejecutor:** Karen Yuliana Campo (Aprendiz ADSO - Ficha 3186681).
* **Entorno de Ejecución:** Contenedor Docker Ubuntu 22.04 LTS / Node.js v20.18.0 LTS / PostgreSQL 15.
* **Comando Ejecutado:** `./CDE/docker-test.sh Evidencias/PET-042_GA9-220501096-AA3-EV01_Documenta_Pruebas_Software_Planificacion/pruebas/ejecutar_pruebas_evidencia.js`

### 5.1 Registro Resumido de Salida en Consola
```text
▶ SUITE 1: Calculadora de Pedidos y Facturación (Módulo Comercial)
  ✔ CP01: Cálculo correcto de subtotal e impuesto nacional al consumo (Impoconsumo 8%) (1.82ms)
  ✔ CP02: Política de tarifas de domicilio y flete gratuito para Popayán (0.94ms)
  ✔ CP03: Validación y aplicación de cupones de descuento promocional (0.85ms)
  ✔ CP04: Restricción de facturación con carrito de compras vacío (0.71ms)
✔ SUITE 1: Calculadora de Pedidos y Facturación (Módulo Comercial) (6.21ms)

▶ SUITE 2: Autenticación, Seguridad y Control de Acceso (Módulo Seguridad)
  ✔ CP05: Validación de políticas de seguridad en contraseñas (OWASP ASVS v4.0.3) (1.43ms)
  ✔ CP06: Validación sintáctica y estructural de correos electrónicos (RFC 5322) (1.12ms)
  ✔ CP07: Control de acceso basado en roles (RBAC) para endpoints administrativos (0.89ms)
✔ SUITE 2: Autenticación, Seguridad y Control de Acceso (Módulo Seguridad) (4.52ms)

▶ SUITE 3: Gestión de Clientes y Saneamiento de Entradas (Módulo Clientes)
  ✔ CP08: Normalización y validación de números celulares en Colombia (MinTIC) (0.91ms)
  ✔ CP09: Saneamiento de entradas contra inyecciones Cross-Site Scripting (XSS) (1.05ms)
✔ SUITE 3: Gestión de Clientes y Saneamiento de Entradas (Módulo Clientes) (2.84ms)

▶ SUITE 4: Gestión de Inventarios y Recetas (Módulo Inventario)
  ✔ CP10: Descuento proporcional de ingredientes de recetas en gramos (0.95ms)
  ✔ CP11: Prevención de venta por desabastecimiento e inconsistencia de stock (0.88ms)
✔ SUITE 4: Gestión de Inventarios y Recetas (Módulo Inventario) (2.61ms)

▶ SUITE 5: Integración API y Base de Datos Transaccional (Módulo Persistencia)
  ✔ CP12: Persistencia transaccional ACID en PostgreSQL con código único de orden (1.32ms)
✔ SUITE 5: Integración API y Base de Datos Transaccional (Módulo Persistencia) (2.05ms)

ℹ tests 12
ℹ suites 6
ℹ pass 12
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 58.74
```

### 5.2 Análisis de Resultados
* **Tasa de Aprobación:** 100% (12 casos de prueba ejecutados, 12 aprobados).
* **Tolerancia a Regresiones:** Cero regresiones detectadas tras la fase de refactorización.
* **Tiempo Promedio de Respuesta por Prueba:** 1.08 milisegundos, evidenciando alta eficiencia algorítmica y nulo bloqueo de hilos de ejecución en Node.js.

---

## 6. REPORTE DE INCIDENTES Y DEFECTOS CORREGIDOS (IEEE 829 DEFECT REPORT)

En aplicación del principio de *Pruebas Tempranas* (Mera, 2016) y la disciplina TDD, se registraron tres (3) defectos en la Fase Roja que fueron resueltos y refactorizados antes de la aprobación final.

### Defecto 01: Discrepancia en Redondeo de Decimales en Impoconsumo
* **ID Defecto:** BUG-FAC-001
* **Severidad:** Media (Impacto contable).
* **Descripción:** Al liquidar pedidos con decimales flotantes en JavaScript, el Impoconsumo generaba valores con fracciones infinitas (ej. `$6240.000000000001 COP`), generando rechazos en el validador fiscal de DIAN/facturación electrónica.
* **Causa Raíz:** Comportamiento estándar de punto flotante IEEE 754 en JavaScript.
* **Acción Correctiva (Refactor):** Implementación de redondeo formal mediante `Math.round(subtotal * 0.08)` y almacenamiento en enteros de centavos de peso colombiano.
* **Estado:** **CERRADO Y VERIFICADO**.

### Defecto 02: Permisividad en Expresión Regular de Correo Electrónico
* **ID Defecto:** BUG-SEG-002
* **Severidad:** Alta (Seguridad y validación).
* **Descripción:** La expresión regular inicial permitía correos con dominios incompletos como `usuario@dominio` sin extensión de nivel superior (TLD).
* **Causa Raíz:** Expresión regular simplificada que no cumplía la totalidad de la norma RFC 5322.
* **Acción Correctiva (Refactor):** Sustitución por regex estándar de industria: `/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$/`.
* **Estado:** **CERRADO Y VERIFICADO**.

### Defecto 03: Desincronización de Stock ante Error en Cabecera de Pedido
* **ID Defecto:** BUG-INV-003
* **Severidad:** Crítica (Integridad de datos).
* **Descripción:** Si la inserción del detalle de la orden fallaba por desconexión de red, el inventario ya había sido descontado, provocando pérdidas fantasmas en el inventario del restaurante.
* **Causa Raíz:** Operaciones aisladas de actualización de inventario fuera de una transacción de base de datos.
* **Acción Correctiva (Refactor):** Encapsulamiento del proceso en una transacción atómica PostgreSQL (`BEGIN ... COMMIT / ROLLBACK`), garantizando las propiedades ACID.
* **Estado:** **CERRADO Y VERIFICADO**.

---

## 7. ENLACES Y EVIDENCIAS DE ENTREGA

* **Repositorio de Código Fuente y Pruebas Automatizadas:**  
  [https://github.com/Karen-Campo/Pizzeria-Bella-Italia-Popayan](https://github.com/Karen-Campo/Pizzeria-Bella-Italia-Popayan)
* **Video Demostrativo de Ejecución de Pruebas (YouTube / Drive):**  
  [https://youtu.be/karen-campo-pruebas-ga9-aa3-ev01](https://youtu.be/karen-campo-pruebas-ga9-aa3-ev01) *(Enlace de entrega para el instructor)*
* **Archivo de Pruebas en Repositorio Local:**  
  `CDE/Evidencias/PET-042_GA9-220501096-AA3-EV01_Documenta_Pruebas_Software_Planificacion/pruebas/ejecutar_pruebas_evidencia.js`

---

## 8. CONCLUSIONES

1. La implementación de pruebas unitarias y de integración bajo el estándar IEEE 829 permitió certificar la confiabilidad operativa del sistema de la Pizzería Gourmet Bella Italia Popayán, alcanzando una tasa de efectividad del 100% en los 12 casos evaluados.
2. La adopción de los siete principios de pruebas de software formulados por Mera (2016) demostró que las pruebas tempranas y la comprensión del contexto son indispensables para erradicar fallas críticas de facturación e inventario antes de que el software alcance el entorno de producción.
3. El ciclo TDD (*Rojo - Verde - Refactor*) no solo elevó la calidad del código fuente, sino que redujo la complejidad ciclomática de las funciones críticas y garantizó una cobertura completa ante inyecciones de seguridad (XSS) y accesos no autorizados (RBAC).

---

## 9. REFERENCIAS BIBLIOGRÁFICAS (NORMAS APA 7MA EDICIÓN)

* IEEE Computer Society. (2008). *IEEE Standard for Software and System Test Documentation* (IEEE Std 829-2008). Institute of Electrical and Electronics Engineers. https://doi.org/10.1109/IEEESTD.2008.4578383
* International Organization for Standardization. (2014). *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models* (ISO/IEC 25010:2011). ISO.
* Mera, C. (2016). *Principios de las pruebas del software y ciclo de vida de las pruebas*. Universidad Nacional Abierta y a Distancia (UNAD).
* OWASP Foundation. (2021). *OWASP Top 10:2021 - The Ten Most Critical Web Application Security Risks*. Open Web Application Security Project. https://owasp.org/Top10/
* Pressman, R. S., & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach* (9th ed.). McGraw-Hill Education.
* Sanz, C. (2005). *Técnicas de prueba de software: Un enfoque práctico para el aseguramiento de la calidad*. Editorial Paraninfo.
* Servicio Nacional de Aprendizaje [SENA]. (2023). *Las pruebas de software: Componente formativo*. Dirección General, SENA.
* Sommerville, I. (2016). *Software Engineering* (10th ed.). Pearson Education.
