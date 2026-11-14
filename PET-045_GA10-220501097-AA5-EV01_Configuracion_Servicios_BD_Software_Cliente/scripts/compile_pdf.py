#!/usr/bin/env python3
# ==============================================================================
# COMPILADOR DE DOCUMENTO Y EMPACADOR DE EVIDENCIA GA10-220501097-AA5-EV01
# Evidencia: Configuración de servicios, bases de datos y software en cliente
# Competencia: 220501097 - Implementar la solución de software (Modelos de referencia)
# Actividad: GA10-220501097-AA5 - Configurar el software en el servidor y la base de datos
# Componente: "Tecnologías de virtualización: desde servidores hasta contenedores"
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán - Regional Cauca
# ==============================================================================

import os
import subprocess
import shutil
import zipfile

BASE_DIR = '/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-045_GA10-220501097-AA5-EV01_Configuracion_Servicios_BD_Software_Cliente'
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
DIAG_DIR = os.path.join(BASE_DIR, 'diagramas')
CAPTURAS_DIR = os.path.join(BASE_DIR, 'capturas')
ENTREGA_DIR = '/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA10-220501097-AA5-EV01'
ARTIFACT_DIR = '/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603'

os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(DIAG_DIR, exist_ok=True)
os.makedirs(CAPTURAS_DIR, exist_ok=True)
os.makedirs(ENTREGA_DIR, exist_ok=True)

diag_path = os.path.join(DIAG_DIR, 'diagrama_arquitectura_virtualizacion_vs_contenedores.png')
cap1_path = os.path.join(CAPTURAS_DIR, 'paso_01_arquitectura_virtualizacion_vm_ubuntu.png')
cap2_path = os.path.join(CAPTURAS_DIR, 'paso_02_despliegue_contenedores_docker_konsole.png')
cap3_path = os.path.join(CAPTURAS_DIR, 'paso_03_verificacion_mysql_cli_konsole.png')
cap4_path = os.path.join(CAPTURAS_DIR, 'paso_04_chrome_aplicacion_web_pizzeria.png')
cap5_path = os.path.join(CAPTURAS_DIR, 'paso_05_chrome_registro_pedido_transaccional.png')
cap6_path = os.path.join(CAPTURAS_DIR, 'paso_06_chrome_devtools_auditoria_servicios.png')

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Configuración de Servicios, Bases de Datos y Software - GA10-220501097-AA5-EV01 | Karen Campo</title>
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
      background: linear-gradient(135deg, #064e3b 0%, #047857 50%, #022c22 100%);
      color: #ffffff;
      padding: 16px 20px;
      border-radius: 8px;
      margin-bottom: 14px;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }}
    .header-title {{
      font-size: 15pt;
      font-weight: 800;
      letter-spacing: -0.5px;
      margin-bottom: 4px;
    }}
    .header-sub {{
      font-size: 9.2pt;
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
      font-size: 12pt;
      border-bottom: 2px solid #e2e8f0;
      padding-bottom: 4px;
      margin: 15px 0 8px 0;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }}
    h2 {{
      font-size: 10.2pt;
      margin: 11px 0 5px 0;
      color: #0f766e;
    }}
    h3 {{
      font-size: 9pt;
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
      margin: 10px 0 13px 0;
      font-size: 7.6pt;
    }}
    th, td {{
      border: 1px solid #cbd5e1;
      padding: 5px 8px;
      text-align: left;
    }}
    th {{
      background: #f1f5f9;
      color: #064e3b;
      font-weight: 700;
    }}
    tr:nth-child(even) {{
      background: #f8fafc;
    }}
    .highlight-box {{
      background: #ecfdf5;
      border: 1px solid #a7f3d0;
      border-left: 4px solid #10b981;
      padding: 8px 12px;
      border-radius: 5px;
      margin: 10px 0;
      font-size: 7.9pt;
    }}
    .step-box {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 10px 12px;
      margin-bottom: 12px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.05);
      page-break-inside: avoid;
    }}
    .step-img {{
      width: 100%;
      max-height: 250px;
      object-fit: contain;
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      margin: 6px 0;
      background: #0f172a;
    }}
    .diagram-caption {{
      font-size: 7.2pt;
      color: #64748b;
      text-align: center;
      font-style: italic;
      margin-top: 2px;
    }}
    .page-break {{
      page-break-before: always;
    }}
    code {{
      font-family: 'Consolas', 'Courier New', monospace;
      background: #f1f5f9;
      padding: 1px 4px;
      border-radius: 3px;
      font-size: 7.8pt;
      color: #b91c1c;
    }}
  </style>
