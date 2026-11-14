#!/usr/bin/env python3
# ==============================================================================
# COMPILADOR DE MODELO LEAN CANVAS Y EMPACADOR DE EVIDENCIA GA10-240201529-AA2-EV02
# Evidencia: GA10-240201529-AA2-EV02 - Modelo Canvas del emprendimiento
# Competencia: 240201529 - Gestionar procesos de la cultura emprendedora
# Actividad: GA10-240201529-AA2 - Definir la idea de negocio a desarrollar en el emprendimiento
# Componente: "Entendiendo la empresa" / "Ser emprendedor"
# Instrumento: Lista de Chequeo IE-GA10-240201529-AA2-EV02
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán - Regional Cauca
# ==============================================================================

import os
import subprocess
import shutil
import zipfile

BASE_DIR = '/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-053_GA10-240201529-AA2-EV02_Modelo_Canvas_Emprendimiento'
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
SITIO_DIR = os.path.join(BASE_DIR, 'sitio_lean_canvas')
DIAG_DIR = os.path.join(BASE_DIR, 'diagramas')
CAPTURAS_DIR = os.path.join(BASE_DIR, 'capturas')
ENTREGA_DIR = '/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA10-240201529-AA2-EV02'
ARTIFACT_DIR = '/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603'

os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(DIAG_DIR, exist_ok=True)
os.makedirs(CAPTURAS_DIR, exist_ok=True)
os.makedirs(ENTREGA_DIR, exist_ok=True)

diag_canvas = os.path.join(DIAG_DIR, 'matriz_lean_canvas_pizzeria_bella_italia.png')

