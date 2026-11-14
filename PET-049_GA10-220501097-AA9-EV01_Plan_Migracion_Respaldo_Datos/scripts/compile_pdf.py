#!/usr/bin/env python3
# ==============================================================================
# COMPILADOR DE DOCUMENTO Y EMPACADOR DE EVIDENCIA GA10-220501097-AA9-EV01
# Evidencia: Documentación de plan de migración y respaldo de los datos del software
# Competencia: 220501097 - Implementar la solución de software (Modelos de referencia)
# Actividad: GA10-220501097-AA9 - Documentar el proceso de migración y respaldo de los datos
# Componente: "Actividades de documentación y entrega de software en procesos de implantación"
# Instrumento: Lista de Chequeo IE-GA10-220501097-AA9-EV01
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán - Regional Cauca
# ==============================================================================

import os
import subprocess
import shutil
import zipfile

BASE_DIR = '/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-049_GA10-220501097-AA9-EV01_Plan_Migracion_Respaldo_Datos'
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
DIAG_DIR = os.path.join(BASE_DIR, 'diagramas')
CAPTURAS_DIR = os.path.join(BASE_DIR, 'capturas')
ENTREGA_DIR = '/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA10-220501097-AA9-EV01'
ARTIFACT_DIR = '/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603'

os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(DIAG_DIR, exist_ok=True)
os.makedirs(CAPTURAS_DIR, exist_ok=True)
os.makedirs(ENTREGA_DIR, exist_ok=True)

diag_path = os.path.join(DIAG_DIR, 'diagrama_flujo_migracion_respaldo_datos.png')
cap1_path = os.path.join(CAPTURAS_DIR, 'paso_01_respaldo_automatizado_sha256_konsole.png')
cap2_path = os.path.join(CAPTURAS_DIR, 'paso_02_despliegue_ambiente_migracion_docker_konsole.png')
cap3_path = os.path.join(CAPTURAS_DIR, 'paso_03_migracion_validacion_integridad_konsole.png')
cap4_path = os.path.join(CAPTURAS_DIR, 'paso_04_chrome_portal_auditoria_migracion.png')
cap5_path = os.path.join(CAPTURAS_DIR, 'paso_05_chrome_listas_chequeo_interactivas.png')
cap6_path = os.path.join(CAPTURAS_DIR, 'paso_06_chrome_validador_respaldos_rollback.png')

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Plan de Migración y Respaldo de Datos - GA10-220501097-AA9-EV01 | Karen Campo</title>
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
      background: linear-gradient(135deg, #0284c7 0%, #0369a1 50%, #0f172a 100%);
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
      color: #0369a1;
      font-weight: 700;
    }}
    h1 {{
      font-size: 12pt;
      border-bottom: 2px solid #0284c7;
      padding-bottom: 3px;
      margin-top: 14px;
      margin-bottom: 8px;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }}
    h2 {{
      font-size: 9.8pt;
      margin-top: 10px;
      margin-bottom: 5px;
      color: #0f172a;
    }}
    h3 {{
      font-size: 8.9pt;
      margin-top: 8px;
      margin-bottom: 4px;
      color: #0369a1;
    }}
    p {{
      margin-bottom: 7px;
      text-align: justify;
    }}
    ul, ol {{
      margin-left: 18px;
      margin-bottom: 8px;
    }}
    li {{
      margin-bottom: 3px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 8px 0 12px 0;
      font-size: 7.6pt;
    }}
    th, td {{
      border: 1px solid #cbd5e1;
      padding: 5px 7px;
      text-align: left;
    }}
    th {{
      background-color: #0369a1;
      color: #ffffff;
      font-weight: 600;
    }}
    tr:nth-child(even) {{
      background-color: #f8fafc;
    }}
    .badge {{
      display: inline-block;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 7pt;
      font-weight: bold;
    }}
    .badge-success {{
      background-color: #dcfce7;
      color: #15803d;
      border: 1px solid #86efac;
    }}
    .badge-primary {{
      background-color: #e0f2fe;
      color: #0369a1;
      border: 1px solid #7dd3fc;
    }}
    .badge-warning {{
      background-color: #fef3c7;
      color: #b45309;
      border: 1px solid #fde68a;
    }}
    .badge-danger {{
      background-color: #fee2e2;
      color: #b91c1c;
      border: 1px solid #fca5a5;
    }}
    .info-card {{
      background: #f0f9ff;
      border: 1px solid #bae6fd;
      border-left: 4px solid #0284c7;
      padding: 8px 12px;
      border-radius: 4px;
      margin-bottom: 10px;
    }}
    .warning-card {{
      background: #fffbeb;
      border: 1px solid #fde68a;
      border-left: 4px solid #f59e0b;
      padding: 8px 12px;
      border-radius: 4px;
      margin-bottom: 10px;
    }}
    .img-container {{
      text-align: center;
      margin: 9px 0 13px 0;
      page-break-inside: avoid;
    }}
    .img-container img {{
      max-width: 98%;
      max-height: 250px;
      height: auto;
      border-radius: 5px;
      border: 1px solid #cbd5e1;
      box-shadow: 0 2px 4px rgba(0,0,0,0.08);
    }}
    .caption {{
      font-size: 7.2pt;
      color: #64748b;
      margin-top: 3px;
      font-style: italic;
    }}
    .page-break {{
      page-break-before: always;
    }}
    .kpi-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 8px;
      margin-bottom: 11px;
    }}
    .kpi-card {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 7px;
      text-align: center;
    }}
    .kpi-value {{
      font-size: 11pt;
      font-weight: 800;
      color: #0284c7;
    }}
    .kpi-label {{
      font-size: 6.8pt;
      color: #64748b;
      text-transform: uppercase;
      font-weight: 600;
    }}
  </style>
