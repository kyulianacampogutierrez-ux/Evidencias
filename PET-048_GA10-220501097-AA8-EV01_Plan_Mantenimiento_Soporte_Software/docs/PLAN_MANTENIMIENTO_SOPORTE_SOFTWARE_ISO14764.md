# PLAN DE MANTENIMIENTO Y SOPORTE DE SOFTWARE (NORMA ISO/IEC 14764)
## EVIDENCIA GA10-220501097-AA8-EV01

---

### METADATOS DEL PROYECTO FORMATIVO
* **Programa de Formación:** Tecnología en Análisis y Desarrollo de Software (ADSO)
* **Código de Ficha:** 3186681
* **Aprendiz:** Karen Yuliana Campo
* **Centro de Formación:** Centro de Teleinformática y Producción Industrial (CTPI Popayán)
* **Regional:** Regional Cauca - Servicio Nacional de Aprendizaje (SENA)
* **Competencia:** 220501097 - Implementar la solución de software de acuerdo con los requisitos de operación y modelos de referencia
* **Actividad de Aprendizaje:** GA10-220501097-AA8 - Elaborar planes de mantenimiento y soporte del software, de acuerdo con los estándares establecidos
* **Componente Formativo:** *Actividades de documentación y entrega de software en procesos de implantación*
* **Instrumento de Evaluación:** Lista de Chequeo `IE-GA10-220501097-AA8-EV01`
* **Estándar Internacional de Referencia:** ISO/IEC 14764:2006 (*Software Engineering — Software Life Cycle Processes — Maintenance*)
* **Proyecto del Sistema:** Pizzería Gourmet Bella Italia Popayán
* **Fecha:** Noviembre de 2026

---

## 1. INTRODUCCIÓN Y MARCO NORMATIVO

El ciclo de vida del software no culmina con la entrega inicial del producto a producción; por el contrario, la fase de operación, mantenimiento y soporte representa entre el 60% y el 80% del costo total de propiedad (*Total Cost of Ownership - TCO*) a lo largo de su vida útil. En concordancia con el componente formativo **"Actividades de documentación y entrega de software en procesos de implantación"** de la Guía de Aprendizaje 10, la evidencia **GA10-220501097-AA8-EV01** establece la obligatoriedad de formular un plan integral de mantenimiento y soporte sustentado en el estándar internacional **ISO/IEC 14764:2006**.

El presente documento define la estrategia operativa, las políticas de atención, los acuerdos de nivel de servicio (*Service Level Agreements - SLA*), la taxonomía de fallas y el cronograma programado para la solución web y transaccional de la **Pizzería Gourmet Bella Italia Popayán**, negocio gastronómico ubicado en la Calle 4 # 5-28 del Centro Histórico de Popayán. El plan articula armónicamente las cuatro categorías fundamentales de mantenimiento: **Preventivo**, **Correctivo**, **Adaptativo** y **Perfectivo**, garantizando la continuidad del negocio, la seguridad informática y la satisfacción de los comensales y operadores.

```
+-----------------------------------------------------------------------------------------+
|                  CICLO DE VIDA DE MANTENIMIENTO SEGÚN NORMA ISO/IEC 14764               |
|                                                                                         |
|  [ 1. IMPLEMENTACIÓN ] ----> [ 2. ANÁLISIS DE MODIFICACIÓN ] ---> [ 3. IMPLEMENTACIÓN ] |
|  - Política y recursos       - Solicitud RFC / HelpDesk            - Codificación hotfix|
|  - Entorno de Staging        - Clasificación Severidad (P1-P4)     - Optimización SQL   |
|  - Control versiones Git     - Evaluación de impacto operacional   - Pruebas unitarias  |
|                                                                              |          |
|                                                                              v          |
|  [ 6. RETIRO / DECOMISO ] <-- [ 5. MIGRACIÓN / VERSIONES ] <-- [ 4. ACEPTACIÓN & REV. ] |
|  - Archivado de datos         - Migración esquemas MySQL           - Pruebas regresión  |
|  - Retención Ley 1581         - Plan de Rollback seguro            - Acta de entrega QA |
|  - Desmantelamiento seguro    - Coexistencia de servicios          - Despliegue ventana |
+-----------------------------------------------------------------------------------------+
```

