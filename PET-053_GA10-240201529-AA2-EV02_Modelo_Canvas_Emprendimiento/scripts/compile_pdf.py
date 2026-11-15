#!/usr/bin/env python3
# ==============================================================================
# COMPILADOR DE MODELO CANVAS Y EMPACADOR DE EVIDENCIA GA10-240201529-AA2-EV02
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
  <title>Modelo Canvas - GA10-240201529-AA2-EV02 | Karen Campo</title>
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
    <div class="header-title">MODELO CANVAS DEL EMPRENDIMIENTO</div>
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
    <div class="meta-item"><strong>Instrumento de Evaluación:</strong> Lista de Chequeo IE-GA10-240201529-AA2-EV02</div>
    <div class="meta-item"><strong>Aprendiz:</strong> Karen Yuliana Campo</div>
    <div class="meta-item"><strong>Instructor Técnico:</strong> Danilo</div>
    <div class="meta-item"><strong>Centro y Regional:</strong> CTPI Popayán - Regional Cauca (Noviembre 2026)</div>
  </div>

  <!-- SECCIÓN 1: INTRODUCCIÓN Y MARCO TEÓRICO -->
  <h1>1. INTRODUCCIÓN Y MARCO TEÓRICO DEL MODELO CANVAS</h1>
  <p>
    El diseño de un modelo de negocio innovador es fundamental para estructurar emprendimientos tecnológicos y de producción industrial. Conforme a las orientaciones curriculares de la <strong>Guía de Aprendizaje 10 (Actividad 3.2.2)</strong>, el <strong>Modelo Canvas</strong>, creado por Alexander Osterwalder e Yves Pigneur (2010), permite a los emprendedores visualizar y validar de forma estructurada cómo una empresa crea, entrega y captura valor.
  </p>
  <p>
    El modelo sintetiza la lógica del negocio en <strong>cuatro (4) áreas estratégicas</strong> directivas: <strong>Infraestructura</strong>, <strong>Oferta</strong>, <strong>Clientes</strong> y <strong>Viabilidad Económica</strong>, las cuales se desagregan en <strong>nueve (9) bloques constructivos</strong> interconectados. El presente informe formaliza el Modelo Canvas desarrollado para el proyecto productivo <strong>Pizzería Gourmet Bella Italia Popayán</strong>, liderado por la aprendiz <strong>Karen Yuliana Campo</strong>.
  </p>

  <!-- SECCIÓN 2: CARACTERIZACIÓN DEL EMPRENDIMIENTO -->
  <h1>2. CONTEXTO Y CARACTERIZACIÓN DE LA IDEA DE NEGOCIO</h1>
  <p>
    <strong>Pizzería Gourmet Bella Italia Popayán</strong> es un modelo gastronómico de alta gama que fusiona la técnica milenaria napolitana de cocción en horno de leña a 400°C con ingredientes identitarios del departamento del Cauca (pipián payanés y quesos campesinos de Silvia). Todo esto se apalanca en una plataforma de software propia de comercio electrónico, comanda digital de cocina KDS y facturación electrónica DIAN desarrollada durante la formación en ADSO.
  </p>
  <div class="info-card">
    <strong>Oportunidad de Mercado en Popayán:</strong> Capitalizar el reconocimiento de Popayán como <em>Ciudad Creativa de la Gastronomía UNESCO</em>, satisfaciendo la demanda de consumidores que exigen alimentos saludables, digestivos (48h de fermentación en masa madre viva) y pedidos directos en línea sin comisiones abusivas de plataformas de intermediación de delivery.
  </div>

  <!-- SECCIÓN 3: LAS 4 ÁREAS ESTRATÉGICAS -->
  <h1>3. ANÁLISIS DE LAS CUATRO (4) ÁREAS ESTRATÉGICAS</h1>
  <table>
    <thead>
      <tr>
        <th style="width:25%;">Área Estratégica</th>
        <th style="width:35%;">Bloques Constructivos</th>
        <th style="width:40%;">Estrategia Bella Italia Popayán</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. Infraestructura</strong></td>
        <td>Socios clave, Actividades clave, Recursos clave</td>
        <td>Alianza directa con campesinos de Silvia, horno de leña a 400°C y plataforma de software contenerizada en Docker (ADSO).</td>
      </tr>
      <tr>
        <td><strong>2. Oferta</strong></td>
        <td>Propuesta de valor</td>
        <td>Pizzas de autor napolitanas fermentadas 48 horas con masa madre viva, combinadas con pipián payanés y quesos madurados.</td>
      </tr>
      <tr>
        <td><strong>3. Clientes</strong></td>
        <td>Relaciones con clientes, Canales, Segmentos de clientes</td>
        <td>Venta directa vía portal web propio (localhost:8101) y salón boutique, club de fidelización y enfoque en familias y turistas UNESCO.</td>
      </tr>
      <tr>
        <td><strong>4. Viabilidad Económica</strong></td>
        <td>Estructura de costos, Fuentes de ingresos</td>
        <td>Costos fijos de $8.000.000 COP, margen de contribución del 67.9% y punto de equilibrio en 310 pizzas/mes (10.3 al día).</td>
      </tr>
    </tbody>
  </table>

  <!-- SECCIÓN 4: LOS 9 BLOQUES DEL MODELO CANVAS -->
  <h1>4. DESARROLLO DETALLADO DE LOS NUEVE (9) BLOQUES DEL MODELO CANVAS</h1>

  <h2>4.1 Bloque 1: Socios Clave (Infraestructura)</h2>
  <ul>
    <li><strong>Asociación Campesina de Silvia (Cauca):</strong> Suministro directo de quesos madurados artesanales y lácteos frescos.</li>
    <li><strong>Productores de Pipián de Popayán:</strong> Proveeduría de maní tostado, achiote ancestral y papa criolla para el pipián.</li>
    <li><strong>Molino Harinero Certificado:</strong> Harina de fuerza tipo 00 (W 300+) para fermentación prolongada de 48 horas.</li>
    <li><strong>SENA CTPI & Fondo Emprender:</strong> Mentoría técnica, validación de modelo y apalancamiento en capital semilla.</li>
    <li><strong>Pasarela de Pagos Wompi / Redebanc:</strong> Transacciones seguras con QR Bancolombia, PSE y tarjetas sin fricción.</li>
    <li><strong>Corporación Gastronómica de Popayán (UNESCO):</strong> Integración con circuitos turísticos y festivales culturales.</li>
  </ul>

  <h2>4.2 Bloque 2: Actividades Clave (Infraestructura)</h2>
  <ul>
    <li>Amasado artesanal y fermentación biológica lenta de 48 horas en frío.</li>
    <li>Cocción napolitana en horno de leña de roble a 400°C en tan solo 90 segundos.</li>
    <li>Elaboración diaria de pipián patrimonial caucano y porcionado de quesos madurados.</li>
    <li>Mantenimiento y soporte continuo de la plataforma web, KDS y API de facturación DIAN.</li>
    <li>Despacho logístico térmico propio en mochilas herméticas a 70°C en menos de 35 minutos.</li>
    <li>Control higiénico-sanitario y trazabilidad de insumos bajo estándares de BPM.</li>
  </ul>

  <h2>4.3 Bloque 3: Recursos Clave (Infraestructura)</h2>
  <ul>
    <li><strong>Físicos:</strong> Local comercial en el Centro Histórico de Popayán, horno de leña abovedado, amasadora espiral y mesas de granito.</li>
    <li><strong>Intelectuales:</strong> Cepa de masa madre viva de 5 años, fórmulas exclusivas registradas (Pizza Pipián, Pizza Silvia).</li>
    <li><strong>Tecnológicos:</strong> Ecosistema web y KDS en microservicios Docker (Karen Campo - ADSO), API facturación electrónica DIAN.</li>
    <li><strong>Humanos:</strong> Maestro pizzero certificado (*Pizzaiolo*), ayudantes de cocina, despachador propio y líder ADSO.</li>
    <li><strong>Financieros:</strong> Capital de trabajo propio y crédito semilla institucional.</li>
  </ul>

  <h2>4.4 Bloque 4: Propuesta de Valor (Oferta)</h2>
  <div class="info-card">
    <strong>Lema Principal:</strong> <em>"El auténtico arte pizzero napolitano con el alma y sabor de la gastronomía caucana."</em><br>
    Pizzas artesanales altamente digestivas con 48h de fermentación natural en horno de leña a 400°C, fusionadas con pipián payanés y quesos campesinos de Silvia, comercializadas por canal web propio sin sobrecostos de intermediarios y con facturación electrónica legal DIAN en 2 segundos.
  </div>

  <h2>4.5 Bloque 5: Relaciones con Clientes (Clientes)</h2>
  <ul>
    <li><strong>Atención Experiencial en Salón:</strong> Servicio cálido y observación en vivo del horno de leña encendido.</li>
    <li><strong>Autoservicio Digital Intuitivo:</strong> Catálogo web interactivo con fotos HD, alérgenos y confirmación por WhatsApp.</li>
    <li><strong>Club "Bella Italia Club":</strong> Acumulación de puntos, degustaciones de recetas de autor y cortesía de cumpleaños.</li>
    <li><strong>Atención Posventa y Escucha Activa:</strong> Encuestas de satisfacción NPS y garantía de reposición inmediata.</li>
  </ul>

  <h2>4.6 Bloque 6: Canales (Clientes)</h2>
  <ul>
    <li>Portal Web Oficial responsivo e-commerce (<code>http://localhost:8101/</code>).</li>
    <li>Restaurante boutique con salón en el Centro Histórico de Popayán.</li>
    <li>Flota propia de domicilios con empaque térmico ecológico a 70°C y datáfono móvil.</li>
    <li>Redes sociales (Instagram, TikTok) con storytelling de la cocina artesanal y origen campesino.</li>
    <li>Canal B2B institucional para catering corporativo en oficinas y entidades bancarias.</li>
  </ul>

  <h2>4.7 Bloque 7: Segmentos de Clientes (Clientes)</h2>
  <ul>
    <li>Familias y comensales urbanos de estratos 3, 4 y 5 que buscan cenas saludables y de calidad.</li>
    <li>Jóvenes profesionales, docentes y médicos que valoran la rapidez de entrega y pedidos web.</li>
    <li>Turistas atraídos por la designación de Popayán como Ciudad Creativa UNESCO.</li>
    <li><em>Early Adopters:</em> Foodies aficionados a la masa madre artesanal y compradores nativos digitales.</li>
    <li>Empresas e instituciones del centro que requieren pedidos ejecutivos con factura legal DIAN.</li>
  </ul>

  <h2>4.8 Bloque 8: Estructura de Costos (Viabilidad Económica)</h2>
  <ul>
    <li><strong>Costos Fijos Mensuales ($8.000.000 COP):</strong> Arriendo local Centro ($2.500.000), Nómina 3 personas ($4.200.000), Servicios e internet fibra ($800.000), Hosting Docker y DIAN ($500.000).</li>
    <li><strong>Costos Variables Unitarios (~$12.200 COP):</strong> Materia prima (~$10.000 COP / 26.3%), empaque térmico biodegradable ($1.800 COP), comisión pasarela Wompi ($400 COP).</li>
    <li><strong>Suministro Operativo:</strong> Leña de roble certificada ($400.000 COP/mes) y pauta publicitaria ($300.000 COP/mes).</li>
  </ul>

  <h2>4.9 Bloque 9: Fuentes de Ingresos (Viabilidad Económica)</h2>
  <ul>
    <li>Pizzas Tradicionales Napolitanas: $32.000 a $38.000 COP por unidad.</li>
    <li>Pizzas Gourmet de Autor Caucanas: $42.000 a $48.000 COP por unidad.</li>
    <li>Focaccias, Calzones y Repostería Artesanal: $8.000 a $16.000 COP por unidad.</li>
    <li>Bebidas Artesanales & Café Especial de Silvia: $5.000 a $9.000 COP por unidad.</li>
    <li>Catering Empresarial: Paquetes corporativos desde $25.000 a $35.000 COP por persona.</li>
    <li>Medios de Pago: Efectivo, datáfono inalámbrico, transferencias QR Bancolombia/Nequi y Wompi/PSE.</li>
  </ul>

  <!-- SECCIÓN 5: MATRIZ GRÁFICA DEL MODELO CANVAS -->
  <h1>5. MATRIZ MODELO CANVAS GRÁFICA OFICIAL</h1>
  <div class="img-container">
    <img src="{diag_canvas}" alt="Matriz Modelo Canvas de la Pizzería">
    <div class="caption">Figura 1: Matriz Modelo Canvas Oficial de 9 Bloques según metodología de Alexander Osterwalder - Pizzería Gourmet Bella Italia Popayán.</div>
  </div>

  <!-- SECCIÓN 6: SIMULACIÓN FINANCIERA -->
  <h1>6. SIMULACIÓN FINANCIERA Y PUNTO DE EQUILIBRIO</h1>
  <p>
    El punto de equilibrio se determinó mediante la relación matemática entre los costos fijos mensuales y el margen de contribución unitario:
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
        <td>Materia prima directa (26.3%) + empaque + pasarela.</td>
      </tr>
      <tr>
        <td>Margen de Contribución (MC)</td>
        <td>$25.800 COP (67.9%)</td>
        <td>Recurso neto por pizza para absorber costos fijos.</td>
      </tr>
      <tr>
        <td>Costos Fijos Mensuales (CF)</td>
        <td>$8.000.000 COP</td>
        <td>Nómina base, arriendo local Centro, servicios y hosting.</td>
      </tr>
      <tr style="background:#ecfdf5; font-weight:bold;">
        <td>PUNTO DE EQUILIBRIO MENSUAL</td>
        <td>310 pizzas / mes</td>
        <td>Solo 10.3 pizzas al día para cubrir la totalidad de costos.</td>
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
    <div class="caption">Paso 1: Despliegue y verificación de salud de contenedores Docker en Konsole (puerto 8101).</div>
  </div>

  <div class="img-container">
    <img src="{cap2_path}" alt="Paso 2: Verificación de Salud en Konsole">
    <div class="caption">Paso 2: Verificación de endpoint HTTP 200 y validación de bloques en archivo JSON de datos.</div>
  </div>

  <div class="img-container">
    <img src="{cap3_path}" alt="Paso 3: Matriz Gráfica Modelo Canvas en Chrome">
    <div class="caption">Paso 3: Navegación en Google Chrome visualizando la Matriz Modelo Canvas Oficial en el portal web.</div>
  </div>

  <div class="page-break"></div>

  <div class="img-container">
    <img src="{cap4_path}" alt="Paso 4: Cuadrícula de 9 Bloques en Chrome">
    <div class="caption">Paso 4: Cuadrícula interactiva de 9 bloques del Modelo Canvas en el portal web (localhost:8101).</div>
  </div>

  <div class="img-container">
    <img src="{cap5_path}" alt="Paso 5: Las 4 Áreas Estratégicas en Chrome">
    <div class="caption">Paso 5: Detalle de las 4 Áreas Estratégicas (Infraestructura, Oferta, Clientes y Viabilidad Económica).</div>
  </div>

  <div class="img-container">
    <img src="{cap6_path}" alt="Paso 6: Simulador Financiero en Chrome">
    <div class="caption">Paso 6: Simulador reactivo de punto de equilibrio y utilidad neta en Google Chrome.</div>
  </div>

  <!-- SECCIÓN 8: CONCLUSIONES -->
  <h1>8. CONCLUSIONES Y FACTIBILIDAD</h1>
  <ul>
    <li><strong>Alineación con la Metodología Canvas:</strong> La matriz de 9 bloques permitió estructurar de forma integral y coherente todos los factores críticos del negocio, cumpliendo a cabalidad con la Guía 10 del SENA.</li>
    <li><strong>Sinergia Tecnológica ADSO:</strong> El desarrollo del software propio elimina intermediarios comerciales, optimiza el flujo en cocina mediante KDS y automatiza la facturación legal DIAN.</li>
    <li><strong>Factibilidad Financiera Comprobada:</strong> Con un margen bruto del 67.9% y un punto de equilibrio de solo 10.3 pizzas al día, el modelo presenta un excelente blindaje financiero ante riesgos de mercado.</li>
    <li><strong>Impacto Social y Regional:</strong> Se articula la economía campesina del municipio de Silvia con la identidad cultural de Popayán, promoviendo el desarrollo productivo del Cauca.</li>
  </ul>

  <!-- SECCIÓN 9: REFERENCIAS -->
  <h1>9. REFERENCIAS BIBLIOGRÁFICAS (NORMAS APA 7.ª EDICIÓN)</h1>
  <ul>
    <li>Aulet, B. (2017). <em>Disciplined Entrepreneurship: 24 Steps to a Successful Startup</em>. John Wiley & Sons, Inc., Hoboken, New Jersey.</li>
    <li>Maurya, A. (2012). <em>Running Lean: Iterate from Plan A to a Plan That Works</em>. O'Reilly Media.</li>
    <li>Osterwalder, A., & Pigneur, Y. (2010). <em>Business Model Generation: A Handbook for Visionaries, Game Changers, and Challengers</em>. John Wiley & Sons.</li>
    <li>Ries, E. (2011). <em>The Lean Startup: How Today's Entrepreneurs Use Continuous Innovation to Create Radically Successful Businesses</em>. Crown Business.</li>
    <li>Servicio Nacional de Aprendizaje (SENA). (2024). <em>Componente formativo: Entendiendo la empresa</em>. Dirección de Formación Profesional, Sistema Nacional de Formación para el Trabajo, Colombia.</li>
    <li>UNESCO. (2005). <em>Popayán, Ciudad Creativa de la Gastronomía</em>. Red de Ciudades Creativas de la UNESCO.</li>
  </ul>

</body>
</html>
"""

html_path = os.path.join(DOCS_DIR, 'GA10-240201529-AA2-EV02_Modelo_Canvas_Emprendimiento.html')
pdf_path = os.path.join(DOCS_DIR, 'GA10-240201529-AA2-EV02_Modelo_Canvas_Emprendimiento.pdf')
docx_path = os.path.join(DOCS_DIR, 'GA10-240201529-AA2-EV02_Modelo_Canvas_Emprendimiento.docx')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"[OK] Archivo HTML maestro generado en: {html_path}")

# Compilación a PDF con Google Chrome Headless
chrome_cmd = [
    'google-chrome',
    '--headless',
    '--disable-gpu',
    '--run-all-compositor-stages-before-draw',
    '--print-to-pdf-no-header',
    f'--print-to-pdf={pdf_path}',
    f'file://{html_path}'
]

print("[INFO] Compilando documento oficial en PDF con Google Chrome...")
subprocess.run(chrome_cmd, check=True)
print(f"[OK] PDF oficial compilado con éxito: {pdf_path} ({os.path.getsize(pdf_path)} bytes)")

# Generar versión editable DOCX con LibreOffice Writer
print("[INFO] Generando versión editable DOCX con LibreOffice...")
docx_cmd = [
    'soffice',
    '--headless',
    '--convert-to',
    'docx:MS Word 2007 XML',
    html_path,
    '--outdir',
    DOCS_DIR
]
subprocess.run(docx_cmd, check=True)
print(f"[OK] DOCX generado con éxito: {docx_path} ({os.path.getsize(docx_path)} bytes)")

# Copiar a carpeta de entrega Zajuna y artefactos del Brain
print("[INFO] Distribuyendo entregables a carpeta ENTREGA_ZAJUNA y Brain...")
shutil.copyfile(pdf_path, os.path.join(ENTREGA_DIR, 'GA10-240201529-AA2-EV02_Modelo_Canvas_Emprendimiento.pdf'))
shutil.copyfile(docx_path, os.path.join(ENTREGA_DIR, 'GA10-240201529-AA2-EV02_Modelo_Canvas_Emprendimiento.docx'))
shutil.copyfile(pdf_path, os.path.join(ARTIFACT_DIR, 'GA10-240201529-AA2-EV02_Modelo_Canvas_Emprendimiento.pdf'))
shutil.copyfile(docx_path, os.path.join(ARTIFACT_DIR, 'GA10-240201529-AA2-EV02_Modelo_Canvas_Emprendimiento.docx'))

# Empaquetar ZIP Institucional
zip_path = os.path.join(ENTREGA_DIR, 'KARENCAMPO_AA2_EV02_GUIA10.zip')
print(f"[INFO] Creando paquete ZIP institucional en: {zip_path}...")
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(ENTREGA_DIR):
        for file in files:
            if file == 'KARENCAMPO_AA2_EV02_GUIA10.zip':
                continue
            abs_f = os.path.join(root, file)
            rel_f = os.path.relpath(abs_f, ENTREGA_DIR)
            zipf.write(abs_f, rel_f)

print(f"[OK] Paquete ZIP generado con éxito ({os.path.getsize(zip_path)} bytes)")
print("=== COMPILACIÓN FINALIZADA SATISFACTORIAMENTE ===")
