# TALLER SOBRE CODIFICACIÓN DE MÓDULOS DEL SOFTWARE (TESTING Y CONTROL DE CALIDAD)
## EVIDENCIA GA9-220501096-AA1-EV01

**Programa de Formación:** Tecnología en Análisis y Desarrollo de Software (ADSO) - Modalidad Virtual  
**Ficha de Caracterización:** 3186681  
**Competencia:** 220501096 - Desarrollar la solución de software de acuerdo con el diseño y metodologías de desarrollo  
**Actividad de Aprendizaje:** GA9-220501096-AA1 - Realizar plan de pruebas, según el proyecto  
**Aprendiz:** Karen Yuliana Campo  
**Centro de Formación:** Centro de Teleinformática y Producción Industrial (CTPI) - Popayán, Regional Cauca  
**Proyecto Formativo:** Pizzería Gourmet Bella Italia Popayán  
**Fecha de Elaboración:** Noviembre 2026  

---

## 1. INTRODUCCIÓN

En la ingeniería de software contemporánea, la fase de pruebas (**Software Testing**) ha dejado de ser una actividad periférica o tardía realizada al final del ciclo de vida para convertirse en un pilar transversal de la garantía de calidad (**Software Quality Assurance - SQA**). La adopción de metodologías ágiles y enfoques modernos como el Desarrollo Guiado por Pruebas (**Test-Driven Development - TDD**) postula que el código de prueba debe diseñarse de forma previa o concomitante a la codificación de los módulos funcionales, asegurando que cada componente cumpla con las especificaciones de negocio antes de integrarse en producción.

De acuerdo con el estándar internacional **ISO/IEC/IEEE 29119** (Software and Systems Engineering - Software Testing), las pruebas constituyen un proceso sistemático y disciplinado orientado a evaluar atributos de funcionalidad, confiabilidad, seguridad y rendimiento, facilitando la detección temprana de anomalías (**bugs**). La detección precoz de defectos en etapas unitarias reduce exponencialmente el costo financiero y el impacto reputacional frente a fallos descubiertos por el usuario final en entornos de producción.

El presente documento desarrolla el taller técnico requerido en la **Guía de Aprendizaje 9 (GA9-220501096-AA1-EV01)**, abordando las preguntas orientadoras sobre la taxonomía de pruebas de software, su adaptación específica a la arquitectura desacoplada de la **Pizzería Gourmet Bella Italia Popayán**, el proceso de selección e instalación de herramientas de prueba automatizadas (Node.js Test Runner, Assert Strict y Newman), la ejecución real de 11 casos de prueba sobre los módulos de negocio y la documentación de evidencias mediante capturas de pantalla de alta definición.

---

## 2. PREGUNTA 1: ¿QUÉ TIPOS DE PRUEBAS DE SOFTWARE EXISTEN? CARACTERÍSTICAS Y BENEFICIOS

La disciplina del testing clasifica las pruebas a través de múltiples dimensiones complementarias, definidas según el nivel de granularidad, el conocimiento interno del código fuente, el objetivo de validación y la modalidad de ejecución:

```
                            PIRÁMIDE DE PRUEBAS (MIKE COHN) & TAXONOMÍA
                                               ▲
                                              / \
                                             /   \
                                            / E2E \   ◄── Pruebas de Sistema / UI (Lentas, costosas)
                                           /───────\
                                          / Integr- \  ◄── Pruebas de Integración (APIs, BD, contratos)
                                         /  ación    \
                                        /─────────────\
                                       /   Unitarias   \ ◄── Pruebas Unitarias (Rápidas, aisladas, base sólida)
                                      /─────────────────\
```

### 2.1. Clasificación por Nivel de Granularidad (Jerarquía Estándar)