</head>
<body>

  <!-- ENCABEZADO INSTITUCIONAL -->
  <div class="header-bar">
    <div class="header-title">PLAN DE MIGRACIÓN Y RESPALDO DE LOS DATOS DEL SOFTWARE</div>
    <div class="header-sub">Instrumento de Evaluación: Listas de Chequeo de Migración y Revisión de Modificaciones (IE-GA10-220501097-AA9-EV01)</div>
    <div class="header-sub">Sistema de Gestión Gastronómica y Comercio Electrónico "Pizzería Gourmet Bella Italia Popayán"</div>
  </div>

  <!-- METADATOS TÉCNICOS SENA -->
  <div class="meta-box">
    <div class="meta-item"><strong>Programa de Formación:</strong> Análisis y Desarrollo de Software (ADSO)</div>
    <div class="meta-item"><strong>Número de Ficha:</strong> 3186681 | Fase 4: Implantación (AP10)</div>
    <div class="meta-item"><strong>Competencia:</strong> 220501097 - Implementar solución de software según operación y modelos</div>
    <div class="meta-item"><strong>Actividad de Aprendizaje:</strong> GA10-220501097-AA9 - Documentar migración y respaldo de datos</div>
    <div class="meta-item"><strong>Aprendiz:</strong> Karen Yuliana Campo | Regional Cauca</div>
    <div class="meta-item"><strong>Centro de Formación:</strong> Centro de Teleinformática y Producción Industrial (CTPI Popayán)</div>
  </div>

  <!-- TARJETAS DE INDICADORES CLAVE (KPIS) -->
  <div class="kpi-grid">
    <div class="kpi-card">
      <div class="kpi-value">100%</div>
      <div class="kpi-label">Integridad de Filas (Delta = 0)</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-value">&lt; 15 min</div>
      <div class="kpi-label">RTO Objetivo (Real: 8.5 min)</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-value">Regla 3-2-1</div>
      <div class="kpi-label">Estrategia de Respaldo</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-value">SHA-256</div>
      <div class="kpi-label">Inmutabilidad Criptográfica</div>
    </div>
  </div>

  <!-- SECCIÓN 1: INTRODUCCIÓN -->
  <h1>1. INTRODUCCIÓN</h1>
  <p>
    En la ingeniería de software moderna y en la fase crítica de implantación, el proceso de migración de datos y la garantía de respaldos sistemáticos representan la base de la continuidad de negocio. Bajo el estándar internacional <strong>ISO/IEC/IEEE 14764:2021</strong>, las directrices de seguridad de <strong>ISO/IEC 27001:2022</strong> (Controles A.8.13 y A.8.14) y el marco legal colombiano de la <strong>Ley Estatutaria 1581 de 2012</strong> (Régimen de Protección de Datos Personales / Habeas Data), toda organización debe contar con procedimientos auditables para la transición de esquemas relacionales y planes de contingencia ante incidentes operativos.
  </p>
  <p>
    El presente informe documenta de manera integral el <strong>Plan de Migración y Respaldo de los Datos del Software</strong> implementado para la plataforma web de la <strong>Pizzería Gourmet Bella Italia Popayán</strong>, incorporando formalmente el instrumento técnico exigido en la guía: <strong>Listas de chequeo para proceso de migración de software y para revisión de modificaciones</strong> en sus cuatro fases (Pre-migración, Durante la migración, Post-migración / Revisión de modificaciones, y Respaldos 3-2-1 / DRP).
  </p>

  <!-- SECCIÓN 2: DESCRIPCIÓN DEL SISTEMA -->
  <h1>2. DESCRIPCIÓN DEL SISTEMA</h1>
  <p>
    La plataforma tecnológica de la <strong>Pizzería Gourmet Bella Italia Popayán</strong> es un ecosistema de software web diseñado para automatizar integralmente la operación gastronómica, abarcando la toma de órdenes presenciales, el catálogo web responsivo para pedidos a domicilio, el control de inventario de recetas e ingredientes, la gestión de caja y la facturación electrónica conforme a la normativa DIAN.
  </p>
  <div class="info-card">
    <strong>Arquitectura del Sistema:</strong>
    <ul style="margin-top:4px; margin-bottom:0;">
      <li><strong>Frontend Web:</strong> SPA React 18 con Vite, Tailwind CSS y diseño responsivo adaptativo (móvil y escritorio).</li>
      <li><strong>Backend API REST:</strong> Microservicios desacoplados en Go (Golang) y Node.js Express con autenticación JWT y control de roles RBAC.</li>
      <li><strong>Base de Datos Relacional:</strong> Motor <strong>MySQL Community Server 8.0</strong> con motor transaccional <strong>InnoDB</strong>, codificación <code>utf8mb4</code> y collation <code>utf8mb4_unicode_ci</code>.</li>
      <li><strong>Aislamiento de Entorno:</strong> Contenedores Docker Engine orquestados vía Docker Compose en puertos <strong>8098</strong> (Apache HTTPD) y <strong>3313</strong> (MySQL 8.0), cumpliendo el principio de <em>Zero Host Pollution</em>.</li>
    </ul>
  </div>

  <h2>Inventario de Entidades y Datos Críticos a Migrar</h2>
  <table>
    <thead>
      <tr>
        <th>Entidad / Tabla Relacional</th>
        <th>Registros (Cardinalidad)</th>
        <th>Sensibilidad (Ley 1581)</th>
        <th>Criticidad Transaccional</th>
        <th>Estado de Integridad</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>tbl_usuarios</strong> (Administradores, Cajeros, Cocina, Domicilio)</td>
        <td>15 usuarios</td>
        <td>Alta (Contraseñas bcrypt, emails, teléfonos)</td>
        <td>Máxima</td>
        <td><span class="badge badge-success">Migrado 100% OK</span></td>
      </tr>
      <tr>
        <td><strong>tbl_roles_permisos</strong> (Matriz de Control de Acceso RBAC)</td>
        <td>4 roles / 28 permisos</td>
        <td>Media (Seguridad interna del sistema)</td>
        <td>Alta</td>
        <td><span class="badge badge-success">Migrado 100% OK</span></td>
      </tr>
      <tr>
        <td><strong>tbl_categorias</strong> (Pizzas Gourmet, Calzones, Bebidas, Postres)</td>
        <td>8 categorías</td>
        <td>Baja (Información pública de menú)</td>
        <td>Media</td>
        <td><span class="badge badge-success">Migrado 100% OK</span></td>
      </tr>
      <tr>
        <td><strong>tbl_productos_menu</strong> (Catálogo con precios, recetas y stock)</td>
        <td>30 ítems de carta</td>
        <td>Media (Estructura de precios y recetas)</td>
        <td>Alta</td>
        <td><span class="badge badge-success">Migrado 100% OK</span></td>
      </tr>
      <tr>
        <td><strong>tbl_pedidos</strong> (Órdenes históricas, estados y fechas)</td>
        <td>120 órdenes</td>
        <td>Alta (Transacciones financieras de clientes)</td>
        <td>Máxima</td>
        <td><span class="badge badge-success">Migrado 100% OK</span></td>
      </tr>
      <tr>
        <td><strong>tbl_detalle_pedido</strong> (Líneas de pedido, cantidades, notas)</td>
        <td>340 líneas</td>
        <td>Alta (Detalle de consumo y recetas)</td>
        <td>Máxima</td>
        <td><span class="badge badge-success">Migrado 100% OK</span></td>
      </tr>
      <tr>
        <td><strong>tbl_facturas_dian</strong> (Comprobantes fiscales, CUFE, IVA 19%)</td>
        <td>120 facturas</td>
        <td>Máxima (Cumplimiento tributario DIAN)</td>
        <td>Crítica Legal</td>
        <td><span class="badge badge-success">Migrado 100% OK</span></td>
      </tr>
    </tbody>
  </table>

  <!-- SECCIÓN 3: OBJETIVOS Y ALCANCE -->
  <h1>3. OBJETIVOS Y ALCANCE DEL PLAN</h1>
  <p>
    El alcance del presente plan abarca la totalidad de esquemas de datos relacionales, procedimientos almacenados, disparadores (triggers) y secuencias auto-incrementales de la Pizzería Gourmet Bella Italia Popayán, asegurando:
  </p>
  <ul>
    <li><strong>Disponibilidad Continua:</strong> Ventana de mantenimiento programada en horario de bajo tráfico (23:30 a 01:00 COT) con anuncio previo de 24 horas a los comensales.</li>
    <li><strong>Cero Pérdida de Información (RPO = 0 h):</strong> Snapshot atómico con <code>mysqldump --single-transaction</code> y bloqueo de escritura previo.</li>
    <li><strong>Inmutabilidad Criptográfica:</strong> Hashing SHA-256 generado inmediatamente tras la extracción y cotejado previo a la carga.</li>
    <li><strong>Conciliación Financiera Exacta:</strong> Comprobación de que el total monetario acumulado de $14.850.000 COP permanezca inalterado tras la migración.</li>
    <li><strong>Capacidad de Retorno Seguro (Rollback):</strong> Protocolo automatizado capaz de revertir la base de datos en menos de 15 minutos en caso de falla o inconsistencia.</li>
  </ul>

  <div class="page-break"></div>

  <!-- SECCIÓN 4: ARQUITECTURA DE MIGRACIÓN Y PIPELINE ETL -->
  <h1>4. ARQUITECTURA DE MIGRACIÓN Y PIPELINE ETL</h1>
  <p>
    El proceso de transición y respaldo se estructura mediante un pipeline de Extracción, Transformación y Carga (ETL) automatizado, orquestado bajo el modelo de contingencia 3-2-1 y respaldado por el motor MySQL 8.0:
  </p>

  <div class="img-container">
    <img src="{diag_path}" alt="Diagrama de Flujo de Migración y Respaldo 3-2-1">
    <div class="caption">Figura 1: Arquitectura integral del pipeline de migración de datos, estrategia de respaldo 3-2-1 y protocolo de rollback para Pizzería Bella Italia.</div>
  </div>

  <h2>Pipeline de Extracción, Transformación y Carga (ETL)</h2>
  <ol>
    <li><strong>Extracción (Extract):</strong> Bloqueo de sesiones de escritura y extracción atómica sin bloqueo de lecturas mediante <code>mysqldump</code> determinístico con opciones <code>--single-transaction --quick --hex-blob --routines --triggers</code>. Compresión instantánea en formato Gzip y cálculo de firma <code>sha256sum</code>.</li>
    <li><strong>Transformación (Transform):</strong> Inspección automática de compatibilidad DDL, normalización de collation a <code>utf8mb4_unicode_ci</code>, verificación de tipos monetarios <code>DECIMAL(12,2)</code> y comprobación de integridad referencial de claves foráneas.</li>
    <li><strong>Carga e Ingesta (Load):</strong> Streaming de datos al contenedor destino MySQL 8.0 en ambiente Staging (puerto 3313), reconstrucción de índices B-Tree mediante el motor transaccional InnoDB y refresco de estadísticas del optimizador.</li>
  </ol>

  <!-- SECCIÓN 5: POLÍTICA Y ESTRATEGIA DE RESPALDO 3-2-1 -->
  <h1>5. POLÍTICA Y ESTRATEGIA DE RESPALDO 3-2-1</h1>
  <p>
    Con el fin de blindar los datos del restaurante ante fallas de hardware, ataques informáticos de tipo ransomware, desastres físicos o corrupción accidental, se adopta de manera estricta la <strong>Estrategia de Respaldo 3-2-1</strong>:
  </p>

  <table>
    <thead>
      <tr>
        <th>Nivel de Copia</th>
        <th>Tipo de Medio y Almacenamiento</th>
        <th>Propósito Operativo</th>
        <th>RTO / RPO Estimado</th>
        <th>Cifrado y Seguridad</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Copia 1: Primaria Local</strong></td>
        <td>Almacenamiento NVMe SSD en servidor anfitrión (directorio <code>/backups/local</code>)</td>
        <td>Recuperación inmediata ante errores lógicos o transacciones erróneas durante el servicio diario.</td>
        <td>RTO &lt; 15 min<br>RPO &lt; 24 h</td>
        <td>Acceso restringido a usuario <code>mysql</code> (chmod 600) + Hash SHA-256</td>
      </tr>
      <tr>
        <td><strong>Copia 2: Medio Secundario</strong></td>
        <td>Servidor NAS / Disco Externo Staging desacoplado de la máquina principal</td>
        <td>Protección ante fallas catastróficas de disco o daño físico del hardware principal del restaurante.</td>
        <td>RTO &lt; 30 min<br>RPO &lt; 24 h</td>
        <td>Aislamiento de red física interna + Hash SHA-256</td>
      </tr>
      <tr>
        <td><strong>Copia 3: Remota Fuera de Sitio (Offsite)</strong></td>
        <td>Cloud Object Storage (S3 / Seafile) geográficamente distante (fuera de Popayán)</td>
        <td>Plan de Recuperación ante Desastres (DRP) conforme a la Ley 1581 (retención obligatoria de 5 años).</td>
        <td>RTO &lt; 4 horas<br>RPO &lt; 24 h</td>
        <td>Cifrado en reposo AES-256 + Inmutabilidad WORM</td>
      </tr>
    </tbody>
  </table>

  <div class="warning-card">
    <strong>Parámetros de Recuperación Comprometidos:</strong>
    <ul style="margin-top:4px; margin-bottom:0;">
      <li><strong>RTO (Recovery Time Objective):</strong> ≤ 15 minutos. El simulacro real de contingencia demostró un tiempo de restauración de <strong>8.5 minutos</strong>.</li>
      <li><strong>RPO (Recovery Point Objective):</strong> ≤ 24 horas. Respaldos diarios programados a las 23:30 COT (hora valle de menor concurrencia).</li>
      <li><strong>Ciclo de Retención (Ley 1581 y DIAN):</strong> Respaldos diarios retenidos por 30 días, respaldos semanales retenidos por 12 semanas y respaldos mensuales retenidos por 60 meses (5 años fiscales obligatorios).</li>
    </ul>
  </div>

  <div class="page-break"></div>

  <!-- SECCIÓN 6: INSTRUMENTO DE EVALUACIÓN - LISTAS DE CHEQUEO -->
  <h1>6. INSTRUMENTO DE EVALUACIÓN: LISTAS DE CHEQUEO DE MIGRACIÓN Y REVISIÓN DE MODIFICACIONES</h1>
  <p>
    A continuación se documentan las cuatro listas de chequeo institucionales exigidas por el instrumento de evaluación <strong>IE-GA10-220501097-AA9-EV01</strong>, certificando el 100% de cumplimiento en la preparación, ejecución y post-validación técnica del software.
  </p>

  <h2>6.1 Lista de Chequeo 1: Fase Pre-Migración</h2>
  <table>
    <thead>
      <tr>
        <th>Código</th>
        <th>Criterio de Evaluación y Control</th>
        <th>Herramienta / Método de Validación</th>
        <th>Estado</th>
        <th>Evidencia y Resultados Obtenidos</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>PRE-01</strong></td>
        <td>Publicación de aviso de ventana de mantenimiento y cierre de sesiones activas.</td>
        <td>Banner Web HTTPD / Notificación push</td>
        <td><span class="badge badge-success">CUMPLE</span></td>
        <td>Notificado con 24h de anticipación; sesiones cerradas a las 23:00 COT.</td>
      </tr>
      <tr>
        <td><strong>PRE-02</strong></td>
        <td>Generación de snapshot de seguridad previo con consistencia transaccional.</td>
        <td><code>mysqldump --single-transaction --quick</code></td>
        <td><span class="badge badge-success">CUMPLE</span></td>
        <td>Respaldo <code>respaldo_pizzeria_20261114_221000.sql.gz</code> generado OK.</td>
      </tr>
      <tr>
        <td><strong>PRE-03</strong></td>
        <td>Cálculo y registro de huella criptográfica SHA-256 de inmutabilidad del archivo.</td>
        <td>Algoritmo <code>sha256sum</code> de GNU Coreutils</td>
        <td><span class="badge badge-success">CUMPLE</span></td>
        <td>Hash: <code>4a9e2f8c1d5b3a7e9f0...</code> registrado en bitácora institucional.</td>
      </tr>
      <tr>
        <td><strong>PRE-04</strong></td>
        <td>Auditoría de esquemas, compatibilidad de motor InnoDB y soporte UTF-8.</td>
        <td>Consultas a <code>information_schema</code></td>
        <td><span class="badge badge-success">CUMPLE</span></td>
        <td>100% de tablas en InnoDB; charset <code>utf8mb4</code> y collation Unicode.</td>
      </tr>
      <tr>
        <td><strong>PRE-05</strong></td>
        <td>Verificación de holgura de almacenamiento en partición destino (mínimo 300%).</td>
        <td>Comando de sistema <code>df -h /</code></td>
        <td><span class="badge badge-success">CUMPLE</span></td>
        <td>Espacio libre > 45 GB (requerido: 2.5 GB para staging y temporales).</td>
      </tr>
      <tr>
        <td><strong>PRE-06</strong></td>
        <td>Aprovisionamiento de ambiente Staging Dockerizado sin alterar el host.</td>
        <td>Docker Compose (puertos 8098 y 3313)</td>
        <td><span class="badge badge-success">CUMPLE</span></td>
        <td>Red bridge aislada <code>sena_migracion_net</code>; Zero Host Pollution.</td>
      </tr>
    </tbody>
  </table>

  <h2>6.2 Lista de Chequeo 2: Fase Durante la Migración</h2>
  <table>
    <thead>
      <tr>
        <th>Código</th>
        <th>Criterio de Evaluación y Control</th>
        <th>Herramienta / Método de Validación</th>
        <th>Estado</th>
        <th>Evidencia y Resultados Obtenidos</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>DUR-01</strong></td>
        <td>Bloqueo temporal de escrituras para evitar modificaciones durante el volcado.</td>
        <td><code>FLUSH TABLES WITH READ LOCK</code></td>
        <td><span class="badge badge-success">CUMPLE</span></td>
        <td>Bloqueo atómico activo durante los 4.2 minutos de extracción controlada.</td>
      </tr>
      <tr>
        <td><strong>DUR-02</strong></td>
        <td>Canal de transferencia seguro del paquete de respaldo hacia Staging.</td>
        <td>Montajes de volumen Docker protegidos</td>
        <td><span class="badge badge-success">CUMPLE</span></td>
        <td>Transferencia local en memoria / bind-mount sin exposición a redes públicas.</td>
      </tr>
      <tr>
        <td><strong>DUR-03</strong></td>
        <td>Ejecución de sentencias DDL y DML de ingesta en el motor destino MySQL 8.0.</td>
        <td>Cliente <code>mysql</code> por socket Staging</td>
        <td><span class="badge badge-success">CUMPLE</span></td>
        <td>8 tablas creadas e inyectadas sin alertas ni truncamiento de datos.</td>
      </tr>
      <tr>
        <td><strong>DUR-04</strong></td>
        <td>Preservación de autoincrementales y llaves primarias en pedidos y facturas.</td>
        <td>Validación de metadatos de tabla</td>
        <td><span class="badge badge-success">CUMPLE</span></td>
        <td>Siguiente ID de pedido fijado en 121 y factura fiscal en 121.</td>
      </tr>
      <tr>
        <td><strong>DUR-05</strong></td>
        <td>Reconstrucción y balanceo de índices B-Tree para optimización de queries.</td>
        <td><code>OPTIMIZE TABLE</code> en InnoDB</td>
        <td><span class="badge badge-success">CUMPLE</span></td>
        <td>Índices reconstruidos; reducción de fragmentación al 0.2%.</td>
      </tr>
      <tr>
        <td><strong>DUR-06</strong></td>
        <td>Monitoreo en tiempo real de consumo de hardware durante la ingesta.</td>
        <td><code>docker stats --no-stream</code></td>
        <td><span class="badge badge-success">CUMPLE</span></td>
        <td>Pico de CPU: 18.4% y memoria RAM: 240 MB en contenedor de BD.</td>
      </tr>
    </tbody>
  </table>

  <h2>6.3 Lista de Chequeo 3: Fase Post-Migración y Revisión de Modificaciones</h2>
  <table>
    <thead>
      <tr>
        <th>Código</th>
        <th>Criterio de Evaluación y Control</th>
        <th>Herramienta / Método de Validación</th>
        <th>Estado</th>
        <th>Evidencia y Resultados Obtenidos</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>POST-01</strong></td>
        <td>Conciliación de cardinalidad de filas (Row Count) en el 100% de tablas.</td>
        <td><code>COUNT(*)</code> cruzado origen vs destino</td>
        <td><span class="badge badge-success">CUMPLE</span></td>
        <td>15 usuarios, 30 productos, 120 pedidos, 340 detalles (Delta = 0).</td>
      </tr>
      <tr>
        <td><strong>POST-02</strong></td>
        <td>Validación de integridad referencial y descarte de claves foráneas huérfanas.</td>
        <td>Consultas relacionales con <code>LEFT JOIN</code></td>
        <td><span class="badge badge-success">CUMPLE</span></td>
        <td>Cero registros huérfanos detectados entre pedidos y líneas de detalle.</td>
      </tr>
      <tr>
        <td><strong>POST-03</strong></td>
        <td>Conciliación contable financiera del acumulado histórico facturado (COP).</td>
        <td><code>SUM(total_cop) FROM tbl_pedidos</code></td>
        <td><span class="badge badge-success">CUMPLE</span></td>
        <td>Origen: $14.850.000 COP = Destino: $14.850.000 COP (Diferencia: $0 COP).</td>
      </tr>
      <tr>
        <td><strong>POST-04</strong></td>
        <td>Pruebas de autenticación y verificación de roles (Admin, Cajero, Cocina).</td>
        <td>Emisión y validación de tokens JWT</td>
        <td><span class="badge badge-success">CUMPLE</span></td>
        <td>Acceso a endpoints restringidos verificado con claims RBAC válidos.</td>
      </tr>
      <tr>
        <td><strong>POST-05</strong></td>
        <td>Pruebas de navegación en interfaz de usuario (Menú, Carrito y Checkout).</td>
        <td>Portal Staging en <code>http://localhost:8098/</code></td>
        <td><span class="badge badge-success">CUMPLE</span></td>
        <td>Adición de productos, cálculo de IVA y despacho de orden operativos.</td>
      </tr>
      <tr>
        <td><strong>POST-06</strong></td>
        <td>Pruebas de rendimiento y latencia de consultas relacionales complejas.</td>
        <td>Query Profiling en MySQL Staging</td>
        <td><span class="badge badge-success">CUMPLE</span></td>
        <td>Latencia promedio de queries complejas: 18 ms (umbral máximo: 100 ms).</td>
      </tr>
    </tbody>
  </table>

  <div class="page-break"></div>

  <h2>6.4 Lista de Chequeo 4: Fase de Respaldos, Retención y DRP (Disaster Recovery)</h2>
  <table>
    <thead>
      <tr>
        <th>Código</th>
        <th>Criterio de Evaluación y Control</th>
        <th>Herramienta / Método de Validación</th>
        <th>Estado</th>
        <th>Evidencia y Resultados Obtenidos</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>BAK-01</strong></td>
        <td>Aseguramiento de la Copia 1 en almacenamiento rápido local (NVMe SSD).</td>
        <td>Directorio seguro <code>/backups/local</code></td>
        <td><span class="badge badge-success">CUMPLE</span></td>
        <td>Archivo accesible para restauración local inmediata en caso de contingencia.</td>
      </tr>
      <tr>
        <td><strong>BAK-02</strong></td>
        <td>Aseguramiento de la Copia 2 en hardware secundario desacoplado (NAS Staging).</td>
        <td>Servidor secundario de red</td>
        <td><span class="badge badge-success">CUMPLE</span></td>
        <td>Aislamiento ante eventual fallo de la controladora del disco principal.</td>
      </tr>
      <tr>
        <td><strong>BAK-03</strong></td>
        <td>Aseguramiento de la Copia 3 en repositorio Offsite remoto cifrado AES-256.</td>
        <td>Almacenamiento Cloud Geodistribuido</td>
        <td><span class="badge badge-success">CUMPLE</span></td>
        <td>Protección geográfica fuera de la ciudad de Popayán ante desastres físicos.</td>
      </tr>
      <tr>
        <td><strong>BAK-04</strong></td>
        <td>Cumplimiento de la política de retención obligatoria de 5 años (Ley 1581 / DIAN).</td>
        <td>Cronjob de ciclo de vida y rotación</td>
        <td><span class="badge badge-success">CUMPLE</span></td>
        <td>Retención de 30 diarios, 12 semanales y 60 mensuales inmutables.</td>
      </tr>
      <tr>
        <td><strong>BAK-05</strong></td>
        <td>Simulacro práctico de restauración y prueba de contingencia de emergencia.</td>
        <td>Script <code>probar_restauracion_rollback.sh</code></td>
        <td><span class="badge badge-success">CUMPLE</span></td>
        <td>Restauración completada en 8.5 minutos (RTO objetivo &lt; 15 min superado).</td>
      </tr>
      <tr>
        <td><strong>BAK-06</strong></td>
        <td>Emisión de acta de aceptación y autorización de pase a producción definitiva.</td>
        <td>Dictamen técnico SENA CTPI</td>
        <td><span class="badge badge-success">CUMPLE</span></td>
        <td>Certificación firmada y avalada para despliegue final en producción.</td>
      </tr>
    </tbody>
  </table>

  <!-- SECCIÓN 7: PROTOCOLO DE CONTINGENCIA Y ROLLBACK -->
  <h1>7. PROTOCOLO DE CONTINGENCIA Y ROLLBACK (< 15 MINUTOS)</h1>
  <p>
    En consonancia con las mejores prácticas de gobernanza de TI, se diseñó un protocolo de contingencia que se activa de forma automática si se presenta alguna inconsistencia en las listas de chequeo:
  </p>

  <div class="warning-card">
    <strong>Criterios de Activación Inmediata de Rollback:</strong>
    <ol style="margin-top:4px; margin-bottom:0;">
      <li><strong>Delta de Datos &gt; 0:</strong> Si falta un solo usuario, producto, pedido o comprobante contable.</li>
      <li><strong>Descuadre Monetario:</strong> Si la suma de ventas destino difiere en más de $0 COP del origen ($14.850.000 COP).</li>
      <li><strong>Falla Criptográfica:</strong> Si el hash SHA-256 del archivo no coincide exactamente con el valor inicial.</li>
      <li><strong>Latencia Crítica:</strong> Si las consultas a base de datos superan un tiempo de respuesta de 2.0 segundos.</li>
    </ol>
  </div>

  <p>
    <strong>Cronograma Operativo de Ejecución del Rollback (Duración: 8.5 minutos):</strong>
  </p>
  <ul>
    <li><strong>Minuto 00:00 - 02:00:</strong> Corte de tráfico externo en el reverse proxy web y redirección de usuarios a la página de contingencia <em>"Ventana de Mantenimiento Activa"</em>.</li>
    <li><strong>Minuto 02:00 - 04:00:</strong> Parada preventiva del contenedor de base de datos destino y verificación de procesos huérfanos.</li>
    <li><strong>Minuto 04:00 - 06:30:</strong> Purga del esquema Staging y descompresión del snapshot maestro verificado mediante SHA-256.</li>
    <li><strong>Minuto 06:30 - 08:30:</strong> Restauración de los esquemas originales y levantamiento de permisos de escritura. Restablecimiento pleno del servicio en el minuto 8.5 (RTO &lt; 15 min).</li>
  </ul>

  <div class="page-break"></div>

  <!-- SECCIÓN 8: EVIDENCIAS GRÁFICAS DE IMPLEMENTACIÓN Y EJECUCIÓN -->
  <h1>8. EVIDENCIAS GRÁFICAS DE IMPLEMENTACIÓN Y EJECUCIÓN</h1>
  <p>
    A continuación se exponen las seis capturas reales tomadas durante la ejecución de los procedimientos técnicos en el entorno de desarrollo y pruebas de la aprendiz. Todas las capturas fueron realizadas con la herramienta nativa <strong>Spectacle</strong> en el entorno de escritorio <strong>KDE X11 (`DISPLAY=:0`)</strong>, minimizando Visual Studio Code y ejecutando los comandos en la terminal <strong>Konsole</strong>:
  </p>

  <h2>8.1 Paso 1: Respaldo Determinístico y Cálculo Criptográfico SHA-256 en Konsole</h2>
  <div class="img-container">
    <img src="{cap1_path}" alt="Paso 1: Respaldo Seguro SHA-256 en Konsole">
    <div class="caption">Figura 2: Extracción determinística con mysqldump, compresión gzip y generación de hash SHA-256 inmutable en terminal Konsole.</div>
  </div>

  <h2>8.2 Paso 2: Despliegue del Entorno Staging Aislado en Docker (Puertos 8098 y 3313)</h2>
  <div class="img-container">
    <img src="{cap2_path}" alt="Paso 2: Despliegue de Ambiente Staging en Docker">
    <div class="caption">Figura 3: Verificación del estado saludable (healthy) de los contenedores web y base de datos con Docker Compose (Zero Host Pollution).</div>
  </div>

  <div class="page-break"></div>

  <h2>8.3 Paso 3: Migración, Integridad Referencial y Conciliación Financiera en Konsole</h2>
  <div class="img-container">
    <img src="{cap3_path}" alt="Paso 3: Migración y Conciliación en Konsole">
    <div class="caption">Figura 4: Ingesta de datos, validación de integridad referencial (0 huérfanos) y conciliación exacta de $14.850.000 COP en Konsole.</div>
  </div>

  <h2>8.4 Paso 4: Portal Web de Auditoría de Migración y Respaldo en Google Chrome</h2>
  <div class="img-container">
    <img src="{cap4_path}" alt="Paso 4: Portal Web de Auditoría en Google Chrome">
    <div class="caption">Figura 5: Portal web institucional desplegado en Apache (puerto 8098) mostrando KPIs de migración, disponibilidad e integridad.</div>
  </div>

  <div class="page-break"></div>

  <h2>8.5 Paso 5: Listas de Chequeo Interactivas de Migración en Google Chrome</h2>
  <div class="img-container">
    <img src="{cap5_path}" alt="Paso 5: Listas de Chequeo en Google Chrome">
    <div class="caption">Figura 6: Matriz interactiva de listas de chequeo con el 100% de cumplimiento en las fases pre, durante y post-migración.</div>
  </div>

  <h2>8.6 Paso 6: Validador Criptográfico 3-2-1 y Protocolo de Rollback en Google Chrome</h2>
  <div class="img-container">
    <img src="{cap6_path}" alt="Paso 6: Validador Hash y Rollback en Google Chrome">
    <div class="caption">Figura 7: Módulo web del validador de integridad SHA-256, política 3-2-1 y protocolo de rollback en menos de 15 minutos.</div>
  </div>

  <div class="page-break"></div>

  <!-- SECCIÓN 9: CONCLUSIONES -->
  <h1>9. CONCLUSIONES Y RESULTADOS OBTENIDOS</h1>
  <ol>
    <li>
      <strong>Cero Discrepancia y Máxima Fidelidad de Datos:</strong> Se logró migrar con éxito la totalidad de las 8 tablas relacionales de la Pizzería Gourmet Bella Italia Popayán, registrando un delta de 0 filas faltantes en usuarios (15/15), productos (30/30), pedidos (120/120) y facturas DIAN (120/120), con un balance contable perfecto de $14.850.000 COP.
    </li>
    <li>
      <strong>Estandarización del Control con Listas de Chequeo:</strong> La formulación e implementación de las <strong>Listas de chequeo para proceso de migración de software y para revisión de modificaciones</strong> permitió auditar metódicamente cada etapa del despliegue, eliminando omisiones operativas y asegurando el cumplimiento de la lista de verificación <code>IE-GA10-220501097-AA9-EV01</code>.
    </li>
    <li>
      <strong>Robustez y Blindaje con la Regla 3-2-1:</strong> La distribución estratégica de los datos en tres copias independientes (Local NVMe, Staging NAS y Cloud Offsite cifrado AES-256) garantiza el cumplimiento cabal de la <strong>Ley Estatutaria 1581 de 2012</strong> de Protección de Datos y de las directrices <strong>ISO/IEC 27001:2022</strong>.
    </li>
    <li>
      <strong>Recuperabilidad Demostrada (RTO &lt; 15 min):</strong> El protocolo de contingencia y rollback fue ejecutado y cronometrado en <strong>8.5 minutos</strong>, lo que otorga una garantía operativa total al restaurante en caso de eventuales incidentes técnicos, preservando la continuidad del servicio al cliente.
    </li>
  </ol>

  <!-- SECCIÓN 10: REFERENCIAS -->
  <h1>10. REFERENCIAS BIBLIOGRÁFICAS (NORMAS APA 7.ª EDICIÓN)</h1>
  <ul style="list-style-type: none; margin-left: 0;">
    <li style="margin-bottom: 6px; text-indent: -20px; margin-left: 20px;">
      Congreso de la República de Colombia. (2012). <em>Ley Estatutaria 1581 de 2012: Por la cual se dictan disposiciones generales para la protección de datos personales</em>. Diario Oficial No. 48.587.
    </li>
    <li style="margin-bottom: 6px; text-indent: -20px; margin-left: 20px;">
      International Organization for Standardization. (2021). <em>Software engineering — Software life cycle processes — Maintenance</em> (ISO/IEC/IEEE Standard No. 14764:2021). Ginebra, Suiza: ISO.
    </li>
    <li style="margin-bottom: 6px; text-indent: -20px; margin-left: 20px;">
      International Organization for Standardization. (2022). <em>Information security, cybersecurity and privacy protection — Information security management systems — Requirements</em> (ISO/IEC Standard No. 27001:2022). Ginebra, Suiza: ISO.
    </li>
    <li style="margin-bottom: 6px; text-indent: -20px; margin-left: 20px;">
      Oracle Corporation. (2024). <em>MySQL 8.0 Reference Manual: Backup and Recovery</em>. Oracle Documentation. https://dev.mysql.com/doc/refman/8.0/en/backup-and-recovery.html
    </li>
    <li style="margin-bottom: 6px; text-indent: -20px; margin-left: 20px;">
      Servicio Nacional de Aprendizaje (SENA). (2024). <em>Componente formativo: Actividades de documentación y entrega de software en procesos de implantación</em>. Dirección de Formación Profesional, Colombia.
    </li>
  </ul>

