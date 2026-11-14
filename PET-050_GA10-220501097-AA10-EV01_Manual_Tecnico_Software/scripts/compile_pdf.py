#!/usr/bin/env python3
# ==============================================================================
# COMPILADOR DE MANUAL TÉCNICO Y EMPACADOR DE EVIDENCIA GA10-220501097-AA10-EV01
# Evidencia: Elabora documentos técnicos y de usuario del software
# Competencia: 220501097 - Implementar la solución de software (Modelos de referencia)
# Actividad: GA10-220501097-AA10 - Elaborar manuales de instalación, técnico y de usuario
# Componente: "Actividades de documentación y entrega de software en procesos de implantación"
# Instrumento: Lista de Chequeo IE-GA10-220501097-AA10-EV01
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán - Regional Cauca
# ==============================================================================

import os
import subprocess
import shutil
import zipfile

BASE_DIR = '/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-050_GA10-220501097-AA10-EV01_Manual_Tecnico_Software'
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
DIAG_DIR = os.path.join(BASE_DIR, 'diagramas')
CAPTURAS_DIR = os.path.join(BASE_DIR, 'capturas')
ENTREGA_DIR = '/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA10-220501097-AA10-EV01'
ARTIFACT_DIR = '/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603'

os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(DIAG_DIR, exist_ok=True)
os.makedirs(CAPTURAS_DIR, exist_ok=True)
os.makedirs(ENTREGA_DIR, exist_ok=True)

diag_casos_uso = os.path.join(DIAG_DIR, 'diagrama_casos_uso_sistema_pizzeria.png')
diag_er = os.path.join(DIAG_DIR, 'modelo_entidad_relacion_pizzeria.png')
diag_comp = os.path.join(DIAG_DIR, 'diagrama_componentes_sistema_pizzeria.png')

cap1_path = os.path.join(CAPTURAS_DIR, 'paso_01_verificacion_prerrequisitos_konsole.png')
cap2_path = os.path.join(CAPTURAS_DIR, 'paso_02_despliegue_contenedores_docker_konsole.png')
cap3_path = os.path.join(CAPTURAS_DIR, 'paso_03_ejecucion_healthcheck_componentes_konsole.png')
cap4_path = os.path.join(CAPTURAS_DIR, 'paso_04_chrome_manual_tecnico_prerrequisitos_frameworks.png')
cap5_path = os.path.join(CAPTURAS_DIR, 'paso_05_chrome_manual_tecnico_diagramas_casos_uso_er.png')
cap6_path = os.path.join(CAPTURAS_DIR, 'paso_06_chrome_manual_tecnico_diccionario_datos_componentes.png')

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Manual Técnico del Software - GA10-220501097-AA10-EV01 | Karen Campo</title>
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
    pre {{
      background: #0f172a;
      color: #38bdf8;
      padding: 6px 10px;
      border-radius: 4px;
      font-size: 7pt;
      margin: 6px 0;
      font-family: monospace;
    }}
    code {{
      font-family: monospace;
      color: #0369a1;
      font-weight: 600;
    }}
  </style>