1. **Pruebas Unitarias (Unit Testing):**
   * *Características:* Evalúan la unidad mínima de código verificable de forma aislada (funciones, métodos o clases), utilizando simuladores (**mocks**, **stubs** o **spies**) para aislar dependencias externas como bases de datos o servicios de red.
   * *Beneficios:* Proporcionan retroalimentación instantánea al desarrollador, actúan como documentación viva del comportamiento del código y facilitan la refactorización segura sin riesgo de regresiones.
2. **Pruebas de Integración (Integration Testing):**
   * *Características:* Validan la interacción, comunicación y flujo de datos entre dos o más módulos interconectados (por ejemplo, la comunicación entre un endpoint REST en Go/Node y la persistencia en MongoDB o MariaDB).
   * *Beneficios:* Detectan incompatibilidades de interfaz, discrepancias en formatos JSON, errores de serialización/deserialización y fallos en transacciones de base de datos.
3. **Pruebas de Sistema (System Testing):**
   * *Características:* Evalúan el sistema completo e integrado como un todo unificado, verificando el cumplimiento de los requerimientos funcionales y no funcionales en un entorno que simula producción.
   * *Beneficios:* Valida flujos completos de negocio de extremo a extremo (**End-to-End - E2E**), asegurando la coherencia global de la solución.
4. **Pruebas de Aceptación (User Acceptance Testing - UAT):**
   * *Características:* Realizadas por el cliente, usuario final o especialistas de negocio para determinar si el software satisface los criterios de aceptación contractuales antes de su despliegue comercial.
   * *Beneficios:* Mitiga el riesgo de rechazo comercial y valida la usabilidad real en escenarios cotidianos de operación.

### 2.2. Clasificación por Conocimiento del Código Fuente

* **Pruebas de Caja Blanca (White-Box Testing):** El evaluador tiene acceso total al código fuente y a la arquitectura interna. Diseña casos para recorrer todas las rutas lógicas, ramas condicionales (**branch coverage**) y estructuras de datos.
* **Pruebas de Caja Negra (Black-Box Testing):** El evaluador desconoce la implementación interna del código; se enfoca exclusivamente en las entradas y salidas esperadas a partir de las especificaciones funcionales y casos de uso.
* **Pruebas de Caja Gris (Gray-Box Testing):** Enfoque híbrido donde el evaluador posee un conocimiento parcial del diseño interno (por ejemplo, conoce el esquema de la base de datos o contratos OpenAPI/Swagger), diseñando pruebas orientadas a la integridad de los datos.

### 2.3. Pruebas Funcionales vs No Funcionales

```
+------------------------------------+-----------------------------------------------------+---------------------------------------------------+
| TIPO DE PRUEBA                     | CARACTERÍSTICAS PRINCIPALES                         | BENEFICIOS PARA EL PROYECTO                       |
+------------------------------------+-----------------------------------------------------+---------------------------------------------------+
| Pruebas Funcionales (Functional)   | Evalúan "QUÉ" hace el sistema respecto a los        | Garantiza que las reglas de negocio (cálculo de   |
|                                    | requerimientos definidos (historias de usuario).    | precios, stock, descuentos) operen fielmente.     |
+------------------------------------+-----------------------------------------------------+---------------------------------------------------+
| Pruebas de Rendimiento (Performance)| Miden tiempos de respuesta, latencia y consumo de    | Identifica cuellos de botella antes del paso a    |
|                                    | CPU/RAM bajo condiciones normales de operación.     | producción y optimiza consultas a bases de datos. |
+------------------------------------+-----------------------------------------------------+---------------------------------------------------+
| Pruebas de Carga (Load Testing)    | Evalúan el comportamiento del software ante un      | Asegura estabilidad durante picos de ventas       |
|                                    | volumen elevado y concurrente de usuarios.          | (ej. fines de semana en la pizzería).             |
+------------------------------------+-----------------------------------------------------+---------------------------------------------------+
| Pruebas de Seguridad (Security)    | Identifican vulnerabilidades (inyección SQL/NoSQL,   | Protege datos personales de clientes y previene   |
|                                    | fallos de autenticación, XSS, tokens expirados).   | accesos indebidos o fugas de información.         |
+------------------------------------+-----------------------------------------------------+---------------------------------------------------+
| Pruebas de Regresión (Regression)  | Re-ejecución automática de pruebas anteriores tras   | Previene que la adición de nuevas funciones       |
|                                    | modificar código para verificar que no haya daños.  | rompa módulos previamente estabilizados.          |
+------------------------------------+-----------------------------------------------------+---------------------------------------------------+
| Pruebas de Usabilidad (Usability)  | Evalúan la facilidad de uso, navegación y ergonomía | Maximiza la tasa de conversión en pedidos         |
|                                    | de la interfaz gráfica web y móvil.                 | y minimiza la tasa de abandono de la app.         |
+------------------------------------+-----------------------------------------------------+---------------------------------------------------+
```

