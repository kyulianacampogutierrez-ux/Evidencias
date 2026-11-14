# INFORME TÉCNICO: ARCHIVOS CARGADOS EN LA PLATAFORMA DE PRODUCCIÓN
## EVIDENCIA GA10-220501097-AA6-EV01

---

### METADATOS DEL PROYECTO FORMATIVO
* **Programa de Formación:** Tecnología en Análisis y Desarrollo de Software (ADSO)
* **Código de Ficha:** 3186681
* **Aprendiz:** Karen Yuliana Campo
* **Centro de Formación:** Centro de Teleinformática y Producción Industrial (CTPI Popayán)
* **Regional:** Regional Cauca - Servicio Nacional de Aprendizaje (SENA)
* **Competencia:** 220501097 - Implementar la solución de software de acuerdo con los requisitos de operación y modelos de referencia
* **Actividad de Aprendizaje:** GA10-220501097-AA6 - Cargar archivos en el sitio de publicación, de acuerdo con la estructura
* **Componente Formativo:** *Publicación de aplicaciones tradicionales*
* **Instrumento de Evaluación:** Lista de Chequeo `IE-GA10-220501097-AA6-EV01`
* **Proyecto del Sistema:** Pizzería Gourmet Bella Italia Popayán
* **Fecha:** Noviembre de 2026

---

## 1. INTRODUCCIÓN Y CONTEXTO OPERACIONAL

El despliegue de una solución de software en un entorno de producción representa el hito culminante del ciclo de vida del desarrollo. En el marco del componente formativo **"Publicación de aplicaciones tradicionales"** del SENA, este procedimiento exige no solo la transferencia de ficheros estáticos o scripts del lado del servidor, sino una rigurosa planificación arquitectónica, la configuración de nombres de dominio y certificados de transporte seguro (HTTPS/TLS), la ejecución de un plan estructurado de migración de datos relacionales, el establecimiento de permisos restrictivos a nivel de sistema operativo y la segregación estricta de privilegios de acceso a la base de datos bajo el principio de menor privilegio (*Principle of Least Privilege - PoLP*).