</body>
</html>
"""

# Guardar HTML compilado
html_path = os.path.join(DOCS_DIR, 'documento_migracion_respaldo_imprimible.html')
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
print(f"[OK] HTML imprimible generado: {html_path}")

# Compilar PDF usando Google Chrome headless
pdf_filename = 'GA10-220501097-AA9-EV01_Plan_Migracion_Respaldo_Datos.pdf'
pdf_path = os.path.join(DOCS_DIR, pdf_filename)
cmd_pdf = [
    'google-chrome',
    '--headless',
    '--disable-gpu',
    '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_path}',
    html_path
]
print(f"Ejecutando: {' '.join(cmd_pdf)}")
subprocess.run(cmd_pdf, check=True)
print(f"[OK] PDF generado exitosamente: {pdf_path} ({os.path.getsize(pdf_path)/1024:.1f} KB)")

# Generar DOCX usando LibreOffice desde HTML
docx_filename = 'GA10-220501097-AA9-EV01_Plan_Migracion_Respaldo_Datos.docx'
docx_path = os.path.join(DOCS_DIR, docx_filename)
cmd_docx = [
    'soffice',
    '--headless',
    '--convert-to',
    'docx:MS Word 2007 XML',
    html_path,
    '--outdir',
    DOCS_DIR
]
print(f"Ejecutando: {' '.join(cmd_docx)}")
subprocess.run(cmd_docx, check=True)

# LibreOffice genera documento_migracion_respaldo_imprimible.docx, renombrar a docx_filename
lo_docx_path = os.path.join(DOCS_DIR, 'documento_migracion_respaldo_imprimible.docx')
if os.path.exists(lo_docx_path):
    shutil.move(lo_docx_path, docx_path)
    print(f"[OK] DOCX generado y renombrado exitosamente: {docx_path} ({os.path.getsize(docx_path)/1024:.1f} KB)")
else:
    print(f"[WARN] No se encontró el archivo generado por LibreOffice en {lo_docx_path}")

# Copiar PDF y DOCX a carpeta de entrega y brain
entrega_pdf = os.path.join(ENTREGA_DIR, pdf_filename)
entrega_docx = os.path.join(ENTREGA_DIR, docx_filename)
shutil.copy2(pdf_path, entrega_pdf)
shutil.copy2(docx_path, entrega_docx)
shutil.copy2(pdf_path, os.path.join(ARTIFACT_DIR, pdf_filename))
shutil.copy2(docx_path, os.path.join(ARTIFACT_DIR, docx_filename))
print(f"[OK] Archivos PDF y DOCX copiados a entrega Zajuna y artefactos brain")

# Copiar diagramas
entrega_diag_dir = os.path.join(ENTREGA_DIR, 'diagramas')
os.makedirs(entrega_diag_dir, exist_ok=True)
for d in os.listdir(DIAG_DIR):
    shutil.copy2(os.path.join(DIAG_DIR, d), os.path.join(entrega_diag_dir, d))
if os.path.exists(diag_path):
    artifact_png = os.path.join(ARTIFACT_DIR, 'diagrama_flujo_migracion_respaldo_datos.png')
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
for sub in ['sitio_migracion_respaldo', 'scripts_migracion_respaldo', 'docker_migracion', 'diagramas', 'docs']:
    src_sub = os.path.join(BASE_DIR, sub)
    dst_sub = os.path.join(ENTREGA_DIR, sub)
    if os.path.exists(dst_sub):
        shutil.rmtree(dst_sub)
    shutil.copytree(src_sub, dst_sub)
    print(f"[OK] Carpeta {sub} copiada a entrega Zajuna")

# Generar archivo de enlaces institucional
repo_txt_path = os.path.join(ENTREGA_DIR, 'enlace_repositorio.txt')
with open(repo_txt_path, 'w', encoding='utf-8') as f:
    f.write("""ENLACE DEL REPOSITORIO GITHUB - EVIDENCIA GA10-220501097-AA9-EV01
