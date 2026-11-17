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
IMG_DIR = os.path.join(BASE_DIR, 'imagenes')
ENTREGA_DIR = '/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA9-240201526-AA1-EV01'
ARTIFACT_DIR = '/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603'

os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(ENTREGA_DIR, exist_ok=True)

# Rutas de fotos
p_foto1 = os.path.join(IMG_DIR, '01_foto_karen_yuliana_campo_retrato.jpg')
p_foto2 = os.path.join(IMG_DIR, '02_foto_familia_mama_hermano_karen.jpg')
p_foto3 = os.path.join(IMG_DIR, '03_foto_pareja_mascotas_karen.jpg')

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Guion Técnico - Presentación Proyecto de Vida | Karen Campo</title>
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
      line-height: 1.45;
      font-size: 8.6pt;
    }}
    .page {{
      page-break-after: always;
      position: relative;
    }}
    .page:last-child {{
      page-break-after: avoid;
    }}

    .header-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid #008C45;
      padding-bottom: 5px;
      margin-bottom: 10px;
    }}
    .header-title {{
      font-size: 7.8pt;
      font-weight: 700;
      color: #008C45;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .header-meta {{
      font-size: 7.2pt;
      color: #64748b;
      text-align: right;
    }}

    .cover-card {{
      background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
      color: white;
      padding: 18px 22px;
      border-radius: 8px;
      border-left: 6px solid #008C45;
      margin-bottom: 12px;
    }}
    .cover-badge {{
      display: inline-block;
      background: #008C45;
      color: white;
      font-size: 7.2pt;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 6px;
    }}
    .cover-title {{
      font-size: 15.5pt;
      font-weight: 800;
      line-height: 1.2;
      margin-bottom: 4px;
    }}
    .cover-subtitle {{
      font-size: 9.5pt;
      color: #cbd5e1;
      margin-bottom: 10px;
    }}
    .cover-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 8px;
      border-top: 1px solid rgba(255,255,255,0.15);
      padding-top: 8px;
      font-size: 7.2pt;
    }}
    .cover-grid-item strong {{
      display: block;
      color: #38bdf8;
      text-transform: uppercase;
      font-size: 6.5pt;
      margin-bottom: 1px;
    }}

    h2 {{
      font-size: 10.5pt;
      color: #0f172a;
      border-left: 4px solid #008C45;
      padding-left: 7px;
      margin: 10px 0 6px 0;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .table-tech {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 10px;
      font-size: 7.8pt;
    }}
    .table-tech th, .table-tech td {{
      border: 1px solid #cbd5e1;
      padding: 4px 7px;
      text-align: left;
    }}
    .table-tech th {{
      background: #f1f5f9;
      color: #0f172a;
      font-weight: 700;
      width: 26%;
    }}

    .scene-card {{
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      margin-bottom: 10px;
      overflow: hidden;
      background: #ffffff;
      box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    }}
    .scene-header {{
      background: #f8fafc;
      border-bottom: 1px solid #e2e8f0;
      padding: 6px 10px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .scene-id {{
      font-weight: 800;
      color: #0f172a;
      font-size: 8.2pt;
    }}
    .scene-time {{
      background: #e2e8f0;
      color: #334155;
      padding: 1px 5px;
      border-radius: 4px;
      font-weight: 700;
      font-size: 7.2pt;
      font-family: monospace;
    }}
    .scene-body {{
      padding: 8px 10px;
      display: grid;
      grid-template-columns: 1.1fr 1.6fr;
      gap: 10px;
    }}
    .scene-tech {{
      border-right: 1px solid #f1f5f9;
      padding-right: 8px;
    }}
    .tech-item {{
      margin-bottom: 5px;
    }}
    .tech-label {{
      font-size: 6.8pt;
      font-weight: 700;
      color: #008C45;
      text-transform: uppercase;
      letter-spacing: 0.3px;
      display: block;
    }}
    .tech-val {{
      font-size: 7.6pt;
      color: #334155;
    }}
    .scene-voice {{
      background: #f0fdf4;
      border: 1px solid #dcfce7;
      border-left: 3px solid #16a34a;
      padding: 7px 9px;
      border-radius: 4px;
    }}
    .voice-label {{
      font-size: 7pt;
      font-weight: 800;
      color: #15803d;
      text-transform: uppercase;
      margin-bottom: 3px;
    }}
    .voice-text {{
      font-size: 8pt;
      color: #14532d;
      font-style: italic;
      line-height: 1.42;
    }}

    .ikigai-box {{
      background: #faf5ff;
      border: 1px solid #e9d5ff;
      border-left: 4px solid #9333ea;
      padding: 8px;
      border-radius: 6px;
      margin: 8px 0;
    }}
    .ikigai-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 6px;
      margin-top: 5px;
      font-size: 7.2pt;
    }}
    .ikigai-item {{
      background: white;
      padding: 5px;
      border-radius: 4px;
      border: 1px solid #f3e8ff;
    }}
    .ikigai-item strong {{
      color: #7e22ce;
      display: block;
      font-size: 6.8pt;
      text-transform: uppercase;
    }}

    .dofa-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 6px;
      margin: 6px 0;
      font-size: 7.2pt;
    }}
    .dofa-card {{
      padding: 6px;
      border-radius: 4px;
      border: 1px solid #e2e8f0;
    }}
    .dofa-f {{ background: #f0fdf4; border-left: 3px solid #22c55e; }}
    .dofa-d {{ background: #fef2f2; border-left: 3px solid #ef4444; }}
    .dofa-o {{ background: #eff6ff; border-left: 3px solid #3b82f6; }}
    .dofa-a {{ background: #fffbeb; border-left: 3px solid #f59e0b; }}
    .dofa-card strong {{ display: block; font-size: 6.8pt; text-transform: uppercase; margin-bottom: 1px; }}

    .gallery-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
      margin: 8px 0;
    }}
    .gallery-card {{
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      overflow: hidden;
      background: #ffffff;
      text-align: center;
      padding: 5px;
    }}
    .gallery-img {{
      width: 100%;
      height: 110px;
      object-fit: cover;
      border-radius: 4px;
      margin-bottom: 4px;
    }}
    .gallery-title {{
      font-size: 6.8pt;
      font-weight: 700;
      color: #0f172a;
      text-transform: uppercase;
    }}
    .gallery-sub {{
      font-size: 6.2pt;
      color: #64748b;
    }}

    .footer-note {{
      font-size: 6.8pt;
      color: #64748b;
      text-align: center;
      margin-top: 10px;
      border-top: 1px solid #e2e8f0;
      padding-top: 4px;
    }}
  </style>
</head>
<body>

  <!-- PÁGINA 1: PORTADA, IKIGAI, DOFA Y GALERÍA DE FOTOS REALES -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">SENA • CENTRO DE TELEINFORMÁTICA Y PRODUCCIÓN INDUSTRIAL (CTPI)</div>
      <div class="header-meta">ADSO • FICHA 3186681 | POPAYÁN, CAUCA</div>
    </div>

    <div class="cover-card">
      <div class="cover-badge">Guion Técnico Oficial y Producción Audiovisual</div>
      <div class="cover-title">Mi Proyecto de Vida: Tecnología, Amor Familiar, Propósito y Paz</div>
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
          <strong>Enfoque</strong>
          Interfaces UI/UX &amp; IA
        </div>
      </div>
    </div>

    <h2>1. Fotografías Reales Incorporadas en el Video</h2>
    <div class="gallery-grid">
      <div class="gallery-card">
        <img class="gallery-img" src="{p_foto1}" alt="Retrato Karen Campo">
        <div class="gallery-title">Foto 1: Retrato de Karen</div>
        <div class="gallery-sub">Escenas 01 y 08 • Identidad y Cierre</div>
      </div>
      <div class="gallery-card">
        <img class="gallery-img" src="{p_foto2}" alt="Familia Karen Campo">
        <div class="gallery-title">Foto 2: Familia (Mamá y Hermano)</div>
        <div class="gallery-sub">Escena 05 • Pilar de superación y amor</div>
      </div>
      <div class="gallery-card">
        <img class="gallery-img" src="{p_foto3}" alt="Pareja y Mascotas">
        <div class="gallery-title">Foto 3: Pareja y Mascotas</div>
        <div class="gallery-sub">Escena 07 • Compañero de vida y hogar</div>
      </div>
    </div>

    <h2>2. Esquema Integrador: Ikigai Personal de Karen Campo</h2>
    <div class="ikigai-box">
      <p style="font-size: 7.5pt; color: #581c87; font-weight: 700; margin-bottom: 3px;">
        CONVERGENCIA DE PROPÓSITO: INTERFACES (UI/UX) E INTELIGENCIA ARTIFICIAL CON SENTIDO SOCIAL
      </p>
      <div class="ikigai-grid">
        <div class="ikigai-item">
          <strong>1. Lo que amo</strong>
          El diseño de interfaces (UI/UX), la Inteligencia Artificial y el tiempo de calidad en familia.
        </div>
        <div class="ikigai-item">
          <strong>2. En lo que soy buena</strong>
          Pensamiento lógico, empatía visual, organización, arquitectura de datos y resiliencia.
        </div>
        <div class="ikigai-item">
          <strong>3. Lo que el mundo necesita</strong>
          Tecnología inclusiva y accesible, empoderamiento femenino en STEM y cultura de paz.
        </div>
        <div class="ikigai-item">
          <strong>4. Por lo que me pagarán</strong>
          Desarrollo de software ADSO, diseño de experiencias UI/UX e integración de modelos de IA.
        </div>
      </div>
    </div>

    <h2>3. Matriz DOFA Personal (Autodiagnóstico Vocacional)</h2>
    <div class="dofa-grid">
      <div class="dofa-card dofa-f">
        <strong style="color: #15803d;">Fortalezas (F)</strong>
        Sensibilidad estética y técnica en interfaces, pensamiento lógico para IA, apoyo incondicional de su mamá y pareja, y disciplina de estudio diario.
      </div>
      <div class="dofa-card dofa-d">
        <strong style="color: #b91c1c;">Debilidades (D)</strong>
        Autoexigencia ante plazos críticos de entregas (regulada mediante pausas activas y balance con su hogar y mascotas).
      </div>
      <div class="dofa-card dofa-o">
        <strong style="color: #1d4ed8;">Oportunidades (O)</strong>
        Auge masivo de la Inteligencia Artificial, alta demanda de diseñadores UI/UX y respaldo académico del SENA CTPI Popayán.
      </div>
      <div class="dofa-card dofa-a">
        <strong style="color: #b45309;">Amenazas (A)</strong>
        Acelerada evolución de herramientas digitales (superada con el hábito de autoaprendizaje constante).
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
            <span class="tech-label">Foto en Pantalla</span>
            <span class="tech-val">Foto 1: Retrato sonriente de Karen en marco dinámico institucional.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Elementos Visuales</span>
            <span class="tech-val">Logo SENA CTPI, Lower Third: Karen Yuliana Campo • Ficha 3186681.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Ambiente Sonoro</span>
            <span class="tech-val">Guitarra acústica y piano suave en fade-in (ducking a -26 dB).</span>
          </div>
        </div>
        <div class="scene-voice">
          <div class="voice-label">🎙️ Locución Karen Yuliana Campo:</div>
          <div class="voice-text">
            "¡Hola a todos! Mi nombre es Karen Yuliana Campo. Soy aprendiz de la tecnología en Análisis y Desarrollo de Software en el Centro de Teleinformática y Producción Industrial, CTPI del SENA, en Popayán.<br><br>
            Hoy quiero compartir con ustedes mi Proyecto de Vida: una construcción que nace desde el amor de mi hogar, mis valores más profundos y mi pasión por la tecnología, con el firme propósito de aportar al desarrollo humano, a la convivencia y a una verdadera cultura de paz."
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
            <span class="tech-label">Concepto y Gráfica</span>
            <span class="tech-val">Infografía de Malala Yousafzai, libro "Yo soy Malala" y UNESCO.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Texto en Pantalla</span>
            <span class="tech-val">¿Qué le diría al mundo si tuviera la palabra para hacerlo mejor?</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Ambiente Sonoro</span>
            <span class="tech-val">Piano emotivo y cinematográfico, transmitiendo reflexión y esperanza.</span>
          </div>
        </div>
        <div class="scene-voice">
          <div class="voice-label">🎙️ Locución Karen Yuliana Campo:</div>
          <div class="voice-text">
            "Al reflexionar sobre la historia de Malala Yousafzai y su valiente lucha por el derecho a la educación de las niñas, me pregunto: Si me dieran la palabra frente al mundo... ¿qué diría para hacerlo un lugar mejor?<br><br>
            Yo le diría al mundo que la educación, el afecto y la tecnología no deben ser privilegios, sino puentes para sanar brechas. Que la paz se construye cuando cada mujer, joven o niña tiene la oportunidad de formarse, creer en sus capacidades y transformar su realidad con dignidad y libertad."
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
            <span class="tech-label">Plano y Gráfica</span>
            <span class="tech-val">Nivel 1 de Dilts con animación de luz cálida y tarjeta de gratitud.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Conceptos Clave</span>
            <span class="tech-val">Fe, Gratitud cotidiana, Humildad y Vocación de servicio.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Ambiente Sonoro</span>
            <span class="tech-val">Cuerdas y armonía serena, tono contemplativo y sincero.</span>
          </div>
        </div>
        <div class="scene-voice">
          <div class="voice-label">🎙️ Locución Karen Yuliana Campo:</div>
          <div class="voice-text">
            "Iniciando con mi Identidad Trascendente: ante Dios y el universo me reconozco como una persona inmensamente bendecida, con un propósito claro de servir y aprender cada día.<br><br>
            Mi espiritualidad se refleja en la gratitud cotidiana: en valorar a los seres que amo, en actuar con honestidad frente a cada reto y en saber que el conocimiento cobra verdadero sentido cuando se pone al servicio de los demás. Me siento llamada a no ser indiferente y a retribuir con generosidad las oportunidades que la vida me da."
          </div>
        </div>
      </div>
    </div>

    <!-- ESCENA 04 -->
    <div class="scene-card">
      <div class="scene-header">
        <span class="scene-id">ESCENA 04: Nivel 2 — Identidad, Roles y Misión/Visión (Interfaces e IA)</span>
        <span class="scene-time">01:45 - 02:25 (40 seg)</span>
      </div>
      <div class="scene-body">
        <div class="scene-tech">
          <div class="tech-item">
            <span class="tech-label">Visuales y Gráfica</span>
            <span class="tech-val">Diagrama de Roles + Iconos de Diseño de Interfaces (UI/UX) e Inteligencia Artificial.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Misión y Visión</span>
            <span class="tech-val">Crear experiencias digitales accesibles potenciadas con IA para transformar vidas.</span>
          </div>
        </div>
        <div class="scene-voice">
          <div class="voice-label">🎙️ Locución Karen Yuliana Campo:</div>
          <div class="voice-text">
            "En el segundo nivel defino quién soy y quién elijo ser. Soy Karen Yuliana: una mujer caucana, hija orgullosa, compañera leal y aprendiz apasionada del desarrollo de software.<br><br>
            Mi misión es diseñar interfaces digitales intuitivas y humanas, integrando herramientas de Inteligencia Artificial que resuelvan necesidades reales en mi comunidad.<br><br>
            Mi visión a cinco años es ser una profesional destacada en diseño UI/UX e IA con enfoque social, demostrando que desde Popayán podemos crear tecnología de clase mundial con rostro humano."
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
        <span class="scene-id">ESCENA 05: Nivel 3 — Valores y el Pilar Familiar: Mamá y Pareja</span>
        <span class="scene-time">02:25 - 03:00 (35 seg)</span>
      </div>
      <div class="scene-body">
        <div class="scene-tech">
          <div class="tech-item">
            <span class="tech-label">Fotos en Pantalla</span>
            <span class="tech-val">Foto 2: Mamá y hermano en cumpleaños + Foto 3: Pareja y mascotas.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Valores Pilares</span>
            <span class="tech-val">Perseverancia materna, Compañerismo, Lealtad, Honestidad y Empatía.</span>
          </div>
        </div>
        <div class="scene-voice">
          <div class="voice-label">🎙️ Locución Karen Yuliana Campo:</div>
          <div class="voice-text">
            "Mis valores tienen raíz en mi hogar. Mi pilar fundamental es mi mamá: aunque no tuvo la oportunidad de obtener un título universitario, se ha destacado por inculcarme con amor e insistencia que debo estudiar, prepararme y superarme sin rendirme jamás.<br><br>
            Junto a ella, mi pareja, mi compañero de vida, está siempre a mi lado brindándome su apoyo incondicional en cada desvelo y en cada proyecto. Ellos son mi mayor motor de integridad, perseverancia y lealtad."
          </div>
        </div>
      </div>
    </div>

    <!-- ESCENA 06 -->
    <div class="scene-card">
      <div class="scene-header">
        <span class="scene-id">ESCENA 06: Nivel 4 — Capacidades: Interfaces UI/UX, IA y Matriz DOFA</span>
        <span class="scene-time">03:00 - 03:40 (40 seg)</span>
      </div>
      <div class="scene-body">
        <div class="scene-tech">
          <div class="tech-item">
            <span class="tech-label">Gráfica Interactiva</span>
            <span class="tech-val">Infografía DOFA: Pasión por Interfaces, Curiosidad en IA y Manejo de la Autoexigencia.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Ambiente Sonoro</span>
            <span class="tech-val">Ritmo moderno, dinámico e innovador.</span>
          </div>
        </div>
        <div class="scene-voice">
          <div class="voice-label">🎙️ Locución Karen Yuliana Campo:</div>
          <div class="voice-text">
            "En el cuarto nivel analizo mis capacidades mediante una matriz DOFA consciente.<br><br>
            Las áreas que más me apasionan son el diseño de interfaces de usuario y la Inteligencia Artificial: combinar la estética y la psicología visual con algoritmos inteligentes para crear experiencias digitales amigables y accesibles.<br><br>
            Reconozco que a veces la autoexigencia me presiona, pero he aprendido a canalizarla con disciplina, pausas activas y una mentalidad donde cada error en código es un peldaño más hacia la maestría técnica."
          </div>
        </div>
      </div>
    </div>

    <!-- ESCENA 07 -->
    <div class="scene-card">
      <div class="scene-header">
        <span class="scene-id">ESCENA 07: Niveles 5 y 6 — Hábitos Diarios, Convivencia y Hogar</span>
        <span class="scene-time">03:40 - 04:15 (35 seg)</span>
      </div>
      <div class="scene-body">
        <div class="scene-tech">
          <div class="tech-item">
            <span class="tech-label">Fotos en Pantalla</span>
            <span class="tech-val">Foto 3: Con su pareja, sus 3 perros y farolitos navideños de velitas.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Hábitos Clave</span>
            <span class="tech-val">Estudio diario riguroso + Tiempo de calidad con mamá, hermano, pareja y mascotas.</span>
          </div>
        </div>
        <div class="scene-voice">
          <div class="voice-label">🎙️ Locución Karen Yuliana Campo:</div>
          <div class="voice-text">
            "En los niveles 5 y 6, mi proyecto se vive en lo cotidiano a través de dos hábitos indispensables: el estudio disciplinado de mi carrera y el tiempo de calidad con mi familia.<br><br>
            Disfrutar de mi mamá, mi hermano, mi pareja y nuestras amadas mascotas llena mi vida de alegría y equilibrio. Convivir en armonía, dialogar sin violencia y cuidar nuestro entorno mediante el reciclaje y el ahorro de recursos son mis compromisos diarios para sembrar paz desde mi propia casa."
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
            <span class="tech-label">Visual Final</span>
            <span class="tech-val">Foto 1 (Retrato Karen) + Diagrama de Venn Ikigai en convergencia total.</span>
          </div>
          <div class="tech-item">
            <span class="tech-label">Placa Institucional</span>
            <span class="tech-val">SENA CTPI Popayán • Ficha 3186681 • Regional Cauca 2026.</span>
          </div>
        </div>
        <div class="scene-voice">
          <div class="voice-label">🎙️ Locución Karen Yuliana Campo:</div>
          <div class="voice-text">
            "Al integrar todo en mi IKIGAI, encuentro mi razón de ser: unir lo que amo, en lo que soy buena, mi profesión ADSO y lo que Colombia necesita.<br><br>
            Mi propósito es crear interfaces inteligentes y humanas, honrando el esfuerzo de mi madre y el respaldo de quienes creen en mí. Mi proyecto de vida demuestra que la tecnología y los valores son la combinación perfecta para construir un futuro mejor.<br><br>
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
    print("=== INICIANDO COMPILACIÓN DE GUION TÉCNICO FORMAL CON FOTOS REALES ===")
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
