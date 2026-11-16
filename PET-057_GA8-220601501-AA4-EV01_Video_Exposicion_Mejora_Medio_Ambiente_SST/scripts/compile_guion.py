#!/usr/bin/env python3
# ==============================================================================
# COMPILADOR DE GUION TÉCNICO INDIVIDUAL (PDF / DOCX)
# Evidencia: GA8-220601501-AA4-EV01 - Oportunidades de Mejora Medio Ambiente y SST
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán
# ==============================================================================

import os
import shutil
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
ENTREGA_DIR = '/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA8-220601501-AA4-EV01'
ARTIFACT_DIR = '/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603'

os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(ENTREGA_DIR, exist_ok=True)

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Guion Técnico - Oportunidades de Mejora en Medio Ambiente y SST | Karen Campo</title>
  <style>
    @page {
      size: letter;
      margin: 1.2cm 1.4cm 1.2cm 1.4cm;
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
      font-size: 9pt;
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
      margin-bottom: 12px;
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
      font-size: 15pt;
      color: #0f172a;
      line-height: 1.2;
      margin-bottom: 8px;
      font-weight: 800;
    }
    h2.section-title {
      font-size: 11pt;
      color: #008C45;
      border-left: 4px solid #008C45;
      padding-left: 8px;
      margin-top: 12px;
      margin-bottom: 8px;
      font-weight: 700;
    }
    h3.sub-title {
      font-size: 9.5pt;
      color: #0f172a;
      margin-top: 8px;
      margin-bottom: 4px;
      font-weight: 700;
    }
    p {
      margin-bottom: 6px;
      text-align: justify;
    }

    .badge-box {
      display: flex;
      gap: 8px;
      margin-bottom: 12px;
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
      margin-bottom: 10px;
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

    table.script-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 8pt;
      margin-top: 6px;
      margin-bottom: 8px;
    }
    table.script-table th {
      background: #1e293b;
      color: white;
      padding: 5px 8px;
      text-align: left;
      font-weight: 700;
      font-size: 7.5pt;
      border: 1px solid #334155;
    }
    table.script-table td {
      border: 1px solid #cbd5e1;
      padding: 6px 8px;
      vertical-align: top;
      font-size: 7.5pt;
      line-height: 1.35;
    }
    table.script-table tr:nth-child(even) {
      background: #fbfcfe;
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

  <!-- PÁGINA 1: PREPRODUCCIÓN -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">SENA CTPI Popayán • Guion Técnico y Pedagógico Individual</div>
      <div class="header-meta">Evidencia: GA8-220601501-AA4-EV01 | Ficha: 3186681</div>
    </div>

    <h1 class="doc-title">GUION TÉCNICO Y STORYBOARD DE PRODUCCIÓN AUDIOVISUAL</h1>
    <p style="font-size: 9.5pt; color: #475569; margin-bottom: 8px;">
      <strong>Oportunidades de Mejora en Medio Ambiente y Seguridad y Salud en el Trabajo (SST) en el Contexto Productivo</strong>
    </p>

    <div class="badge-box">
      <span class="badge badge-green">Competencia: 220601501</span>
      <span class="badge">Actividad: GA8-220601501-AA4</span>
      <span class="badge">Aprendiz: Karen Yuliana Campo</span>
      <span class="badge">Programa: Tecnólogo en ADSO</span>
      <span class="badge">Duración: 08:30 min</span>
      <span class="badge">Resolución: 1080p Full HD</span>
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
          <th>Aprendiz Expositora:</th>
          <td>Karen Yuliana Campo</td>
          <th>Instrumento de Evaluación:</th>
          <td>IE-GA8-220601501-AA4-EV01</td>
        </tr>
        <tr>
          <th>Contextos Productivos:</th>
          <td>Entorno de Desarrollo de Software ADSO & Pizzería Gourmet Bella Italia Popayán</td>
          <th>Enfoque Metodológico:</th>
          <td>Ciclo PHVA (Planear, Hacer, Verificar, Actuar) + Normatividad Legal Colombiana</td>
        </tr>
      </table>
    </div>

    <h2 class="section-title">1. Fase de Preproducción Audiovisual</h2>
    <p>
      El presente guion técnico establece la planificación integral de la preproducción, producción y postproducción del video expositivo sobre oportunidades de mejora ambiental y de Seguridad y Salud en el Trabajo (SST). La evidencia se diseña bajo un <strong>estudio de casos reales</strong> articulando el entorno tecnológico del tecnólogo ADSO (cómputo intensivo, riesgos biomecánicos, fatiga visual, consumo energético y RAEE) y el entorno operativo gastronómico de la Pizzería Gourmet Bella Italia de Popayán (residuos orgánicos, grasas y aceites de cocina usados ACU, riesgo locativo y térmico).
    </p>

    <div class="callout-green">
      <strong>Pilares Normativos Ambientales Colombianos:</strong><br>
      • <strong>Res. 2184 de 2019:</strong> Código unificado de colores (Blanco: aprovechables; Verde: orgánicos; Negro: no aprovechables).<br>
      • <strong>Res. 316 de 2018:</strong> Manejo integral y entrega certificada de Aceites de Cocina Usados (ACU).<br>
      • <strong>Leyes 1715 de 2014 & 2099 de 2021:</strong> Eficiencia energética e incorporación de tecnologías LED y domótica.<br>
      • <strong>Ley 1672 de 2013:</strong> Gestión integral de Residuos de Aparatos Eléctricos y Electrónicos (RAEE).<br>
      • <strong>Ley 373 de 1997:</strong> Uso eficiente y ahorro del agua potable en instalaciones de servicios.
    </div>

    <div class="callout-blue">
      <strong>Pilares Normativos en Seguridad y Salud en el Trabajo (SST):</strong><br>
      • <strong>Decreto 1072 de 2015:</strong> SG-SST institucional y matriz de identificación de peligros.<br>
      • <strong>Guía Técnica GTC 45:</strong> Prevención de peligros biomecánicos y adecuación ergonómica del puesto de cómputo.<br>
      • <strong>Resolución 2400 de 1979:</strong> Estatuto de Seguridad Industrial, escaleras seguras y pisos antideslizantes.<br>
      • <strong>Norma Técnica NTC 2885 / NFPA 10:</strong> Extintores Clase K para cocinas y CO2/Solkaflam para centros de cómputo.<br>
      • <strong>Reglamento RETIE & Metodología 5S:</strong> Canalización ordenada de cableado y despeje de áreas de trabajo.<br>
      • <strong>Ley 2191 de 2022:</strong> Desconexión laboral y pausas activas programadas.
    </div>

    <h2 class="section-title">2. Ficha Técnica de Grabación y Especificaciones</h2>
    <table class="info-table">
      <tr>
        <th style="width: 25%;">Parámetro</th>
        <th style="width: 35%;">Especificación Técnica</th>
        <th style="width: 40%;">Justificación Pedagógica y Operativa</th>
      </tr>
      <tr>
        <td><strong>Formato de Video</strong></td>
        <td>MP4 (H.264 / MPEG-4 AVC) High Profile</td>
        <td>Máxima compatibilidad web, LMS Zajuna y dispositivos móviles.</td>
      </tr>
      <tr>
        <td><strong>Resolución / FPS</strong></td>
        <td>1920 × 1080 (Full HD 1080p) a 30 FPS progresivo</td>
        <td>Nitidez fotográfica para evidenciar los detalles de las mejoras reales.</td>
      </tr>
      <tr>
        <td><strong>Mezcla de Audio</strong></td>
        <td>Voz en off prioritaria + Ducking ambiental (-20 dB)</td>
        <td>Claridad del mensaje pedagógico de Karen Yuliana Campo con música de fondo sutil.</td>
      </tr>
      <tr>
        <td><strong>Recursos Fotográficos</strong></td>
        <td>10 imágenes reales de alta resolución</td>
        <td>Validación empírica en el contexto laboral de las 10 oportunidades propuestas.</td>
      </tr>
      <tr>
        <td><strong>Estructura</strong></td>
        <td>12 Bloques temáticos de ~42 a 45 segundos c/u</td>
        <td>Ritmo audiovisual dinámico, estructurado y de fácil comprensión.</td>
      </tr>
    </table>
  </div>

  <!-- PÁGINA 2: ESCALETA Y GUION PARTE 1 (BLOQUES 1 AL 6) -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">SENA CTPI Popayán • Fase de Producción: Escaleta y Guion Técnico</div>
      <div class="header-meta">Bloques 01 al 06 (Apertura y 5 Mejoras Ambientales)</div>
    </div>

    <h2 class="section-title" style="margin-top: 0;">2. Fase de Producción: Guion a Dos Columnas (Parte 1)</h2>

    <table class="script-table">
      <thead>
        <tr>
          <th style="width: 14%;">Bloque / Tiempo</th>
          <th style="width: 38%;">Video (Encuadres, Gráficos y Fotos Reales)</th>
          <th style="width: 48%;">Audio (Locución de Karen Yuliana Campo)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Bloque 01</strong><br>00:00 - 00:45<br><em>(45 seg)</em></td>
          <td><strong>Pantalla 01: Apertura Institucional</strong><br>• Logotipo animado del SENA y CTPI Popayán.<br>• Título: Oportunidades de Mejora en Medio Ambiente y SST.<br>• Ficha 3186681 - ADSO.<br>• Aprendiz: Karen Yuliana Campo.</td>
          <td>"Cordial saludo. Mi nombre es Karen Yuliana Campo, aprendiz del programa Tecnólogo en Análisis y Desarrollo de Software con ficha 3186681 del SENA CTPI Popayán, Regional Cauca. En esta oportunidad presento la evidencia GA8-220601501-AA4-EV01, exponiendo diez oportunidades concretas de mejora en gestión ambiental y en seguridad y salud en el trabajo, fundamentadas en el ciclo PHVA y en la normatividad colombiana. Acompáñenme a recorrer cómo la sostenibilidad y la protección del trabajador transforman nuestra productividad."</td>
        </tr>
        <tr>
          <td><strong>Bloque 02</strong><br>00:45 - 01:30<br><em>(45 seg)</em></td>
          <td><strong>Pantalla 02: Oportunidad Ambiental 01</strong><br>• <strong>Foto Real 01:</strong> Batería de canecas con código unificado de colores (Blanco: aprovechables, Verde: orgánicos, Negro: no aprovechables).<br>• Rótulo: <em>Res. 2184 de 2019 - Separación en la Fuente</em>.</td>
          <td>"Iniciamos con el bloque de Gestión Ambiental. Nuestra primera oportunidad de mejora es la separación estricta de residuos en la fuente mediante el código unificado de colores de la Resolución 2184 de 2019. Implementamos estaciones ecológicas compuestas por tres contenedores: blanco para residuos aprovechables limpios como papel, cartón y botellas plásticas; verde para orgánicos biodegradables; y negro para residuos ordinarios. Esta práctica minimiza la disposición final en rellenos sanitarios y fomenta la economía circular."</td>
        </tr>
        <tr>
          <td><strong>Bloque 03</strong><br>01:30 - 02:15<br><em>(45 seg)</em></td>
          <td><strong>Pantalla 03: Oportunidad Ambiental 02</strong><br>• <strong>Foto Real 02:</strong> Trampa de grasas industrial en acero inoxidable y caneca de almacenamiento de ACU rotulada.<br>• Rótulo: <em>Res. 316 de 2018 - Gestión Integral de ACU</em>.</td>
          <td>"Nuestra segunda oportunidad ambiental corresponde al manejo técnico de trampas de grasas y recolección certificada de Aceites de Cocina Usados (ACU), regulado por la Resolución 316 de 2018. Un solo litro de aceite vertido al sifón contamina hasta mil litros de agua potable y colapsa las redes de alcantarillado. La mejora consiste en instalar trampas de grasas con mantenimiento periódico y recolectar los aceites usados en bidones rotulados para su entrega exclusiva a gestores certificados que los transforman en biocombustibles."</td>
        </tr>
        <tr>
          <td><strong>Bloque 04</strong><br>02:15 - 03:00<br><em>(45 seg)</em></td>
          <td><strong>Pantalla 04: Oportunidad Ambiental 03</strong><br>• <strong>Foto Real 03:</strong> Luminarias LED de bajo consumo con sensores infrarrojos pasivos (PIR) de presencia.<br>• Rótulo: <em>Leyes 1715/2014 y 2099/2021 - Eficiencia Energética</em>.</td>
          <td>"La tercera oportunidad ambiental es la eficiencia energética mediante luminarias LED y automatización de consumo eléctrico, bajo las Leyes 1715 de 2014 y 2099 de 2021. Sustituimos lámparas convencionales por paneles LED de bajo consumo y larga vida útil, integrando sensores de movimiento infrarrojos en áreas comunes. En las estaciones de cómputo de desarrollo de software, establecemos directivas de suspensión automática de monitores tras diez minutos de inactividad, reduciendo drásticamente la huella de carbono."</td>
        </tr>
        <tr>
          <td><strong>Bloque 05</strong><br>03:00 - 03:45<br><em>(45 seg)</em></td>
          <td><strong>Pantalla 05: Oportunidad Ambiental 04</strong><br>• <strong>Foto Real 04:</strong> Contenedor institucional especializado para RAEE (tarjetas madre, memorias, periféricos y baterías).<br>• Rótulo: <em>Ley 1672 de 2013 - Gestión Posconsumo de RAEE</em>.</td>
          <td>"Como cuarta oportunidad ambiental en el entorno tecnológico, implementamos la gestión integral de Residuos de Aparatos Eléctricos y Electrónicos (RAEE), según la Ley 1672 de 2013. En el ciclo de vida del software y hardware descartamos tarjetas, periféricos y cables. La mejora radica en prohibir su desecho en basura común, canalizándolos mediante programas posconsumo y gestores de reciclaje autorizados para la recuperación de componentes, metales nobles y la correcta disposición de sustancias químicas peligrosas."</td>
        </tr>
        <tr>
          <td><strong>Bloque 06</strong><br>03:45 - 04:30<br><em>(45 seg)</em></td>
          <td><strong>Pantalla 06: Oportunidad Ambiental 05</strong><br>• <strong>Foto Real 05:</strong> Griferías con aireadores reductores de caudal e hidrómetros de control de fugas.<br>• Rótulo: <em>Ley 373 de 1997 - Uso Eficiente y Ahorro del Agua</em>.</td>
          <td>"Completando el bloque ambiental, la quinta oportunidad es el uso eficiente y ahorro del agua potable mediante tecnologías economizadoras, conforme a la Ley 373 de 1997. Instalamos aireadores en todas las griferías de lavamanos y áreas de preparación, reduciendo el caudal de doce a cuatro coma cinco litros por minuto mediante inyección de microburbujas de aire sin pérdida de confort, complementado con auditorías mensuales para detección temprana de fugas en tuberías y sanitarios."</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- PÁGINA 3: ESCALETA Y GUION PARTE 2 (BLOQUES 7 AL 12) -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">SENA CTPI Popayán • Fase de Producción: Escaleta y Guion Técnico</div>
      <div class="header-meta">Bloques 07 al 12 (5 Mejoras SST y Cierre Institucional)</div>
    </div>

    <h2 class="section-title" style="margin-top: 0;">2. Fase de Producción: Guion a Dos Columnas (Parte 2)</h2>

    <table class="script-table">
      <thead>
        <tr>
          <th style="width: 14%;">Bloque / Tiempo</th>
          <th style="width: 38%;">Video (Encuadres, Gráficos y Fotos Reales)</th>
          <th style="width: 48%;">Audio (Locución de Karen Yuliana Campo)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Bloque 07</strong><br>04:30 - 05:15<br><em>(45 seg)</em></td>
          <td><strong>Pantalla 07: Oportunidad SST 06</strong><br>• <strong>Foto Real 06:</strong> Puesto ergonómico ADSO con pantalla regulable a nivel de ojos, silla anatómica y apoyapiés.<br>• Rótulo: <em>GTC 45 / Dec. 1072/2015 - Ergonomía y Biomecánica</em>.</td>
          <td>"Pasamos al componente de Seguridad y Salud en el Trabajo. La sexta oportunidad es la adecuación ergonómica y antropométrica del puesto de cómputo para desarrolladores de software, bajo la Guía GTC 45 y Decreto 1072 de 2015. Al pasar jornadas prolongadas frente a pantallas, es vital ajustar monitores a la altura horizontal de la mirada, emplear sillas con soporte lumbar regulable y descansapiés que garanticen un ángulo de 90 grados en codos y rodillas, previniendo el síndrome del túnel carpiano y contracturas cervicales."</td>
        </tr>
        <tr>
          <td><strong>Bloque 08</strong><br>05:15 - 06:00<br><em>(45 seg)</em></td>
          <td><strong>Pantalla 08: Oportunidad SST 07</strong><br>• <strong>Foto Real 07:</strong> Gradas con cintas de carborundo fotoluminiscente antideslizante, pasamanos y piso rugoso.<br>• Rótulo: <em>Res. 2400 de 1979 - Seguridad Locativa y Prevención de Caídas</em>.</td>
          <td>"La séptima oportunidad en SST corresponde a la adecuación locativa de escaleras y superficies antideslizantes, bajo la Resolución 2400 de 1979. Tanto en escaleras de acceso como en cocinas y pasillos de tránsito frecuente, instalamos cintas antideslizantes fotoluminiscentes en las huellas de los peldaños, pasamanos dobles y pisos de alto coeficiente de fricción. Esta medida previene de raíz el factor de riesgo locativo más recurrente: los resbalones y caídas a nivel o desnivel."</td>
        </tr>
        <tr>
          <td><strong>Bloque 09</strong><br>06:00 - 06:45<br><em>(45 seg)</em></td>
          <td><strong>Pantalla 09: Oportunidad SST 08</strong><br>• <strong>Foto Real 08:</strong> Estación de extintores especializados: Clase K (acetato de potasio) y Solkaflam/CO2 para racks de servidores.<br>• Rótulo: <em>NTC 2885 / NFPA 10 - Protección Contra Incendios</em>.</td>
          <td>"Como octava oportunidad, abordamos la dotación técnica de extintores especializados Clase K y agentes limpios CO2/Solkaflam, según la Norma Técnica NTC 2885. En cocinas y freidoras se requiere extintores Clase K que sofocan fuegos de grasas mediante saponificación sin salpicaduras. En simultáneo, para salas de servidores y equipos informáticos disponemos de extintores de agente limpio que no conducen electricidad ni dejan residuos que dañen los circuitos, respaldados por inspección mensual."</td>
        </tr>
        <tr>
          <td><strong>Bloque 10</strong><br>06:45 - 07:30<br><em>(45 seg)</em></td>
          <td><strong>Pantalla 10: Oportunidad SST 09</strong><br>• <strong>Foto Real 09:</strong> Cableado estructurado en canaletas perimetrales ignífugas bajo norma RETIE y metodología 5S.<br>• Rótulo: <em>Metodología 5S y RETIE - Orden, Aseo y Riesgo Eléctrico</em>.</td>
          <td>"La novena oportunidad combina la metodología japonesa de las 5S con la canalización segura de cableado eléctrico y de telecomunicaciones bajo el reglamento RETIE. El desorden de cables sueltos en el piso representa un doble peligro: caídas para el personal y riesgo de sobrecalentamiento eléctrico. Mediante canaletas ranuradas ignífugas y una disciplina estricta de orden y despeje de vías de evacuación, logramos un entorno de trabajo limpio, seguro y altamente eficiente."</td>
        </tr>
        <tr>
          <td><strong>Bloque 11</strong><br>07:30 - 08:15<br><em>(45 seg)</em></td>
          <td><strong>Pantalla 11: Oportunidad SST 10</strong><br>• <strong>Foto Real 10:</strong> Equipo de trabajo realizando estiramientos osteomusculares guiados y software de notificación.<br>• Rótulo: <em>Ley 2191 de 2022 y Dec. 1072/2015 - Pausas Activas</em>.</td>
          <td>"Nuestra décima oportunidad de mejora en SST es el programa sistemático de pausas activas, higiene postural y desconexión laboral, conforme a la Ley 2191 de 2022. Establecemos dos descansos activos diarios obligatorios de diez minutos, a las diez de la mañana y a las tres y media de la tarde. Con ejercicios guiados de estiramiento de extremidades superiores, movilidad articular y descanso visual con la técnica 20-20-20, combatimos la fatiga neuromuscular y el estrés laboral."</td>
        </tr>
        <tr>
          <td><strong>Bloque 12</strong><br>08:15 - 09:00<br><em>(45 seg)</em></td>
          <td><strong>Pantalla 12: Conclusiones y Cierre</strong><br>• Diagrama síntesis del Ciclo PHVA.<br>• Cuadro de beneficios cuantitativos y cumplimiento de ODS.<br>• Créditos finales: Karen Yuliana Campo, SENA CTPI Popayán.</td>
          <td>"En conclusión, implementar estas diez oportunidades de mejora en medio ambiente y SST bajo el ciclo PHVA no solo asegura el cumplimiento de la normatividad colombiana, sino que salva vidas, previene enfermedades laborales y preserva los recursos naturales de nuestra comunidad. Agradezco a los instructores del SENA y a mis compañeros del CTPI Popayán por fortalecer nuestras competencias integrales como desarrolladores de software al servicio del país. ¡Muchas gracias!"</td>
        </tr>
      </tbody>
    </table>

    <h2 class="section-title">3. Fase de Postproducción y Especificaciones Finales</h2>
    <div class="card" style="margin-bottom: 0;">
      <p style="font-size: 8pt; margin-bottom: 4px;">
        <strong>Parámetros de Edición NLE, Mezcla y Renderizado:</strong><br>
        • <strong>Edición y Montaje:</strong> FilmCraft CLI y suite FFmpeg con pipeline de renderizado H.264 High Profile (CRF 22, 4500 kbps) y audio AAC estéreo 320 kbps a 48 kHz.<br>
        • <strong>Ducking Automático:</strong> Filtro <code>sidechaincompress</code> que atenúa la música ambiental (-20 dB) automáticamente al detectar presencia de la señal vocal principal.<br>
        • <strong>Despliegue Contenerizado:</strong> Portal web responsive interactivo alojado en servidor Docker Apache HTTPD (puerto 8105) con reproductor HTML5, galería fotográfica y visor de datos JSON.<br>
        • <strong>Validación Académica:</strong> Aprobación bajo la rúbrica del instrumento de evaluación IE-GA8-220601501-AA4-EV01.
      </p>
      <div style="margin-top: 8px; border-top: 1px solid #cbd5e1; padding-top: 6px; font-size: 7.5pt; color: #64748b; display: flex; justify-content: space-between;">
        <div><strong>Aprendiz:</strong> Karen Yuliana Campo — Ficha 3186681 (ADSO)</div>
        <div><strong>Institución:</strong> SENA Regional Cauca — CTPI Popayán</div>
      </div>
    </div>
  </div>

</body>
</html>
"""

html_temp_path = os.path.join(DOCS_DIR, 'temp_guion_print.html')
pdf_output_path = os.path.join(DOCS_DIR, 'GA8-220601501-AA4-EV01_Guion_Video_Exposicion_Mejora_Medio_Ambiente_SST.pdf')
docx_output_path = os.path.join(DOCS_DIR, 'GA8-220601501-AA4-EV01_Guion_Video_Exposicion_Mejora_Medio_Ambiente_SST.docx')

def main():
    print("=== COMPILANDO GUION TÉCNICO INDIVIDUAL (PDF Y DOCX) ===")
    with open(html_temp_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    # 1. Compile PDF with headless chrome
    print("Compilando PDF de Guion Técnico...")
    subprocess.run([
        "google-chrome",
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_output_path}",
        html_temp_path
    ], check=True)
    pdf_size_kb = os.path.getsize(pdf_output_path) / 1024
    print(f"[OK] PDF Guion generado: {pdf_output_path} ({pdf_size_kb:.1f} KB)")

    # 2. Compile DOCX via LibreOffice (HTML -> ODT -> DOCX)
    print("Compilando DOCX de Guion Técnico...")
    subprocess.run([
        "libreoffice", "--headless",
        "--convert-to", "odt:writer8",
        html_temp_path,
        "--outdir", DOCS_DIR
    ], check=True)
    temp_odt = os.path.join(DOCS_DIR, 'temp_guion_print.odt')
    subprocess.run([
        "libreoffice", "--headless",
        "--convert-to", "docx:MS Word 2007 XML",
        temp_odt,
        "--outdir", DOCS_DIR
    ], check=True)
    temp_docx = os.path.join(DOCS_DIR, 'temp_guion_print.docx')
    if os.path.exists(temp_docx):
        shutil.move(temp_docx, docx_output_path)
    if os.path.exists(temp_odt):
        os.remove(temp_odt)
    if os.path.exists(html_temp_path):
        os.remove(html_temp_path)

    docx_size_kb = os.path.getsize(docx_output_path) / 1024
    print(f"[OK] DOCX Guion generado: {docx_output_path} ({docx_size_kb:.1f} KB)")

    # 3. Distribute to Zajuna and Brain
    shutil.copy(pdf_output_path, ENTREGA_DIR)
    shutil.copy(docx_output_path, ENTREGA_DIR)
    shutil.copy(pdf_output_path, ARTIFACT_DIR)
    shutil.copy(docx_output_path, ARTIFACT_DIR)

    # Also copy markdown
    md_guion = os.path.join(DOCS_DIR, 'GUION_TECNICO_VIDEO_EXPOSICION_MEJORA_MEDIO_AMBIENTE_SST.md')
    if os.path.exists(md_guion):
        shutil.copy(md_guion, ENTREGA_DIR)
        shutil.copy(md_guion, ARTIFACT_DIR)

    print("=== GUION TÉCNICO INDIVIDUAL COMPILADO Y DISTRIBUIDO EXITOSAMENTE ===")

if __name__ == '__main__':
    main()