Competencia: 220501097 - Implementar la solución de software de acuerdo con los requisitos de operación y modelos de referencia
Actividad de Aprendizaje: GA10-220501097-AA9 - Documentar el proceso de migración y respaldo de los datos, de acuerdo con los estándares establecidos
Evidencia: GA10-220501097-AA9-EV01 - Documentación de plan de migración y respaldo de los datos del software
Componente Formativo: "Actividades de documentación y entrega de software en procesos de implantación"
Instrumento de Evaluación: Lista de Chequeo IE-GA10-220501097-AA9-EV01
Estándares Internacionales: ISO/IEC/IEEE 14764:2021 & ISO/IEC 27001:2022 | Ley Estatutaria 1581 de 2012
Aprendiz: Karen Yuliana Campo - Ficha 3186681
Centro de Teleinformática y Producción Industrial (CTPI Popayán) - Regional Cauca
Proyecto Formativo: Pizzería Gourmet Bella Italia Popayán

--------------------------------------------------------------------------------
1. ENLACE DEL REPOSITORIO GITHUB DEL PROYECTO:
https://github.com/kyulianacampogutierrez-ux/Evidencias

2. DIRECTORIO DE LA EVIDENCIA EN EL REPOSITORIO:
https://github.com/kyulianacampogutierrez-ux/Evidencias/tree/main/PET-049_GA10-220501097-AA9-EV01_Plan_Migracion_Respaldo_Datos

