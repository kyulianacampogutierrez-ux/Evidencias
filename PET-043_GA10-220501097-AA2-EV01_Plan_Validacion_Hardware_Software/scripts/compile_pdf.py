#!/usr/bin/env python3
# ==============================================================================
# COMPILADOR DE DOCUMENTO Y EMPACADOR DE EVIDENCIA GA10-220501097-AA2-EV01
# Evidencia: Elaborar plan de validación de características mínimas de hardware
# Competencia: 220501097 - Implementar la solución de software (Modelos de referencia)
# Actividad: GA10-220501097-AA2 - Verificar el cumplimiento de hardware requerido
# Componente: "Sistemas operativos de red" (Sistemas operativos y licenciamiento)
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán - Regional Cauca
# ==============================================================================

import os
import subprocess
import shutil
import zipfile

BASE_DIR = '/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-043_GA10-220501097-AA2-EV01_Plan_Validacion_Hardware_Software'
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
DIAG_DIR = os.path.join(BASE_DIR, 'diagramas')
AUDIT_DIR = os.path.join(BASE_DIR, 'auditoria')
ENTREGA_DIR = '/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA10-220501097-AA2-EV01'
ARTIFACT_DIR = '/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603'

os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(DIAG_DIR, exist_ok=True)
os.makedirs(AUDIT_DIR, exist_ok=True)
os.makedirs(ENTREGA_DIR, exist_ok=True)