</head>
<body>

  <!-- ENCABEZADO INSTITUCIONAL -->
  <div class="header-bar">
    <div class="header-title">MANUAL TÉCNICO Y DE OPERACIONES DEL SISTEMA DE SOFTWARE</div>
    <div class="header-sub">Guía de Aprendizaje 10 - Evidencia GA10-220501097-AA10-EV01 | Instrumento: Lista de Chequeo IE-GA10-220501097-AA10-EV01</div>
    <div class="header-sub">Sistema de Información Gastronómica y Comercio Electrónico "Pizzería Gourmet Bella Italia Popayán"</div>
  </div>

  <!-- METADATOS TÉCNICOS SENA -->
  <div class="meta-box">
    <div class="meta-item"><strong>Programa de Formación:</strong> Análisis y Desarrollo de Software (ADSO)</div>
    <div class="meta-item"><strong>Número de Ficha:</strong> 3186681 | Fase 4: Implantación (AP10)</div>
    <div class="meta-item"><strong>Competencia:</strong> 220501097 - Implementar solución de software según operación y modelos</div>
    <div class="meta-item"><strong>Actividad de Aprendizaje:</strong> GA10-220501097-AA10 - Elaborar manuales de instalación, técnico y de usuario</div>
    <div class="meta-item"><strong>Aprendiz:</strong> Karen Yuliana Campo | Regional Cauca</div>
    <div class="meta-item"><strong>Centro de Formación:</strong> Centro de Teleinformática y Producción Industrial (CTPI Popayán)</div>
  </div>

  <!-- INDICADORES TÉCNICOS -->
  <div class="kpi-grid">
    <div class="kpi-card">
      <div class="kpi-value">Microservicios</div>
      <div class="kpi-label">Arquitectura del Software</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-value">MySQL 8.0</div>
      <div class="kpi-label">Persistencia InnoDB</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-value">8 Tablas 3FN</div>
      <div class="kpi-label">Diccionario Normalizado</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-value">Docker Compose</div>
      <div class="kpi-label">Puertos 8099 y 3314</div>
    </div>
  </div>

  <!-- SECCIÓN 1: INTRODUCCIÓN -->
  <h1>1. INTRODUCCIÓN Y JUSTIFICACIÓN TÉCNICA</h1>
  <p>
    La documentación técnica formal constituye el cimiento operativo sobre el cual reposa la estabilidad, mantenibilidad y transferibilidad de los sistemas computacionales en entornos productivos. En estricto cumplimiento de los lineamientos establecidos en la <em>Guía para la elaboración de manual técnico y de operaciones de los sistemas de información</em> emitida por el <strong>Departamento Nacional de Planeación (DNP)</strong> de Colombia, y respaldado por los estándares internacionales <strong>ISO/IEC/IEEE 12207:2017</strong> (Procesos del ciclo de vida del software) e <strong>ISO/IEC 25010:2023</strong> (Calidad del producto de software), se presenta el <strong>Manual Técnico del Software</strong> para la plataforma web de la <strong>Pizzería Gourmet Bella Italia Popayán</strong>.
  </p>
  <p>
    Este manual contiene las especificaciones detalladas de prerrequisitos de hardware y software, frameworks y estándares de desarrollo, diagrama de casos de uso (UML), modelo entidad-relación (E-R), diccionario de datos completo de las ocho tablas relacionales, scripts de instalación automatizados y el diagrama de componentes del sistema, proporcionando una guía inequívoca para administradores de sistemas y equipos de desarrollo.
  </p>

  <!-- SECCIÓN 2: DESCRIPCIÓN DEL SISTEMA -->
  <h1>2. DESCRIPCIÓN DEL SISTEMA</h1>
  <p>
    <strong>Pizzería Gourmet Bella Italia Popayán</strong> es un sistema de información y comercio electrónico diseñado específicamente para el sector gastronómico, orientado a automatizar el ciclo de atención presencial en salón, pedidos web omnicanal, despacho geolocalizado en Popayán, gestión de comandas en cocina digital (KDS) y facturación electrónica autorizada ante la DIAN.
  </p>
  <div class="info-card">
    <strong>Resumen Arquitectónico del Sistema:</strong>
    <ul style="margin-top:4px; margin-bottom:0;">
      <li><strong>Frontend Web &amp; Móvil:</strong> Aplicación de Página Única (SPA) desarrollada en React 18 con Vite, Tailwind CSS y diseño responsivo para móviles y terminales POS.</li>
      <li><strong>Backend &amp; Microservicios:</strong> API RESTful modular construida en Go (Golang) y Node.js Express, con autenticación sin estado mediante tokens JWT (RFC 7519) y control de acceso RBAC.</li>
      <li><strong>Persistencia de Datos:</strong> Motor relacional MySQL Community Server 8.0 con motor transaccional InnoDB, soporte ACID y collation <code>utf8mb4_unicode_ci</code>.</li>
      <li><strong>Aislamiento de Despliegue:</strong> Orquestación multicontenedor con Docker Compose en puertos <strong>8099</strong> (Apache Web) y <strong>3314</strong> (MySQL 8.0), cumpliendo el principio de <em>Zero Host Pollution</em>.</li>
    </ul>
  </div>

  <!-- SECCIÓN 3: PRERREQUISITOS DE INSTALACIÓN -->
  <h1>3. PRERREQUISITOS DE INSTALACIÓN DEL SISTEMA</h1>
  <p>
    Para asegurar la adecuada puesta en marcha y desempeño del software, la infraestructura de servidores debe satisfacer los siguientes requerimientos técnicos:
  </p>
  <table>
    <thead>
      <tr>
        <th>Recurso Tecnológico</th>
        <th>Requerimiento Mínimo (Staging)</th>
        <th>Requerimiento Recomendado (Producción)</th>
        <th>Propósito Operativo</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Procesador (CPU)</strong></td>
        <td>2 Cores x86_64 @ 2.0 GHz</td>
        <td>4 Cores x86_64 / Intel Xeon o AMD Epyc</td>
        <td>Cálculo de rutas de despacho y procesamiento transaccional.</td>
      </tr>
      <tr>
        <td><strong>Memoria RAM</strong></td>
        <td>4 GB DDR4</td>
        <td>8 GB a 16 GB DDR4/DDR5 con ECC</td>
        <td>Gestión de caché de consultas y buffers de memoria InnoDB.</td>
      </tr>
      <tr>
        <td><strong>Almacenamiento</strong></td>
        <td>20 GB SSD SATA</td>
        <td>50 GB NVMe PCIe 4.0 (RAID 1)</td>
        <td>Persistencia de base de datos, logs y respaldos 3-2-1.</td>
      </tr>
      <tr>
        <td><strong>Sistema Operativo</strong></td>
        <td>Linux Ubuntu Server 22.04 LTS / Debian 12</td>
        <td>Ubuntu 24.04 LTS / Rocky Linux 9</td>
        <td>Entorno anfitrión estable y seguro para Docker.</td>
      </tr>
      <tr>
        <td><strong>Motor Contenedores</strong></td>
        <td>Docker Engine v24.0+</td>
        <td>Docker Engine v26.0+ &amp; Compose v2.26+</td>
        <td>Aislamiento inmutable sin alteración del sistema host.</td>
      </tr>
      <tr>
        <td><strong>Motor de Base de Datos</strong></td>
        <td>MySQL 8.0.35 Community Server</td>
        <td>MySQL 8.0 Enterprise / Percona 8.0</td>
        <td>Persistencia relacional con transacciones ACID.</td>
      </tr>
    </tbody>
  </table>

  <h2>Matriz de Puertos y Variables de Entorno (.env)</h2>
  <pre>PUERTO_WEB_HTTP=8099
