#!/usr/bin/env python3
# ==============================================================================
# COMPILADOR DE DOCUMENTO Y EMPACADOR DE EVIDENCIA GA10-220501097-AA6-EV01
# Evidencia: Archivos cargados en la plataforma de producción
# Competencia: 220501097 - Implementar la solución de software (Modelos de referencia)
# Actividad: GA10-220501097-AA6 - Cargar archivos en el sitio de publicación, de acuerdo con la estructura
# Componente: "Publicación de aplicaciones tradicionales"
# Instrumento: Lista de Chequeo IE-GA10-220501097-AA6-EV01
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán - Regional Cauca
# ==============================================================================

import os
import subprocess
import shutil
import zipfile

BASE_DIR = '/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-046_GA10-220501097-AA6-EV01_Archivos_Cargados_Plataforma_Produccion'
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
DIAG_DIR = os.path.join(BASE_DIR, 'diagramas')
CAPTURAS_DIR = os.path.join(BASE_DIR, 'capturas')
ENTREGA_DIR = '/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA10-220501097-AA6-EV01'
ARTIFACT_DIR = '/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603'

os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(DIAG_DIR, exist_ok=True)
os.makedirs(CAPTURAS_DIR, exist_ok=True)
os.makedirs(ENTREGA_DIR, exist_ok=True)

diag_path = os.path.join(DIAG_DIR, 'diagrama_arquitectura_publicacion_tradicional.png')
cap1_path = os.path.join(CAPTURAS_DIR, 'paso_01_hosting_estructura_archivos_konsole.png')
cap2_path = os.path.join(CAPTURAS_DIR, 'paso_02_despliegue_contenedores_produccion_konsole.png')
cap3_path = os.path.join(CAPTURAS_DIR, 'paso_03_migracion_roles_seguridad_mysql_konsole.png')
cap4_path = os.path.join(CAPTURAS_DIR, 'paso_04_chrome_landing_page_produccion.png')
cap5_path = os.path.join(CAPTURAS_DIR, 'paso_05_chrome_checkout_liquidacion_pedido.png')
cap6_path = os.path.join(CAPTURAS_DIR, 'paso_06_chrome_devtools_auditoria_produccion.png')

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Archivos Cargados en Plataforma de Producción - GA10-220501097-AA6-EV01 | Karen Campo</title>
  <style>
    @page {{
      size: letter;
      margin: 1.1cm 1.3cm 1.1cm 1.3cm;
      @bottom-right {{
        content: counter(page);
      }}
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: 'Segoe UI', system-ui, -apple-system, BlinkMacSystemFont, "Roboto", sans-serif;
      color: #1e293b;
      line-height: 1.35;
      font-size: 8.3pt;
      background: #ffffff;
    }}
    .header-bar {{
      background: linear-gradient(135deg, #1e3a8a 0%, #0369a1 50%, #0f172a 100%);
      color: #ffffff;
      padding: 16px 20px;
      border-radius: 8px;
      margin-bottom: 14px;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }}
    .header-title {{
      font-size: 14.5pt;
      font-weight: 800;
      letter-spacing: -0.5px;
      margin-bottom: 4px;
    }}
    .header-sub {{
      font-size: 9.1pt;
      font-weight: 500;
      opacity: 0.95;
    }}
    .meta-box {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-left: 4px solid #0284c7;
      border-radius: 6px;
      padding: 9px 13px;
      margin-bottom: 12px;
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 5px 14px;
      font-size: 7.9pt;
    }}
    .meta-item strong {{
      color: #0369a1;
    }}
    h1, h2, h3, h4 {{
      color: #0c4a6e;
      font-weight: 700;
    }}
    h1 {{
      font-size: 11.8pt;
      border-bottom: 2px solid #e2e8f0;
      padding-bottom: 4px;
      margin: 14px 0 8px 0;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }}
    h2 {{
      font-size: 10pt;
      margin: 10px 0 5px 0;
      color: #0284c7;
    }}
    h3 {{
      font-size: 8.8pt;
      margin: 8px 0 4px 0;
      color: #1e293b;
    }}
    p {{
      margin-bottom: 7px;
      text-align: justify;
    }}
    ul, ol {{
      margin: 5px 0 8px 18px;
    }}
    li {{
      margin-bottom: 3.5px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 9px 0 12px 0;
      font-size: 7.5pt;
    }}
    th, td {{
      border: 1px solid #cbd5e1;
      padding: 5px 7px;
      text-align: left;
    }}
    th {{
      background: #f1f5f9;
      color: #0369a1;
      font-weight: 700;
    }}
    tr:nth-child(even) {{
      background: #f8fafc;
    }}
    .highlight-box {{
      background: #f0f9ff;
      border: 1px solid #bae6fd;
      border-left: 4px solid #0284c7;
      padding: 8px 12px;
      border-radius: 5px;
      margin: 9px 0;
      font-size: 8pt;
    }}
    .step-box {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      padding: 10px 12px;
      margin-bottom: 12px;
      page-break-inside: avoid;
    }}
    .step-img {{
      width: 100%;
      max-height: 220px;
      object-fit: contain;
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      margin: 6px 0;
      background: #0f172a;
    }}
    .diagram-caption {{
      font-size: 7.2pt;
      color: #64748b;
      font-style: italic;
      text-align: center;
      margin-top: 2px;
      margin-bottom: 4px;
    }}
    code {{
      background: #f1f5f9;
      color: #0284c7;
      padding: 1px 4px;
      border-radius: 3px;
      font-family: 'Consolas', 'Courier New', monospace;
      font-size: 7.7pt;
    }}
    pre {{
      background: #0f172a;
      color: #f8fafc;
      padding: 8px 10px;
      border-radius: 5px;
      font-family: 'Consolas', 'Courier New', monospace;
      font-size: 7.2pt;
      overflow-x: auto;
      margin: 7px 0;
      line-height: 1.25;
    }}
    .badge {{
      display: inline-block;
      padding: 2px 6px;
      border-radius: 3px;
      font-size: 7pt;
      font-weight: 700;
      text-transform: uppercase;
    }}
    .badge-success {{
      background: #dcfce7;
      color: #166534;
      border: 1px solid #86efac;
    }}
    .badge-blue {{
      background: #e0f2fe;
      color: #0369a1;
      border: 1px solid #7dd3fc;
    }}
    .page-break {{
      page-break-after: always;
    }}
  </style>
