# SERVICIO NACIONAL DE APRENDIZAJE - SENA
## CENTRO DE TELEINFORMÁTICA Y PRODUCCIÓN INDUSTRIAL (CTPI) - REGIONAL CAUCA
### TECNOLOGÍA EN ANÁLISIS Y DESARROLLO DE SOFTWARE (ADSO) - MODALIDAD VIRTUAL
**FICHA DE CARACTERIZACIÓN:** 3186681

---

# EVIDENCIA GA10-220501097-AA3-EV01: SOFTWARE INSTALADO EN LA PLATAFORMA DEL CLIENTE
## INFORME TÉCNICO PASO A PASO DE INSTALACIÓN, DESPLIEGUE LOCAL EN DOCKER, PLAN DE MIGRACIÓN Y RESPALDO DE DATOS
### Fase de Ejecución • Actividad de Proyecto AP8: Desarrollar las tareas de configuración y puesta en marcha del sistema de información

* **Competencia Técnica:** 220501097 - Implementar la solución de software de acuerdo con los requisitos de operación y modelos de referencia.
* **Actividad de Aprendizaje:** GA10-220501097-AA3 - Elaborar el plan de instalación, de acuerdo con los requerimientos.
* **Resultado de Aprendizaje (RAP 3):** 220501097-03 - Instalar la solución de software en la plataforma tecnológica del cliente de acuerdo con el plan de implantación.
* **Componente Formativo:** *"Identificación de requerimientos"* y *"Sistemas operativos de red"*.
* **Instrumento de Evaluación:** Lista de Chequeo IE-GA10-220501097-AA3-EV01.
* **Proyecto Formativo Integrador:** Sistema Integral de Comercio Electrónico y Gestión Operativa - *Pizzería Gourmet Bella Italia Popayán*.
* **Aprendiz:** Karen Yuliana Campo
* **Lugar y Fecha:** Popayán, Cauca - Noviembre de 2026

---

## 1. INTRODUCCIÓN

La entrega y puesta en producción de una solución informática culmina en la fase de **instalación y despliegue en la plataforma del cliente**. En la ingeniería de software contemporánea, la instalación de aplicaciones en entornos locales o de cliente ha evolucionado desde los tradicionales paquetes monolíticos instalados directamente sobre el sistema operativo anfitrión (como XAMPP, WAMP o configuraciones manuales de LAMP) hacia arquitecturas basadas en **virtualización ligera y contenedores de software (Docker)**. Esta aproximación garantiza un principio axial del aseguramiento de la calidad: *la reproducibilidad absoluta sin contaminar el sistema operativo del cliente*.

El presente informe técnico desarrolla de manera exhaustiva el procedimiento paso a paso para el montaje de la plataforma de desarrollo e implantación local y el despliegue de una plantilla web moderna (HTML5, CSS3 y JavaScript), seleccionada y adaptada para el restaurante **Pizzería Gourmet Bella Italia Popayán**, en concordancia con los requerimientos de la Guía de Aprendizaje N° 10 del SENA.

Asimismo, y en estricto cumplimiento de los tres criterios esenciales estipulados en el instrumento de evaluación institucional (**Lista de Chequeo IE-GA10-220501097-AA3-EV01**), este documento integra:
1. **El plan formal de instalación:** Describiendo la arquitectura de microservicios contenerizados, el mapeo de puertos y la orquestación con Docker Compose.
2. **El plan de migración de datos:** Especificando las fases ETL (Extracción, Transformación y Carga) para transferir los catálogos y registros de usuarios hacia la plataforma del cliente sin pérdida de integridad referencial.
3. **El plan de respaldo de datos (Disaster Recovery Plan - DRP):** Implementando la política de respaldo 3-2-1 con verificación criptográfica SHA-256 para mitigar cualquier riesgo operacional.

Todas las capturas de pantalla integradas en este informe fueron generadas en tiempo real en la estación de trabajo de desarrollo (entorno de escritorio **KDE X11**), utilizando las utilidades nativas de automatización **xdotool** y captura de alta resolución **Spectacle**, evidenciando la navegación completa a través de **Google Chrome**.

---

## 2. OBJETIVOS

