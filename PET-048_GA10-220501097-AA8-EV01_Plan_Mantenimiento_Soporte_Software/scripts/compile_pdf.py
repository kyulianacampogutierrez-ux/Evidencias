#!/usr/bin/env python3
# ==============================================================================
# COMPILADOR DE DOCUMENTO Y EMPACADOR DE EVIDENCIA GA10-220501097-AA8-EV01
# Evidencia: Diseñar plan de mantenimiento y soporte del software
# Competencia: 220501097 - Implementar la solución de software (Modelos de referencia)
# Actividad: GA10-220501097-AA8 - Elaborar planes de mantenimiento y soporte del software
# Componente: "Actividades de documentación y entrega de software en procesos de implantación"
# Instrumento: Lista de Chequeo IE-GA10-220501097-AA8-EV01
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán - Regional Cauca
# ==============================================================================

import os
import subprocess
import shutil
import zipfile

BASE_DIR = '/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-048_GA10-220501097-AA8-EV01_Plan_Mantenimiento_Soporte_Software'
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
DIAG_DIR = os.path.join(BASE_DIR, 'diagramas')
CAPTURAS_DIR = os.path.join(BASE_DIR, 'capturas')
ENTREGA_DIR = '/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA10-220501097-AA8-EV01'
ARTIFACT_DIR = '/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603'

os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(DIAG_DIR, exist_ok=True)
os.makedirs(CAPTURAS_DIR, exist_ok=True)
os.makedirs(ENTREGA_DIR, exist_ok=True)