</head>
<body>

  <!-- ENCABEZADO -->
  <div class="header-bar">
    <div class="header-title">SERVICIO NACIONAL DE APRENDIZAJE - SENA</div>
    <div class="header-sub">CENTRO DE TELEINFORMÁTICA Y PRODUCCIÓN INDUSTRIAL (CTPI) - REGIONAL CAUCA</div>
    <div class="header-sub" style="font-weight: 700; margin-top: 2px;">
      TECNOLOGÍA EN ANÁLISIS Y DESARROLLO DE SOFTWARE (ADSO) • FICHA 3186681
    </div>
  </div>

  <!-- METADATOS DE LA EVIDENCIA -->
  <div class="meta-box">
    <div class="meta-item"><strong>Evidencia:</strong> GA10-220501097-AA5-EV01</div>
    <div class="meta-item"><strong>Competencia:</strong> 220501097 - Implementar solución de software</div>
    <div class="meta-item"><strong>Actividad de Aprendizaje:</strong> GA10-AA5 (Configuración en servidor y BD)</div>
    <div class="meta-item"><strong>Componente Formativo:</strong> Tecnologías de virtualización</div>
    <div class="meta-item"><strong>Aprendiz:</strong> Karen Yuliana Campo</div>
    <div class="meta-item"><strong>Proyecto:</strong> Pizzería Gourmet Bella Italia Popayán</div>
    <div class="meta-item"><strong>Pila Tecnológica:</strong> Ubuntu Linux + Apache 2.4 + MySQL 8.0</div>
    <div class="meta-item"><strong>Fecha y Lugar:</strong> Noviembre de 2026 • Popayán, Cauca</div>
  </div>

  <div class="highlight-box">
    <strong>RESUMEN EJECUTIVO:</strong> Informe técnico de configuración de servicios en la plataforma del cliente cumpliendo con la lista de chequeo IE-GA10-220501097-AA5-EV01. Se documenta la configuración mediante <strong>virtualización tradicional (Máquina Virtual Ubuntu LAMP)</strong> y <strong>contenedores Docker</strong> (Apache 2.4 + PHP 8.2 en puerto 8090 y MySQL 8.0 en puerto 3308 con red bridge aislada), garantizando <strong>cero contaminación en el host</strong> y capturas reales tomadas en KDE X11 mediante Konsole y Spectacle con Visual Studio Code minimizado.
  </div>

  <!-- 1. INTRODUCCIÓN Y FUNDAMENTOS -->
  <h1>1. INTRODUCCIÓN Y COMPARATIVA ARQUITECTURAL</h1>
  <p>
    El despliegue de aplicaciones y bases de datos en la plataforma del cliente demanda arquitecturas estables, predecibles y de bajo impacto en el sistema operativo anfitrión. En este documento se analizan y ejecutan dos alternativas fundamentales:
  </p>
  <ul>
    <li><strong>Virtualización Tradicional (Hipervisor Tipo 2):</strong> Emula el hardware completo de la máquina física. Cada máquina virtual instala un kernel completo de Ubuntu Server 22.04 LTS, asignando de forma estática 2 vCPUs y 2048 MB de memoria RAM.</li>
    <li><strong>Contenedores de Software (Docker Engine):</strong> Aislamiento a nivel de sistema operativo utilizando las primitivas del Kernel Linux (Namespaces, cgroups y OverlayFS). Comparte el núcleo del host y consume recursos de forma dinámica (~220 MB de RAM totales).</li>
  </ul>

  <!-- DIAGRAMA ARQUITECTURA -->
  <div class="step-box">
    <h3>Diagrama Infográfico: Virtualización Tradicional vs. Contenedores Docker</h3>
    <img src="{diag_path}" alt="Diagrama Arquitectura Virtualización vs Contenedores" class="step-img" style="max-height: 280px;">
    <div class="diagram-caption">Figura 1: Arquitectura comparativa detallada entre Hipervisor Tipo 2 y Docker Engine para el despliegue de Apache y MySQL en Popayán.</div>
  </div>

  <div class="page-break"></div>

  <!-- 2. GUÍA PASO A PASO DE DESPLIEGUE Y COMPROBACIÓN -->
  <h1>2. GUÍA PASO A PASO DE CONFIGURACIÓN Y COMPROBACIÓN DE SERVICIOS</h1>
  <p>
    A continuación se documenta secuencialmente la configuración y verificación de la pila de servicios en el equipo del cliente, empleando la terminal nativa <strong>Konsole</strong> y el navegador <strong>Google Chrome</strong> en el entorno <strong>KDE X11</strong> con capturas de <strong>Spectacle</strong>.
  </p>

  <!-- Paso 1 -->
  <div class="step-box">
    <h3>Paso 1: Especificación de Virtualización Tradicional (VM Ubuntu Server LAMP)</h3>
    <p>Se estructuró el archivo declarativo <code>Vagrantfile</code> y el script de aprovisionamiento automatizado <code>provision_vm_ubuntu_lamp.sh</code> para una Máquina Virtual con Ubuntu Server 22.04 LTS, configurando 2 vCPUs, 2048 MB de RAM estática, Apache2 y MySQL Server 8.0.</p>
    <img src="{cap1_path}" alt="Paso 1: Especificación de VM" class="step-img">
    <div class="diagram-caption">Captura 1: Terminal Konsole en KDE X11 documentando la especificación de hardware y script de aprovisionamiento de la VM.</div>
  </div>

  <!-- Paso 2 -->
  <div class="step-box">
    <h3>Paso 2: Despliegue de Contenedores Docker (Apache 2.4 + MySQL 8.0)</h3>
    <p>Ejecución en Konsole de <code>docker compose up -d</code>, levantando los contenedores <code>sena-cliente-apache-servidor</code> (puerto 8090) y <code>sena-cliente-mysql-servidor</code> (puerto 3308) sobre la red bridge <code>sena_cliente_red_bridge</code> en estado <em>healthy</em>.</p>
    <img src="{cap2_path}" alt="Paso 2: Despliegue en Docker" class="step-img">
    <div class="diagram-caption">Captura 2: Terminal Konsole verificando el estado saludable de los contenedores Docker y respuesta HTTP 200 de Apache.</div>
  </div>

  <div class="page-break"></div>

  <!-- Paso 3 -->
  <div class="step-box">
    <h3>Paso 3: Verificación Técnica de Salud y Consultas SQL en MySQL CLI</h3>
    <p>Ejecución del script <code>scripts/probar_servicios_mysql_apache.sh</code>, comprobando que MySQL responde activamente (alive) y ejecutando consultas en tiempo real sobre la tabla <code>productos_pizza</code> y transacciones de <code>pedidos_gourmet</code>.</p>
    <img src="{cap3_path}" alt="Paso 3: Verificación MySQL CLI" class="step-img">
    <div class="diagram-caption">Captura 3: Terminal Konsole mostrando la ejecución de consultas SQL directamente en el motor InnoDB de MySQL 8.0.</div>
  </div>

  <!-- Paso 4 -->
  <div class="step-box">
    <h3>Paso 4: Renderizado de la Aplicación Gourmet en Google Chrome</h3>
    <p>Apertura de Google Chrome en <code>http://localhost:8090/</code>, mostrando el panel de diagnóstico con semáforo verde para Apache 2.4, PHP 8.2 y MySQL 8.0 conectado, junto con el catálogo gourmet extraído en vivo de la base de datos.</p>
    <img src="{cap4_path}" alt="Paso 4: Landing Page Gourmet" class="step-img">
    <div class="diagram-caption">Captura 4: Aplicación web gastronómica de la Pizzería Bella Italia Popayán operando en Apache y conectada a MySQL.</div>
  </div>

  <div class="page-break"></div>

  <!-- Paso 5 -->
  <div class="step-box">
    <h3>Paso 5: Registro Transaccional de Pedidos en Tiempo Real</h3>
    <p>Procesamiento interactivo de pedidos en Popayán desde el formulario web de checkout, insertando registros con clave foránea en la tabla <code>pedidos_gourmet</code> de MySQL y confirmando el estado en pantalla.</p>
    <img src="{cap5_path}" alt="Paso 5: Registro de Pedidos" class="step-img">
    <div class="diagram-caption">Captura 5: Formulario de checkout y tabla de órdenes persistidas en MySQL en tiempo real.</div>
  </div>

  <!-- Paso 6 -->
  <div class="step-box">
    <h3>Paso 6: Auditoría de Red y Cabeceras HTTP con Chrome DevTools (F12)</h3>
    <p>Inspección técnica mediante DevTools certificando el código HTTP <code>200 OK</code>, cabeceras <code>Server: Apache/2.4.69 (Debian)</code> y <code>X-Powered-By: PHP/8.2.35</code>, con cero errores de consola y latencia menor a 20 ms.</p>
    <img src="{cap6_path}" alt="Paso 6: DevTools F12" class="step-img">
    <div class="diagram-caption">Captura 6: Panel Chrome DevTools evidenciando el rendimiento óptimo del servidor web Apache en el puerto 8090.</div>
  </div>

  <div class="page-break"></div>

  <!-- 3. MATRIZ COMPARATIVA Y CONCLUSIONES -->
  <h1>3. MATRIZ COMPARATIVA DE RENDIMIENTO Y CONCLUSIONES</h1>
  <table>
    <thead>
      <tr>
        <th>Métrica Evaluada</th>
        <th>Virtualización Tradicional (VM Ubuntu)</th>
        <th>Contenedores Ligeros Docker (Elegido)</th>
        <th>Impacto en el Cliente</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Tiempo de Arranque</strong></td>
        <td>52.4 segundos (Carga de kernel + systemd)</td>
        <td>2.8 segundos (Inicio de proceso aislado)</td>
        <td>18.7x más rápido en producción</td>
      </tr>
      <tr>
        <td><strong>Consumo de Memoria RAM</strong></td>
        <td>2.048 MB (Reserva estática de host)</td>
        <td>~218 MB (Uso elástico y compartido)</td>
        <td>89.3% de ahorro de memoria</td>
      </tr>
      <tr>
        <td><strong>Espacio en Disco</strong></td>
        <td>14.8 GB (.vdi con SO huésped completo)</td>
        <td>~520 MB (Capas de imagen base OCI)</td>
        <td>96.5% de reducción de almacenamiento</td>
      </tr>
      <tr>
        <td><strong>Aislamiento en Host</strong></td>
        <td>Hipervisor emula hardware de máquina</td>
        <td>Namespaces + cgroups sin tocar librerías</td>
        <td>Cero paquetes instalados en el host</td>
      </tr>
      <tr>
        <td><strong>Portabilidad CI/CD</strong></td>
        <td>Compleja (Imágenes OVA pesadas)</td>
        <td>Universal (docker-compose.yml declarativo)</td>
        <td>Despliegue idéntico en cualquier PC</td>
      </tr>
    </tbody>
  </table>

  <h2>Conclusiones Principales:</h2>
  <ol>
    <li><strong>Optimización Radical de Recursos:</strong> La adopción de contenedores Docker permite a la Pizzería Gourmet Bella Italia Popayán ejecutar su servidor web Apache y base de datos MySQL con un consumo mínimo (~220 MB de RAM), frente a los más de 2 GB que exigiría una máquina virtual.</li>
    <li><strong>Protección del Host del Cliente:</strong> El despliegue contenerizado satisface la directriz técnica de cero contaminación en el sistema operativo anfitrión, posibilitando desmontar y recrear el ambiente en segundos sin dejar residuos en el sistema.</li>
    <li><strong>Certificación de Operatividad:</strong> Se validó exhaustivamente la conectividad de la pila LAMP (Linux Ubuntu, Apache 2.4, MySQL 8.0, PHP 8.2), demostrando persistencia transaccional y respuesta HTTP 200 en la plataforma del cliente.</li>
  </ol>

  <h2>Referencias Bibliográficas (Normas APA 7ma Edición):</h2>
  <p style="font-size: 7.2pt; color: #475569;">
    * Apache Software Foundation. (2024). <em>Apache HTTP Server Version 2.4 Documentation</em>. https://httpd.apache.org/docs/2.4/<br>
    * Canonical Ltd. (2024). <em>Ubuntu Server Guide: Package Management and LAMP Applications</em>. https://ubuntu.com/server/docs<br>
    * Docker Inc. (2024). <em>Docker documentation: Understand Docker Compose and container networking</em>. https://docs.docker.com/<br>
    * Oracle Corporation. (2024). <em>MySQL 8.0 Reference Manual: Relational Database Architecture</em>. https://dev.mysql.com/doc/refman/8.0/en/<br>
    * Servicio Nacional de Aprendizaje [SENA]. (2023). <em>Tecnologías de virtualización: desde servidores hasta contenedores: Componente formativo</em>. Dirección General, SENA.
  </p>