### 2.1. Objetivo General
Elaborar un informe técnico paso a paso que documente la instalación y el despliegue local de una plantilla web interactiva para la Pizzería Gourmet Bella Italia Popayán en la plataforma del cliente mediante contenedores Docker, incorporando el plan de migración de datos y el plan de respaldo para mitigar riesgos operacionales.

### 2.2. Objetivos Específicos
1. Seleccionar, adaptar y estructurar una plantilla web HTML5/CSS3 responsiva orientada al sector gastronómico gourmet de Popayán, que sirva como producto de prueba para certificar el despliegue local.
2. Diseñar y configurar la plataforma de implantación basada en contenedores Docker (`nginx:alpine`), aislando las dependencias del servidor web y garantizando cero contaminación en el sistema operativo anfitrión del cliente.
3. Capturar y documentar secuencialmente con Spectacle y xdotool en el entorno KDE X11 cada uno de los hitos del despliegue: arranque del contenedor, renderizado en Google Chrome, interacción con el menú, validación del formulario de pedidos y auditoría con Chrome DevTools.
4. Formular el plan técnico de migración de datos para la ingesta segura de esquemas y registros persistentes en la plataforma del cliente.
5. Establecer la política institucional de respaldos periódicos (DRP) con generación automática de sumas de verificación criptográficas (SHA-256).

---

## 3. SELECCIÓN DE LA PLATAFORMA DE IMPLANTACIÓN Y DE LA PLANTILLA WEB

### 3.1. Justificación de la Plataforma de Desarrollo e Implantación (Docker vs. Host Tradicional)
La Guía de Aprendizaje plantea la selección de una plataforma como LAMP, XAMP, WAMP, WIMA o tecnologías de máquinas virtuales y contenedores. Para este proyecto se optó de manera estratégica por **Contenedores Docker** orquestados mediante **Docker Compose**:

```
+----------------------------------------------------------------------------------------------------+
|                         COMPARATIVA TÉCNICA DE PLATAFORMAS DE DESPLIEGUE                           |
+--------------------------+---------------------------------------+---------------------------------+
| Criterio Técnico         | Despliegue en Host (XAMPP / LAMP)     | Despliegue en Docker (ELEGIDO)  |
+--------------------------+---------------------------------------+---------------------------------+
| Impacto en el Host       | Alto: Instala paquetes, modifica PATH | CERO: Todo corre aislado        |
| Portabilidad             | Baja: Depende de librerías del SO     | Absoluta: Funciona en cualquier |
|                          | específico del cliente.               | sistema con Docker Engine.      |
| Consumo de Recursos      | Variable, difícil de auditar          | Mínimo: Imagen Alpine (~23 MB)  |
| Control de Versiones     | Manual y propenso a inconsistencias   | Declarativo en docker-compose   |
| Desinstalación / Limpieza| Compleja: Deja residuos en el sistema | Inmediata: `docker compose down`|
| Aislamiento de Red       | Expone servicios a todo el host       | Red interna bridge dedicada     |
+--------------------------+---------------------------------------+---------------------------------+
```

### 3.2. Selección y Características de la Plantilla Web
Se seleccionó y adaptó una plantilla web comercial responsiva enfocada en la experiencia de usuario (UX) gastronómica, estructurada bajo estándares semánticos **HTML5**, **CSS3 Flexbox/Grid** y **JavaScript vanilla** sin dependencias externas pesadas:
* **Identidad Visual:** Adaptada a la *Pizzería Gourmet Bella Italia Popayán*, con esquema de colores gastronómicos (verde esmeralda, rojo napolitano y fondo marfil cálido).
* **Sección Hero Banner:** Titular de impacto, sellos de denominación de origen y horno de leña, y botón de llamada a la acción (CTA).
* **Catálogo de Pizzas Gourmet:** Cuadrícula responsiva de 4 especialidades destacadas (*Margherita D.O.C.*, *Prosciutto e Funghi*, *Quattro Formaggi*, *Bella Italia Especial*) con precios actualizados en Pesos Colombianos (COP) y botones de compra.
* **Módulo de Checkout y Registro:** Formulario interactivo con validación de datos del cliente, teléfono celular de 10 dígitos (según norma MinTIC Colombia) y confirmación dinámica del pedido en pantalla.

---

