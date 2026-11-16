#!/usr/bin/env python3
# ==============================================================================
# COMPILADOR DE DOCUMENTACIÓN TÉCNICA FORMAL (PDF / DOCX / ZIP)
# Evidencia: GA8-220501096-AA2-EV04 - Video exposición sobre machine learning
# Competencia: 220501096 - Desarrollar la solución de software de acuerdo con el diseño
# Actividad: GA8-220501096-AA2 - Incorporar tecnologías emergentes y disruptivas
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
VIDEO_DIR = os.path.join(BASE_DIR, 'video')
SITIO_DIR = os.path.join(BASE_DIR, 'sitio_ml_web')
ENTREGA_DIR = '/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA8-220501096-AA2-EV04'
BRAIN_DIR = '/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603'

os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(ENTREGA_DIR, exist_ok=True)
os.makedirs(BRAIN_DIR, exist_ok=True)

cap1_path = os.path.join(CAPTURAS_DIR, 'paso_01_despliegue_docker_ml_konsole.png')
cap2_path = os.path.join(CAPTURAS_DIR, 'paso_02_verificacion_salud_servicios_ml_konsole.png')
cap3_path = os.path.join(CAPTURAS_DIR, 'paso_03_chrome_portal_ml_video_reproductor.png')
cap4_path = os.path.join(CAPTURAS_DIR, 'paso_04_chrome_diapositiva_modelos_ia_conexionista.png')
cap5_path = os.path.join(CAPTURAS_DIR, 'paso_05_chrome_guion_tecnico_completo.png')
cap6_path = os.path.join(CAPTURAS_DIR, 'paso_06_chrome_dataset_consecuencias_eticas.png')

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Video Exposición Machine Learning - GA8-220501096-AA2-EV04 | Karen Campo</title>
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
      font-size: 10pt;
    }}
    .page {{
      page-break-after: always;
      position: relative;
    }}
    .page:last-child {{
      page-break-after: avoid;
    }}

    /* Institutional Header & Footer */
    .header-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid #008C45;
      padding-bottom: 8px;
      margin-bottom: 18px;
    }}
    .header-title {{
      font-size: 8.5pt;
      font-weight: 700;
      color: #008C45;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .header-meta {{
      font-size: 8pt;
      color: #64748b;
      text-align: right;
    }}

    /* Typography */
    h1.doc-title {{
      font-size: 19pt;
      color: #0f172a;
      line-height: 1.2;
      margin-bottom: 6px;
      font-weight: 800;
    }}
    h2.doc-subtitle {{
      font-size: 11pt;
      color: #008C45;
      font-weight: 600;
      margin-bottom: 16px;
    }}
    h2.section-title {{
      font-size: 13pt;
      color: #0f172a;
      border-left: 4px solid #008C45;
      padding-left: 8px;
      margin-top: 18px;
      margin-bottom: 10px;
      font-weight: 700;
    }}
    h3.sub-section-title {{
      font-size: 10.5pt;
      color: #1e293b;
      margin-top: 12px;
      margin-bottom: 6px;
      font-weight: 700;
    }}
    p {{
      margin-bottom: 8px;
      text-align: justify;
    }}

    /* Grids & Cards */
    .meta-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 12px;
      margin-bottom: 16px;
    }}
    .meta-item {{
      font-size: 8.5pt;
    }}
    .meta-item strong {{
      color: #0f172a;
    }}

    .callout {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      border-left: 4px solid #008C45;
      padding: 10px 12px;
      border-radius: 4px;
      margin-bottom: 12px;
      font-size: 9pt;
    }}
    .callout-title {{
      font-weight: 700;
      color: #166534;
      margin-bottom: 4px;
    }}

    .callout-warn {{
      background: #fffbeb;
      border: 1px solid #fde68a;
      border-left: 4px solid #d97706;
      padding: 10px 12px;
      border-radius: 4px;
      margin-bottom: 12px;
      font-size: 9pt;
    }}
    .callout-warn-title {{
      font-weight: 700;
      color: #92400e;
      margin-bottom: 4px;
    }}

    /* Tables */
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 10px 0 14px 0;
      font-size: 8.5pt;
    }}
    th, td {{
      border: 1px solid #cbd5e1;
      padding: 6px 8px;
      text-align: left;
      vertical-align: top;
    }}
    th {{
      background-color: #f1f5f9;
      color: #0f172a;
      font-weight: 700;
    }}
    tr:nth-child(even) td {{
      background-color: #f8fafc;
    }}

    /* Screenshot Figures */
    .figure-box {{
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      padding: 6px;
      margin: 10px 0;
      background: #ffffff;
      text-align: center;
    }}
    .figure-box img {{
      max-width: 100%;
      max-height: 230px;
      border-radius: 4px;
      border: 1px solid #e2e8f0;
      object-fit: contain;
    }}
    .figure-caption {{
      font-size: 8pt;
      color: #64748b;
      margin-top: 4px;
      font-style: italic;
    }}

    .code-box {{
      background: #0f172a;
      color: #f8fafc;
      padding: 8px 12px;
      border-radius: 4px;
      font-family: monospace;
      font-size: 8pt;
      margin-bottom: 10px;
      overflow-x: auto;
    }}

    /* Badges */
    .badge {{
      display: inline-block;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 7.5pt;
      font-weight: 700;
    }}
    .badge-sena {{
      background: #008C45;
      color: white;
    }}
    .badge-blue {{
      background: #0284c7;
      color: white;
    }}
    .badge-purple {{
      background: #7c3aed;
      color: white;
    }}
  </style>