PUERTO_MYSQL_DB=3314
MYSQL_DATABASE=pizzeria_manual_tecnico_db
MYSQL_USER=pizzeria_user
MYSQL_PASSWORD=Pizzeria2026*Pass!
JWT_SECRET_KEY=sena_ctpi_pizzeria_super_secret_jwt_key_2026!
CORS_ALLOWED_ORIGINS=http://localhost:8099,https://pizzeriabellaitalia.com</pre>

  <div class="page-break"></div>

  <!-- SECCIÓN 4: FRAMEWORKS Y ESTÁNDARES -->
  <h1>4. FRAMEWORKS Y ESTÁNDARES CON LOS QUE SE CONSTRUYÓ EL SISTEMA</h1>
  <p>
    En consonancia con la <em>Guía para la elaboración de manual técnico y de operaciones de los sistemas de información</em> del DNP, el software implementa tecnologías modernas y estándares formales de ingeniería:
  </p>
  <table>
    <thead>
      <tr>
        <th>Ámbito Tecnológico</th>
        <th>Framework / Estándar</th>
        <th>Versión</th>
        <th>Justificación Técnica y Funcional</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Frontend Web &amp; UI</strong></td>
        <td>React 18 / Vite / Tailwind CSS</td>
        <td>18.3 / 5.2 / 3.4</td>
        <td>Vistas dinámicas sin recargas, renderizado atómico y diseño adaptativo a tabletas de salón y smartphones.</td>
      </tr>
      <tr>
        <td><strong>Backend API REST</strong></td>
        <td>Go (Golang) / Node.js Express</td>
        <td>1.22 / 4.19</td>
        <td>Microservicios compilados de alto rendimiento concurrente, baja latencia (&lt; 20 ms) y enrutamiento perimetral.</td>
      </tr>
      <tr>
        <td><strong>Seguridad y Auth</strong></td>
        <td>JWT (RFC 7519) &amp; Bcrypt</td>
        <td>HMAC-SHA256 / Cost 12</td>
        <td>Tokens de sesión sin estado con claims de rol y hashing irreversible de contraseñas de usuarios.</td>
      </tr>
      <tr>
        <td><strong>Base de Datos</strong></td>
        <td>MySQL 8.0 (InnoDB)</td>
        <td>8.0.35</td>
        <td>Transaccionalidad ACID, comprobación de integridad referencial de llaves foráneas y soporte nativo JSON.</td>
      </tr>
      <tr>
        <td><strong>Contenedores / DevOps</strong></td>
        <td>Docker Compose &amp; Apache HTTPD</td>
        <td>v2.20+ / 2.4 Alpine</td>
        <td>Despliegue reproducible multicontenedor, proxy perimetral con compresión gzip y aislamiento de red bridge.</td>
      </tr>
      <tr>
        <td><strong>Estándar de Calidad</strong></td>
        <td>ISO/IEC 25010:2023 (SQuaRE)</td>
        <td>2023</td>
        <td>Garantía de adecuación funcional, fiabilidad, seguridad, usabilidad y mantenibilidad modular.</td>
      </tr>
      <tr>
        <td><strong>Norma de Ciclo de Vida</strong></td>
        <td>ISO/IEC/IEEE 12207:2017</td>
        <td>2017</td>
        <td>Procesos de ingeniería para implantación, verificación, entrega formal y transición a soporte.</td>
      </tr>
      <tr>
        <td><strong>Protección de Datos</strong></td>
        <td>Ley Estatutaria 1581 de 2012</td>
        <td>Colombia</td>
        <td>Seguridad de datos de comensales, trazabilidad forense en logs y retención histórica de 5 años.</td>
      </tr>
    </tbody>
  </table>

  <!-- SECCIÓN 5: DIAGRAMA DE CASOS DE USO -->
  <h1>5. DIAGRAMA DE CASOS DE USO DEL SISTEMA (UML)</h1>
  <p>
    El diagrama de casos de uso modela los requisitos funcionales del sistema bajo la notación UML 2.5, ilustrando la interacción de los cinco actores con los módulos de negocio:
  </p>

  <div class="img-container">
    <img src="{diag_casos_uso}" alt="Diagrama de Casos de Uso UML">
    <div class="caption">Figura 1: Diagrama de Casos de Uso UML del sistema Pizzería Gourmet Bella Italia Popayán.</div>
  </div>

  <h2>Especificación de Actores y Casos de Uso</h2>
  <ul>
    <li><strong>Cliente Comensal:</strong> Ejecuta <code>CU-01</code> (Explorar carta y precios) y <code>CU-02</code> (Registrar pedido y carrito de compras), con inclusión mandatoria de <code>CU-03</code> (Pago electrónico o en efectivo).</li>
    <li><strong>Administrador:</strong> Gestiona <code>CU-07</code> (Administrar menú, ingredientes y precios) y supervisa <code>CU-08</code> (Arqueo de caja y reportes consolidados).</li>
    <li><strong>Cajero / Facturador:</strong> Registra pedidos presenciales en salón, gestiona cobros y ejecuta <code>CU-05</code> (Emitir Factura Electrónica con CUFE y QR ante la DIAN).</li>
    <li><strong>Jefe de Cocina:</strong> Monitorea <code>CU-04</code> (Gestionar comandas digitales en cocina KDS) y actualiza estados de preparación.</li>
    <li><strong>Domiciliario:</strong> Atiende <code>CU-06</code> (Despacho geolocalizado en Popayán) y confirma entrega efectiva al cliente.</li>
  </ul>

  <div class="page-break"></div>

  <!-- SECCIÓN 6: MODELO ENTIDAD-RELACIÓN -->
  <h1>6. MODELO ENTIDAD-RELACIÓN DE LA BASE DE DATOS (E-R)</h1>
  <p>
    El modelo relacional fue normalizado en Tercera Forma Normal (3FN), garantizando la ausencia de redundancias y la atomicidad de las transacciones operativas:
  </p>

  <div class="img-container">
    <img src="{diag_er}" alt="Modelo Entidad-Relación E-R">
    <div class="caption">Figura 2: Esquema Entidad-Relación de la base de datos relacional MySQL 8.0 InnoDB.</div>
  </div>

  <!-- SECCIÓN 7: DICCIONARIO DE DATOS -->
  <h1>7. DICCIONARIO DE DATOS COMPLETO</h1>
  <p>
    A continuación se documenta el diccionario formal con la totalidad de campos, tipos de datos, longitudes, restricciones de nulidad y descripciones funcionales de las ocho tablas relacionales:
  </p>

  <h2>7.1 Tablas: tbl_roles_permisos y tbl_usuarios</h2>
  <table>
    <thead>
      <tr>
        <th>Tabla</th>
        <th>Campo</th>
        <th>Tipo Dato</th>
        <th>Long.</th>
        <th>Nulo</th>
        <th>Clave</th>
        <th>Descripción y Regla de Negocio</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td rowspan="4"><strong>tbl_roles_permisos</strong></td>
        <td><code>id_rol</code></td><td>INT</td><td>11</td><td>NO</td><td>PK</td><td>Identificador correlativo del rol (AUTO_INCREMENT).</td>
      </tr>
      <tr>
        <td><code>nombre_rol</code></td><td>VARCHAR</td><td>50</td><td>NO</td><td>UQ</td><td>Nombre de perfil: SuperAdmin, Cajero, Chef, Domicilio.</td>
      </tr>
      <tr>
        <td><code>descripcion</code></td><td>VARCHAR</td><td>255</td><td>NO</td><td>-</td><td>Resumen de privilegios operativos asignados.</td>
      </tr>
      <tr>
        <td><code>nivel_acceso</code></td><td>INT</td><td>11</td><td>NO</td><td>-</td><td>Jerarquía de 1 (cliente) a 10 (administrador).</td>
      </tr>
      <tr>
        <td rowspan="7"><strong>tbl_usuarios</strong></td>
        <td><code>id_usuario</code></td><td>INT</td><td>11</td><td>NO</td><td>PK</td><td>Identificador único del usuario (AUTO_INCREMENT).</td>
      </tr>
      <tr>
        <td><code>id_rol</code></td><td>INT</td><td>11</td><td>NO</td><td>FK</td><td>Rol asignado. REFERENCES <code>tbl_roles_permisos(id_rol)</code>.</td>
      </tr>
      <tr>
        <td><code>nombre_completo</code></td><td>VARCHAR</td><td>120</td><td>NO</td><td>-</td><td>Nombres y apellidos completos del titular.</td>
      </tr>
      <tr>
        <td><code>email</code></td><td>VARCHAR</td><td>100</td><td>NO</td><td>UQ</td><td>Correo electrónico corporativo / comensal (RFC 5322).</td>
      </tr>
      <tr>
        <td><code>telefono</code></td><td>VARCHAR</td><td>20</td><td>NO</td><td>-</td><td>Teléfono móvil para contacto de despacho.</td>
      </tr>
      <tr>
        <td><code>password_hash</code></td><td>VARCHAR</td><td>255</td><td>NO</td><td>-</td><td>Hash Bcrypt seguro de coste 12 (Ley 1581).</td>
      </tr>
      <tr>
        <td><code>estado</code></td><td>ENUM</td><td>-</td><td>NO</td><td>-</td><td>Valores válidos: 'ACTIVO', 'INACTIVO', 'BLOQUEADO'.</td>
      </tr>
    </tbody>
  </table>

  <h2>7.2 Tablas: tbl_categorias, tbl_productos_menu y tbl_pedidos</h2>
  <table>
    <thead>
      <tr>
        <th>Tabla</th>
        <th>Campo</th>
        <th>Tipo Dato</th>
        <th>Long.</th>
        <th>Nulo</th>
        <th>Clave</th>
        <th>Descripción y Regla de Negocio</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td rowspan="3"><strong>tbl_categorias</strong></td>
        <td><code>id_categoria</code></td><td>INT</td><td>11</td><td>NO</td><td>PK</td><td>Identificador único de categoría (AUTO_INCREMENT).</td>
      </tr>
      <tr>
        <td><code>nombre_categoria</code></td><td>VARCHAR</td><td>60</td><td>NO</td><td>UQ</td><td>Pizzas Tradicionales, Gourmet Popayán, Bebidas.</td>
      </tr>
      <tr>
        <td><code>activo</code></td><td>BOOLEAN</td><td>1</td><td>NO</td><td>-</td><td>Visibilidad en carta web (DEFAULT TRUE).</td>
      </tr>
      <tr>
        <td rowspan="5"><strong>tbl_productos_menu</strong></td>
        <td><code>id_producto</code></td><td>INT</td><td>11</td><td>NO</td><td>PK</td><td>Identificador primario del producto (AUTO_INCREMENT).</td>
      </tr>
      <tr>
        <td><code>id_categoria</code></td><td>INT</td><td>11</td><td>NO</td><td>FK</td><td>Categoría. REFERENCES <code>tbl_categorias(id_categoria)</code>.</td>
      </tr>
      <tr>
        <td><code>sku</code></td><td>VARCHAR</td><td>30</td><td>NO</td><td>UQ</td><td>Código único de inventario (ej. PIZ-MARG-01).</td>
      </tr>
      <tr>
        <td><code>nombre_producto</code></td><td>VARCHAR</td><td>100</td><td>NO</td><td>-</td><td>Nombre comercial del plato en la carta.</td>
      </tr>
      <tr>
        <td><code>precio_unitario</code></td><td>DECIMAL</td><td>12,2</td><td>NO</td><td>-</td><td>Precio en moneda colombiana COP (DECIMAL 12,2).</td>
      </tr>
      <tr>
        <td rowspan="6"><strong>tbl_pedidos</strong></td>
        <td><code>id_pedido</code></td><td>INT</td><td>11</td><td>NO</td><td>PK</td><td>Identificador de la orden de compra (AUTO_INCREMENT).</td>
      </tr>
      <tr>
        <td><code>codigo_orden</code></td><td>VARCHAR</td><td>30</td><td>NO</td><td>UQ</td><td>Código de seguimiento comensal (ORD-YYYYMM-XXX).</td>
      </tr>
      <tr>
        <td><code>id_cliente</code></td><td>INT</td><td>11</td><td>NO</td><td>FK</td><td>Cliente titular. REFERENCES <code>tbl_usuarios(id_usuario)</code>.</td>
      </tr>
      <tr>
        <td><code>estado_pedido</code></td><td>ENUM</td><td>-</td><td>NO</td><td>-</td><td>'RECIBIDO','EN_COCINA','EN_REPARTO','ENTREGADO'.</td>
      </tr>
      <tr>
        <td><code>total_cop</code></td><td>DECIMAL</td><td>12,2</td><td>NO</td><td>-</td><td>Monto final liquidado en pesos colombianos COP.</td>
      </tr>
      <tr>
        <td><code>direccion_entrega</code></td><td>VARCHAR</td><td>200</td><td>NO</td><td>-</td><td>Dirección física de domicilio en Popayán.</td>
      </tr>
    </tbody>
  </table>

  <div class="page-break"></div>

  <h2>7.3 Tablas: tbl_detalle_pedido, tbl_facturas_dian y tbl_auditoria_logs</h2>
  <table>
    <thead>
      <tr>
        <th>Tabla</th>
        <th>Campo</th>
        <th>Tipo Dato</th>
        <th>Long.</th>
        <th>Nulo</th>
        <th>Clave</th>
        <th>Descripción y Regla de Negocio</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td rowspan="4"><strong>tbl_detalle_pedido</strong></td>
        <td><code>id_detalle</code></td><td>INT</td><td>11</td><td>NO</td><td>PK</td><td>Identificador único de ítem de pedido.</td>
      </tr>
      <tr>
        <td><code>id_pedido</code></td><td>INT</td><td>11</td><td>NO</td><td>FK</td><td>Orden padre. REFERENCES <code>tbl_pedidos</code> (CASCADE).</td>
      </tr>
      <tr>
        <td><code>id_producto</code></td><td>INT</td><td>11</td><td>NO</td><td>FK</td><td>Plato pedido. REFERENCES <code>tbl_productos_menu</code>.</td>
      </tr>
      <tr>
        <td><code>subtotal_linea</code></td><td>DECIMAL</td><td>12,2</td><td>NO</td><td>-</td><td>Valor liquidado (cantidad * precio_unitario).</td>
      </tr>
      <tr>
        <td rowspan="4"><strong>tbl_facturas_dian</strong></td>
        <td><code>id_factura</code></td><td>INT</td><td>11</td><td>NO</td><td>PK</td><td>Identificador fiscal de factura electrónica.</td>
      </tr>
      <tr>
        <td><code>id_pedido</code></td><td>INT</td><td>11</td><td>NO</td><td>FK/UQ</td><td>Pedido liquidado (Relación 1 a 1 estricta).</td>
      </tr>
      <tr>
        <td><code>numero_factura</code></td><td>VARCHAR</td><td>40</td><td>NO</td><td>UQ</td><td>Numeración fiscal autorizada (FE-POPY-XXXX).</td>
      </tr>
      <tr>
        <td><code>cufe</code></td><td>VARCHAR</td><td>100</td><td>NO</td><td>UQ</td><td>Código Único de Factura Electrónica emitido por DIAN.</td>
      </tr>
      <tr>
        <td rowspan="4"><strong>tbl_auditoria_logs</strong></td>
        <td><code>id_log</code></td><td>BIGINT</td><td>20</td><td>NO</td><td>PK</td><td>Identificador correlativo de pista forense.</td>
      </tr>
      <tr>
        <td><code>accion</code></td><td>VARCHAR</td><td>50</td><td>NO</td><td>-</td><td>Operación ejecutada (LOGIN, INSERT, UPDATE, etc.).</td>
      </tr>
      <tr>
        <td><code>tabla_afectada</code></td><td>VARCHAR</td><td>50</td><td>NO</td><td>-</td><td>Tabla relacional intervenida en la base de datos.</td>
      </tr>
      <tr>
        <td><code>detalles_json</code></td><td>JSON</td><td>-</td><td>SÍ</td><td>-</td><td>Payload diferencial con estados antes y después.</td>
      </tr>
    </tbody>
  </table>

  <!-- SECCIÓN 8: DIAGRAMA DE COMPONENTES -->
  <h1>8. DIAGRAMA DE COMPONENTES DEL SISTEMA (UML)</h1>
  <p>
    El diagrama de componentes define la arquitectura multicapa desacoplada y los puertos de comunicación entre frontend, proxy, microservicios y bases de datos:
  </p>

  <div class="img-container">
    <img src="{diag_comp}" alt="Diagrama de Componentes UML">
    <div class="caption">Figura 3: Arquitectura de componentes desacoplados del sistema Pizzería Bella Italia.</div>
  </div>

  <h2>Descomposición por Capas de Arquitectura</h2>
  <ol>
    <li><strong>Capa de Presentación:</strong> Módulos SPA en React 18 / Tailwind para comensales, salón y pantalla de cocina (KDS).</li>
    <li><strong>Capa Perimetral &amp; Gateway:</strong> Servidor Apache HTTPD (puerto 8099) como reverse proxy y Node.js Express (puerto 8085) para rate limiting y CORS.</li>
    <li><strong>Capa de Microservicios:</strong> Auth Service en Go (:8083), Catalog Service en Go (:8084), Orders &amp; Checkout en Go (:8086), y DIAN Fiscal Service en Node.js (:8087).</li>
    <li><strong>Capa de Persistencia:</strong> Motor MySQL Community Server 8.0 (:3314) con motor InnoDB, volúmenes de almacenamiento Docker y respaldos 3-2-1.</li>
  </ol>

  <div class="page-break"></div>

  <!-- SECCIÓN 9: SCRIPTS DE INSTALACIÓN -->
  <h1>9. SCRIPTS Y PROCEDIMIENTOS DE INSTALACIÓN PASO A PASO</h1>
  <p>
    El aprovisionamiento de la plataforma se encuentra completamente automatizado mediante scripts de consola bajo los principios de portabilidad y <em>Zero Host Pollution</em>:
  </p>
  <pre># 1. Clonar el repositorio institucional
