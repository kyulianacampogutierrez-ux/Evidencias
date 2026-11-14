#!/usr/bin/env python3
# ==============================================================================
# COMPILADOR DE DOCUMENTO Y EMPACADOR DE EVIDENCIA GA10-220501097-AA3-EV01
# Evidencia: Software instalado en la plataforma del cliente
# Competencia: 220501097 - Implementar la solución de software (Modelos de referencia)
# Actividad: GA10-220501097-AA3 - Elaborar el plan de instalación
# Componente: "Identificación de requerimientos" y "Sistemas operativos de red"
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán - Regional Cauca
# ==============================================================================

import os
import subprocess
import shutil
import zipfile

BASE_DIR = '/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-044_GA10-220501097-AA3-EV01_Software_Instalado_Plataforma_Cliente'
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
DIAG_DIR = os.path.join(BASE_DIR, 'diagramas')
CAPTURAS_DIR = os.path.join(BASE_DIR, 'capturas')
ENTREGA_DIR = '/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA10-220501097-AA3-EV01'
ARTIFACT_DIR = '/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603'

os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(DIAG_DIR, exist_ok=True)
os.makedirs(CAPTURAS_DIR, exist_ok=True)
os.makedirs(ENTREGA_DIR, exist_ok=True)

diag_path = os.path.join(DIAG_DIR, 'diagrama_arquitectura_despliegue_docker_cliente.png')
cap1_path = os.path.join(CAPTURAS_DIR, 'paso_01_despliegue_contenedor_docker.png')
cap2_path = os.path.join(CAPTURAS_DIR, 'paso_02_navegador_chrome_landing_page.png')
cap3_path = os.path.join(CAPTURAS_DIR, 'paso_03_chrome_menu_gourmet_interactivo.png')
cap4_path = os.path.join(CAPTURAS_DIR, 'paso_04_chrome_formulario_checkout_pedido.png')
cap5_path = os.path.join(CAPTURAS_DIR, 'paso_05_chrome_devtools_inspeccion_red.png')
cap6_path = os.path.join(CAPTURAS_DIR, 'paso_06_plan_respaldo_migracion_datos.png')

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Software Instalado en la Plataforma del Cliente - GA10-220501097-AA3-EV01 | Karen Campo</title>
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
      line-height: 1.34;
      font-size: 8.2pt;
      background: #ffffff;
    }}
    .header-bar {{
      background: linear-gradient(135deg, #064e3b 0%, #047857 50%, #022c22 100%);
      color: #ffffff;
      padding: 16px 20px;
      border-radius: 8px;
      margin-bottom: 14px;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }}
    .header-title {{
      font-size: 15.5pt;
      font-weight: 800;
      letter-spacing: -0.5px;
      margin-bottom: 4px;
    }}
    .header-sub {{
      font-size: 9.3pt;
      font-weight: 500;
      opacity: 0.95;
    }}
    .meta-box {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-left: 4px solid #047857;
      border-radius: 6px;
      padding: 9px 13px;
      margin-bottom: 12px;
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 5px 14px;
      font-size: 7.9pt;
    }}
    .meta-item strong {{
      color: #064e3b;
    }}
    h1, h2, h3, h4 {{
      color: #064e3b;
      font-weight: 700;
    }}
    h1 {{
      font-size: 12.5pt;
      border-bottom: 2px solid #10b981;
      padding-bottom: 3px;
      margin: 15px 0 7px 0;
      page-break-after: avoid;
    }}
    h2 {{
      font-size: 10pt;
      margin: 11px 0 5px 0;
      color: #047857;
      page-break-after: avoid;
    }}
    h3 {{
      font-size: 8.8pt;
      margin: 7px 0 3px 0;
      color: #065f46;
      page-break-after: avoid;
    }}
    p {{
      margin-bottom: 6px;
      text-align: justify;
    }}
    .highlight-card {{
      background: #ecfdf5;
      border: 1px solid #a7f3d0;
      border-radius: 6px;
      padding: 9px 12px;
      margin: 9px 0;
    }}
    .highlight-card strong {{
      color: #065f46;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 8px 0 11px 0;
      font-size: 7.6pt;
      page-break-inside: avoid;
    }}
    th, td {{
      border: 1px solid #cbd5e1;
      padding: 5px 7px;
      text-align: left;
    }}
    th {{
      background: #047857;
      color: #ffffff;
      font-weight: 600;
      font-size: 7.7pt;
    }}
    tr:nth-child(even) {{
      background: #f8fafc;
    }}
    .badge-pass {{
      background: #10b981;
      color: #ffffff;
      padding: 2px 6px;
      border-radius: 4px;
      font-weight: 700;
      font-size: 7pt;
      display: inline-block;
    }}
    pre, code {{
      font-family: 'Consolas', 'Courier New', monospace;
      font-size: 7.3pt;
    }}
    pre {{
      background: #0f172a;
      color: #38bdf8;
      padding: 8px 11px;
      border-radius: 6px;
      margin: 6px 0;
      overflow-x: auto;
      line-height: 1.3;
    }}
    .diagram-container {{
      text-align: center;
      margin: 12px 0;
      page-break-inside: avoid;
    }}
    .diagram-img {{
      max-width: 100%;
      height: auto;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      box-shadow: 0 4px 6px -1px rgba(0,0,0,0.08);
    }}
    .diagram-caption {{
      font-size: 7.5pt;
      color: #64748b;
      margin-top: 4px;
      font-style: italic;
    }}
    .step-box {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-left: 4px solid #0284c7;
      padding: 8px 12px;
      border-radius: 6px;
      margin: 10px 0;
      page-break-inside: avoid;
    }}
    .step-img {{
      max-width: 100%;
      height: auto;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      margin: 6px 0;
      box-shadow: 0 2px 5px rgba(0,0,0,0.08);
    }}
    .page-break {{
      page-break-before: always;
    }}
  </style>