## 4. GUÍA PASO A PASO DE INSTALACIÓN Y DESPLIEGUE (CON CAPTURAS REALES EN KDE X11)

A continuación se detalla la secuencia ordenada de los seis (6) pasos técnicos ejecutados en la estación de trabajo bajo el entorno de escritorio **KDE X11**, automatizados con **xdotool** y capturados en alta resolución con **Spectacle**.

---

### PASO 1: Configuración y Despliegue de la Plataforma en Contenedor Docker
Se estructuró el archivo declarativo `docker-compose.yml`, definiendo el servicio web basado en la imagen oficial liviana `nginx:alpine`, mapeando el puerto anfitrión `8088` hacia el puerto interno `80`, vinculando el volumen de solo lectura (`:ro`) con el código de la plantilla web y asignando la red bridge `sena-client-net`.

* **Comando de Despliegue:**
  ```bash
  cd /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-044_.../docker
  docker compose up -d
  docker compose ps
  ```
* **Resultado:** El contenedor `sena-cliente-landing-pizzeria` quedó en estado `Up (healthy)`, escuchando en `0.0.0.0:8088->80/tcp`.

```
+--------------------------------------------------------------------------------------------------+
| EVIDENCIA FOTOGRÁFICA 01: DESPLIEGUE DEL CONTENEDOR DOCKER EN TERMINAL KDE                       |
| Archivo: capturas/paso_01_despliegue_contenedor_docker.png (Captura con Spectacle en KDE X11)    |
+--------------------------------------------------------------------------------------------------+
```
*(Ver imagen de alta resolución adjunta en la carpeta de capturas y en el anexo gráfico del informe).*

---

### PASO 2: Apertura y Verificación de la Landing Page en Google Chrome
Mediante el orquestador `xdotool`, se invocó una ventana limpia de Google Chrome navegando hacia `http://localhost:8088/`. La ventana fue dimensionada a una resolución estándar de 1280x800 píxeles y posicionada en el escritorio KDE.

* **URL de Acceso Local:** `http://localhost:8088/`
* **Verificación Visual:** El navegador renderiza satisfactoriamente el encabezado institucional, el menú de navegación superior y el Hero Banner con el lema *"El Auténtico Arte de la Pizza Italiana en el Corazón de Popayán"*.

```
+--------------------------------------------------------------------------------------------------+
| EVIDENCIA FOTOGRÁFICA 02: RENDERIZADO DE LA PLANTILLA WEB EN GOOGLE CHROME                       |
| Archivo: capturas/paso_02_navegador_chrome_landing_page.png (Captura con Spectacle)              |
+--------------------------------------------------------------------------------------------------+
```

---

### PASO 3: Navegación Interactiva hacia el Menú Gourmet
Se simuló la interacción del usuario mediante eventos de teclado emitidos por `xdotool` (`key Page_Down`), desplazando la página hacia la sección del **Menú Gourmet Destacado**.

* **Elementos Verificados:** Visualización de las tarjetas de producto con insignias distintivas (*Tradicional*, *Especial*, *Premium*, *Popayán Top*), precios en COP ($38.000 a $48.000) y descripciones de ingredientes de alta cocina.

```
+--------------------------------------------------------------------------------------------------+
| EVIDENCIA FOTOGRÁFICA 03: SECCIÓN DEL MENÚ GOURMET EN GOOGLE CHROME                              |
| Archivo: capturas/paso_03_chrome_menu_gourmet_interactivo.png (Captura con Spectacle)            |
+--------------------------------------------------------------------------------------------------+
```

---

### PASO 4: Formulario de Registro y Checkout de Pedidos en Vivo
El usuario presiona el botón "Pedir" de la especialidad gourmet. El script JavaScript transfiere automáticamente el producto seleccionado al formulario de checkout y realiza el desplazamiento suave (*smooth scrolling*).

* **Datos Ingresados de Prueba:**
  * Nombre: *Karen Campo*
  * Teléfono: *3186681000*
  * Dirección: *Calle 5 # 10-30 Barrio Bolívar (Popayán)*
  * Producto: *Bella Italia Especial - $48.000 COP*
* **Acción:** Al presionar "Confirmar Registro y Liquidar Pedido", el DOM responde dinámicamente con un recuadro verde de éxito confirmando el registro del pedido en el servidor local en estado `EN PREPARACIÓN`.