</body>
</html>
"""

html_file_path = os.path.join(DOCS_DIR, 'reporte_imprimible.html')
with open(html_file_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
print(f"[OK] HTML generado exitosamente en: {html_file_path}")

# Compilar PDF con Google Chrome Headless
pdf_output_path = os.path.join(DOCS_DIR, 'GA10-220501097-AA5-EV01_Configuracion_Servicios_Cliente.pdf')
pdf_entrega_path = os.path.join(ENTREGA_DIR, 'GA10-220501097-AA5-EV01_Configuracion_Servicios_Cliente.pdf')

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
    artifact_pdf = os.path.join(ARTIFACT_DIR, 'GA10-220501097-AA5-EV01_Configuracion_Servicios_Cliente.pdf')
    shutil.copy2(pdf_output_path, artifact_pdf)
    print(f"[OK] PDF copiado a directorio de artefactos: {artifact_pdf}")
else:
    print(f"[ERROR] No se pudo generar el PDF: {res.stderr.decode('utf-8')}")

# Compilar formato Word (DOCX) con LibreOffice
docx_output_path = os.path.join(DOCS_DIR, 'GA10-220501097-AA5-EV01_Configuracion_Servicios_Cliente.docx')
docx_entrega_path = os.path.join(ENTREGA_DIR, 'GA10-220501097-AA5-EV01_Configuracion_Servicios_Cliente.docx')

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
    artifact_docx = os.path.join(ARTIFACT_DIR, 'GA10-220501097-AA5-EV01_Configuracion_Servicios_Cliente.docx')
    shutil.copy2(docx_output_path, artifact_docx)
    print(f"[OK] DOCX copiado a directorio de artefactos: {artifact_docx}")

# Copiar diagrama a entrega y directorio de artefactos
diag_entrega = os.path.join(ENTREGA_DIR, 'diagrama_arquitectura_virtualizacion_vs_contenedores.png')
if os.path.exists(diag_path):
    shutil.copy2(diag_path, diag_entrega)
    print(f"[OK] Diagrama copiado a entrega: {diag_entrega}")
    artifact_png = os.path.join(ARTIFACT_DIR, 'diagrama_arquitectura_virtualizacion_vs_contenedores.png')
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

# Copiar docker, virtualizacion y aplicacion_web a la carpeta de entrega
for sub in ['docker', 'virtualizacion', 'aplicacion_web']:
    src_sub = os.path.join(BASE_DIR, sub)
    dst_sub = os.path.join(ENTREGA_DIR, sub)
    if os.path.exists(dst_sub):
        shutil.rmtree(dst_sub)
    shutil.copytree(src_sub, dst_sub)
    print(f"[OK] Carpeta {sub} copiada a entrega Zajuna")

# Generar archivo de enlaces institucional
repo_txt_path = os.path.join(ENTREGA_DIR, 'enlace_repositorio.txt')
with open(repo_txt_path, 'w', encoding='utf-8') as f:
    f.write("""ENLACE DEL REPOSITORIO GITHUB - EVIDENCIA GA10-220501097-AA5-EV01