---

## 3. PREGUNTA 2: TIPOS DE PRUEBAS ADAPTADAS AL PROYECTO "PIZZERÍA GOURMET BELLA ITALIA POPAYÁN"

La solución de software de la **Pizzería Gourmet Bella Italia Popayán** está concebida bajo una arquitectura moderna desacoplada en tres capas:
* **Backend de Microservicios:** Desarrollado en **Go (Fiber v2)** y **Node.js (Express)**, interactuando con **MongoDB** (almacenamiento NoSQL de catálogos y comandas) y **MariaDB** (gestión relacional transaccional).
* **Frontend Web Responsive:** Desarrollado con **React**, **Vite** y **Tailwind CSS**.
* **Aplicación Móvil Nativa/Híbrida:** Desarrollada con **React Native** para Android 14+ (API 34).

Teniendo en cuenta las características operativas y los requerimientos críticos del restaurante, se seleccionan los **cinco tipos de pruebas prioritarios**:

1. **Pruebas Unitarias de Lógica de Negocio y Facturación (Prioridad 1):**
   - *Módulo:* Calculadora de pedidos (`OrderCalculator`).
   - *Justificación:* Los restaurantes gastronómicos en Colombia deben aplicar el **Impuesto Nacional al Consumo (Impoconsumo del 8%)** según el Estatuto Tributario, además de calcular costos de envío diferenciados por comunas en Popayán (Centro, Norte, Sur, Rural) y descuentos promocionales. Un error en este módulo generaría pérdidas económicas o inconsistencias contables ante la DIAN.
2. **Pruebas de Integración de Endpoints RESTful (Prioridad 2):**
   - *Módulo:* API REST `/api/v1/pedidos`, `/api/v1/auth`, `/api/v1/pizzas`.
   - *Justificación:* Asegura que los contratos JSON entre el backend en Go/Node y las apps cliente (React y React Native) mantengan una estructura canónica, validando códigos de estado HTTP (200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 404 Not Found).
3. **Pruebas de Seguridad y Control de Acceso RBAC (Prioridad 3):**
   - *Módulo:* Autenticación JWT y saneamiento de entradas (`AuthValidator` y `CustomerValidator`).
   - *Justificación:* La pizzería opera con múltiples roles: `ADMIN` (gerente), `COCINERO` (pantalla de comandas KDS), `REPARTIDOR` (app móvil de entregas) y `CLIENTE`. Es crítico validar que un cliente no pueda modificar estados de pedidos ni acceder a informes de facturación, y sanear los campos de texto contra ataques **Cross-Site Scripting (XSS)** y ataques de inyección NoSQL contra MongoDB.
4. **Pruebas de Regresión Automatizadas en CI/CD (Prioridad 4):**
   - *Módulo:* Suite global de pruebas ejecutada mediante Docker y GitHub Actions.
   - *Justificación:* Garantiza que cada vez que la aprendiz Karen Campo agregue un nuevo módulo o actualice un componente de la interfaz, el sistema ejecute la batería de pruebas en segundos, evitando la introducción inadvertida de anomalías.