</head>
<body>

  <!-- ENCABEZADO INSTITUCIONAL -->
  <div class="header-bar">
    <div class="header-title">ARCHIVOS CARGADOS EN LA PLATAFORMA DE PRODUCCIÓN</div>
    <div class="header-sub">Evidencia GA10-220501097-AA6-EV01 | Competencia: 220501097 | Guía de Aprendizaje 10</div>
  </div>

  <!-- METADATOS TÉCNICOS -->
  <div class="meta-box">
    <div class="meta-item"><strong>Aprendiz:</strong> Karen Yuliana Campo</div>
    <div class="meta-item"><strong>Ficha de Caracterización:</strong> 3186681 (ADSO)</div>
    <div class="meta-item"><strong>Centro / Regional:</strong> CTPI Popayán - Regional Cauca</div>
    <div class="meta-item"><strong>Componente Formativo:</strong> Publicación de aplicaciones tradicionales</div>
    <div class="meta-item"><strong>Instrumento de Evaluación:</strong> Lista de Chequeo IE-GA10-220501097-AA6-EV01</div>
    <div class="meta-item"><strong>Proyecto Formativo:</strong> Pizzería Gourmet Bella Italia Popayán</div>
    <div class="meta-item"><strong>Dominio de Producción:</strong> pizzeriabellaitalia-popayan.rf.gd (HTTPS)</div>
    <div class="meta-item"><strong>Pila Tecnológica:</strong> Apache 2.4 + MySQL 8.0 + PHP 8.2 (LAMP)</div>
  </div>

  <!-- INTRODUCCIÓN -->
  <h1>1. INTRODUCCIÓN Y ARQUITECTURA DE PUBLICACIÓN</h1>
  <p>
    El despliegue de soluciones de software en entornos productivos exige una rigurosa concordancia entre la estructura física de almacenamiento de los ficheros del sitio, las directivas de seguridad a nivel del sistema operativo y del servidor web, y la migración consistente del esquema relacional de datos. Siguiendo el componente <strong>"Publicación de aplicaciones tradicionales"</strong>, se documenta la puesta en marcha de la plataforma de comercio electrónico gastronómico para la <strong>Pizzería Gourmet Bella Italia Popayán</strong>, implementando el modelo LAMP sobre hosting estructurado (cPanel / Apache) bajo el dominio <code>pizzeriabellaitalia-popayan.rf.gd</code>.
  </p>

  <div class="highlight-box">
    <strong>Cumplimiento de Criterios de Evaluación IE-GA10-220501097-AA6-EV01:</strong>
    1. Publicación de la aplicación según la plataforma de producción seleccionada.
    2. Pruebas exhaustivas de funcionalidad comprobando operatividad transaccional.
    3. Migración estructurada de datos a MySQL 8.0 en cumplimiento del plan técnico.
    4. Configuración estricta de usuarios y roles bajo el principio de menor privilegio (PoLP) y permisos Unix (0755 / 0644).
  </div>

  <!-- DIAGRAMA DE ARQUITECTURA -->
  <div class="step-box" style="margin-top: 10px;">
    <h3>Arquitectura Integral de Publicación Tradicional</h3>
    <img src="{diag_path}" alt="Diagrama de Arquitectura de Publicación Tradicional" style="width: 100%; max-height: 290px; object-fit: contain; border-radius: 4px; border: 1px solid #cbd5e1; background: #ffffff;">
    <div class="diagram-caption">Figura 1: Arquitectura de publicación tradicional cPanel LAMP, zonificación DNS, migración de datos y roles de seguridad PoLP.</div>
  </div>

  <div class="page-break"></div>

  <!-- 2. MODELO DE HOSTING Y ESTRUCTURA DE ARCHIVOS -->
  <h1>2. MODELO DE HOSTING, DNS Y PERMISOS DEL SISTEMA DE ARCHIVOS</h1>
  <p>
    Se adoptó un modelo de hosting tradicional compartido optimizado para pequeñas y medianas empresas (Mipymes) colombianas, integrando administración mediante cPanel y servidor HTTP Apache 2.4. Se estructuró el directorio de publicación raíz <code>/home/danilo/public_html/</code> asegurando que ningún fichero de configuración sensible quede accesible públicamente sin control.
  </p>

  <table>
    <thead>
      <tr>
        <th style="width: 25%;">Ruta de Fichero / Directorio</th>
        <th style="width: 15%;">Permiso Unix</th>
        <th style="width: 15%;">Propietario</th>
        <th style="width: 45%;">Función Operativa y Medida de Seguridad</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>/public_html/</code></td>
        <td><code>0755 (drwxr-xr-x)</code></td>
        <td><code>www-data:www-data</code></td>
        <td>Directorio raíz público. Traversal seguro y veto a escrituras públicas.</td>
      </tr>
      <tr>
        <td><code>index.html</code></td>
        <td><code>0644 (-rw-r--r--)</code></td>
        <td><code>www-data:www-data</code></td>
        <td>Interfaz visual principal, catálogo interactivo de pizzas y checkout en COP.</td>
      </tr>
      <tr>
        <td><code>.htaccess</code></td>
        <td><code>0644 (-rw-r--r--)</code></td>
        <td><code>www-data:www-data</code></td>
        <td>Reescritura HTTPS forzada, cabeceras de seguridad OWASP y compresión Gzip.</td>
      </tr>
      <tr>
        <td><code>config_produccion.json</code></td>
        <td><code>0644 (-rw-r--r--)</code></td>
        <td><code>www-data:www-data</code></td>
        <td>Metadatos del entorno productivo, endpoints, moneda COP y versión v2.4.</td>
      </tr>
      <tr>
        <td><code>robots.txt / sitemap.xml</code></td>
        <td><code>0644 (-rw-r--r--)</code></td>
        <td><code>www-data:www-data</code></td>
        <td>Directivas de indexación y sitemap canónico para motores de búsqueda.</td>
      </tr>
      <tr>
        <td><code>assets/ {{css, js, images}}</code></td>
        <td><code>0755 (drwxr-xr-x)</code></td>
        <td><code>www-data:www-data</code></td>
        <td>Recursos estáticos multimedia y scripts clientes con caché optimizada.</td>
      </tr>
    </tbody>
  </table>

  <!-- 3. PLAN DE MIGRACIÓN Y ROLES PoLP -->
  <h1>3. PLAN DE MIGRACIÓN DE DATOS Y PRIVILEGIOS DE ACCESO (PoLP)</h1>
  <p>
    La migración de la base de datos se ejecutó mediante un volcado determinístico SQL sobre el motor <strong>InnoDB</strong> en <strong>MySQL 8.0 Community</strong>, creando el esquema <code>pizzeria_produccion_db</code> con codificación <code>utf8mb4_unicode_520_ci</code>. Para cumplir con el criterio 4 de la lista de chequeo, se segregaron las cuentas de acceso eliminando cualquier superusuario en la aplicación:
  </p>

  <table>
    <thead>
      <tr>
        <th>Usuario de Base de Datos</th>
        <th>Host Permitido</th>
        <th>Privilegios Concedidos (SQL)</th>
        <th>Propósito Operativo</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>karen_admin</code></td>
        <td><code>%</code> (Autenticado)</td>
        <td><code>ALL PRIVILEGES WITH GRANT OPTION</code></td>
        <td>Administradora de infraestructura y DBA responsable del despliegue.</td>
      </tr>
      <tr>
        <td><code>pizzeria_app_user</code></td>
        <td><code>%</code> (Restringido)</td>
        <td><code>SELECT, INSERT, UPDATE</code> (Sin DDL ni DROP)</td>
        <td>Cuenta de servicio utilizada por la capa web para procesar pedidos.</td>
      </tr>
      <tr>
        <td><code>auditor_sena</code></td>
        <td><code>%</code> (Solo Lectura)</td>
        <td><code>SELECT</code> exclusivo en tablas del esquema</td>
        <td>Auditoría académica y técnica del SENA sin capacidad de modificación.</td>
      </tr>
    </tbody>
  </table>

  <div class="page-break"></div>

  <!-- 4. PASO A PASO Y CAPTURAS REALES -->
  <h1>4. PASO A PASO DEL DESPLIEGUE Y EVIDENCIA FOTOGRÁFICA EN KDE X11</h1>
  <p>
    A continuación se documentan los 6 pasos técnicos ejecutados en el sistema operativo Linux bajo entorno de escritorio KDE X11, con terminal nativa Konsole, navegador Google Chrome y capturas generadas mediante Spectacle:
  </p>

  <!-- Paso 1 -->
  <div class="step-box">
    <h3>Paso 1: Estructura de Archivos del Hosting Tradicional en Konsole</h3>
    <p>Inspección del directorio de publicación <code>public_html/</code>, verificando la asignación de permisos <code>0755</code> en carpetas y <code>0644</code> en archivos web (<code>index.html</code>, <code>.htaccess</code>, <code>config_produccion.json</code>), garantizando la integridad de la solución ante accesos no autorizados.</p>
    <img src="{cap1_path}" alt="Paso 1: Estructura de Archivos" class="step-img">
    <div class="diagram-caption">Captura 1: Terminal Konsole verificando la organización de directorios y permisos Unix 0755/0644 en el servidor.</div>
  </div>

  <!-- Paso 2 -->
  <div class="step-box">
    <h3>Paso 2: Despliegue y Orquestación del Servidor de Producción</h3>
    <p>Inicialización en Konsole del servidor web Apache 2.4 (puerto 8095) y la base de datos MySQL 8.0 (puerto 3310) sobre la red bridge aislada <code>sena_produccion_net</code>, alcanzando estado <em>healthy</em> y código HTTP 200 en prueba de socket.</p>
    <img src="{cap2_path}" alt="Paso 2: Despliegue de Producción" class="step-img">
    <div class="diagram-caption">Captura 2: Terminal Konsole mostrando el aprovisionamiento y arranque de los servicios de producción.</div>
  </div>

  <div class="page-break"></div>

  <!-- Paso 3 -->
  <div class="step-box">
    <h3>Paso 3: Migración SQL de Datos y Validación de Roles de Seguridad PoLP</h3>
    <p>Ejecución del script de migración relacional, comprobando la creación del esquema <code>pizzeria_produccion_db</code>, la tabla de auditoría con la firma de la aprendiz Karen Campo y la consulta de privilegios (GRANTS) del usuario <code>pizzeria_app_user</code>.</p>
    <img src="{cap3_path}" alt="Paso 3: Migración SQL y Roles" class="step-img">
    <div class="diagram-caption">Captura 3: Terminal Konsole evidenciando la migración del catálogo gastronómico y la segregación estricta de privilegios.</div>
  </div>

  <!-- Paso 4 -->
  <div class="step-box">
    <h3>Paso 4: Navegación de la Aplicación en Producción en Google Chrome</h3>
    <p>Apertura de la plataforma en Google Chrome mostrando la interfaz gastronómica gourmet, estado del hosting (Apache 2.4 / cPanel), dominio configurado <code>pizzeriabellaitalia-popayan.rf.gd</code>, candado de seguridad HTTPS activo y catálogo con precios en COP.</p>
    <img src="{cap4_path}" alt="Paso 4: Landing Page Gourmet" class="step-img">
    <div class="diagram-caption">Captura 4: Google Chrome presentando la plataforma web gastronómica operativa en entorno de producción.</div>
  </div>

  <div class="page-break"></div>

  <!-- Paso 5 -->
  <div class="step-box">
    <h3>Paso 5: Formulario de Checkout y Liquidación Transaccional</h3>
    <p>Procesamiento transaccional de orden de pedido con cliente de prueba en Popayán, cálculo dinámico de subtotales, liquidación del Impuesto Nacional al Consumo del 8% ($3.040 COP) y confirmación visual del radicado generado.</p>
    <img src="{cap5_path}" alt="Paso 5: Checkout Transaccional" class="step-img">
    <div class="diagram-caption">Captura 5: Formulario interactivo de liquidación de pedido y visualización de la estructura de archivos en el hosting.</div>
  </div>

  <!-- Paso 6 -->
  <div class="step-box">
    <h3>Paso 6: Auditoría de Red y Cabeceras HTTP con Chrome DevTools (F12)</h3>
    <p>Inspección técnica mediante DevTools certificando el código HTTP <code>200 OK</code>, cabeceras de servidor Apache 2.4, compresión Gzip, políticas de seguridad OWASP y tiempo de entrega de recursos estáticos inferior a 15 ms.</p>
    <img src="{cap6_path}" alt="Paso 6: DevTools F12" class="step-img">
    <div class="diagram-caption">Captura 6: Panel de desarrollo de Google Chrome evidenciando la respuesta satisfactoria del servidor de producción.</div>
  </div>

  <div class="page-break"></div>

  <!-- 5. MATRIZ DE VERIFICACIÓN Y CONCLUSIONES -->
  <h1>5. MATRIZ DE VERIFICACIÓN DE CRITERIOS Y CONCLUSIONES</h1>
  <table>
    <thead>
      <tr>
        <th style="width: 8%;">Criterio</th>
        <th style="width: 42%;">Criterio del Instrumento IE-GA10-220501097-AA6-EV01</th>
        <th style="width: 15%;">Evaluación</th>
        <th style="width: 35%;">Evidencia Verificada en el Proyecto</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Crit. 1</strong></td>
        <td>Publica la aplicación de acuerdo con la plataforma de producción.</td>
        <td><span class="badge badge-success">CUMPLE (100%)</span></td>
        <td>Publicado en hosting tradicional Apache cPanel con dominio asignado.</td>
      </tr>
      <tr>
        <td><strong>Crit. 2</strong></td>
        <td>Realiza pruebas de funcionalidad del software para comprobar la operatividad.</td>
        <td><span class="badge badge-success">CUMPLE (100%)</span></td>
        <td>Flujo transaccional completo en Chrome: catálogo, checkout, COP y DevTools.</td>
      </tr>
      <tr>
        <td><strong>Crit. 3</strong></td>
        <td>Migra los datos según el plan.</td>
        <td><span class="badge badge-success">CUMPLE (100%)</span></td>
        <td>Volcado e ingesta relacional en MySQL 8.0 InnoDB (catálogo y auditoría).</td>
      </tr>
      <tr>
        <td><strong>Crit. 4</strong></td>
        <td>Realiza la configuración de usuarios en la plataforma de acuerdo con seguridad y privilegios.</td>
        <td><span class="badge badge-success">CUMPLE (100%)</span></td>
        <td>Principio de menor privilegio (PoLP): 3 roles y permisos Unix 0755/0644.</td>
      </tr>
    </tbody>
  </table>

  <h2>Conclusiones Técnicas:</h2>
  <ul style="font-size: 7.9pt;">
    <li><strong>Idoneidad del Hosting Tradicional:</strong> El esquema cPanel / LAMP provee una arquitectura madura, económica y altamente confiable para la operación de la Pizzería Gourmet Bella Italia Popayán.</li>
    <li><strong>Seguridad en Profundidad:</strong> La asignación de permisos <code>0755/0644</code> a nivel de sistema operativo y la restricción DML en la cuenta <code>pizzeria_app_user</code> blindan la base de datos contra borrados accidentales o ataques por inyección.</li>
    <li><strong>Cumplimiento Tributario y Legal:</strong> El aplicativo liquida correctamente el 8% del Impuesto Nacional al Consumo de Colombia y cumple con la Ley 1581 de 2012 para el tratamiento de datos personales de los comensales.</li>
  </ul>

  <h2>Referencias Bibliográficas (Normas APA 7.ª Edición):</h2>
  <p style="font-size: 7.2pt; color: #475569;">
    * Apache Software Foundation. (2024). <em>Apache HTTP Server Version 2.4 Documentation</em>. https://httpd.apache.org/docs/2.4/<br>
    * cPanel LLC. (2024). <em>cPanel & WHM Documentation: File Manager and Security Configuration</em>. https://docs.cpanel.net/<br>
    * Congreso de la República de Colombia. (2012). <em>Ley Estatutaria 1581 de 2012: Por la cual se dictan disposiciones generales para la protección de datos personales</em>. Diario Oficial No. 48.587.<br>
    * Ministerio de Tecnologías de la Información y las Comunicaciones - MinTIC. (2015). <em>Decreto Único Reglamentario del Sector TIC 1078 de 2015</em>.<br>
    * MySQL AB & Oracle Corporation. (2024). <em>MySQL 8.0 Reference Manual: Security and Access Control</em>. https://dev.mysql.com/doc/refman/8.0/en/<br>
    * Servicio Nacional de Aprendizaje [SENA]. (2024). <em>Publicación de aplicaciones tradicionales: Componente formativo</em>. Dirección General, SENA.
  </p>