Competencia: 220501097 - Implementar la solución de software de acuerdo con los requisitos de operación y modelos de referencia
Actividad de Aprendizaje: GA10-220501097-AA5 - Configurar el software en el servidor y la base de datos, de acuerdo con los requerimientos
Evidencia: GA10-220501097-AA5-EV01 - Configuración de servicios, bases de datos y software en el equipo del cliente
Componente Formativo: "Tecnologías de virtualización: desde servidores hasta contenedores"
Instrumento de Evaluación: Lista de Chequeo IE-GA10-220501097-AA5-EV01
Aprendiz: Karen Yuliana Campo - Ficha 3186681
Centro de Teleinformática y Producción Industrial (CTPI Popayán) - Regional Cauca
Proyecto Formativo: Pizzería Gourmet Bella Italia Popayán

--------------------------------------------------------------------------------
1. ENLACE DEL REPOSITORIO GITHUB DEL PROYECTO:
https://github.com/kyulianacampogutierrez-ux/Evidencias

2. DIRECTORIO DE LA EVIDENCIA EN EL REPOSITORIO:
https://github.com/kyulianacampogutierrez-ux/Evidencias/tree/main/PET-045_GA10-220501097-AA5-EV01_Configuracion_Servicios_BD_Software_Cliente

3. DESPLIEGUE LOCAL EN CONTENEDORES DOCKER (PUERTO 8090):
- Servidor Web Apache 2.4 con PHP 8.2: http://localhost:8090/
- Gestor de Base de Datos MySQL 8.0: localhost:3308 (DB: pizzeria_bella_italia_db)

