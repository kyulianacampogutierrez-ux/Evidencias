#!/usr/bin/env python3
"""
Generador Maestro del Video Expositivo sobre Machine Learning (Full HD 1080p 16:9)
Evidencia: GA8-220501096-AA2-EV04
Aprendiz: Karen Yuliana Campo - SENA ADSO Ficha 3186681
Centro: Centro de Teleinformática y Producción Industrial (CTPI) - Popayán

Incorpora:
- Audio oficial de Karen Yuliana Campo: audio_machine_learning.mp4 (8 min 38.59 s)
- Banda sonora ambiental sintetizada con ducking dinámico FFmpeg (-18 dB bajo voz)
- 10 Diapositivas gráficas Full HD sincronizadas con los 10 bloques de la exposición
- Renderizado Full HD 1080p H.264 / AAC 48kHz
- Proyecto FilmCraft (.fcproj) complementario
"""

import os
import sys
import wave
import struct
import math
import subprocess
import shutil
from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
FPS = 30
SAMPLE_RATE = 44100

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
VIDEO_DIR = os.path.join(BASE_DIR, "video")
SITIO_VIDEO_DIR = os.path.join(BASE_DIR, "sitio_ml_web", "video")
SITIO_CAPTURAS_DIR = os.path.join(BASE_DIR, "sitio_ml_web", "capturas")
DELIVERY_DIR = "/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA8-220501096-AA2-EV04"
DELIVERY_VIDEO_DIR = os.path.join(DELIVERY_DIR, "video")
BRAIN_DIR = "/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603"
BUILD_DIR = "/tmp/video_ml_build"
USER_AUDIO_MP4 = "/home/danilo/Escritorio/Karen/SENA/CDE/base_conocimiento/audio_machine_learning.mp4"

os.makedirs(VIDEO_DIR, exist_ok=True)
os.makedirs(SITIO_VIDEO_DIR, exist_ok=True)
os.makedirs(SITIO_CAPTURAS_DIR, exist_ok=True)
os.makedirs(DELIVERY_DIR, exist_ok=True)
os.makedirs(DELIVERY_VIDEO_DIR, exist_ok=True)
os.makedirs(BRAIN_DIR, exist_ok=True)
os.makedirs(BUILD_DIR, exist_ok=True)

FINAL_MP4_LOCAL = os.path.join(VIDEO_DIR, "GA8-220501096-AA2-EV04_Video_Exposicion_Machine_Learning.mp4")

FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
FONT_MONO = "/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf"

f_top = ImageFont.truetype(FONT_BOLD, 22)
f_meta = ImageFont.truetype(FONT_BOLD, 20)
f_pill = ImageFont.truetype(FONT_BOLD, 18)
f_title = ImageFont.truetype(FONT_BOLD, 46)
f_sub = ImageFont.truetype(FONT_BOLD, 26)
f_card_head = ImageFont.truetype(FONT_BOLD, 26)
f_body_bold = ImageFont.truetype(FONT_BOLD, 21)
f_body = ImageFont.truetype(FONT_REG, 20)
f_caption = ImageFont.truetype(FONT_BOLD, 22)
f_code = ImageFont.truetype(FONT_MONO, 20)