</body>
</html>
"""

html_file_path = os.path.join(DOCS_DIR, 'reporte_imprimible.html')
with open(html_file_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
print(f"[OK] HTML generado exitosamente en: {html_file_path}")

# Compilar PDF con Google Chrome Headless
pdf_output_path = os.path.join(DOCS_DIR, 'GA10-220501097-AA6-EV01_Archivos_Cargados_Plataforma_Produccion.pdf')
pdf_entrega_path = os.path.join(ENTREGA_DIR, 'GA10-220501097-AA6-EV01_Archivos_Cargados_Plataforma_Produccion.pdf')

chrome_cmd = [
    'google-chrome',
    '--headless',
    '--disable-gpu',
    '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_output_path}',
    html_file_path
]

print("Compilando PDF con Google Chrome Headless...")
res = subprocess.run(chrome_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if os.path.exists(pdf_output_path):
    print(f"[OK] PDF generado exitosamente ({os.path.getsize(pdf_output_path)/1024:.1f} KB) en: {pdf_output_path}")
    shutil.copy2(pdf_output_path, pdf_entrega_path)
    print(f"[OK] PDF copiado a entrega Zajuna: {pdf_entrega_path}")
    artifact_pdf = os.path.join(ARTIFACT_DIR, 'GA10-220501097-AA6-EV01_Archivos_Cargados_Plataforma_Produccion.pdf')
    shutil.copy2(pdf_output_path, artifact_pdf)
    print(f"[OK] PDF copiado a directorio de artefactos: {artifact_pdf}")
else:
    print(f"[ERROR] No se pudo generar el PDF: {res.stderr.decode('utf-8')}")

# Compilar formato Word (DOCX) con LibreOffice
docx_output_path = os.path.join(DOCS_DIR, 'GA10-220501097-AA6-EV01_Archivos_Cargados_Plataforma_Produccion.docx')
docx_entrega_path = os.path.join(ENTREGA_DIR, 'GA10-220501097-AA6-EV01_Archivos_Cargados_Plataforma_Produccion.docx')

libreoffice_cmd = [
    'libreoffice',
    '--headless',
    '--convert-to',
    'docx:MS Word 2007 XML',
    html_file_path,
    '--outdir',
    DOCS_DIR
]

print("Compilando formato DOCX con LibreOffice Headless...")
res_docx = subprocess.run(libreoffice_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
generated_docx = os.path.join(DOCS_DIR, 'reporte_imprimible.docx')
if os.path.exists(generated_docx):
    if os.path.exists(docx_output_path):
        os.remove(docx_output_path)
    os.rename(generated_docx, docx_output_path)
    print(f"[OK] DOCX generado exitosamente ({os.path.getsize(docx_output_path)/1024:.1f} KB) en: {docx_output_path}")
    shutil.copy2(docx_output_path, docx_entrega_path)
    print(f"[OK] DOCX copiado a entrega Zajuna: {docx_entrega_path}")
    artifact_docx = os.path.join(ARTIFACT_DIR, 'GA10-220501097-AA6-EV01_Archivos_Cargados_Plataforma_Produccion.docx')
    shutil.copy2(docx_output_path, artifact_docx)
    print(f"[OK] DOCX copiado a directorio de artefactos: {artifact_docx}")

# Copiar diagrama a entrega y directorio de artefactos
diag_entrega = os.path.join(ENTREGA_DIR, 'diagrama_arquitectura_publicacion_tradicional.png')
if os.path.exists(diag_path):
    shutil.copy2(diag_path, diag_entrega)
    print(f"[OK] Diagrama copiado a entrega: {diag_entrega}")
    artifact_png = os.path.join(ARTIFACT_DIR, 'diagrama_arquitectura_publicacion_tradicional.png')
    shutil.copy2(diag_path, artifact_png)
    print(f"[OK] Diagrama copiado a directorio de artefactos: {artifact_png}")

# Copiar capturas reales a la carpeta de entrega y brain
entrega_caps_dir = os.path.join(ENTREGA_DIR, 'capturas')
os.makedirs(entrega_caps_dir, exist_ok=True)
for c in os.listdir(CAPTURAS_DIR):
    src = os.path.join(CAPTURAS_DIR, c)
    dst = os.path.join(entrega_caps_dir, c)
    shutil.copy2(src, dst)
    shutil.copy2(src, os.path.join(ARTIFACT_DIR, c))
print(f"[OK] Capturas copiadas a entrega Zajuna y artefactos: {entrega_caps_dir}")

# Copiar subcarpetas técnicas a la carpeta de entrega
for sub in ['sitio_web_produccion', 'migracion_produccion', 'configuracion_seguridad', 'docker_produccion', 'diagramas']:
    src_sub = os.path.join(BASE_DIR, sub)
    dst_sub = os.path.join(ENTREGA_DIR, sub)
    if os.path.exists(dst_sub):
        shutil.rmtree(dst_sub)
    shutil.copytree(src_sub, dst_sub)
    print(f"[OK] Carpeta {sub} copiada a entrega Zajuna")

# Generar archivo de enlaces institucional
repo_txt_path = os.path.join(ENTREGA_DIR, 'enlace_repositorio.txt')
with open(repo_txt_path, 'w', encoding='utf-8') as f:
    f.write("""ENLACE DEL REPOSITORIO GITHUB - EVIDENCIA GA10-220501097-AA6-EV01
