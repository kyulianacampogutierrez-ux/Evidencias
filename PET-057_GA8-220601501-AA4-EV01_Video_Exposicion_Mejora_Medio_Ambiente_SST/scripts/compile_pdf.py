#!/usr/bin/env python3
# ==============================================================================
# COMPILADOR DE DOCUMENTACIÓN TÉCNICA FORMAL (PDF / DOCX / ZIP / ENLACE)
# Evidencia: GA8-220601501-AA4-EV01 - Oportunidades de Mejora Medio Ambiente y SST
# Competencia: 220601501 | Actividad: GA8-220601501-AA4
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán - Regional Cauca
# ==============================================================================

import os
import sys
import shutil
import zipfile
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
CAPTURAS_DIR = os.path.join(BASE_DIR, 'capturas')
IMG_DIR = os.path.join(BASE_DIR, 'imagenes_reales')
VIDEO_DIR = os.path.join(BASE_DIR, 'video')
SITIO_DIR = os.path.join(BASE_DIR, 'sitio_sst_web')
ENTREGA_DIR = '/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA8-220601501-AA4-EV01'
BRAIN_DIR = '/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603'

os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(ENTREGA_DIR, exist_ok=True)
os.makedirs(BRAIN_DIR, exist_ok=True)

cap1_path = os.path.join(CAPTURAS_DIR, 'paso_01_despliegue_docker_sst_konsole.png')
cap2_path = os.path.join(CAPTURAS_DIR, 'paso_02_verificacion_salud_servicios_sst_konsole.png')
cap3_path = os.path.join(CAPTURAS_DIR, 'paso_03_chrome_portal_sst_video_reproductor.png')
cap4_path = os.path.join(CAPTURAS_DIR, 'paso_04_chrome_galeria_imagenes_reales_mejora.png')
cap5_path = os.path.join(CAPTURAS_DIR, 'paso_05_chrome_guion_tecnico_completo.png')
cap6_path = os.path.join(CAPTURAS_DIR, 'paso_06_chrome_dataset_indicadores_phva.png')

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Informe Técnico - Oportunidades de Mejora Medio Ambiente y SST | Karen Campo</title>
  <style>
    @page {
      size: letter;
      margin: 1.1cm 1.3cm 1.1cm 1.3cm;
      @bottom-right {
        content: counter(page);
      }
    }
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      font-family: 'Segoe UI', system-ui, -apple-system, BlinkMacSystemFont, "Roboto", sans-serif;
      color: #1e293b;
      line-height: 1.45;
      font-size: 9.5pt;
    }
    .page {
      page-break-after: always;
      position: relative;
    }
    .page:last-child {
      page-break-after: avoid;
    }

    .header-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid #008C45;
      padding-bottom: 6px;
      margin-bottom: 14px;
    }
    .header-title {
      font-size: 8pt;
      font-weight: 700;
      color: #008C45;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .header-meta {
      font-size: 7.5pt;
      color: #64748b;
      text-align: right;
    }

    h1.doc-title {
      font-size: 16pt;
      color: #0f172a;
      line-height: 1.2;
      margin-bottom: 6px;
      font-weight: 800;
    }
    h2.doc-subtitle {
      font-size: 10.5pt;
      color: #008C45;
      font-weight: 700;
      margin-bottom: 12px;
    }
    h2.section-title {
      font-size: 11pt;
      color: #008C45;
      border-left: 4px solid #008C45;
      padding-left: 8px;
      margin-top: 14px;
      margin-bottom: 8px;
      font-weight: 700;
    }
    h3.sub-title {
      font-size: 9.5pt;
      color: #0f172a;
      margin-top: 10px;
      margin-bottom: 4px;
      font-weight: 700;
    }
    p {
      margin-bottom: 6px;
      text-align: justify;
    }

    .badge-box {
      display: flex;
      gap: 6px;
      margin-bottom: 10px;
      flex-wrap: wrap;
    }
    .badge {
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 7.5pt;
      font-weight: 600;
      color: #334155;
    }
    .badge-green {
      background: #ecfdf5;
      border-color: #a7f3d0;
      color: #065f46;
    }

    .card {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 8px 12px;
      margin-bottom: 10px;
    }

    table.info-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 8pt;
      margin-bottom: 8px;
    }
    table.info-table th {
      background: #008C45;
      color: white;
      text-align: left;
      padding: 5px 8px;
      font-weight: 600;
      border: 1px solid #008C45;
    }
    table.info-table td {
      border: 1px solid #e2e8f0;
      padding: 4px 8px;
      vertical-align: top;
    }
    table.info-table tr:nth-child(even) {
      background: #f8fafc;
    }

    table.mejora-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 7.5pt;
      margin-top: 6px;
      margin-bottom: 10px;
    }
    table.mejora-table th {
      background: #1e293b;
      color: white;
      padding: 5px 8px;
      text-align: left;
      font-weight: 700;
      border: 1px solid #334155;
    }
    table.mejora-table td {
      border: 1px solid #cbd5e1;
      padding: 5px 8px;
      vertical-align: top;
    }
    table.mejora-table tr:nth-child(even) {
      background: #fbfcfe;
    }

    .img-box {
      text-align: center;
      margin: 8px 0;
    }
    .img-box img {
      width: 100%;
      max-height: 250px;
      object-fit: contain;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    }
    .img-caption {
      font-size: 7.5pt;
      color: #64748b;
      margin-top: 3px;
      font-weight: 600;
    }

    .callout-green {
      border-left: 4px solid #10b981;
      background: #ecfdf5;
      padding: 6px 10px;
      border-radius: 0 4px 4px 0;
      margin-bottom: 8px;
      font-size: 8pt;
      color: #065f46;
    }
    .callout-blue {
      border-left: 4px solid #0284c7;
      background: #f0f9ff;
      padding: 6px 10px;
      border-radius: 0 4px 4px 0;
      margin-bottom: 8px;
      font-size: 8pt;
      color: #0369a1;
    }
  </style>