BLOQUES = [
    {
        "id": 1,
        "fase": "FASE 1: PREPRODUCCIÓN • APERTURA",
        "duracion": 35.0,
        "titulo": "Video Exposición: Machine Learning",
        "subtitulo": "Fundamentos Matemáticos, Modelos de IA, Aplicaciones y Ética en el Software",
        "caption": "Apertura institucional • Karen Yuliana Campo • Ficha 3186681 • ADSO SENA Popayán",
        "card_left_title": "Ficha Técnica y Datos Institucionales",
        "card_left_items": [
            ("Aprendiz", "Karen Yuliana Campo"),
            ("Ficha de Caracterización", "3186681"),
            ("Programa", "Tecnólogo en Análisis y Desarrollo de Software"),
            ("Regional / Centro", "Regional Cauca • CTPI Popayán"),
            ("Entidad", "Servicio Nacional de Aprendizaje (SENA) 2026")
        ],
        "card_right_title": "Estructura y Resultados de Aprendizaje",
        "card_right_items": [
            ("Competencia", "220501096 - Desarrollar la solución de software"),
            ("Actividad de Aprendizaje", "GA8-220501096-AA2: Tecnologías emergentes y disruptivas"),
            ("Instrumento", "IE-GA8-220501096-AA2-EV04 (Lista de chequeo)"),
            ("Fases Metodológicas", "Preproducción, Producción de screencast y Postproducción"),
            ("Alcance", "8 Núcleos Temáticos rigurosamente demostrados")
        ]
    },
    {
        "id": 2,
        "fase": "FASE 2: PRODUCCIÓN • NÚCLEO TEMÁTICO 1",
        "duracion": 50.0,
        "titulo": "¿En qué consiste el Machine Learning?",
        "subtitulo": "Definición Formal, Paradigmas de Aprendizaje y Ciclo Operativo MLOps",
        "caption": "Definición de Mitchell: Tarea (T), Experiencia (E), Desempeño (P) • Supervisado, No Supervisado y Refuerzo",
        "card_left_title": "Definición Formal de Tom Mitchell (1997)",
        "card_left_items": [
            ("Principio Central", "Mejora del desempeño P en la tarea T mediante experiencia E"),
            ("Supervisado", "Datos etiquetados: Regresión (valores continuos) y Clasificación"),
            ("No Supervisado", "Datos sin etiquetas: Clustering (K-Means, PCA, autoencoders)"),
            ("Por Refuerzo", "Agente, Estado, Acción y Recompensa escalar (Q-Learning)"),
            ("Autosupervisado", "Generación de pseudoetiquetas en secuencias masivas")
        ],
        "card_right_title": "Ciclo de Vida MLOps en Ingeniería de Software",
        "card_right_items": [
            ("1. Ingesta & Limpieza", "Pipelines de extracción ETL y mitigación de nulos"),
            ("2. Feature Engineering", "Normalización, embeddings y reducción dimensional"),
            ("3. Entrenamiento", "Ajuste de hiperparámetros y optimización matemática"),
            ("4. Validación Cruzada", "Métricas: Precision, Recall, F1-Score, RMSE, AUC-ROC"),
            ("5. Despliegue API", "Microservicios contenerizados Docker con inferencia REST")
        ]
    },
    {
        "id": 3,
        "fase": "FASE 2: PRODUCCIÓN • NÚCLEO TEMÁTICO 2",
        "duracion": 53.0,
        "titulo": "Objetivos de la Tecnología Machine Learning",
        "subtitulo": "Capacidades Cognitivas, Generalización y Extracción Automática de Patrones",
        "caption": "Objetivo Primario: Generalización estadística óptima ante datos no vistos (Trade-off Sesgo-Varianza)",
        "card_left_title": "Pilares Operativos del Machine Learning",
        "card_left_items": [
            ("Capacidad de Generalización", "Desempeño robusto en entornos de producción no vistos"),
            ("Automatización Cognitiva", "Reemplazo de heurísticas manuales rígidas por modelos"),
            ("Optimización Continua", "Minimización de funciones de pérdida en tiempo real"),
            ("Escalabilidad Big Data", "Tratamiento de volumen, velocidad, variedad y veracidad"),
            ("Adaptabilidad Dinámica", "Reentrenamiento continuo ante deriva de datos (Concept Drift)")
        ],
        "card_right_title": "Trade-off Fundamental: Sesgo vs Varianza",
        "card_right_items": [
            ("Subajuste (Underfitting)", "Alto sesgo: El modelo es demasiado simple y no aprende"),
            ("Sobreajuste (Overfitting)", "Alta varianza: El modelo memoriza el ruido del dataset"),
            ("Punto Óptimo", "Equilibrio que minimiza el error total de generalización"),
            ("Técnicas de Regularización", "Lasso (L1), Ridge (L2), Dropout, Early Stopping"),
            ("Impacto en Software", "Reducción de incidentes y mantenimiento preventivo")
        ]
    },
    {
        "id": 4,
        "fase": "FASE 2: PRODUCCIÓN • NÚCLEO TEMÁTICO 3",
        "duracion": 66.0,
        "titulo": "Antecedentes Históricos y Evolución de la IA",
        "subtitulo": "Línea de Tiempo: De la Máquina de Turing a la Revolución de los Transformers",
        "caption": "Evolución histórica: 1950 Turing • 1956 Dartmouth • 1958 Perceptrón • 1986 Backprop • 2012 AlexNet • 2017 Transformer",
        "card_left_title": "Fundamentos Pioneros (1950 - 1986)",
        "card_left_items": [
            ("1950 - Alan Turing", "Artículo canónico 'Computing Machinery and Intelligence'"),
            ("1956 - Dartmouth College", "McCarthy, Minsky y Shannon acuñan formalmente 'IA'"),
            ("1958 - Frank Rosenblatt", "Perceptrón: Primera arquitectura de neurona artificial"),
            ("1959 - Arthur Samuel", "Programa jugador de damas y definición de Machine Learning"),
            ("1986 - Rumelhart & Hinton", "Formalización de Retropropagación (Backpropagation)")
        ],
        "card_right_title": "Revolución Moderna y Deep Learning (2012 - 2026)",
        "card_right_items": [
            ("2012 - AlexNet (ImageNet)", "Convoluciones profundas aceleradas por GPUs Nvidia"),
            ("2016 - AlphaGo (DeepMind)", "Aprendizaje por refuerzo vence a campeón mundial de Go"),
            ("2017 - Vaswani et al. (Google)", "Paper 'Attention Is All You Need' y arquitectura Transformer"),
            ("2020 - 2024 Era de LLMs", "GPT-4, Gemini, Claude y modelos multimodales masivos"),
            ("2026 - Agentes Autónomos", "Sistemas integrados de razonamiento y desarrollo guiado")
        ]
    },
    {
        "id": 5,
        "fase": "FASE 2: PRODUCCIÓN • NÚCLEO TEMÁTICO 4",
        "duracion": 60.0,
        "titulo": "¿En qué consiste la Inteligencia Artificial?",
        "subtitulo": "Taxonomía Disciplinar, Niveles Evolutivos y Relación Jerárquica",
        "caption": "Taxonomía IA: ANI (Estrecha / Actual) • AGI (General / Hipotética) • ASI (Superinteligencia)",
        "card_left_title": "Estadios Evolutivos de la Inteligencia Artificial",
        "card_left_items": [
            ("ANI (Narrow AI)", "IA Específica o Débil: Domina una sola tarea concreta (Estado Actual)"),
            ("AGI (General AI)", "Capacidad cognitiva transversal equivalente al ser humano"),
            ("ASI (Super AI)", "Intelecto artificial superior a la suma de toda la humanidad"),
            ("Agente Racional", "Sistema que percibe su entorno y actúa para maximizar éxito"),
            ("Criterio de Russell & Norvig", "Sistemas que piensan/actúan humana o racionalmente")
        ],
        "card_right_title": "Relación Jerárquica de Contención (Euler)",
        "card_right_items": [
            ("1. Inteligencia Artificial (IA)", "Campo superior amplio de razonamiento computacional"),
            ("2. Machine Learning (ML)", "Subcampo centrado en el aprendizaje inductivo con datos"),
            ("3. Deep Learning (DL)", "Subcampo de ML con redes neuronales profundas"),
            ("4. Generative AI (GenAI)", "Modelos probabilísticos de síntesis de texto, código e imagen"),
            ("Diferenciación Clave", "Toda DL es ML, y toda ML es IA; pero no toda IA es ML")
        ]
    },
    {
        "id": 6,
        "fase": "FASE 2: PRODUCCIÓN • NÚCLEO TEMÁTICO 5",
        "duracion": 51.0,
        "titulo": "Modelo IA Orientado a la Programación",
        "subtitulo": "Enfoque Simbólico Clásico (GOFAI), Sistemas Expertos y Deducción Lógica",
        "caption": "Paradigma Simbólico: Base de Hechos + Reglas SI-ENTONCES + Motor de Inferencia (Modus Ponens)",
        "card_left_title": "Arquitectura de los Sistemas Expertos",
        "card_left_items": [
            ("Base de Conocimiento", "Reglas formales: SI <condición> ENTONCES <acción/hecho>"),
            ("Motor de Inferencia", "Encadenamiento hacia adelante (Forward) y hacia atrás"),
            ("Memoria de Trabajo", "Estado actual de los hechos observados en la sesión"),
            ("Módulo de Explicación", "Trazabilidad paso a paso del porqué de cada deducción"),
            ("Lenguajes Canónicos", "Prolog (Lógica de predicados), Lisp, CLIPS, Jess")
        ],
        "card_right_title": "Evaluación Técnica: Fortalezas vs Fragilidad",
        "card_right_items": [
            ("Ventaja: Explicabilidad Total", "100% auditable y determinista en cada conclusión"),
            ("Ventaja: Cero Dependencia Big Data", "Opera perfectamente sin requerir millones de ejemplos"),
            ("Fragilidad Cognitiva", "Incapaz de generalizar ante casos no codificados previamente"),
            ("El Cuello de Botella", "Dificultad extrema para extraer y estructurar el saber humano"),
            ("Fallo ante Ambigüedad", "Colapso total ante ruido sensorial o contradicciones")
        ]
    },
    {
        "id": 7,
        "fase": "FASE 2: PRODUCCIÓN • NÚCLEO TEMÁTICO 6",
        "duracion": 85.0,
        "titulo": "Modelo IA: Conexiones Neuronales",
        "subtitulo": "Enfoque Conexionista Bioinspirado, Redes Profundas y Retropropagación",
        "caption": "Paradigma Conexionista: y = f( Σ w_i * x_i + b ) • Retropropagación del Gradiente (Adam Optimizer)",
        "card_left_title": "La Neurona Artificial (Perceptrón Multicapa)",
        "card_left_items": [
            ("Ecuación Matemática", "y = f( Σ_{i=1}^n w_i * x_i + b )"),
            ("Pesos Sinápticos (w)", "Parámetros ajustables que ponderan la importancia de cada input"),
            ("Sesgo (Bias b)", "Permite desplazar la frontera de activación en el hiperplano"),
            ("Funciones de Activación", "Sigmoide, Tanh, ReLU (Rectified Linear Unit), GELU"),
            ("Mecanismo de Aprendizaje", "Cálculo analítico del gradiente mediante Regla de la Cadena")
        ],
        "card_right_title": "Grandes Familias de Arquitecturas Neuronales",
        "card_right_items": [
            ("CNN (Convolucionales)", "Filtros espaciales y pooling para visión artificial"),
            ("RNN / LSTM / GRU", "Celdas de memoria recurrente para series de tiempo"),
            ("Transformers (Atención)", "Mecanismo Self-Attention paralelo (Q, K, V) sin recurrencia"),
            ("Autoencoders & GANs", "Modelos generativos antagónicos y compresión latente"),
            ("Optimizadores Modernos", "Adam, AdamW, RMSProp con decaimiento de momento")
        ]
    },
    {
        "id": 8,
        "fase": "FASE 2: PRODUCCIÓN • NÚCLEO TEMÁTICO 7",
        "duracion": 35.0,
        "titulo": "Ejemplos Comerciales y Caso Aplicado",
        "subtitulo": "Soluciones de Vanguardia Mundial y Caso Real en Pizzería Bella Italia Popayán",
        "caption": "Productos Globales: Tesla, ChatGPT, Netflix • Caso Aplicado: Random Forest en Bella Italia Popayán",
        "card_left_title": "Productos Comerciales Basados en IA",
        "card_left_items": [
            ("Tesla Autopilot / FSD", "8 cámaras Full HD y redes neuronales profundas de control"),
            ("OpenAI ChatGPT / GPT-4", "Modelos Transformer autoregresivos para lenguaje natural"),
            ("Netflix & Spotify", "Filtrado colaborativo con embeddings neuronales de usuario"),
            ("AlphaFold (Google DeepMind)", "Predicción tridimensional precisa de estructuras proteicas"),
            ("Sistemas de Fraude Bancario", "Modelos de Gradient Boosting (XGBoost) en tiempo real")
        ],
        "card_right_title": "Caso de Aplicación: Bella Italia Popayán",
        "card_right_items": [
            ("Módulo Implementado", "Motor Predictivo de Demanda Diaria de Pizzas Artesanales"),
            ("Algoritmo Empleado", "Random Forest Regressor (Scikit-Learn + Python FastAPI)"),
            ("Variables de Entrada", "Día, clima Popayán, festivos, histórico de comandas"),
            ("Impacto Operativo", "Reducción del 28% en mermas de masa madre y quesos"),
            ("Despliegue Técnico", "Contenedor Docker HTTPD en arquitectura cliente-servidor")
        ]
    },
    {
        "id": 9,
        "fase": "FASE 2: PRODUCCIÓN • NÚCLEO TEMÁTICO 8",
        "duracion": 59.0,
        "titulo": "Consecuencias Sociales, Éticas y Filosóficas",
        "subtitulo": "Responsabilidad Civil, Sesgos Algorítmicos, Privacidad y Human-in-the-Loop",
        "caption": "Ética del Desarrollador: Mitigación de Sesgos • Ley 1581 / GDPR • Explicabilidad XAI • Human-in-the-Loop",
        "card_left_title": "Desafíos Éticos y Regulatorios Críticos",
        "card_left_items": [
            ("Sesgos Algorítmicos (Bias)", "Modelos que replican prejuicios raciales, de género o socioeconómicos"),
            ("Privacidad y Soberanía", "Uso consentido de datos (Ley 1581 de 2012 / GDPR europeo)"),
            ("Transformación del Empleo", "Desplazamiento de tareas rutinarias y reconversión técnica"),
            ("Impacto Energético y Huella", "Alto consumo eléctrico en el preentrenamiento de supermodelos"),
            ("Deepfakes y Desinformación", "Generación no consentida de identidades y noticias falsas")
        ],
        "card_right_title": "Principios para el Tecnólogo en Software ADSO",
        "card_right_items": [
            ("Explicabilidad (XAI)", "Implementación de métodos SHAP y LIME para desmitificar decisiones"),
            ("Principio Human-in-the-Loop", "Supervisión humana obligatoria en fallos judiciales o de salud"),
            ("Auditoría de Datasets", "Validación de representatividad estadística y equidad (Fairness)"),
            ("Seguridad y Resiliencia", "Protección contra ataques adversariales y envenenamiento de datos"),
            ("Ética desde el Diseño", "Integración de postulados bioéticos en el ciclo DevOps")
        ]
    },
    {
        "id": 10,
        "fase": "FASE 3: POSTPRODUCCIÓN • CONCLUSIONES",
        "duracion": 24.59,
        "titulo": "Conclusiones y Cierre Institucional",
        "subtitulo": "Síntesis Pedagógica, Balance Metodológico y Créditos Oficiales ADSO",
        "caption": "Conclusión: El Machine Learning transforma el software moderno • Rigor Técnico y Ética Profesional",
        "card_left_title": "Síntesis de Aprendizajes Clave",
        "card_left_items": [
            ("1. No es Magia, es Álgebra", "Optimización matemática, cálculo vectorial y probabilidad"),
            ("2. Complementariedad de Enfoques", "Simbólico para reglas normativas y Conexionista para percepción"),
            ("3. Ciclo MLOps Riguroso", "El modelo solo es útil cuando se integra a un software estable"),
            ("4. Responsabilidad Ineludible", "El programador responde por el sesgo y la seguridad del algoritmo"),
            ("5. Innovación Regional", "Aplicación viable en empresas caucanas (ej. Bella Italia)")
        ],
        "card_right_title": "Créditos Institucionales de Producción",
        "card_right_items": [
            ("Expositora / Aprendiz", "Karen Yuliana Campo"),
            ("Programa de Formación", "Tecnólogo en Análisis y Desarrollo de Software"),
            ("Ficha de Caracterización", "3186681"),
            ("Regional / Centro", "Regional Cauca • CTPI Popayán"),
            ("Herramientas Utilizadas", "OBS Studio, FFmpeg 8.x, Python PIL, FilmCraft CLI")
        ]
    }
]