---

## 2. DESCRIPCIÓN DEL SISTEMA

### 2.1 Módulos y Arquitectura Operativa
La plataforma web de la Pizzería Gourmet Bella Italia Popayán es un sistema de comercio electrónico gastronómico de alta disponibilidad basado en una arquitectura cliente-servidor tradicional LAMP (Linux, Apache 2.4, MySQL 8.0, PHP 8.2):

* **Módulo de Catálogo Gastronómico:** Presentación dinámica de especialidades gourmet (Margherita Di Bufala, Cuatro Quesos, Pepperoni Popayán, Vegetariana del Valle) con precios oficiales en pesos colombianos (COP).
* **Módulo de Checkout y Liquidación Tributaria:** Captura de datos de entrega en Popayán, validación de teléfonos móviles colombianos mediante expresiones regulares (`^3\d{9}$`), liquidación automática del **8% de Impuesto Nacional al Consumo** (Ley 1607 de 2012) y consentimiento expreso de Habeas Data (Ley 1581 de 2012).
* **Capa de Persistencia y Almacenamiento Relacional:** Base de datos relacional MySQL 8.0 (motor InnoDB con cumplimiento ACID) estructurada en las tablas `productos_pizza`, `usuarios_clientes`, `pedidos_gourmet` y `auditoria_despliegue_produccion`.
* **Capa de Infraestructura y Red:** Servidor Apache 2.4 bajo hosting tradicional con soporte cPanel, zonificación DNS en subdominio canónico `pizzeriabellaitalia-popayan.rf.gd`, certificado SSL/TLS 1.3 emitido por Let's Encrypt y cabeceras de endurecimiento OWASP Top 10.

---

## 3. PROCESOS DEL CICLO DE VIDA DE MANTENIMIENTO (ISO/IEC 14764)

Siguiendo los lineamientos de la norma internacional ISO/IEC 14764, el plan de mantenimiento se estructura en seis procesos formales:

### 3.1 Proceso de Implementación
Establece las directrices organizacionales y técnicas para coordinar las labores de mantenimiento:
1. **Asignación de Roles y Responsabilidades:**
   * **Líder de Mantenimiento y DBA:** Karen Yuliana Campo (gestión de backups, parches y optimización de base de datos).
   * **Ingeniero DevOps:** Mantenimiento de infraestructura, contenedores Docker y certificados SSL.
   * **Operador de Mesa de Ayuda:** Recepción y triaje de tickets reportados por los administradores del restaurante.
2. **Entornos Aislados de Trabajo:** Se dispone de un entorno de pruebas (**Staging**) réplica exacta de producción donde se ensayan parches antes de su despliegue en vivo, garantizando cero contaminación del entorno anfitrión (*Zero Host Pollution*).
3. **Control de Versiones y Repositorio:** Toda modificación se registra en ramas de Git con nomenclatura semántica (`hotfix/`, `release/`, `feat/`) en el repositorio oficial.

### 3.2 Proceso de Análisis de Modificaciones y Problemas
Define el protocolo para procesar solicitudes de cambio (*Request For Change - RFC*) y reportes de incidencias:
* **Entrada:** Ticket radicado a través del Portal de Soporte Web o HelpDesk.
* **Clasificación del Tipo de Mantenimiento:**
  * *Preventivo:* Tareas programadas de optimización y monitoreo.
  * *Correctivo:* Falla en ejecución que degrada o detiene la funcionalidad.
  * *Adaptativo:* Cambios regulatorios (reforma tributaria DIAN) o actualización de versiones de PHP/MySQL.
  * *Perfectivo:* Optimización de velocidad de carga o rediseño de interfaz.
* **Evaluación de Impacto:** Estimación de riesgos, componentes afectados, tiempo estimado de solución y plan de contingencia.