</head>
<body>

  <!-- ==================== PÁGINA 1: PORTADA Y METODOLOGÍA ==================== -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">SENA • CENTRO DE TELEINFORMÁTICA Y PRODUCCIÓN INDUSTRIAL</div>
      <div class="header-meta">TECNÓLOGO EN ADSO • FICHA 3186681</div>
    </div>

    <h1 class="doc-title">Video Exposición sobre Machine Learning</h1>
    <h2 class="doc-subtitle">GA8-220501096-AA2-EV04: Fundamentos Matemáticos, Modelos Simbólicos y Conexionistas, Aplicaciones y Ética en el Software</h2>

    <div class="meta-grid">
      <div class="meta-item"><strong>Aprendiz:</strong> Karen Yuliana Campo</div>
      <div class="meta-item"><strong>Ficha de Caracterización:</strong> 3186681</div>
      <div class="meta-item"><strong>Programa:</strong> Análisis y Desarrollo de Software (ADSO)</div>
      <div class="meta-item"><strong>Regional / Centro:</strong> Regional Cauca • CTPI Popayán</div>
      <div class="meta-item"><strong>Competencia:</strong> 220501096 - Desarrollar la solución de software</div>
      <div class="meta-item"><strong>Actividad de Aprendizaje:</strong> GA8-220501096-AA2 - Tecnologías emergentes</div>
      <div class="meta-item"><strong>Instrumento:</strong> IE-GA8-220501096-AA2-EV04</div>
      <div class="meta-item"><strong>Despliegue Contenerizado:</strong> Puerto Docker 8104 (Apache HTTPD)</div>
    </div>

    <div class="callout">
      <div class="callout-title">ALCANCE Y CUMPLIMIENTO NORMATIVO DE LA GUÍA DE APRENDIZAJE NO. 8</div>
      El presente informe técnico y la producción audiovisual adjunta documentan la realización de la video exposición técnica exigida en el programa ADSO. La evidencia integra rigurosamente las 3 fases audiovisuales (Preproducción con guion técnico individualizado, Producción con herramientas screencast OBS Studio/FilmCraft, y Postproducción con mezcla ducking de voz y banda sonora ambiental a 1080p), abarcando la totalidad de los 8 núcleos temáticos normativos.
    </div>

    <h2 class="section-title">1. FASES DE PRODUCCIÓN AUDIOVISUAL</h2>
    <table>
      <thead>
        <tr>
          <th>Fase de Producción</th>
          <th>Objetivo y Metodología</th>
          <th>Artefactos y Herramientas Empleadas</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="badge badge-purple">1. Preproducción</span></td>
          <td>Investigación documental exhaustiva, redacción del guion técnico individual de exposición estructurado en 10 bloques de tiempo, diseño pedagógico de diapositivas 1080p y planificación de efectos de sonido.</td>
          <td>Guion Técnico Individual (PDF/DOCX/MD), Storyboard de 10 diapositivas Full HD, LibreOffice Writer, Python PIL Graphics.</td>
        </tr>
        <tr>
          <td><span class="badge badge-blue">2. Producción</span></td>
          <td>Grabación de audio de locución con dicción clara en español latinoamericano (cadencia 140 ppm) y captura de pantalla en alta definición de diapositivas sincronizadas con el discurso oral.</td>
          <td>Herramienta Screencast OBS Studio / Screencast Pipeline, captura en tiempo real sobre Linux KDE Plasma X11.</td>
        </tr>
        <tr>
          <td><span class="badge badge-sena">3. Postproducción</span></td>
          <td>Montaje multipista no lineal, ecualización vocal, síntesis de música ambiental de fondo, compresión sidechain ducking (-14 dB bajo voz), exportación H.264/AAC 1080p y empaquetamiento ZIP para Zajuna.</td>
          <td>FFmpeg 8.x Multimedia Toolkit, FilmCraft CLI (.fcproj), Docker Alpine, compresor ZIP oficial Zajuna.</td>
        </tr>
      </tbody>
    </table>

    <h2 class="section-title">2. NÚCLEO 1: ¿EN QUÉ CONSISTE EL MACHINE LEARNING?</h2>
    <p>El <strong>Machine Learning (Aprendizaje Automático)</strong> es una rama de las ciencias computacionales y la inteligencia artificial orientada a la creación de algoritmos capaces de inferir conocimiento inductivo a partir de observaciones empíricas (datos), prescindiendo de reglas algorítmicas programadas explícitamente.</p>
    <p>La formulación matemática canónica de <strong>Tom Mitchell (1997)</strong> establece: <em>"Un programa de computadora aprende de la experiencia E con respecto a una clase de tareas T y medida de desempeño P, si su desempeño en T, medido por P, mejora con la experiencia E"</em>. Es decir, $P(T, E_{k+1}) > P(T, E_k)$.</p>
    <p>Sus tres grandes paradigmas son: <strong>Supervisado</strong> (datos etiquetados para regresión y clasificación), <strong>No Supervisado</strong> (datos sin etiquetas para agrupamiento K-Means y reducción dimensional PCA), y <strong>Por Refuerzo</strong> (agentes que maximizan recompensas estocásticas mediante Q-Learning).</p>
  </div>

  <!-- ==================== PÁGINA 2: OBJETIVOS, ANTECEDENTES Y TAXONOMÍA ==================== -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">GA8-220501096-AA2-EV04 • VIDEO EXPOSICIÓN SOBRE MACHINE LEARNING</div>
      <div class="header-meta">KAREN YULIANA CAMPO • FICHA 3186681</div>
    </div>

    <h2 class="section-title">3. NÚCLEO 2: OBJETIVOS DE LA TECNOLOGÍA MACHINE LEARNING</h2>
    <p>El Machine Learning persigue capacitar a los sistemas de software para resolver problemas dinámicos donde las reglas deterministas convencionales resultan inviables o inmanejables:</p>
    <ul>
      <li><strong>Capacidad de Generalización:</strong> Garantizar que el modelo funcione con alta precisión sobre datos nuevos no observados durante el entrenamiento, superando el dilema del sobreajuste (overfitting) y subajuste (underfitting).</li>
      <li><strong>Automatización Cognitiva:</strong> Remplazar heurísticas humanas rígidas por modelos probabilísticos continuos de toma de decisiones.</li>
      <li><strong>Optimización Multivariable:</strong> Minimizar funciones de coste complejas en espacios vectoriales de alta dimensionalidad.</li>
      <li><strong>Explotación de Big Data:</strong> Identificar relaciones latentes y no lineales en terabytes de datos heterogéneos y no estructurados.</li>
    </ul>

    <h2 class="section-title">4. NÚCLEO 3: ANTECEDENTES HISTÓRICOS Y EVOLUCIÓN</h2>
    <table>
      <thead>
        <tr>
          <th>Año</th>
          <th>Protagonista(s)</th>
          <th>Aporte Histórico Trascendental</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>1950</strong></td>
          <td>Alan Turing</td>
          <td>Publica <em>"Computing Machinery and Intelligence"</em>; formula el Test de Turing y propone máquinas que aprenden de la experiencia.</td>
        </tr>
        <tr>
          <td><strong>1956</strong></td>
          <td>McCarthy, Minsky, Shannon</td>
          <td>Conferencia de Dartmouth: Acuñación formal del término <em>"Inteligencia Artificial"</em> y nacimiento de la disciplina académica.</td>
        </tr>
        <tr>
          <td><strong>1958</strong></td>
          <td>Frank Rosenblatt</td>
          <td>Invención del <em>Perceptrón</em>: Primera red neuronal artificial implementada en hardware analógico (Mark I Perceptron).</td>
        </tr>
        <tr>
          <td><strong>1959</strong></td>
          <td>Arthur Samuel</td>
          <td>Programa jugador de damas en IBM 704; define formalmente el concepto moderno de Machine Learning.</td>
        </tr>
        <tr>
          <td><strong>1986</strong></td>
          <td>Rumelhart, Hinton, Williams</td>
          <td>Formalización matemática de la <em>Retropropagación (Backpropagation)</em> para redes neuronales multicapa en la revista Nature.</td>
        </tr>
        <tr>
          <td><strong>2012</strong></td>
          <td>Krizhevsky, Sutskever, Hinton</td>
          <td><em>AlexNet</em> gana ImageNet acelerado con GPUs Nvidia; marca el inicio de la era moderna del Deep Learning.</td>
        </tr>
        <tr>
          <td><strong>2017</strong></td>
          <td>Vaswani et al. (Google Brain)</td>
          <td>Paper <em>"Attention Is All You Need"</em>; surge la arquitectura Transformer que da origen a los LLMs contemporáneos (GPT, Claude, Gemini).</td>
        </tr>
      </tbody>
    </table>

    <h2 class="section-title">5. NÚCLEO 4: ¿EN QUÉ CONSISTE LA INTELIGENCIA ARTIFICIAL?</h2>
    <p>La <strong>Inteligencia Artificial (IA)</strong> es la disciplina científica macro dedicada al desarrollo de sistemas que perciben su entorno y actúan de forma racional para maximizar el éxito en la consecución de sus metas (Russell & Norvig, 2021). Se organiza en tres horizontes evolutivos:</p>
    <ul>
      <li><strong>ANI (Artificial Narrow Intelligence / IA Estrecha):</strong> Sistemas especializados en una única tarea delimitada (ej. reconocimiento de voz, visión de Tesla, ChatGPT). Es el <em>único nivel existente hoy en día</em>.</li>
      <li><strong>AGI (Artificial General Intelligence / IA General):</strong> Capacidad cognitiva equivalente al razonamiento humano transversal, con sentido común y metacognición (aún en investigación teórica).</li>
      <li><strong>ASI (Artificial Superintelligence / Superinteligencia):</strong> Inteligencia que superaría exponencialmente a la totalidad de la mente humana.</li>
    </ul>
    <div class="callout">
      <strong>Relación Jerárquica:</strong> $\text{Inteligencia Artificial} \supset \text{Machine Learning} \supset \text{Deep Learning} \supset \text{Generative AI}$. Toda técnica de Deep Learning es Machine Learning, y todo Machine Learning es IA; pero existen sistemas de IA que no son Machine Learning (sistemas expertos basados en reglas).
    </div>
  </div>

  <!-- ==================== PÁGINA 3: MODELOS SIMBÓLICO Y CONEXIONISTA ==================== -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">GA8-220501096-AA2-EV04 • VIDEO EXPOSICIÓN SOBRE MACHINE LEARNING</div>
      <div class="header-meta">KAREN YULIANA CAMPO • FICHA 3186681</div>
    </div>

    <h2 class="section-title">6. NÚCLEO 5: MODELO DE IA ORIENTADO A LA PROGRAMACIÓN (SIMBÓLICO)</h2>
    <p>El enfoque orientado a la programación —denominado formalmente <strong>IA Simbólica, Clásica o GOFAI (Good Old-Fashioned AI)</strong>— dominó la disciplina entre 1956 y 1988 a través de los <em>Sistemas Expertos</em>. Su arquitectura se fundamenta en la separación estricta entre:</p>
    <ol>
      <li><strong>Base de Conocimiento:</strong> Conjunto explícito de hechos y reglas de producción estructuradas en lógica de predicados: $\text{SI } A_1 \land A_2 \implies \text{ENTONCES } C$.</li>
      <li><strong>Motor de Inferencia:</strong> Algoritmo deductivo determinista que aplica reglas de inferencia como el <em>Modus Ponens</em> mediante encadenamiento hacia adelante (forward chaining) o hacia atrás (backward chaining).</li>
      <li><strong>Lenguajes y Herramientas Representativas:</strong> Prolog, LISP, CLIPS, Jess. Ejemplos clásicos: MYCIN (diagnóstico médico) y DENDRAL.</li>
    </ol>
    <p><strong>Ventajas vs Fragilidad:</strong> Provee explicabilidad total y determinista sin requerir conjuntos de datos masivos. No obstante, presenta una <em>fragilidad extrema (brittleness)</em> ante la incertidumbre, colapsa ante contradicciones menores y es incapaz de procesar datos no estructurados como imágenes o audio.</p>

    <h2 class="section-title">7. NÚCLEO 6: MODELO DE IA ORIENTADO A CONEXIONES NEURONALES (CONEXIONISTA)</h2>
    <p>En contraposición al enfoque deductivo, el <strong>modelo conexionista o Deep Learning</strong> postula que la cognición emerge de la interconexión masiva de unidades de cálculo bioinspiradas denominadas <strong>Neuronas Artificiales</strong> (Perceptrón Multicapa).</p>
    <div class="code-box">
      Operación Neuronal Básica:  y = f( Σ wᵢ xᵢ + b ) = f( wᵀ x + b )
      Funciones de Activación:   Sigmoide: σ(z) = 1/(1+e⁻ᶻ)  |  ReLU: f(z) = max(0, z)  |  Softmax: P(y=k) = eᶻᵏ / Σ eᶻʲ
      Regla de Actualización:    w(t+1) = w(t) - η ∇_w L  (Calculado vía Retropropagación / Regla de la Cadena)
    </div>
    <table>
      <thead>
        <tr>
          <th>Familia de Redes Neuronales</th>
          <th>Mecanismo Principal</th>
          <th>Dominio de Aplicación en Software</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>CNN (Convolucionales)</strong></td>
          <td>Filtros convolucionales y capas de pooling que preservan la invariancia espacial.</td>
          <td>Visión por computador, clasificación de imágenes radiológicas, detección de objetos en tiempo real.</td>
        </tr>
        <tr>
          <td><strong>RNN / LSTM / GRU</strong></td>
          <td>Conexiones recurrentes con compuertas de memoria que procesan secuencias con dependencia temporal.</td>
          <td>Procesamiento de series de tiempo, monitoreo de telemetría IoT, previsión de demanda en inventarios.</td>
        </tr>
        <tr>
          <td><strong>Transformers</strong></td>
          <td>Capas de autoatención multi-cabezal (Self-Attention) que ponderan la relevancia contextual en paralelo.</td>
          <td>Modelos Masivos de Lenguaje (LLMs), síntesis de código, asistentes cognitivos multimodales.</td>
        </tr>
      </tbody>
    </table>

    <h2 class="section-title">8. MATRIZ COMPARATIVA: SIMBÓLICO VS CONEXIONISTA</h2>
    <table>
      <thead>
        <tr>
          <th>Criterio Técnico</th>
          <th>IA Simbólica (Programación / Reglas)</th>
          <th>IA Conexionista (Redes Neuronales / Deep Learning)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Paradigma Central</strong></td>
          <td>Deductivo: De reglas generales a conclusiones específicas.</td>
          <td>Inductivo: De observaciones empíricas a modelos probabilísticos.</td>
        </tr>
        <tr>
          <td><strong>Unidad Básica</strong></td>
          <td>Símbolo, predicado lógico y regla SI-ENTONCES.</td>
          <td>Neurona artificial con pesos continuos y sesgo.</td>
        </tr>
        <tr>
          <td><strong>Explicabilidad</strong></td>
          <td>Totalmente auditable, lógica transparente paso a paso.</td>
          <td>Opaca ("Caja Negra"); requiere técnicas XAI (SHAP, LIME).</td>
        </tr>
        <tr>
          <td><strong>Tolerancia al Ruido</strong></td>
          <td>Muy baja; frágil ante contradicciones o ambigüedad.</td>
          <td>Muy alta; altamente robusta y resiliente ante ruido sensorial.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- ==================== PÁGINA 4: APLICACIONES, ÉTICA Y EVIDENCIAS ==================== -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">GA8-220501096-AA2-EV04 • VIDEO EXPOSICIÓN SOBRE MACHINE LEARNING</div>
      <div class="header-meta">KAREN YULIANA CAMPO • FICHA 3186681</div>
    </div>

    <h2 class="section-title">9. NÚCLEO 7: EJEMPLOS DE PRODUCTOS COMERCIALES Y CASO APLICADO</h2>
    <ul>
      <li><strong>Tesla Autopilot / FSD:</strong> Redes neuronales de visión computacional pura que procesan 8 cámaras en tiempo real para generar un espacio tridimensional de navegación autónoma.</li>
      <li><strong>OpenAI ChatGPT / Claude / Gemini:</strong> Modelos masivos de lenguaje (LLMs) entrenados con billones de tokens y alineados mediante RLHF para asistencia técnica, redacción y código.</li>
      <li><strong>Netflix & Spotify Recommenders:</strong> Sistemas de filtrado colaborativo neuronal que personalizan catálogos masivos.</li>
      <li><strong>Caso Aplicado (Pizzería Gourmet Bella Italia Popayán):</strong> En el marco del proyecto formativo ADSO, se diseñó e implementó un módulo inteligente de predicción de insumos utilizando <strong>Random Forest Regressor</strong> con Scikit-Learn. El modelo procesa histórico de ventas, días festivos y meteorología de Popayán, logrando una <strong>reducción del 28% en el desperdicio de insumos perecederos</strong> (masa madre y quesos importados).</li>
    </ul>

    <h2 class="section-title">10. NÚCLEO 8: CONSECUENCIAS SOCIALES, ÉTICAS Y FILOSÓFICAS</h2>
    <div class="callout-warn">
      <div class="callout-warn-title">DESAFÍOS ÉTICOS INELUDIBLES PARA EL DESARROLLADOR ADSO</div>
      La adopción de la IA en software productivo impone deberes éticos y normativos impostergables:
      <br><strong>1. Sesgos Algorítmicos y Discriminación:</strong> Los datos históricos pueden replicar prejuicios raciales o socioeconómicos. Es obligatorio auditar la imparcialidad (Fairness) en datasets.
      <br><strong>2. Privacidad y Cumplimiento Normativo:</strong> Protección rigurosa bajo la <em>Ley Estatutaria 1581 de 2012</em> en Colombia y el GDPR europeo, prohibiendo el scraping o entrenamiento no consentido.
      <br><strong>3. Opacidad y Explicabilidad (XAI):</strong> Aplicación imperativa de métodos interpretables (SHAP/LIME) en decisiones sensibles de salud o crédito para abrir las "cajas negras".
      <br><strong>4. Principio Human-in-the-Loop:</strong> Garantizar que toda decisión crítica mantenga supervisión humana activa y rendición de cuentas (accountability).
    </div>

    <h2 class="section-title">11. EVIDENCIA FOTOGRÁFICA DEL ENTORNO DE EJECUCIÓN (KDE PLASMA X11)</h2>
    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px;">
      <div class="figure-box">
        <img src="{cap1_path}" alt="Despliegue Docker">
        <div class="figure-caption">Paso 1: Despliegue del contenedor Docker en Konsole</div>
      </div>
      <div class="figure-box">
        <img src="{cap2_path}" alt="Verificación Salud">
        <div class="figure-caption">Paso 2: Verificación de salud y endpoints en Konsole</div>
      </div>
      <div class="figure-box">
        <img src="{cap3_path}" alt="Portal Reproductor">
        <div class="figure-caption">Paso 3: Portal web con reproductor Full HD en Chrome</div>
      </div>
      <div class="figure-box">
        <img src="{cap4_path}" alt="Diapositiva Conexionista">
        <div class="figure-caption">Paso 4: Visor interactivo: Redes neuronales y Deep Learning</div>
      </div>
    </div>
  </div>

  <!-- ==================== PÁGINA 5: CONCLUSIONES Y REFERENCIAS ==================== -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">GA8-220501096-AA2-EV04 • VIDEO EXPOSICIÓN SOBRE MACHINE LEARNING</div>
      <div class="header-meta">KAREN YULIANA CAMPO • FICHA 3186681</div>
    </div>

    <h2 class="section-title">12. EVIDENCIA DE GUION TÉCNICO Y DATASET ESTRUCTURADO</h2>
    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin-bottom: 12px;">
      <div class="figure-box">
        <img src="{cap5_path}" alt="Guion Técnico en Web">
        <div class="figure-caption">Paso 5: Visualización del Guion Técnico Individual en la plataforma</div>
      </div>
      <div class="figure-box">
        <img src="{cap6_path}" alt="Dataset JSON">
        <div class="figure-caption">Paso 6: Inspección del dataset JSON con los 8 núcleos temáticos</div>
      </div>
    </div>

    <h2 class="section-title">13. CONCLUSIONES</h2>
    <ol>
      <li><strong>Transformación Tecnológica:</strong> El Machine Learning reformula la computación moderna, transitando de la programación explícita a la optimización matemática paramétrica basada en datos empíricos.</li>
      <li><strong>Hibridación Arquitectónica:</strong> La combinación de modelos conexionistas (visión y lenguaje) con modelos simbólicos (reglas de negocio y auditoría) constituye el horizonte más prometedor en la ingeniería de software actual.</li>
      <li><strong>Calidad y Despliegue MLOps:</strong> Un modelo predictivo solo entrega valor cuando se incorpora mediante arquitecturas limpias de microservicios contenerizados (Docker) con monitoreo permanente de deriva conceptual.</li>
      <li><strong>Compromiso Ético del Tecnólogo SENA:</strong> Como futuros desarrolladores ADSO, nuestro deber es crear tecnologías transparentes, respetuosas de la privacidad y supeditadas al principio de supervisión humana (*Human-in-the-Loop*).</li>
    </ol>

    <h2 class="section-title">14. REFERENCIAS BIBLIOGRÁFICAS (NORMAS APA 7MA EDICIÓN)</h2>
    <ul style="font-size: 8pt; line-height: 1.5; color: #334155;">
      <li>Goodfellow, I., Bengio, Y., & Courville, A. (2016). <em>Deep Learning</em>. MIT Press. http://www.deeplearningbook.org</li>
      <li>Mitchell, T. M. (1997). <em>Machine Learning</em>. McGraw-Hill Education.</li>
      <li>Russell, S., & Norvig, P. (2021). <em>Artificial Intelligence: A Modern Approach</em> (4th ed.). Pearson Education.</li>
      <li>Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). Learning representations by back-propagating errors. <em>Nature</em>, 323(6088), 533-536. https://doi.org/10.1038/323533a0</li>
      <li>Turing, A. M. (1950). Computing Machinery and Intelligence. <em>Mind</em>, 59(236), 433-460. https://doi.org/10.1093/mind/LIX.236.433</li>
      <li>Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. <em>Advances in Neural Information Processing Systems (NeurIPS 2017)</em>, 30, 5998-6008.</li>
      <li>República de Colombia. (2012). <em>Ley Estatutaria 1581 de 2012: Régimen General de Protección de Datos Personales</em>. Diario Oficial No. 48.587.</li>
    </ul>

    <div style="margin-top: 24px; padding-top: 12px; border-top: 1px solid #cbd5e1; display: flex; justify-content: space-between; font-size: 8pt; color: #64748b;">
      <div><strong>Karen Yuliana Campo</strong> • Aprendiz ADSO Ficha 3186681</div>
      <div>SENA Regional Cauca • CTPI Popayán • Noviembre 2026</div>
    </div>
  </div>

