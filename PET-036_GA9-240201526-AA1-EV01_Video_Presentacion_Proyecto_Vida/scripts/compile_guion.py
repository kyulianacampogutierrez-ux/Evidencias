#!/usr/bin/env python3
# ==============================================================================
# COMPILADOR DE GUION TÉCNICO INDIVIDUAL (PDF / DOCX)
# Evidencia: GA9-240201526-AA1-EV01 - Presentación del Proyecto de Vida
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán
# Competencia: 240201526 - Ética y Cultura de Paz
# ==============================================================================

import os
import shutil
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
ENTREGA_DIR = '/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA9-240201526-AA1-EV01'
ARTIFACT_DIR = '/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603'

os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(ENTREGA_DIR, exist_ok=True)

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Guion Técnico - Presentación Proyecto de Vida | Karen Campo</title>
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
      font-size: 8.8pt;
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

    .cover-card {
      background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
      color: white;
      padding: 24px;
      border-radius: 8px;
      border-left: 6px solid #008C45;
      margin-bottom: 16px;
    }
    .cover-badge {
      display: inline-block;
      background: #008C45;
      color: white;
      font-size: 7.5pt;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
    }
    .cover-title {
      font-size: 17pt;
      font-weight: 800;
      line-height: 1.2;
      margin-bottom: 6px;
    }
    .cover-subtitle {
      font-size: 10pt;
      color: #cbd5e1;
      margin-bottom: 14px;
    }
    .cover-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
      border-top: 1px solid rgba(255,255,255,0.15);
      padding-top: 12px;
      font-size: 7.5pt;
    }
    .cover-grid-item strong {
      display: block;
      color: #38bdf8;
      text-transform: uppercase;
      font-size: 6.8pt;
      margin-bottom: 2px;
    }

    h2 {
      font-size: 11pt;
      color: #0f172a;
      border-left: 4px solid #008C45;
      padding-left: 8px;
      margin: 12px 0 8px 0;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .table-tech {
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 14px;
      font-size: 8pt;
    }
    .table-tech th, .table-tech td {
      border: 1px solid #cbd5e1;
      padding: 5px 8px;
      text-align: left;
    }
    .table-tech th {
      background: #f1f5f9;
      color: #0f172a;
      font-weight: 700;
      width: 25%;
    }

    .scene-card {
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      margin-bottom: 12px;
      overflow: hidden;
      background: #ffffff;
      box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    }
    .scene-header {
      background: #f8fafc;
      border-bottom: 1px solid #e2e8f0;
      padding: 7px 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .scene-id {
      font-weight: 800;
      color: #0f172a;
      font-size: 8.5pt;
    }
    .scene-time {
      background: #e2e8f0;
      color: #334155;
      padding: 2px 6px;
      border-radius: 4px;
      font-weight: 700;
      font-size: 7.5pt;
      font-family: monospace;
    }
    .scene-body {
      padding: 9px 12px;
      display: grid;
      grid-template-columns: 1fr 1.6fr;
      gap: 12px;
    }
    .scene-tech {
      border-right: 1px solid #f1f5f9;
      padding-right: 10px;
    }
    .tech-item {
      margin-bottom: 6px;
    }
    .tech-label {
      font-size: 7pt;
      font-weight: 700;
      color: #008C45;
      text-transform: uppercase;
      letter-spacing: 0.4px;
      display: block;
    }
    .tech-val {
      font-size: 7.8pt;
      color: #334155;
    }
    .scene-voice {
      background: #f0fdf4;
      border: 1px solid #dcfce7;
      border-left: 3px solid #16a34a;
      padding: 8px 10px;
      border-radius: 4px;
    }
    .voice-label {
      font-size: 7.2pt;
      font-weight: 800;
      color: #15803d;
      text-transform: uppercase;
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .voice-text {
      font-size: 8.3pt;
      color: #14532d;
      font-style: italic;
      line-height: 1.45;
    }

    .ikigai-box {
      background: #faf5ff;
      border: 1px solid #e9d5ff;
      border-left: 4px solid #9333ea;
      padding: 10px;
      border-radius: 6px;
      margin: 10px 0;
    }
    .ikigai-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 8px;
      margin-top: 6px;
      font-size: 7.5pt;
    }
    .ikigai-item {
      background: white;
      padding: 6px;
      border-radius: 4px;
      border: 1px solid #f3e8ff;
    }
    .ikigai-item strong {
      color: #7e22ce;
      display: block;
      font-size: 7pt;
      text-transform: uppercase;
    }

    .dofa-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      margin: 8px 0;
      font-size: 7.5pt;
    }
    .dofa-card {
      padding: 7px;
      border-radius: 4px;
      border: 1px solid #e2e8f0;
    }
    .dofa-f { background: #f0fdf4; border-left: 3px solid #22c55e; }
    .dofa-d { background: #fef2f2; border-left: 3px solid #ef4444; }
    .dofa-o { background: #eff6ff; border-left: 3px solid #3b82f6; }
    .dofa-a { background: #fffbeb; border-left: 3px solid #f59e0b; }
    .dofa-card strong { display: block; font-size: 7pt; text-transform: uppercase; margin-bottom: 2px; }

    .footer-note {
      font-size: 7pt;
      color: #64748b;
      text-align: center;
      margin-top: 12px;
      border-top: 1px solid #e2e8f0;
      padding-top: 6px;
    }
  </style>
</head>
<body>

  <!-- PÁGINA 1: PORTADA Y FICHA TÉCNICA -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">SENA • CENTRO DE TELEINFORMÁTICA Y PRODUCCIÓN INDUSTRIAL (CTPI)</div>
      <div class="header-meta">ADSO • FICHA 3186681 | POPAYÁN, CAUCA</div>
    </div>

    <div class="cover-card">
      <div class="cover-badge">Guion Técnico y Literario Oficial</div>
      <div class="cover-title">Mi Proyecto de Vida: Tecnología, Propósito y Cultura de Paz</div>
      <div class="cover-subtitle">Evidencia GA9-240201526-AA1-EV01 • Presentación del Proyecto de Vida</div>
      <div class="cover-grid">
        <div class="cover-grid-item">
          <strong>Aprendiz</strong>
          Karen Yuliana Campo
        </div>
        <div class="cover-grid-item">
          <strong>Programa</strong>
          Tecnólogo en ADSO
        </div>
        <div class="cover-grid-item">
          <strong>Competencia</strong>
          240201526 Ética y Paz
        </div>
        <div class="cover-grid-item">
          <strong>Duración Video</strong>
          4:50 min (Máx 6:00 min)
        </div>
      </div>
    </div>

    <h2>1. Ficha Técnica de Producción Audiovisual</h2>
    <table class="table-tech">
      <tr>
        <th>Título del Video</th>
        <td><em>Mi Proyecto de Vida: Tecnología, Propósito y Cultura de Paz</em></td>
      </tr>
      <tr>
        <th>Aprendiz / Locutora</th>
        <td><strong>Karen Yuliana Campo</strong> (C.C. / Ficha 3186681)</td>
      </tr>
      <tr>
        <th>Estructura Metodológica</th>
        <td>6 Niveles Neurológicos de Robert Dilts + Esquema Ikigai + Matriz DOFA + Reflexión ética de Malala Yousafzai</td>
      </tr>
      <tr>
        <th>Formato y Resolución</th>
        <td>1920 × 1080 Full HD (16:9), MP4 (H.264 / AAC 48kHz estéreo), Enlace institucional YouTube</td>
      </tr>
      <tr>
        <th>Música y Sonido</th>
        <td>Pista instrumental acústica/cinemática suave a -26 dB con compresión ducking automática frente a la voz principal</td>
      </tr>
      <tr>
        <th>Público Objetivo</th>
        <td>Comunidad académica SENA, instructores de ética, evaluadores Zajuna y sociedad caucana</td>
      </tr>
    </table>

    <h2>2. Esquema Integrador: Ikigai Personal de Karen Campo</h2>
    <div class="ikigai-box">
      <p style="font-size: 7.8pt; color: #581c87; font-weight: 700; margin-bottom: 4px;">
        CONVERGENCIA DE PROPÓSITO: TECNOLOGÍA HUMANISTA AL SERVICIO DE LA CULTURA DE PAZ
      </p>
      <div class="ikigai-grid">
        <div class="ikigai-item">
          <strong>1. Lo que amo</strong>
          Aprender continuamente, programar soluciones lógicas, el arte y crear proyectos con impacto social.
        </div>
        <div class="ikigai-item">
          <strong>2. En lo que soy buena</strong>
          Pensamiento analítico, arquitectura de datos, empatía humana, escucha activa y resiliencia.
        </div>
        <div class="ikigai-item">
          <strong>3. Lo que el mundo necesita</strong>
          Educación accesible, cierre de brechas de género en STEM, ética digital y cultura de paz en Colombia.
        </div>
        <div class="ikigai-item">
          <strong>4. Por lo que me pagarán</strong>
          Desarrollo de software frontend/backend, control de calidad, aseguramiento y desarrollo web profesional.
        </div>
      </div>
    </div>

    <h2>3. Matriz DOFA Personal (Autodiagnóstico Nivel 4)</h2>
    <div class="dofa-grid">
      <div class="dofa-card dofa-f">
        <strong style="color: #15803d;">Fortalezas (F)</strong>
        Disciplina académica, pensamiento lógico estructurado, vocación de servicio, empatía comunicativa y adaptabilidad al cambio.
      </div>
      <div class="dofa-card dofa-d">
        <strong style="color: #b91c1c;">Debilidades (D)</strong>
        Autoexigencia desmedida ante plazos críticos y sobrecarga mental (mitigada con técnicas Pomodoro y pausas activas).
      </div>
      <div class="dofa-card dofa-o">
        <strong style="color: #1d4ed8;">Oportunidades (O)</strong>
        Alta empleabilidad en software, ecosistema de innovación CTPI Popayán, certificaciones cloud y proyectos sociales.
      </div>
      <div class="dofa-card dofa-a">
        <strong style="color: #b45309;">Amenazas (A)</strong>
        Brechas de conectividad en la región y acelerada obsolescencia tecnológica (superadas con estudio autónomo continuo).
      </div>
    </div>
  </div>

  <!-- PÁGINA 2: ESCENAS 01 A 04 -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">GUION TÉCNICO ESCENA POR ESCENA • PARTE 1</div>
      <div class="header-meta">GA9-240201526-AA1-EV01 | KAREN YULIANA CAMPO</div>
    </div>

    <!-- ESCENA 01 -->
    <div class="scene-card">
      <div class="scene-header">
        <span class="scene-id">ESCENA 01: Apertura Institucional y Presentación Personal</span>
        <span class="scene-time">00:00 - 00:35 (35 seg)</span>
      </div>
      <div class="scene-body">
        <div class="scene-tech">
          <div class="tech-item">
            <span class="tech-label">Plano y Cámara</span>
            <span class="tech-val">Plano Medio Frontal (Medium Shot). Luz suave, Karen sonriente y empática.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Elementos Visuales</span>
            <span class="tech-val">Logo SENA CTPI, Zócalo inferior: Karen Yuliana Campo • Aprendiz ADSO Ficha 3186681.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Foto Sugerida</span>
            <span class="tech-val">Foto personal 1: Retrato nítido sonriendo en ambiente de estudio o cotidiano.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Ambiente Sonoro</span>
            <span class="tech-val">Acordes de guitarra acústica y piano suave en fade-in (ducking a -26 dB).</span>
          </div>
        </div>
        <div class="scene-voice">
          <div class="voice-label">🎙️ Locución Karen Yuliana Campo:</div>
          <div class="voice-text">
            "¡Hola a todos! Mi nombre es Karen Yuliana Campo. Soy aprendiz de la tecnología en Análisis y Desarrollo de Software en el Centro de Teleinformática y Producción Industrial, CTPI del SENA, en la hermosa ciudad de Popayán.<br><br>
            Hoy quiero compartir con ustedes mi Proyecto de Vida: una construcción consciente que nace desde lo más íntimo de mis valores, mis raíces familiares y mi formación tecnológica, con el propósito de aportar al desarrollo humano, a la convivencia armónica y a una auténtica cultura de paz."
          </div>
        </div>
      </div>
    </div>

    <!-- ESCENA 02 -->
    <div class="scene-card">
      <div class="scene-header">
        <span class="scene-id">ESCENA 02: Inspiración Ética — La Voz de Malala y la Cultura de Paz</span>
        <span class="scene-time">00:35 - 01:10 (35 seg)</span>
      </div>
      <div class="scene-body">
        <div class="scene-tech">
          <div class="tech-item">
            <span class="tech-label">Plano y Cámara</span>
            <span class="tech-val">Plano medio corto alternado con infografía de Malala Yousafzai y UNESCO.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Elementos Visuales</span>
            <span class="tech-val">Palabras flotantes: Resiliencia, Educación, Igualdad, Cultura de Paz. Pregunta guía en pantalla.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Ambiente Sonoro</span>
            <span class="tech-val">Piano emotivo y cinematográfico, transmitiendo reflexión y esperanza.</span>
          </div>
        </div>
        <div class="scene-voice">
          <div class="voice-label">🎙️ Locución Karen Yuliana Campo:</div>
          <div class="voice-text">
            "Al reflexionar sobre la historia de Malala Yousafzai y su valiente lucha por el derecho a la educación de las niñas, surge una pregunta que transforma cualquier proyecto de vida: Si me dieran la palabra... ¿qué le diría al mundo para hacerlo un lugar mejor?<br><br>
            Yo le diría al mundo que la educación, la empatía y la tecnología no son privilegios, sino puentes para sanar brechas sociales. Que construir paz no es solo silenciar las armas, sino garantizar que cada niña, joven y mujer tenga la oportunidad de soñar, educarse y escribir su propia historia con dignidad y libertad."
          </div>
        </div>
      </div>
    </div>

    <!-- ESCENA 03 -->
    <div class="scene-card">
      <div class="scene-header">
        <span class="scene-id">ESCENA 03: Nivel 1 — Identidad Trascendente (Espiritualidad y Sentido)</span>
        <span class="scene-time">01:10 - 01:45 (35 seg)</span>
      </div>
      <div class="scene-body">
        <div class="scene-tech">
          <div class="tech-item">
            <span class="tech-label">Plano y Cámara</span>
            <span class="tech-val">Plano detalle con fondo translúcido y gráfico del Nivel 1 de Dilts.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Elementos Visuales</span>
            <span class="tech-val">Íconos de gratitud y trascendencia. Tarjeta: Fe, Servicio y Propósito Superior.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Ambiente Sonoro</span>
            <span class="tech-val">Cuerdas y atmósfera suave y contemplativa.</span>
          </div>
        </div>
        <div class="scene-voice">
          <div class="voice-label">🎙️ Locución Karen Yuliana Campo:</div>
          <div class="voice-text">
            "Comenzando por el primer nivel de mi proyecto: mi Identidad Trascendente. Ante Dios y ante la inmensidad del universo, me reconozco como un ser bendecido, creado con un propósito de amor, servicio y aprendizaje constante.<br><br>
            Mi espiritualidad se expresa en la gratitud diaria: en la forma como cuido a los seres que me rodean, en la honestidad con la que enfrento cada reto y en la convicción de que estamos aquí para ser instrumentos de bien. Me siento invitada a no pasar indiferente ante el dolor ajeno, sino a retribuir con generosidad las oportunidades que la vida me brinda."
          </div>
        </div>
      </div>
    </div>

    <!-- ESCENA 04 -->
    <div class="scene-card">
      <div class="scene-header">
        <span class="scene-id">ESCENA 04: Nivel 2 — Identidad, Roles, Misión y Visión Personal</span>
        <span class="scene-time">01:45 - 02:25 (40 seg)</span>
      </div>
      <div class="scene-body">
        <div class="scene-tech">
          <div class="tech-item">
            <span class="tech-label">Plano y Cámara</span>
            <span class="tech-val">Plano medio en Split-Screen mostrando infografía de Roles y Misión/Visión.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Elementos Visuales</span>
            <span class="tech-val">Infografía de roles: Hija, Mujer, Aprendiz ADSO, Ciudadana constructora de paz.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Foto Sugerida</span>
            <span class="tech-val">Foto personal 2: Karen programando en computador o en un ambiente del SENA CTPI.</span>
          </div>
        </div>
        <div class="scene-voice">
          <div class="voice-label">🎙️ Locución Karen Yuliana Campo:</div>
          <div class="voice-text">
            "En el segundo nivel, defino quién soy hoy y quién elijo ser. Soy Karen Yuliana: una joven caucana, hija comprometida, mujer resiliente y aprendiz apasionada del desarrollo de software.<br><br>
            Mi misión personal es transformar realidades a través del código: diseñando sistemas informáticos eficientes, seguros y accesibles que mejoren la calidad de vida de las personas y fortalezcan el tejido productivo de nuestra región.<br><br>
            Mi visión a cinco años es consolidarme como una ingeniera de software íntegra, liderando proyectos de innovación digital con enfoque social, inspirando a más mujeres a incursionar en el mundo de la tecnología."
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- PÁGINA 3: ESCENAS 05 A 08 Y CIERRE -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">GUION TÉCNICO ESCENA POR ESCENA • PARTE 2</div>
      <div class="header-meta">GA9-240201526-AA1-EV01 | KAREN YULIANA CAMPO</div>
    </div>

    <!-- ESCENA 05 -->
    <div class="scene-card">
      <div class="scene-header">
        <span class="scene-id">ESCENA 05: Nivel 3 — Valores, Creencias y Actitudes para la Convivencia</span>
        <span class="scene-time">02:25 - 03:00 (35 seg)</span>
      </div>
      <div class="scene-body">
        <div class="scene-tech">
          <div class="tech-item">
            <span class="tech-label">Plano y Cámara</span>
            <span class="tech-val">Primer plano expresivo (Close-up) alternado con tarjetas de valores en 3D.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Elementos Visuales</span>
            <span class="tech-val">Tarjetas: Integridad, Perseverancia, Empatía, Solidaridad y Respeto a la Dignidad.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Ambiente Sonoro</span>
            <span class="tech-val">Ritmo instrumental inspirador y constante, tono afirmativo.</span>
          </div>
        </div>
        <div class="scene-voice">
          <div class="voice-label">🎙️ Locución Karen Yuliana Campo:</div>
          <div class="voice-text">
            "Mis acciones están guiadas por cuatro valores cardinales: la integridad, la perseverancia, la empatía y la solidaridad.<br><br>
            He decidido asumir ante la vida una actitud proactiva y receptiva. Elijo transformar creencias limitantes —como el temor a equivocarse— en la certeza de que cada desafío es una lección de crecimiento. Creo firmemente que la ética no se negocia: ni en las decisiones cotidianas, ni en las líneas de código que gobiernan los sistemas que usamos todos los días."
          </div>
        </div>
      </div>
    </div>

    <!-- ESCENA 06 -->
    <div class="scene-card">
      <div class="scene-header">
        <span class="scene-id">ESCENA 06: Nivel 4 — Capacidades, Habilidades y Matriz DOFA Personal</span>
        <span class="scene-time">03:00 - 03:40 (40 seg)</span>
      </div>
      <div class="scene-body">
        <div class="scene-tech">
          <div class="tech-item">
            <span class="tech-label">Plano y Cámara</span>
            <span class="tech-val">Infografía animada de la Matriz DOFA con Picture-in-Picture de Karen.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Elementos Visuales</span>
            <span class="tech-val">Cuadrante DOFA resaltando Fortalezas en ADSO y Estrategias de mejora.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Foto Sugerida</span>
            <span class="tech-val">Foto personal 3: Karen en sustentación académica, taller o trabajo en equipo.</span>
          </div>
        </div>
        <div class="scene-voice">
          <div class="voice-label">🎙️ Locución Karen Yuliana Campo:</div>
          <div class="voice-text">
            "En el cuarto nivel evalué mis capacidades mediante una matriz DOFA consciente.<br><br>
            Mis mayores fortalezas son el pensamiento analítico, la capacidad de estructurar soluciones lógicas y la empatía para trabajar en equipo. Con disciplina en el SENA he cultivado habilidades en desarrollo frontend, arquitecturas backend, pruebas de software y bases de datos.<br><br>
            Reconozco también mis áreas de mejora: a veces me exijo demasiado ante los plazos ajustados, por lo que he adoptado técnicas de gestión del tiempo y pausas activas para cuidar mi bienestar mental y físico."
          </div>
        </div>
      </div>
    </div>

    <!-- ESCENA 07 -->
    <div class="scene-card">
      <div class="scene-header">
        <span class="scene-id">ESCENA 07: Niveles 5 y 6 — Acciones Cotidianas, Convivencia y Medio Ambiente</span>
        <span class="scene-time">03:40 - 04:15 (35 seg)</span>
      </div>
      <div class="scene-body">
        <div class="scene-tech">
          <div class="tech-item">
            <span class="tech-label">Plano y Cámara</span>
            <span class="tech-val">Plano medio alternado con imágenes cálidas de Popayán, naturaleza y familia.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Elementos Visuales</span>
            <span class="tech-val">Gráfico de hábitos diarios: Comunicación asertiva, estudio ético, cuidado ambiental.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Fotos Sugeridas</span>
            <span class="tech-val">Foto 4: Con la familia o seres queridos. Foto 5: En un paisaje de Popayán/Cauca.</span>
          </div>
        </div>
        <div class="scene-voice">
          <div class="voice-label">🎙️ Locución Karen Yuliana Campo:</div>
          <div class="voice-text">
            "En mi vida cotidiana —niveles 5 y 6— el proyecto de vida se traduce en hábitos concretos: madrugar con gratitud, practicar una comunicación asertiva y libre de violencia en mi hogar y con mis compañeros, y dedicar tiempo de calidad a quienes amo.<br><br>
            Quiero estar en mi comunidad de Popayán, conviviendo con personas que sumen y compartan valores de progreso. Y con el medio ambiente, mi compromiso es activo: separando residuos desde la fuente, ahorrando energía en mis equipos de cómputo y promoviendo un consumo consciente y responsable."
          </div>
        </div>
      </div>
    </div>

    <!-- ESCENA 08 -->
    <div class="scene-card">
      <div class="scene-header">
        <span class="scene-id">ESCENA 08: El Ikigai de Karen y Conclusión — Cultura de Paz al Mundo</span>
        <span class="scene-time">04:15 - 04:50 (35 seg)</span>
      </div>
      <div class="scene-body">
        <div class="scene-tech">
          <div class="tech-item">
            <span class="tech-label">Plano y Cámara</span>
            <span class="tech-val">Medium Close-up de Karen mirando a cámara con convicción, convergencia Ikigai en fondo.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Elementos Visuales</span>
            <span class="tech-val">Diagrama de Venn Ikigai convergiendo en Tecnología Humanista. Placa final SENA CTPI.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Ambiente Sonoro</span>
            <span class="tech-val">Clímax musical inspirador con crescendo suave y fade-out cálido al despedirse.</span>
          </div>
        </div>
        <div class="scene-voice">
          <div class="voice-label">🎙️ Locución Karen Yuliana Campo:</div>
          <div class="voice-text">
            "Al integrar todo esto en mi IKIGAI o razón de ser, descubro que mi verdadera vocación es hacer de la tecnología un vehículo de humanismo. Uniendo lo que amo, en lo que soy buena, lo que el mundo necesita y mi profesión como tecnóloga ADSO.<br><br>
            Mi proyecto de vida es mi compromiso vivo con Colombia: demostrar que cada línea de código, cada palabra de aliento y cada acción honesta son semillas para sembrar la paz que todos anhelamos.<br><br>
            ¡Muchas gracias!"
          </div>
        </div>
      </div>
    </div>

    <div class="footer-note">
      SENA Regional Cauca • CTPI Popayán | Tecnólogo en Análisis y Desarrollo de Software (ADSO) • Ficha 3186681<br>
      Evidencia: GA9-240201526-AA1-EV01: Presentación del Proyecto de Vida | Aprendiz: Karen Yuliana Campo
    </div>
  </div>

</body>
</html>
"""

def main():
    print("=== INICIANDO COMPILACIÓN DE GUION TÉCNICO FORMAL (PDF Y DOCX) ===")
    print("Evidencia: GA9-240201526-AA1-EV01 | Aprendiz: Karen Yuliana Campo")

    html_temp_path = os.path.join(DOCS_DIR, 'temp_guion_print.html')
    pdf_output_path = os.path.join(DOCS_DIR, 'GA9-240201526-AA1-EV01_Guion_Video_Presentacion_Proyecto_Vida.pdf')
    docx_output_path = os.path.join(DOCS_DIR, 'GA9-240201526-AA1-EV01_Guion_Video_Presentacion_Proyecto_Vida.docx')

    with open(html_temp_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    # 1. Compile PDF via Chrome Headless
    print(f"Compilando PDF en: {pdf_output_path}...")
    subprocess.run([
        "google-chrome",
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_output_path}",
        html_temp_path
    ], check=True)
    pdf_sz = os.path.getsize(pdf_output_path) / 1024
    print(f"[OK] PDF Guion generado: {pdf_output_path} ({pdf_sz:.1f} KB)")

    # 2. Compile DOCX via LibreOffice
    print(f"Compilando DOCX en: {docx_output_path}...")
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

    docx_sz = os.path.getsize(docx_output_path) / 1024
    print(f"[OK] DOCX Guion generado: {docx_output_path} ({docx_sz:.1f} KB)")

    # 3. Distribution to Zajuna delivery folder and Brain artifacts
    shutil.copy(pdf_output_path, ENTREGA_DIR)
    shutil.copy(docx_output_path, ENTREGA_DIR)
    shutil.copy(pdf_output_path, ARTIFACT_DIR)
    shutil.copy(docx_output_path, ARTIFACT_DIR)

    md_source = os.path.join(DOCS_DIR, 'GUION_TECNICO_VIDEO_PRESENTACION_PROYECTO_VIDA.md')
    if os.path.exists(md_source):
        shutil.copy(md_source, ENTREGA_DIR)
        shutil.copy(md_source, ARTIFACT_DIR)

    print("=== GUION TÉCNICO FORMAL COMPILADO Y DISTRIBUIDO EXITOSAMENTE ===")

if __name__ == '__main__':
    main()
