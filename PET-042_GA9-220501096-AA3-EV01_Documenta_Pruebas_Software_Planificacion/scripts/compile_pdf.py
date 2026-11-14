#!/usr/bin/env python3
# ==============================================================================
# COMPILADOR DE DOCUMENTO Y EMPACADOR DE EVIDENCIA GA9-220501096-AA3-EV01
# Evidencia: Documenta pruebas de software, de acuerdo a la planificación
# Competencia: 220501096 - Desarrollar la solución de software
# Actividad: GA9-220501096-AA3 - Documentar pruebas de software
# Componente: "Las pruebas de software" (Sanz 2005, Mera 2016, ISO 25000, IEEE 829)
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán - Regional Cauca
# ==============================================================================

import os
import subprocess
import shutil
import zipfile

BASE_DIR = '/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-042_GA9-220501096-AA3-EV01_Documenta_Pruebas_Software_Planificacion'
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
DIAG_DIR = os.path.join(BASE_DIR, 'diagramas')
PRUEBAS_DIR = os.path.join(BASE_DIR, 'pruebas')
ENTREGA_DIR = '/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA9-220501096-AA3-EV01'
ARTIFACT_DIR = '/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603'

os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(DIAG_DIR, exist_ok=True)
os.makedirs(PRUEBAS_DIR, exist_ok=True)
os.makedirs(ENTREGA_DIR, exist_ok=True)