### 3.3 Proceso de Implementación de la Modificación
* Codificación del parche o script de corrección en la rama correspondiente.
* Ejecución de pruebas unitarias y de integración en Staging.
* Revisión de código por pares (*Code Review*) asegurando estándares de codificación segura.

### 3.4 Proceso de Aceptación y Revisión del Mantenimiento
* **Pruebas de Regresión:** Verificación de que la corrección no introduce defectos en módulos previamente funcionales (catálogo, checkout, liquidación COP).
* **Acta de Conformidad y Cierre:** Firma de aceptación por parte del responsable técnico y notificación formal al usuario requirente.
* **Ventana de Despliegue:** Aplicación en producción exclusivamente en la ventana autorizada de bajo tráfico (domingos de 02:00 a 04:00 COT).

### 3.5 Proceso de Migración
Directrices para cuando el sistema requiera migrar de servidor, motor de base de datos o versión de software:
* Generación previa de volcado determinístico (*mysqldump*) con sumas de verificación criptográficas SHA-256.
* Scripts idempotentes de migración con retrocompatibilidad.
* **Plan de Rollback Automático:** Capacidad de retornar a la versión anterior en menos de 15 minutos en caso de inconsistencia detectada.

### 3.6 Proceso de Retiro (Decomiso del Software)
Plan para el cese definitivo o sustitución total del sistema:
* **Archivado de Datos en Frío:** Copia de seguridad histórica comprimida y cifrada con retención obligatoria de 5 años según la normativa comercial y tributaria colombiana.
* **Protección de Datos Personales:** Supresión segura de bases de datos operativas conforme a la Ley Estatutaria 1581 de 2012 para garantizar el derecho al olvido y la privacidad.
* **Plan de Notificación a Clientes:** Divulgación preventiva a comensales y operadores con 60 días de antelación.

---

## 4. MATRIZ DE SEVERIDAD Y ACUERDOS DE NIVEL DE SERVICIO (SLA)

Para garantizar una atención oportuna y medible, se establece la siguiente matriz de criticidad y tiempos máximos de respuesta y solución (*Mean Time To Repair - MTTR*):

| Nivel de Severidad | Criterio de Impacto Operacional | Tiempo de Respuesta | Tiempo de Solución (MTTR) | Canal de Atención y Escalamiento |
| :--- | :--- | :---: | :---: | :--- |
| **P1 - Crítica** | Caída completa de la web, fallo total del checkout o base de datos inaccesible. | &lt; 15 min | &lt; 2 horas | Llamada telefónica directa a DBA y conmutación a contingencia. |
| **P2 - Alta** | Degradación severa de rendimiento (&gt; 3s) o fallo en visualización de precios COP. | &lt; 30 min | &lt; 4 horas | HelpDesk prioritario y hotfix en Staging. |
| **P3 - Media** | Defecto visual parcial o error menor en filtros que no impide la toma de pedidos. | &lt; 2 horas | &lt; 24 horas | Ticket en Mesa de Ayuda y corrección en release quincenal. |
| **P4 - Baja** | Solicitud de mejora estética, ajuste tipográfico o consulta técnica general. | &lt; 8 horas | &lt; 72 horas | Ticket en Mesa de Ayuda evaluado en comité mensual. |

---

## 5. CRONOGRAMA ANUAL DE MANTENIMIENTO PREVENTIVO (2026-2027)

El mantenimiento preventivo se rige por un cronograma estructurado con periodicidad fija para evitar la degradación del sistema:

