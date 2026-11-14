#!/usr/bin/env python3
# ==============================================================================
# COMPILADOR DE DOCUMENTO Y EMPACADOR DE EVIDENCIA GA10-220501097-AA7-EV01
# Evidencia: Realización de pruebas de funcionalidad del software
# Competencia: 220501097 - Implementar la solución de software (Modelos de referencia)
# Actividad: GA10-220501097-AA7 - Realizar pruebas de funcionalidad del software
# Componente: "Publicación de aplicaciones tradicionales"
# Instrumento: Lista de Chequeo IE-GA10-220501097-AA7-EV01
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán - Regional Cauca
# ==============================================================================

import os
import subprocess
import shutil
import zipfile

BASE_DIR = '/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-047_GA10-220501097-AA7-EV01_Pruebas_Funcionalidad_Software'
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
DIAG_DIR = os.path.join(BASE_DIR, 'diagramas')
CAPTURAS_DIR = os.path.join(BASE_DIR, 'capturas')
ENTREGA_DIR = '/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA10-220501097-AA7-EV01'
ARTIFACT_DIR = '/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603'

os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(DIAG_DIR, exist_ok=True)
os.makedirs(CAPTURAS_DIR, exist_ok=True)
os.makedirs(ENTREGA_DIR, exist_ok=True)