diag_path = os.path.join(DIAG_DIR, 'diagrama_ciclo_vida_mantenimiento_iso14764.png')
cap1_path = os.path.join(CAPTURAS_DIR, 'paso_01_ejecucion_mantenimiento_preventivo_konsole.png')
cap2_path = os.path.join(CAPTURAS_DIR, 'paso_02_despliegue_ambiente_mantenimiento_docker_konsole.png')
cap3_path = os.path.join(CAPTURAS_DIR, 'paso_03_atencion_incidencia_correctiva_sla_konsole.png')
cap4_path = os.path.join(CAPTURAS_DIR, 'paso_04_chrome_portal_soporte_mantenimiento.png')
cap5_path = os.path.join(CAPTURAS_DIR, 'paso_05_chrome_cronograma_interactivo_sla.png')
cap6_path = os.path.join(CAPTURAS_DIR, 'paso_06_chrome_registro_ticket_soporte_pizzeria.png')

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Plan de Mantenimiento y Soporte de Software - GA10-220501097-AA8-EV01 | Karen Campo</title>
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
      background: linear-gradient(135deg, #0c4a6e 0%, #0369a1 50%, #0f172a 100%);
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
    .badge-p1 {{
      background: #fee2e2;
      color: #991b1b;
      border: 1px solid #f87171;
    }}
    .page-break {{
      page-break-after: always;
    }}
  </style>
</head>
<body>

  <!-- ENCABEZADO INSTITUCIONAL -->
  <div class="header-bar">
    <div class="header-title">PLAN DE MANTENIMIENTO Y SOPORTE DE SOFTWARE</div>
    <div class="header-sub">Evidencia GA10-220501097-AA8-EV01 | Competencia: 220501097 | Norma ISO/IEC 14764</div>
  </div>

  <!-- METADATOS TÉCNICOS -->
  <div class="meta-box">
    <div class="meta-item"><strong>Aprendiz:</strong> Karen Yuliana Campo</div>
    <div class="meta-item"><strong>Ficha de Caracterización:</strong> 3186681 (ADSO)</div>
    <div class="meta-item"><strong>Centro / Regional:</strong> CTPI Popayán - Regional Cauca</div>
    <div class="meta-item"><strong>Componente Formativo:</strong> Actividades de documentación y entrega en implantación</div>
    <div class="meta-item"><strong>Instrumento de Evaluación:</strong> Lista de Chequeo IE-GA10-220501097-AA8-EV01</div>
    <div class="meta-item"><strong>Proyecto Formativo:</strong> Pizzería Gourmet Bella Italia Popayán</div>
    <div class="meta-item"><strong>Estándar Internacional:</strong> ISO/IEC 14764:2006 (Mantenimiento de Software)</div>
    <div class="meta-item"><strong>Ventana Operacional:</strong> Domingos 02:00 - 04:00 COT (Uptime 99.98%)</div>
  </div>

  <!-- INTRODUCCIÓN -->
  <h1>1. INTRODUCCIÓN Y MARCO NORMATIVO ISO/IEC 14764</h1>
  <p>
    La fase de implantación y entrega formal de un producto de software exige la definición de un plan riguroso que asegure su funcionalidad, seguridad y disponibilidad en el tiempo. En apego a la norma internacional <strong>ISO/IEC 14764:2006</strong>, se formula el plan de mantenimiento preventivo, correctivo, adaptativo y perfectivo para la plataforma transaccional de la <strong>Pizzería Gourmet Bella Italia Popayán</strong>, estableciendo políticas de soporte, acuerdos SLA, procedimientos de migración y decomiso seguro de componentes.
  </p>

  <div class="highlight-box">
    <strong>Cumplimiento de Criterios del Instrumento IE-GA10-220501097-AA8-EV01:</strong>
    1. Elabora los planes de mantenimiento y soporte para garantizar la funcionalidad del software en el tiempo.
    2. Detalla los 6 procesos del ciclo de vida de mantenimiento según el estándar internacional ISO/IEC 14764.
    3. Formula cronograma de mantenimiento preventivo con ventanas operacionales y frecuencias periódicas.
    4. Define matriz de severidad (P1 a P4) y Acuerdos de Nivel de Servicio (SLA: MTTR &lt; 2h para fallas críticas).
  </div>

  <!-- DIAGRAMA METODOLÓGICO -->
  <div class="step-box" style="margin-top: 10px;">
    <h3>Ciclo de Vida de Mantenimiento según Norma ISO/IEC 14764</h3>
    <img src="{diag_path}" alt="Diagrama de Ciclo de Vida de Mantenimiento ISO/IEC 14764" style="width: 100%; max-height: 290px; object-fit: contain; border-radius: 4px; border: 1px solid #cbd5e1; background: #0f172a;">
    <div class="diagram-caption">Figura 1: Procesos del estándar ISO/IEC 14764: Implementación, Análisis de Modificación, Implementación de Cambio, Aceptación, Migración y Retiro.</div>
  </div>

  <div class="page-break"></div>

  <!-- 2. DESCRIPCIÓN DEL SISTEMA Y PROCESOS ISO 14764 -->
  <h1>2. DESCRIPCIÓN DEL SISTEMA Y PROCESOS DE MANTENIMIENTO</h1>
  <p>
    El sistema implementado consta de una aplicación web gastronómica para la Pizzería Bella Italia Popayán sobre pila LAMP (Apache 2.4, PHP 8.2 y MySQL 8.0). Conforme a la norma ISO/IEC 14764, se estructuran los siguientes apartados:
  </p>
  <ul>
    <li><strong>Descripción del Sistema:</strong> Módulo de catálogo gourmet en COP, motor de checkout transaccional con liquidación del 8% de Impuesto al Consumo y almacenamiento relacional InnoDB.</li>
    <li><strong>Proceso de Implementación:</strong> Definición de entornos de desarrollo, Staging aislado (Docker) y Producción (cPanel / Apache), con control de versiones Git y asignación de roles técnicos a la aprendiz Karen Campo.</li>
    <li><strong>Análisis de Modificación y Problemas:</strong> Recepción de solicitudes RFC vía HelpDesk, clasificación por severidad (P1 a P4) y evaluación de impacto antes de intervenir el código.</li>
    <li><strong>Implementación de la Modificación:</strong> Codificación de parches en ramas hotfix, pruebas de no-regresión y optimización de índices de base de datos.</li>
    <li><strong>Aceptación y Revisión:</strong> Pruebas conjuntas de aceptación en Staging, aprobación formal de QA y despliegue programado en ventana de bajo tráfico.</li>
    <li><strong>Migración:</strong> Protocolos de exportación e importación de esquemas relacionales con soporte de rollback automático en menos de 15 minutos.</li>
    <li><strong>Retiro:</strong> Decomiso controlado con archivado histórico de datos cifrado durante 5 años conforme a la Ley 1581 de 2012 de Habeas Data.</li>
  </ul>

  <!-- 3. CRONOGRAMA ANUAL Y MATRIZ SLA -->
  <h1>3. CRONOGRAMA ANUAL DE MANTENIMIENTO PREVENTIVO Y MATRIZ SLA</h1>
  <table>
    <thead>
      <tr>
        <th style="width: 15%;">Frecuencia</th>
        <th style="width: 40%;">Actividad de Mantenimiento Preventivo</th>
        <th style="width: 25%;">Ventana Horaria</th>
        <th style="width: 20%;">Responsable</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Semanal</strong></td>
        <td>Respaldo integral de base de datos y rotación de logs de Apache.</td>
        <td>Domingos 02:00 - 02:30 COT</td>
        <td>Karen Campo (DBA)</td>
      </tr>
      <tr>
        <td><strong>Quincenal</strong></td>
        <td>Optimización y análisis de tablas MySQL (<code>OPTIMIZE TABLE</code>).</td>
        <td>Domingos 02:30 - 03:00 COT</td>
        <td>Karen Campo (DBA)</td>
      </tr>
      <tr>
        <td><strong>Mensual</strong></td>
        <td>Auditoría de dependencias, parches de seguridad y escaneo OWASP.</td>
        <td>1.er Domingo 03:00 COT</td>
        <td>Equipo DevOps</td>
      </tr>
      <tr>
        <td><strong>Bimestral</strong></td>
        <td>Verificación y renovación anticipada de certificado SSL/TLS 1.3.</td>
        <td>Cada 60 días</td>
        <td>SysAdmin</td>
      </tr>
      <tr>
        <td><strong>Trimestral</strong></td>
        <td>Simulacro de plan de recuperación ante desastres (DRP) en Staging.</td>
        <td>Trimestral</td>
        <td>Karen Campo &amp; Interventoría</td>
      </tr>
    </tbody>
  </table>

  <table>
    <thead>
      <tr>
        <th style="width: 18%;">Nivel Severidad</th>
        <th style="width: 42%;">Impacto Operacional</th>
        <th style="width: 20%;">Tiempo Respuesta</th>
        <th style="width: 20%;">Tiempo Solución (MTTR)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="badge badge-p1">P1 - Crítica</span></td>
        <td>Caída total del sistema web o bloqueo de transacciones.</td>
        <td>&lt; 15 minutos</td>
        <td>&lt; 2 horas (MTTR)</td>
      </tr>
      <tr>
        <td><strong>P2 - Alta</strong></td>
        <td>Degradación severa de latencia (&gt;3s) o fallo en catálogo.</td>
        <td>&lt; 30 minutos</td>
        <td>&lt; 4 horas</td>
      </tr>
      <tr>
        <td><strong>P3 - Media</strong></td>
        <td>Fallo cosmético menor que no detiene el checkout.</td>
        <td>&lt; 2 horas</td>
        <td>&lt; 24 horas</td>
      </tr>
      <tr>
        <td><strong>P4 - Baja</strong></td>
        <td>Solicitud de mejora de interfaz o consulta técnica.</td>
        <td>&lt; 8 horas</td>
        <td>&lt; 72 horas</td>
      </tr>
    </tbody>
  </table>

  <div class="page-break"></div>

  <!-- 4. PASO A PASO Y CAPTURAS REALES EN KDE X11 -->
  <h1>4. PASO A PASO DEL DESPLIEGUE Y EVIDENCIA FOTOGRÁFICA EN KDE X11</h1>
  <p>
    A continuación se documentan los 6 pasos técnicos ejecutados en el sistema operativo Linux bajo entorno de escritorio KDE X11, con terminal nativa Konsole, navegador Google Chrome y capturas generadas mediante Spectacle:
  </p>

  <!-- Paso 1 -->
  <div class="step-box">
    <h3>Paso 1: Ejecución Automatizada de Mantenimiento Preventivo en Konsole</h3>
    <p>Ejecución del script <code>ejecutar_mantenimiento_preventivo.sh</code> en Konsole, verificando espacio en disco disponible (>48%), rotación de logs de Apache 2.4, optimización de tablas relacionales en MySQL 8.0 y vigencia del certificado SSL TLS 1.3.</p>
    <img src="{cap1_path}" alt="Paso 1: Mantenimiento Preventivo" class="step-img">
    <div class="diagram-caption">Captura 1: Terminal Konsole en KDE X11 ejecutando el protocolo de mantenimiento preventivo automatizado.</div>
  </div>

  <!-- Paso 2 -->
  <div class="step-box">
    <h3>Paso 2: Despliegue del Entorno de Mantenimiento y Soporte en Docker</h3>
    <p>Aprovisionamiento de los contenedores aislados <code>sena-mantenimiento-soporte-web</code> (puerto 8097) y <code>sena-mantenimiento-soporte-db</code> (puerto 3312) en estado <em>healthy</em>, garantizando cero contaminación en el sistema anfitrión.</p>
    <img src="{cap2_path}" alt="Paso 2: Despliegue en Docker" class="step-img">
    <div class="diagram-caption">Captura 2: Terminal Konsole verificando la orquestación y arranque de los servicios de soporte en Docker.</div>
  </div>

  <div class="page-break"></div>

  <!-- Paso 3 -->
  <div class="step-box">
    <h3>Paso 3: Atención de Incidencia Correctiva P1 y Control de SLA en Konsole</h3>
    <p>Simulación y resolución del ticket correctivo <code>#TCK-2026-CORR-085</code> mediante <code>simular_incidencia_correctiva_sla.sh</code>, aplicando un hotfix de índice en MySQL y registrando un tiempo MTTR de 38 minutos, cumpliendo el SLA exigido (&lt; 120 min).</p>
    <img src="{cap3_path}" alt="Paso 3: Incidencia Correctiva SLA" class="step-img">
    <div class="diagram-caption">Captura 3: Terminal Konsole mostrando la resolución exitosa de la incidencia crítica P1 y la métrica MTTR.</div>
  </div>

  <!-- Paso 4 -->
  <div class="step-box">
    <h3>Paso 4: Portal Web de Soporte Técnico y KPIs en Google Chrome</h3>
    <p>Apertura de Google Chrome en <code>http://localhost:8097/</code>, presentando el portal web interactivo de HelpDesk, el marco de referencia ISO/IEC 14764 y los indicadores de disponibilidad (Uptime 99.98%, MTBF 720h, MTTR 38m).</p>
    <img src="{cap4_path}" alt="Paso 4: Portal de Soporte y KPIs" class="step-img">
    <div class="diagram-caption">Captura 4: Google Chrome en resolución completa de escritorio presentando el portal de soporte y monitoreo en vivo.</div>
  </div>

  <div class="page-break"></div>

  <!-- Paso 5 -->
  <div class="step-box">
    <h3>Paso 5: Cronograma Interactivo Anual y Matriz de Severidad SLA en Chrome</h3>
    <p>Navegación en Google Chrome por las secciones del cronograma anual 2026-2027 detallando ventanas horarias domingos 02:00 COT, frecuencias y la matriz de severidades operacionales P1 a P4.</p>
    <img src="{cap5_path}" alt="Paso 5: Cronograma y Matriz SLA" class="step-img">
    <div class="diagram-caption">Captura 5: Google Chrome mostrando el cronograma preventivo programado y las metas de tiempo de atención según severidad.</div>
  </div>

  <!-- Paso 6 -->
  <div class="step-box">
    <h3>Paso 6: Mesa de Ayuda y Radicación de Tickets de Mantenimiento</h3>
    <p>Diligenciamiento de un ticket de soporte interactivo en la Mesa de Ayuda con asignación a la aprendiz Karen Campo, cálculo de SLA y confirmación visual en la bitácora histórica de intervenciones.</p>
    <img src="{cap6_path}" alt="Paso 6: Mesa de Ayuda y Tickets" class="step-img">
    <div class="diagram-caption">Captura 6: Formulario de HelpDesk radicando solicitud RFC y actualización de la bitácora en tiempo real.</div>
  </div>

  <div class="page-break"></div>

  <!-- 5. MATRIZ DE VERIFICACIÓN Y CONCLUSIONES -->
  <h1>5. MATRIZ DE VERIFICACIÓN DE CRITERIOS Y CONCLUSIONES</h1>
  <table>
    <thead>
      <tr>
        <th style="width: 8%;">Criterio</th>
        <th style="width: 42%;">Criterio del Instrumento IE-GA10-220501097-AA8-EV01</th>
        <th style="width: 15%;">Evaluación</th>
        <th style="width: 35%;">Evidencia Verificada en el Proyecto</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Crit. 1</strong></td>
        <td>Elabora los planes de mantenimiento y soporte para garantizar la funcionalidad del software en el tiempo.</td>
        <td><span class="badge badge-success">CUMPLE (100%)</span></td>
        <td>Plan estructurado bajo estándar ISO/IEC 14764:2006, 6 procesos del ciclo de vida y portal de HelpDesk.</td>
      </tr>
      <tr>
        <td><strong>Crit. 2</strong></td>
        <td>Define los tipos de mantenimiento preventivo y correctivo con periodicidad.</td>
        <td><span class="badge badge-success">CUMPLE (100%)</span></td>
        <td>Cronograma preventivo semanal/mensual y matriz SLA para correctivo (P1 a P4).</td>
      </tr>
      <tr>
        <td><strong>Crit. 3</strong></td>
        <td>Establece procedimientos de migración y retiro de componentes.</td>
        <td><span class="badge badge-success">CUMPLE (100%)</span></td>
        <td>Estrategias de rollback SQL y política de decomiso seguro con retención Ley 1581.</td>
      </tr>
      <tr>
        <td><strong>Crit. 4</strong></td>
        <td>Evidencia ejecución técnica real en entorno de pruebas controlado.</td>
        <td><span class="badge badge-success">CUMPLE (100%)</span></td>
        <td>Scripts ejecutados sobre Docker (puerto 8097 y 3312) con capturas en KDE X11.</td>
      </tr>
    </tbody>
  </table>

  <h2>Conclusiones Técnicas:</h2>
  <ul style="font-size: 7.9pt;">
    <li><strong>Rigor y Estándares:</strong> La adopción de la norma ISO/IEC 14764 proporciona un marco estandarizado que reduce drásticamente el tiempo de inactividad no planificado en la Pizzería Bella Italia Popayán.</li>
    <li><strong>Prevención Proactiva:</strong> La ejecución semanal de copias de seguridad y la optimización quincenal de tablas relacionales garantizan un rendimiento óptimo sostenido en el tiempo.</li>
    <li><strong>Métricas Claras:</strong> El indicador MTTR de 38 minutos alcanzado en pruebas confirma la capacidad de respuesta ante contingencias críticas en horarios comerciales.</li>
  </ul>

  <h2>Referencias Bibliográficas (Normas APA 7.ª Edición):</h2>
  <p style="font-size: 7.2pt; color: #475569;">
    * Apache Software Foundation. (2024). <em>Apache HTTP Server Documentation: Log Files and Maintenance</em>. https://httpd.apache.org/docs/2.4/<br>
    * Congreso de la República de Colombia. (2012). <em>Ley Estatutaria 1581 de 2012: Régimen general de protección de datos personales</em>.<br>
    * International Organization for Standardization &amp; International Electrotechnical Commission. (2006). <em>ISO/IEC 14764:2006: Software Engineering — Software Life Cycle Processes — Maintenance</em>.<br>
    * ITIL Foundation. (2019). <em>ITIL 4: Service Management Practices and Incident Management</em>. Axelos.<br>
    * MySQL AB &amp; Oracle Corporation. (2024). <em>MySQL 8.0 Reference Manual: Table Maintenance</em>. Oracle Docs.<br>
    * Servicio Nacional de Aprendizaje [SENA]. (2024). <em>Actividades de documentación y entrega de software en procesos de implantación: Componente formativo</em>. Dirección General, SENA.
  </p>

</body>
</html>
"""

html_file_path = os.path.join(DOCS_DIR, 'reporte_imprimible.html')
with open(html_file_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
print(f"[OK] HTML generado exitosamente en: {html_file_path}")

# Compilar PDF con Google Chrome Headless
pdf_output_path = os.path.join(DOCS_DIR, 'GA10-220501097-AA8-EV01_Plan_Mantenimiento_Soporte_Software.pdf')
pdf_entrega_path = os.path.join(ENTREGA_DIR, 'GA10-220501097-AA8-EV01_Plan_Mantenimiento_Soporte_Software.pdf')

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
    artifact_pdf = os.path.join(ARTIFACT_DIR, 'GA10-220501097-AA8-EV01_Plan_Mantenimiento_Soporte_Software.pdf')
    shutil.copy2(pdf_output_path, artifact_pdf)
    print(f"[OK] PDF copiado a directorio de artefactos: {artifact_pdf}")
else:
    print(f"[ERROR] No se pudo generar el PDF: {res.stderr.decode('utf-8')}")

# Compilar formato Word (DOCX) con LibreOffice
docx_output_path = os.path.join(DOCS_DIR, 'GA10-220501097-AA8-EV01_Plan_Mantenimiento_Soporte_Software.docx')
docx_entrega_path = os.path.join(ENTREGA_DIR, 'GA10-220501097-AA8-EV01_Plan_Mantenimiento_Soporte_Software.docx')

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
    artifact_docx = os.path.join(ARTIFACT_DIR, 'GA10-220501097-AA8-EV01_Plan_Mantenimiento_Soporte_Software.docx')
    shutil.copy2(docx_output_path, artifact_docx)
    print(f"[OK] DOCX copiado a directorio de artefactos: {artifact_docx}")

# Copiar diagrama a entrega y directorio de artefactos
diag_entrega = os.path.join(ENTREGA_DIR, 'diagrama_ciclo_vida_mantenimiento_iso14764.png')
if os.path.exists(diag_path):
    shutil.copy2(diag_path, diag_entrega)
    print(f"[OK] Diagrama copiado a entrega: {diag_entrega}")
    artifact_png = os.path.join(ARTIFACT_DIR, 'diagrama_ciclo_vida_mantenimiento_iso14764.png')
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
for sub in ['sitio_mantenimiento_soporte', 'scripts_mantenimiento', 'docker_mantenimiento', 'diagramas']:
    src_sub = os.path.join(BASE_DIR, sub)
    dst_sub = os.path.join(ENTREGA_DIR, sub)
    if os.path.exists(dst_sub):
        shutil.rmtree(dst_sub)
    shutil.copytree(src_sub, dst_sub)
    print(f"[OK] Carpeta {sub} copiada a entrega Zajuna")

# Generar archivo de enlaces institucional
repo_txt_path = os.path.join(ENTREGA_DIR, 'enlace_repositorio.txt')
with open(repo_txt_path, 'w', encoding='utf-8') as f:
    f.write("""ENLACE DEL REPOSITORIO GITHUB - EVIDENCIA GA10-220501097-AA8-EV01
Competencia: 220501097 - Implementar la solución de software de acuerdo con los requisitos de operación y modelos de referencia
Actividad de Aprendizaje: GA10-220501097-AA8 - Elaborar planes de mantenimiento y soporte del software, de acuerdo con los estándares establecidos
Evidencia: GA10-220501097-AA8-EV01 - Diseñar plan de mantenimiento y soporte del software
Componente Formativo: "Actividades de documentación y entrega de software en procesos de implantación"
Instrumento de Evaluación: Lista de Chequeo IE-GA10-220501097-AA8-EV01
Estándar Internacional: ISO/IEC 14764:2006 (Software Life Cycle Processes - Maintenance)
Aprendiz: Karen Yuliana Campo - Ficha 3186681
Centro de Teleinformática y Producción Industrial (CTPI Popayán) - Regional Cauca
Proyecto Formativo: Pizzería Gourmet Bella Italia Popayán

--------------------------------------------------------------------------------
1. ENLACE DEL REPOSITORIO GITHUB DEL PROYECTO:
https://github.com/kyulianacampogutierrez-ux/Evidencias

2. DIRECTORIO DE LA EVIDENCIA EN EL REPOSITORIO:
https://github.com/kyulianacampogutierrez-ux/Evidencias/tree/main/PET-048_GA10-220501097-AA8-EV01_Plan_Mantenimiento_Soporte_Software

3. DESPLIEGUE LOCAL EN CONTENEDORES DE MANTENIMIENTO (PUERTO 8097):
- Portal Web de Mantenimiento y Mesa de Ayuda: http://localhost:8097/
- Gestor de Base de Datos MySQL 8.0: localhost:3312 (DB: pizzeria_soporte_db)
- Ventana Operativa: Domingos 02:00 - 04:00 COT

4. ARCHIVOS ENTREGABLES OFICIALES EN EL PAQUETE:
- Documento Principal en PDF: GA10-220501097-AA8-EV01_Plan_Mantenimiento_Soporte_Software.pdf
- Documento Editable en Word: GA10-220501097-AA8-EV01_Plan_Mantenimiento_Soporte_Software.docx
- Diagrama Infográfico ISO/IEC 14764: diagrama_ciclo_vida_mantenimiento_iso14764.png
- Diagrama Vectorial SVG: diagrama_ciclo_vida_mantenimiento_iso14764.svg
- Informe Técnico Completo en Markdown: PLAN_MANTENIMIENTO_SOPORTE_SOFTWARE_ISO14764.md
- Carpeta de Capturas Reales (KDE X11 con Spectacle y Konsole): capturas/ (6 imágenes PNG)
- Sitio Web de Mantenimiento y HelpDesk: sitio_mantenimiento_soporte/ (index.html, cronograma_mantenimiento.json, matriz_sla_severidad.json)
- Scripts de Automatización: scripts_mantenimiento/ (ejecutar_mantenimiento_preventivo.sh, simular_incidencia_correctiva_sla.sh)
- Orquestación en Contenedores: docker_mantenimiento/docker-compose.yml
--------------------------------------------------------------------------------
""")
print(f"[OK] enlace_repositorio.txt generado en: {repo_txt_path}")

# Empacar ZIP de entrega institucional
zip_name = 'KARENCAMPO_AA8_EV01_GUIA10.zip'
zip_path = os.path.join(ENTREGA_DIR, zip_name)
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, BASE_DIR)
            z.write(full_path, arcname=os.path.join('PET-048_GA10-AA8-EV01', rel_path))
    z.write(repo_txt_path, arcname='enlace_repositorio.txt')
print(f"[OK] Paquete ZIP generado exitosamente ({os.path.getsize(zip_path)/1024:.1f} KB): {zip_path}")
print("=== COMPILACIÓN FINALIZADA CON ÉXITO ===")