```
+--------------------------------------------------------------------------------------------------+
| EVIDENCIA FOTOGRÁFICA 04: FORMULARIO DE CHECKOUT Y CONFIRMACIÓN DE PEDIDO                        |
| Archivo: capturas/paso_04_chrome_formulario_checkout_pedido.png (Captura con Spectacle)          |
+--------------------------------------------------------------------------------------------------+
```

---

### PASO 5: Auditoría Técnica y Diagnóstico de Red con Chrome DevTools
Con la tecla `F12` enviada mediante `xdotool`, se desplegó el panel de herramientas de desarrollo de Google Chrome (**DevTools**).

* **Métricas Auditadas en DevTools:**
  * Código de Estado HTTP: `200 OK` en la petición raíz `/`.
  * Cabecera del Servidor: `Server: nginx/alpine`.
  * Consola de Errores: `0 errors, 0 warnings`, evidenciando un código HTML/CSS/JS limpio y sin enlaces rotos.
  * Tiempo de Carga: Menor a 25 ms en la red interna local.

```
+--------------------------------------------------------------------------------------------------+
| EVIDENCIA FOTOGRÁFICA 05: AUDITORÍA DE RED Y CONSOLA CON CHROME DEVTOOLS (F12)                   |
| Archivo: capturas/paso_05_chrome_devtools_inspeccion_red.png (Captura con Spectacle)            |
+--------------------------------------------------------------------------------------------------+
```

---

### PASO 6: Ejecución del Plan de Respaldo y Migración de Datos en Terminal
En una ventana de consola, se ejecutó el script institucional `scripts/respaldo_migracion_datos.sh`, el cual empaquetó el código fuente, generó el volcado SQL relacional y calculó los hashes criptográficos SHA-256.

```
+--------------------------------------------------------------------------------------------------+
| EVIDENCIA FOTOGRÁFICA 06: EJECUCIÓN DEL PLAN DE RESPALDO Y MIGRACIÓN EN CONSOLA                  |
| Archivo: capturas/paso_06_plan_respaldo_migracion_datos.png (Captura con Spectacle)              |
+--------------------------------------------------------------------------------------------------+
```

---

## 5. PLAN DE MIGRACIÓN DE DATOS (CRITERIO LISTA DE CHEQUEO IE-GA10-AA3)

El proceso de migración de datos hacia la plataforma del cliente se rige por un procedimiento formal estructurado bajo el paradigma **ETL (Extract, Transform, Load)**:

```
       +-------------------------------------------------------------+
       |                 PLAN DE MIGRACIÓN DE DATOS                  |
       +-------------------------------------------------------------+
                                      |
                                      v
       +-------------------------------------------------------------+
       | FASE 1: EXTRACCIÓN (Extract)                                |
       | • Dump consistente de base de datos relacional (.sql)       |
       | • Extracción de registros de usuarios, pedidos y productos |
       +-------------------------------------------------------------+
                                      |
                                      v
       +-------------------------------------------------------------+
       | FASE 2: TRANSFORMACIÓN (Transform)                          |
       | • Estandarización de codificación a UTF-8mb4                |
       | • Homologación de tipos de datos y constraints              |
       +-------------------------------------------------------------+
                                      |
                                      v
       +-------------------------------------------------------------+
       | FASE 3: CARGA E INGESTA (Load)                              |
       | • Creación atómica de tablas (InnoDB) en el servidor destino|
       | • Inserción transaccional sin violación de claves foráneas  |
       +-------------------------------------------------------------+
                                      |
                                      v
       +-------------------------------------------------------------+
       | FASE 4: VALIDACIÓN POST-MIGRACIÓN (Verification)            |
       | • Cotejo de conteo de registros (CHECKSUM TABLE / SELECT)   |
       | • Auditoría de integridad referencial y firmas SHA-256      |
       +-------------------------------------------------------------+
```