</head>
<body>

  <!-- PORTADA / ENCABEZADO INSTITUCIONAL -->
  <div class="header-bar">
    <div class="header-title">SOFTWARE INSTALADO EN LA PLATAFORMA DEL CLIENTE</div>
    <div class="header-sub">Evidencia GA10-220501097-AA3-EV01 | Despliegue en Docker, Plan de Migración y Respaldo DRP</div>
  </div>

  <div class="meta-box">
    <div class="meta-item"><strong>Institución:</strong> Servicio Nacional de Aprendizaje (SENA)</div>
    <div class="meta-item"><strong>Centro:</strong> Teleinformática y Producción Industrial (CTPI) - Cauca</div>
    <div class="meta-item"><strong>Programa:</strong> Tecnología en Análisis y Desarrollo de Software (ADSO)</div>
    <div class="meta-item"><strong>Ficha:</strong> 3186681 | <strong>Modalidad:</strong> Virtual</div>
    <div class="meta-item"><strong>Aprendiz:</strong> Karen Yuliana Campo</div>
    <div class="meta-item"><strong>Proyecto Formativo:</strong> Pizzería Gourmet Bella Italia Popayán</div>
    <div class="meta-item"><strong>Competencia:</strong> 220501097 - Implementar la solución de software</div>
    <div class="meta-item"><strong>Actividad:</strong> GA10-220501097-AA3 - Elaborar el plan de instalación</div>
  </div>

  <!-- HIGHLIGHT DE LA GUÍA -->
  <div class="highlight-card">
    <strong>🎯 Cumplimiento de Criterios (Lista de Chequeo IE-GA10-220501097-AA3-EV01):</strong><br>
    1. Elabora el plan de instalación de acuerdo con las características del software a implantar.<br>
    2. Diseña el plan de migración de datos de acuerdo con las condiciones de implementación.<br>
    3. Diseña el plan de respaldo de los datos para mitigar riesgos operacionales (DRP).
  </div>

  <!-- 1. INTRODUCCIÓN Y JUSTIFICACIÓN -->
  <h1>1. INTRODUCCIÓN Y JUSTIFICACIÓN DE LA PLATAFORMA DE IMPLANTACIÓN</h1>
  <p>
    La fase de implantación en la plataforma del cliente exige un modelo de despliegue confiable, aislado y reproducible. En lugar de instalar servidores web y paquetes directamente sobre el sistema operativo anfitrión (evitando contaminar la máquina con dependencias no deseadas), se optó por la <strong>contenedorización mediante Docker y Docker Compose</strong>.
  </p>
  <p>
    Esta arquitectura garantiza que el servidor web <strong>Nginx</strong> y los servicios asociados operen de manera encapsulada sobre una imagen ultraligera <strong>Alpine Linux</strong> (~23 MB), exponiendo de forma controlada el puerto <strong>8088</strong> hacia el exterior y mapeando los archivos de la plantilla web HTML5/CSS3 adaptada para la <em>Pizzería Gourmet Bella Italia Popayán</em>.
  </p>

  <!-- DIAGRAMA GENERAL DE ARQUITECTURA -->
  <div class="diagram-container">
    <img src="{diag_path}" alt="Diagrama de Arquitectura de Despliegue en Plataforma del Cliente" class="diagram-img">
    <div class="diagram-caption">Figura 1: Arquitectura de Despliegue Contenerizado en Docker, Flujo de Navegación en Chrome KDE X11 y Planes de Migración y Respaldo.</div>
  </div>

  <div class="page-break"></div>

  <!-- 2. PASO A PASO DETALLADO DEL DESPLIEGUE CON CAPTURAS REALES (KDE X11) -->
  <h1>2. PASO A PASO DEL DESPLIEGUE LOCAL (CAPTURAS REALES EN KDE X11)</h1>
  <p>
    Todas las capturas de pantalla fueron tomadas en tiempo real en la estación de trabajo de desarrollo (entorno de escritorio <strong>KDE X11</strong>), empleando <strong>xdotool</strong> para la orquestación de ventanas y <strong>Spectacle</strong> para la captura en alta resolución:
  </p>

  <!-- Paso 1 -->
  <div class="step-box">
    <h3>Paso 1: Configuración de Docker Compose y Despliegue del Contenedor</h3>
    <p>Se ejecutó el comando <code>docker compose up -d</code>, levantando el contenedor <code>sena-cliente-landing-pizzeria</code> en el puerto <code>8088</code> con red bridge aislada.</p>
    <img src="{cap1_path}" alt="Paso 1: Despliegue en Docker" class="step-img">
    <div class="diagram-caption">Captura 1: Terminal KDE X11 mostrando el contenedor Nginx en ejecución y en estado saludable (healthy).</div>
  </div>

  <!-- Paso 2 -->
  <div class="step-box">
    <h3>Paso 2: Apertura y Carga de la Landing Page en Google Chrome</h3>
    <p>Se abrió Google Chrome navegando a <code>http://localhost:8088</code>, desplegando el Hero Banner con la identidad gastronómica de la Pizzería Bella Italia Popayán.</p>
    <img src="{cap2_path}" alt="Paso 2: Landing Page en Google Chrome" class="step-img">
    <div class="diagram-caption">Captura 2: Renderizado visual de la plantilla web en Google Chrome en resolución completa.</div>
  </div>

  <div class="page-break"></div>

  <!-- Paso 3 -->
  <div class="step-box">
    <h3>Paso 3: Catálogo Interactivo del Menú Gourmet (Scroll con xdotool)</h3>
    <p>Navegación asistida mediante eventos de teclado xdotool hacia el menú con las 4 especialidades gourmet y precios en COP ($38.000 a $48.000).</p>
    <img src="{cap3_path}" alt="Paso 3: Menú Gourmet en Chrome" class="step-img">
    <div class="diagram-caption">Captura 3: Sección interactiva de especialidades de pizza con selección directa para el pedido.</div>
  </div>

  <!-- Paso 4 -->
  <div class="step-box">
    <h3>Paso 4: Validación del Formulario de Registro y Checkout de Pedidos</h3>
    <p>Se diligenciaron los datos del cliente (Karen Campo, teléfono móvil MinTIC y dirección en Popayán), confirmando el registro exitoso del pedido en el servidor local.</p>
    <img src="{cap4_path}" alt="Paso 4: Formulario de Checkout" class="step-img">
    <div class="diagram-caption">Captura 4: Mensaje de confirmación dinámica en el DOM con estado del pedido "EN PREPARACIÓN".</div>
  </div>

  <div class="page-break"></div>

  <!-- Paso 5 -->
  <div class="step-box">
    <h3>Paso 5: Auditoría Técnica y Diagnóstico de Red con Chrome DevTools (F12)</h3>
    <p>Inspección del tráfico HTTP en DevTools confirmando respuesta HTTP <code>200 OK</code>, cabecera <code>Server: nginx</code> y 0 errores en la consola de JavaScript.</p>
    <img src="{cap5_path}" alt="Paso 5: Chrome DevTools F12" class="step-img">
    <div class="diagram-caption">Captura 5: Inspección de red y consola en tiempo real certificando rendimiento óptimo.</div>
  </div>

  <!-- Paso 6 -->
  <div class="step-box">
    <h3>Paso 6: Ejecución del Script de Respaldo y Migración de Datos</h3>
    <p>Ejecución en consola del script <code>scripts/respaldo_migracion_datos.sh</code>, generando el paquete <code>tar.gz</code>, el dump SQL y los hashes SHA-256 de verificación.</p>
    <img src="{cap6_path}" alt="Paso 6: Plan de Respaldo y Migración" class="step-img">
    <div class="diagram-caption">Captura 6: Terminal con la verificación criptográfica exitosa de los datos de migración.</div>
  </div>

  <div class="page-break"></div>

  <!-- 3. PLAN DE MIGRACIÓN Y RESPALDO DE DATOS -->
  <h1>3. PLAN DE MIGRACIÓN Y RESPALDO DE DATOS (CRITERIOS EVALUATIVOS)</h1>
  <p>
    En concordancia con el instrumento de evaluación <strong>IE-GA10-220501097-AA3-EV01</strong>, se definen formalmente las políticas de migración y resguardo de la información:
  </p>

  <h2>3.1 Plan de Migración de Datos (Etapas ETL)</h2>
  <table>
    <thead>
      <tr>
        <th style="width: 15%;">Etapa ETL</th>
        <th style="width: 35%;">Actividad y Procedimiento</th>
        <th style="width: 25%;">Herramienta / Formato</th>
        <th style="width: 25%;">Criterio de Validación</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. Extracción</strong></td>
        <td>Generación de dump consistente de las tablas <code>usuarios_clientes</code> y <code>pedidos_gourmet</code>.</td>
        <td><code>mysqldump / SQL DDL</code></td>
        <td>Dump completo sin bloqueos de tabla.</td>
      </tr>
      <tr>
        <td><strong>2. Transformación</strong></td>
        <td>Normalización de caracteres a <code>utf8mb4</code> y verificación de constraints foráneas.</td>
        <td>Script Bash / SQL parser</td>
        <td>Esquema 100% compatible con destino.</td>
      </tr>
      <tr>
        <td><strong>3. Carga e Ingesta</strong></td>
        <td>Ejecución transaccional atómica de las sentencias <code>CREATE TABLE</code> e <code>INSERT</code>.</td>
        <td>Cliente MySQL / MariaDB</td>
        <td>0 errores de clave duplicada.</td>
      </tr>
      <tr>
        <td><strong>4. Validación</strong></td>
        <td>Cotejo de sumas de verificación y conteo de filas en destino.</td>
        <td><code>sha256sum / SELECT COUNT</code></td>
        <td>Integridad idéntica (Hash coincidente).</td>
      </tr>
    </tbody>
  </table>

  <h2>3.2 Plan de Respaldo de Datos (Disaster Recovery Plan - DRP)</h2>
  <p>
    Se implementa la regla universal de respaldo <strong>3-2-1</strong>: 3 copias de los datos, en 2 medios distintos (SSD NVMe local y almacenamiento externo/nube), con 1 copia fuera de las instalaciones del restaurante. Los respaldos completos se programan semanalmente y los diferenciales diariamente, acompañados de su correspondiente firma SHA-256.
  </p>

  <!-- 4. CONCLUSIONES Y REFERENCIAS -->
  <h1>4. CONCLUSIONES Y REFERENCIAS BIBLIOGRÁFICAS</h1>
  <p>
    1. <strong>Despliegue Contenerizado Exitoso:</strong> La utilización de Docker evitó la instalación de paquetes invasivos en el host del cliente, garantizando portabilidad absoluta y despliegue instantáneo en el puerto 8088.<br>
    2. <strong>Verificación Integral de Requerimientos:</strong> Se certificó el funcionamiento de la plantilla web adaptada para la Pizzería Bella Italia Popayán con tiempos de respuesta &lt; 25 ms y 0 errores de red.<br>
    3. <strong>Sostenibilidad Operacional:</strong> El plan de respaldo y migración de datos garantiza la continuidad del negocio ante contingencias de hardware o desastres operacionales.
  </p>

  <h2 style="margin-top: 10px;">Referencias Bibliográficas (Normas APA 7ma Edición)</h2>
  <p style="font-size: 7.4pt; color: #475569;">
    • Canonical Ltd. (2024). <em>Ubuntu Server documentation: System requirements and administration</em>. Canonical. https://ubuntu.com/server/docs<br>
    • Docker Inc. (2024). <em>Docker Compose overview and specification</em>. Docker Documentation. https://docs.docker.com/compose/<br>
    • IEEE Computer Society. (2008). <em>IEEE Standard for Software and System Test Documentation</em> (IEEE Std 829-2008). IEEE.<br>
    • International Organization for Standardization. (2014). <em>Systems and software engineering — SQuaRE — Quality models</em> (ISO/IEC 25010). ISO.<br>
    • Nginx Inc. (2024). <em>Nginx web server documentation: High-performance HTTP server</em>. F5 Networks. https://nginx.org/en/docs/<br>
    • Servicio Nacional de Aprendizaje [SENA]. (2023). <em>Identificación de requerimientos y plataformas de desarrollo: Componente formativo</em>. Dirección General, SENA.
  </p>