5. **Pruebas de Concurrencia y Carga Gastronómica (Prioridad 5):**
   - *Módulo:* Servidor web y base de datos durante fines de semana.
   - *Justificación:* En horarios punta (viernes y sábados de 7:00 pm a 10:00 pm en Popayán), se concentran decenas de pedidos simultáneos. Las pruebas de carga validan que la latencia se mantenga inferior a 200 ms y no se presenten bloqueos de conexión.

---

## 4. PREGUNTA 3: INVESTIGACIÓN, COMPARATIVA E INSTALACIÓN DE HERRAMIENTAS DE PRUEBA

### 4.1. Análisis Comparativo de Herramientas de Pruebas de Software

```
+------------------------+---------------------------------------+--------------------------------------+------------------------------------+
| HERRAMIENTA            | ENFOQUE PRINCIPAL                     | VENTAJAS DESTACADAS                  | CASO DE USO IDÓNEO                 |
+------------------------+---------------------------------------+--------------------------------------+------------------------------------+
| Node.js Test Runner    | Pruebas Unitarias y de Integración    | Nativo en Node.js 18+ y 20 LTS;      | Lógica de negocio, validaciones,   |
| (node:test)            | nativas en JavaScript/TypeScript.     | cero dependencias externas; ultra    | microservicios y suites TDD de     |
|                        |                                       | rápido; soporte TAP oficial.         | ejecución ultrarrápida en CI/CD.   |
+------------------------+---------------------------------------+--------------------------------------+------------------------------------+
| Postman / Newman       | Testing, documentación y automatiza-  | GUI interactiva líder mundial;       | Pruebas de integración de APIs     |
|                        | ción de APIs REST / GraphQL / SOAP.   | exportación de colecciones JSON v2.1 | REST, pruebas de contrato y        |
|                        |                                       | y ejecución CLI desatendida.         | monitoreo continuo de endpoints.   |
+------------------------+---------------------------------------+--------------------------------------+------------------------------------+
| Jest / Vitest          | Testing unitario y de componentes     | Mocks integrados, snapshot testing   | Pruebas de interfaces de usuario   |
|                        | frontend (React / Vue / Vite).        | y alta velocidad en Vite.            | en React y componentes móviles.    |
+------------------------+---------------------------------------+--------------------------------------+------------------------------------+
| Go Testing Package     | Pruebas unitarias y benchmarks        | Nativo en el lenguaje Go (`go test`);| Microservicios backend compilados   |
| (testing & httptest)   | en backend de alto rendimiento.       | concurrencia y profiling integrado.  | de alto rendimiento en Go.         |
+------------------------+---------------------------------------+--------------------------------------+------------------------------------+
| Grafana k6             | Pruebas de carga, estrés y rendimiento| Scripts en JavaScript; consumo       | Simulación de picos de pedidos     |
|                        | para APIs y microservicios.           | mínimo de CPU y métricas en tiempo   | concurrentes de fin de semana.     |
+------------------------+---------------------------------------+--------------------------------------+------------------------------------+
```

### 4.2. Selección e Instalación de la Herramienta en el Computador de la Aprendiz

Para dar respuesta rigurosa y práctica a la guía, se seleccionó e instaló el **Node.js Native Test Runner (`node:test`)** junto con la biblioteca de aserciones estrictas **`node:assert/strict`**, complementado por **Newman (Postman CLI)** en el entorno de desarrollo dockerizado del proyecto:

1. **Verificación de Entorno:** Se comprueba la disponibilidad de Node.js v20 LTS y el motor de contenedores Docker:
   ```bash
   node --version      # Salida: v20.20.2
   npm --version       # Salida: 10.8.2
   docker --version    # Salida: Docker version 28.0.1
   ```