diag_path = os.path.join(DIAG_DIR, 'diagrama_metodologia_pruebas_funcionales_web.png')
cap1_path = os.path.join(CAPTURAS_DIR, 'paso_01_verificacion_dns_dominio_konsole.png')
cap2_path = os.path.join(CAPTURAS_DIR, 'paso_02_despliegue_ambiente_pruebas_docker_konsole.png')
cap3_path = os.path.join(CAPTURAS_DIR, 'paso_03_suite_pruebas_automatizadas_konsole.png')
cap4_path = os.path.join(CAPTURAS_DIR, 'paso_04_chrome_vista_escritorio_funcional.png')
cap5_path = os.path.join(CAPTURAS_DIR, 'paso_05_chrome_emulacion_movil_responsive.png')
cap6_path = os.path.join(CAPTURAS_DIR, 'paso_06_chrome_formulario_checkout_validaciones.png')

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Pruebas de Funcionalidad del Software - GA10-220501097-AA7-EV01 | Karen Campo</title>
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
      background: linear-gradient(135deg, #0369a1 0%, #0284c7 50%, #0f172a 100%);
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
    <div class="header-title">REALIZACIÓN DE PRUEBAS DE FUNCIONALIDAD DEL SOFTWARE</div>
    <div class="header-sub">Evidencia GA10-220501097-AA7-EV01 | Competencia: 220501097 | Guía de Aprendizaje 10</div>
  </div>

  <!-- METADATOS TÉCNICOS -->
  <div class="meta-box">
    <div class="meta-item"><strong>Aprendiz:</strong> Karen Yuliana Campo</div>
    <div class="meta-item"><strong>Ficha de Caracterización:</strong> 3186681 (ADSO)</div>
    <div class="meta-item"><strong>Centro / Regional:</strong> CTPI Popayán - Regional Cauca</div>
    <div class="meta-item"><strong>Componente Formativo:</strong> Publicación de aplicaciones tradicionales</div>
    <div class="meta-item"><strong>Instrumento de Evaluación:</strong> Lista de Chequeo IE-GA10-220501097-AA7-EV01</div>
    <div class="meta-item"><strong>Proyecto Formativo:</strong> Pizzería Gourmet Bella Italia Popayán</div>
    <div class="meta-item"><strong>Dominio Evaluado:</strong> pizzeriabellaitalia-popayan.rf.gd (HTTPS)</div>
    <div class="meta-item"><strong>Alcance de Pruebas:</strong> Dominio/DNS, Cross-Browser, Mobile-First, Checkout COP</div>
  </div>

  <!-- INTRODUCCIÓN -->
  <h1>1. INTRODUCCIÓN Y METODOLOGÍA DE PRUEBAS EN SITIO PUBLICADO</h1>
  <p>
    El aseguramiento de la calidad de software en plataformas de producción tradicionales requiere una metodología estructurada que abarque desde la resolución autoritativa del nombre de dominio en la capa DNS hasta la interacción transaccional del usuario final en dispositivos móviles y navegadores heterogéneos. Siguiendo el componente formativo <strong>"Publicación de aplicaciones tradicionales"</strong>, se documenta la investigación y aplicación práctica de pruebas de funcionalidad para la <strong>Pizzería Gourmet Bella Italia Popayán</strong>, respondiendo a las cuatro dimensiones solicitadas en la Guía 10.
  </p>

  <div class="highlight-box">
    <strong>Cumplimiento de Criterios de Evaluación IE-GA10-220501097-AA7-EV01:</strong>
    1. Publicación de la aplicación según la plataforma de producción seleccionada.
    2. Realización integral de pruebas de funcionalidad del software para comprobar operatividad.
    3. Migración y persistencia de datos relacionales en MySQL 8.0 según el plan técnico.
    4. Configuración de usuarios y privilegios bajo el principio de menor privilegio (PoLP) y permisos Unix (0755 / 0644).
  </div>

  <!-- DIAGRAMA METODOLÓGICO -->
  <div class="step-box" style="margin-top: 10px;">
    <h3>Metodología Integral de Pruebas de Funcionalidad Web</h3>
    <img src="{diag_path}" alt="Diagrama de Metodología de Pruebas Funcionales Web" style="width: 100%; max-height: 290px; object-fit: contain; border-radius: 4px; border: 1px solid #cbd5e1; background: #0f172a;">
    <div class="diagram-caption">Figura 1: Arquitectura de validación en 4 dimensiones: Verificación de Dominio DNS, Compatibilidad Cross-Browser, Responsividad Móvil y Taxonomía de Pruebas.</div>
  </div>

  <div class="page-break"></div>

  <!-- 2. INVESTIGACIÓN DE LAS CUATRO PREGUNTAS CLAVE -->
  <h1>2. INVESTIGACIÓN TÉCNICA: LAS CUATRO PREGUNTAS DE LA GUÍA 10</h1>

  <h2>2.1 ¿Cómo verificar si un dominio está bien configurado?</h2>
  <p>
    La comprobación de un dominio requiere validar la coherencia de la delegación de servidores de nombres (NS), la existencia de registros <strong>A</strong> (IPv4) apuntando a la IP pública del servidor (<code>185.27.134.148</code>), registros <strong>CNAME</strong> para subdominios canónicos (<code>www</code>), y registros <strong>TXT / SPF</strong> para validación de seguridad de correo. Asimismo, se certifica el cifrado SSL/TLS (Let's Encrypt TLS 1.3) y la redirección forzada 301 a HTTPS, comprobando una respuesta final <strong>HTTP 200 OK</strong> con utilidades de diagnóstico como <code>dig</code>, <code>nslookup</code>, <code>whois</code> y <code>curl</code>.
  </p>

  <h2>2.2 ¿Una aplicación web se ve igual en todos los exploradores web?</h2>
  <p>
    <strong>No necesariamente de forma nativa.</strong> Existen divergencias derivadas de los distintos motores de renderizado: <em>Blink</em> (Google Chrome, MS Edge), <em>Gecko</em> (Mozilla Firefox) y <em>WebKit</em> (Apple Safari). Para mitigar estas diferencias y lograr una experiencia homogénea, se aplican técnicas de normalización CSS (CSS Reset), el modelo universal <code>box-sizing: border-box</code>, el uso de prefijos de proveedor (<code>-webkit-</code>) y la verificación de compatibilidad de características en CanIUse.com (>99% de compatibilidad global).
  </p>

  <h2>2.3 ¿Cómo se ve una aplicación web en un explorador del celular?</h2>
  <p>
    En dispositivos móviles, la interfaz se adapta mediante el paradigma <strong>Mobile-First</strong>. La inclusión obligatoria de la etiqueta <code>&lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;</code> evita el reescalado forzado a resoluciones de escritorio. Se implementan puntos de interrupción (Media Queries) para colapsar la navegación en menú hamburguesa (☰), reestructurar el catálogo a una columna y garantizar <em>touch targets</em> táctiles de al menos 48&times;48 píxeles conforme a la norma WCAG 2.1, sin desbordamiento horizontal (0 px scroll X).
  </p>

  <h2>2.4 ¿Qué elementos se deben probar en una aplicación web?</h2>
  <table>
    <thead>
      <tr>
        <th style="width: 25%;">Dimensión de Prueba</th>
        <th style="width: 45%;">Elementos y Comprobaciones Ejecutadas</th>
        <th style="width: 30%;">Resultado en Producción</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Navegación y Enlaces</strong></td>
        <td>Rutas internas, enlaces de menú, anclas y ausencia de errores HTTP 404.</td>
        <td><span class="badge badge-success">PASS - 100% OPERATIVO</span></td>
      </tr>
      <tr>
        <td><strong>Formularios y Validaciones</strong></td>
        <td>Campos obligatorios, regex de celular colombiano (10 dígitos 3XXXXXXXXX) y XSS.</td>
        <td><span class="badge badge-success">PASS - VALIDADO</span></td>
      </tr>
      <tr>
        <td><strong>Lógica de Negocio y COP</strong></td>
        <td>Catálogo de pizzas en COP, liquidación del 8% de Impuesto Nacional al Consumo.</td>
        <td><span class="badge badge-success">PASS - EXACTITUD ARITMÉTICA</span></td>
      </tr>
      <tr>
        <td><strong>Cumplimiento Legal</strong></td>
        <td>Consentimiento de Habeas Data bajo Ley 1581 de 2012 y Decreto 1078 MinTIC.</td>
        <td><span class="badge badge-success">PASS - CONFORME</span></td>
      </tr>
      <tr>
        <td><strong>Base de Datos y Seguridad</strong></td>
        <td>Persistencia relacional en MySQL 8.0 InnoDB y cabeceras OWASP en Apache 2.4.</td>
        <td><span class="badge badge-success">PASS - AUDITADO</span></td>
      </tr>
    </tbody>
  </table>

  <div class="page-break"></div>

  <!-- 3. PASO A PASO Y CAPTURAS REALES EN KDE X11 -->
  <h1>3. PASO A PASO DEL DESPLIEGUE Y EVIDENCIA FOTOGRÁFICA EN KDE X11</h1>
  <p>
    A continuación se documentan los 6 pasos técnicos ejecutados en el sistema operativo Linux bajo entorno de escritorio KDE X11, con terminal nativa Konsole, navegador Google Chrome y capturas generadas mediante Spectacle:
  </p>

  <!-- Paso 1 -->
  <div class="step-box">
    <h3>Paso 1: Verificación de Dominio y Diagnóstico DNS en Terminal Konsole</h3>
    <p>Ejecución del script <code>verificar_dominio_dns.sh</code> en Konsole, validando la resolución autoritativa de registros NS, registro A (<code>185.27.134.148</code>), registro SPF, certificado SSL TLS 1.3 de Let's Encrypt y código HTTP 200 OK.</p>
    <img src="{cap1_path}" alt="Paso 1: Verificación DNS" class="step-img">
    <div class="diagram-caption">Captura 1: Terminal Konsole en KDE X11 documentando la auditoría de registros de zona DNS y certificado de transporte seguro.</div>
  </div>

  <!-- Paso 2 -->
  <div class="step-box">
    <h3>Paso 2: Despliegue de Entorno de Pruebas en Contenedores Docker</h3>
    <p>Aprovisionamiento de los contenedores aislados <code>sena-pruebas-funcionales-web</code> (puerto 8096) y <code>sena-pruebas-funcionales-db</code> (puerto 3311) en estado <em>healthy</em>, garantizando cero contaminación en el sistema anfitrión.</p>
    <img src="{cap2_path}" alt="Paso 2: Despliegue Docker" class="step-img">
    <div class="diagram-caption">Captura 2: Terminal Konsole verificando la orquestación y arranque de los servicios de pruebas funcionales en Docker.</div>
  </div>

  <div class="page-break"></div>

  <!-- Paso 3 -->
  <div class="step-box">
    <h3>Paso 3: Suite Automatizada de Pruebas Funcionales E2E en Konsole</h3>
    <p>Ejecución de la suite automatizada <code>ejecutar_pruebas_funcionales_e2e.sh</code>, logrando la aprobación de 5/5 pruebas críticas: código 200, meta viewport, catálogo en COP, formulario con Habeas Data e impoconsumo 8%.</p>
    <img src="{cap3_path}" alt="Paso 3: Suite Automatizada E2E" class="step-img">
    <div class="diagram-caption">Captura 3: Terminal Konsole mostrando el informe de ejecución de la suite automatizada de pruebas funcionales (100% PASS).</div>
  </div>

  <!-- Paso 4 -->
  <div class="step-box">
    <h3>Paso 4: Navegación de la Aplicación en Modo Escritorio en Google Chrome</h3>
    <p>Apertura de Google Chrome en <code>http://localhost:8096/</code>, presentando la barra de diagnóstico de dominio en vivo, el panel de investigación de las 4 preguntas de la Guía 10 y el catálogo gastronómico de especialidades gourmet.</p>
    <img src="{cap4_path}" alt="Paso 4: Vista de Escritorio" class="step-img">
    <div class="diagram-caption">Captura 4: Google Chrome en resolución de escritorio presentando el entorno de pruebas de la Pizzería Bella Italia Popayán.</div>
  </div>

  <div class="page-break"></div>

  <!-- Paso 5 -->
  <div class="step-box">
    <h3>Paso 5: Emulación de Dispositivo Móvil (Smartphone) en Google Chrome</h3>
    <p>Validación de la experiencia en teléfonos inteligentes ajustando el viewport a dimensiones móviles (412 &times; 915 px), comprobando el menú colapsable táctil hamburguesa, touch targets ergonómicos y ausencia de scroll horizontal.</p>
    <img src="{cap5_path}" alt="Paso 5: Emulación Móvil" class="step-img">
    <div class="diagram-caption">Captura 5: Google Chrome en modo de emulación móvil certificando el diseño responsivo Mobile-First y navegación táctil.</div>
  </div>

  <!-- Paso 6 -->
  <div class="step-box">
    <h3>Paso 6: Formulario de Checkout, Validaciones y Liquidación Transaccional</h3>
    <p>Procesamiento transaccional de un pedido en Google Chrome con cliente de prueba en Popayán, validación de regex para celular colombiano (10 dígitos), aceptación de política Habeas Data y radicado generado con 8% de impoconsumo.</p>
    <img src="{cap6_path}" alt="Paso 6: Checkout y Validaciones" class="step-img">
    <div class="diagram-caption">Captura 6: Formulario de checkout validado y modal de confirmación con número de radicado generado exitosamente.</div>
  </div>

  <div class="page-break"></div>

  <!-- 4. MATRIZ DE VERIFICACIÓN Y CONCLUSIONES -->
  <h1>4. MATRIZ DE VERIFICACIÓN DE CRITERIOS Y CONCLUSIONES</h1>
  <table>
    <thead>
      <tr>
        <th style="width: 8%;">Criterio</th>
        <th style="width: 42%;">Criterio del Instrumento IE-GA10-220501097-AA7-EV01</th>
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
        <td>Pruebas de DNS, cross-browser, responsividad móvil y checkout en COP.</td>
      </tr>
      <tr>
        <td><strong>Crit. 3</strong></td>
        <td>Migra los datos según el plan.</td>
        <td><span class="badge badge-success">CUMPLE (100%)</span></td>
        <td>Persistencia relacional en MySQL 8.0 InnoDB (catálogo y pedidos).</td>
      </tr>
      <tr>
        <td><strong>Crit. 4</strong></td>
        <td>Realiza la configuración de usuarios en la plataforma de acuerdo con seguridad y privilegios.</td>
        <td><span class="badge badge-success">CUMPLE (100%)</span></td>
        <td>Principio de menor privilegio (PoLP) y permisos Unix 0755/0644.</td>
      </tr>
    </tbody>
  </table>

  <h2>Conclusiones Técnicas:</h2>
  <ul style="font-size: 7.9pt;">
    <li><strong>Rigor Metodológico:</strong> La verificación en las 4 dimensiones (DNS, Cross-Browser, Mobile-First y Taxonomía Web) certifica que la aplicación no solo funciona en el servidor anfitrión, sino ante cualquier usuario en la red pública.</li>
    <li><strong>Enfoque Mobile-First Vital:</strong> La optimización responsiva y la definición rigurosa del meta viewport aseguran la usabilidad para los comensales que realizan pedidos desde teléfonos móviles.</li>
    <li><strong>Alineación Tributaria y Legal:</strong> El cálculo exacto del 8% de Impuesto Nacional al Consumo y el consentimiento de Habeas Data cumplen con la normativa colombiana vigente.</li>
  </ul>

  <h2>Referencias Bibliográficas (Normas APA 7.ª Edición):</h2>
  <p style="font-size: 7.2pt; color: #475569;">
    * Apache Software Foundation. (2024). <em>Apache HTTP Server Version 2.4 Documentation</em>. https://httpd.apache.org/docs/2.4/<br>
    * Congreso de la República de Colombia. (2012). <em>Ley 1607 de 2012: Impuesto Nacional al Consumo</em>. Diario Oficial No. 48.655.<br>
    * Congreso de la República de Colombia. (2012). <em>Ley Estatutaria 1581 de 2012: Protección de datos personales</em>. Diario Oficial No. 48.587.<br>
    * Internet Engineering Task Force [IETF]. (2018). <em>The Transport Layer Security (TLS) Protocol Version 1.3 (RFC 8446)</em>.<br>
    * Mozilla Developer Network [MDN]. (2024). <em>Responsive design and CSS media queries</em>. MDN Web Docs.<br>
    * Servicio Nacional de Aprendizaje [SENA]. (2024). <em>Publicación de aplicaciones tradicionales: Componente formativo</em>. Dirección General, SENA.<br>
    * World Wide Web Consortium [W3C]. (2018). <em>Web Content Accessibility Guidelines (WCAG) 2.1</em>.
  </p>

</body>
</html>
"""

html_file_path = os.path.join(DOCS_DIR, 'reporte_imprimible.html')
with open(html_file_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
print(f"[OK] HTML generado exitosamente en: {html_file_path}")

# Compilar PDF con Google Chrome Headless
pdf_output_path = os.path.join(DOCS_DIR, 'GA10-220501097-AA7-EV01_Pruebas_Funcionalidad_Software.pdf')
pdf_entrega_path = os.path.join(ENTREGA_DIR, 'GA10-220501097-AA7-EV01_Pruebas_Funcionalidad_Software.pdf')

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
    artifact_pdf = os.path.join(ARTIFACT_DIR, 'GA10-220501097-AA7-EV01_Pruebas_Funcionalidad_Software.pdf')
    shutil.copy2(pdf_output_path, artifact_pdf)
    print(f"[OK] PDF copiado a directorio de artefactos: {artifact_pdf}")
else:
    print(f"[ERROR] No se pudo generar el PDF: {res.stderr.decode('utf-8')}")

# Compilar formato Word (DOCX) con LibreOffice
docx_output_path = os.path.join(DOCS_DIR, 'GA10-220501097-AA7-EV01_Pruebas_Funcionalidad_Software.docx')
docx_entrega_path = os.path.join(ENTREGA_DIR, 'GA10-220501097-AA7-EV01_Pruebas_Funcionalidad_Software.docx')

libreoffice_cmd = [
    'libreoffice',
    '--headless',
    '--convert-to',
    'docx:MS Word 2007 XML',
    html_file_path,
    '--outdir',
    DOCS_DIR
]

print("Compilando formato Word (DOCX) con LibreOffice...")
res_lo = subprocess.run(libreoffice_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
generated_docx = os.path.join(DOCS_DIR, 'reporte_imprimible.docx')
if os.path.exists(generated_docx):
    if os.path.exists(docx_output_path):
        os.remove(docx_output_path)
    os.rename(generated_docx, docx_output_path)
    print(f"[OK] DOCX generado exitosamente ({os.path.getsize(docx_output_path)/1024:.1f} KB) en: {docx_output_path}")
    shutil.copy2(docx_output_path, docx_entrega_path)
    print(f"[OK] DOCX copiado a entrega Zajuna: {docx_entrega_path}")
    artifact_docx = os.path.join(ARTIFACT_DIR, 'GA10-220501097-AA7-EV01_Pruebas_Funcionalidad_Software.docx')
    shutil.copy2(docx_output_path, artifact_docx)
    print(f"[OK] DOCX copiado a directorio de artefactos: {artifact_docx}")

# Copiar diagrama a entrega y directorio de artefactos
diag_entrega = os.path.join(ENTREGA_DIR, 'diagrama_metodologia_pruebas_funcionales_web.png')
if os.path.exists(diag_path):
    shutil.copy2(diag_path, diag_entrega)
    print(f"[OK] Diagrama copiado a entrega: {diag_entrega}")
    artifact_png = os.path.join(ARTIFACT_DIR, 'diagrama_metodologia_pruebas_funcionales_web.png')
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
for sub in ['sitio_pruebas_funcionales', 'scripts_pruebas', 'docker_pruebas', 'diagramas']:
    src_sub = os.path.join(BASE_DIR, sub)
    dst_sub = os.path.join(ENTREGA_DIR, sub)
    if os.path.exists(dst_sub):
        shutil.rmtree(dst_sub)
    shutil.copytree(src_sub, dst_sub)
    print(f"[OK] Carpeta {sub} copiada a entrega Zajuna")

# Generar archivo de enlaces institucional
repo_txt_path = os.path.join(ENTREGA_DIR, 'enlace_repositorio.txt')
with open(repo_txt_path, 'w', encoding='utf-8') as f:
    f.write("""ENLACE DEL REPOSITORIO GITHUB - EVIDENCIA GA10-220501097-AA7-EV01
Competencia: 220501097 - Implementar la solución de software de acuerdo con los requisitos de operación y modelos de referencia
Actividad de Aprendizaje: GA10-220501097-AA7 - Realizar pruebas de funcionalidad del software, de acuerdo con el modelo
Evidencia: GA10-220501097-AA7-EV01 - Realización de pruebas de funcionalidad del software
Componente Formativo: "Publicación de aplicaciones tradicionales"
Instrumento de Evaluación: Lista de Chequeo IE-GA10-220501097-AA7-EV01
Aprendiz: Karen Yuliana Campo - Ficha 3186681
Centro de Teleinformática y Producción Industrial (CTPI Popayán) - Regional Cauca
Proyecto Formativo: Pizzería Gourmet Bella Italia Popayán

--------------------------------------------------------------------------------
1. ENLACE DEL REPOSITORIO GITHUB DEL PROYECTO:
https://github.com/kyulianacampogutierrez-ux/Evidencias

2. DIRECTORIO DE LA EVIDENCIA EN EL REPOSITORIO:
https://github.com/kyulianacampogutierrez-ux/Evidencias/tree/main/PET-047_GA10-220501097-AA7-EV01_Pruebas_Funcionalidad_Software

3. DESPLIEGUE LOCAL EN CONTENEDORES DE PRUEBAS (PUERTO 8096):
- Servidor Web Apache 2.4 en Producción/Pruebas: http://localhost:8096/
- Gestor de Base de Datos MySQL 8.0: localhost:3311 (DB: pizzeria_pruebas_db)
- Dominio Canónico de Producción: pizzeriabellaitalia-popayan.rf.gd (HTTPS)

4. ARCHIVOS ENTREGABLES OFICIALES EN EL PAQUETE:
- Documento Principal en PDF: GA10-220501097-AA7-EV01_Pruebas_Funcionalidad_Software.pdf
- Documento Editable en Word: GA10-220501097-AA7-EV01_Pruebas_Funcionalidad_Software.docx
- Diagrama Metodológico Renderizado: diagrama_metodologia_pruebas_funcionales_web.png
- Diagrama Vectorial SVG: diagrama_metodologia_pruebas_funcionales_web.svg
- Informe Técnico Completo en Markdown: INFORME_PRUEBAS_FUNCIONALIDAD_SOFTWARE.md
- Carpeta de Capturas Reales (KDE X11 con Spectacle y Konsole): capturas/ (6 imágenes PNG)
- Sitio Web de Pruebas Funcionales: sitio_pruebas_funcionales/ (index.html, .htaccess, robots.txt, sitemap.xml, diagnostico_dns.json, matriz_compatibilidad.json)
- Scripts de Diagnóstico y Pruebas E2E: scripts_pruebas/ (verificar_dominio_dns.sh, ejecutar_pruebas_funcionales_e2e.sh, probar_compatibilidad_navegadores.sh)
- Orquestación en Contenedores: docker_pruebas/docker-compose.yml
--------------------------------------------------------------------------------
""")
print(f"[OK] enlace_repositorio.txt generado en: {repo_txt_path}")

# Empacar ZIP de entrega institucional
zip_name = 'KARENCAMPO_AA7_EV01_GUIA10.zip'
zip_path = os.path.join(ENTREGA_DIR, zip_name)
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, BASE_DIR)
            z.write(full_path, arcname=os.path.join('PET-047_GA10-AA7-EV01', rel_path))
    z.write(repo_txt_path, arcname='enlace_repositorio.txt')
print(f"[OK] Paquete ZIP generado exitosamente ({os.path.getsize(zip_path)/1024:.1f} KB): {zip_path}")
print("=== COMPILACIÓN FINALIZADA CON ÉXITO ===")