</head>
<body>

  <!-- PÁGINA 1: PORTADA Y METODOLOGÍA -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">SENA CTPI Popayán • Regional Cauca • Informe Técnico Formal</div>
      <div class="header-meta">Evidencia: GA8-220601501-AA4-EV01 | Ficha: 3186681</div>
    </div>

    <h1 class="doc-title">INFORME TÉCNICO: VIDEO EXPOSITIVO SOBRE OPORTUNIDADES DE MEJORA EN MEDIO AMBIENTE Y SST</h1>
    <h2 class="doc-subtitle">Estudio de Casos en el Entorno de Desarrollo de Software ADSO y Sector Productivo de Popayán</h2>

    <div class="badge-box">
      <span class="badge badge-green">Competencia: 220601501</span>
      <span class="badge">Actividad: GA8-220601501-AA4</span>
      <span class="badge">Instrumento: IE-GA8-220601501-AA4-EV01</span>
      <span class="badge">Aprendiz: Karen Yuliana Campo</span>
      <span class="badge">Programa: Tecnólogo en ADSO</span>
      <span class="badge">Servidor Docker: Puerto 8105</span>
    </div>

    <div class="card">
      <table class="info-table" style="margin-bottom: 0;">
        <tr>
          <th style="width: 25%;">Centro de Formación:</th>
          <td>CTPI Popayán — Regional Cauca</td>
          <th style="width: 25%;">Ficha de Caracterización:</th>
          <td>3186681 (ADSO)</td>
        </tr>
        <tr>
          <th>Aprendiz Autora:</th>
          <td>Karen Yuliana Campo</td>
          <th>Fase del Proyecto:</th>
          <td>Fase 4 — Evaluación</td>
        </tr>
        <tr>
          <th>Contextos Productivos:</th>
          <td>Entorno Tecnológico ADSO & Pizzería Gourmet Bella Italia Popayán</td>
          <th>Metodología Central:</th>
          <td>Ciclo PHVA (Planear, Hacer, Verificar, Actuar) + Normatividad Colombiana</td>
        </tr>
      </table>
    </div>

    <h2 class="section-title">1. Introducción y Justificación</h2>
    <p>
      La formulación y adopción de oportunidades de mejora en el medio ambiente y en Seguridad y Salud en el Trabajo (SST) constituye una competencia transversal imprescindible para el tecnólogo en desarrollo de software. En el marco productivo colombiano, el cumplimiento del Sistema de Gestión de la Seguridad y Salud en el Trabajo (SG-SST) bajo el Decreto 1072 de 2015 y la adopción de normativas ambientales como la Resolución 2184 de 2019 garantizan espacios laborales seguros, sostenibles y altamente competitivos.
    </p>
    <p>
      El presente informe formaliza la entrega de la evidencia <strong>GA8-220601501-AA4-EV01</strong>, la cual integra un video expositivo interactivo Full HD 1080p con locución, un guion técnico individual de preproducción, la fundamentación de diez (10) oportunidades de mejora acompañadas por <strong>imágenes fotográficas reales</strong>, y el despliegue de un portal web contenedorizado en Docker Apache HTTPD (puerto 8105).
    </p>

    <h2 class="section-title">2. Marco Normativo Colombiano</h2>
    <div class="callout-green">
      <strong>Pilares Normativos en Gestión Ambiental:</strong><br>
      • <strong>Res. 2184 de 2019:</strong> Código unificado de colores (Blanco: aprovechables; Verde: orgánicos; Negro: no aprovechables).<br>
      • <strong>Res. 316 de 2018:</strong> Manejo integral y entrega certificada de Aceites de Cocina Usados (ACU).<br>
      • <strong>Leyes 1715 de 2014 & 2099 de 2021:</strong> Eficiencia energética e incorporación de luminarias LED.<br>
      • <strong>Ley 1672 de 2013:</strong> Gestión integral de Residuos de Aparatos Eléctricos y Electrónicos (RAEE).<br>
      • <strong>Ley 373 de 1997:</strong> Uso eficiente y ahorro del agua potable en instalaciones de servicios.
    </div>

    <div class="callout-blue">
      <strong>Pilares Normativos en Seguridad y Salud en el Trabajo (SST):</strong><br>
      • <strong>Decreto 1072 de 2015:</strong> SG-SST institucional y ciclo PHVA de mejora continua.<br>
      • <strong>Guía Técnica GTC 45:</strong> Prevención de peligros biomecánicos y adecuación antropométrica del puesto de cómputo.<br>
      • <strong>Resolución 2400 de 1979:</strong> Estatuto de Seguridad Industrial, escaleras seguras y pisos antideslizantes.<br>
      • <strong>Norma Técnica NTC 2885 / NFPA 10:</strong> Extintores Clase K para cocinas y CO2/Solkaflam para centros de cómputo.<br>
      • <strong>Reglamento RETIE & Metodología 5S:</strong> Canalización ordenada de cableado y despeje perimetral.<br>
      • <strong>Ley 2191 de 2022:</strong> Desconexión laboral y programa de pausas activas osteomusculares.
    </div>
  </div>

  <!-- PÁGINA 2: LAS 10 MEJORAS REALES -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">SENA CTPI Popayán • Matriz de 10 Oportunidades de Mejora Demostradas</div>
      <div class="header-meta">5 Gestión Ambiental + 5 Seguridad y Salud en el Trabajo</div>
    </div>

    <h2 class="section-title" style="margin-top: 0;">3. Catálogo de 10 Oportunidades de Mejora con Imágenes Reales</h2>

    <table class="mejora-table">
      <thead>
        <tr>
          <th style="width: 10%;">ID / Pilar</th>
          <th style="width: 25%;">Oportunidad de Mejora</th>
          <th style="width: 15%;">Normativa</th>
          <th style="width: 32%;">Acciones Operativas Clave</th>
          <th style="width: 18%;">Meta / Indicador</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>OM-AMB-01</strong><br>Ambiental</td>
          <td><strong>Separación en la fuente con código unificado</strong></td>
          <td>Res. 2184 de 2019</td>
          <td>Batería de 3 canecas (Blanco: aprovechables, Verde: orgánicos, Negro: ordinarios). Capacitación semestral y alianza con recicladores.</td>
          <td>Aprovechamiento &gt; 65% de residuos generados.</td>
        </tr>
        <tr>
          <td><strong>OM-AMB-02</strong><br>Ambiental</td>
          <td><strong>Trampa de grasas y gestión certificada de ACU</strong></td>
          <td>Res. 316 de 2018</td>
          <td>Trampa inox bajo pozuelos de lavado. Almacenamiento en bidones rotulados y entrega mensual a gestores de biodiesel.</td>
          <td>100% de ACU recolectado sin vertimiento a redes de agua.</td>
        </tr>
        <tr>
          <td><strong>OM-AMB-03</strong><br>Ambiental</td>
          <td><strong>Eficiencia energética y sensores PIR</strong></td>
          <td>Leyes 1715/14 &amp; 2099/21</td>
          <td>Paneles LED de 18W, sensores de presencia infrarrojos en zonas comunes y suspensión automática de pantallas ADSO tras 10 min.</td>
          <td>Reducción del 25% en consumo mensual de kWh.</td>
        </tr>
        <tr>
          <td><strong>OM-AMB-04</strong><br>Ambiental</td>
          <td><strong>Gestión integral de residuos RAEE</strong></td>
          <td>Ley 1672 de 2013</td>
          <td>Contenedor segregado para hardware, fuentes y tarjetas. Priorización de reparación y entrega a programas posconsumo.</td>
          <td>Cero kg de desechos electrónicos en basura común.</td>
        </tr>
        <tr>
          <td><strong>OM-AMB-05</strong><br>Ambiental</td>
          <td><strong>Ahorro eficiente de agua con aireadores</strong></td>
          <td>Ley 373 de 1997</td>
          <td>Difusores aireadores en griferías (reducción a 4.5 L/min) y monitoreo nocturno de hidrómetros para detección precoz de fugas.</td>
          <td>Ahorro del 40% en consumo mensual de agua potable.</td>
        </tr>
        <tr>
          <td><strong>OM-SST-06</strong><br>SST</td>
          <td><strong>Ergonomía antropométrica del puesto ADSO</strong></td>
          <td>GTC 45 / Dec. 1072/15</td>
          <td>Pantallas a la altura de los ojos, sillas anatómicas con soporte lumbar y descansapiés con ángulo de 90° en codos y rodillas.</td>
          <td>100% de puestos evaluados con nivel de riesgo aceptable.</td>
        </tr>
        <tr>
          <td><strong>OM-SST-07</strong><br>SST</td>
          <td><strong>Seguridad en escaleras y pisos antideslizantes</strong></td>
          <td>Res. 2400 de 1979</td>
          <td>Cintas de carborundo fotoluminiscente en peldaños, pasamanos dobles a 90 cm y pisos rugosos en zonas de preparación.</td>
          <td>Tasa cero de caídas o resbalones en jornada laboral.</td>
        </tr>
        <tr>
          <td><strong>OM-SST-08</strong><br>SST</td>
          <td><strong>Extintores Clase K y CO2 especializados</strong></td>
          <td>NTC 2885 / NFPA 10</td>
          <td>Extintor Clase K (acetato de potasio) para grasas en cocina y extintor CO2 / Solkaflam para servidores informáticos.</td>
          <td>100% de extintores inspeccionados y vigentes.</td>
        </tr>
        <tr>
          <td><strong>OM-SST-09</strong><br>SST</td>
          <td><strong>Metodología 5S y canalización RETIE</strong></td>
          <td>RETIE &amp; Metodología 5S</td>
          <td>Canaletas perimetrales ignífugas en PVC ranurado, peinado vertical en racks de telecomunicaciones y despeje perimetral.</td>
          <td>Índice 5S superior a 90 puntos en auditoría mensual.</td>
        </tr>
        <tr>
          <td><strong>OM-SST-10</strong><br>SST</td>
          <td><strong>Programa de pausas activas e higiene postural</strong></td>
          <td>Ley 2191 de 2022</td>
          <td>Dos descansos activos diarios de 10 min (10:00 am y 3:30 pm), estiramientos musculares y descanso visual con regla 20-20-20.</td>
          <td>Participación del 100% del personal en pausas activas.</td>
        </tr>
      </tbody>
    </table>

    <h2 class="section-title">4. Ficha Técnica Audiovisual del Video Expositivo</h2>
    <table class="info-table">
      <tr>
        <th style="width: 25%;">Parámetro Técnico</th>
        <th style="width: 35%;">Valor / Especificación</th>
        <th style="width: 40%;">Justificación Pedagógica y Operativa</th>
      </tr>
      <tr>
        <td><strong>Título del Video</strong></td>
        <td>Oportunidades de Mejora en Medio Ambiente y SST</td>
        <td>Evidencia oficial GA8-220601501-AA4-EV01 para Zajuna.</td>
      </tr>
      <tr>
        <td><strong>Formato y Códec</strong></td>
        <td>MP4 (H.264 / AVC High Profile + AAC 192k)</td>
        <td>Compatibilidad universal en navegadores, LMS y móviles.</td>
      </tr>
      <tr>
        <td><strong>Resolución / FPS</strong></td>
        <td>1920 × 1080 (Full HD 1080p) a 30 FPS progresivo</td>
        <td>Máxima nitidez para apreciar detalles de las 10 fotografías reales.</td>
      </tr>
      <tr>
        <td><strong>Duración Total</strong></td>
        <td>07 minutos y 52 segundos (472.08 segundos)</td>
        <td>12 bloques temáticos sincronizados con el guion técnico individual.</td>
      </tr>
      <tr>
        <td><strong>Mezcla de Audio</strong></td>
        <td>Locución vocal de Karen Campo + Ducking BGM (-20 dB)</td>
        <td>Claridad acústica de la voz con compresión sidechain automática.</td>
      </tr>
    </table>
  </div>

  <!-- PÁGINA 3: EVIDENCIAS KDE KONSOLE -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">SENA CTPI Popayán • Evidencias del Despliegue Tecnológico en KDE Plasma X11</div>
      <div class="header-meta">Capturas 1 y 2: Servicios Docker y Verificación HTTP 200</div>
    </div>

    <h2 class="section-title" style="margin-top: 0;">5. Evidencias del Despliegue Tecnológico en KDE Plasma X11 (Parte 1)</h2>

    <div class="img-box">
      <img src="{cap1_path}" alt="Paso 01: Despliegue Docker SST Konsole">
      <div class="img-caption">Captura 1: Despliegue del contenedor Docker sena-sst-ambiental-web (puerto 8105) y verificación de artefactos en Konsole.</div>
    </div>

    <div class="img-box" style="margin-top: 12px;">
      <img src="{cap2_path}" alt="Paso 02: Verificación de Salud de Servicios SST Konsole">
      <div class="img-caption">Captura 2: Verificación HTTP 200 OK del portal web, streaming de video MP4 y consulta del dataset JSON en Konsole.</div>
    </div>
  </div>

  <!-- PÁGINA 4: EVIDENCIAS CHROME PORTAL Y GALERÍA -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">SENA CTPI Popayán • Evidencias del Despliegue Tecnológico en KDE Plasma X11</div>
      <div class="header-meta">Capturas 3 y 4: Reproductor de Video y Galería de Fotos Reales</div>
    </div>

    <h2 class="section-title" style="margin-top: 0;">5. Evidencias del Despliegue Tecnológico en KDE Plasma X11 (Parte 2)</h2>

    <div class="img-box">
      <img src="{cap3_path}" alt="Paso 03: Chrome Portal SST Reproductor Video">
      <div class="img-caption">Captura 3: Portal Web responsive alojado en http://localhost:8105/ con reproductor de video HTML5 Full HD 1080p y métricas.</div>
    </div>

    <div class="img-box" style="margin-top: 12px;">
      <img src="{cap4_path}" alt="Paso 04: Chrome Galería de Imágenes Reales de Mejora">
      <div class="img-caption">Captura 4: Pestaña interactiva con la galería de las 10 oportunidades de mejora ilustradas con sus fotografías reales auténticas.</div>
    </div>
  </div>

  <!-- PÁGINA 5: EVIDENCIAS CHROME GUION Y PHVA / CONCLUSIONES -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">SENA CTPI Popayán • Evidencias KDE Plasma X11 y Conclusiones PHVA</div>
      <div class="header-meta">Capturas 5 y 6: Guion Técnico y Dashboard PHVA / ODS</div>
    </div>

    <h2 class="section-title" style="margin-top: 0;">5. Evidencias del Despliegue Tecnológico en KDE Plasma X11 (Parte 3)</h2>

    <div class="img-box">
      <img src="{cap5_path}" alt="Paso 05: Chrome Guion Técnico Completo">
      <div class="img-caption">Captura 5: Visualizador web del guion técnico y pedagógico estructurado a dos columnas con marcas de tiempo y locución.</div>
    </div>

    <div class="img-box" style="margin-top: 12px;">
      <img src="{cap6_path}" alt="Paso 06: Chrome Dataset Indicadores PHVA">
      <div class="img-caption">Captura 6: Dashboard de articulación del Ciclo PHVA y compromiso con los Objetivos de Desarrollo Sostenible (ODS 3, 6, 7, 8 y 12).</div>
    </div>
  </div>

  <!-- PÁGINA 6: CONCLUSIONES Y REFERENCIAS -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">SENA CTPI Popayán • Conclusiones Finales y Referencias Bibliográficas</div>
      <div class="header-meta">Cierre Académico • Karen Yuliana Campo • ADSO 3186681</div>
    </div>

    <h2 class="section-title" style="margin-top: 0;">6. Conclusiones y Recomendaciones</h2>
    <div class="card">
      <p>
        <strong>1. Articulación Práctica del SG-SST y la Gestión Ambiental:</strong> La formulación de las diez oportunidades de mejora demuestra que los principios de sostenibilidad y prevención de riesgos son perfectamente aplicables tanto en un centro de desarrollo de software (ADSO) como en una empresa gastronómica real en Popayán.
      </p>
      <p>
        <strong>2. Relevancia de las Imágenes Reales:</strong> La incorporación de fotografías auténticas en lugar de gráficos abstractos dota a la evidencia de una validez técnica superior, permitiendo contrastar de forma empírica la situación actual frente a la mejora propuesta.
      </p>
      <p>
        <strong>3. Rigor Normativo Colombiano:</strong> Cada una de las mejoras se fundamentó en instrumentos legales de obligatorio cumplimiento (Res. 2184/2019, Res. 316/2018, Dec. 1072/2015, Res. 2400/1979, Ley 1715/2014, Ley 1672/2013, Ley 373/1997, Ley 2191/2022 y GTC 45), garantizando la idoneidad profesional del tecnólogo en software.
      </p>
      <p>
        <strong>4. Solución Contenerizada en Docker (Puerto 8105):</strong> La implementación web permite la inspección inmediata de los artefactos, reproductor de video, galería de mejoras y visor JSON sin depender de servicios externos.
      </p>
    </div>

    <h2 class="section-title">7. Referencias Bibliográficas (Normas APA 7ma Edición)</h2>
    <ul style="font-size: 8pt; line-height: 1.4; padding-left: 18px; color: #334155;">
      <li style="margin-bottom: 5px;">Congreso de la República de Colombia. (1997, 6 de junio). <em>Ley 373 de 1997: Por la cual se establece el programa para el uso eficiente y ahorro del agua</em>. Diario Oficial No. 43.058.</li>
      <li style="margin-bottom: 5px;">Congreso de la República de Colombia. (2013, 19 de julio). <em>Ley 1672 de 2013: Por la cual se establecen los lineamientos para la adopción de una política pública de gestión integral de Residuos de Aparatos Eléctricos y Electrónicos (RAEE)</em>. Diario Oficial No. 48.856.</li>
      <li style="margin-bottom: 5px;">Congreso de la República de Colombia. (2014, 13 de mayo). <em>Ley 1715 de 2014: Por medio de la cual se regula la integración de las energías renovables no convencionales al Sistema Energético Nacional</em>. Diario Oficial No. 49.150.</li>
      <li style="margin-bottom: 5px;">Congreso de la República de Colombia. (2022, 6 de enero). <em>Ley 2191 de 2022: Por medio de la cual se regula la desconexión laboral</em>. Diario Oficial No. 51.909.</li>
      <li style="margin-bottom: 5px;">Instituto Colombiano de Normas Técnicas y Certificación [ICONTEC]. (2012). <em>Guía Técnica Colombiana GTC 45: Guía para la identificación de los peligros y la valoración de los riesgos en seguridad y salud ocupacional</em>. ICONTEC.</li>
      <li style="margin-bottom: 5px;">Instituto Colombiano de Normas Técnicas y Certificación [ICONTEC]. (2017). <em>Norma Técnica Colombiana NTC 2885: Extintores de fuego portátiles</em>. ICONTEC.</li>
      <li style="margin-bottom: 5px;">Ministerio de Ambiente y Desarrollo Sostenible. (2018, 1 de marzo). <em>Resolución 316 de 2018: Por la cual se establecen las disposiciones para la adecuada gestión de los Aceites de Cocina Usados (ACU)</em>. MinAmbiente.</li>
      <li style="margin-bottom: 5px;">Ministerio de Ambiente y Desarrollo Sostenible. (2019, 26 de diciembre). <em>Resolución 2184 de 2019: Por la cual se modifica la Resolución 668 de 2016 sobre uso racional de bolsas plásticas y se adoptan otras disposiciones</em>. MinAmbiente.</li>
      <li style="margin-bottom: 5px;">Ministerio del Trabajo. (1979, 22 de mayo). <em>Resolución 2400 de 1979: Por la cual se establecen algunas disposiciones sobre vivienda, higiene y seguridad en los establecimientos de trabajo</em>. Diario Oficial No. 35.304.</li>
      <li style="margin-bottom: 5px;">Ministerio del Trabajo. (2015, 26 de mayo). <em>Decreto 1072 de 2015: Por medio del cual se expide el Decreto Único Reglamentario del Sector Trabajo</em>. Presidencia de la República de Colombia.</li>
      <li style="margin-bottom: 5px;">Servicio Nacional de Aprendizaje [SENA]. (2024). <em>Guía de Aprendizaje No. 8: Programa Tecnólogo en Análisis y Desarrollo de Software</em>. Centro de Teleinformática y Producción Industrial (CTPI), Regional Cauca.</li>
    </ul>

    <div style="margin-top: 25px; border-top: 1px solid #cbd5e1; padding-top: 8px; font-size: 8pt; color: #64748b; display: flex; justify-content: space-between;">
      <div><strong>Aprendiz Autora:</strong> Karen Yuliana Campo — Tecnóloga en ADSO</div>
      <div><strong>Regional:</strong> SENA Regional Cauca — CTPI Popayán</div>
    </div>
  </div>