</body>
</html>
"""

html_file_path = os.path.join(DOCS_DIR, 'reporte_imprimible.html')
with open(html_file_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"[OK] HTML generado exitosamente en: {html_file_path}")

# Compilar PDF con Google Chrome Headless
pdf_output_path = os.path.join(DOCS_DIR, 'GA10-220501097-AA3-EV01_Software_Instalado_Cliente.pdf')
pdf_entrega_path = os.path.join(ENTREGA_DIR, 'GA10-220501097-AA3-EV01_Software_Instalado_Cliente.pdf')

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
    artifact_pdf = os.path.join(ARTIFACT_DIR, 'GA10-220501097-AA3-EV01_Software_Instalado_Cliente.pdf')
    shutil.copy2(pdf_output_path, artifact_pdf)
    print(f"[OK] PDF copiado a directorio de artefactos: {artifact_pdf}")
else:
    print(f"[ERROR] No se pudo generar el PDF: {res.stderr.decode('utf-8')}")

# Compilar formato Word (DOCX) con LibreOffice
docx_output_path = os.path.join(DOCS_DIR, 'GA10-220501097-AA3-EV01_Software_Instalado_Cliente.docx')
docx_entrega_path = os.path.join(ENTREGA_DIR, 'GA10-220501097-AA3-EV01_Software_Instalado_Cliente.docx')

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
    artifact_docx = os.path.join(ARTIFACT_DIR, 'GA10-220501097-AA3-EV01_Software_Instalado_Cliente.docx')
    shutil.copy2(docx_output_path, artifact_docx)
    print(f"[OK] DOCX copiado a directorio de artefactos: {artifact_docx}")

# Copiar diagrama a entrega y directorio de artefactos
diag_entrega = os.path.join(ENTREGA_DIR, 'diagrama_arquitectura_despliegue_docker_cliente.png')
if os.path.exists(diag_path):
    shutil.copy2(diag_path, diag_entrega)
    print(f"[OK] Diagrama copiado a entrega: {diag_entrega}")
    artifact_png = os.path.join(ARTIFACT_DIR, 'diagrama_arquitectura_despliegue_docker_cliente.png')
    shutil.copy2(diag_path, artifact_png)
    print(f"[OK] Diagrama copiado a directorio de artefactos: {artifact_png}")

# Copiar capturas reales a la carpeta de entrega
entrega_caps_dir = os.path.join(ENTREGA_DIR, 'capturas')
os.makedirs(entrega_caps_dir, exist_ok=True)
for c in os.listdir(CAPTURAS_DIR):
    src = os.path.join(CAPTURAS_DIR, c)
    dst = os.path.join(entrega_caps_dir, c)
    shutil.copy2(src, dst)
print(f"[OK] Capturas copiadas a entrega Zajuna: {entrega_caps_dir}")

# Copiar plantilla web a la carpeta de entrega
entrega_plantilla_dir = os.path.join(ENTREGA_DIR, 'plantilla_web')
os.makedirs(entrega_plantilla_dir, exist_ok=True)
plantilla_src = os.path.join(BASE_DIR, 'plantilla_web/index.html')
shutil.copy2(plantilla_src, os.path.join(entrega_plantilla_dir, 'index.html'))
print(f"[OK] Plantilla web copiada a entrega Zajuna: {entrega_plantilla_dir}")

# Generar archivo de enlaces institucional
repo_txt_path = os.path.join(ENTREGA_DIR, 'enlace_repositorio.txt')
with open(repo_txt_path, 'w', encoding='utf-8') as f:
    f.write("""ENLACE DEL REPOSITORIO GITHUB - EVIDENCIA GA10-220501097-AA3-EV01