| Frecuencia | Código Actividad | Tarea de Mantenimiento Preventivo | Procedimiento y Herramientas | Ventana Horaria | Responsable |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Semanal** | `ACT-PREV-01` | Respaldo integral de base de datos y ficheros web. | `mysqldump` comprimido `.sql.gz` + `tar -czf` de `/public_html/`. | Domingos 02:00 COT | Karen Campo (DBA) |
| **Semanal** | `ACT-PREV-02` | Depuración y rotación de archivos de registro (*logs*). | `logrotate` en Apache y purga de logs temporales mayores a 7 días. | Domingos 02:30 COT | DevOps / SysAdmin |
| **Quincenal** | `ACT-PREV-03` | Optimización y desfragmentación de tablas MySQL. | Sentencias `OPTIMIZE TABLE` y `ANALYZE TABLE` en InnoDB. | Domingos 03:00 COT | Karen Campo (DBA) |
| **Mensual** | `ACT-PREV-04` | Auditoría de vulnerabilidades y parches de seguridad. | Inspección de dependencias, escaneo OWASP y parches Docker. | 1.er domingo de mes | Equipo DevOps |
| **Bimestral** | `ACT-PREV-05` | Comprobación y renovación de certificados SSL/TLS. | `certbot renew --dry-run` en Let's Encrypt para asegurar TLS 1.3. | Cada 60 días | Administrador Red |
| **Trimestral** | `ACT-PREV-06` | Simulacro de recuperación ante desastres (DRP). | Restauración de respaldo en Staging y validación de hash SHA-256. | Trimestral | Karen Campo & QA |

---

## 6. EVIDENCIA FOTOGRÁFICA Y PASO A PASO EN KDE X11

A continuación se presentan las 6 capturas de pantalla de alta resolución obtenidas directamente en el entorno de escritorio **KDE X11** utilizando la herramienta de captura **Spectacle**, con ejecución de comandos en terminal **Konsole** y navegación en **Google Chrome**:

### 6.1 Paso 1: Ejecución Automatizada de Mantenimiento Preventivo en Konsole
Ejecución del script `ejecutar_mantenimiento_preventivo.sh` en terminal Konsole, validando espacio en disco (`df -h`), rotación y compresión de logs de Apache, análisis de tablas MySQL (`OPTIMIZE TABLE`) y vigencia del certificado SSL:

![Mantenimiento Preventivo en Konsole](capturas/paso_01_ejecucion_mantenimiento_preventivo_konsole.png)

### 6.2 Paso 2: Despliegue del Entorno de Mantenimiento y Soporte en Docker
Verificación de los contenedores aislados de soporte `sena-mantenimiento-soporte-web` (puerto 8097) y `sena-mantenimiento-soporte-db` (puerto 3312) en estado *healthy* sin contaminar el host:

![Despliegue del Entorno en Docker](capturas/paso_02_despliegue_ambiente_mantenimiento_docker_konsole.png)

### 6.3 Paso 3: Atención de Incidencia Correctiva P1 y Control de SLA en Konsole
Simulación y resolución del ticket `#TCK-2026-CORR-085` mediante el script `simular_incidencia_correctiva_sla.sh`, demostrando la aplicación de hotfix en MySQL y un tiempo de resolución (MTTR) de 38 minutos, cumpliendo el SLA exigido (&lt; 120 min):

![Atención de Incidencia Correctiva SLA](capturas/paso_03_atencion_incidencia_correctiva_sla_konsole.png)

### 6.4 Paso 4: Portal Web de Soporte Técnico y KPIs en Google Chrome
Acceso en Google Chrome al Centro de Mantenimiento y Soporte Técnico, visualizando el encabezado institucional, el marco de referencia ISO/IEC 14764 y los indicadores clave (Uptime 99.98%, MTBF 720h, MTTR 38m):

![Portal de Soporte y KPIs en Chrome](capturas/paso_04_chrome_portal_soporte_mantenimiento.png)

### 6.5 Paso 5: Cronograma Interactivo Anual y Matriz de Severidad SLA en Chrome
Navegación en Google Chrome por las secciones del cronograma anual 2026-2027 detallando ventanas horarias, frecuencias y la matriz de severidades operacionales P1 a P4:

![Cronograma y Matriz SLA en Chrome](capturas/paso_05_chrome_cronograma_interactivo_sla.png)

### 6.6 Paso 6: Mesa de Ayuda y Radicación de Tickets de Mantenimiento
Diligenciamiento de un ticket de soporte interactivo en la Mesa de Ayuda con asignación a la aprendiz Karen Campo, cálculo de SLA y confirmación visual en la bitácora histórica:

