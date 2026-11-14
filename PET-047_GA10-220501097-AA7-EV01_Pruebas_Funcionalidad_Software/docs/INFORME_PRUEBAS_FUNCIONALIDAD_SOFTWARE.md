# INFORME TÉCNICO: REALIZACIÓN DE PRUEBAS DE FUNCIONALIDAD DEL SOFTWARE
## EVIDENCIA GA10-220501097-AA7-EV01

---

### METADATOS DEL PROYECTO FORMATIVO
* **Programa de Formación:** Tecnología en Análisis y Desarrollo de Software (ADSO)
* **Código de Ficha:** 3186681
* **Aprendiz:** Karen Yuliana Campo
* **Centro de Formación:** Centro de Teleinformática y Producción Industrial (CTPI Popayán)
* **Regional:** Regional Cauca - Servicio Nacional de Aprendizaje (SENA)
* **Competencia:** 220501097 - Implementar la solución de software de acuerdo con los requisitos de operación y modelos de referencia
* **Actividad de Aprendizaje:** GA10-220501097-AA7 - Realizar pruebas de funcionalidad del software, de acuerdo con el modelo
* **Componente Formativo:** *Publicación de aplicaciones tradicionales*
* **Instrumento de Evaluación:** Lista de Chequeo `IE-GA10-220501097-AA7-EV01`
* **Proyecto del Sistema:** Pizzería Gourmet Bella Italia Popayán
* **Dominio Publicado:** `pizzeriabellaitalia-popayan.rf.gd` (HTTPS / TLS 1.3)
* **Fecha:** Noviembre de 2026

---

## 1. INTRODUCCIÓN Y CONTEXTO METODOLÓGICO

El proceso de aseguramiento de la calidad de software (*Quality Assurance - QA*) en entornos de producción tradicionales exige una rigurosa verificación posterior al despliegue. En el marco del componente formativo **"Publicación de aplicaciones tradicionales"** de la Guía de Aprendizaje 10, la actividad **GA10-220501097-AA7** plantea la exploración y ejecución de pruebas de funcionalidad sobre aplicaciones web alojadas en plataformas de hosting y dominio comercialmente utilizadas.