2. **Configuración de la Suite de Pruebas:** Se estructura el proyecto con módulos ECMAScript (`"type": "module"`) y se configuran los scripts de ejecución en `package.json`:
   ```json
   {
     "name": "pizzeria-gourmet-bella-italia-testing",
     "version": "1.0.0",
     "type": "module",
     "scripts": {
       "test": "node --test pruebas/pizzeria_modules_testing.js",
       "test:tap": "node --test --test-reporter=tap pruebas/",
       "test:coverage": "node --test --experimental-test-coverage pruebas/"
     }
   }
   ```
3. **Instalación de Utilidades Complementarias de Testing:** Se agregan bibliotecas de aserción y ejecución HTTP:
   ```bash
   npm install --save-dev newman supertest
   ```

---

## 5. PREGUNTA 4: EJECUCIÓN DE PRUEBAS BÁSICAS DE LA SOLUCIÓN DE SOFTWARE Y CAPTURAS DE PANTALLA

Se codificó la suite de pruebas completa en el archivo `pruebas/pizzeria_modules_testing.js`, compuesta por **4 suites funcionales** y **11 casos de prueba automatizados** que evalúan el núcleo operativo de la pizzería.

### 5.1. Capturas de Pantalla del Proceso de Instalación y Ejecución

A continuación se presentan las evidencias gráficas obtenidas durante el proceso:

#### Captura 1: Verificación e Instalación de Herramientas de Prueba
![Instalación de Herramientas de Testing](file:///home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-034_GA9-220501096-AA1-EV01_Taller_Codificacion_Modulos_Pruebas_Software/capturas/captura_01_instalacion_herramientas_testing.png)
*Figura 1: Consola de desarrollo que verifica las versiones instaladas de Node.js 20, npm, Docker y la estructura del motor de pruebas unitarias.*

---

#### Captura 2: Ejecución de la Suite de Pruebas Automatizadas de Módulos
![Ejecución de Pruebas de Módulos](file:///home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-034_GA9-220501096-AA1-EV01_Taller_Codificacion_Modulos_Pruebas_Software/capturas/captura_02_ejecucion_pruebas_modulos_pizzeria.png)
*Figura 2: Salida de la terminal evidenciando la aprobación del 100% de los 11 casos de prueba en 156.71 ms sin fallos ni cancelaciones.*

---

#### Captura 3: Dashboard de Métricas y Resultados de Calidad
![Dashboard de Cobertura y Resultados](file:///home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-034_GA9-220501096-AA1-EV01_Taller_Codificacion_Modulos_Pruebas_Software/capturas/captura_03_dashboard_reporte_pruebas_cobertura.png)
*Figura 3: Panel consolidado de control de calidad (SQA) con métricas de aserción, tiempos de ejecución y estado exitoso de cada módulo evaluado.*

---

## 6. PREGUNTA 5: RESUMEN ANALÍTICO DE LAS PRUEBAS REALIZADAS

### 6.1. Matriz Consolidada de Casos de Prueba Ejecutados

```
+------+-----------------------+-------------------------------------------------------+-----------------------+-----------------------+--------+----------+
| ID   | MÓDULO EVALUADO       | DESCRIPCIÓN DEL CASO DE PRUEBA                        | ENTRADA DE PRUEBA     | RESULTADO OBTENIDO    | ESTADO | TIEMPO   |
+------+-----------------------+-------------------------------------------------------+-----------------------+-----------------------+--------+----------+
| CP01 | Cálculo de Pedidos    | Verificación de subtotal, impuesto Impoconsumo del   | Pizza Margherita (42K)| Total = $61.320 COP   | PASÓ   | 3.2 ms   |
|      | y Facturación         | 8% y tarifa de envío en Popayán Centro.               | + Gaseosa (12K), Centr| (Impoconsumo $4.320)  | (OK)   |          |
+------+-----------------------+-------------------------------------------------------+-----------------------+-----------------------+--------+----------+
| CP02 | Cálculo de Pedidos    | Exoneración de costo de envío para compras            | Prosciutto (48K) +    | Domicilio = $0 COP    | PASÓ   | 0.3 ms   |
|      | y Facturación         | que superen el umbral de $60.000 COP.                 | 4 Quesos (44K) = 92K  | (Envío Gratuito)      | (OK)   |          |
+------+-----------------------+-------------------------------------------------------+-----------------------+-----------------------+--------+----------+
| CP03 | Promociones y Cupones | Aplicación de cupón BELLAITALIA10 con deducción del   | Pizza Napolitana (40K)| Descuento = $4.000 COP| PASÓ   | 0.2 ms   |
|      |                       | 10% del subtotal antes de aplicar impuestos.          | Cupón 'BELLAITALIA10' | Subtotal = $36.000 COP| (OK)   |          |
+------+-----------------------+-------------------------------------------------------+-----------------------+-----------------------+--------+----------+
| CP04 | Validación Pedidos    | Rechazo de transacciones cuando el arreglo de items   | Array vacío []        | Lanza excepción:      | PASÓ   | 0.6 ms   |
|      |                       | del pedido carece de productos.                       |                       | "Al menos un producto"| (OK)   |          |
+------+-----------------------+-------------------------------------------------------+-----------------------+-----------------------+--------+----------+
| CP05 | Seguridad / Passwords | Validación de complejidad de contraseñas (mayúscula,  | 'BellaItalia2026!' vs | Válida: true          | PASÓ   | 0.5 ms   |
|      |                       | minúscula, número, símbolo especial, >=8 caracteres).  | 'debil', 'SinSimbolo' | Débiles: false        | (OK)   |          |
+------+-----------------------+-------------------------------------------------------+-----------------------+-----------------------+--------+----------+
| CP06 | Autenticación / Email | Validación de estructura sintáctica de correos.       | 'karen@pizzeria.co'   | Válido: true          | PASÓ   | 0.4 ms   |
|      |                       |                                                       | '@sindominio.com'     | Inválido: false       | (OK)   |          |
+------+-----------------------+-------------------------------------------------------+-----------------------+-----------------------+--------+----------+
| CP07 | Control de Acceso RBAC| Verificación de jerarquía de roles de usuario         | Roles: ADMIN, COCINERO| ADMIN accede a cocina | PASÓ   | 0.3 ms   |
|      |                       | (Admin > Cocinero > Repartidor > Cliente).            | CLIENTE, REPARTIDOR   | CLIENTE no es admin   | (OK)   |          |
+------+-----------------------+-------------------------------------------------------+-----------------------+-----------------------+--------+----------+
| CP08 | Clientes y Teléfonos  | Validación de teléfonos móviles en Colombia           | '3127894561' (10 dig) | Celular válido: true  | PASÓ   | 0.8 ms   |
|      |                       | (10 dígitos iniciando en 3).                          | '2127894561' (fijo)   | Fijo/Inválido: false  | (OK)   |          |
+------+-----------------------+-------------------------------------------------------+-----------------------+-----------------------+--------+----------+
| CP09 | Seguridad / Web       | Saneamiento de entradas de texto contra ataques de    | '<script>alert(1)</   | Escapado a entidades  | PASÓ   | 0.5 ms   |
|      |                       | Cross-Site Scripting (XSS) e inyección NoSQL.         | script>'              | HTML seguras &lt;&gt; | (OK)   |          |
+------+-----------------------+-------------------------------------------------------+-----------------------+-----------------------+--------+----------+
| CP10 | Inventario Gourmet    | Reserva de insumos de receta (harina 00, mozzarella,  | Receta Margherita:    | Reserva: true         | PASÓ   | 0.7 ms   |
|      |                       | pomodoro) y descuento exacto en gramos de bodega.     | 300g H, 250g M, 200g P| Stock actualizado OK  | (OK)   |          |
+------+-----------------------+-------------------------------------------------------+-----------------------+-----------------------+--------+----------+
| CP11 | Inventario Gourmet    | Control de desabastecimiento: bloqueo de pedidos si   | Solicitud de 999 kg   | Lanza excepción:      | PASÓ   | 0.3 ms   |
|      |                       | la demanda de ingredientes excede el stock real.      | de mozzarella         | "Stock insuficiente"  | (OK)   |          |
+------+-----------------------+-------------------------------------------------------+-----------------------+-----------------------+--------+----------+
```

### 6.2. Análisis de Métricas de Calidad Obtenidas

* **Tasa de Aprobación (Pass Rate):** Se obtuvo un **100.0% de éxito** (11/11 casos aprobados), con **0 defectos críticos** y **0 casos cancelados**.
* **Eficiencia Temporal:** La ejecución completa de la batería de pruebas tomó únicamente **156.71 ms** (promedio inferior a 1 ms por caso de prueba), demostrando la altísima ligereza y velocidad del motor de pruebas nativo de Node.js frente a frameworks más pesados.
* **Cobertura de Riesgos:** Las pruebas protegieron los tres activos más críticos de la pizzería: la exactitud financiera de las cuentas por cobrar, la seguridad contra intrusiones en la base de datos de clientes y la consistencia operativa del inventario de insumos artesanales.

---

## 7. CONCLUSIONES

1. **El Testing como Pilar de Calidad Profesional:** La implementación de pruebas automatizadas trasciende la simple comprobación técnica; constituye el mecanismo de ingeniería más confiable para blindar la solución de software frente a errores humanos y cambios imprevistos en los requerimientos.
2. **Superioridad de las Herramientas Ligeras en Microservicios:** La selección del **Node.js Native Test Runner (`node:test`)** demostró que es posible alcanzar una cobertura de pruebas de alto nivel sin sobrecargar el proyecto con cientos de dependencias externas complejas, logrando tiempos de ejecución inferiores a 200 ms ideales para pipelines de integración continua (CI/CD).
3. **Impacto Positivo en el Proyecto "Bella Italia Popayán":** La suite desarrollada garantiza que el cobro del Impoconsumo (8%), los domicilios zonales en Popayán, las políticas de contraseñas robustas y el inventario de recetas operen con exactitud matemática, ofreciendo a los clientes una experiencia digital confiable, rápida y segura.
4. **Formación Integral del Tecnólogo ADSO:** El desarrollo del taller afianza en la aprendiz Karen Campo la disciplina metodológica necesaria para diseñar, codificar, ejecutar y documentar planes de prueba formales bajo estándares internacionales de la industria del software.

---

## 8. REFERENCIAS BIBLIOGRÁFICAS (NORMAS APA 7MA EDICIÓN)

* Cohn, M. (2009). *Succeeding with Agile: Software Development Using Scrum*. Addison-Wesley Professional.
* Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.). Addison-Wesley Professional.
* Freeman, S., & Pryce, N. (2009). *Growing Object-Oriented Software, Guided by Tests*. Addison-Wesley Professional.
* International Organization for Standardization. (2013). *ISO/IEC/IEEE 29119-1: Software and systems engineering — Software testing — Part 1: Concepts and definitions*. ISO.
* Node.js Foundation. (2024). *Node.js v20.x Documentation: Test runner module (node:test)*. https://nodejs.org/api/test.html
* Open Web Application Security Project - OWASP. (2021). *OWASP Top 10: The Ten Most Critical Web Application Security Risks*. OWASP Foundation. https://owasp.org/Top10/
* Postman Inc. (2024). *Newman: The command-line collection runner for Postman*. Postman Documentation. https://learning.postman.com/docs/collections/using-newman-cli/
* Pressman, R. S., & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach* (9th ed.). McGraw-Hill Education.
* Servicio Nacional de Aprendizaje - SENA. (2026). *Componente Formativo: Las pruebas de software*. Dirección de Formación Profesional.
* Sommerville, I. (2016). *Software Engineering* (10th ed.). Pearson.