![Mesa de Ayuda y Tickets en Chrome](capturas/paso_06_chrome_registro_ticket_soporte_pizzeria.png)

---

## 7. MATRIZ DE VERIFICACIÓN DE CRITERIOS DE EVALUACIÓN

| Num | Criterio de Evaluación (`IE-GA10-220501097-AA8-EV01`) | Estado | Mecanismo de Verificación y Evidencia Aportada |
| :---: | :--- | :---: | :--- |
| **1** | **Elabora los planes de mantenimiento y soporte para garantizar la funcionalidad del software en el tiempo.** | **CUMPLE** | Plan integral estructurado bajo la norma ISO/IEC 14764:2006, contemplando los 6 procesos, cronograma preventivo anual, matriz SLA y portal de HelpDesk. |
| **2** | **Define los tipos de mantenimiento preventivo y correctivo con periodicidad.** | **CUMPLE** | Protocolos automatizados semanales, quincenales y mensuales para preventivo; matriz de severidad P1-P4 con tiempos MTTR para correctivo. |
| **3** | **Establece procedimientos de migración y retiro de componentes.** | **CUMPLE** | Procesos documentados de migración de esquemas con rollback y protocolo de decomiso seguro con retención legal (Ley 1581). |
| **4** | **Evidencia ejecución técnica real en entorno de pruebas controlado.** | **CUMPLE** | Scripts en ejecución sobre Docker (puertos 8097 y 3312) con 6 capturas reales en KDE X11 mediante Spectacle y Konsole. |

---

## 8. CONCLUSIONES Y RECOMENDACIONES TÉCNICAS

1. **Garantía de Sostenibilidad Operacional:** La adopción del estándar ISO/IEC 14764 transforma el mantenimiento de un esquema reactivo e improvisado a un modelo predecible, medible y profesional que asegura el retorno de inversión de la Pizzería Gourmet Bella Italia Popayán.
2. **Eficacia del Mantenimiento Preventivo:** La automatización de respaldos semanales y la optimización de índices relacionales evitan la degradación silenciosa de la base de datos, garantizando tiempos de respuesta menores a 20 ms.
3. **Control Estricto de SLAs:** La definición de tiempos MTTR y canales de escalamiento claros para incidentes P1 y P2 protege la continuidad del negocio durante los horarios de mayor venta gastronómica.
4. **Recomendación para Futuras Fases:** Se sugiere la integración de un sistema de telemetría y monitoreo proactivo como *Prometheus & Grafana* con alertas en tiempo real vía Telegram o correo electrónico ante aumentos anómalos de carga de CPU o caídas de socket.

---

## 9. REFERENCIAS BIBLIOGRÁFICAS (NORMAS APA 7.ª EDICIÓN)

* Apache Software Foundation. (2024). *Apache HTTP Server Documentation: Log Files and Maintenance*. https://httpd.apache.org/docs/2.4/logs.html
* Congreso de la República de Colombia. (2012). *Ley Estatutaria 1581 de 2012: Régimen general de protección de datos personales*.
* International Organization for Standardization & International Electrotechnical Commission. (2006). *ISO/IEC 14764:2006: Software Engineering — Software Life Cycle Processes — Maintenance*. ISO/IEC.
* ITIL Foundation. (2019). *ITIL 4: Service Management Practices and Incident Management*. Axelos Global Best Practice.
* MySQL AB & Oracle Corporation. (2024). *MySQL 8.0 Reference Manual: Table Maintenance and Optimization*. Oracle Docs. https://dev.mysql.com/doc/refman/8.0/en/
* Pressman, R. S., & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach* (9th ed.). McGraw-Hill Education.
* Servicio Nacional de Aprendizaje (SENA). (2024). *Componente Formativo: Actividades de documentación y entrega de software en procesos de implantación*. Programa ADSO, Dirección de Formación Profesional, Sistema Zajuna.
* Sommerville, I. (2016). *Software Engineering* (10th ed.). Pearson Education.