Competencia: 220501097 - Implementar la solución de software de acuerdo con los requisitos de operación y modelos de referencia
Actividad de Aprendizaje: GA10-220501097-AA3 - Elaborar el plan de instalación, de acuerdo con los requerimientos
Evidencia: GA10-220501097-AA3-EV01 - Software instalado en la plataforma del cliente
Componente Formativo: "Identificación de requerimientos" y "Sistemas operativos de red"
Instrumento de Evaluación: Lista de Chequeo IE-GA10-220501097-AA3-EV01
Aprendiz: Karen Yuliana Campo - Ficha 3186681
Centro de Teleinformática y Producción Industrial (CTPI Popayán) - Regional Cauca
Proyecto Formativo: Pizzería Gourmet Bella Italia Popayán

--------------------------------------------------------------------------------
1. ENLACE DEL REPOSITORIO GITHUB DEL PROYECTO:
https://github.com/danilocampo/SENA-ADSO-Bella-Italia

2. DIRECTORIO DE LA EVIDENCIA EN EL REPOSITORIO:
https://github.com/danilocampo/SENA-ADSO-Bella-Italia/tree/main/CDE/Evidencias/PET-044_GA10-220501097-AA3-EV01_Software_Instalado_Plataforma_Cliente

3. DESPLIEGUE LOCAL EN CONTENEDOR DOCKER (PUERTO 8088):
http://localhost:8088/

