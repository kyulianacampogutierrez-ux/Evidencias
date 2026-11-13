# PLAN MAESTRO DE PRUEBAS DE SOFTWARE (ESTÁNDAR IEEE 829 / ISO/IEC/IEEE 29119)
## PROYECTO FORMATIVO: PIZZERÍA GOURMET BELLA ITALIA POPAYÁN
### EVIDENCIA: GA9-220501096-AA1-EV02 - REALIZA PLAN PRUEBAS DE SOFTWARE

**Programa de Formación:** Tecnología en Análisis y Desarrollo de Software (ADSO) - Modalidad Virtual  
**Ficha de Caracterización:** 3186681  
**Competencia:** 220501096 - Desarrollar la solución de software de acuerdo con el diseño y metodologías de desarrollo  
**Actividad de Aprendizaje:** GA9-220501096-AA1 - Realizar plan de pruebas, según el proyecto  
**Aprendiz:** Karen Yuliana Campo  
**Centro de Formación:** Centro de Teleinformática y Producción Industrial (CTPI) - Popayán, Regional Cauca  
**Fecha de Elaboración:** Noviembre 2026  

---

## 1. INTRODUCCIÓN

El desarrollo de soluciones de software de alto impacto comercial y transaccional, como la plataforma de comercio electrónico y gestión operativa de la **Pizzería Gourmet Bella Italia Popayán**, requiere de mecanismos formales que aseguren que cada módulo cumpla rigurosamente con los requerimientos de los usuarios y opere de forma confiable, segura y eficiente. Las pruebas de software no representan un suceso aislado o improvisado al término del proyecto, sino un proceso de ingeniería planificado, estructurado y medible.

El presente **Plan Maestro de Pruebas de Software (Master Test Plan)** ha sido formulado bajo las directrices internacionales del estándar **IEEE 829-2008** (*Standard for Software and System Test Documentation*) y la norma **ISO/IEC/IEEE 29119** (*Software Testing*). Este documento define el alcance, los objetivos de calidad, los entornos de ejecución, los criterios de aceptación, las metodologías, los artefactos de registro y el cronograma para la verificación exhaustiva de los módulos backend, frontend web y aplicación móvil del proyecto formativo.

---

## 2. ANÁLISIS DE REQUERIMIENTOS DEL SISTEMA

La solución de software de la pizzería artesanal se concibe bajo una arquitectura de microservicios desacoplada en tres capas principales:
* **Capa Backend:** APIs RESTful desarrolladas en **Go (Fiber v2)** y **Node.js**, orquestadas en contenedores Docker y respaldadas por **MongoDB** (base de datos NoSQL para catálogos y comandas) y **MariaDB** (gestión relacional de transacciones contables).
* **Capa Frontend Web:** Aplicación de comercio electrónico desarrollada en **React**, **Vite** y **Tailwind CSS**.
* **Capa Móvil:** Aplicación híbrida de despacho y pedidos desarrollada en **React Native** para Android 14+ (API 34).

```
                                          PIRÁMIDE DE PRUEBAS DEL PROYECTO
                                                         ▲
                                                        / \
                                                       /   \
                                                      / E2E \   ◄── Pruebas de Sistema y Móvil (React Native)
                                                     /───────\
                                                    / Integr- \  ◄── Pruebas de API REST (Go Fiber + MongoDB)
                                                   /  ación    \
                                                  /─────────────\
                                                 /   Unitarias   \ ◄── Pruebas de Lógica de Negocio e Impuestos
                                                /─────────────────\
```

---

## 3. IDENTIFICACIÓN DE FUNCIONALIDADES EXISTENTES VS NUEVAS FUNCIONALIDADES A PROBAR

Para optimizar el esfuerzo de testing y enfocar los recursos en las áreas de mayor riesgo, se efectúa la segregación técnica entre las funcionalidades preexistentes y las nuevas características implementadas:

### 3.1. Funcionalidades Existentes (Sujetas a Pruebas de Regresión)
1. **Módulo de Autenticación Básica:** Registro de usuarios, inicio de sesión mediante credenciales de correo y contraseña, y almacenamiento de tokens de sesión.
2. **Módulo Catálogo de Productos:** Consulta pública de pizzas artesanales, bebidas y postres con filtrado por categorías.
3. **Módulo Carrito de Compras Básico:** Adición de productos, selección de cantidades y cálculo básico de suma de precios.

### 3.2. Funcionalidades Nuevas a Probar (Foco Primario del Plan)
1. **Liquidación Tributaria Automatizada (Impoconsumo 8%):** Cálculo obligatorio del Impuesto Nacional al Consumo para restaurantes en Colombia (Estatuto Tributario Art. 512-1) sobre el subtotal neto de cada pedido.
2. **Tarifas Zonales de Domicilio en Popayán:** Regla de cálculo dinámico de envío según la comuna de destino (Centro: $3.000, Norte: $4.500, Sur/Occidente: $5.000, Rural: $8.000 COP) y exoneración de envío gratuito para pedidos iguales o superiores a $60.000 COP.
3. **Motor de Cupones y Promociones Gourmet:** Aplicación de descuentos porcentuales (ej. `BELLAITALIA10` para 10% OFF) previa liquidación de impuestos.
4. **Control de Acceso Basado en Roles (RBAC):** Jerarquía de privilegios entre `ADMIN` (gerente), `COCINERO` (pantalla KDS de cocina), `REPARTIDOR` (app móvil) y `CLIENTE`.
5. **Saneamiento Web y Seguridad de Entradas:** Mecanismos de escape y validación contra ataques de inyección NoSQL en MongoDB y Cross-Site Scripting (XSS).
6. **Módulo KDS de Cocina y Reserva Transaccional de Inventario:** Descuento automático en gramos de insumos de bodega (harina 00, mozzarella di bufala, pomodoro San Marzano) y bloqueo transaccional si hay desabastecimiento.

---

## 4. ESTRATEGIA Y ENFOQUE DE PRUEBAS DE SOFTWARE

La estrategia de pruebas adopta un enfoque multinivel guiado por la calidad en el diseño:

```
+-----------------------------------+-----------------------------------------------------+----------------------------------------------------+
| NIVEL / TIPO DE PRUEBA            | OBJETIVO DE LA EVALUACIÓN                           | HERRAMIENTAS Y RUNNERS APLICADOS                   |
+-----------------------------------+-----------------------------------------------------+----------------------------------------------------+
| 1. Pruebas Unitarias (Lógica)     | Validar funciones puras de cálculo matemático,      | Node.js Native Test Runner (node:test) y           |
|                                   | descuentos, validaciones sintácticas y excepciones. | Biblioteca de Aserciones node:assert/strict.       |
+-----------------------------------+-----------------------------------------------------+----------------------------------------------------+
| 2. Pruebas de Integración (APIs)  | Verificar contratos JSON, códigos HTTP (200, 201,   | Supertest, Postman v2.1 y ejecutor CLI Newman      |
|                                   | 400, 401, 404) y persistencia en MongoDB.           | en contenedor Docker aislado.                      |
+-----------------------------------+-----------------------------------------------------+----------------------------------------------------+
| 3. Pruebas de Seguridad (OWASP)   | Evaluar fortaleza de contraseñas, expiración JWT    | Scripts de inyección de payloads y análisis        |
|                                   | y saneamiento de inputs contra inyecciones NoSQL.   | estático con validadores de expresiones regulares. |
+-----------------------------------+-----------------------------------------------------+----------------------------------------------------+
| 4. Pruebas de Rendimiento y Carga | Medir tiempos de respuesta (< 200 ms) y estabilidad | Grafana k6 y benchmarks nativos simulando          |
|                                   | bajo concurrencia en horas pico en Popayán.         | picos de pedidos en fin de semana.                 |
+-----------------------------------+-----------------------------------------------------+----------------------------------------------------+
| 5. Pruebas de Regresión           | Ejecución automática desatendida en cada commit     | Docker runner integrado en scripts de despliegue   |
|                                   | para certificar que el código previo no se rompa.   | continuo (docker-test.sh).                         |
+-----------------------------------+-----------------------------------------------------+----------------------------------------------------+
```