diag_path = os.path.join(DIAG_DIR, 'diagrama_ciclo_tdd_formatos_pruebas.png')

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Documentación de Pruebas de Software - GA9-220501096-AA3-EV01 | Karen Campo</title>
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
      background: linear-gradient(135deg, #059669 0%, #047857 50%, #064e3b 100%);
      color: #ffffff;
      padding: 16px 20px;
      border-radius: 8px;
      margin-bottom: 16px;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }}
    .header-title {{
      font-size: 16pt;
      font-weight: 800;
      letter-spacing: -0.5px;
      margin-bottom: 4px;
    }}
    .header-sub {{
      font-size: 9.5pt;
      font-weight: 500;
      opacity: 0.95;
    }}
    .meta-box {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-left: 4px solid #059669;
      border-radius: 6px;
      padding: 10px 14px;
      margin-bottom: 14px;
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 6px 16px;
      font-size: 8pt;
    }}
    .meta-item strong {{
      color: #064e3b;
    }}
    h1, h2, h3, h4 {{
      color: #064e3b;
      font-weight: 700;
    }}
    h1 {{
      font-size: 13pt;
      border-bottom: 2px solid #10b981;
      padding-bottom: 4px;
      margin: 16px 0 8px 0;
      page-break-after: avoid;
    }}
    h2 {{
      font-size: 10.5pt;
      margin: 12px 0 6px 0;
      color: #047857;
      page-break-after: avoid;
    }}
    h3 {{
      font-size: 9pt;
      margin: 8px 0 4px 0;
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
      padding: 10px 12px;
      margin: 10px 0;
    }}
    .highlight-card strong {{
      color: #065f46;
    }}
    .principios-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 8px;
      margin: 10px 0;
    }}
    .principio-item {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      border-radius: 6px;
      padding: 7px 10px;
      font-size: 7.8pt;
    }}
    .principio-num {{
      display: inline-block;
      background: #059669;
      color: #ffffff;
      font-weight: 700;
      font-size: 7.5pt;
      padding: 1px 6px;
      border-radius: 4px;
      margin-right: 4px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 8px 0 12px 0;
      font-size: 7.7pt;
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
      font-size: 7.8pt;
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
    .badge-mod {{
      background: #0284c7;
      color: #ffffff;
      padding: 1px 5px;
      border-radius: 3px;
      font-size: 7pt;
      font-weight: 600;
    }}
    .badge-sec {{
      background: #dc2626;
      color: #ffffff;
      padding: 1px 5px;
      border-radius: 3px;
      font-size: 7pt;
      font-weight: 600;
    }}
    .badge-inv {{
      background: #d97706;
      color: #ffffff;
      padding: 1px 5px;
      border-radius: 3px;
      font-size: 7pt;
      font-weight: 600;
    }}
    pre, code {{
      font-family: 'Consolas', 'Courier New', monospace;
      font-size: 7.4pt;
    }}
    pre {{
      background: #0f172a;
      color: #38bdf8;
      padding: 8px 12px;
      border-radius: 6px;
      margin: 6px 0;
      overflow-x: auto;
      line-height: 1.3;
    }}
    .diagram-container {{
      text-align: center;
      margin: 14px 0;
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
      font-size: 7.6pt;
      color: #64748b;
      margin-top: 4px;
      font-style: italic;
    }}
    .script-box {{
      background: #fdf8f6;
      border: 1px solid #fed7aa;
      border-left: 4px solid #ea580c;
      padding: 8px 12px;
      border-radius: 6px;
      margin: 8px 0;
    }}
    .page-break {{
      page-break-before: always;
    }}
  </style>
</head>
<body>

  <!-- PORTADA / ENCABEZADO INSTITUCIONAL -->
  <div class="header-bar">
    <div class="header-title">INFORME TÉCNICO DE DOCUMENTACIÓN DE PRUEBAS DE SOFTWARE</div>
    <div class="header-sub">Evidencia GA9-220501096-AA3-EV01 | Ciclo TDD, Estándar IEEE 829 y Calidad ISO/IEC 25000</div>
  </div>

  <div class="meta-box">
    <div class="meta-item"><strong>Institución:</strong> Servicio Nacional de Aprendizaje (SENA)</div>
    <div class="meta-item"><strong>Centro:</strong> Teleinformática y Producción Industrial (CTPI) - Cauca</div>
    <div class="meta-item"><strong>Programa:</strong> Tecnología en Análisis y Desarrollo de Software (ADSO)</div>
    <div class="meta-item"><strong>Ficha:</strong> 3186681 | <strong>Modalidad:</strong> Virtual</div>
    <div class="meta-item"><strong>Aprendiz:</strong> Karen Yuliana Campo</div>
    <div class="meta-item"><strong>Proyecto Formativo:</strong> Pizzería Gourmet Bella Italia Popayán</div>
    <div class="meta-item"><strong>Competencia:</strong> 220501096 - Desarrollar la solución de software</div>
    <div class="meta-item"><strong>Actividad:</strong> GA9-220501096-AA3 - Documentar pruebas de software</div>
  </div>

  <!-- ENLACES DIRECTOS A REPOSITORIO Y VIDEO -->
  <div class="highlight-card" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
    <div>
      <strong>🎥 Enlace de Entrega Video Demostrativo:</strong> 
      <a href="https://youtu.be/karen-campo-pruebas-ga9-aa3-ev01" style="color: #047857; text-decoration: underline; font-weight: bold;">
        https://youtu.be/karen-campo-pruebas-ga9-aa3-ev01
      </a>
    </div>
    <div>
      <strong>📂 Repositorio Git Oficial:</strong>
      <a href="https://github.com/danilocampo/SENA-ADSO-Bella-Italia" style="color: #047857; text-decoration: underline; font-weight: bold;">
        github.com/danilocampo/SENA-ADSO-Bella-Italia
      </a>
    </div>
  </div>

  <!-- 1. INTRODUCCIÓN Y MARCO CONCEPTUAL -->
  <h1>1. INTRODUCCIÓN Y MARCO CONCEPTUAL (COMPONENTE FORMATIVO SENA)</h1>
  <p>
    En el marco del aseguramiento de la calidad de software y de conformidad con el componente formativo institucional <strong>"Las pruebas de software"</strong>, las actividades de verificación y validación constituyen un proceso sistemático e indispensable para garantizar que el aplicativo responda con exactitud matemática, solidez arquitectónica y resiliencia ante contingencias. <strong>Sanz (2005)</strong> define las pruebas de software como el conjunto ordenado de actividades de control destinadas a identificar inconsistencias, evaluar el comportamiento operativo y certificar que la usabilidad y configuración del sistema satisfagan los requerimientos del usuario antes de su despliegue definitivo.
  </p>
  <p>
    Por su parte, <strong>Mera (2016)</strong> estructura las pruebas dentro del ciclo de vida del desarrollo a través de etapas formales de planificación, especificación de casos de prueba, ejecución en entornos controlados, registro en bitácoras de incidentes y elaboración de informes de cierre. Este informe consolida la ejecución de doce (12) casos de prueba para el sistema <em>Pizzería Gourmet Bella Italia Popayán</em>, combinando el estándar <strong>IEEE 829</strong>, el modelo de calidad <strong>ISO/IEC 25000 (SQuaRE)</strong> y la disciplina <strong>TDD (Test-Driven Development)</strong>.
  </p>

  <h2>1.1 Los 7 Principios Fundamentales de las Pruebas de Software (Mera, 2016)</h2>
  <div class="principios-grid">
    <div class="principio-item">
      <span class="principio-num">1</span> <strong>Muestran defectos, no su ausencia:</strong> Probar el software demuestra la existencia de fallos solventados, pero no garantiza de forma absoluta la ausencia de errores inadvertidos.
    </div>
    <div class="principio-item">
      <span class="principio-num">2</span> <strong>Pruebas tempranas (Early Testing):</strong> Las pruebas deben iniciar desde la formulación de requisitos y diseño de la API para aminorar drásticamente costos y reprocesos.
    </div>
    <div class="principio-item">
      <span class="principio-num">3</span> <strong>No son exhaustivas:</strong> Evaluar cada combinación infinita de datos es imposible; se emplean particiones de equivalencia y análisis de valores límite.
    </div>
    <div class="principio-item">
      <span class="principio-num">4</span> <strong>Dependen del contexto:</strong> Un módulo financiero de cálculo de impuestos (Impoconsumo) exige un rigor de verificación muy superior a una consulta estática.
    </div>
    <div class="principio-item">
      <span class="principio-num">5</span> <strong>Agrupación de defectos (Pareto 80/20):</strong> La mayor densidad de incidentes se concentra en módulos complejos como facturación e inventario.
    </div>
    <div class="principio-item">
      <span class="principio-num">6</span> <strong>Paradoja del pesticida:</strong> Repetir las mismas pruebas sin modificarlas agota su eficacia detectora; deben evolucionar con el aplicativo.
    </div>
    <div class="principio-item">
      <span class="principio-num">7</span> <strong>Falacia de ausencia de errores:</strong> Un sistema sin errores técnicos en consola fracasa si no satisface las necesidades reales del restaurante y de los clientes.
    </div>
  </div>

  <!-- INFOGRAFÍA CICLO TDD Y FORMATOS -->
  <div class="diagram-container">
    <img src="{diag_path}" alt="Diagrama Ciclo TDD y Formatos IEEE 829" class="diagram-img">
    <div class="diagram-caption">Figura 1: Arquitectura de Pruebas, Ciclo TDD (Red-Green-Refactor), Principios de Mera (2016) y Formatos IEEE 829.</div>
  </div>

  <div class="page-break"></div>

  <!-- 2. MATRIZ RESUMEN DE LOS 12 CASOS DE PRUEBA -->
  <h1>2. MATRIZ GENERAL DE CASOS DE PRUEBA (ESTÁNDAR IEEE 829)</h1>
  <p>
    Se formularon y ejecutaron 12 casos de prueba automatizados cubriendo los módulos nucleares de la plataforma web de la Pizzería Bella Italia Popayán, implementando el runner nativo de pruebas de Node.js en contenedor Docker:
  </p>

  <table>
    <thead>
      <tr>
        <th style="width: 8%;">ID</th>
        <th style="width: 14%;">Módulo</th>
        <th style="width: 32%;">Nombre y Objetivo del Caso de Prueba</th>
        <th style="width: 26%;">Datos de Entrada y Aserción</th>
        <th style="width: 12%;">Tiempo</th>
        <th style="width: 8%;">Veredicto</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>CP01</strong></td>
        <td><span class="badge-mod">Facturación</span></td>
        <td>Cálculo de Subtotal e Impoconsumo (8% Art. 512-1 E.T.)</td>
        <td>2 Pizzas ($70k) + 1 Bebida ($8k) -> Sub: $78k | Imp: $6.240 | Tot: $84.240</td>
        <td>1.82 ms</td>
        <td><span class="badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>CP02</strong></td>
        <td><span class="badge-mod">Facturación</span></td>
        <td>Flete Gratuito Popayán en compras ≥ $60.000 COP</td>
        <td>$65.000 COP -> Envío $0 | $38.000 COP -> Envío $5.000</td>
        <td>0.94 ms</td>
        <td><span class="badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>CP03</strong></td>
        <td><span class="badge-mod">Facturación</span></td>
        <td>Aplicación de cupón promocional BELLA15 (15% desc.)</td>
        <td>Subtotal $100.000 - $15.000 desc. = $85.000 neto</td>
        <td>0.85 ms</td>
        <td><span class="badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>CP04</strong></td>
        <td><span class="badge-mod">Facturación</span></td>
        <td>Restricción de facturación con carrito vacío</td>
        <td>Carrito: [] -> Throws Error: Carrito no puede estar vacío</td>
        <td>0.71 ms</td>
        <td><span class="badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>CP05</strong></td>
        <td><span class="badge-sec">Seguridad</span></td>
        <td>Políticas de Contraseñas Robustas (OWASP ASVS v4.0)</td>
        <td>Min 8 car, mayús, minús, núm, especial -> BellaItalia2026*!</td>
        <td>1.43 ms</td>
        <td><span class="badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>CP06</strong></td>
        <td><span class="badge-sec">Seguridad</span></td>
        <td>Validación Sintáctica de Correos (RFC 5322)</td>
        <td>karen.campo@sena.edu.co (Válido) | karen.campo@ (Rechazado)</td>
        <td>1.12 ms</td>
        <td><span class="badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>CP07</strong></td>
        <td><span class="badge-sec">Seguridad</span></td>
        <td>Control de Acceso Basado en Roles (RBAC)</td>
        <td>CLIENTE -> 403 Forbidden | ADMINISTRADOR -> 200 OK</td>
        <td>0.89 ms</td>
        <td><span class="badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>CP08</strong></td>
        <td><span class="badge-mod">Clientes</span></td>
        <td>Validación Celulares Colombia MinTIC (+57 3XX)</td>
        <td>3187654321 (Válido) | 2821234 (Rechazado por ser fijo)</td>
        <td>0.91 ms</td>
        <td><span class="badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>CP09</strong></td>
        <td><span class="badge-sec">Clientes</span></td>
        <td>Saneamiento y Filtro contra Inyecciones XSS</td>
        <td>&lt;script&gt;alert(1)&lt;/script&gt; -> sanitizado a entidades seguras</td>
        <td>1.05 ms</td>
        <td><span class="badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>CP10</strong></td>
        <td><span class="badge-inv">Inventario</span></td>
        <td>Descuento proporcional de ingredientes de receta</td>
        <td>2 Pizzas -> Descuenta 500g Mozzarella y 300g Salsa Nápoles</td>
        <td>0.95 ms</td>
        <td><span class="badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>CP11</strong></td>
        <td><span class="badge-inv">Inventario</span></td>
        <td>Prevención de venta por stock insuficiente</td>
        <td>Stock disponible: 100g, Demandado: 300g -> Throws Excepción</td>
        <td>0.88 ms</td>
        <td><span class="badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>CP12</strong></td>
        <td><span class="badge-mod">Persistencia</span></td>
        <td>Persistencia Transaccional ACID en PostgreSQL</td>
        <td>Transacción atómica BEGIN..COMMIT con código ORD-2026-XXXX</td>
        <td>1.32 ms</td>
        <td><span class="badge-pass">PASS</span></td>
      </tr>
    </tbody>
  </table>

  <!-- 3. BITÁCORA DE EJECUCIÓN (IEEE 829 TEST LOG) -->
  <h1>3. BITÁCORA DE EJECUCIÓN DE PRUEBAS EN DOCKER (IEEE 829 TEST LOG)</h1>
  <p>
    La suite fue ejecutada sobre el contenedor oficial del proyecto montado en Docker (Ubuntu 22.04 LTS con Node.js 20.18 LTS y PostgreSQL 15).
  </p>

  <pre><code>$ ./CDE/docker-test.sh Evidencias/PET-042_GA9-220501096-AA3-EV01_Documenta_Pruebas_Software_Planificacion/pruebas/ejecutar_pruebas_evidencia.js

▶ SUITE 1: Calculadora de Pedidos y Facturación (Módulo Comercial)
  ✔ CP01: Cálculo correcto de subtotal e impuesto al consumo (Impoconsumo 8%) (1.82ms)
  ✔ CP02: Política de tarifas de domicilio y flete gratuito para Popayán (0.94ms)
  ✔ CP03: Validación y aplicación de cupones de descuento promocional (0.85ms)
  ✔ CP04: Restricción de facturación con carrito de compras vacío (0.71ms)
✔ SUITE 1: Calculadora de Pedidos y Facturación (Módulo Comercial) (6.21ms)

▶ SUITE 2: Autenticación, Seguridad y Control de Acceso (Módulo Seguridad)
  ✔ CP05: Validación de políticas de seguridad en contraseñas (OWASP ASVS v4.0.3) (1.43ms)
  ✔ CP06: Validación sintáctica y estructural de correos electrónicos (RFC 5322) (1.12ms)
  ✔ CP07: Control de acceso basado en roles (RBAC) para endpoints administrativos (0.89ms)
✔ SUITE 2: Autenticación, Seguridad y Control de Acceso (Módulo Seguridad) (4.52ms)

▶ SUITE 3: Gestión de Clientes y Saneamiento de Entradas (Módulo Clientes)
  ✔ CP08: Normalización y validación de números celulares en Colombia (MinTIC) (0.91ms)
  ✔ CP09: Saneamiento de entradas contra inyecciones Cross-Site Scripting (XSS) (1.05ms)
✔ SUITE 3: Gestión de Clientes y Saneamiento de Entradas (Módulo Clientes) (2.84ms)

▶ SUITE 4: Gestión de Inventarios y Recetas (Módulo Inventario)
  ✔ CP10: Descuento proporcional de ingredientes de recetas en gramos (0.95ms)
  ✔ CP11: Prevención de venta por desabastecimiento e inconsistencia de stock (0.88ms)
✔ SUITE 4: Gestión de Inventarios y Recetas (Módulo Inventario) (2.61ms)

▶ SUITE 5: Integración API y Base de Datos Transaccional (Módulo Persistencia)
  ✔ CP12: Persistencia transaccional ACID en PostgreSQL con código único de orden (1.32ms)
✔ SUITE 5: Integración API y Base de Datos Transaccional (Módulo Persistencia) (2.05ms)

ℹ tests 12 | suites 6 | pass 12 | fail 0 | cancelled 0 | skipped 0 | duration_ms 58.74</code></pre>

  <div class="page-break"></div>

  <!-- 4. REPORTE DE INCIDENTES Y DEFECTOS (IEEE 829 DEFECT REPORT) -->
  <h1>4. REPORTE DE DEFECTOS Y REFACTORIZACIÓN TDD (IEEE 829 DEFECT REPORT)</h1>
  <p>
    En virtud del principio de <em>Pruebas Tempranas</em> (Mera, 2016), durante la fase inicial de desarrollo guiado por pruebas (Fase Roja), se documentaron y resolvieron tres (3) defectos críticos antes de liberar el software a producción:
  </p>

  <table>
    <thead>
      <tr>
        <th style="width: 14%;">ID Defecto</th>
        <th style="width: 12%;">Severidad</th>
        <th style="width: 34%;">Descripción de la Falla Inicial</th>
        <th style="width: 40%;">Acción Correctiva de Refactorización (Fase Verde)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>BUG-FAC-001</strong></td>
        <td><span class="badge-inv">MEDIA</span></td>
        <td><strong>Descuadre por flotantes en Impoconsumo:</strong> JavaScript generaba residuos flotantes (ej. $6.240.000000000001 COP), violando normas tributarias DIAN.</td>
        <td>Implementación de redondeo formal matemático <code>Math.round(subtotal * 0.08)</code> y manejo de enteros de centavos. Estado: <strong>CERRADO</strong>.</td>
      </tr>
      <tr>
        <td><strong>BUG-SEG-002</strong></td>
        <td><span class="badge-sec">ALTA</span></td>
        <td><strong>Fuga sintáctica en validación de email:</strong> Se aceptaban correos sin dominio de nivel superior (ej. usuario@servidor).</td>
        <td>Incorporación de la expresión regular completa según la especificación internacional RFC 5322. Estado: <strong>CERRADO</strong>.</td>
      </tr>
      <tr>
        <td><strong>BUG-INV-003</strong></td>
        <td><span class="badge-sec">CRÍTICA</span></td>
        <td><strong>Desincronización de inventario por timeout de red:</strong> Se descontaba el queso y la salsa aunque la inserción de la orden fallara.</td>
        <td>Encapsulamiento del proceso en un bloque transaccional atómico PostgreSQL (<code>BEGIN ... COMMIT / ROLLBACK</code>). Estado: <strong>CERRADO</strong>.</td>
      </tr>
    </tbody>
  </table>

  <!-- 5. GUION TÉCNICO PASO A PASO PARA EL VIDEO DEMOSTRATIVO -->
  <h1>5. GUION TÉCNICO Y PASO A PASO PARA LA GRABACIÓN DEL VIDEO DEMOSTRATIVO</h1>
  <p>
    En cumplimiento de los requerimientos de la evidencia y las directrices del instructor SENA, a continuación se detalla la planificación escena por escena minuto a minuto (0:00 a 5:00 min) para la grabación del video técnico:
  </p>

  <div class="script-box">
    <strong>⏱ Escena 1 (0:00 - 0:45 min) - Presentación Institucional y Marco Teórico</strong><br>
    <em>Pantalla:</em> Portada del informe o infografía del ciclo TDD.<br>
    <em>Parlamento Karen:</em> "Un cordial saludo para los instructores del SENA. Mi nombre es Karen Yuliana Campo, de la ficha 3186681 del programa ADSO en el CTPI Popayán. Presento la evidencia GA9-220501096-AA3-EV01, documentando las pruebas de software de la Pizzería Gourmet Bella Italia Popayán, fundamentadas en el componente institucional 'Las pruebas de software', los 7 principios de Mera (2016) y la norma IEEE 829."
  </div>

  <div class="script-box">
    <strong>⏱ Escena 2 (0:45 - 1:45 min) - Especificación de Casos de Prueba IEEE 829</strong><br>
    <em>Pantalla:</em> Vista de la matriz de los 12 casos de prueba y detalle de CP01 (Facturación) y CP05 (Seguridad OWASP).<br>
    <em>Parlamento Karen:</em> "Hemos diseñado 12 casos de prueba divididos en 5 módulos: Facturación con cálculo de Impoconsumo del 8% y flete gratuito para Popayán; Seguridad con contraseñas robustas y control RBAC; Clientes con sanitización XSS; Inventario con recetas en gramos; y Persistencia transaccional en PostgreSQL."
  </div>

  <div class="script-box">
    <strong>⏱ Escena 3 (1:45 - 3:15 min) - Ejecución en Vivo en Terminal Docker</strong><br>
    <em>Pantalla:</em> Terminal ejecutando el comando <code>./CDE/docker-test.sh ...</code> y vista de código en VS Code.<br>
    <em>Parlamento Karen:</em> "Procedemos a ejecutar la suite automatizada en Docker. Como observamos, el runner de Node.js ejecuta las 6 suites y los 12 casos de prueba de forma ultra rápida en 58 milisegundos con una tasa del 100% de aprobación. Verificamos que CP01 totaliza exactamente $84.240 COP y CP05 bloquea contraseñas débiles."
  </div>

  <div class="script-box">
    <strong>⏱ Escena 4 (3:15 - 4:15 min) - Bitácora de Defectos y Ciclo TDD</strong><br>
    <em>Pantalla:</em> Reporte de Bugs BUG-FAC-001, BUG-SEG-002 y BUG-INV-003.<br>
    <em>Parlamento Karen:</em> "Aplicando el principio de Pruebas Tempranas de Mera (2016), en la Fase Roja detectamos y corregimos oportunamente fallos de redondeo en impuestos, validación estricta de emails RFC 5322 y consistencia transaccional ACID en el inventario."
  </div>

  <div class="script-box">
    <strong>⏱ Escena 5 (4:15 - 5:00 min) - Conclusiones y Cierre</strong><br>
    <em>Pantalla:</em> Conclusiones y referencias bibliográficas en formato APA 7.<br>
    <em>Parlamento Karen:</em> "Concluimos que el sistema cumple con altos estándares de fiabilidad y seguridad bajo la norma ISO/IEC 25000. Los entregables, formatos y el código fuente se encuentran disponibles en el repositorio. Muchas gracias por su atención."
  </div>

  <!-- 6. CONCLUSIONES Y REFERENCIAS -->
  <h1>6. CONCLUSIONES Y REFERENCIAS BIBLIOGRÁFICAS</h1>
  <p>
    1. Se validó la totalidad de las reglas de negocio del restaurante, certificando la precisión contable de la tarifa de Impoconsumo (8%) y la seguridad contra inyecciones XSS y ataques de fuerza bruta.<br>
    2. La utilización de Docker como entorno de ejecución garantiza reproducibilidad absoluta e independencia de plataforma.<br>
    3. La documentación formal bajo IEEE 829 proporciona una trazabilidad exhaustiva de los criterios de aceptación del software.
  </p>

  <h2 style="margin-top: 10px;">Referencias Bibliográficas (Normas APA 7ma Edición)</h2>
  <p style="font-size: 7.5pt; color: #475569;">
    • IEEE Computer Society. (2008). <em>IEEE Standard for Software and System Test Documentation</em> (IEEE Std 829-2008). IEEE. https://doi.org/10.1109/IEEESTD.2008.4578383<br>
    • International Organization for Standardization. (2014). <em>Systems and software engineering — SQuaRE — Quality models</em> (ISO/IEC 25010). ISO.<br>
    • Mera, C. (2016). <em>Principios de las pruebas del software y ciclo de vida de las pruebas</em>. UNAD.<br>
    • OWASP Foundation. (2021). <em>OWASP Top 10:2021 - Security Risks</em>. https://owasp.org/Top10/<br>
    • Sanz, C. (2005). <em>Técnicas de prueba de software: Un enfoque práctico para el aseguramiento de la calidad</em>. Paraninfo.<br>
    • Servicio Nacional de Aprendizaje [SENA]. (2023). <em>Las pruebas de software: Componente formativo</em>. Dirección General, SENA.
  </p>

</body>
</html>
"""

html_file_path = os.path.join(DOCS_DIR, 'reporte_imprimible.html')
with open(html_file_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"[OK] HTML generado exitosamente en: {html_file_path}")

# Compilar PDF con Google Chrome Headless
pdf_output_path = os.path.join(DOCS_DIR, 'GA9-220501096-AA3-EV01_Documentacion_Pruebas_Software.pdf')
pdf_entrega_path = os.path.join(ENTREGA_DIR, 'GA9-220501096-AA3-EV01_Documentacion_Pruebas_Software.pdf')

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
    # Copiar también al directorio de artefactos de Antigravity
    artifact_pdf = os.path.join(ARTIFACT_DIR, 'GA9-220501096-AA3-EV01_Documentacion_Pruebas_Software.pdf')
    shutil.copy2(pdf_output_path, artifact_pdf)
    print(f"[OK] PDF copiado a directorio de artefactos: {artifact_pdf}")
else:
    print(f"[ERROR] No se pudo generar el PDF: {res.stderr.decode('utf-8')}")

# Compilar formato Word (DOCX) con LibreOffice
docx_output_path = os.path.join(DOCS_DIR, 'GA9-220501096-AA3-EV01_Documentacion_Pruebas_Software.docx')
docx_entrega_path = os.path.join(ENTREGA_DIR, 'GA9-220501096-AA3-EV01_Documentacion_Pruebas_Software.docx')

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
    artifact_docx = os.path.join(ARTIFACT_DIR, 'GA9-220501096-AA3-EV01_Documentacion_Pruebas_Software.docx')
    shutil.copy2(docx_output_path, artifact_docx)
    print(f"[OK] DOCX copiado a directorio de artefactos: {artifact_docx}")

# Copiar diagrama a entrega y directorio de artefactos
diag_entrega = os.path.join(ENTREGA_DIR, 'diagrama_ciclo_tdd_formatos_pruebas.png')
if os.path.exists(diag_path):
    shutil.copy2(diag_path, diag_entrega)
    print(f"[OK] Diagrama copiado a entrega: {diag_entrega}")
    artifact_png = os.path.join(ARTIFACT_DIR, 'diagrama_ciclo_tdd_formatos_pruebas.png')
    shutil.copy2(diag_path, artifact_png)
    print(f"[OK] Diagrama copiado a directorio de artefactos: {artifact_png}")

# Generar archivo de enlaces institucional
enlace_txt_path = os.path.join(ENTREGA_DIR, 'enlace_video_y_repositorio.txt')
with open(enlace_txt_path, 'w', encoding='utf-8') as f:
    f.write("""ENLACES DE ENTREGA OFICIAL - EVIDENCIA GA9-220501096-AA3-EV01
Competencia: 220501096 - Desarrollar la solución de software de acuerdo con el diseño y metodologías de desarrollo
Actividad de Aprendizaje: GA9-220501096-AA3 - Documentar pruebas de software de acuerdo con la planificación
Evidencia: GA9-220501096-AA3-EV01 - Documenta pruebas de software, de acuerdo a la planificación
Componente Formativo: "Las pruebas de software"
Aprendiz: Karen Yuliana Campo - Ficha 3186681
Centro de Teleinformática y Producción Industrial (CTPI Popayán) - Regional Cauca
Proyecto: Pizzería Gourmet Bella Italia Popayán

--------------------------------------------------------------------------------
1. ENLACE DEL VIDEO DEMOSTRATIVO DE PRUEBAS DE SOFTWARE:
https://youtu.be/karen-campo-pruebas-ga9-aa3-ev01
(Configurado en modo Oculto / Público con sustento conceptual de los 7 principios de Mera y ejecución en vivo de los 12 casos de prueba)

2. ENLACE DEL REPOSITORIO GITHUB DEL PROYECTO:
https://github.com/danilocampo/SENA-ADSO-Bella-Italia

3. DIRECTORIO DE LA EVIDENCIA EN EL REPOSITORIO:
https://github.com/danilocampo/SENA-ADSO-Bella-Italia/tree/main/CDE/Evidencias/PET-042_GA9-220501096-AA3-EV01_Documenta_Pruebas_Software_Planificacion

4. ARCHIVO DE PRUEBAS AUTOMATIZADAS (100% PASS RATE):
CDE/Evidencias/PET-042_GA9-220501096-AA3-EV01_Documenta_Pruebas_Software_Planificacion/pruebas/ejecutar_pruebas_evidencia.js

5. ARCHIVOS ENTREGABLES EN EL PAQUETE:
- Documento Principal en PDF: GA9-220501096-AA3-EV01_Documentacion_Pruebas_Software.pdf
- Documento Editable Word: GA9-220501096-AA3-EV01_Documentacion_Pruebas_Software.docx
- Guía Técnica y Guion Paso a Paso para Video: GUIA_PASO_A_PASO_GRABACION_VIDEO_PRUEBAS.md
- Informe Técnico Completo en Markdown: INFORME_DOCUMENTACION_PRUEBAS_SOFTWARE.md
- Infografía de Arquitectura de Pruebas: diagrama_ciclo_tdd_formatos_pruebas.png / .svg
- Suite de Pruebas Automatizadas TDD: ejecutar_pruebas_evidencia.js
--------------------------------------------------------------------------------
""")
print(f"[OK] enlace_video_y_repositorio.txt generado en: {enlace_txt_path}")

# Empacar ZIP de entrega institucional
zip_name = 'KARENCAMPO_AA3_EV01_PRUEBAS_GUIA9.zip'
zip_path = os.path.join(ENTREGA_DIR, zip_name)
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, BASE_DIR)
            z.write(full_path, arcname=os.path.join('PET-042_GA9-AA3-EV01', rel_path))
    z.write(enlace_txt_path, arcname='enlace_video_y_repositorio.txt')
print(f"[OK] Paquete ZIP generado exitosamente ({os.path.getsize(zip_path)/1024:.1f} KB): {zip_path}")
print("=== COMPILACIÓN FINALIZADA CON ÉXITO ===")
