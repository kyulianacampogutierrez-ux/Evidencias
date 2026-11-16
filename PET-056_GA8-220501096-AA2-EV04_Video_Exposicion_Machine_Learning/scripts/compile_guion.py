#!/usr/bin/env python3
# ==============================================================================
# COMPILADOR DE GUION TÉCNICO INDIVIDUAL (PDF / DOCX)
# Evidencia: GA8-220501096-AA2-EV04 - Video exposición sobre machine learning
# Documento: Guion Técnico y Storyboard Audiovisual Individual
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán
# ==============================================================================

import os
import shutil
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
ENTREGA_DIR = '/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA8-220501096-AA2-EV04'
ARTIFACT_DIR = '/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603'

os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(ENTREGA_DIR, exist_ok=True)

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Guion Técnico y Storyboard - Video Exposición Machine Learning | Karen Campo</title>
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
      line-height: 1.48;
      font-size: 9.5pt;
    }
    .page {
      page-break-after: always;
      position: relative;
    }
    .page:last-child {
      page-break-after: avoid;
    }

    /* Header & Footer */
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
      margin-bottom: 10px;
      font-weight: 800;
    }
    h2.section-title {
      font-size: 11.5pt;
      color: #008C45;
      border-left: 4px solid #008C45;
      padding-left: 8px;
      margin-top: 14px;
      margin-bottom: 8px;
      font-weight: 700;
    }
    h3.sub-title {
      font-size: 9.5pt;
      color: #1e293b;
      margin-top: 10px;
      margin-bottom: 4px;
      font-weight: 700;
    }
    p {
      margin-bottom: 8px;
      text-align: justify;
    }

    /* Tables */
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 8px 0 12px;
      font-size: 8pt;
    }
    th {
      background: #008C45;
      color: #ffffff;
      font-weight: 700;
      padding: 6px 8px;
      text-align: left;
      border: 1px solid #007037;
    }
    td {
      padding: 5px 8px;
      border: 1px solid #cbd5e1;
      vertical-align: top;
    }
    tr:nth-child(even) td {
      background: #f8fafc;
    }

    /* Callouts & Quotes */
    .callout {
      background: #f0fdf4;
      border-left: 4px solid #16a34a;
      padding: 8px 12px;
      margin: 10px 0;
      border-radius: 0 6px 6px 0;
      font-size: 8.5pt;
    }
    .callout-amber {
      background: #fffbeb;
      border-left: 4px solid #f59e0b;
      padding: 8px 12px;
      margin: 10px 0;
      border-radius: 0 6px 6px 0;
      font-size: 8.5pt;
    }
    blockquote {
      background: #f8fafc;
      border-left: 3px solid #008C45;
      padding: 7px 12px;
      margin: 7px 0;
      font-style: italic;
      color: #334155;
      font-size: 8.5pt;
      line-height: 1.45;
    }

    /* Cover Page */
    .cover-container {
      height: 92vh;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      border: 2px solid #008C45;
      padding: 34px;
      background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
      border-radius: 8px;
    }
    .cover-top {
      border-bottom: 3px solid #008C45;
      padding-bottom: 14px;
    }
    .cover-inst {
      font-size: 13pt;
      font-weight: 800;
      color: #008C45;
      letter-spacing: 0.5px;
    }
    .cover-subinst {
      font-size: 9.5pt;
      color: #475569;
      font-weight: 600;
    }
    .cover-center {
      margin: 22px 0;
    }
    .badge-pill {
      display: inline-block;
      background: #dcfce7;
      color: #166534;
      padding: 4px 10px;
      border-radius: 12px;
      font-size: 8pt;
      font-weight: 700;
      margin-bottom: 12px;
    }
    .cover-title {
      font-size: 19pt;
      color: #0f172a;
      font-weight: 800;
      line-height: 1.25;
      margin-bottom: 10px;
    }
    .cover-desc {
      font-size: 9.5pt;
      color: #334155;
      line-height: 1.45;
    }
    .meta-box {
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      padding: 14px 18px;
      margin-top: 14px;
      display: grid;
      grid-template-columns: 140px 1fr;
      row-gap: 5px;
      font-size: 8.5pt;
    }
    .meta-label {
      font-weight: 700;
      color: #64748b;
    }
    .meta-value {
      font-weight: 600;
      color: #0f172a;
    }
    .cover-bottom {
      border-top: 1px solid #cbd5e1;
      padding-top: 12px;
      font-size: 8pt;
      color: #64748b;
      display: flex;
      justify-content: space-between;
    }
  </style>