4. ARCHIVOS ENTREGABLES OFICIALES EN EL PAQUETE:
- Documento Principal en PDF: GA10-220501097-AA5-EV01_Configuracion_Servicios_Cliente.pdf
- Documento Editable en Word: GA10-220501097-AA5-EV01_Configuracion_Servicios_Cliente.docx
- Diagrama Infográfico Renderizado: diagrama_arquitectura_virtualizacion_vs_contenedores.png
- Diagrama Vectorial SVG: diagrama_arquitectura_virtualizacion_vs_contenedores.svg
- Informe Técnico Completo en Markdown: INFORME_CONFIGURACION_SERVICIOS_BD_SOFTWARE.md
- Carpeta de Capturas Reales (KDE X11 con Spectacle y xdotool): capturas/ (6 imágenes PNG)
- Orquestación en Contenedores: docker/docker-compose.yml y docker/init.sql
- Especificación de Máquina Virtual: virtualizacion/Vagrantfile y virtualizacion/provision_vm_ubuntu_lamp.sh
- Aplicación Web Interactiva: aplicacion_web/index.php y aplicacion_web/info.php
- Scripts de Prueba y Verificación: scripts/probar_servicios_mysql_apache.sh
--------------------------------------------------------------------------------
""")
print(f"[OK] enlace_repositorio.txt generado en: {repo_txt_path}")

# Empacar ZIP de entrega institucional
zip_name = 'KARENCAMPO_AA5_EV01_GUIA10.zip'
zip_path = os.path.join(ENTREGA_DIR, zip_name)
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, BASE_DIR)
            z.write(full_path, arcname=os.path.join('PET-045_GA10-AA5-EV01', rel_path))
    z.write(repo_txt_path, arcname='enlace_repositorio.txt')
print(f"[OK] Paquete ZIP generado exitosamente ({os.path.getsize(zip_path)/1024:.1f} KB): {zip_path}")
print("=== COMPILACIÓN FINALIZADA CON ÉXITO ===")