diag_path = os.path.join(DIAG_DIR, 'diagrama_arquitectura_servidor_php_hardware.png')

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Plan de Validación de Características Mínimas de Hardware - GA10-220501097-AA2-EV01 | Karen Campo</title>
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
    .badge-warn {{
      background: #f59e0b;
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
    .formula-box {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      border-left: 4px solid #16a34a;
      padding: 7px 11px;
      border-radius: 6px;
      margin: 7px 0;
      font-family: 'Consolas', monospace;
      font-size: 8pt;
      color: #14532d;
    }}
    .page-break {{
      page-break-before: always;
    }}
  </style>
</head>
<body>

  <!-- PORTADA / ENCABEZADO INSTITUCIONAL -->
  <div class="header-bar">
    <div class="header-title">PLAN DE VALIDACIÓN DE CARACTERÍSTICAS MÍNIMAS DE HARDWARE</div>
    <div class="header-sub">Evidencia GA10-220501097-AA2-EV01 | Sistemas Operativos de Red, Licenciamiento y Dimensionamiento PHP</div>
  </div>

  <div class="meta-box">
    <div class="meta-item"><strong>Institución:</strong> Servicio Nacional de Aprendizaje (SENA)</div>
    <div class="meta-item"><strong>Centro:</strong> Teleinformática y Producción Industrial (CTPI) - Cauca</div>
    <div class="meta-item"><strong>Programa:</strong> Tecnología en Análisis y Desarrollo de Software (ADSO)</div>
    <div class="meta-item"><strong>Ficha:</strong> 3186681 | <strong>Modalidad:</strong> Virtual</div>
    <div class="meta-item"><strong>Aprendiz:</strong> Karen Yuliana Campo</div>
    <div class="meta-item"><strong>Proyecto Formativo:</strong> Pizzería Gourmet Bella Italia Popayán</div>
    <div class="meta-item"><strong>Competencia:</strong> 220501097 - Implementar la solución de software</div>
    <div class="meta-item"><strong>Actividad:</strong> GA10-220501097-AA2 - Verificar características mínimas de hardware</div>
  </div>

  <!-- CASO DE ESTUDIO DE LA GUÍA -->
  <div class="highlight-card">
    <strong>🎯 Parámetros del Caso de Estudio (Guía de Aprendizaje 10 - Numeral 3.1.2):</strong>
    Aplicación web desarrollada en <strong>PHP</strong> • Persistencia relacional para identificación y registro de usuarios • Demanda proyectada de <strong>250 usuarios activos no concurrentes</strong> • Enfoque en sistemas operativos de red y régimen de licenciamiento de software.
  </div>

  <!-- 1. INTRODUCCIÓN Y MARCO CONCEPTUAL -->
  <h1>1. INTRODUCCIÓN Y MARCO CONCEPTUAL (SISTEMAS OPERATIVOS DE RED)</h1>
  <p>
    El aseguramiento de la operatividad de una solución de software requiere verificar rigurosamente que la plataforma tecnológica satisfaga las condiciones mínimas de cómputo, almacenamiento, memoria y conectividad. Según el componente formativo institucional <strong>"Sistemas operativos de red"</strong>, la elección del Sistema Operativo de Red (NOS) y la política de licenciamiento de software constituyen pilares fundamentales para garantizar la estabilidad, seguridad y sostenibilidad económica del proyecto.
  </p>
  <p>
    En una arquitectura cliente-servidor para aplicaciones web basadas en PHP (como el portal transaccional de la <em>Pizzería Gourmet Bella Italia Popayán</em>), el sistema operativo debe gestionar eficientemente llamadas al sistema no bloqueantes (<code>epoll</code>), administrar memoria compartida para aceleradores de código (OPcache) y proveer aislamiento seguro para el motor de base de datos relacional.
  </p>

  <h2>1.1 Análisis Comparativo de Sistemas Operativos y Licenciamiento de Software</h2>
  <table>
    <thead>
      <tr>
        <th style="width: 20%;">Parámetro Técnico</th>
        <th style="width: 40%;">Linux Server (Ubuntu / Debian LTS) - SELECCIONADO</th>
        <th style="width: 40%;">Windows Server 2022 / 2025 Standard</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Modelo de Licenciamiento</strong></td>
        <td><strong>FOSS / Código Abierto (GNU GPL v2/v3):</strong> Libre de costos de adquisición.</td>
        <td><strong>Comercial Propietario (EULA):</strong> Cobro obligatorio por paquetes de 16 núcleos.</td>
      </tr>
      <tr>
        <td><strong>Licencias CAL (250 Usuarios)</strong></td>
        <td><strong>$0 COP:</strong> Sin restricción de usuarios concurrentes ni clientes conectados.</td>
        <td><strong>Alto Costo:</strong> Requiere 250 licencias CAL (~$45 USD c/u = ~$11.250 USD).</td>
      </tr>
      <tr>
        <td><strong>Consumo de Memoria en Reposo</strong></td>
        <td><strong>Mínimo (~350 MB a 400 MB RAM):</strong> Ejecución en modo headless CLI sin GUI.</td>
        <td><strong>Elevado (~2.5 a 4.0 GB RAM):</strong> Dependencias de telemetría y subsistema gráfico.</td>
      </tr>
      <tr>
        <td><strong>Rendimiento con Pila PHP</strong></td>
        <td><strong>Óptimo y Nativo:</strong> Comunicación de alta velocidad vía Sockets UNIX locales.</td>
        <td><strong>Vía FastCGI en IIS:</strong> Mayor latencia por capas de emulación y procesos CGI.</td>
      </tr>
      <tr>
        <td><strong>Costo Total de Propiedad (TCO)</strong></td>
        <td><strong>Óptimo para PYMES ($0 COP en licencias):</strong> Inversión enfocada en hardware.</td>
        <td><strong>Elevado (> $50.000.000 COP):</strong> Inviable para modelos gastronómicos regionales.</td>
      </tr>
    </tbody>
  </table>

  <!-- INFOGRAFÍA DE ARQUITECTURA Y VALIDACIÓN -->
  <div class="diagram-container">
    <img src="{diag_path}" alt="Diagrama de Arquitectura de Servidor PHP y Validación de Hardware" class="diagram-img">
    <div class="diagram-caption">Figura 1: Arquitectura de Pila LEMP, Modelado Matemático con Ley de Little y Matriz de Validación de Hardware.</div>
  </div>

  <div class="page-break"></div>

  <!-- 2. MODELADO MATEMÁTICO DE CARGA Y DIMENSIONAMIENTO -->
  <h1>2. MODELADO MATEMÁTICO DE CARGA Y DIMENSIONAMIENTO DE RECURSOS</h1>
  <p>
    Para dimensionar con rigor de ingeniería los recursos de hardware requeridos para la población objetivo de 250 usuarios activos no concurrentes, se modela el comportamiento del sistema mediante la <strong>Ley de Little</strong>:
  </p>

  <div class="formula-box">
    Población Activa (P) = 250 usuarios | Ratio de Concurrencia Pico (fc) = 12%<br>
    Usuarios Concurrentes Pico (N) = 250 × 0.12 = 30 usuarios simultáneos<br>
    Ley de Little: N = X × (R + Z)  ==>  X = N / (R + Z)<br>
    X_nominal = 30 / (0.5s + 5.0s) = 5.45 peticiones/segundo (RPS)<br>
    X_diseño (Factor de Seguridad 2.5x) = 15 RPS (Requests Per Second)
  </div>

  <h2>2.1 Desglose Granular de Consumo de Memoria RAM (Pila LEMP)</h2>
  <table>
    <thead>
      <tr>
        <th style="width: 15%;">Capa del Stack</th>
        <th style="width: 30%;">Software y Componente</th>
        <th style="width: 40%;">Detalle de Cálculo y Consumo de Memoria</th>
        <th style="width: 15%;">Memoria RAM</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Capa 1: SO / Kernel</strong></td>
        <td>Ubuntu Server 22.04 LTS Headless</td>
        <td>Kernel Linux 6.8 + demonios esenciales (systemd, sshd, rsyslog, cron).</td>
        <td>400 MB</td>
      </tr>
      <tr>
        <td><strong>Capa 2: Web Server</strong></td>
        <td>Nginx 1.24 (Reverse Proxy)</td>
        <td>Arquitectura asíncrona no bloqueante (epoll), 2 workers gestionando HTTP/HTTPS.</td>
        <td>50 MB</td>
      </tr>
      <tr>
        <td><strong>Capa 3: Aplicación</strong></td>
        <td>PHP 8.2 FPM (FastCGI)</td>
        <td>30 workers dinámicos a 40 MB c/u (1.200 MB) + OPcache bytecode compartido (128 MB).</td>
        <td>1.33 GB</td>
      </tr>
      <tr>
        <td><strong>Capa 4: Base Datos</strong></td>
        <td>MySQL 8.0 / MariaDB 10.11</td>
        <td>InnoDB Buffer Pool (1.024 MB) + pool de 30 conexiones activas y overhead (380 MB).</td>
        <td>1.40 GB</td>
      </tr>
      <tr style="background: #dcfce7; font-weight: bold;">
        <td colspan="3">TOTAL MEMORIA ACTIVA DE TRABAJO EN HORA PICO (15 RPS)</td>
        <td>3.18 GB (~4 GB)</td>
      </tr>
    </tbody>
  </table>

  <h2>2.2 Dimensionamiento de CPU, Almacenamiento y Red</h2>
  <p>
    • <strong>Procesador (CPU):</strong> Cada petición en PHP 8.2 requiere ~45 ms de procesamiento CPU. A 15 RPS se demanda 0.68 núcleos sostenidos; sumando el overhead de Nginx y MySQL se requieren mínimo <strong>2 vCPUs</strong> (Recomendado: <strong>4 vCPUs</strong> a ≥ 2.4 GHz).<br>
    • <strong>Almacenamiento (Disco e IOPS):</strong> 8 GB para el SO, 2 GB para código PHP, 5 GB para base de datos de usuarios, 10 GB para backups diarios y 4 GB de Swap. Se requiere mínimo <strong>50 GB en disco SSD SATA o NVMe PCIe (≥ 3.000 IOPS)</strong> para evitar cuellos de botella en la escritura síncrona del log transaccional.<br>
    • <strong>Conectividad de Red:</strong> A un promedio de 80 KB por respuesta HTTP, 15 RPS generan un tráfico saliente de 9.6 Mbps. Se requiere una tarjeta de red <strong>Gigabit Ethernet (1000 Mbps)</strong> y un enlace simétrico a Internet de mínimo <strong>20 a 50 Mbps</strong>.
  </p>

  <!-- 3. PLAN DE VALIDACIÓN DE HARDWARE -->
  <h1>3. PLAN PROCEDURAL DE VALIDACIÓN DE HARDWARE</h1>
  <p>
    El plan de validación se estructura en cinco (5) fases secuenciales que permiten auditar de forma objetiva las capacidades del servidor antes del despliegue:
  </p>

  <table>
    <thead>
      <tr>
        <th style="width: 12%;">Fase</th>
        <th style="width: 25%;">Objetivo de la Fase</th>
        <th style="width: 35%;">Comandos de Diagnóstico en Linux</th>
        <th style="width: 28%;">Criterio de Aceptación (SLA)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Fase 1: Inventario</strong></td>
        <td>Identificación de la plataforma y arquitectura</td>
        <td><code>uname -a ; cat /etc/os-release ; hostnamectl</code></td>
        <td>Arquitectura de 64 bits (x86_64), Linux LTS.</td>
      </tr>
      <tr>
        <td><strong>Fase 2: CPU</strong></td>
        <td>Verificación de núcleos y juego de instrucciones</td>
        <td><code>lscpu | grep -E "Model|CPU\(s\):" ; nproc</code></td>
        <td>≥ 2 Cores lógicos, frecuencia base ≥ 2.0 GHz.</td>
      </tr>
      <tr>
        <td><strong>Fase 3: Memoria</strong></td>
        <td>Comprobación de RAM física y Swap</td>
        <td><code>free -h --giga ; cat /proc/meminfo</code></td>
        <td>Total RAM ≥ 2.0 GB (Rec: ≥ 4 GB), Swap ≥ 2 GB.</td>
      </tr>
      <tr>
        <td><strong>Fase 4: Disco</strong></td>
        <td>Espacio en disco, particiones e IOPS</td>
        <td><code>df -hT / ; lsblk -o NAME,SIZE,TYPE,ROTA</code></td>
        <td>Espacio libre en / ≥ 20 GB, ROTA == 0 (SSD/NVMe).</td>
      </tr>
      <tr>
        <td><strong>Fase 5: Red / Carga</strong></td>
        <td>Velocidad de interfaz y prueba de estrés</td>
        <td><code>ip -br addr ; ab -n 1000 -c 30 http://localhost/</code></td>
        <td>NIC 1 Gbps, 0 errores en estrés, SLA &lt; 500 ms.</td>
      </tr>
    </tbody>
  </table>

  <div class="page-break"></div>

  <!-- 4. MATRIZ DE VALIDACIÓN Y RESULTADOS DE AUDITORÍA REAL -->
  <h1>4. MATRIZ DE VALIDACIÓN Y RESULTADOS DE AUDITORÍA EN SERVIDOR</h1>
  <p>
    A continuación se presentan los resultados de la auditoría ejecutada en el servidor de pruebas del proyecto mediante el script automatizado <code>scripts/auditar_hardware.js</code>:
  </p>

  <table>
    <thead>
      <tr>
        <th style="width: 18%;">Componente</th>
        <th style="width: 18%;">Requisito Mínimo</th>
        <th style="width: 20%;">Perfil Recomendado</th>
        <th style="width: 26%;">Valor Auditado en Servidor</th>
        <th style="width: 18%;">Dictamen</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Procesador (CPU)</strong></td>
        <td>2 vCPUs @ ≥ 2.0 GHz</td>
        <td>4 vCPUs @ ≥ 2.4 GHz</td>
        <td>Intel Core i7-8700T (12 núcleos @ 2.40GHz)</td>
        <td><span class="badge-pass">PASS - CUMPLE</span></td>
      </tr>
      <tr>
        <td><strong>Memoria RAM</strong></td>
        <td>2.0 GB Física</td>
        <td>4.0 GB a 8.0 GB</td>
        <td>19.40 GB RAM (8.99 GB libres en reposo)</td>
        <td><span class="badge-pass">PASS - CUMPLE</span></td>
      </tr>
      <tr>
        <td><strong>Almacenamiento</strong></td>
        <td>20 GB SSD SATA</td>
        <td>50 GB NVMe PCIe</td>
        <td>181.58 GB Ext4 (92.11 GB disponibles)</td>
        <td><span class="badge-pass">PASS - CUMPLE</span></td>
      </tr>
      <tr>
        <td><strong>Interfaz de Red</strong></td>
        <td>100 Mbps Fast Eth</td>
        <td>1000 Mbps Gigabit</td>
        <td>NIC Gigabit enp1s0 (Full Duplex) + Docker</td>
        <td><span class="badge-pass">PASS - CUMPLE</span></td>
      </tr>
      <tr>
        <td><strong>Sistema Operativo</strong></td>
        <td>Linux x86_64</td>
        <td>Ubuntu 22.04 LTS (FOSS)</td>
        <td>Ubuntu 22.04.5 LTS (Kernel 6.8.0-149-generic)</td>
        <td><span class="badge-pass">PASS - CUMPLE</span></td>
      </tr>
      <tr>
        <td><strong>Licenciamiento</strong></td>
        <td>Libre de CALs</td>
        <td>GNU GPLv3 / Open Source</td>
        <td>FOSS Total ($0 COP en licencias operativas)</td>
        <td><span class="badge-pass">PASS - CUMPLE</span></td>
      </tr>
    </tbody>
  </table>

  <h2>4.1 Registro de Salida de Auditoría en Consola</h2>
  <pre><code>$ node CDE/Evidencias/PET-043_GA10-220501097-AA2-EV01_.../scripts/auditar_hardware.js

================================================================================
REPORTE TÉCNICO DE AUDITORÍA DE HARDWARE - EVIDENCIA GA10-220501097-AA2-EV01
Plan de Validación de Características Mínimas de Hardware para Aplicación PHP
Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán - Regional Cauca
================================================================================
* PROCESADOR: Intel(R) Core(TM) i7-8700T CPU @ 2.40GHz (12 cores) -> [PASS - CUMPLE]
* MEMORIA RAM: 19.40 GB Total (8.99 GB disponible) -> [PASS - CUMPLE]
* ALMACENAMIENTO: 181.58 GB Total (92.11 GB disponible, Uso 47%) -> [PASS - CUMPLE]
* ARQUITECTURA / SO: Linux x64 (Kernel 6.8.0-149-generic) -> [PASS - CUMPLE]
* ADAPTADORES DE RED: 1 interfaz IPv4 activa Gigabit Ethernet -> [PASS - CUMPLE]
--------------------------------------------------------------------------------
DICTAMEN FINAL: APROBADO_CUMPLE_REQUERIMIENTOS
El entorno de hardware satisface holgadamente las demandas para 250 usuarios activos.</code></pre>

  <!-- 5. CONCLUSIONES Y REFERENCIAS -->
  <h1>5. CONCLUSIONES Y REFERENCIAS BIBLIOGRÁFICAS</h1>
  <p>
    1. <strong>Idoneidad Técnica y Operativa:</strong> El dimensionamiento basado en la Ley de Little demostró que una infraestructura con 4 GB de RAM y 2 vCPUs garantiza tiempos de respuesta SLA &lt; 500 ms ante 30 usuarios simultáneos en hora pico para la Pizzería Bella Italia.<br>
    2. <strong>Eficiencia de Costos:</strong> La adopción de Ubuntu Server LTS y la pila LEMP bajo licencia FOSS elimina sobrecostos de más de $12.000 USD en licencias comerciales propietarias y CALs.<br>
    3. <strong>Validación Exitosa:</strong> La auditoría en el servidor certificó 12 núcleos lógicos, 19.4 GB de RAM y almacenamiento Ext4 de 181 GB, superando con holgura los requerimientos mínimos de la evidencia.
  </p>

  <h2 style="margin-top: 10px;">Referencias Bibliográficas (Normas APA 7ma Edición)</h2>
  <p style="font-size: 7.4pt; color: #475569;">
    • Canonical Ltd. (2024). <em>Ubuntu Server documentation: System requirements and administration</em>. Canonical. https://ubuntu.com/server/docs<br>
    • IEEE Computer Society. (2008). <em>IEEE Standard for Software and System Test Documentation</em> (IEEE Std 829-2008). IEEE.<br>
    • International Organization for Standardization. (2014). <em>Systems and software engineering — SQuaRE — Quality models</em> (ISO/IEC 25010). ISO.<br>
    • Little, J. D. C. (2011). Little's law as viewed on its 50th anniversary. <em>Operations Research</em>, 59(3), 536-549.<br>
    • Menascé, D. A., Almeida, V. A. F., & Dowdy, L. W. (2004). <em>Performance by Design: Capacity Planning By Example</em>. Prentice Hall.<br>
    • Servicio Nacional de Aprendizaje [SENA]. (2023). <em>Sistemas operativos de red: Componente formativo</em>. Dirección General, SENA.
  </p>

</body>
</html>
"""

html_file_path = os.path.join(DOCS_DIR, 'reporte_imprimible.html')
with open(html_file_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"[OK] HTML generado exitosamente en: {html_file_path}")

# Compilar PDF con Google Chrome Headless
pdf_output_path = os.path.join(DOCS_DIR, 'GA10-220501097-AA2-EV01_Plan_Validacion_Hardware.pdf')
pdf_entrega_path = os.path.join(ENTREGA_DIR, 'GA10-220501097-AA2-EV01_Plan_Validacion_Hardware.pdf')

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
    artifact_pdf = os.path.join(ARTIFACT_DIR, 'GA10-220501097-AA2-EV01_Plan_Validacion_Hardware.pdf')
    shutil.copy2(pdf_output_path, artifact_pdf)
    print(f"[OK] PDF copiado a directorio de artefactos: {artifact_pdf}")
else:
    print(f"[ERROR] No se pudo generar el PDF: {res.stderr.decode('utf-8')}")

# Compilar formato Word (DOCX) con LibreOffice
docx_output_path = os.path.join(DOCS_DIR, 'GA10-220501097-AA2-EV01_Plan_Validacion_Hardware.docx')
docx_entrega_path = os.path.join(ENTREGA_DIR, 'GA10-220501097-AA2-EV01_Plan_Validacion_Hardware.docx')

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
    artifact_docx = os.path.join(ARTIFACT_DIR, 'GA10-220501097-AA2-EV01_Plan_Validacion_Hardware.docx')
    shutil.copy2(docx_output_path, artifact_docx)
    print(f"[OK] DOCX copiado a directorio de artefactos: {artifact_docx}")

# Copiar diagrama a entrega y directorio de artefactos
diag_entrega = os.path.join(ENTREGA_DIR, 'diagrama_arquitectura_servidor_php_hardware.png')
if os.path.exists(diag_path):
    shutil.copy2(diag_path, diag_entrega)
    print(f"[OK] Diagrama copiado a entrega: {diag_entrega}")
    artifact_png = os.path.join(ARTIFACT_DIR, 'diagrama_arquitectura_servidor_php_hardware.png')
    shutil.copy2(diag_path, artifact_png)
    print(f"[OK] Diagrama copiado a directorio de artefactos: {artifact_png}")

# Generar archivo de enlaces institucional
repo_txt_path = os.path.join(ENTREGA_DIR, 'enlace_repositorio.txt')
with open(repo_txt_path, 'w', encoding='utf-8') as f:
    f.write("""ENLACE DEL REPOSITORIO GITHUB - EVIDENCIA GA10-220501097-AA2-EV01
Competencia: 220501097 - Implementar la solución de software de acuerdo con los requisitos de operación y modelos de referencia
Actividad de Aprendizaje: GA10-220501097-AA2 - Verificar el cumplimiento de las características mínimas de hardware requeridas, para el software desarrollado
Evidencia: GA10-220501097-AA2-EV01 - Elaborar plan de validación de características mínimas de hardware para el software
Componente Formativo: "Sistemas operativos de red" (Sistemas operativos y licenciamiento de software)
Instrumento de Evaluación: Lista de Chequeo IE-GA10-220501097-AA2-EV01
Aprendiz: Karen Yuliana Campo - Ficha 3186681
Centro de Teleinformática y Producción Industrial (CTPI Popayán) - Regional Cauca
Proyecto Formativo: Pizzería Gourmet Bella Italia Popayán

--------------------------------------------------------------------------------
1. ENLACE DEL REPOSITORIO GITHUB DEL PROYECTO:
https://github.com/danilocampo/SENA-ADSO-Bella-Italia

2. DIRECTORIO DE LA EVIDENCIA EN EL REPOSITORIO:
https://github.com/danilocampo/SENA-ADSO-Bella-Italia/tree/main/CDE/Evidencias/PET-043_GA10-220501097-AA2-EV01_Plan_Validacion_Hardware_Software

3. ARCHIVOS ENTREGABLES OFICIALES EN EL PAQUETE:
- Documento Principal en PDF: GA10-220501097-AA2-EV01_Plan_Validacion_Hardware.pdf
- Documento Editable en Word: GA10-220501097-AA2-EV01_Plan_Validacion_Hardware.docx
- Diagrama Infográfico Renderizado: diagrama_arquitectura_servidor_php_hardware.png
- Diagrama Vectorial SVG: diagrama_arquitectura_servidor_php_hardware.svg
- Informe Técnico Completo en Markdown: INFORME_PLAN_VALIDACION_HARDWARE_SOFTWARE.md
- Scripts de Auditoría Automatizada: auditar_hardware.js / validar_hardware_servidor.sh
- Registros de Auditoría: resultado_auditoria_hardware.json / resultado_auditoria_hardware.txt
--------------------------------------------------------------------------------
""")
print(f"[OK] enlace_repositorio.txt generado en: {repo_txt_path}")

# Empacar ZIP de entrega institucional
zip_name = 'KARENCAMPO_AA2_EV01_GUIA10.zip'
zip_path = os.path.join(ENTREGA_DIR, zip_name)
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, BASE_DIR)
            z.write(full_path, arcname=os.path.join('PET-043_GA10-AA2-EV01', rel_path))
    z.write(repo_txt_path, arcname='enlace_repositorio.txt')
print(f"[OK] Paquete ZIP generado exitosamente ({os.path.getsize(zip_path)/1024:.1f} KB): {zip_path}")
print("=== COMPILACIÓN FINALIZADA CON ÉXITO ===")