</body>
</html>
"""

def main():
    print("=== INICIANDO COMPILACIÓN DE INFORME TÉCNICO FORMAL Y ARTEFACTOS ===")
    
    # Inyectar rutas absolutas de capturas
    html_rendered = html_content.replace("{cap1_path}", cap1_path)\
                                .replace("{cap2_path}", cap2_path)\
                                .replace("{cap3_path}", cap3_path)\
                                .replace("{cap4_path}", cap4_path)\
                                .replace("{cap5_path}", cap5_path)\
                                .replace("{cap6_path}", cap6_path)

    temp_html = os.path.join(DOCS_DIR, "temp_informe_sst_print.html")
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_rendered)

    # 1. Compilar PDF con Google Chrome Headless
    pdf_out = os.path.join(DOCS_DIR, "GA8-220601501-AA4-EV01_Video_Exposicion_Mejora_Medio_Ambiente_SST.pdf")
    cmd_pdf = [
        "google-chrome",
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_out}",
        temp_html
    ]
    print(f"Compilando PDF en: {pdf_out}...")
    subprocess.run(cmd_pdf, check=True)
    print(f"[OK] PDF Informe generado: {pdf_out} ({os.path.getsize(pdf_out)/1024:.1f} KB)")

    # 2. Compilar DOCX vía LibreOffice (HTML -> ODT -> DOCX)
    temp_odt = os.path.join(DOCS_DIR, "temp_informe_sst_print.odt")
    cmd_odt = ["libreoffice", "--headless", "--convert-to", "odt:writer8", temp_html, "--outdir", DOCS_DIR]
    subprocess.run(cmd_odt, check=True)
    
    docx_out = os.path.join(DOCS_DIR, "GA8-220601501-AA4-EV01_Video_Exposicion_Mejora_Medio_Ambiente_SST.docx")
    cmd_docx = ["libreoffice", "--headless", "--convert-to", "docx:MS Word 2007 XML", temp_odt, "--outdir", DOCS_DIR]
    subprocess.run(cmd_docx, check=True)
    
    final_docx = os.path.join(DOCS_DIR, "temp_informe_sst_print.docx")
    if os.path.exists(final_docx):
        shutil.move(final_docx, docx_out)
    print(f"[OK] DOCX Informe generado: {docx_out} ({os.path.getsize(docx_out)/1024:.1f} KB)")

    # Limpieza temporal
    for f in [temp_html, temp_odt]:
        if os.path.exists(f): os.remove(f)

    # 3. Crear archivo enlace_repositorio.txt
    enlace_path = os.path.join(BASE_DIR, "enlace_repositorio.txt")
    with open(enlace_path, "w", encoding="utf-8") as ef:
        ef.write("""# ==============================================================================