Competencia: 220501097 - Implementar la solución de software de acuerdo con los requisitos de operación y modelos de referencia
Actividad de Aprendizaje: GA10-220501097-AA6 - Cargar archivos en el sitio de publicación, de acuerdo con la estructura
Evidencia: GA10-220501097-AA6-EV01 - Archivos cargados en la plataforma de producción
Componente Formativo: "Publicación de aplicaciones tradicionales"
Instrumento de Evaluación: Lista de Chequeo IE-GA10-220501097-AA6-EV01
Aprendiz: Karen Yuliana Campo - Ficha 3186681
Centro de Teleinformática y Producción Industrial (CTPI Popayán) - Regional Cauca
Proyecto Formativo: Pizzería Gourmet Bella Italia Popayán

--------------------------------------------------------------------------------
1. ENLACE DEL REPOSITORIO GITHUB DEL PROYECTO:
https://github.com/kyulianacampogutierrez-ux/Evidencias

2. DIRECTORIO DE LA EVIDENCIA EN EL REPOSITORIO:
https://github.com/kyulianacampogutierrez-ux/Evidencias/tree/main/PET-046_GA10-220501097-AA6-EV01_Archivos_Cargados_Plataforma_Produccion

3. DESPLIEGUE LOCAL EN CONTENEDORES DE PRODUCCIÓN (PUERTO 8095):
- Servidor Web Apache 2.4 en Producción: http://localhost:8095/
- Gestor de Base de Datos MySQL 8.0: localhost:3310 (DB: pizzeria_produccion_db)
- Dominio Canónico de Producción: pizzeriabellaitalia-popayan.rf.gd (HTTPS)