### Gráfico 1: Ciclo de Vida del Proceso de Pruebas (IEEE 829)
![Ciclo de Vida del Proceso de Pruebas](file:///home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-035_GA9-220501096-AA1-EV02_Plan_Pruebas_Software/diagramas/ciclo_vida_pruebas_software_ieee829.png)
*Figura 1: Fases formales del proceso de pruebas bajo el estándar IEEE 829 y gobernanza de artefactos de registro.*

---

## 5. CRITERIOS DE INICIO, SUSPENSIÓN, REANUDACIÓN Y ACEPTACIÓN (SALIDA)

Para garantizar la objetividad del proceso, se establecen criterios formales de compuerta (**Quality Gates**):

### 5.1. Criterios de Inicio (Entry Criteria)
* Disponibilidad del código fuente compilado y libre de errores sintácticos.
* Contenedores Docker de base de datos MongoDB y backend en estado `healthy`.
* Matriz de Trazabilidad de Requisitos (RTM) aprobada por el líder de QA.

### 5.2. Criterios de Suspensión (Suspension Criteria)
* Identificación de un defecto de severidad **Bloqueante** que impida la ejecución de más del 30% de los casos de prueba planeados.
* Inestabilidad del entorno de base de datos o fallos de conectividad en el clúster de prueba.

### 5.3. Criterios de Reanudación (Resumption Criteria)
* Despliegue de un parche correctivo (**bug fix**) verificado en un entorno de pruebas unitarias.
* Confirmación de la restauración del entorno por el equipo de DevOps.

### 5.4. Criterios de Aceptación / Salida (Exit Criteria)
* **100% de casos de prueba críticos y de alta prioridad ejecutados.**
* **Tasa de aprobación mínima del 98% en pruebas funcionales (100% en lógica contable).**
* **Cero (0) defectos abiertos clasificados con severidad Bloqueante o Alta.**
* Todos los defectos menores documentados con su respectivo plan de mitigación.

---

## 6. IDENTIFICACIÓN DE ENTORNOS DE TRABAJO (SOFTWARE Y HARDWARE)

Las pruebas se ejecutarán en ambientes virtualizados y reproducibles mediante **Docker Compose**:

### Gráfico 2: Arquitectura de Ambientes de Prueba Orquestados
![Arquitectura de Ambientes de Prueba](file:///home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-035_GA9-220501096-AA1-EV02_Plan_Pruebas_Software/diagramas/arquitectura_ambientes_pruebas_docker.png)
*Figura 2: Ecosistema dockerizado de pruebas de la Pizzería Bella Italia Popayán.*

```
+------------------------+------------------------------------+-----------------------------------------------------+
| COMPONENTE DE ENTORNO  | ESPECIFICACIÓN TÉCNICA             | CONFIGURACIÓN Y SERVICIO DOCKER                     |
+------------------------+------------------------------------+-----------------------------------------------------+
| Sistema Operativo Base | Linux Ubuntu 24.04 LTS / Kernel 6.8| Entorno de ejecución host del desarrollador         |
+------------------------+------------------------------------+-----------------------------------------------------+
| Motor de Contenedores  | Docker Engine 28.0.1 / Compose 3.8 | Red aislada en puente: `sena-net`                   |
+------------------------+------------------------------------+-----------------------------------------------------+
| Contenedor Test Runner | Node.js v20.20.2 LTS Alpine        | Servicio `test-runner`, volumen montado `/sena/CDE` |
+------------------------+------------------------------------+-----------------------------------------------------+
| Backend Microservicio  | Golang 1.22 Alpine (Fiber v2)      | Servicio `backend-go` (Puerto 8085)                 |
+------------------------+------------------------------------+-----------------------------------------------------+
| Base de Datos NoSQL    | MongoDB Community Server 7.0       | Servicio `mongodb` (Puerto 27017, healthcheck)      |
+------------------------+------------------------------------+-----------------------------------------------------+
| Cliente Frontend Web   | Vite 5 + React 18 + Tailwind CSS   | Servicio `frontend-vite` (Puerto 5173)              |
+------------------------+------------------------------------+-----------------------------------------------------+
| Cliente Móvil          | Android 14+ (API Level 34)         | Emulador AVD Pixel 7 y APK Release compilada        |
+------------------------+------------------------------------+-----------------------------------------------------+
```

---

## 7. METODOLOGÍA, PROCEDIMIENTOS, CRONOGRAMA Y PLANIFICACIÓN

El plan se estructura en **cuatro semanas de trabajo**, sincronizadas con los sprints ágiles de desarrollo:

### Gráfico 3: Cronograma de Ejecución del Plan de Pruebas (Gantt)
![Cronograma Plan de Pruebas](file:///home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-035_GA9-220501096-AA1-EV02_Plan_Pruebas_Software/diagramas/cronograma_plan_pruebas_gantt.png)
*Figura 3: Cronograma temporal de actividades del plan de pruebas por semanas.*

```
+-----------+-------------------------------------------------------+-----------------------------+-------------------------+
| SEMANA    | FASE Y ACTIVIDAD PRINCIPAL                            | ENTREGABLE INTERMEDIO       | RESPONSABLE             |
+-----------+-------------------------------------------------------+-----------------------------+-------------------------+
| Semana 1  | Análisis de requerimientos y diseño de matriz RTM.    | Matriz RTM y Casos CP-01..04| Karen Campo (QA Lead)   |
+-----------+-------------------------------------------------------+-----------------------------+-------------------------+
| Semana 2  | Configuración de entornos Docker y pruebas unitarias. | Scripts TDD y mocks en test | Karen Campo (Dev/Tester)|
+-----------+-------------------------------------------------------+-----------------------------+-------------------------+
| Semana 3  | Pruebas de integración de APIs REST y seguridad RBAC. | Colección Newman y Bug Logs | Karen Campo (QA Tester) |
+-----------+-------------------------------------------------------+-----------------------------+-------------------------+
| Semana 4  | Pruebas de carga, verificación de fixes y cierre SQA. | Informe Final y Aprobación  | Karen Campo / Evaluador |
+-----------+-------------------------------------------------------+-----------------------------+-------------------------+
```

---

## 8. DISEÑO DE ARTEFACTOS E INSTRUMENTOS PARA EL REGISTRO DE PRUEBAS

En cumplimiento riguroso de la recomendación de la Guía 9 (*"Entregar el diseño de los artefactos o instrumentos para llevar el registro de las pruebas"*), el proyecto cuenta con tres formatos estandarizados formalmente construidos en el repositorio:

1. **Especificación Formal de Caso de Prueba (IEEE 829 Test Case Specification):** Documento detallado en `plantillas/plantilla_caso_prueba_ieee829.md` que incluye identificador único, requerimiento asociado, precondiciones, pasos detallados, datos de entrada en JSON y resultados esperados.
2. **Formato de Registro y Seguimiento de Incidencias (Bug / Defect Tracking Report):** Documento en `plantillas/plantilla_reporte_defectos_bugs.md` con clasificación de severidad (Bloqueante, Alta, Media, Baja), prioridad, pasos exactos para reproducir el fallo, logs y ciclo de vida del defecto.
3. **Matriz de Trazabilidad de Requisitos (Requirements Traceability Matrix - RTM):** Documento en `plantillas/matriz_trazabilidad_requisitos_rtm.md` que mapea cada Requisito Funcional (RF-01 a RF-12) y Requisito No Funcional (RNF-01 y RNF-02) con sus respectivas historias de usuario y casos de prueba, garantizando una **cobertura de pruebas del 100%**.

---

## 9. SELECCIÓN DE HERRAMIENTAS Y UTILIDADES DE TESTING

Para materializar las pruebas planificadas, se seleccionó el siguiente conjunto de herramientas de código abierto e industriales:
* **Node.js Native Test Runner (`node:test`) & `node:assert/strict`:** Motor de pruebas unitarias ultrarrápido nativo en Node.js 20 LTS, sin sobrecostos de dependencias externas.
* **Newman / Postman:** Automatización por línea de comandos para la ejecución desatendida de peticiones a endpoints RESTful en pipelines CI/CD.
* **Supertest:** Biblioteca HTTP para pruebas de integración de microservicios.
* **Docker y Docker Compose:** Plataforma de virtualización para aislar los entornos de prueba de la máquina host.

---

## 10. GESTIÓN DE RIESGOS Y PLANES DE CONTINGENCIA

```
+-----------------------------------+----------------+-------------+---------------------------------------------------+
| RIESGO IDENTIFICADO               | PROBABILIDAD   | IMPACTO     | PLAN DE MITIGACIÓN Y CONTINGENCIA                 |
+-----------------------------------+----------------+-------------+---------------------------------------------------+
| R01: Retraso en la estabilización | Media          | Alto        | Implementación de mocks tempranos de endpoints    |
| de endpoints del backend en Go.   |                |             | para no bloquear las pruebas unitarias del front. |
+-----------------------------------+----------------+-------------+---------------------------------------------------+
| R02: Datos de prueba corruptos o  | Baja           | Alto        | Scripts de semillas (**seeders**) automáticos que |
| desincronizados en MongoDB.       |                |             | restablecen la base de datos antes de cada suite. |
+-----------------------------------+----------------+-------------+---------------------------------------------------+
| R03: Falso positivo por latencia  | Media          | Medio       | Configuración de timeouts elásticos en peticiones |
| de red en pruebas de integración. |                |             | HTTP y reintentos automáticos controlados.        |
+-----------------------------------+----------------+-------------+---------------------------------------------------+
| R04: Cuello de botella en pruebas | Baja           | Medio       | Ejecución nocturna desatendida y monitoreo de     |
| de carga por recursos del host.   |                |             | consumo de CPU mediante Docker stats.             |
+-----------------------------------+----------------+-------------+---------------------------------------------------+
```

---

## 11. CONCLUSIONES

1. **Cumplimiento Integral de Estándares Internacionales:** La estructuración del plan de pruebas bajo los lineamientos **IEEE 829** e **ISO/IEC/IEEE 29119** aporta a la solución "Pizzería Gourmet Bella Italia Popayán" un marco de calidad riguroso y sistemático, eliminando la improvisación en el proceso de verificación.
2. **Control Efectivo del Alcance y Trazabilidad:** La implementación de la Matriz de Trazabilidad de Requisitos (RTM) asegura que el 100% de las historias de usuario críticas (facturación, impuestos, despachos y seguridad) cuenten con casos de prueba diseñados y ejecutables.
3. **Optimización con Ambientes Dockerizados:** El uso de contenedores Docker Compose permite reproducir fielmente las condiciones del entorno de producción, garantizando pruebas de integración independientes, repetibles y libres de efectos secundarios en el sistema operativo del desarrollador.
4. **Valor Formativo para el Tecnólogo ADSO:** Este plan de pruebas consolida en la aprendiz Karen Campo la visión estratégica de un ingeniero de calidad de software (**QA Engineer**), capaz de anticipar riesgos, coordinar cronogramas y asegurar la excelencia técnica en productos de software reales.

---

## 12. REFERENCIAS BIBLIOGRÁFICAS (NORMAS APA 7MA EDICIÓN)

* IEEE Computer Society. (2008). *IEEE Standard for Software and System Test Documentation* (IEEE Std 829-2008). Institute of Electrical and Electronics Engineers.
* International Organization for Standardization. (2013). *ISO/IEC/IEEE 29119-1: Software and systems engineering — Software testing — Part 1: Concepts and definitions*. ISO.
* International Organization for Standardization. (2013). *ISO/IEC/IEEE 29119-2: Software and systems engineering — Software testing — Part 2: Test processes*. ISO.
* International Organization for Standardization. (2013). *ISO/IEC/IEEE 29119-3: Software and systems engineering — Software testing — Part 3: Test documentation*. ISO.
* Pressman, R. S., & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach* (9th ed.). McGraw-Hill Education.
* Servicio Nacional de Aprendizaje - SENA. (2026). *Componente Formativo: Las pruebas de software*. Dirección de Formación Profesional.
* Sommerville, I. (2016). *Software Engineering* (10th ed.). Pearson Education.