# SERVICIO NACIONAL DE APRENDIZAJE - SENA
# EVIDENCIA: GA8-220601501-AA4-EV01: Video expositivo sobre oportunidades de mejora en el medio ambiente y SST
# PROGRAMA: ANÁLISIS Y DESARROLLO DE SOFTWARE (ADSO) - FICHA: 3186681
# APRENDIZ: KAREN YULIANA CAMPO | CTPI POPAYÁN - REGIONAL CAUCA
# ==============================================================================

Estimado Instructor / Evaluador Técnico:

A continuación se relacionan los enlaces oficiales y recursos de acceso a los artefactos desarrollados para la evidencia GA8-220601501-AA4-EV01:

1. REPOSITORIO GIT OFICIAL DEL PROYECTO:
   https://github.com/danilocampo2024/Evidencias.git
   Rama: main
   Directorio de la Evidencia:
   PET-057_GA8-220601501-AA4-EV01_Video_Exposicion_Mejora_Medio_Ambiente_SST

2. SERVICIO WEB INTERACTIVO EN CONTENEDOR DOCKER (PUERTO 8105):
   http://localhost:8105/
   - Reproductor de Video Expositivo HTML5 con índice por bloques
   - Catálogo responsive de las 10 Oportunidades de Mejora con Fotografías Reales
   - Visor del Guion Técnico Individual estructurado
   - Dashboard de Ciclo PHVA y articulación con los ODS (3, 6, 7, 8 y 12)
   - Inspector del Dataset JSON oficial (/datos_mejora_sst_ambiental.json)