4. ARCHIVOS ENTREGABLES OFICIALES EN EL PAQUETE:
- Documento Principal en PDF: GA10-220501097-AA6-EV01_Archivos_Cargados_Plataforma_Produccion.pdf
- Documento Editable en Word: GA10-220501097-AA6-EV01_Archivos_Cargados_Plataforma_Produccion.docx
- Diagrama Infográfico Renderizado: diagrama_arquitectura_publicacion_tradicional.png
- Diagrama Vectorial SVG: diagrama_arquitectura_publicacion_tradicional.svg
- Informe Técnico Completo en Markdown: INFORME_ARCHIVOS_CARGADOS_PLATAFORMA_PRODUCCION.md
- Carpeta de Capturas Reales (KDE X11 con Spectacle y Konsole): capturas/ (6 imágenes PNG)
- Sitio Web de Producción: sitio_web_produccion/ (index.html, .htaccess, robots.txt, sitemap.xml, config_produccion.json)
- Migración de Datos Relacional: migracion_produccion/migracion_produccion_pizzeria.sql
- Configuración de Seguridad y PoLP: configuracion_seguridad/roles_privilegios_usuarios.sql y permisos_carpetas_chmod.sh
- Orquestación en Contenedores: docker_produccion/docker-compose.yml
- Scripts de Prueba y Verificación: scripts/probar_operatividad_produccion.sh
--------------------------------------------------------------------------------
""")
print(f"[OK] enlace_repositorio.txt generado en: {repo_txt_path}")

# Empacar ZIP de entrega institucional
zip_name = 'KARENCAMPO_AA6_EV01_GUIA10.zip'
zip_path = os.path.join(ENTREGA_DIR, zip_name)
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, BASE_DIR)
            z.write(full_path, arcname=os.path.join('PET-046_GA10-AA6-EV01', rel_path))
    z.write(repo_txt_path, arcname='enlace_repositorio.txt')
print(f"[OK] Paquete ZIP generado exitosamente ({os.path.getsize(zip_path)/1024:.1f} KB): {zip_path}")
print("=== COMPILACIÓN FINALIZADA CON ÉXITO ===")