</head>
<body>

  <!-- ==================== PÁGINA 1: PORTADA ==================== -->
  <div class="page">
    <div class="cover-container">
      <div class="cover-top">
        <div class="cover-inst">SERVICIO NACIONAL DE APRENDIZAJE (SENA)</div>
        <div class="cover-subinst">CENTRO DE TELEINFORMÁTICA Y PRODUCCIÓN INDUSTRIAL (CTPI) • REGIONAL CAUCA</div>
      </div>

      <div class="cover-center">
        <span class="badge-pill">DOCUMENTO INDIVIDUAL TÉCNICO • GUÍA DE APRENDIZAJE NO. 8</span>
        <h1 class="cover-title">GUION TÉCNICO Y STORYBOARD AUDIOVISUAL<br>VIDEO EXPOSICIÓN SOBRE MACHINE LEARNING</h1>
        <p class="cover-desc">
          Planificación audiovisual detallada, desglose técnico de preproducción, libreto de locución completo y storyboard segundo a segundo para la exposición en video de 10 minutos sobre la tecnología emergente y disruptiva de <strong>Machine Learning e Inteligencia Artificial</strong>, conforme a los criterios de evaluación de la evidencia GA8-220501096-AA2-EV04.
        </p>

        <div class="meta-box">
          <div class="meta-label">Programa:</div>
          <div class="meta-value">Tecnólogo en Análisis y Desarrollo de Software (ADSO)</div>

          <div class="meta-label">Ficha de Caracterización:</div>
          <div class="meta-value">3186681</div>

          <div class="meta-label">Fase del Proyecto:</div>
          <div class="meta-value">Evaluación</div>

          <div class="meta-label">Competencia:</div>
          <div class="meta-value">220501096 — Desarrollar la solución de software según diseño y metodologías</div>

          <div class="meta-label">Actividad de Aprendizaje:</div>
          <div class="meta-value">GA8-220501096-AA2 — Incorporar tecnologías emergentes y disruptivas según diseño</div>

          <div class="meta-label">Resultado de Aprendizaje:</div>
          <div class="meta-value">220501096-02 — Incorporar tecnologías emergentes y disruptivas de acuerdo con propósitos del software</div>

          <div class="meta-label">Evidencia:</div>
          <div class="meta-value">GA8-220501096-AA2-EV04 — Video exposición sobre machine learning</div>

          <div class="meta-label">Aprendiz Autora:</div>
          <div class="meta-value">Karen Yuliana Campo</div>

          <div class="meta-label">Duración Estimada:</div>
          <div class="meta-value">10 minutos de exposición técnica continua</div>

          <div class="meta-label">Formato de Video:</div>
          <div class="meta-value">MP4 Full HD 1080p (1920x1080 Widescreen 16:9, H.264 / AAC 320k)</div>
        </div>
      </div>

      <div class="cover-bottom">
        <div>Popayán, Departamento del Cauca — Colombia</div>
        <div>Noviembre de 2026</div>
      </div>
    </div>
  </div>

  <!-- ==================== PÁGINA 2: METODOLOGÍA DE PRODUCCIÓN Y GUION LITERARIO (PARTE 1) ==================== -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">GUION TÉCNICO • VIDEO EXPOSICIÓN MACHINE LEARNING • SENA ADSO 3186681</div>
      <div class="header-meta">Karen Yuliana Campo | Noviembre 2026</div>
    </div>

    <h2 class="section-title">1. METODOLOGÍA DE PRODUCCIÓN AUDIOVISUAL (3 FASES NORMATIVAS)</h2>
    <p>
      Dando estricto cumplimiento a las directrices pedagógicas de la <strong>Guía de Aprendizaje No. 8 (Págs. 20-21)</strong>, la elaboración de la video exposición sobre Machine Learning se rige por el ciclo estándar de producción en 3 fases:
    </p>

    <table>
      <thead>
        <tr>
          <th style="width: 25%;">Fase de Producción</th>
          <th style="width: 35%;">Actividades Clave Desarrolladas</th>
          <th style="width: 40%;">Entregables y Herramientas Utilizadas</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Fase 1: Preproducción</strong></td>
          <td>Investigación temática rigurosa, redacción del guion literario, elaboración del guion técnico segundo a segundo, diseño de diapositivas y diagramas vectoriales.</td>
          <td>Guion individual (PDF/DOCX), Storyboard gráfico, diapositivas HTML5 interactivas y selección de fuentes sonoras.</td>
        </tr>
        <tr>
          <td><strong>Fase 2: Producción</strong></td>
          <td>Grabación en vivo de la locución y screencast en alta definición, captura de pantalla de diapositivas, demostración de modelos y registro audiovisual continuo.</td>
          <td>OBS Studio v30.2 (Open Broadcaster Software), micrófono dinámico con filtro pop y entorno de desarrollo Linux KDE Plasma.</td>
        </tr>
        <tr>
          <td><strong>Fase 3: Postproducción</strong></td>
          <td>Edición digital no lineal, sincronización de audio y video, aplicación de audio ducking dinámico, ecualización vocal, títulos y renderizado final.</td>
          <td>FilmCraft CLI v0.20.1 NLE Engine, exportación a MP4 1080p (H.264 / AAC estéreo 48 kHz) y despliegue web en Docker.</td>
        </tr>
      </tbody>
    </table>

    <h2 class="section-title">2. GUION LITERARIO COMPLETO (DISCURSO NARRATIVO PARTE 1)</h2>
    <p>
      A continuación se presenta el discurso narrativo continuo que orienta la locución de la aprendiz durante la grabación de la pieza:
    </p>

    <blockquote>
      <strong>[00:00 - 00:45] Bloque 1: Apertura Institucional e Introducción:</strong><br>
      "Un cordial saludo para el cuerpo de instructores y compañeros del Servicio Nacional de Aprendizaje (SENA). Mi nombre es Karen Yuliana Campo, aprendiz de la tecnología en Análisis y Desarrollo de Software (ADSO), con ficha de caracterización 3186681 en el Centro de Teleinformática y Producción Industrial (CTPI), Regional Cauca. En el marco de la competencia de desarrollo de software y la actividad GA8-220501096-AA2, presento esta video exposición formal orientada al estudio, principios, taxonomía y consecuencias éticas del Machine Learning y la Inteligencia Artificial como tecnologías emergentes y disruptivas."
    </blockquote>

    <blockquote>
      <strong>[00:45 - 02:00] Bloque 2: ¿En qué consiste el Machine Learning?:</strong><br>
      "Iniciemos definiendo en qué consiste el Machine Learning o Aprendizaje Automático. Tradicionalmente, la programación informática requería que un desarrollador escribiera de forma explícita cada regla lógica: entraban datos y reglas, y el computador generaba respuestas. Machine Learning invierte este paradigma: suministramos datos masivos y las respuestas deseadas, y la máquina induce los patrones matemáticos subyacentes. Como lo formalizó Tom Mitchell en 1997: se dice que un programa aprende de la experiencia E con respecto a una tarea T y una medida de rendimiento P, si su rendimiento en T mejora con la experiencia E. Existen tres grandes paradigmas: el Aprendizaje Supervisado, donde contamos con datos etiquetados para tareas de regresión y clasificación; el Aprendizaje No Supervisado, que descubre estructuras ocultas y agrupamientos en datos crudos; y el Aprendizaje por Refuerzo, donde un agente toma acciones en un entorno para maximizar una función de recompensa acumulada."
    </blockquote>

    <blockquote>
      <strong>[02:00 - 03:00] Bloque 3: Objetivos de la Tecnología Machine Learning:</strong><br>
      "¿Cuáles son los objetivos cardinales del Machine Learning? Primero: la capacidad de generalización predictiva, es decir, inferir resultados certeros sobre datos que el sistema nunca ha visto en su entrenamiento. Segundo: la automatización de procesos cognitivos complejos que escapan a la programación heurística convencional. Tercero: la optimización y adaptación dinámica a entornos cambiantes, permitiendo que el software evolucione con nuevos datos. Y cuarto: el descubrimiento de correlaciones y conocimientos no evidentes dentro de volúmenes masivos de información (Big Data), aportando valor estratégico a la industria del software."
    </blockquote>
  </div>

  <!-- ==================== PÁGINA 3: GUION LITERARIO (PARTE 2) ==================== -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">GUION LITERARIO • VIDEO EXPOSICIÓN MACHINE LEARNING • PÁGINA 3</div>
      <div class="header-meta">GA8-220501096-AA2-EV04 • Ficha 3186681</div>
    </div>

    <blockquote>
      <strong>[03:00 - 04:15] Bloque 4: Antecedentes Históricos y Evolución de la Tecnología:</strong><br>
      "Para comprender el estado actual del Machine Learning es indispensable revisar sus antecedentes históricos. En 1950, Alan Turing formula su célebre artículo 'Computing Machinery and Intelligence', introduciendo el Test de Turing. En 1952, Arthur Samuel diseña el primer programa capaz de aprender a jugar damas y acuña en 1959 el término 'Machine Learning'. En 1958, Frank Rosenblatt presenta el Perceptrón, la primera formulación de una neurona artificial. Sin embargo, en 1969, Marvin Minsky y Seymour Papert demuestran las limitaciones matemáticas del perceptrón simple para resolver funciones no lineales como XOR, desatando el 'Primer Invierno de la IA'. El renacimiento surge en 1986 con Rumelhart, Hinton y Williams mediante el algoritmo de retropropagación (Backpropagation) para redes multicapa. Finalmente, la confluencia en 2012 de cómputo en GPUs, grandes volúmenes de datos en Internet y redes neuronales profundas (AlexNet) cataliza la era moderna del Deep Learning y los modelos Transformer."
    </blockquote>

    <blockquote>
      <strong>[04:15 - 05:15] Bloque 5: ¿En qué consiste la Inteligencia Artificial?:</strong><br>
      "La Inteligencia Artificial es el campo matriz de las ciencias de la computación dedicado a crear sistemas capaces de emular capacidades cognitivas humanas como el razonamiento, la percepción visual, la toma de decisiones y el procesamiento del lenguaje natural. Debemos clarificar su jerarquía: la Inteligencia Artificial es la disciplina amplia; el Machine Learning es un subconjunto enfocado en el aprendizaje estadístico; el Deep Learning es un subconjunto del ML basado en redes neuronales multicapa; y los Modelos Fundacionales o LLMs son implementaciones avanzadas de Deep Learning. En términos de capacidades, distinguimos la IA Estrecha o Débil (ANI), orientada a tareas puntuales; la IA General (AGI), equivalente a la versatilidad cognitiva humana; y la Superinteligencia Artificial (ASI)."
    </blockquote>

    <blockquote>
      <strong>[05:15 - 06:30] Bloque 6: Modelo de IA Orientado a la Programación (IA Simbólica / Basada en Reglas):</strong><br>
      "El primer gran modelo de la IA es el orientado a la programación, conocido técnicamente como IA Simbólica, GOFAI (Good Old-Fashioned AI) o sistemas basados en reglas. Este enfoque sigue una metodología Top-Down: el conocimiento humano es traducido formalmente por ingenieros del conocimiento a bases de hechos y reglas 'SI-ENTONCES' (`IF-THEN`). Un motor de inferencia aplica lógica proposicional o de predicados para deducir conclusiones. Su gran fortaleza radica en el determinismo y la explicabilidad: cada deducción tiene una trazabilidad auditable. No obstante, su gran debilidad histórica fue el 'cuello de botella de adquisición de conocimiento', la fragilidad ante datos ambiguos o ruidosos y la incapacidad de resolver problemas de percepción visual o auditiva."
    </blockquote>

    <blockquote>
      <strong>[06:30 - 07:45] Bloque 7: Modelo de IA Orientado a Conexiones Neuronales (Enfoque Conexionista):</strong><br>
      "En contraposición radical a la IA simbólica, el modelo orientado a conexiones neuronales adopta un enfoque Bottom-Up inspirado en la neurobiología. En lugar de programar reglas lógicas, construimos grafos de nodos o neuronas artificiales interconectadas. Cada neurona recibe entradas ponderadas por pesos sinápticos ($W$), suma un sesgo ($b$) y aplica una función de activación no lineal como ReLU o Sigmoide. Durante el entrenamiento, la red procesa datos en propagación hacia adelante (Forward Propagation), cuantifica la discrepancia mediante una función de pérdida (Loss Function) y ajusta los pesos en sentido inverso mediante el algoritmo de Backpropagation y Descenso de Gradiente Estocástico (SGD/Adam). Las arquitecturas conexionistas clave incluyen las CNN para visión, las LSTM para series temporales y los Transformers con atención propia para modelos de lenguaje masivo."
    </blockquote>
  </div>

  <!-- ==================== PÁGINA 4: GUION LITERARIO (PARTE 3) Y STORYBOARD (1/2) ==================== -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">GUION LITERARIO Y STORYBOARD TÉCNICO • PÁGINA 4</div>
      <div class="header-meta">GA8-220501096-AA2-EV04 • Ficha 3186681</div>
    </div>

    <blockquote>
      <strong>[07:45 - 08:45] Bloque 8: Productos Realizados con IA y Aplicación en el Proyecto ADSO:</strong><br>
      "Hoy en día la Inteligencia Artificial materializa productos transformadores a nivel global: vehículos autónomos con visión computacional de Tesla, motores de recomendación predictiva en Netflix y Amazon, diagnóstico de patologías asistido por Deep Learning, y sistemas generativos de vanguardia como ChatGPT, Gemini y Claude. En nuestro proyecto formativo ADSO, 'Pizzería Gourmet Bella Italia Popayán', la IA y el Machine Learning se integran en tres componentes esenciales: primero, un motor predictivo de demanda de insumos campesinos de Silvia y Timbío utilizando modelos de series temporales para minimizar el desperdicio perecedero; segundo, un sistema de recomendación personalizado de combinaciones gastronómicas; y tercero, un algoritmo heurístico de optimización de rutas de delivery térmico para asegurar pizzas a más de 70°C en menos de 30 minutos."
    </blockquote>

    <blockquote>
      <strong>[08:45 - 09:45] Bloque 9: Consecuencias Sociales, Éticas y Filosóficas de la Tecnología:</strong><br>
      "La adopción masiva del Machine Learning plantea interrogantes trascendentales: Primero, el sesgo algorítmico y la discriminación: si un modelo se entrena con datos históricos que contienen prejuicios humanos, la IA amplificará esas inequidades en selección de personal o créditos bancarios. Segundo, la privacidad y vigilancia masiva en la era del Big Data y reconocimiento facial no consentido. Tercero, la opacidad algorítmica o el problema de la 'Caja Negra', que exige la adopción urgente de IA Explicable (XAI) en sectores críticos como medicina y justicia penal. Cuarto, el impacto en el mercado laboral y la automatización del trabajo, demandando una profunda reconversión de competencias. Y quinto, dilemas filosóficos sobre la agencia moral, los deepfakes, la manipulación de la opinión pública y la necesidad ética de mantener siempre al ser humano en el centro de las decisiones (Human-in-the-Loop)."
    </blockquote>

    <blockquote>
      <strong>[09:45 - 10:00] Bloque 10: Conclusiones y Cierre Académico:</strong><br>
      "Como conclusión, el Machine Learning no sustituye la ingeniería de software tradicional, sino que expande exponencialmente sus capacidades para abordar problemas complejos de percepción y predicción. Como tecnólogos en ADSO del SENA, nuestra responsabilidad ética y técnica radica en diseñar software robusto, auditable, equitativo y comprometido con el desarrollo productivo y social de nuestra región. Muchas gracias por su atención."
    </blockquote>

    <h2 class="section-title">3. STORYBOARD Y MATRIZ TÉCNICA DETALLADA (BLOQUES 1 A 5)</h2>
    <table>
      <thead>
        <tr>
          <th style="width: 12%;">Bloque</th>
          <th style="width: 22%;">Tema y Diapositiva</th>
          <th style="width: 24%;">Encuadre / Tipo de Plano</th>
          <th style="width: 42%;">Elementos en Pantalla y Gráficos Visuales</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>01<br>(00:00 - 00:45)</strong></td>
          <td>Apertura Institucional e Introducción</td>
          <td>Plano medio de la expositora con cintillo institucional inferior</td>
          <td>Logotipo SENA, CTPI Regional Cauca, Título de la evidencia, datos de Karen Campo ADSO 3186681 y fondo tecnológico sutil.</td>
        </tr>
        <tr>
          <td><strong>02<br>(00:45 - 02:00)</strong></td>
          <td>¿En qué consiste el Machine Learning?</td>
          <td>Screencast de diapositiva técnica + Picture-in-Picture circular</td>
          <td>Diagrama comparativo Tradicional (Datos + Reglas = Respuestas) vs ML (Datos + Respuestas = Reglas). Cuadro de paradigmas: Supervisado, No Supervisado y Refuerzo.</td>
        </tr>
        <tr>
          <td><strong>03<br>(02:00 - 03:00)</strong></td>
          <td>Objetivos de la Tecnología Machine Learning</td>
          <td>Screencast con infografía modular de 4 paneles</td>
          <td>4 pilares: 1) Generalización Predictiva, 2) Automatización Cognitiva, 3) Adaptabilidad Continua y 4) Descubrimiento en Big Data.</td>
        </tr>
        <tr>
          <td><strong>04<br>(03:00 - 04:15)</strong></td>
          <td>Antecedentes Históricos y Evolución</td>
          <td>Línea de tiempo horizontal animada con hitos</td>
          <td>Hitos: Turing (1950), Arthur Samuel (1952/1959), Perceptrón (1958), Inviernos de la IA (1969), Backpropagation (1986), AlexNet (2012) y Transformers (2017).</td>
        </tr>
        <tr>
          <td><strong>05<br>(04:15 - 05:15)</strong></td>
          <td>Fundamentos de la Inteligencia Artificial</td>
          <td>Diagrama de Euler con conjuntos anidados</td>
          <td>Conjuntos concéntricos (IA $\supset$ ML $\supset$ DL $\supset$ LLMs). Tabla clasificatoria de capacidades: ANI (Estrecha), AGI (General) y ASI (Superinteligencia).</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- ==================== PÁGINA 5: STORYBOARD (2/2) Y ESPECIFICACIONES TÉCNICAS ==================== -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">STORYBOARD TÉCNICO Y ESPECIFICACIÓN DE GRABACIÓN • PÁGINA 5</div>
      <div class="header-meta">GA8-220501096-AA2-EV04 • Ficha 3186681</div>
    </div>

    <h2 class="section-title">STORYBOARD Y MATRIZ TÉCNICA DETALLADA (BLOQUES 6 A 10)</h2>
    <table>
      <thead>
        <tr>
          <th style="width: 12%;">Bloque</th>
          <th style="width: 22%;">Tema y Diapositiva</th>
          <th style="width: 24%;">Encuadre / Tipo de Plano</th>
          <th style="width: 42%;">Elementos en Pantalla y Gráficos Visuales</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>06<br>(05:15 - 06:30)</strong></td>
          <td>IA Orientada a la Programación (Simbólica)</td>
          <td>Diagrama de árbol lógico y motor de inferencia</td>
          <td>Paradigma Top-Down, sistemas expertos (MYCIN, Dendral), bases de hechos y reglas `IF-THEN`. Cuadro de ventajas (trazabilidad) y desventajas (fragilidad).</td>
        </tr>
        <tr>
          <td><strong>07<br>(06:30 - 07:45)</strong></td>
          <td>IA Orientada a Conexiones Neuronales</td>
          <td>Diagrama anatómico de neurona artificial y red profunda</td>
          <td>Estructura de la neurona $\sigma(\sum w_i x_i + b)$, funciones de activación (ReLU/Sigmoid), propagación hacia adelante, cálculo de error y Backpropagation.</td>
        </tr>
        <tr>
          <td><strong>08<br>(07:45 - 08:45)</strong></td>
          <td>Productos de IA y Aplicación en Proyecto ADSO</td>
          <td>Mosaico de productos globales + Portal Web ADSO</td>
          <td>Productos mundiales (Tesla Autopilot, ChatGPT, Netflix). Caso Bella Italia Popayán: previsión de demanda de insumos campesinos y optimización de entrega térmica.</td>
        </tr>
        <tr>
          <td><strong>09<br>(08:45 - 09:45)</strong></td>
          <td>Consecuencias Sociales, Éticas y Filosóficas</td>
          <td>Panel de dilemas éticos con iconografía de alerta</td>
          <td>5 dimensiones: Sesgos algorítmicos, privacidad y vigilancia masiva, problema de la 'Caja Negra' (XAI), impacto laboral/empleo y alineación ética (Human-in-the-Loop).</td>
        </tr>
        <tr>
          <td><strong>10<br>(09:45 - 10:00)</strong></td>
          <td>Conclusiones y Despedida Institucional</td>
          <td>Plano medio de la expositora + Créditos institucionales</td>
          <td>Resumen de aprendizajes, rol del tecnólogo ADSO, enlace a repositorio GitHub oficial y cierre formal.</td>
        </tr>
      </tbody>
    </table>

    <h2 class="section-title">4. PARÁMETROS TÉCNICOS DE CAPTURA EN OBS STUDIO / FILMCRAFT</h2>
    <div class="callout-amber">
      <strong>Parámetros de Grabación y Procesamiento de Señal:</strong><br>
      • <strong>Lienzo de Captura:</strong> 1920x1080 píxeles a 30 FPS progresivo, formato de color NV12 / sRGB.<br>
      • <strong>Filtros Vocales en OBS:</strong> Puerta de ruido (-40 dB), Supresor de ruido Speex (-30 dB) y Compresor con relación 3:1 para nivelación vocal homogénea.<br>
      • <strong>Pipeline de Exportación:</strong> Ensamblado NLE en FilmCraft CLI bajo perfil High H.264 (4500 kbps) y audio AAC estéreo (320 kbps, 48 kHz).<br>
      • <strong>Despliegue Web:</strong> Servidor Docker HTTPD en puerto 8104 para streaming y revisión interactiva de la presentación.
    </div>

    <div style="margin-top: 25px; border-top: 1px solid #cbd5e1; padding-top: 10px; font-size: 8pt; color: #64748b; display: flex; justify-content: space-between;">
      <div><strong>Aprendiz Autora:</strong> Karen Yuliana Campo — Tecnóloga en ADSO</div>
      <div><strong>Regional:</strong> SENA Regional Cauca — CTPI Popayán</div>
    </div>
  </div>

</body>
</html>
"""

html_temp_path = os.path.join(DOCS_DIR, 'temp_guion_print.html')
pdf_output_path = os.path.join(DOCS_DIR, 'GA8-220501096-AA2-EV04_Guion_Video_Exposicion_Machine_Learning.pdf')
docx_output_path = os.path.join(DOCS_DIR, 'GA8-220501096-AA2-EV04_Guion_Video_Exposicion_Machine_Learning.docx')

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
    md_guion = os.path.join(DOCS_DIR, 'GUION_TECNICO_VIDEO_EXPOSICION_MACHINE_LEARNING.md')
    if os.path.exists(md_guion):
        shutil.copy(md_guion, ENTREGA_DIR)
        shutil.copy(md_guion, ARTIFACT_DIR)

    print("=== GUION TÉCNICO INDIVIDUAL COMPILADO Y DISTRIBUIDO ===")

if __name__ == '__main__':
    main()