3. ARTEFACTOS ENTREGABLES DISPONIBLES EN EL PAQUETE:
   - GA8-220601501-AA4-EV01_Guion_Video_Exposicion_Mejora_Medio_Ambiente_SST.pdf (Guion Técnico Individual en PDF)
   - GA8-220601501-AA4-EV01_Guion_Video_Exposicion_Mejora_Medio_Ambiente_SST.docx (Guion Técnico Individual en DOCX)
   - GUION_TECNICO_VIDEO_EXPOSICION_MEJORA_MEDIO_AMBIENTE_SST.md (Guion en formato Markdown)
   - GA8-220601501-AA4-EV01_Video_Exposicion_Mejora_Medio_Ambiente_SST.pdf (Informe Técnico Formal en PDF)
   - GA8-220601501-AA4-EV01_Video_Exposicion_Mejora_Medio_Ambiente_SST.docx (Informe Técnico Formal en DOCX)
   - GA8-220601501-AA4-EV01_Video_Exposicion_Mejora_Medio_Ambiente_SST.mp4 (Video Expositivo Maestro Full HD 1080p)
   - ExposicionSSTyMedioAmbiente.fcproj (Proyecto de montaje FilmCraft CLI)
   - 10 Fotografías reales de oportunidades de mejora (/imagenes_reales/)
   - 6 Capturas de pantalla reales en KDE Plasma X11 (/capturas/)