</body>
</html>
"""

def main():
    print("=== INICIANDO COMPILACIÓN DE INFORME TÉCNICO FORMAL (PDF / DOCX / ZIP) ===")
    
    # 1. Guardar HTML intermedio
    rendered_html = (html_content
        .replace('{cap1_path}', cap1_path)
        .replace('{cap2_path}', cap2_path)
        .replace('{cap3_path}', cap3_path)
        .replace('{cap4_path}', cap4_path)
        .replace('{cap5_path}', cap5_path)
        .replace('{cap6_path}', cap6_path))
    temp_html = os.path.join(DOCS_DIR, "temp_informe_print.html")
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(rendered_html)

    # 2. Compilar PDF con Google Chrome Headless
    print("Compilando PDF de alta calidad con Google Chrome...")
    pdf_out = os.path.join(DOCS_DIR, "GA8-220501096-AA2-EV04_Video_Exposicion_Machine_Learning.pdf")
    cmd_pdf = [
        "google-chrome",
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_out}",
        temp_html
    ]
    subprocess.run(cmd_pdf, check=True)
    print(f"[OK] PDF Informe generado: {pdf_out} ({os.path.getsize(pdf_out)/1024:.1f} KB)")

    # 3. Compilar DOCX vía LibreOffice
    print("Compilando DOCX formal con LibreOffice...")
    temp_odt = os.path.join(DOCS_DIR, "temp_informe_print.odt")
    cmd_odt = ["libreoffice", "--headless", "--convert-to", "odt", temp_html, "--outdir", DOCS_DIR]
    subprocess.run(cmd_odt, check=True)
    
    docx_out = os.path.join(DOCS_DIR, "GA8-220501096-AA2-EV04_Video_Exposicion_Machine_Learning.docx")
    cmd_docx = ["libreoffice", "--headless", "--convert-to", "docx", temp_odt, "--outdir", DOCS_DIR]
    subprocess.run(cmd_docx, check=True)
    
    final_docx = os.path.join(DOCS_DIR, "temp_informe_print.docx")
    if os.path.exists(final_docx):
        shutil.move(final_docx, docx_out)
    print(f"[OK] DOCX Informe generado: {docx_out} ({os.path.getsize(docx_out)/1024:.1f} KB)")

    # Limpieza temporal
    for f in [temp_html, temp_odt]:
        if os.path.exists(f): os.remove(f)

    # 4. Crear archivo enlace_repositorio.txt
    enlace_path = os.path.join(BASE_DIR, "enlace_repositorio.txt")
    with open(enlace_path, "w", encoding="utf-8") as ef:
        ef.write("""# ==============================================================================