cap1_path = os.path.join(CAPTURAS_DIR, 'paso_01_despliegue_docker_lean_canvas_konsole.png')
cap2_path = os.path.join(CAPTURAS_DIR, 'paso_02_verificacion_salud_servicios_konsole.png')
cap3_path = os.path.join(CAPTURAS_DIR, 'paso_03_chrome_lean_canvas_portada_canvas.png')
cap4_path = os.path.join(CAPTURAS_DIR, 'paso_04_chrome_lean_canvas_bloques_problema_solucion.png')
cap5_path = os.path.join(CAPTURAS_DIR, 'paso_05_chrome_lean_canvas_propuesta_valor_ventaja.png')
cap6_path = os.path.join(CAPTURAS_DIR, 'paso_06_chrome_lean_canvas_costos_ingresos_metricas.png')

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Modelo Lean Canvas - GA10-240201529-AA2-EV02 | Karen Campo</title>
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
      line-height: 1.38;
      font-size: 8.4pt;
      background: #ffffff;
    }}
    .header-bar {{
      background: linear-gradient(135deg, #047857 0%, #065f46 50%, #064e3b 100%);
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
      color: #047857;
    }}
    h1, h2, h3, h4 {{
      color: #047857;
      font-weight: 700;
    }}
    h1 {{
      font-size: 11.8pt;
      border-bottom: 2px solid #047857;
      padding-bottom: 3px;
      margin-top: 14px;
      margin-bottom: 8px;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }}
    h2 {{
      font-size: 9.7pt;
      margin-top: 10px;
      margin-bottom: 5px;
      color: #0f172a;
    }}
    h3 {{
      font-size: 8.8pt;
      margin-top: 8px;
      margin-bottom: 4px;
      color: #047857;
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
      background-color: #047857;
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
    .badge-danger {{
      background-color: #fee2e2;
      color: #b91c1c;
      border: 1px solid #fca5a5;
    }}
    .badge-primary {{
      background-color: #e0f2fe;
      color: #0369a1;
      border: 1px solid #7dd3fc;
    }}
    .badge-warning {{
      background-color: #fef3c7;
      color: #b45309;
      border: 1px solid #fcd34d;
    }}
    .info-card {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      border-left: 4px solid #047857;
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
    .step-card {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 8px 11px;
      margin-bottom: 8px;
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
      margin-top: 4px;
      font-style: italic;
    }}
    .page-break {{
      page-break-before: always;
    }}
    code {{
      background-color: #f1f5f9;
      padding: 1px 4px;
      border-radius: 3px;
      font-family: 'Consolas', 'Courier New', monospace;
      font-size: 7.6pt;
      color: #065f46;
    }}
  </style>
</head>
<body>

  <!-- ENCABEZADO INSTITUCIONAL -->
  <div class="header-bar">
    <div class="header-title">MODELO LEAN CANVAS DEL EMPRENDIMIENTO</div>
    <div class="header-sub">Definir la idea de negocio a desarrollar en el emprendimiento, según las oportunidades de mercado</div>
  </div>

  <!-- METADATOS INSTITUCIONALES SENA -->
  <div class="meta-box">
    <div class="meta-item"><strong>Programa:</strong> Análisis y Desarrollo de Software (ADSO)</div>
    <div class="meta-item"><strong>Ficha SENA:</strong> 3186681</div>
    <div class="meta-item"><strong>Competencia Transversal:</strong> 240201529 - Cultura Emprendedora y Empresarial</div>
    <div class="meta-item"><strong>Fase del Proyecto:</strong> Fase 4 - Implantación (AP10)</div>
    <div class="meta-item"><strong>Actividad de Aprendizaje:</strong> GA10-240201529-AA2 - Definir la idea de negocio</div>
    <div class="meta-item"><strong>Evidencia Oficial:</strong> GA10-240201529-AA2-EV02 - Modelo Canvas del emprendimiento</div>
    <div class="meta-item"><strong>Instrumento de Evaluación:</strong> IE-GA10-240201529-AA2-EV02 (Lista de Chequeo)</div>
    <div class="meta-item"><strong>Componente Formativo:</strong> Entendiendo la empresa / Ser emprendedor</div>
    <div class="meta-item"><strong>Aprendiz:</strong> Karen Yuliana Campo</div>
    <div class="meta-item"><strong>Instructor Técnico:</strong> Danilo</div>
    <div class="meta-item"><strong>Centro de Formación:</strong> CTPI Popayán - Regional Cauca</div>
    <div class="meta-item"><strong>Proyecto Productivo:</strong> Pizzería Gourmet Bella Italia Popayán</div>
  </div>

  <div class="info-card">
    <strong>Resumen Ejecutivo:</strong> La presente evidencia consolida la estructuración del modelo de negocio ágil <strong>Lean Canvas</strong> para la iniciativa empresarial y tecnológica <strong>Pizzería Gourmet Bella Italia Popayán</strong>. De acuerdo con las pautas de la <strong>Guía 10 (Sección 3.2.2)</strong> y la metodología de Ash Maurya (2012), se analizaron las cuatro (4) áreas estratégicas (Clientes, Oferta, Infraestructura y Viabilidad Económica) y se desarrollaron a profundidad los nueve (9) bloques constitutivos, complementados con un portal web interactivo desplegado en Docker en el puerto <code>8101</code>, análisis financiero de punto de equilibrio (310 pizzas/mes) y validación de hipótesis con <em>Early Adopters</em>.
  </div>

  <!-- SECCIÓN 1: INTRODUCCIÓN Y MARCO METODOLÓGICO -->
  <h1>1. INTRODUCCIÓN Y MARCO METODOLÓGICO DEL LEAN CANVAS</h1>
  <p>
    El éxito de una empresa en etapas tempranas no depende de planes de negocio burocráticos y extensos, sino de la capacidad para formular hipótesis claras, probarlas con clientes reales y pivotar rápidamente. El **Lean Canvas** es la herramienta estándar del movimiento *Lean Startup* para modelar negocios en un lienzo visual de una sola página.
  </p>
  <p>
    En el contexto del Servicio Nacional de Aprendizaje (SENA) y la formación ADSO, el Lean Canvas permite que la aprendiz **Karen Yuliana Campo** vincule el rigor técnico del desarrollo de software (arquitectura web, pantalla de cocina KDS y facturación electrónica DIAN) con las dinámicas comerciales del sector gastronómico de Popayán (reconocida internacionalmente como Ciudad Creativa de la Gastronomía por la UNESCO).
  </p>

  <!-- SECCIÓN 2: CONTEXTO DE LA IDEA DE NEGOCIO -->
  <h1>2. CONTEXTO Y DESCRIPCIÓN DE LA IDEA DE NEGOCIO</h1>
  <p>
    <strong>Pizzería Gourmet Bella Italia Popayán</strong> es un modelo de negocio híbrido que combina la alta cocina artesanal con una infraestructura tecnológica propia:
  </p>
  <ul>
    <li><strong>Propuesta Gastronómica:</strong> Masas con fermentación natural lenta de 48 horas en leña de roble a 400°C, fusionadas con ingredientes autóctonos caucanos de alta cocina: pipián payanés tradicional, quesos madurados de Silvia y trucha ahumada.</li>
    <li><strong>Infraestructura Digital:</strong> Portal de comercio electrónico propio que elimina las comisiones abusivas del 25%-30% de plataformas de delivery comerciales, conectado en tiempo real a una pantalla de cocina KDS y facturación electrónica DIAN con código CUFE y QR.</li>
  </ul>

  <!-- SECCIÓN 3: LAS CUATRO ÁREAS ESTRATÉGICAS -->
  <h1>3. ANÁLISIS DE LAS CUATRO (4) ÁREAS ESTRATÉGICAS</h1>
  <table>
    <thead>
      <tr>
        <th style="width: 25%;">Área Estratégica</th>
        <th style="width: 35%;">Bloques Constitutivos</th>
        <th style="width: 40%;">Aporte Estratégico al Emprendimiento</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. Área de Clientes</strong></td>
        <td>• Segmento de Clientes<br>• Canales Directos<br>• Early Adopters</td>
        <td>Focalización en comensales locales (estratos 3-5) y turistas gastronómicos UNESCO, conectando por canal web propio sin intermediarios.</td>
      </tr>
      <tr>
        <td><strong>2. Área de Oferta</strong></td>
        <td>• Problema Validado<br>• Solución Innovadora<br>• Propuesta Única de Valor</td>
        <td>Sustitución de masas industriales por pizzas digestivas de 48h con sabor caucano auténtico y personalización interactiva.</td>
      </tr>
      <tr>
        <td><strong>3. Área de Infraestructura</strong></td>
        <td>• Ventaja Injusta<br>• Métricas Claves (KPIs)</td>
        <td>Apalancamiento de software propietario ADSO (cero costo de licencias), hornos de leña y control de tiempos de cocción (14 min).</td>
      </tr>
      <tr>
        <td><strong>4. Viabilidad Económica</strong></td>
        <td>• Estructura de Costos<br>• Flujos de Ingresos</td>
        <td>Margen bruto del 67.9% con costos de materia prima menores al 32% y punto de equilibrio alcanzable con solo 10.3 pizzas/día.</td>
      </tr>
    </tbody>
  </table>

  <!-- SECCIÓN 4: LOS NUEVE BLOQUES DEL LEAN CANVAS -->
  <h1>4. DESARROLLO DETALLADO DE LOS NUEVE (9) BLOQUES DEL LEAN CANVAS</h1>
  <h2>4.1 Bloque 1: Problema</h2>
  <ul>
    <li><strong>Masas Pesadas e Industriales:</strong> Falta de pizzas con fermentación natural lenta de 48 horas en Popayán; predominio de harinas refinadas con químicos que causan pesadez digestiva.</li>
    <li><strong>Falta de Identidad Caucana:</strong> Inexistencia de cartas de pizzas casuales que incorporen pipián payanés o quesos de Silvia.</li>
    <li><strong>Altas Comisiones de Delivery:</strong> Apps comerciales cobran 25%-30% y generan demoras sin emitir factura electrónica formal.</li>
    <li><em>Alternativas Existentes:</em> Cadenas multinacionales de pizza rápida congelada y pizzerías informales de barrio.</li>
  </ul>

  <h2>4.2 Bloque 2: Segmento de Clientes</h2>
  <ul>
    <li>Familias, jóvenes y profesionales de estratos 3, 4 y 5 de Popayán que buscan alimentación saludable y de autor.</li>
    <li>Turistas atraídos por el patrimonio gastronómico de Popayán UNESCO.</li>
    <li>Empleados de oficinas del Centro Histórico que requieren despachos ejecutivos con factura formal DIAN.</li>
    <li><em>Early Adopters:</em> Comensales apasionados por la masa madre y usuarios digitales que ordenan por smartphone.</li>
  </ul>

  <h2>4.3 Bloque 3: Propuesta Única de Valor (UVP)</h2>
  <div class="info-card">
    <strong>Lema Principal:</strong> <em>"El auténtico arte pizzero napolitano con el alma y sabor de la gastronomía caucana."</em><br>
    Pizzas artesanales altamente digestivas con 48h de fermentación en horno de leña a 400°C e ingredientes autóctonos de Silvia y Popayán, gestionadas por plataforma web propia con facturación DIAN en 2 segundos.
  </div>

  <h2>4.4 Bloque 4: Solución</h2>
  <ul>
    <li>Masa de fermentación de 48h horneada en leña a 400°C en solo 90 segundos.</li>
    <li>Línea de autor con productos de origen: Pipián Gourmet y Silvia Campesina.</li>
    <li>Ecosistema digital propio (E-Commerce, KDS en cocina y facturación DIAN) sin intermediarios.</li>
  </ul>

  <h2>4.5 Bloque 5: Canales</h2>
  <ul>
    <li>Portal Web Oficial responsivo (<code>http://localhost:8101/</code>).</li>
    <li>Restaurante boutique con salón en el Centro Histórico de Popayán.</li>
    <li>Flota propia de domicilios con empaque térmico ecológico a 70°C.</li>
    <li>Redes sociales (Instagram, TikTok) con storytelling del proceso de leña.</li>
  </ul>

  <h2>4.6 Bloque 6: Flujos de Ingresos</h2>
  <ul>
    <li>Pizzas Clásicas: $32.000 a $38.000 COP por unidad.</li>
    <li>Especialidades Caucana Gourmet: $42.000 a $48.000 COP por unidad.</li>
    <li>Calzones, Focaccias y Postres: $8.000 a $16.000 COP por unidad.</li>
    <li>Bebidas Artesanales & Café de Silvia: $5.000 a $9.000 COP por unidad.</li>
    <li>Medios de Pago: Wompi (PSE, Tarjetas), Bancolombia QR, Datáfono y Efectivo.</li>
  </ul>

  <h2>4.7 Bloque 7: Estructura de Costos</h2>
  <ul>
    <li><strong>Costos Fijos Mensuales ($8.000.000 COP):</strong> Arriendo local Centro ($2.500.000), Nómina base 3 personas ($4.200.000), Servicios y fibra óptica ($800.000), Hosting y DIAN ($500.000).</li>
    <li><strong>Costos Variables Unitarios (~$12.200 COP):</strong> Materia prima (~30%), empaque ecológico ($1.800), leña de roble y pasarela digital.</li>
  </ul>

  <h2>4.8 Bloque 8: Métricas Claves (KPIs)</h2>
  <ul>
    <li>Costo de Adquisición de Clientes (CAC): &lt; $6.000 COP.</li>
    <li>Valor del Tiempo de Vida del Cliente (LTV): $320.000 COP anuales.</li>
    <li>Tasa de Retención Mensual: &gt; 42% de recompra recurrente.</li>
    <li>Tiempo Promedio KDS: 14 minutos en horno de leña.</li>
    <li>Margen de Contribución Bruto: 67.9% sobre ventas.</li>
  </ul>

  <h2>4.9 Bloque 9: Ventaja Injusta</h2>
  <ul>
    <li>Software propietario ADSO (E-Commerce, KDS, POS) programado por Karen Campo sin pagos de licencias a terceros.</li>
    <li>Recetas registradas de masa madre 48h con pipián payanés.</li>
    <li>Alianzas directas de comercio justo con productores campesinos de Silvia.</li>
    <li>Sello de Popayán UNESCO y asesoría del Fondo Emprender SENA.</li>
  </ul>

  <!-- SECCIÓN 5: MATRIZ GRÁFICA DEL LEAN CANVAS -->
  <h1>5. MATRIZ LEAN CANVAS GRÁFICA OFICIAL</h1>
  <div class="img-container">
    <img src="{diag_canvas}" alt="Matriz Lean Canvas de la Pizzería">
    <div class="caption">Figura 1: Matriz Lean Canvas Oficial de 9 Bloques - Pizzería Gourmet Bella Italia Popayán.</div>
  </div>

  <!-- SECCIÓN 6: SIMULACIÓN FINANCIERA -->
  <h1>6. SIMULACIÓN FINANCIERA Y PUNTO DE EQUILIBRIO</h1>
  <p>
    El punto de equilibrio se determinó mediante la relación entre los costos fijos mensuales y el margen de contribución unitario:
  </p>
  <table>
    <thead>
      <tr>
        <th>Variable Financiera</th>
        <th>Valor Unitario / Mensual</th>
        <th>Interpretación Operativa</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Precio de Venta Promedio (P)</td>
        <td>$38.000 COP</td>
        <td>Ticket promedio ponderado de la carta.</td>
      </tr>
      <tr>
        <td>Costo Variable Unitario (CV)</td>
        <td>$12.200 COP</td>
        <td>Materia prima directa (30%) + empaque + leña.</td>
      </tr>
      <tr>
        <td>Margen de Contribución (MC)</td>
        <td>$25.800 COP (67.9%)</td>
        <td>Recurso neto por pizza para absorber fijos.</td>
      </tr>
      <tr>
        <td>Costos Fijos Mensuales (CF)</td>
        <td>$8.000.000 COP</td>
        <td>Nómina, arriendo Centro, servicios y hosting.</td>
      </tr>
      <tr style="background:#ecfdf5; font-weight:bold;">
        <td>PUNTO DE EQUILIBRIO MENSUAL</td>
        <td>310 pizzas / mes</td>
        <td>Solo 10.3 pizzas al día para cubrir la operación.</td>
      </tr>
      <tr style="background:#f0f9ff; font-weight:bold;">
        <td>UTILIDAD NETA (650 pizzas/mes)</td>
        <td>$8.770.000 COP / mes</td>
        <td>Rentabilidad neta del 35.5% sobre ventas.</td>
      </tr>
    </tbody>
  </table>

  <div class="page-break"></div>

  <!-- SECCIÓN 7: EVIDENCIAS GRÁFICAS -->
  <h1>7. EVIDENCIAS GRÁFICAS DE IMPLEMENTACIÓN EN ENTORNO KDE X11</h1>
  <p>
    Capturas de pantalla tomadas con la utilidad nativa <strong>Spectacle</strong> sobre el servidor gráfico <strong>KDE X11 (`DISPLAY=:0`)</strong>, ejecutando las instrucciones en la terminal <strong>Konsole</strong> y visualizando la plataforma en <strong>Google Chrome</strong> (usuario <code>danilo</code>, clave <code>choco</code>), minimizando Visual Studio Code:
  </p>

  <div class="img-container">
    <img src="{cap1_path}" alt="Paso 1: Despliegue Docker en Konsole">
    <div class="caption">Figura 2: Paso 1 - Despliegue de los contenedores Docker en puerto 8101 verificado en Konsole.</div>
  </div>

  <div class="img-container">
    <img src="{cap2_path}" alt="Paso 2: Healthcheck y JSON en Konsole">
    <div class="caption">Figura 3: Paso 2 - Verificación de respuesta HTTP 200 y parsing del modelo Lean Canvas JSON en Konsole.</div>
  </div>

  <div class="img-container">
    <img src="{cap3_path}" alt="Paso 3: Portal Web Lean Canvas en Chrome">
    <div class="caption">Figura 4: Paso 3 - Visualización del Portal Web interactivo en Google Chrome mostrando la cuadrícula de 9 bloques.</div>
  </div>

  <div class="page-break"></div>

  <div class="img-container">
    <img src="{cap4_path}" alt="Paso 4: Bloques de Problema y Solución en Chrome">
    <div class="caption">Figura 5: Paso 4 - Inspección interactiva de los bloques de Problema, Solución y Propuesta de Valor en Google Chrome.</div>
  </div>

  <div class="img-container">
    <img src="{cap5_path}" alt="Paso 5: Las 4 Áreas Estratégicas en Chrome">
    <div class="caption">Figura 6: Paso 5 - Pestaña interactiva de las cuatro áreas estratégicas (Clientes, Oferta, Infraestructura y Viabilidad).</div>
  </div>

  <div class="img-container">
    <img src="{cap6_path}" alt="Paso 6: Simulador Financiero en Chrome">
    <div class="caption">Figura 7: Paso 6 - Simulador reactivo de costos, márgenes y punto de equilibrio en Google Chrome.</div>
  </div>

  <!-- SECCIÓN 8: CONCLUSIONES Y REFERENCIAS -->
  <h1>8. CONCLUSIONES Y VIABILIDAD DEL MODELO</h1>
  <div class="info-card">
    <ol>
      <li><strong>Apropiación Metodológica Ágil:</strong> El Lean Canvas demostró ser la herramienta idónea para sintetizar los aspectos críticos del negocio y contrastar las hipótesis antes de incurrir en costos operativos mayores.</li>
      <li><strong>Ventaja Competitiva Tecnológica:</strong> Contar con software full-stack propio programado por la aprendiz ADSO suprime las tarifas de intermediación, devolviendo el 30% del margen al negocio.</li>
      <li><strong>Solvencia Económica Demostrada:</strong> La necesidad de solo 10 pizzas diarias para alcanzar el punto de equilibrio confiere una gran resiliencia al emprendimiento.</li>
      <li><strong>Identidad y Pertinencia Caucana:</strong> La articulación de masa madre con productos de Silvia y la distinción UNESCO de Popayán crea un posicionamiento imposible de replicar por cadenas multinacionales.</li>
    </ol>
  </div>

  <h1>9. REFERENCIAS BIBLIOGRÁFICAS (NORMAS APA 7.ª EDICIÓN)</h1>
  <ul style="font-size: 7.7pt; line-height: 1.45;">
    <li>Aulet, B. (2017). <em>Disciplined Entrepreneurship: 24 Steps to a Successful Startup</em>. John Wiley & Sons, Inc., Hoboken, New Jersey.</li>
    <li>Maurya, A. (2012). <em>Running Lean: Iterate from Plan A to a Plan That Works</em>. O'Reilly Media.</li>
    <li>Osterwalder, A., & Pigneur, Y. (2010). <em>Business Model Generation: A Handbook for Visionaries, Game Changers, and Challengers</em>. John Wiley & Sons.</li>
    <li>Ries, E. (2011). <em>The Lean Startup: How Today's Entrepreneurs Use Continuous Innovation to Create Radically Successful Businesses</em>. Crown Business.</li>
    <li>Servicio Nacional de Aprendizaje (SENA). (2024). <em>Componente formativo: Entendiendo la empresa</em>. Dirección de Formación Profesional, Colombia.</li>
    <li>UNESCO. (2005). <em>Popayán, Ciudad Creativa de la Gastronomía</em>. Red de Ciudades Creativas de la UNESCO.</li>
  </ul>

</body>
</html>
"""

# Guardar HTML para conversión
html_path = os.path.join(DOCS_DIR, 'GA10-240201529-AA2-EV02_Modelo_Canvas_Emprendimiento.html')
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
print(f"[OK] HTML generado exitosamente en: {html_path}")

# Compilar PDF mediante Google Chrome Headless
pdf_path = os.path.join(DOCS_DIR, 'GA10-240201529-AA2-EV02_Modelo_Canvas_Emprendimiento.pdf')
chrome_cmd = [
    'google-chrome',
    '--headless',
    '--disable-gpu',
    '--no-sandbox',
    '--print-to-pdf-no-header',
    f'--print-to-pdf={pdf_path}',
    html_path
]
print("[INFO] Ejecutando compilación a PDF vía Google Chrome...")
subprocess.run(chrome_cmd, check=True)
print(f"[OK] PDF compilado ({os.path.getsize(pdf_path)/1024:.1f} KB): {pdf_path}")

# Compilar DOCX editable mediante LibreOffice soffice
print("[INFO] Generando versión editable DOCX vía LibreOffice soffice...")
soffice_cmd = [
    'soffice',
    '--headless',
    '--convert-to',
    'docx:MS Word 2007 XML',
    html_path,
    '--outdir',
    DOCS_DIR
]
subprocess.run(soffice_cmd, check=True)
docx_auto = os.path.join(DOCS_DIR, 'GA10-240201529-AA2-EV02_Modelo_Canvas_Emprendimiento.docx')
print(f"[OK] DOCX generado ({os.path.getsize(docx_auto)/1024:.1f} KB): {docx_auto}")

# Copiar a ENTREGA_DIR y ARTIFACT_DIR
dst_pdf = os.path.join(ENTREGA_DIR, 'GA10-240201529-AA2-EV02_Modelo_Canvas_Emprendimiento.pdf')
dst_docx = os.path.join(ENTREGA_DIR, 'GA10-240201529-AA2-EV02_Modelo_Canvas_Emprendimiento.docx')
shutil.copy2(pdf_path, dst_pdf)
shutil.copy2(docx_auto, dst_docx)

art_pdf = os.path.join(ARTIFACT_DIR, 'GA10-240201529-AA2-EV02_Modelo_Canvas_Emprendimiento.pdf')
art_docx = os.path.join(ARTIFACT_DIR, 'GA10-240201529-AA2-EV02_Modelo_Canvas_Emprendimiento.docx')
shutil.copy2(pdf_path, art_pdf)
shutil.copy2(docx_auto, art_docx)

# Copiar sitio_lean_canvas, diagramas y capturas a ENTREGA_DIR
for sub in ['sitio_lean_canvas', 'diagramas', 'capturas']:
    src_sub = os.path.join(BASE_DIR, sub)
    dst_sub = os.path.join(ENTREGA_DIR, sub)
    if os.path.exists(dst_sub):
        shutil.rmtree(dst_sub)
    shutil.copytree(src_sub, dst_sub)
    print(f"[OK] Carpeta {sub} copiada a entrega Zajuna")

# Copiar diagramas y capturas a ARTIFACT_DIR
shutil.copy2(diag_canvas, os.path.join(ARTIFACT_DIR, 'matriz_lean_canvas_pizzeria_bella_italia.png'))
for cap in os.listdir(CAPTURAS_DIR):
    if cap.endswith('.png'):
        shutil.copy2(os.path.join(CAPTURAS_DIR, cap), os.path.join(ARTIFACT_DIR, cap))
print(f"[OK] Diagramas y capturas copiados a artefactos: {ARTIFACT_DIR}")

# Generar archivo de enlaces institucional
repo_txt_path = os.path.join(ENTREGA_DIR, 'enlace_repositorio.txt')
with open(repo_txt_path, 'w', encoding='utf-8') as f:
    f.write("""ENLACE DEL REPOSITORIO GITHUB - EVIDENCIA GA10-240201529-AA2-EV02
Competencia: 240201529 - Gestionar procesos propios de la cultura emprendedora y empresarial de acuerdo con el perfil personal y los requerimientos de los contextos productivo y social
Actividad de Aprendizaje: GA10-240201529-AA2 - Definir la idea de negocio a desarrollar en el emprendimiento, según las oportunidades de mercado
Evidencia: GA10-240201529-AA2-EV02 - Modelo Canvas del emprendimiento
Resultado de Aprendizaje: 240201529-02 - Caracterizar la idea de negocio teniendo en cuenta las oportunidades y necesidades del sector productivo y social
Componente Formativo: "Entendiendo la empresa" / "Ser emprendedor"
Instrumento de Evaluación: Lista de Chequeo IE-GA10-240201529-AA2-EV02
Metodología: Lean Canvas (Ash Maurya) / Lean Startup (Eric Ries)
Aprendiz: Karen Yuliana Campo - Ficha 3186681
Centro de Teleinformática y Producción Industrial (CTPI Popayán) - Regional Cauca
Proyecto de Emprendimiento: Pizzería Gourmet Bella Italia Popayán

--------------------------------------------------------------------------------
1. ENLACE DEL REPOSITORIO GITHUB DEL PROYECTO:
https://github.com/kyulianacampogutierrez-ux/Evidencias

2. DIRECTORIO DE LA EVIDENCIA EN EL REPOSITORIO:
https://github.com/kyulianacampogutierrez-ux/Evidencias/tree/main/PET-053_GA10-240201529-AA2-EV02_Modelo_Canvas_Emprendimiento

3. DESPLIEGUE LOCAL EN CONTENEDOR DOCKER (PUERTO 8101):
- Portal Web Interactivo del Lean Canvas: http://localhost:8101/
- Especificación de Datos JSON: http://localhost:8101/modelo_lean_canvas.json
- Red Aislada de Contenedores: sena_lean_canvas_net (Zero Host Pollution)

4. ARCHIVOS ENTREGABLES OFICIALES EN EL PAQUETE:
- Documento Principal en PDF: GA10-240201529-AA2-EV02_Modelo_Canvas_Emprendimiento.pdf
- Documento Editable en Word: GA10-240201529-AA2-EV02_Modelo_Canvas_Emprendimiento.docx
- Diagrama Oficial Lean Canvas: matriz_lean_canvas_pizzeria_bella_italia.png / .svg
- Documento Técnico Completo en Markdown: MODELO_CANVAS_EMPRENDIMIENTO_PIZZERIA.md
- Carpeta de Capturas Reales (KDE X11 con Spectacle, Konsole y Chrome): capturas/ (6 imágenes PNG)
- Sitio Web Interactivo del Lean Canvas: sitio_lean_canvas/ (index.html, modelo_lean_canvas.json)
- Orquestación en Contenedores: docker_lean_canvas/docker-compose.yml
- Scripts de Automatización: scripts/ (capturar_pantallas_kde.sh, compile_pdf.py)
--------------------------------------------------------------------------------
""")
print(f"[OK] enlace_repositorio.txt generado en: {repo_txt_path}")

# Empacar ZIP de entrega institucional
zip_name = 'KARENCAMPO_AA2_EV02_GUIA10.zip'
zip_path = os.path.join(ENTREGA_DIR, zip_name)
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, BASE_DIR)
            z.write(full_path, arcname=os.path.join('PET-053_GA10-AA2-EV02', rel_path))
    z.write(repo_txt_path, arcname='enlace_repositorio.txt')
print(f"[OK] Paquete ZIP generado exitosamente ({os.path.getsize(zip_path)/1024:.1f} KB): {zip_path}")
print("=== COMPILACIÓN FINALIZADA CON ÉXITO ===")
