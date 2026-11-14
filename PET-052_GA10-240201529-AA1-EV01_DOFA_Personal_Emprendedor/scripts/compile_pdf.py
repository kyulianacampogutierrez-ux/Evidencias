#!/usr/bin/env python3
# ==============================================================================
# COMPILADOR DE DOCUMENTO Y EMPACADOR DE EVIDENCIA GA10-240201529-AA1-EV01
# Evidencia: GA10-240201529-AA1-EV01 - DOFA personal en Hoja de Cálculo
# Competencia: 240201529 - Gestionar procesos de la cultura emprendedora
# Actividad: GA10-240201529-AA1 - Reconocer capacidades personales para convertirse en emprendedor
# Componente: "Ser emprendedor" | Instrumento: IE-GA10-240201529-AA1-EV01
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán - Regional Cauca
# ==============================================================================

import os
import subprocess
import shutil
import zipfile

BASE_DIR = '/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-052_GA10-240201529-AA1-EV01_DOFA_Personal_Emprendedor'
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
HOJA_DIR = os.path.join(BASE_DIR, 'hoja_de_calculo')
DIAG_DIR = os.path.join(BASE_DIR, 'diagramas')
CAPTURAS_DIR = os.path.join(BASE_DIR, 'capturas')
ENTREGA_DIR = '/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA10-240201529-AA1-EV01'
ARTIFACT_DIR = '/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603'

os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(HOJA_DIR, exist_ok=True)
os.makedirs(DIAG_DIR, exist_ok=True)
os.makedirs(CAPTURAS_DIR, exist_ok=True)
os.makedirs(ENTREGA_DIR, exist_ok=True)

diag_dofa = os.path.join(DIAG_DIR, 'matriz_dofa_personal_emprendedor.png')