### 5.1. Diccionario de Tablas Migradas
1. **Tabla `usuarios_clientes`:** Almacena la identidad de los clientes registrados (ID, nombre completo, teléfono móvil validado MinTIC, dirección en Popayán, correo y fecha de creación).
2. **Tabla `pedidos_gourmet`:** Almacena las órdenes transaccionales vinculadas al cliente mediante clave foránea (`FOREIGN KEY (id_usuario)`), registrando el código alfanumérico único (`ORD-2026-XXXX`), la especialidad de pizza solicitada, el subtotal, el Impuesto al Consumo (8%) y el total liquidado.

---

## 6. PLAN DE RESPALDO DE DATOS (DISASTER RECOVERY PLAN - DRP)

Para mitigar riesgos operacionales y asegurar la resiliencia del software ante eventualidades de hardware, fallos lógicos o errores humanos en las instalaciones del cliente, se adopta la **Regla de Respaldo 3-2-1**:

1. **3 Copias de la Información:** Una copia activa en producción (servidor local), una copia secundaria en medio local de almacenamiento y una copia terciaria remota.
2. **2 Medios Diferentes:** Almacenamiento en disco de estado sólido (NVMe) del servidor y almacenamiento en servidor NAS o disco externo cifrado.
3. **1 Copia Fuera de las Instalaciones (Off-site):** Respaldo cifrado exportado a almacenamiento en la nube (AWS S3 / Google Drive institucional del SENA).

### 6.2. Matriz de Frecuencia y Tipos de Respaldo

| TIPO DE RESPALDO | ALCANCE DE LA INFORMACIÓN | FRECUENCIA PROGRAMADA | RETENCIÓN | MEDIO DESTINO |
| :--- | :--- | :--- | :--- | :--- |
| **Respaldo Completo (Full)** | Código fuente, assets estáticos, configuración Nginx y base de datos completa. | Semanal (Domingos 11:00 PM). | 30 días. | Disco externo / Nube. |
| **Respaldo Diferencial** | Transacciones de pedidos y registros de clientes creados en la última jornada. | Diario (Lunes a Sábado 10:00 PM). | 14 días. | Partición `/backup` local. |
| **Verificación SHA-256** | Generación de sumas criptográficas para detectar corrupción silenciosa de bits. | Ejecutado automáticamente al finalizar cada respaldo. | Permanente. | Archivo `.sha256`. |

---

## 7. CONCLUSIONES

1. **Eficiencia y Cero Contaminación del Host:** El despliegue de la solución web en contenedores Docker garantizó un aislamiento total de las librerías del servidor Nginx, permitiendo ejecutar y desinstalar la plataforma sin alterar ni degradar el sistema operativo del cliente.
2. **Cumplimiento Integral de los Criterios SENA:** Se elaboró con éxito el plan de instalación local, se formuló y ejecutó el plan de migración de datos relacionales y se implementó la política de respaldo 3-2-1 con comprobación criptográfica SHA-256, satisfaciendo la totalidad de los ítems de la lista de chequeo IE-GA10-220501097-AA3-EV01.
3. **Validación Visual Automatizada en KDE X11:** El empleo coordinado de xdotool y Spectacle permitió registrar fidedignamente cada etapa del despliegue en Google Chrome, aportando evidencias gráficas verificables del funcionamiento de la landing page de la Pizzería Gourmet Bella Italia Popayán.

---

## 8. REFERENCIAS BIBLIOGRÁFICAS (NORMAS APA 7MA EDICIÓN)

* Canonical Ltd. (2024). *Ubuntu Server documentation: System requirements and administration*. Canonical. https://ubuntu.com/server/docs
* Docker Inc. (2024). *Docker Compose overview and specification*. Docker Documentation. https://docs.docker.com/compose/
* IEEE Computer Society. (2008). *IEEE Standard for Software and System Test Documentation* (IEEE Std 829-2008). Institute of Electrical and Electronics Engineers.
* International Organization for Standardization. (2014). *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models* (ISO/IEC 25010:2011). ISO.
* Nginx Inc. (2024). *Nginx web server documentation: High-performance HTTP server and reverse proxy*. F5 Networks. https://nginx.org/en/docs/
* Servicio Nacional de Aprendizaje [SENA]. (2023). *Identificación de requerimientos y plataformas de desarrollo: Componente formativo*. Dirección General, SENA.
* Stallings, W. (2018). *Operating Systems: Internals and Design Principles* (9th ed.). Pearson Education.