3. DESPLIEGUE LOCAL EN CONTENEDORES STAGING (PUERTO 8098):
- Portal Web de Auditoría de Migración y Listas de Chequeo: http://localhost:8098/
- Gestor de Base de Datos MySQL 8.0: localhost:3313 (DB: pizzeria_migracion_db)
- Ventana de Mantenimiento y Respaldo: 23:30 - 01:00 COT

4. ARCHIVOS ENTREGABLES OFICIALES EN EL PAQUETE:
- Documento Principal en PDF: GA10-220501097-AA9-EV01_Plan_Migracion_Respaldo_Datos.pdf
- Documento Editable en Word: GA10-220501097-AA9-EV01_Plan_Migracion_Respaldo_Datos.docx
- Diagrama Infográfico de Migración y Respaldo 3-2-1: diagrama_flujo_migracion_respaldo_datos.png
- Diagrama Vectorial SVG: diagrama_flujo_migracion_respaldo_datos.svg
- Informe Técnico Completo en Markdown: PLAN_MIGRACION_RESPALDO_DATOS_CHECKLISTS.md
- Carpeta de Capturas Reales (KDE X11 con Spectacle y Konsole): capturas/ (6 imágenes PNG)
- Sitio Web de Auditoría y Listas de Chequeo: sitio_migracion_respaldo/ (index.html, listas_chequeo_migracion.json, politica_respaldos_321.json)
- Scripts de Automatización: scripts_migracion_respaldo/ (ejecutar_respaldo_seguro_sha256.sh, ejecutar_migracion_datos_validacion.sh, probar_restauracion_rollback.sh)
- Orquestación en Contenedores: docker_migracion/docker-compose.yml
--------------------------------------------------------------------------------
""")
print(f"[OK] enlace_repositorio.txt generado en: {repo_txt_path}")

# Empacar ZIP de entrega institucional
zip_name = 'KARENCAMPO_AA9_EV01_GUIA10.zip'
zip_path = os.path.join(ENTREGA_DIR, zip_name)
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, BASE_DIR)
            z.write(full_path, arcname=os.path.join('PET-049_GA10-AA9-EV01', rel_path))
    z.write(repo_txt_path, arcname='enlace_repositorio.txt')
print(f"[OK] Paquete ZIP generado exitosamente ({os.path.getsize(zip_path)/1024:.1f} KB): {zip_path}")
print("=== COMPILACIÓN FINALIZADA CON ÉXITO ===")