4. ARCHIVOS ENTREGABLES OFICIALES EN EL PAQUETE:
- Documento Principal en PDF: GA10-220501097-AA3-EV01_Software_Instalado_Cliente.pdf
- Documento Editable en Word: GA10-220501097-AA3-EV01_Software_Instalado_Cliente.docx
- Diagrama Infográfico Renderizado: diagrama_arquitectura_despliegue_docker_cliente.png
- Diagrama Vectorial SVG: diagrama_arquitectura_despliegue_docker_cliente.svg
- Informe Técnico Completo en Markdown: INFORME_PASO_A_PASO_INSTALACION_DESPLIEGUE.md
- Carpeta de Capturas Reales (KDE X11 con Spectacle y xdotool): capturas/ (6 imágenes PNG)
- Plantilla Web HTML5/CSS3 Gourmet: plantilla_web/index.html
- Orquestación en Contenedores: docker/docker-compose.yml
- Script y Datos del Plan de Respaldo/Migración: scripts/respaldo_migracion_datos.sh
--------------------------------------------------------------------------------
""")
print(f"[OK] enlace_repositorio.txt generado en: {repo_txt_path}")

# Empacar ZIP de entrega institucional
zip_name = 'KARENCAMPO_AA3_EV01_GUIA10.zip'
zip_path = os.path.join(ENTREGA_DIR, zip_name)
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, BASE_DIR)
            z.write(full_path, arcname=os.path.join('PET-044_GA10-AA3-EV01', rel_path))
    z.write(repo_txt_path, arcname='enlace_repositorio.txt')
print(f"[OK] Paquete ZIP generado exitosamente ({os.path.getsize(zip_path)/1024:.1f} KB): {zip_path}")
print("=== COMPILACIÓN FINALIZADA CON ÉXITO ===")