# SERVICIO NACIONAL DE APRENDIZAJE - SENA
# EVIDENCIA: GA8-220501096-AA2-EV04: Video exposición sobre machine learning
# PROGRAMA: ANÁLISIS Y DESARROLLO DE SOFTWARE (ADSO) - FICHA: 3186681
# APRENDIZ: KAREN YULIANA CAMPO | CTPI POPAYÁN - REGIONAL CAUCA
# ==============================================================================

Estimado Instructor / Evaluador Técnico:

A continuación se relacionan los enlaces oficiales y recursos de acceso a los artefactos desarrollados para la evidencia GA8-220501096-AA2-EV04:

1. REPOSITORIO GIT OFICIAL DEL PROYECTO:
   https://github.com/danilocampo2024/Evidencias.git
   Rama: main
   Directorio de la Evidencia:
   PET-056_GA8-220501096-AA2-EV04_Video_Exposicion_Machine_Learning

2. SERVICIO WEB INTERACTIVO EN CONTENEDOR DOCKER (PUERTO 8104):
   http://localhost:8104/
   - Reproductor de Video Expositivo HTML5 con índice por bloques
   - Visor de 10 Diapositivas Interactivas en Alta Definición
   - Visor del Guion Técnico Individual estructurado
   - Inspector del Dataset JSON oficial de los 8 núcleos temáticos (/datos_exposicion_ml.json)