El objetivo central de este informe es condensar una investigación exhaustiva y su aplicación práctica sobre la pregunta estructurante: **¿Cómo se deberían realizar las pruebas de funcionalidad de un sitio publicado en Internet?**, contrastando la teoría con el entorno productivo real implementado para la **Pizzería Gourmet Bella Italia Popayán** (ubicada en el Centro Histórico de Popayán, Calle 4 # 5-28).

```
+-----------------------------------------------------------------------------------------+
|                  MODELO INTEGRAL DE PRUEBAS FUNCIONALES EN SITIO PUBLICADO               |
|                                                                                         |
|  [ 1. DOMINIO Y DNS ]       [ 2. CROSS-BROWSER ]      [ 3. MOBILE-FIRST ]               |
|  * Registros A, CNAME, SPF   * Blink (Chrome, Edge)    * Meta Viewport Responsivo       |
|  * Propagación DNS Global    * Gecko (Firefox)         * Breakpoints 375px/412px/768px  |
|  * Certificado TLS 1.3       * WebKit (Safari iOS)     * Menú Hamburguesa Táctil        |
|  * Redirección 301 HTTPS     * Normalización CSS/JS    * Touch Targets >= 48x48 px      |
|              \                       |                       /                          |
|               \                      |                      /                           |
|                v                     v                     v                            |
|  +-----------------------------------------------------------------------------------+  |
|  |             4. TAXONOMÍA DE ELEMENTOS A PROBAR EN LA APLICACIÓN WEB               |  |
|  |  a) Navegación y Enlaces: Consistencia de rutas internas, anclas y ausencia 404   |  |
|  |  b) Formularios y Validación: Reglas regex (celular Colombia 10 dígitos 3XXXXXXXXX)|  |
|  |  c) Lógica Transaccional: Liquidación en COP + 8% Impuesto Nacional al Consumo   |  |
|  |  d) Cumplimiento Normativo: Cláusula Habeas Data Ley 1581 / Decreto 1078 MinTIC  |  |
|  |  e) Persistencia e Integridad BD: Motor MySQL 8.0 InnoDB con transacciones ACID   |  |
|  |  f) Seguridad y Rendimiento: Cabeceras OWASP (nosniff, X-Frame) y compresión Gzip |  |
|  +-----------------------------------------------------------------------------------+  |
+-----------------------------------------------------------------------------------------+
```

---

## 2. DESARROLLO DE LA INVESTIGACIÓN: LAS CUATRO DIMENSIONES CLAVE DE PRUEBAS

### 2.1 ¿Cómo verificar si un dominio está bien configurado?
La correcta configuración de un nombre de dominio es la piedra angular para que los clientes y sistemas externos accedan a los servicios web. La verificación técnica se desglosa en cuatro niveles de inspección:

#### A. Resolución Autoritativa de Servidores de Nombres (Name Servers - NS)
Se comprueba que el registrador del dominio (Registrar) apunte a los servidores NS autorizados que alojan la zona DNS:
* Servidores configurados: `ns1.epizy.com` y `ns2.epizy.com`.
* Herramientas de consulta: `whois pizzeriabellaitalia-popayan.rf.gd` y `dig NS pizzeriabellaitalia-popayan.rf.gd`.

#### B. Comprobación de Registros de Zona DNS Esenciales
* **Registro A (Host Address):** Asocia el nombre de dominio con la dirección IPv4 pública del servidor de producción (`185.27.134.148`). Se verifica con:
  ```bash
  dig A pizzeriabellaitalia-popayan.rf.gd +short
  nslookup pizzeriabellaitalia-popayan.rf.gd
  ```
* **Registro CNAME (Canonical Name):** Garantiza que subdominios habituales como `www.pizzeriabellaitalia-popayan.rf.gd` resuelvan hacia el dominio canónico sin generar certificados SSL mismatch.
* **Registro TXT / SPF (Sender Policy Framework):** Protege contra el envío de correos suplantados (phishing) al emitir radicados de pedidos:
  ```text
  v=spf1 include:_spf.rf.gd ~all
  ```
* **Tiempo de Vida (TTL - Time To Live):** Se valida un TTL óptimo (300 a 3600 segundos) para permitir cambios ágiles durante despliegues sin esperas prolongadas.

#### C. Validación de Certificados de Seguridad SSL/TLS y Transporte HTTPS
Un dominio moderno debe garantizar el cifrado en tránsito para evitar intercepciones de credenciales o pedidos:
* Se ejecuta inspección de socket seguro con OpenSSL:
  ```bash
  openssl s_client -connect pizzeriabellaitalia-popayan.rf.gd:443 -servername pizzeriabellaitalia-popayan.rf.gd
  ```
* Verificación de la autoridad de certificación (Let's Encrypt Authority X3), vigencia del certificado x509, soporte de protocolo TLS 1.3 y algoritmos de intercambio efímero de claves (ECDHE-RSA-AES256-GCM-SHA384).
* Validación de redirección canónica **HTTP 301 Moved Permanently** hacia la versión segura HTTPS mediante `curl -I http://pizzeriabellaitalia-popayan.rf.gd/`.

---

### 2.2 ¿Una aplicación web se ve igual en todos los exploradores web?
**No, una aplicación web no se ve de forma idéntica de manera nativa en todos los navegadores.** Esta discrepancia se origina en la existencia de múltiples motores de renderizado y ejecución de código:

| Motor de Renderizado | Navegadores que lo Utilizan | Características y Desafíos de Compatibilidad |
| :--- | :--- | :--- |
| **Blink** (Chromium) | Google Chrome, Microsoft Edge, Brave, Opera | Soporte pionero en estándares W3C modernos; motor V8 ultra-rápido para JavaScript ES2024. |
| **Gecko** | Mozilla Firefox, Tor Browser | Motor Quantum con estricta adherencia a especificaciones W3C y renderizado tipográfico de alta fidelidad. |
| **WebKit** | Apple Safari (macOS, iOS, iPadOS) | Alta eficiencia energética; comportamientos particulares en inputs de formularios (`-webkit-appearance`), viewport táctil y zoom automático. |

#### Estrategias Técnicas de Mitigación (Cross-Browser Testing):
1. **Normalización CSS:** Inclusión de reglas de reseteo (*CSS Reset* o *Normalize.css*) para unificar los márgenes, rellenos y tipografías predeterminadas por los agentes de usuario.
2. **Uso de Box-Sizing Universal:** La regla `* { box-sizing: border-box; }` asegura que el padding y los bordes no desborden el ancho calculado en ningún explorador.
3. **Verificación de Soporte en CanIUse.com:** Auditoría de características modernas como CSS Grid, Flexbox gap y funciones matemáticas (`clamp()`, `calc()`) confirmando más del 99% de compatibilidad global.
4. **Prefijos de Proveedor (*Vendor Prefixes*):** Aplicación de directivas como `-webkit-`, `-moz-` para propiedades emergentes o estilos de controles en dispositivos Apple.

---

### 2.3 ¿Cómo se ve una aplicación web en un explorador del celular?
La visualización en dispositivos móviles no es una simple reducción de escala de la versión de escritorio, sino una adaptación estructural regida por el paradigma **Mobile-First**:

1. **Etiqueta Meta Viewport Indispensable:**
   ```html
   <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
   ```
   Indica al motor del navegador móvil que la anchura del área visible debe coincidir exactamente con la resolución física del dispositivo (`width=device-width`), previniendo que el celular asuma un ancho de escritorio virtual (980 px) que obligue al usuario a hacer zoom manual.
2. **Puntos de Interrupción (*Media Queries*):**
   * *Smartphones (max-width: 640px):* Rejilla de productos en 1 columna, navegación colapsada en menú hamburguesa (☰), fuentes redimensionadas a escala legible (mínimo 15 px).
   * *Tablets (max-width: 900px):* Rejilla en 2 columnas, espaciados intermedios.
   * *Escritorio (min-width: 1200px):* Distribución en 2 paneles paralelos (Catálogo gastronómico y Checkout lateral).
3. **Ergonomía Táctil (*Touch Targets*):** De acuerdo con las pautas de accesibilidad **WCAG 2.1 (Criterio 2.5.5)**, los elementos accionables (botones, campos de texto, checkboxes) deben tener un tamaño objetivo mínimo de **48 &times; 48 píxeles**, con separación suficiente para evitar pulsaciones erróneas.
4. **Ausencia de Desbordamiento Horizontal:** Se comprueba que ningún contenedor exceda el 100% del ancho de la pantalla (`overflow-x: hidden`), garantizando desplazamiento vertical fluido y natural.

---

### 2.4 ¿Qué elementos se deben probar en una aplicación web?
Para declarar que un sistema publicado es operativo, se debe ejecutar una taxonomía integral de pruebas funcionales dividida en seis áreas críticas:

1. **Pruebas de Navegación y Enlaces (Hipervínculos):**
   * Verificación de que todos los enlaces del menú (`#preguntas-qa`, `#catalogo`, `#checkout`) desplacen suavemente hacia las secciones correspondientes.
   * Comprobación de que no existan enlaces rotos que desemboquen en errores HTTP 404 o 500.
2. **Pruebas de Formularios y Validación de Entradas:**
   * **Campos Requeridos:** Bloqueo de envíos con campos vacíos.
   * **Validación Regex de Celular Colombiano:** Restricción a 10 dígitos iniciando estrictamente por el dígito 3 (`^3\d{9}$`).
   * **Dirección de Popayán:** Longitud mínima y obligatoriedad para la logística de entrega.
   * **Prevención de Inyección de Código (XSS):** Saneamiento de cadenas en inputs de texto.
3. **Pruebas de Flujo Transaccional y Liquidación de Negocio:**
   * Selección dinámica de productos y actualización en tiempo real de subtotales.
   * **Liquidación del Impuesto Nacional al Consumo (8%):** Cálculo exacto según la Ley 1607 de 2012 y el Estatuto Tributario colombiano (ejemplo: Pizza Margherita de $38.000 COP genera exactamente $3.040 COP de impoconsumo, totalizando $41.040 COP).
   * Generación y despliegue del radicado transaccional oficial (`#PIZ-QA-2026-XXXX`).
4. **Pruebas de Cumplimiento Legal y Tratamiento de Datos:**
   * Verificación del checkbox mandatorio de consentimiento previo, informado y expreso para el tratamiento de datos personales conforme a la **Ley Estatutaria 1581 de 2012** y el **Decreto 1078 de 2015 del MinTIC**.
5. **Pruebas de Base de Datos e Integridad:**
   * Verificación de persistencia relacional en el motor **MySQL 8.0 (InnoDB)**.
   * Integridad referencial mediante claves foráneas y auditoría de transacciones.
6. **Pruebas de Rendimiento y Cabeceras de Seguridad:**
   * Latencia de carga de página inferior a 50 milisegundos en red local / pruebas.
   * Cabeceras de protección activas: `X-Frame-Options: SAMEORIGIN`, `X-Content-Type-Options: nosniff`.

---

## 3. PASO A PASO DEL DESPLIEGUE Y EVIDENCIA FOTOGRÁFICA EN KDE X11

A continuación se presentan las 6 capturas de pantalla de alta resolución obtenidas directamente en el entorno de escritorio **KDE X11** utilizando la herramienta de captura **Spectacle**, con ejecución de comandos en terminal **Konsole** y navegación en **Google Chrome**:

### 3.1 Paso 1: Verificación de Dominio y Diagnóstico DNS en Konsole
Ejecución del script `verificar_dominio_dns.sh` en terminal Konsole, demostrando la consulta autoritativa de registros NS, registros A (`185.27.134.148`), validación del certificado SSL Let's Encrypt con TLS 1.3 y respuesta HTTP 200:

![Verificación de Dominio y Diagnóstico DNS](capturas/paso_01_verificacion_dns_dominio_konsole.png)

### 3.2 Paso 2: Despliegue del Entorno de Pruebas en Contenedores Docker
Aprovisionamiento del entorno de pruebas funcionales mediante Docker Compose en Konsole, verificando los contenedores `sena-pruebas-funcionales-web` (puerto 8096) y `sena-pruebas-funcionales-db` (puerto 3311) en estado saludable (*healthy*) sin contaminar el host:

![Despliegue del Entorno en Docker](capturas/paso_02_despliegue_ambiente_pruebas_docker_konsole.png)

### 3.3 Paso 3: Suite Automatizada de Pruebas Funcionales E2E en Konsole
Ejecución de la suite automatizada `ejecutar_pruebas_funcionales_e2e.sh`, certificando el paso del 100% de las pruebas (5/5 PASS): código HTTP 200, meta viewport, catálogo en COP, formulario con Habeas Data y liquidación exacta del 8% de impoconsumo:

![Suite Automatizada de Pruebas Funcionales](capturas/paso_03_suite_pruebas_automatizadas_konsole.png)

### 3.4 Paso 4: Navegación de la Aplicación en Modo Escritorio en Google Chrome
Acceso a la plataforma web a través de Google Chrome en resolución completa de escritorio, visualizando el encabezado gourmet, la barra de diagnóstico de dominio, el panel de investigación de las 4 preguntas de la Guía 10 y el catálogo de especialidades:

![Vista de Escritorio en Google Chrome](capturas/paso_04_chrome_vista_escritorio_funcional.png)

### 3.5 Paso 5: Emulación de Dispositivo Móvil (Smartphone) en Chrome
Comprobación del comportamiento responsivo Mobile-First en Google Chrome ajustado a dimensiones de teléfono celular (412 &times; 915 px), evidenciando el menú colapsado en botón hamburguesa, touch targets táctiles y adaptación de tarjetas:

![Emulación Móvil en Google Chrome](capturas/paso_05_chrome_emulacion_movil_responsive.png)

### 3.6 Paso 6: Formulario de Checkout, Validaciones y Liquidación en COP
Interacción transaccional con el formulario de pedidos en Google Chrome, evidenciando las validaciones de campos requeridos, formato de teléfono colombiano (10 dígitos), consentimiento de Habeas Data y modal de confirmación con radicado de orden:

![Formulario de Checkout y Liquidación](capturas/paso_06_chrome_formulario_checkout_validaciones.png)

---

## 4. MATRIZ DE VERIFICACIÓN DE CRITERIOS DE EVALUACIÓN

| Num | Criterio de Evaluación (`IE-GA10-220501097-AA7-EV01`) | Estado | Mecanismo de Verificación y Evidencia Aportada |
| :---: | :--- | :---: | :--- |
| **1** | **Publica la aplicación de acuerdo con la plataforma de producción.** | **CUMPLE** | Publicación verificada bajo hosting tradicional cPanel Apache con dominio canónico `pizzeriabellaitalia-popayan.rf.gd` y transporte HTTPS. |
| **2** | **Realiza pruebas de funcionalidad del software para comprobar la operatividad.** | **CUMPLE** | Pruebas integrales de dominio, compatibilidad cross-browser, responsividad móvil, navegación, formularios y liquidación COP con 8% impoconsumo. |
| **3** | **Migra los datos según el plan.** | **CUMPLE** | Esquema de base de datos relacional MySQL 8.0 InnoDB persistiendo el catálogo gourmet y órdenes de prueba con claves foráneas. |
| **4** | **Realiza la configuración de usuarios en la plataforma de acuerdo con seguridad y privilegios.** | **CUMPLE** | Principio de menor privilegio (PoLP) con usuarios dedicados (`karen_admin`, `pizzeria_test_user`) y permisos Unix restrictivos 0755/0644. |

---

## 5. CONCLUSIONES Y RECOMENDACIONES TÉCNICAS

1. **Trascendencia del Testing en Producción:** Las pruebas funcionales en ambientes de producción o staging idénticos son indispensables para detectar anomalías de resolución DNS, incompatibilidades de certificados SSL o discrepancias visuales entre navegadores que no se manifiestan en desarrollo local.
2. **Prioridad del Diseño Responsivo (Mobile-First):** Dado que más del 70% del tráfico gastronómico en Colombia proviene de smartphones, la implementación rigurosa de la etiqueta `meta viewport` y touch targets de al menos 48 px es un factor crítico de éxito comercial.
3. **Rigurosidad Normativa y Tributaria:** La validación automática de expresiones regulares para celulares colombianos y la liquidación del Impuesto Nacional al Consumo (8%) otorgan certeza contable y blindaje legal al establecimiento.
4. **Recomendación para Futuras Fases:** Se aconseja incorporar herramientas de pruebas de rendimiento automatizadas como *Google Lighthouse* y pipelines de pruebas de regresión visual utilizando *Playwright* o *Cypress* en modo headless.

---

## 6. REFERENCIAS BIBLIOGRÁFICAS (NORMAS APA 7.ª EDICIÓN)

* Apache Software Foundation. (2024). *Apache HTTP Server Documentation (Version 2.4)*. https://httpd.apache.org/docs/2.4/
* Congreso de la República de Colombia. (2012). *Ley 1607 de 2012: Por la cual se expiden normas en materia tributaria y se dictan otras disposiciones (Impuesto Nacional al Consumo)*. Diario Oficial No. 48.655.
* Congreso de la República de Colombia. (2012). *Ley Estatutaria 1581 de 2012: Por la cual se dictan disposiciones generales para la protección de datos personales*. Diario Oficial No. 48.587.
* Internet Engineering Task Force (IETF). (2018). *The Transport Layer Security (TLS) Protocol Version 1.3 (RFC 8446)*. https://datatracker.ietf.org/doc/html/rfc8446
* Mozilla Developer Network (MDN). (2024). *Responsive design and CSS media queries*. MDN Web Docs. https://developer.mozilla.org/es/docs/Learn/CSS/CSS_layout/Responsive_Design
* MySQL AB & Oracle Corporation. (2024). *MySQL 8.0 Reference Manual*. Oracle Docs. https://dev.mysql.com/doc/refman/8.0/en/
* Servicio Nacional de Aprendizaje (SENA). (2024). *Componente Formativo: Publicación de aplicaciones tradicionales*. Programa de Tecnología en Análisis y Desarrollo de Software (ADSO), Dirección de Formación Profesional, Sistema Zajuna.
* World Wide Web Consortium (W3C). (2018). *Web Content Accessibility Guidelines (WCAG) 2.1: Target Size (Level AAA / Mobile Considerations)*. https://www.w3.org/TR/WCAG21/