def render_slide(bloque, index, total):
    im = Image.new("RGBA", (W, H), (11, 19, 43, 255))
    draw = ImageDraw.Draw(im)

    for y in range(H):
        ratio = y / H
        r = int(11 + 17 * ratio)
        g = int(19 + 22 * ratio)
        b = int(43 + 30 * ratio)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # Top Navigation Banner (Height: 90px)
    draw.rectangle([(0, 0), (W, 90)], fill=(15, 23, 42, 240))
    draw.line([(0, 90), (W, 90)], fill=(57, 169, 0, 255), width=3)

    # Logo SENA circular badge
    draw.ellipse([(45, 18), (99, 72)], fill=(57, 169, 0, 255))
    draw.text((62, 26), "S", fill=(255, 255, 255, 255), font=f_top)

    # Header text
    draw.text((115, 22), "SENA | ADSO Ficha 3186681", fill=(255, 255, 255, 255), font=f_top)
    draw.text((115, 52), "Centro de Teleinformática y Producción Industrial - CTPI Popayán", fill=(148, 163, 184, 255), font=f_meta)

    right_text = "Aprendiz: Karen Yuliana Campo"
    bbox_rt = f_top.getbbox(right_text)
    rt_w = bbox_rt[2] - bbox_rt[0]
    draw.text((W - 45 - rt_w, 22), right_text, fill=(56, 189, 248, 255), font=f_top)
    ev_text = "Evidencia GA8-220501096-AA2-EV04"
    bbox_ev = f_meta.getbbox(ev_text)
    ev_w = bbox_ev[2] - bbox_ev[0]
    draw.text((W - 45 - ev_w, 52), ev_text, fill=(57, 169, 0, 255), font=f_meta)

    # Pill of Phase & Block
    pill_text = f"  {bloque['fase']}  •  BLOQUE {index + 1} DE {total}  "
    bbox_pill = f_pill.getbbox(pill_text)
    pill_w = bbox_pill[2] - bbox_pill[0]
    draw.rounded_rectangle([(45, 115), (45 + pill_w + 10, 150)], radius=6, fill=(57, 169, 0, 200), outline=(255, 255, 255, 100))
    draw.text((50, 122), pill_text, fill=(255, 255, 255, 255), font=f_pill)

    # Titles
    draw.text((45, 165), bloque["titulo"], fill=(255, 255, 255, 255), font=f_title)
    draw.text((45, 225), bloque["subtitulo"], fill=(56, 189, 248, 255), font=f_sub)

    # Body Cards (2 Columns Layout)
    card_y = 285
    card_h = 635
    card_w = 885
    gap = 60

    # Card Left
    draw.rounded_rectangle([(45, card_y), (45 + card_w, card_y + card_h)], radius=14, fill=(30, 41, 59, 230), outline=(51, 65, 85, 255), width=2)
    draw.rounded_rectangle([(45, card_y), (45 + card_w, card_y + 60)], radius=14, fill=(15, 23, 42, 255))
    draw.line([(45, card_y + 60), (45 + card_w, card_y + 60)], fill=(57, 169, 0, 255), width=2)
    draw.text((75, card_y + 16), bloque["card_left_title"], fill=(255, 255, 255, 255), font=f_card_head)

    item_y = card_y + 85
    for label, val in bloque["card_left_items"]:
        draw.text((75, item_y), f"• {label}:", fill=(245, 158, 11, 255), font=f_body_bold)
        draw.text((75, item_y + 28), val, fill=(226, 232, 240, 255), font=f_body)
        item_y += 105

    # Card Right
    rx = 45 + card_w + gap
    draw.rounded_rectangle([(rx, card_y), (rx + card_w, card_y + card_h)], radius=14, fill=(30, 41, 59, 230), outline=(51, 65, 85, 255), width=2)
    draw.rounded_rectangle([(rx, card_y), (rx + card_w, card_y + 60)], radius=14, fill=(15, 23, 42, 255))
    draw.line([(rx, card_y + 60), (rx + card_w, card_y + 60)], fill=(56, 189, 248, 255), width=2)
    draw.text((rx + 30, card_y + 16), bloque["card_right_title"], fill=(255, 255, 255, 255), font=f_card_head)

    item_y = card_y + 85
    for label, val in bloque["card_right_items"]:
        draw.text((rx + 30, item_y), f"• {label}:", fill=(56, 189, 248, 255), font=f_body_bold)
        draw.text((rx + 30, item_y + 28), val, fill=(226, 232, 240, 255), font=f_body)
        item_y += 105

    # Bottom Subtitles Banner (Height: 95px)
    draw.rectangle([(0, H - 125), (W, H - 30)], fill=(10, 15, 29, 245))
    draw.line([(0, H - 125), (W, H - 125)], fill=(51, 65, 85, 255), width=1)
    
    draw.rounded_rectangle([(45, H - 110), (160, H - 45)], radius=6, fill=(57, 169, 0, 220))
    draw.text((58, H - 93), "LOCUCIÓN", fill=(255, 255, 255, 255), font=f_pill)
    draw.text((180, H - 95), bloque["caption"], fill=(255, 255, 255, 255), font=f_caption)

    # Bottom Progress Bar (Height: 30px)
    draw.rectangle([(0, H - 30), (W, H)], fill=(15, 23, 42, 255))
    progress_w = int(W * (index + 1) / total)
    draw.rectangle([(0, H - 30), (progress_w, H)], fill=(57, 169, 0, 255))
    
    prog_label = f"Avance Exposición: Bloque {index + 1} de {total} ({(index + 1)*100//total}%)"
    draw.text((W // 2 - 120, H - 24), prog_label, fill=(255, 255, 255, 255), font=f_meta)

    return im

def build_audio_pipeline():
    """
    1. Extrae karen_voice_raw.wav desde audio_machine_learning.mp4
    2. Genera bucle musical armónico bg_loop.wav (32s)
    3. Mezcla en Docker FFmpeg aplicando filtro sidechaincompress (ducking)
    """
    print(f"--- Procesando locución oficial de Karen Campo desde: {USER_AUDIO_MP4} ---")
    karen_voice_wav = os.path.join(BUILD_DIR, "karen_voice_raw.wav")
    
    # 1. Extraer voz cruda
    cmd_extract = [
        "docker", "run", "--rm",
        "-v", "/home/danilo/Escritorio/Karen/SENA/CDE/base_conocimiento:/data",
        "-v", f"{BUILD_DIR}:/tmp_dir",
        "sena-ffmpeg:alpine",
        "-y", "-i", "/data/audio_machine_learning.mp4",
        "-ar", "44100", "-ac", "2",
        "/tmp_dir/karen_voice_raw.wav"
    ]
    subprocess.run(cmd_extract, check=True)

    with wave.open(karen_voice_wav, 'rb') as wf:
        total_duration = wf.getnframes() / wf.getframerate()
    print(f"Pista de voz extraída: {total_duration:.2f}s ({total_duration/60:.2f} min)")

    # 2. Generar bucle musical de 32 segundos
    loop_wav = os.path.join(BUILD_DIR, "bg_loop.wav")
    total_samples = int(SAMPLE_RATE * 32.0)
    chords = [
        [220.0, 261.63, 329.63, 392.0],  # Am7
        [146.83, 220.0, 261.63, 349.23], # Dm7
        [196.0, 246.94, 293.66, 349.23], # G7
        [130.81, 164.81, 196.0, 246.94], # Cmaj7
        [174.61, 220.0, 261.63, 329.63], # Fmaj7
        [123.47, 146.83, 220.0, 293.66], # Bm7b5
        [164.81, 207.65, 246.94, 293.66], # E7
        [220.0, 261.63, 329.63, 440.0],  # Am
    ]
    chord_duration = 4.0

    samples = []
    for s in range(total_samples):
        t = s / SAMPLE_RATE
        chord_idx = int((t / chord_duration) % len(chords))
        current_chord = chords[chord_idx]
        val = 0.0
        for i, freq in enumerate(current_chord):
            osc = math.sin(2.0 * math.pi * freq * t) * 0.7 + math.sin(4.0 * math.pi * freq * t) * 0.2
            lfo = 0.85 + 0.15 * math.sin(2.0 * math.pi * 0.25 * t + i)
            val += osc * lfo * 0.25
        sample_amp = val * 0.18
        int_val = int(max(-1.0, min(1.0, sample_amp)) * 32767)
        samples.append(int_val)

    with wave.open(loop_wav, 'wb') as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        raw_bytes = struct.pack(f"<{len(samples)*2}h", *[val for val in samples for _ in (0, 1)])
        wf.writeframes(raw_bytes)
    print("Bucle musical sintetizado (32s).")

    # 3. Mezclar con Docker FFmpeg aplicando sidechaincompress (ducking profesional)
    print("Mezclando voz y música con sidechaincompress en FFmpeg...")
    mixed_master_wav = os.path.join(BUILD_DIR, "mixed_master_audio.wav")
    cmd_mix = [
        "docker", "run", "--rm",
        "-v", f"{BUILD_DIR}:/tmp_dir",
        "sena-ffmpeg:alpine",
        "-y",
        "-i", "/tmp_dir/karen_voice_raw.wav",
        "-stream_loop", "-1", "-i", "/tmp_dir/bg_loop.wav",
        "-filter_complex",
        "[1:a]volume=0.20[bg];[bg][0:a]sidechaincompress=threshold=0.035:ratio=10:attack=15:release=250[ducked];[0:a][ducked]amix=inputs=2:weights=1.0 1.0:dropout_transition=0",
        "-t", f"{total_duration:.2f}",
        "/tmp_dir/mixed_master_audio.wav"
    ]
    subprocess.run(cmd_mix, check=True)
    print(f"Pista maestra de audio mezclada lista: {mixed_master_wav}")
    return total_duration, mixed_master_wav

def main():
    print("=== INICIANDO PRODUCCIÓN DEL VIDEO EXPOSITIVO DE MACHINE LEARNING ===")
    print("=== USANDO AUDIO OFICIAL DE KAREN YULIANA CAMPO: audio_machine_learning.mp4 ===")
    
    total_video_duration, mixed_audio_wav = build_audio_pipeline()

    # 2. Renderizar 10 Diapositivas Full HD (1920x1080)
    slide_files = []
    print("Renderizando 10 diapositivas Full HD (1920x1080)...")
    for i, bloque in enumerate(BLOQUES):
        im = render_slide(bloque, i, len(BLOQUES))
        slide_path = os.path.join(BUILD_DIR, f"slide_{i+1:02d}.png")
        im.save(slide_path, "PNG")
        slide_files.append(slide_path)
        print(f" [OK] Diapositiva {i+1:02d} generada: {bloque['titulo']} ({bloque['duracion']}s)")

    # Guardar poster para el reproductor web
    poster_path = os.path.join(SITIO_CAPTURAS_DIR, "poster_video_ml.png")
    shutil.copyfile(slide_files[0], poster_path)
    shutil.copyfile(slide_files[0], os.path.join(BASE_DIR, "capturas", "poster_video_ml.png"))

    # 3. Crear archivo concat de FFmpeg
    durations = [b["duracion"] for b in BLOQUES]
    concat_txt = os.path.join(BUILD_DIR, "concat.txt")
    with open(concat_txt, "w") as cf:
        for s_path, dur in zip(slide_files, durations):
            cf.write(f"file '{s_path}'\n")
            cf.write(f"duration {dur}\n")
        cf.write(f"file '{slide_files[-1]}'\n")

    # 4. Renderizar video MP4 con FFmpeg Docker
    cmd_render = [
        "docker", "run", "--rm",
        "-v", f"{BUILD_DIR}:{BUILD_DIR}",
        "-v", f"{VIDEO_DIR}:{VIDEO_DIR}",
        "sena-ffmpeg:alpine",
        "-y",
        "-f", "concat", "-safe", "0", "-i", concat_txt,
        "-i", mixed_audio_wav,
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "22",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        FINAL_MP4_LOCAL
    ]
    print("Ejecutando renderizado FFmpeg del video con locución real de Karen...")
    subprocess.run(cmd_render, check=True)
    print(f"[OK] Video renderizado con éxito en: {FINAL_MP4_LOCAL}")

    # 5. Distribuir a carpetas requeridas
    target_sitio_mp4 = os.path.join(SITIO_VIDEO_DIR, "video_exposicion_ml.mp4")
    target_delivery_mp4 = os.path.join(DELIVERY_VIDEO_DIR, "GA8-220501096-AA2-EV04_Video_Exposicion_Machine_Learning.mp4")
    target_delivery_root_mp4 = os.path.join(DELIVERY_DIR, "GA8-220501096-AA2-EV04_Video_Exposicion_Machine_Learning.mp4")
    target_brain_mp4 = os.path.join(BRAIN_DIR, "GA8-220501096-AA2-EV04_Video_Exposicion_Machine_Learning.mp4")

    shutil.copyfile(FINAL_MP4_LOCAL, target_sitio_mp4)
    shutil.copyfile(FINAL_MP4_LOCAL, target_delivery_mp4)
    shutil.copyfile(FINAL_MP4_LOCAL, target_delivery_root_mp4)
    shutil.copyfile(FINAL_MP4_LOCAL, target_brain_mp4)
    print(f" [OK] Copiado a sitio web: {target_sitio_mp4}")
    print(f" [OK] Copiado a entrega Zajuna (video/): {target_delivery_mp4}")
    print(f" [OK] Copiado a entrega Zajuna raíz: {target_delivery_root_mp4}")
    print(f" [OK] Copiado a artefactos: {target_brain_mp4}")

    # 6. Generar proyecto FilmCraft complementario (.fcproj)
    fcproj_path = os.path.join(VIDEO_DIR, "ExposicionMachineLearning.fcproj")
    fcproj_data = {
        "version": "1.0",
        "project_name": "ExposicionMachineLearning_SENA",
        "author": "Karen Yuliana Campo",
        "ficha": "3186681",
        "audio_source": "audio_machine_learning.mp4",
        "total_duration_sec": total_video_duration,
        "resolution": {"width": 1920, "height": 1080, "fps": 30},
        "audio_tracks": [
            {"name": "Narration_KarenCampo_Original", "file": "mixed_master_audio.wav", "volume": 1.0},
            {"name": "Ambient_BGM_Ducking", "file": "bg_loop.wav", "volume": 0.20}
        ],
        "timeline_blocks": [
            {"block": b["id"], "title": b["titulo"], "slide": f"slide_{b['id']:02d}.png", "duration_sec": d}
            for b, d in zip(BLOQUES, durations)
        ]
    }
    with open(fcproj_path, "w") as fcp:
        import json
        json.dump(fcproj_data, fcp, indent=2)
    print(f" [OK] Proyecto FilmCraft registrado en: {fcproj_path}")

    print("=== PRODUCCIÓN Y DISTRIBUCIÓN DEL VIDEO CON AUDIO REAL FINALIZADA CON ÉXITO ===")

if __name__ == "__main__":
    main()