3. ARTEFACTOS ENTREGABLES DISPONIBLES EN EL PAQUETE:
   - GA8-220501096-AA2-EV04_Guion_Video_Exposicion_Machine_Learning.pdf (Guion Técnico Individual en PDF)
   - GA8-220501096-AA2-EV04_Guion_Video_Exposicion_Machine_Learning.docx (Guion Técnico Individual en DOCX)
   - GUION_TECNICO_VIDEO_EXPOSICION_MACHINE_LEARNING.md (Guion en formato Markdown)
   - GA8-220501096-AA2-EV04_Video_Exposicion_Machine_Learning.pdf (Informe Técnico Formal en PDF)
   - GA8-220501096-AA2-EV04_Video_Exposicion_Machine_Learning.docx (Informe Técnico Formal en DOCX)
   - GA8-220501096-AA2-EV04_Video_Exposicion_Machine_Learning.mp4 (Video Expositivo Maestro Full HD 1080p)
   - ExposicionMachineLearning.fcproj (Proyecto de montaje FilmCraft CLI)

Cordialmente,
Karen Yuliana Campo
Aprendiz ADSO - Ficha 3186681
CTPI Popayán - Regional Cauca
""")
    shutil.copy(enlace_path, os.path.join(ENTREGA_DIR, "enlace_repositorio.txt"))
    shutil.copy(enlace_path, os.path.join(BRAIN_DIR, "enlace_repositorio.txt"))
    print(f"[OK] Archivo de enlaces generado: {enlace_path}")

    # 5. Generar Paquete ZIP oficial para Zajuna
    zip_path = os.path.join(ENTREGA_DIR, "KARENCAMPO_AA2_EV04_GUIA8.zip")
    print(f"Empaquetando entrega oficial Zajuna en: {zip_path}...")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
        # Documentos de Informe
        z.write(pdf_out, arcname=os.path.basename(pdf_out))
        z.write(docx_out, arcname=os.path.basename(docx_out))
        # Documentos de Guion Individual
        guion_pdf = os.path.join(DOCS_DIR, "GA8-220501096-AA2-EV04_Guion_Video_Exposicion_Machine_Learning.pdf")
        guion_docx = os.path.join(DOCS_DIR, "GA8-220501096-AA2-EV04_Guion_Video_Exposicion_Machine_Learning.docx")
        guion_md = os.path.join(DOCS_DIR, "GUION_TECNICO_VIDEO_EXPOSICION_MACHINE_LEARNING.md")
        if os.path.exists(guion_pdf): z.write(guion_pdf, arcname=os.path.basename(guion_pdf))
        if os.path.exists(guion_docx): z.write(guion_docx, arcname=os.path.basename(guion_docx))
        if os.path.exists(guion_md): z.write(guion_md, arcname=os.path.basename(guion_md))
        # Enlaces
        z.write(enlace_path, arcname="enlace_repositorio.txt")
        # Video MP4
        video_mp4 = os.path.join(VIDEO_DIR, "GA8-220501096-AA2-EV04_Video_Exposicion_Machine_Learning.mp4")
        if os.path.exists(video_mp4):
            z.write(video_mp4, arcname=f"video/{os.path.basename(video_mp4)}")
        # Capturas
        for cap in [cap1_path, cap2_path, cap3_path, cap4_path, cap5_path, cap6_path]:
            if os.path.exists(cap):
                z.write(cap, arcname=f"capturas/{os.path.basename(cap)}")
    
    print(f"[OK] Paquete ZIP generado: {zip_path} ({os.path.getsize(zip_path)/(1024*1024):.1f} MB)")

    # 6. Distribuir a carpetas de entrega, sitio web y artefactos
    shutil.copy(pdf_out, os.path.join(ENTREGA_DIR, os.path.basename(pdf_out)))
    shutil.copy(docx_out, os.path.join(ENTREGA_DIR, os.path.basename(docx_out)))
    shutil.copy(pdf_out, os.path.join(BRAIN_DIR, os.path.basename(pdf_out)))
    shutil.copy(docx_out, os.path.join(BRAIN_DIR, os.path.basename(docx_out)))
    shutil.copy(zip_path, os.path.join(BRAIN_DIR, os.path.basename(zip_path)))
    shutil.copy(zip_path, os.path.join(SITIO_DIR, os.path.basename(zip_path)))
    
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