Cordialmente,
Karen Yuliana Campo
Aprendiz ADSO - Ficha 3186681
CTPI Popayán - Regional Cauca
""")
    shutil.copy(enlace_path, os.path.join(ENTREGA_DIR, "enlace_repositorio.txt"))
    shutil.copy(enlace_path, os.path.join(BRAIN_DIR, "enlace_repositorio.txt"))
    print(f"[OK] Archivo de enlaces generado: {enlace_path}")

    # 4. Generar Paquete ZIP oficial para Zajuna
    zip_path = os.path.join(BASE_DIR, "KARENCAMPO_AA4_EV01_GUIA8.zip")
    zip_zajuna = os.path.join(ENTREGA_DIR, "KARENCAMPO_AA4_EV01_GUIA8.zip")
    print(f"Empaquetando entrega oficial Zajuna en: {zip_path}...")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
        # Documentos de Informe
        z.write(pdf_out, arcname=os.path.basename(pdf_out))
        z.write(docx_out, arcname=os.path.basename(docx_out))
        # Documentos de Guion Individual
        guion_pdf = os.path.join(DOCS_DIR, "GA8-220601501-AA4-EV01_Guion_Video_Exposicion_Mejora_Medio_Ambiente_SST.pdf")
        guion_docx = os.path.join(DOCS_DIR, "GA8-220601501-AA4-EV01_Guion_Video_Exposicion_Mejora_Medio_Ambiente_SST.docx")
        guion_md = os.path.join(DOCS_DIR, "GUION_TECNICO_VIDEO_EXPOSICION_MEJORA_MEDIO_AMBIENTE_SST.md")
        if os.path.exists(guion_pdf): z.write(guion_pdf, arcname=os.path.basename(guion_pdf))
        if os.path.exists(guion_docx): z.write(guion_docx, arcname=os.path.basename(guion_docx))
        if os.path.exists(guion_md): z.write(guion_md, arcname=os.path.basename(guion_md))
        # Enlaces
        z.write(enlace_path, arcname="enlace_repositorio.txt")
        # Video MP4
        video_mp4 = os.path.join(VIDEO_DIR, "GA8-220601501-AA4-EV01_Video_Exposicion_Mejora_Medio_Ambiente_SST.mp4")
        if os.path.exists(video_mp4):
            z.write(video_mp4, arcname=f"video/{os.path.basename(video_mp4)}")
        # 10 Imágenes Reales
        if os.path.exists(IMG_DIR):
            for img in os.listdir(IMG_DIR):
                if img.endswith('.png'):
                    z.write(os.path.join(IMG_DIR, img), arcname=f"imagenes_reales/{img}")
        # Capturas
        for cap in [cap1_path, cap2_path, cap3_path, cap4_path, cap5_path, cap6_path]:
            if os.path.exists(cap):
                z.write(cap, arcname=f"capturas/{os.path.basename(cap)}")
    
    shutil.copy(zip_path, zip_zajuna)
    shutil.copy(zip_path, os.path.join(BRAIN_DIR, os.path.basename(zip_path)))
    shutil.copy(zip_path, os.path.join(SITIO_DIR, os.path.basename(zip_path)))
    print(f"[OK] Paquete ZIP generado: {zip_path} ({os.path.getsize(zip_path)/(1024*1024):.1f} MB)")

    # 5. Distribuir entregables formales a Zajuna y Brain
    shutil.copy(pdf_out, os.path.join(ENTREGA_DIR, os.path.basename(pdf_out)))
    shutil.copy(docx_out, os.path.join(ENTREGA_DIR, os.path.basename(docx_out)))
    shutil.copy(pdf_out, os.path.join(BRAIN_DIR, os.path.basename(pdf_out)))
    shutil.copy(docx_out, os.path.join(BRAIN_DIR, os.path.basename(docx_out)))
    
    # Copiar documentos al directorio docs del sitio web para descargas directas
    sitio_docs = os.path.join(SITIO_DIR, "docs")
    os.makedirs(sitio_docs, exist_ok=True)
    shutil.copy(pdf_out, os.path.join(sitio_docs, os.path.basename(pdf_out)))
    shutil.copy(docx_out, os.path.join(sitio_docs, os.path.basename(docx_out)))
    if os.path.exists(guion_pdf): shutil.copy(guion_pdf, os.path.join(sitio_docs, os.path.basename(guion_pdf)))
    if os.path.exists(guion_docx): shutil.copy(guion_docx, os.path.join(sitio_docs, os.path.basename(guion_docx)))
    if os.path.exists(guion_md): shutil.copy(guion_md, os.path.join(sitio_docs, os.path.basename(guion_md)))

    print("=== COMPILACIÓN, EMPAQUETADO Y DISTRIBUCIÓN FINALIZADOS CON ÉXITO ===")

if __name__ == "__main__":
    main()