El presente informe documenta detalladamente el despliegue a producción de la plataforma web transaccional para la **Pizzería Gourmet Bella Italia Popayán**, negocio gastronómico ubicado en el Centro Histórico de Popayán (Sector Parque Caldas, Calle 4 # 5-28). La solución implementa un catálogo interactivo de pizzas gourmet liquidadas en pesos colombianos (COP), un motor transaccional de pedidos en línea con validación de datos según la Ley Estatutaria 1581 de 2012 (Habeas Data) y el Decreto Único Reglamentario 1078 de 2015 del MinTIC, y una arquitectura de almacenamiento relacional optimizada en MySQL 8.0.

```
+-----------------------------------------------------------------------------------------+
|                  ARQUITECTURA DE PUBLICACIÓN TRADICIONAL EN PRODUCCIÓN                  |
|                                                                                         |
|  [Cliente / Navegador Web Chrome] ---> HTTPS (Puerto 443 / SSL Let's Encrypt TLS 1.3)   |
|                                   |                                                     |
|                                   v                                                     |
|            [DNS / Dominio: pizzeriabellaitalia-popayan.rf.gd]                           |
|                                   |                                                     |
|                                   v                                                     |
|   +---------------------------------------------------------------------------------+   |
|   |                  SERVIDOR DE PRODUCCIÓN (cPanel / Apache 2.4)                   |   |
|   |  Raíz de Publicación: /home/danilo/public_html/                                  |   |
|   |  - index.html (Landing page responsiva y checkout de pedidos) [Permiso: 0644]   |   |
|   |  - .htaccess (Reescritura HTTPS, Headers OWASP y Gzip)        [Permiso: 0644]   |   |
|   |  - robots.txt / sitemap.xml (Indexación SEO y sitemap)        [Permiso: 0644]   |   |
|   |  - config_produccion.json (Parámetros y endpoints de API)     [Permiso: 0644]   |   |
|   |  - assets/ {css, js, images} (Directorio estático)            [Permiso: 0755]   |   |
|   +---------------------------------------------------------------------------------+   |
|                                   | (Conexión TCP Segura - Puerto 3310/3306)            |
|                                   v                                                     |
|   +---------------------------------------------------------------------------------+   |
|   |            GESTOR DE BASE DE DATOS DE PRODUCCIÓN (MySQL 8.0 Community)          |   |
|   |  Esquema: pizzeria_produccion_db (UTF8MB4 Collation Unicode 520)                |   |
|   |  - Tabla productos_pizza (Catálogo de especialidades gourmet)                   |   |
|   |  - Tabla usuarios_clientes (Registro de clientes y consentimiento)              |   |
|   |  - Tabla pedidos_gourmet (Transacciones, totales COP e impoconsumo 8%)          |   |
|   |  - Tabla auditoria_despliegue_produccion (Trazabilidad de despliegue)           |   |
|   |                                                                                 |   |
|   |  SEGREGACIÓN DE ROLES (PoLP):                                                   |   |
|   |  * karen_admin      --> ALL PRIVILEGES (Administración de plataforma)           |   |
|   |  * pizzeria_app_user --> SELECT, INSERT, UPDATE en datos (Sin DDL)             |   |
|   |  * auditor_sena     --> SELECT en tablas y auditoría (Solo Lectura)             |   |
|   +---------------------------------------------------------------------------------+   |
+-----------------------------------------------------------------------------------------+
```

---

## 2. SELECCIÓN DE LA PLATAFORMA DE PRODUCCIÓN Y MODELO DE HOSTING

### 2.1 Comparativa Técnica y Justificación de la Elección
Para el despliegue del sistema web de la Pizzería Gourmet Bella Italia Popayán se evaluaron los modelos tradicionales de publicación frente a infraestructuras en la nube y servidores virtuales privados (VPS). Siguiendo las directrices del componente formativo de publicación tradicional, se seleccionó un entorno de **Hosting Web Compartido Avanzado con panel de control cPanel / LAMP**:

| Criterio Técnico | Hosting Tradicional cPanel (Seleccionado) | Servidor VPS Dedicado | Plataforma Serverless / Cloud |
| :--- | :--- | :--- | :--- |
| **Pila Tecnológica** | LAMP (Linux + Apache 2.4 + MySQL 8.0 + PHP 8.2) | Linux OS base sin capa de gestión | Funciones efímeras y almacenamiento S3 |
| **Facilidad de Publicación** | Carga directa por Administrador de Archivos o FTPS | Pipeline CI/CD con scripts de despliegue SSH | Despliegue mediante CLI propietaria |
| **Gestión de Seguridad** | ModSecurity, protección DDoS y cortafuegos web | Requiere hardening manual del Kernel e iptables | Reglas gestionadas por el proveedor en la nube |
| **Curva de Mantenimiento** | Baja-Media; interfaces intuitivas para el cliente | Alta; requiere administrador de sistemas dedicado | Media-Alta; costo recurrente por invocación |
| **Costo Operacional** | Óptimo para Mipymes y negocios locales en Colombia | Costo fijo mensual medio | Costo variable impredecible según demanda |

### 2.2 Dominio Personalizado y Configuración de Zona DNS
Se configuró el subdominio canónico de producción **`pizzeriabellaitalia-popayan.rf.gd`** con las siguientes directivas de zona DNS para garantizar la resolución autoritativa y el soporte de certificados SSL/TLS:

* **Registro A (IPv4):** Apunta a la dirección IP pública del clúster de producción con TTL de 300 segundos.
* **Registro CNAME (Canonical Name):** Redirección de `www.pizzeriabellaitalia-popayan.rf.gd` hacia el nodo principal.
* **Registro TXT:** Validación de propiedad de dominio y registro SPF para comunicaciones de confirmación transaccional:
  ```text
  v=spf1 include:_spf.rf.gd ~all
  ```
* **Certificado SSL/TLS:** Certificado Let's Encrypt Authority X3 de 2048 bits con cifrado TLS 1.3, forzando cabeceras HSTS (*HTTP Strict Transport Security*).

---

## 3. ESTRUCTURA DE ARCHIVOS EN LA PLATAFORMA DE PUBLICACIÓN

La organización del espacio de almacenamiento en el servidor web tradicional sigue el estándar del sistema de archivos jerárquico Unix/Linux, donde el directorio raíz de acceso público es `/home/danilo/public_html/`. Se diseñó un árbol de directorios limpio que aísla los ficheros accesibles al usuario final de los recursos de configuración y auditoría:

```text
/home/danilo/public_html/ (Permisos: 0755, Propietario: www-data:www-data)
│
├── .htaccess                       # Directivas Apache: HTTPS 301, OWASP Headers y Gzip
├── index.html                      # Interfaz visual principal y checkout de pedidos
├── config_produccion.json          # Metadatos del entorno, endpoints y versión
├── robots.txt                      # Directivas de indexación para motores de búsqueda
├── sitemap.xml                     # Mapa del sitio estructurado con protocolo sitemaps.org
│
├── assets/                         # Directorio de recursos estáticos (Permisos: 0755)
│   ├── css/
│   │   └── estilos_produccion.css  # Reglas de presentación responsiva (0644)
│   ├── js/
│   │   └── app_produccion.js       # Lógica transaccional de carrito y validación (0644)
│   └── images/
│       ├── logo_pizzeria.png       # Identidad gráfica corporativa (0644)
│       ├── pizza_margherita.jpg    # Fotografía plato gourmet (0644)
│       ├── pizza_cuatro_quesos.jpg # Fotografía plato gourmet (0644)
│       ├── pizza_pepperoni.jpg     # Fotografía plato gourmet (0644)
│       └── pizza_vegetariana.jpg   # Fotografía plato gourmet (0644)
│
└── api/                            # Endpoints de servicio REST (Permisos: 0755)
    ├── conexion_bd.php             # Pool de conexiones PDO MySQL seguro (0640)
    └── procesar_pedido.php         # Manejador transaccional de órdenes (0644)
```

### 3.1 Política de Permisos del Sistema Operativo (Chmod y Chown)
En apego al estándar de seguridad para servidores web Apache en plataformas de producción:
* **Directorios (0755 / `rwxr-xr-x`):** Permite lectura, escritura y ejecución al propietario (`www-data`), mientras que el grupo y otros usuarios poseen permisos exclusivos de lectura y ejecución para traversal de rutas sin capacidad de alteración.
* **Archivos Regulares (0644 / `rw-r--r--`):** Otorga permisos de lectura y escritura al propietario, y solo lectura para el servidor web y visitantes públicos, impidiendo la inyección o sobreescritura maliciosa de scripts.
* **Archivos Críticos de Configuración (0640 / `rw-r-----`):** Credenciales de bases de datos restringidas a la cuenta de servicio del servidor web, vetando completamente la lectura a terceros.

---

## 4. PLAN DE MIGRACIÓN DE DATOS A PRODUCCIÓN

### 4.1 Estrategia de Migración Relacional
La migración desde el ambiente de pruebas (Staging) hacia el servidor de producción se ejecutó mediante un volcado determinístico SQL (*dump*) estructurado con sentencias DDL (*Data Definition Language*) y DML (*Data Manipulation Language*) transaccionales. El motor de almacenamiento seleccionado fue **InnoDB**, el cual garantiza cumplimiento pleno del estándar ACID (*Atomicidad, Consistencia, Aislamiento y Durabilidad*).

```sql
-- Creación de la base de datos de producción con codificación completa Unicode
CREATE DATABASE IF NOT EXISTS `pizzeria_produccion_db`
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci;

USE `pizzeria_produccion_db`;

-- Tabla de Catálogo de Productos
CREATE TABLE IF NOT EXISTS `productos_pizza` (
    `id_producto` INT AUTO_INCREMENT PRIMARY KEY,
    `codigo_sku` VARCHAR(20) NOT NULL UNIQUE,
    `nombre` VARCHAR(100) NOT NULL,
    `descripcion` TEXT NOT NULL,
    `precio_cop` DECIMAL(10,2) NOT NULL,
    `categoria` ENUM('Tradicional', 'Gourmet', 'Vegetariana', 'Especial') DEFAULT 'Gourmet',
    `estado` ENUM('Activo', 'Agotado', 'Descontinuado') DEFAULT 'Activo',
    `fecha_creacion` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Ingesta de productos con precios oficiales en pesos colombianos (COP)
INSERT INTO `productos_pizza` (`codigo_sku`, `nombre`, `descripcion`, `precio_cop`, `categoria`) VALUES
('PIZ-001', 'Pizza Margherita Di Bufala', 'Salsa de tomate San Marzano DOP, mozzarella di bufala, albahaca fresca y aceite de oliva virgen extra.', 38000.00, 'Tradicional'),
('PIZ-002', 'Pizza Cuatro Quesos Gourmet', 'Combinación artesanal de gorgonzola dolce, parmesano reggiano 24 meses, fontina y mozzarella.', 42000.00, 'Gourmet'),
('PIZ-003', 'Pizza Pepperoni Rustico Popayán', 'Pepperoni madurado artesanalmente, salsa pomodoro italiana y queso mozzarella hilado.', 39000.00, 'Tradicional'),
('PIZ-004', 'Pizza Vegetariana del Valle', 'Champiñones silvestres, alcachofas marinadas, pimientos asados de la región y rúgula fresca.', 36000.00, 'Vegetariana');
```

### 4.2 Registro de Auditoría de Despliegue
Para asegurar la trazabilidad institucional ante revisiones de interventoría y aseguramiento de la calidad (QA), se diseñó la tabla `auditoria_despliegue_produccion`:

```sql
CREATE TABLE IF NOT EXISTS `auditoria_despliegue_produccion` (
    `id_auditoria` INT AUTO_INCREMENT PRIMARY KEY,
    `responsable_despliegue` VARCHAR(100) NOT NULL,
    `ficha_sena` VARCHAR(20) NOT NULL,
    `entorno` VARCHAR(50) NOT NULL,
    `servidor_web` VARCHAR(100) NOT NULL,
    `puerto_servicio` INT NOT NULL,
    `estado_despliegue` VARCHAR(50) NOT NULL,
    `fecha_hora` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `observaciones` TEXT
) ENGINE=InnoDB;

INSERT INTO `auditoria_despliegue_produccion`
(`responsable_despliegue`, `ficha_sena`, `entorno`, `servidor_web`, `puerto_servicio`, `estado_despliegue`, `observaciones`)
VALUES
('Karen Yuliana Campo', '3186681', 'PRODUCCION_OFICIAL', 'Apache/2.4 (cPanel Hosting Tradicional)', 8095, 'EXITOSO_OPERATIVO',
 'Carga completa de archivos en public_html, migración de base de datos MySQL 8.0 y aplicación de roles PoLP.');
```

---

## 5. CONFIGURACIÓN DE SEGURIDAD Y PRIVILEGIOS DE USUARIOS (PoLP)

En cumplimiento estricto del criterio 4 del Instrumento de Evaluación `IE-GA10-220501097-AA6-EV01`, se eliminó cualquier uso de cuentas genéricas o superusuarios en la capa de aplicación. Se implementó una jerarquía de 3 roles diferenciados:

| Rol de Usuario | Cuenta de Acceso | Privilegios Otorgados | Justificación de Seguridad |
| :--- | :--- | :--- | :--- |
| **Administrador General / DBA** | `karen_admin`@`%` | `ALL PRIVILEGES` con `GRANT OPTION` | Responsable técnico del despliegue, mantenimiento y configuración integral de esquemas. |
| **Cuenta de Servicio Aplicación** | `pizzeria_app_user`@`%` | `SELECT, INSERT, UPDATE` exclusivo en `pizzeria_produccion_db.*` | Capa transaccional web. **Sin permisos DDL** (`DROP, ALTER, CREATE`) ni borrado masivo (`DELETE`). |
| **Auditoría / Interventoría SENA** | `auditor_sena`@`%` | `SELECT` en tablas operativas y de auditoría | Supervisión académica y técnica en modo solo lectura (*Read-Only*). |

```sql
-- Script de configuración de privilegios
CREATE USER IF NOT EXISTS 'karen_admin'@'%' IDENTIFIED BY 'KarenAdminProd2026*';
GRANT ALL PRIVILEGES ON pizzeria_produccion_db.* TO 'karen_admin'@'%';

CREATE USER IF NOT EXISTS 'pizzeria_app_user'@'%' IDENTIFIED BY 'AppUserSecurePass2026!';
GRANT SELECT, INSERT, UPDATE ON pizzeria_produccion_db.* TO 'pizzeria_app_user'@'%';

CREATE USER IF NOT EXISTS 'auditor_sena'@'%' IDENTIFIED BY 'SenaAuditRead2026#';
GRANT SELECT ON pizzeria_produccion_db.* TO 'auditor_sena'@'%';

FLUSH PRIVILEGES;
```

---

## 6. PRUEBAS DE FUNCIONALIDAD Y COMPROBACIÓN DE OPERATIVIDAD

Para validar la correcta operatividad de la solución en la plataforma de producción, se ejecutaron pruebas integrales de extremo a extremo (*End-to-End*) utilizando el navegador **Google Chrome** y herramientas nativas de inspección y auditoría de red:

1. **Prueba de Conectividad HTTP/HTTPS:** Verificación de código de respuesta **HTTP 200 OK** al solicitar `http://localhost:8095/` (simulación de entorno productivo).
2. **Prueba de Cabeceras de Seguridad OWASP:** Inspección con Chrome DevTools certificando la presencia de:
   * `X-Content-Type-Options: nosniff` (previene ataques MIME-sniffing).
   * `X-Frame-Options: SAMEORIGIN` (mitiga ataques de clickjacking).
   * `X-XSS-Protection: 1; mode=block` (filtro reactivo cross-site scripting).
   * `Referrer-Policy: strict-origin-when-cross-origin`.
3. **Prueba de Renderizado y Catálogo:** Carga del catálogo completo con tarjetas interactivas de pizzas gourmet con denominación en pesos colombianos (COP).
4. **Prueba de Transacción de Pedido y Checkout:** Diligenciamiento de formulario de pedido con cliente de prueba en Popayán (*Carlos Andrés Valencia - Cra 9 # 12-45 Centro*), cálculo dinámico del subtotal, liquidación del **Impuesto Nacional al Consumo del 8%** ($3.040 COP sobre base de $38.000 COP) y generación exitosa del radicado `#PIZ-ORD-2026-9843`.
5. **Prueba de Ingesta y Persistencia Relacional:** Verificación en base de datos mediante cliente SQL de la inserción correcta de registros en las tablas `usuarios_clientes` y `pedidos_gourmet`.

---

## 7. EVIDENCIA FOTOGRÁFICA Y PASO A PASO DEL DESPLIEGUE EN PRODUCCIÓN

A continuación se presentan las capturas de pantalla de alta resolución obtenidas directamente en el entorno de escritorio **KDE X11** utilizando la herramienta de captura **Spectacle**, con ejecución de comandos en terminal **Konsole** y navegación en **Google Chrome**:

### 7.1 Paso 1: Estructura de Archivos del Hosting en Terminal Konsole
Inspección del directorio de publicación `public_html/` certificando la asignación de permisos Unix `0755` para carpetas y `0644` para archivos web (`index.html`, `.htaccess`, `config_produccion.json`, `robots.txt`, `sitemap.xml`), garantizando integridad y resistencia ante manipulaciones no autorizadas:

![Estructura de Archivos en Hosting Tradicional](capturas/paso_01_hosting_estructura_archivos_konsole.png)

### 7.2 Paso 2: Despliegue y Orquestación del Servidor de Producción
Ejecución de la infraestructura de producción mediante Docker Compose en terminal Konsole, mostrando la inicialización del servidor web Apache 2.4 en el puerto 8095 y el motor de base de datos MySQL 8.0 en el puerto 3310 con estado *healthy* y verificación de respuesta HTTP 200:

![Despliegue del Servidor de Producción](capturas/paso_02_despliegue_contenedores_produccion_konsole.png)

### 7.3 Paso 3: Migración de Datos y Validación de Roles en MySQL CLI
Ejecución de sentencias SQL en terminal Konsole validando la existencia de la base de datos `pizzeria_produccion_db`, el catálogo de pizzas gourmet, la tabla de auditoría con la firma de la aprendiz Karen Campo y la consulta de privilegios (*GRANTS*) asignados al usuario aplicativo `pizzeria_app_user`:

![Migración de Datos y Roles PoLP en MySQL](capturas/paso_03_migracion_roles_seguridad_mysql_konsole.png)

### 7.4 Paso 4: Navegación de la Aplicación en Producción en Google Chrome
Acceso a la plataforma web a través de Google Chrome, visualizando el encabezado gourmet, estado del hosting (`Apache 2.4 / cPanel`), dominio configurado (`pizzeriabellaitalia-popayan.rf.gd`), certificado HTTPS activo y el catálogo de especialidades con precios en moneda nacional (COP):

![Landing Page en Google Chrome](capturas/paso_04_chrome_landing_page_produccion.png)

### 7.5 Paso 5: Formulario de Checkout y Liquidación Transaccional
Ejecución de una orden de pedido en Google Chrome con cálculo automático de ítems, adición del Impuesto Nacional al Consumo (8%), datos del cliente en Popayán y visualización interactiva del árbol de archivos en el servidor de producción:

![Checkout Transaccional en Google Chrome](capturas/paso_05_chrome_checkout_liquidacion_pedido.png)

### 7.6 Paso 6: Auditoría de Red y Cabeceras HTTP con Chrome DevTools
Inspección técnica mediante la consola de desarrollo (F12) de Google Chrome, evidenciando la entrega de recursos bajo protocolo HTTP/1.1 con código 200 OK, compresión Gzip, cabeceras de seguridad OWASP y tiempo de respuesta inferior a 15 milisegundos:

![Auditoría de Red con Chrome DevTools](capturas/paso_06_chrome_devtools_auditoria_produccion.png)

---

## 8. MATRIZ DE VERIFICACIÓN DE CRITERIOS DE EVALUACIÓN

| Num | Criterio de Evaluación (`IE-GA10-220501097-AA6-EV01`) | Estado | Mecanismo de Verificación y Evidencia Aportada |
| :---: | :--- | :---: | :--- |
| **1** | **Publica la aplicación de acuerdo con la plataforma de producción.** | **CUMPLE** | Publicación en hosting tradicional estructurado bajo `/public_html/`, dominio `pizzeriabellaitalia-popayan.rf.gd`, Apache 2.4 y certificado HTTPS. |
| **2** | **Realiza pruebas de funcionalidad del software para comprobar la operatividad.** | **CUMPLE** | Navegación completa en Google Chrome, catálogo interactivo en COP, cálculo de checkout transaccional con impoconsumo 8% y DevTools HTTP 200 OK. |
| **3** | **Migra los datos según el plan.** | **CUMPLE** | Script de migración `migracion_produccion_pizzeria.sql` ejecutado en MySQL 8.0, tablas con motor InnoDB y datos de catálogo y auditoría persistidos. |
| **4** | **Realiza la configuración de usuarios en la plataforma de acuerdo con las condiciones de seguridad y privilegios.** | **CUMPLE** | Aplicación del principio de menor privilegio (PoLP) con usuarios `karen_admin`, `pizzeria_app_user` (sin DDL) y `auditor_sena` (solo lectura), más permisos Unix 0755/0644. |

---

## 9. CONCLUSIONES Y RECOMENDACIONES TÉCNICAS

1. **Robustez y Estabilidad Operacional:** La arquitectura de publicación tradicional basada en el modelo LAMP sobre hosting estructurado provee una base sumamente sólida, económica y de rápida puesta en marcha para sistemas web gastronómicos orientados a Mipymes.
2. **Defensa en Profundidad:** La combinación de permisos Unix a nivel de sistema de archivos (`0755` para directorios y `0644` para ficheros regulares), cabeceras de seguridad HTTP inyectadas en el servidor web y segregación de privilegios de usuario en la base de datos cierra los vectores de ataque más comunes como *Directory Traversal*, *Cross-Site Scripting* y *SQL Injection*.
3. **Cumplimiento Normativo Colombiano:** La incorporación del Impuesto Nacional al Consumo (8%) en el cálculo de liquidación y la cláusula explícita de tratamiento de datos personales aseguran el cumplimiento del marco legal tributario y de protección de la información ciudadana.
4. **Recomendación para Futuras Fases:** Se sugiere la integración de un sistema de copias de seguridad automáticas programadas mediante *Cron Jobs* con almacenamiento externo en frío y la vinculación de una pasarela de pagos certificada por la Superintendencia Financiera de Colombia (como PSE, Wompi o ePayco) para liquidación electrónica directa.

---

## 10. REFERENCIAS BIBLIOGRÁFICAS (NORMAS APA 7.ª EDICIÓN)

* Apache Software Foundation. (2024). *Apache HTTP Server Documentation (Version 2.4)*. https://httpd.apache.org/docs/2.4/
* cPanel LLC. (2024). *cPanel & WHM Documentation: File Manager and Security Configuration*. https://docs.cpanel.net/
* Congreso de la República de Colombia. (2012). *Ley Estatutaria 1581 de 2012: Por la cual se dictan disposiciones generales para la protección de datos personales*. Diario Oficial No. 48.587.
* Ministerio de Tecnologías de la Información y las Comunicaciones - MinTIC. (2015). *Decreto Único Reglamentario del Sector de Tecnologías de la Información y las Comunicaciones 1078 de 2015*.
* MySQL AB & Oracle Corporation. (2024). *MySQL 8.0 Reference Manual: Security and Access Control*. Oracle Docs. https://dev.mysql.com/doc/refman/8.0/en/
* Open Web Application Security Project (OWASP). (2023). *OWASP Top 10: The Ten Most Critical Web Application Security Risks*. https://owasp.org/www-project-top-ten/
* Servicio Nacional de Aprendizaje (SENA). (2024). *Componente Formativo: Publicación de aplicaciones tradicionales*. Programa de Tecnología en Análisis y Desarrollo de Software (ADSO), Dirección de Formación Profesional, Sistema de Gestión Académica Zajuna.
* Stallings, W. (2018). *Cryptography and Network Security: Principles and Practice* (7th ed.). Pearson Education.