git clone https://github.com/kyulianacampogutierrez-ux/Evidencias.git
cd Evidencias/PET-050_GA10-220501097-AA10-EV01_Manual_Tecnico_Software

# 2. Ejecutar validación de prerrequisitos de hardware y dependencias
chmod +x scripts_instalacion_despliegue/*.sh
./scripts_instalacion_despliegue/instalar_prerrequisitos_sistema.sh

# 3. Desplegar contenedores con Docker Compose en puertos 8099 y 3314
cd docker_manual_tecnico
docker compose up -d

# 4. Ejecutar comprobación de salud y auditoría de esquemas
cd ..
./scripts_instalacion_despliegue/verificar_estado_componentes_healthcheck.sh</pre>

  <!-- SECCIÓN 10: EVIDENCIAS GRÁFICAS -->
  <h1>10. EVIDENCIAS GRÁFICAS DE IMPLEMENTACIÓN Y EJECUCIÓN</h1>
  <p>
    A continuación se exponen las seis capturas reales tomadas durante los procedimientos técnicos. Todas las capturas fueron realizadas con la herramienta oficial <strong>Spectacle</strong> sobre el servidor gráfico <strong>KDE X11 (`DISPLAY=:0`)</strong>, minimizando Visual Studio Code y ejecutando los comandos en la terminal nativa <strong>Konsole</strong>:
  </p>

  <h2>10.1 Paso 1: Verificación de Prerrequisitos de Instalación en Konsole</h2>
  <div class="img-container">
    <img src="{cap1_path}" alt="Paso 1: Prerrequisitos Konsole">
    <div class="caption">Figura 4: Verificación automatizada de CPU, RAM, almacenamiento y motores Docker en Konsole.</div>
  </div>

  <h2>10.2 Paso 2: Despliegue de Contenedores en Docker (Zero Host Pollution)</h2>
  <div class="img-container">
    <img src="{cap2_path}" alt="Paso 2: Despliegue Docker Konsole">
    <div class="caption">Figura 5: Contenedores web (puerto 8099) y MySQL 8.0 (puerto 3314) en estado saludable con Docker Compose.</div>
  </div>

  <div class="page-break"></div>

  <h2>10.3 Paso 3: Healthchecks de Componentes y Auditoría MySQL en Konsole</h2>
  <div class="img-container">
    <img src="{cap3_path}" alt="Paso 3: Healthchecks Konsole">
    <div class="caption">Figura 6: Comprobación HTTP 200 OK, lectura de diccionario JSON y auditoría de 8 tablas en MySQL 8.0.</div>
  </div>

  <h2>10.4 Paso 4: Portal Web del Manual Técnico - Prerrequisitos y Frameworks</h2>
  <div class="img-container">
    <img src="{cap4_path}" alt="Paso 4: Portal Prerrequisitos Chrome">
    <div class="caption">Figura 7: Portal interactivo del Manual Técnico en Google Chrome desplegado en http://localhost:8099/.</div>
  </div>

  <div class="page-break"></div>

  <h2>10.5 Paso 5: Diagramas de Casos de Uso UML y Modelo Entidad-Relación en Chrome</h2>
  <div class="img-container">
    <img src="{cap5_path}" alt="Paso 5: Diagramas Casos Uso y ER Chrome">
    <div class="caption">Figura 8: Visualización interactiva de los modelos UML y E-R en Google Chrome.</div>
  </div>

  <h2>10.6 Paso 6: Diccionario de Datos Interactivo y Diagrama de Componentes en Chrome</h2>
  <div class="img-container">
    <img src="{cap6_path}" alt="Paso 6: Diccionario y Componentes Chrome">
    <div class="caption">Figura 9: Módulo de búsqueda y filtrado de tablas del diccionario de datos y arquitectura de componentes.</div>
  </div>

  <div class="page-break"></div>

  <!-- SECCIÓN 11: CONCLUSIONES -->
  <h1>11. CONCLUSIONES Y RECOMENDACIONES</h1>
  <ol>
    <li>
      <strong>Estandarización Rigurosa según Guía DNP:</strong> La estructuración formal del manual técnico de acuerdo con las directrices del Departamento Nacional de Planeación asegura que la plataforma cuente con una documentación robusta, facilitando futuras auditorías técnicas y procesos de transferencia tecnológica.
    </li>
    <li>
      <strong>Consistencia del Modelo Relacional:</strong> La especificación en 3FN de las 8 tablas de la base de datos MySQL 8.0, junto al detalle exhaustivo del diccionario de datos, blinda la integridad referencial y evita la corrupción de pedidos, facturas DIAN y balances contables.
    </li>
    <li>
      <strong>Claridad y Modularidad Arquitectónica:</strong> La inclusión articulada de los diagramas de Casos de Uso, Modelo E-R y Diagrama de Componentes UML permite a los equipos de desarrollo desacoplar dependencias y escalar los microservicios sin fricción.
    </li>
    <li>
      <strong>Reproducibilidad Total del Despliegue:</strong> Gracias a los scripts de verificación y la contenedorización con Docker Compose, cualquier ingeniero puede levantar el ecosistema completo en menos de 3 minutos sin alterar el sistema operativo del anfitrión.
    </li>
  </ol>

  <!-- SECCIÓN 12: REFERENCIAS -->
  <h1>12. REFERENCIAS BIBLIOGRÁFICAS (NORMAS APA 7.ª EDICIÓN)</h1>
  <ul style="list-style-type: none; margin-left: 0;">
    <li style="margin-bottom: 6px; text-indent: -20px; margin-left: 20px;">
      Congreso de la República de Colombia. (2012). <em>Ley Estatutaria 1581 de 2012: Por la cual se dictan disposiciones generales para la protección de datos personales</em>. Diario Oficial No. 48.587.
    </li>
    <li style="margin-bottom: 6px; text-indent: -20px; margin-left: 20px;">
      Departamento Nacional de Planeación (DNP). (2020). <em>Guía para la elaboración de manual técnico y de operaciones de los sistemas de información</em>. Dirección de Tecnologías de Información y las Comunicaciones, Bogotá D.C., Colombia.
    </li>
    <li style="margin-bottom: 6px; text-indent: -20px; margin-left: 20px;">
      International Organization for Standardization. (2017). <em>Systems and software engineering — Software life cycle processes</em> (ISO/IEC/IEEE Standard No. 12207:2017). Ginebra, Suiza: ISO.
    </li>
    <li style="margin-bottom: 6px; text-indent: -20px; margin-left: 20px;">
      International Organization for Standardization. (2023). <em>Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model</em> (ISO/IEC Standard No. 25010:2023). Ginebra, Suiza: ISO.
    </li>
    <li style="margin-bottom: 6px; text-indent: -20px; margin-left: 20px;">
      Object Management Group (OMG). (2017). <em>Unified Modeling Language (OMG UML) Specification Version 2.5.1</em>. OMG Standard. https://www.omg.org/spec/UML/
    </li>
    <li style="margin-bottom: 6px; text-indent: -20px; margin-left: 20px;">
      Oracle Corporation. (2024). <em>MySQL 8.0 Reference Manual: InnoDB Storage Engine Architecture</em>. Oracle Documentation. https://dev.mysql.com/doc/refman/8.0/en/innodb-storage-engine.html
    </li>
    <li style="margin-bottom: 6px; text-indent: -20px; margin-left: 20px;">
      Servicio Nacional de Aprendizaje (SENA). (2024). <em>Componente formativo: Actividades de documentación y entrega de software en procesos de implantación</em>. Dirección de Formación Profesional, Colombia.
    </li>
  </ul>

</body>
</html>
"""

# Guardar HTML imprimible
html_path = os.path.join(DOCS_DIR, 'documento_manual_tecnico_imprimible.html')
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
print(f"[OK] HTML imprimible generado: {html_path}")

# Compilar PDF usando Google Chrome headless
pdf_filename = 'GA10-220501097-AA10-EV01_Manual_Tecnico_Software.pdf'
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
docx_filename = 'GA10-220501097-AA10-EV01_Manual_Tecnico_Software.docx'
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

lo_docx_path = os.path.join(DOCS_DIR, 'documento_manual_tecnico_imprimible.docx')
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

# Copiar diagramas a entrega y artefactos
entrega_diag_dir = os.path.join(ENTREGA_DIR, 'diagramas')
os.makedirs(entrega_diag_dir, exist_ok=True)
for d in os.listdir(DIAG_DIR):
    shutil.copy2(os.path.join(DIAG_DIR, d), os.path.join(entrega_diag_dir, d))
    if d.endswith('.png'):
        shutil.copy2(os.path.join(DIAG_DIR, d), os.path.join(ARTIFACT_DIR, d))
print(f"[OK] Diagramas copiados a entrega Zajuna y artefactos")

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
for sub in ['sitio_manual_tecnico', 'scripts_instalacion_despliegue', 'docker_manual_tecnico', 'diagramas', 'docs']:
    src_sub = os.path.join(BASE_DIR, sub)
    dst_sub = os.path.join(ENTREGA_DIR, sub)
    if os.path.exists(dst_sub):
        shutil.rmtree(dst_sub)
    shutil.copytree(src_sub, dst_sub)
    print(f"[OK] Carpeta {sub} copiada a entrega Zajuna")

# Generar archivo de enlaces institucional
repo_txt_path = os.path.join(ENTREGA_DIR, 'enlace_repositorio.txt')
with open(repo_txt_path, 'w', encoding='utf-8') as f:
    f.write("""ENLACE DEL REPOSITORIO GITHUB - EVIDENCIA GA10-220501097-AA10-EV01
Competencia: 220501097 - Implementar la solución de software de acuerdo con los requisitos de operación y modelos de referencia
Actividad de Aprendizaje: GA10-220501097-AA10 - Elaborar manuales de instalación, técnico y de usuario, de acuerdo con los estándares establecidos
Evidencia: GA10-220501097-AA10-EV01 - Elabora documentos técnicos y de usuario del software
Componente Formativo: "Actividades de documentación y entrega de software en procesos de implantación"
Instrumento de Evaluación: Lista de Chequeo IE-GA10-220501097-AA10-EV01
Estándares y Guías: Guía DNP (Departamento Nacional de Planeación), ISO/IEC/IEEE 12207:2017 & ISO/IEC 25010:2023 | Ley 1581 de 2012
Aprendiz: Karen Yuliana Campo - Ficha 3186681
Centro de Teleinformática y Producción Industrial (CTPI Popayán) - Regional Cauca
Proyecto Formativo: Pizzería Gourmet Bella Italia Popayán

--------------------------------------------------------------------------------
1. ENLACE DEL REPOSITORIO GITHUB DEL PROYECTO:
https://github.com/kyulianacampogutierrez-ux/Evidencias

2. DIRECTORIO DE LA EVIDENCIA EN EL REPOSITORIO:
https://github.com/kyulianacampogutierrez-ux/Evidencias/tree/main/PET-050_GA10-220501097-AA10-EV01_Manual_Tecnico_Software

3. DESPLIEGUE LOCAL EN CONTENEDORES STAGING (PUERTO 8099):
- Portal Web del Manual Técnico Interactivo: http://localhost:8099/
- Gestor de Base de Datos MySQL 8.0: localhost:3314 (DB: pizzeria_manual_tecnico_db)
- Red Aislada de Contenedores: sena_manual_tecnico_net (Zero Host Pollution)

4. ARCHIVOS ENTREGABLES OFICIALES EN EL PAQUETE:
- Documento Principal en PDF: GA10-220501097-AA10-EV01_Manual_Tecnico_Software.pdf
- Documento Editable en Word: GA10-220501097-AA10-EV01_Manual_Tecnico_Software.docx
- Diagrama de Casos de Uso (UML): diagrama_casos_uso_sistema_pizzeria.png / .svg
- Modelo Entidad-Relación (E-R): modelo_entidad_relacion_pizzeria.png / .svg
- Diagrama de Componentes (UML): diagrama_componentes_sistema_pizzeria.png / .svg
- Informe Técnico Completo en Markdown: MANUAL_TECNICO_SISTEMA_PIZZERIA.md
- Carpeta de Capturas Reales (KDE X11 con Spectacle y Konsole): capturas/ (6 imágenes PNG)
- Sitio Web del Manual Técnico: sitio_manual_tecnico/ (index.html, diccionario_datos.json, arquitectura_componentes.json)
- Scripts de Automatización: scripts_instalacion_despliegue/ (instalar_prerrequisitos_sistema.sh, desplegar_ecosistema_produccion.sh, verificar_estado_componentes_healthcheck.sh)
- Orquestación en Contenedores: docker_manual_tecnico/docker-compose.yml
--------------------------------------------------------------------------------
""")
print(f"[OK] enlace_repositorio.txt generado en: {repo_txt_path}")

# Empacar ZIP de entrega institucional
zip_name = 'KARENCAMPO_AA10_EV01_GUIA10.zip'
zip_path = os.path.join(ENTREGA_DIR, zip_name)
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, BASE_DIR)
            z.write(full_path, arcname=os.path.join('PET-050_GA10-AA10-EV01', rel_path))
    z.write(repo_txt_path, arcname='enlace_repositorio.txt')
print(f"[OK] Paquete ZIP generado exitosamente ({os.path.getsize(zip_path)/1024:.1f} KB): {zip_path}")
print("=== COMPILACIÓN FINALIZADA CON ÉXITO ===")