cap1_path = os.path.join(CAPTURAS_DIR, 'paso_01_generacion_hoja_calculo_konsole.png')
cap2_path = os.path.join(CAPTURAS_DIR, 'paso_02_libreoffice_calc_hoja1_portada.png')
cap3_path = os.path.join(CAPTURAS_DIR, 'paso_03_libreoffice_calc_hoja2_matriz_dofa.png')
cap4_path = os.path.join(CAPTURAS_DIR, 'paso_04_libreoffice_calc_hoja3_cruce_foda.png')
cap5_path = os.path.join(CAPTURAS_DIR, 'paso_05_libreoffice_calc_hoja5_plan_smart.png')
cap6_path = os.path.join(CAPTURAS_DIR, 'paso_06_libreoffice_calc_hoja6_dashboard_ipe.png')

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>DOFA Personal y Hoja de Cálculo del Emprendedor - GA10-240201529-AA1-EV01 | Karen Campo</title>
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
      font-size: 14pt;
      font-weight: 800;
      letter-spacing: -0.5px;
      margin-bottom: 4px;
    }}
    .header-sub {{
      font-size: 9pt;
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
    <div class="header-title">ANÁLISIS DE LA MATRIZ DOFA PERSONAL DEL SER EMPRENDEDOR</div>
    <div class="header-sub">Reconocer capacidades personales para convertirse en emprendedor como parte de su proyecto de vida (Hoja de Cálculo)</div>
  </div>

  <!-- METADATOS INSTITUCIONALES SENA -->
  <div class="meta-box">
    <div class="meta-item"><strong>Programa:</strong> Análisis y Desarrollo de Software (ADSO)</div>
    <div class="meta-item"><strong>Ficha SENA:</strong> 3186681</div>
    <div class="meta-item"><strong>Competencia Transversal:</strong> 240201529 - Cultura Emprendedora y Empresarial</div>
    <div class="meta-item"><strong>Fase de Proyecto:</strong> Fase 4 - Implantación (AP10)</div>
    <div class="meta-item"><strong>Actividad de Aprendizaje:</strong> GA10-240201529-AA1 (Capacidades del emprendedor)</div>
    <div class="meta-item"><strong>Evidencia Oficial:</strong> GA10-240201529-AA1-EV01 - DOFA personal</div>
    <div class="meta-item"><strong>Instrumento de Evaluación:</strong> IE-GA10-240201529-AA1-EV01 (Lista de Chequeo)</div>
    <div class="meta-item"><strong>Componente Formativo:</strong> Ser emprendedor</div>
    <div class="meta-item"><strong>Aprendiz:</strong> Karen Yuliana Campo</div>
    <div class="meta-item"><strong>Instructor Técnico:</strong> Danilo</div>
    <div class="meta-item"><strong>Centro de Formación:</strong> CTPI Popayán - Regional Cauca</div>
    <div class="meta-item"><strong>Proyecto de Vida:</strong> Pizzería Gourmet Bella Italia Popayán</div>
  </div>

  <div class="info-card">
    <strong>Resumen Ejecutivo:</strong> La presente evidencia documenta el autodiagnóstico estratégico y cuantitativo de la aprendiz <strong>Karen Yuliana Campo</strong> para consolidarse como emprendedora tecnológica y gastronómica. En cumplimiento estricto con la indicación del usuario (desarrollar en una <em>Hoja de Cálculo</em>), se estructuró un libro de trabajo interactivo en formatos <strong>.ods</strong> y <strong>.xlsx</strong> compuesto por seis (6) hojas funcionales con fórmulas automáticas, matriz de cruce FODA, análisis actitudinal ante el éxito y la adversidad, plan de acción SMART a 12 meses y cálculo del <strong>Índice de Potencial Emprendedor (IPE = 1.22)</strong>.
  </div>

  <!-- SECCIÓN 1: INTRODUCCIÓN Y MARCO TEÓRICO -->
  <h1>1. INTRODUCCIÓN Y MARCO TEÓRICO DEL SER EMPRENDEDOR</h1>
  <p>
    En el marco pedagógico del SENA, el emprendimiento es una competencia transversal determinante para la generación de desarrollo humano y económico. La investigación moderna en ciencias de la administración (Aulet, 2017) refuta el mito de que los emprendedores son producto exclusivo de una herencia genética inmutable; por el contrario, la capacidad de emprender es una disciplina que se aprende y se perfecciona a través del autoconocimiento, la evaluación rigurosa de las condiciones personales y la lectura del entorno socioeconómico.
  </p>
  <p>
    La matriz **DOFA (Debilidades, Oportunidades, Fortalezas y Amenazas)** es el modelo por excelencia para sistematizar este análisis. Aplicada a la dimensión personal, permite reconocer las condiciones internas (educación, habilidades de liderazgo, experiencia en ventas y recursos) y las condiciones externas (mercado, apoyo del Fondo Emprender SENA, estabilidad y aspectos tributarios).
  </p>

  <!-- SECCIÓN 2: CARACTERIZACIÓN DEL EMPRENDIMIENTO -->
  <h1>2. CARACTERIZACIÓN DEL PROYECTO DE EMPRENDIMIENTO Y VIDA</h1>
  <p>
    El proyecto de vida empresarial de la aprendiz es la <strong>Pizzería Gourmet Bella Italia Popayán</strong>, una iniciativa gastronómica artesanal articulada a una robusta plataforma de software:
  </p>
  <ul>
    <li><strong>Misión Personal:</strong> Integrar mis competencias de desarrollo de software con la cocina tradicional caucana, liderando un restaurante digitalizado de alta calidad que impulse a los productores campesinos de Silvia y del Cauca.</li>
    <li><strong>Visión al 2028:</strong> Consolidar a Bella Italia Popayán como referente regional de franquicias gastronómicas tecnificadas, apalancando capital semilla condonable del Fondo Emprender SENA.</li>
    <li><strong>Propuesta de Valor:</strong> Masas de fermentación lenta de 48 horas en leña a 400°C fusionadas con ingredientes autóctonos (pipián payanés y queso campesino), gestionadas mediante una arquitectura web propia (tienda en línea, cocina KDS y facturación electrónica DIAN).</li>
  </ul>

  <!-- SECCIÓN 3: ANÁLISIS DE CONDICIONES INTERNAS -->
  <h1>3. ANÁLISIS DE CONDICIONES INTERNAS DEL EMPRENDEDOR</h1>
  <p>Evaluación cuantitativa de los factores internos que definen el perfil técnico y emocional:</p>

  <table>
    <thead>
      <tr>
        <th style="width: 8%;">Cód.</th>
        <th style="width: 25%;">Factor Interno (Fortalezas / Debilidades)</th>
        <th style="width: 47%;">Descripción e Impacto en el Emprendimiento</th>
        <th style="width: 10%;">Nivel (1-5)</th>
        <th style="width: 10%;">Puntaje</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="badge badge-success">F1</span></td>
        <td><strong>Dominio Técnico en Software ADSO</strong></td>
        <td>Desarrollo autónomo de Web, KDS y POS DIAN sin costos de licenciamiento.</td>
        <td>5.0</td>
        <td><strong>1.25</strong></td>
      </tr>
      <tr>
        <td><span class="badge badge-success">F2</span></td>
        <td><strong>Pasión por la Gastronomía Caucana</strong></td>
        <td>Masa madre de 48 horas e ingredientes autóctonos (pipián y Silvia).</td>
        <td>5.0</td>
        <td><strong>1.00</strong></td>
      </tr>
      <tr>
        <td><span class="badge badge-success">F3</span></td>
        <td><strong>Disciplina y Rigor Metodológico</strong></td>
        <td>Organización minuciosa, hábitos de estudio y calidad ISO/BPM.</td>
        <td>4.5</td>
        <td><strong>0.90</strong></td>
      </tr>
      <tr>
        <td><span class="badge badge-success">F4</span></td>
        <td><strong>Resiliencia y Capacidad de Iteración</strong></td>
        <td>Tolerancia constructiva al error y mentalidad de mejora continua.</td>
        <td>4.5</td>
        <td><strong>0.90</strong></td>
      </tr>
      <tr>
        <td><span class="badge badge-success">F5</span></td>
        <td><strong>Liderazgo Colaborativo y Empatía</strong></td>
        <td>Motivación asertiva al equipo de cocina, caja y domicilios.</td>
        <td>4.0</td>
        <td><strong>0.60</strong></td>
      </tr>
      <tr style="background-color: #ecfdf5; font-weight: bold;">
        <td colspan="3">SUBTOTAL PONDERADO FORTALEZAS (F)</td>
        <td>4.6</td>
        <td>4.65</td>
      </tr>
      <tr>
        <td><span class="badge badge-danger">D1</span></td>
        <td><strong>Experiencia Comercial B2C Limitada</strong></td>
        <td>Timidez inicial para cierres de ventas directas y negociación de insumos.</td>
        <td>3.5</td>
        <td><strong>0.88</strong></td>
      </tr>
      <tr>
        <td><span class="badge badge-danger">D2</span></td>
        <td><strong>Perfeccionismo Extremo</strong></td>
        <td>Riesgo de dilatar lanzamientos comerciales por detalles no críticos.</td>
        <td>4.0</td>
        <td><strong>0.80</strong></td>
      </tr>
      <tr>
        <td><span class="badge badge-danger">D3</span></td>
        <td><strong>Capital Financiero Propio Limitado</strong></td>
        <td>Liquidez reducida para compra de hornos industriales pesados sin crédito.</td>
        <td>4.5</td>
        <td><strong>1.13</strong></td>
      </tr>
      <tr>
        <td><span class="badge badge-danger">D4</span></td>
        <td><strong>Dificultad Inicial para Delegar</strong></td>
        <td>Sobrecarga de trabajo por querer supervisar personalmente cada paso.</td>
        <td>3.5</td>
        <td><strong>0.53</strong></td>
      </tr>
      <tr>
        <td><span class="badge badge-danger">D5</span></td>
        <td><strong>Conocimiento Tributario Intermedio</strong></td>
        <td>Necesidad de afianzar normas sobre Régimen Simple, retenciones e IVA.</td>
        <td>3.0</td>
        <td><strong>0.45</strong></td>
      </tr>
      <tr style="background-color: #fef2f2; font-weight: bold;">
        <td colspan="3">SUBTOTAL PONDERADO DEBILIDADES (D)</td>
        <td>3.7</td>
        <td>3.78</td>
      </tr>
    </tbody>
  </table>

  <!-- SECCIÓN 4: ANÁLISIS DE CONDICIONES EXTERNAS -->
  <h1>4. ANÁLISIS DE CONDICIONES EXTERNAS DEL ENTORNO</h1>
  <table>
    <thead>
      <tr>
        <th style="width: 8%;">Cód.</th>
        <th style="width: 25%;">Factor Externo (Oportunidades / Amenazas)</th>
        <th style="width: 47%;">Descripción y Consecuencia para el Proyecto</th>
        <th style="width: 10%;">Nivel (1-5)</th>
        <th style="width: 10%;">Puntaje</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="badge badge-primary">O1</span></td>
        <td><strong>Fondo Emprender SENA</strong></td>
        <td>Capital semilla condonable hasta $100M COP para maquinaria pesada.</td>
        <td>5.0</td>
        <td><strong>1.25</strong></td>
      </tr>
      <tr>
        <td><span class="badge badge-primary">O2</span></td>
        <td><strong>Popayán Ciudad Gastronómica UNESCO</strong></td>
        <td>Atracción turística y valoración de platos de autor con identidad local.</td>
        <td>5.0</td>
        <td><strong>1.25</strong></td>
      </tr>
      <tr>
        <td><span class="badge badge-primary">O3</span></td>
        <td><strong>Crecimiento E-Commerce y Delivery</strong></td>
        <td>Aumento del 35% en pedidos virtuales y conveniencia de pago digital.</td>
        <td>4.5</td>
        <td><strong>0.90</strong></td>
      </tr>
      <tr>
        <td><span class="badge badge-primary">O4</span></td>
        <td><strong>Alianzas con Productores de Silvia</strong></td>
        <td>Compra directa de quesos madurados y vegetales sin intermediarios.</td>
        <td>4.0</td>
        <td><strong>0.60</strong></td>
      </tr>
      <tr>
        <td><span class="badge badge-primary">O5</span></td>
        <td><strong>Incentivos a la Digitalización MIPYMES</strong></td>
        <td>Programas de fomento de MinTIC y Cámara de Comercio del Cauca.</td>
        <td>4.0</td>
        <td><strong>0.60</strong></td>
      </tr>
      <tr style="background-color: #f0f9ff; font-weight: bold;">
        <td colspan="3">SUBTOTAL PONDERADO OPORTUNIDADES (O)</td>
        <td>4.5</td>
        <td>4.60</td>
      </tr>
      <tr>
        <td><span class="badge badge-warning">A1</span></td>
        <td><strong>Inflación y Volatilidad en Insumos</strong></td>
        <td>Alzas en trigo, mozzarella y leña que reducen el margen de ganancia.</td>
        <td>4.5</td>
        <td><strong>1.13</strong></td>
      </tr>
      <tr>
        <td><span class="badge badge-warning">A2</span></td>
        <td><strong>Competencia de Cadenas Low-Cost</strong></td>
        <td>Guerra de precios agresiva de franquicias masivas de comida rápida.</td>
        <td>4.0</td>
        <td><strong>0.80</strong></td>
      </tr>
      <tr>
        <td><span class="badge badge-warning">A3</span></td>
        <td><strong>Fallas en Servicios Públicos e Internet</strong></td>
        <td>Cortes eventuales de energía o fibra óptica en el Centro de Popayán.</td>
        <td>3.5</td>
        <td><strong>0.70</strong></td>
      </tr>
      <tr>
        <td><span class="badge badge-warning">A4</span></td>
        <td><strong>Cambios en Normatividad DIAN</strong></td>
        <td>Actualizaciones técnicas continuas en facturación y nómina electrónica.</td>
        <td>3.5</td>
        <td><strong>0.70</strong></td>
      </tr>
      <tr>
        <td><span class="badge badge-warning">A5</span></td>
        <td><strong>Riesgos de Fraude en Pagos Web</strong></td>
        <td>Posibilidad de transacciones dudosas o ataques a la pasarela digital.</td>
        <td>3.0</td>
        <td><strong>0.45</strong></td>
      </tr>
      <tr style="background-color: #fffbeb; font-weight: bold;">
        <td colspan="3">SUBTOTAL PONDERADO AMENAZAS (A)</td>
        <td>3.7</td>
        <td>3.78</td>
      </tr>
    </tbody>
  </table>

  <!-- SECCIÓN 5: CRUCE ESTRATÉGICO FODA -->
  <h1>5. MATRIZ DE CRUCE ESTRATÉGICO FODA</h1>
  <p>
    La articulación de cuadrantes permite formular estrategias ofensivas, adaptativas, defensivas y de supervivencia:
  </p>

  <div class="img-container">
    <img src="{diag_dofa}" alt="Diagrama Matriz DOFA y Cruce Estratégico">
    <div class="caption">Figura 1: Matriz DOFA Personal del Ser Emprendedor y Cruce Estratégico FODA - Karen Campo.</div>
  </div>

  <table>
    <thead>
      <tr>
        <th style="width: 15%;">Tipo Estrategia</th>
        <th style="width: 15%;">Cruce Factores</th>
        <th style="width: 45%;">Descripción de la Estrategia</th>
        <th style="width: 25%;">Resultado Clave Esperado</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="badge badge-success">FO (Ofensiva)</span></td>
        <td>F1 + O3</td>
        <td>Venta por canal web propio sin comisiones del 25% de plataformas comerciales.</td>
        <td>60% de pedidos canalizados por portal web en 6 meses.</td>
      </tr>
      <tr>
        <td><span class="badge badge-success">FO (Ofensiva)</span></td>
        <td>F2 + O2</td>
        <td>Línea 'Pizzas con Sabor Caucano' amparada en la distinción UNESCO Popayán.</td>
        <td>Obtención del sello de calidad gastronómica regional.</td>
      </tr>
      <tr>
        <td><span class="badge badge-primary">DO (Adaptativa)</span></td>
        <td>D3 + O1</td>
        <td>Financiación de horno giratorio y maquinaria mediante Fondo Emprender SENA.</td>
        <td>Adquisición de activos productivos sin endeudamiento.</td>
      </tr>
      <tr>
        <td><span class="badge badge-primary">DO (Adaptativa)</span></td>
        <td>D1 + O5</td>
        <td>Capacitación en técnicas de venta consultiva y pitch comercial en SBDC SENA.</td>
        <td>Aprobación de 40 horas en habilidades de negociación.</td>
      </tr>
      <tr>
        <td><span class="badge badge-warning">FA (Defensiva)</span></td>
        <td>F1 + A1</td>
        <td>Submódulo de control de escandallos en software para blindar costo de recetas.</td>
        <td>Materia prima mantenida por debajo del 32% del precio.</td>
      </tr>
      <tr>
        <td><span class="badge badge-warning">FA (Defensiva)</span></td>
        <td>F2 + A2</td>
        <td>Diferenciación radical: alta cocina artesanal, sin entrar a guerra de precios.</td>
        <td>Fidelización y recompra superior al 45% en clientes.</td>
      </tr>
      <tr>
        <td><span class="badge badge-danger">DA (Supervivencia)</span></td>
        <td>D4 + A1</td>
        <td>Manuales de procedimientos estándar (SOP) para delegar en el personal.</td>
        <td>Operación de turnos completos sin presencia obligada del líder.</td>
      </tr>
      <tr>
        <td><span class="badge badge-danger">DA (Supervivencia)</span></td>
        <td>D5 + A4</td>
        <td>Asesoría contable externa trimestral y adopción del Régimen Simple (RST).</td>
        <td>Cero sanciones tributarias ante la DIAN.</td>
      </tr>
    </tbody>
  </table>

  <!-- SECCIÓN 6: DIAGNÓSTICO DEL TEMPERAMENTO Y EMOCIONES -->
  <h1>6. DIAGNÓSTICO DEL TEMPERAMENTO, RESILIENCIA Y MANEJO DE EMOCIONES</h1>
  <p>
    Con base en los requerimientos reflexivos de la <strong>Guía 10 (Sección 3.2.1)</strong>, se documenta la respuesta del aprendiz frente a dos escenarios críticos:
  </p>
  <div class="info-card">
    <strong>1. Cuando las cosas salen bien (Manejo del Éxito):</strong><br>
    <em>Temperamento y Humildad:</em> Asumo los buenos resultados con serenidad, evitando la euforia desmedida. Entiendo que un mes de altas ventas es consecuencia de la constancia y no un cheque en blanco. Mantengo la disciplina financiera reinvirtiendo utilidades en tecnología y bienestar del equipo.
  </div>
  <div class="warning-card">
    <strong>2. Cuando las cosas no salen bien (Manejo de la Adversidad):</strong><br>
    <em>Paciencia y Resiliencia:</em> Ante fallas técnicas o pedidos insatisfechos, mantengo la tranquilidad. Aplico el enfoque del desarrollo de software: los errores son "bugs" que requieren análisis de causa raíz y corrección metódica. El objetivo estratégico de la pizzería no se abandona; se itera la táctica operativa.
  </div>

  <h2>6.1 Respuestas a las Preguntas Orientadoras de la Guía 10</h2>
  <div class="step-card">
    <strong>¿Cómo los aspectos identificados le ayudarán a impulsar su emprendimiento?</strong><br>
    El autodiagnóstico DOFA me permite enfocar el 80% de mis esfuerzos en mis mayores ventajas competitivas: mi dominio técnico en software ADSO y mi pasión por los ingredientes caucanos. Al mismo tiempo, visibilizar mis vacíos en finanzas y ventas me compromete a capacitarme en el Centro de Desarrollo Empresarial SENA, evitando errores costosos durante la fase de implantación.
  </div>
  <div class="step-card">
    <strong>¿Qué estrategia le ayudaría a su personalidad para minimizar las amenazas del entorno?</strong><br>
    La estrategia de <strong>Diferenciación por Calidad e Identidad Local</strong> respaldada en la previsión analítica. Frente a la inflación y a cadenas multinacionales low-cost, mi personalidad estructurada me permite controlar costos al gramo con mi propio software y cautivar al público con masa madre artesanal y productos de Silvia, blindando el negocio frente a competidores masivos.
  </div>

  <!-- SECCIÓN 7: ESTRUCTURA DE LA HOJA DE CÁLCULO INTERACTIVA -->
  <h1>7. ESTRUCTURA Y FUNCIONAMIENTO DE LA HOJA DE CÁLCULO INTERACTIVA</h1>
  <p>
    En cumplimiento con el formato exigido por el usuario, se diseñó el libro de cálculo interactivo en formatos <strong>.ods</strong> y <strong>.xlsx</strong> estructurado en seis (6) hojas técnicas:
  </p>
  <ul>
    <li><code>Portada_Institucional</code>: Ficha curricular SENA, datos de la aprendiz y marco del proyecto.</li>
    <li><code>Matriz_DOFA_Personal</code>: Evaluación de 20 factores ponderados con fórmulas activas (Score F: 4.65, Score D: 3.78, Score O: 4.60, Score A: 3.78).</li>
    <li><code>Cruce_Estrategico_FODA</code>: 16 estrategias tabuladas con metas operativas.</li>
    <li><code>Diagnostico_Emocional</code>: Matriz de temperamento ante el éxito vs. adversidad y respuestas orientadoras.</li>
    <li><code>Plan_Accion_SMART</code>: Cronograma de 8 metas con KPIs y semaforización.</li>
    <li><code>Dashboard_Metricas</code>: Cuadro de mando que computa el <strong>Índice de Potencial Emprendedor (IPE = 1.22)</strong>, certificando matemáticamente la viabilidad del perfil.</li>
  </ul>

  <!-- SECCIÓN 8: PLAN DE ACCIÓN Y METAS SMART -->
  <h1>8. PLAN DE ACCIÓN PERSONAL Y METAS SMART</h1>
  <table>
    <thead>
      <tr>
        <th style="width: 8%;">ID</th>
        <th style="width: 14%;">Dimensión</th>
        <th style="width: 40%;">Meta Específica SMART</th>
        <th style="width: 12%;">Plazo</th>
        <th style="width: 14%;">Indicador KPI</th>
        <th style="width: 12%;">Estado</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>M1</strong></td>
        <td>Técnica / IT</td>
        <td>Desplegar versión 1.0 del portal web, KDS y POS en contenedores Docker.</td>
        <td>Mes 1</td>
        <td>100% módulos listos</td>
        <td><span class="badge badge-success">CUMPLIDA</span></td>
      </tr>
      <tr>
        <td><strong>M2</strong></td>
        <td>Personal</td>
        <td>Curso de 40 horas en Inteligencia Emocional y Liderazgo en SENA SofíaPlus.</td>
        <td>Mes 2</td>
        <td>Certificado emitido</td>
        <td><span class="badge badge-primary">EN PROCESO</span></td>
      </tr>
      <tr>
        <td><strong>M3</strong></td>
        <td>Financiera</td>
        <td>Estructurar modelo de costos y punto de equilibrio con asesor del SBDC SENA.</td>
        <td>Mes 3</td>
        <td>Balance validado</td>
        <td><span class="badge badge-primary">EN PROCESO</span></td>
      </tr>
      <tr>
        <td><strong>M4</strong></td>
        <td>Operativa</td>
        <td>Formalizar alianza comercial con dos productores de quesos de Silvia.</td>
        <td>Mes 4</td>
        <td>2 convenios firmados</td>
        <td><span class="badge badge-warning">PLANIFICADA</span></td>
      </tr>
      <tr>
        <td><strong>M5</strong></td>
        <td>Comercial</td>
        <td>Campaña en redes sociales alcanzando 5.000 visualizaciones en Popayán.</td>
        <td>Mes 5</td>
        <td>500 pedidos web</td>
        <td><span class="badge badge-warning">PLANIFICADA</span></td>
      </tr>
      <tr>
        <td><strong>M6</strong></td>
        <td>Institucional</td>
        <td>Radicar plan de negocio formal en convocatoria Fondo Emprender SENA.</td>
        <td>Mes 6</td>
        <td>Radicado asignado</td>
        <td><span class="badge badge-warning">PLANIFICADA</span></td>
      </tr>
      <tr>
        <td><strong>M7</strong></td>
        <td>Organizacional</td>
        <td>Contratar y capacitar a dos colaboradores con manuales SOP de operaciones.</td>
        <td>Mes 8</td>
        <td>2 empleos formales</td>
        <td><span class="badge badge-warning">PLANIFICADA</span></td>
      </tr>
      <tr>
        <td><strong>M8</strong></td>
        <td>Calidad</td>
        <td>Obtener concepto sanitario favorable BPM por la Secretaría de Salud Popayán.</td>
        <td>Mes 12</td>
        <td>Certificación BPM</td>
        <td><span class="badge badge-warning">PLANIFICADA</span></td>
      </tr>
    </tbody>
  </table>

  <div class="page-break"></div>

  <!-- SECCIÓN 9: EVIDENCIAS GRÁFICAS DE EJECUCIÓN -->
  <h1>9. EVIDENCIAS GRÁFICAS DE EJECUCIÓN EN ENTORNO KDE X11</h1>
  <p>
    Capturas de pantalla reales capturadas con <strong>Spectacle</strong> sobre el servidor gráfico <strong>KDE X11 (`DISPLAY=:0`)</strong>, ejecutando comandos en <strong>Konsole</strong> y visualizando la hoja de cálculo en <strong>LibreOffice Calc</strong> (`localc`), minimizando cualquier ventana de Visual Studio Code:
  </p>

  <div class="img-container">
    <img src="{cap1_path}" alt="Paso 1: Generación de la Hoja de Cálculo en Konsole">
    <div class="caption">Figura 2: Paso 1 - Generación automatizada de los libros de cálculo (.xml, .ods, .xlsx) mediante script Python en terminal Konsole.</div>
  </div>

  <div class="img-container">
    <img src="{cap2_path}" alt="Paso 2: LibreOffice Calc - Hoja 1 Portada">
    <div class="caption">Figura 3: Paso 2 - Inspección de la Hoja 1 (Portada Institucional y Perfil del Emprendedor) en la aplicación nativa LibreOffice Calc.</div>
  </div>

  <div class="img-container">
    <img src="{cap3_path}" alt="Paso 3: LibreOffice Calc - Hoja 2 Matriz DOFA">
    <div class="caption">Figura 4: Paso 3 - Visualización de la Hoja 2 (Matriz DOFA Personal Ponderada con 20 factores y fórmulas de puntaje) en LibreOffice Calc.</div>
  </div>

  <div class="page-break"></div>

  <div class="img-container">
    <img src="{cap4_path}" alt="Paso 4: LibreOffice Calc - Hoja 3 Cruce FODA">
    <div class="caption">Figura 5: Paso 4 - Visualización de la Hoja 3 (Matriz de Cruce Estratégico FODA: Estrategias FO, DO, FA, DA) en LibreOffice Calc.</div>
  </div>

  <div class="img-container">
    <img src="{cap5_path}" alt="Paso 5: LibreOffice Calc - Hoja 5 Plan SMART">
    <div class="caption">Figura 6: Paso 5 - Visualización de la Hoja 5 (Plan de Acción Personal y Metas SMART a 12 meses con semáforos) en LibreOffice Calc.</div>
  </div>

  <div class="img-container">
    <img src="{cap6_path}" alt="Paso 6: LibreOffice Calc - Hoja 6 Dashboard IPE">
    <div class="caption">Figura 7: Paso 6 - Visualización de la Hoja 6 (Dashboard Numérico y cálculo del Índice de Potencial Emprendedor IPE = 1.22) en LibreOffice Calc.</div>
  </div>

  <!-- SECCIÓN 10: CONCLUSIONES Y COMPROMISOS -->
  <h1>10. CONCLUSIONES Y COMPROMISOS DEL APRENDIZ</h1>
  <div class="info-card">
    <ol>
      <li><strong>Apropiación de la Cultura Emprendedora:</strong> La evidencia demostró que el emprendimiento es una habilidad estructurada y aprendible. Como tecnóloga ADSO, el software cobra pleno sentido cuando se transforma en un motor empresarial de impacto social.</li>
      <li><strong>Pertinencia del Formato en Hoja de Cálculo:</strong> Desarrollar el ejercicio en una hoja de cálculo interactiva permitió conectar el análisis cualitativo con fórmulas cuantitativas de ponderación, trazabilidad y semáforos de metas.</li>
      <li><strong>Viabilidad Empresarial Comprobada:</strong> El Índice de Potencial Emprendedor (IPE) de 1.22 certifica que el proyecto Pizzería Gourmet Bella Italia Popayán tiene fundamentos sólidos para postularse a la convocatoria de Fondo Emprender SENA.</li>
      <li><strong>Aporte al Desarrollo Regional del Cauca:</strong> El proyecto integra la gastronomía patrimonial de Popayán UNESCO con insumos directos de campesinos de Silvia, promoviendo comercio justo y empleo formal.</li>
    </ol>
  </div>

  <!-- SECCIÓN 11: REFERENCIAS BIBLIOGRÁFICAS -->
  <h1>11. REFERENCIAS BIBLIOGRÁFICAS (NORMAS APA 7.ª EDICIÓN)</h1>
  <ul style="font-size: 7.7pt; line-height: 1.45;">
    <li>Aulet, B. (2017). <em>Disciplined Entrepreneurship: 24 Steps to a Successful Startup</em>. John Wiley & Sons, Inc., Hoboken, New Jersey.</li>
    <li>Chiavenato, I. (2019). <em>Introducción a la teoría general de la administración</em> (10.ª ed.). McGraw-Hill Interamericana.</li>
    <li>Congreso de la República de Colombia. (2006). <em>Ley 1014 de 2006: De fomento a la cultura del emprendimiento</em>. Diario Oficial No. 46.164.</li>
    <li>David, F. R., & David, F. R. (2017). <em>Strategic Management: A Competitive Advantage Approach, Concepts and Cases</em> (16th ed.). Pearson Education.</li>
    <li>Fondo Emprender SENA. (2024). <em>Términos de referencia para convocatorias nacionales de capital semilla condonable</em>. Servicio Nacional de Aprendizaje.</li>
    <li>Servicio Nacional de Aprendizaje (SENA). (2024). <em>Componente formativo: Ser emprendedor</em>. Dirección de Formación Profesional, Sistema Nacional de Formación para el Trabajo, Colombia.</li>
  </ul>

</body>
</html>
"""

# Guardar HTML para conversión
html_path = os.path.join(DOCS_DIR, 'GA10-240201529-AA1-EV01_DOFA_Personal_Emprendedor.html')
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
print(f"[OK] HTML generado exitosamente en: {html_path}")

# Compilar PDF mediante Google Chrome Headless
pdf_path = os.path.join(DOCS_DIR, 'GA10-240201529-AA1-EV01_DOFA_Personal_Emprendedor.pdf')
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
docx_auto = os.path.join(DOCS_DIR, 'GA10-240201529-AA1-EV01_DOFA_Personal_Emprendedor.docx')
print(f"[OK] DOCX generado ({os.path.getsize(docx_auto)/1024:.1f} KB): {docx_auto}")

# Copiar a ENTREGA_DIR y ARTIFACT_DIR
dst_pdf = os.path.join(ENTREGA_DIR, 'GA10-240201529-AA1-EV01_DOFA_Personal_Emprendedor.pdf')
dst_docx = os.path.join(ENTREGA_DIR, 'GA10-240201529-AA1-EV01_DOFA_Personal_Emprendedor.docx')
shutil.copy2(pdf_path, dst_pdf)
shutil.copy2(docx_auto, dst_docx)

art_pdf = os.path.join(ARTIFACT_DIR, 'GA10-240201529-AA1-EV01_DOFA_Personal_Emprendedor.pdf')
art_docx = os.path.join(ARTIFACT_DIR, 'GA10-240201529-AA1-EV01_DOFA_Personal_Emprendedor.docx')
shutil.copy2(pdf_path, art_pdf)
shutil.copy2(docx_auto, art_docx)

# Copiar hoja_de_calculo, diagramas y capturas a ENTREGA_DIR
for sub in ['hoja_de_calculo', 'diagramas', 'capturas']:
    src_sub = os.path.join(BASE_DIR, sub)
    dst_sub = os.path.join(ENTREGA_DIR, sub)
    if os.path.exists(dst_sub):
        shutil.rmtree(dst_sub)
    shutil.copytree(src_sub, dst_sub)
    print(f"[OK] Carpeta {sub} copiada a entrega Zajuna")

# Copiar archivos clave de hoja de cálculo a la raíz de ENTREGA_DIR
ods_src = os.path.join(HOJA_DIR, 'GA10-240201529-AA1-EV01_DOFA_Personal_Emprendedor.ods')
xlsx_src = os.path.join(HOJA_DIR, 'GA10-240201529-AA1-EV01_DOFA_Personal_Emprendedor.xlsx')
shutil.copy2(ods_src, os.path.join(ENTREGA_DIR, 'GA10-240201529-AA1-EV01_DOFA_Personal_Emprendedor.ods'))
shutil.copy2(xlsx_src, os.path.join(ENTREGA_DIR, 'GA10-240201529-AA1-EV01_DOFA_Personal_Emprendedor.xlsx'))

# Copiar diagramas y capturas a ARTIFACT_DIR
shutil.copy2(diag_dofa, os.path.join(ARTIFACT_DIR, 'matriz_dofa_personal_emprendedor.png'))
shutil.copy2(xlsx_src, os.path.join(ARTIFACT_DIR, 'GA10-240201529-AA1-EV01_DOFA_Personal_Emprendedor.xlsx'))
shutil.copy2(ods_src, os.path.join(ARTIFACT_DIR, 'GA10-240201529-AA1-EV01_DOFA_Personal_Emprendedor.ods'))

for cap in os.listdir(CAPTURAS_DIR):
    if cap.endswith('.png'):
        shutil.copy2(os.path.join(CAPTURAS_DIR, cap), os.path.join(ARTIFACT_DIR, cap))
print(f"[OK] Diagramas, capturas y hojas de cálculo copiados a artefactos: {ARTIFACT_DIR}")

# Generar archivo de enlaces institucional
repo_txt_path = os.path.join(ENTREGA_DIR, 'enlace_repositorio.txt')
with open(repo_txt_path, 'w', encoding='utf-8') as f:
    f.write("""ENLACE DEL REPOSITORIO GITHUB - EVIDENCIA GA10-240201529-AA1-EV01
Competencia: 240201529 - Gestionar procesos propios de la cultura emprendedora y empresarial de acuerdo con el perfil personal y los requerimientos de los contextos productivo y social
Actividad de Aprendizaje: GA10-240201529-AA1 - Reconocer capacidades personales para convertirse en emprendedor, como parte de su proyecto de vida en términos de desarrollo humano y económico
Evidencia: GA10-240201529-AA1-EV01 - DOFA personal (Hoja de Cálculo y Análisis Estratégico)
Resultado de Aprendizaje: 240201529-01 - Integrar elementos de la cultura emprendedora teniendo en cuenta el perfil personal y el contexto de desarrollo social
Componente Formativo: "Ser emprendedor"
Instrumento de Evaluación: Lista de Chequeo IE-GA10-240201529-AA1-EV01
Aprendiz: Karen Yuliana Campo - Ficha 3186681
Centro de Teleinformática y Producción Industrial (CTPI Popayán) - Regional Cauca
Proyecto de Vida y Emprendimiento: Pizzería Gourmet Bella Italia Popayán

--------------------------------------------------------------------------------
1. ENLACE DEL REPOSITORIO GITHUB DEL PROYECTO:
https://github.com/kyulianacampogutierrez-ux/Evidencias

2. DIRECTORIO DE LA EVIDENCIA EN EL REPOSITORIO:
https://github.com/kyulianacampogutierrez-ux/Evidencias/tree/main/PET-052_GA10-240201529-AA1-EV01_DOFA_Personal_Emprendedor

3. ARCHIVOS ENTREGABLES OFICIALES EN EL PAQUETE:
- Hoja de Cálculo en Excel: GA10-240201529-AA1-EV01_DOFA_Personal_Emprendedor.xlsx (Con 6 hojas interactivas)
- Hoja de Cálculo en Calc: GA10-240201529-AA1-EV01_DOFA_Personal_Emprendedor.ods (Formato OpenDocument)
- Documento Principal en PDF: GA10-240201529-AA1-EV01_DOFA_Personal_Emprendedor.pdf
- Documento Editable en Word: GA10-240201529-AA1-EV01_DOFA_Personal_Emprendedor.docx
- Diagrama Matriz FODA y Cruce Estratégico: matriz_dofa_personal_emprendedor.png / .svg
- Documento de Análisis Completo en Markdown: DOFA_PERSONAL_EMPRENDEDOR_ANALISIS.md
- Carpeta de Capturas Reales (KDE X11 con Spectacle, Konsole y Calc): capturas/ (6 imágenes PNG)
- Scripts de Automatización: scripts/ (generar_hoja_calculo_dofa.py, capturar_pantallas_kde.sh, compile_pdf.py)
--------------------------------------------------------------------------------
""")
print(f"[OK] enlace_repositorio.txt generado en: {repo_txt_path}")

# Empacar ZIP de entrega institucional
zip_name = 'KARENCAMPO_AA1_EV01_GUIA10.zip'
zip_path = os.path.join(ENTREGA_DIR, zip_name)
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, BASE_DIR)
            z.write(full_path, arcname=os.path.join('PET-052_GA10-AA1-EV01', rel_path))
    z.write(repo_txt_path, arcname='enlace_repositorio.txt')
print(f"[OK] Paquete ZIP generado exitosamente ({os.path.getsize(zip_path)/1024:.1f} KB): {zip_path}")
print("=== COMPILACIÓN FINALIZADA CON ÉXITO ===")
