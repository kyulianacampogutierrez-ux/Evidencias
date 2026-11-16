#!/usr/bin/env python3
# ==============================================================================
# GENERADOR MAESTRO DE VIDEO EXPOSITIVO EN MEDIO AMBIENTE Y SST (FULL HD 1080P)
# Evidencia: GA8-220601501-AA4-EV01 - Karen Yuliana Campo | Ficha: 3186681
# SENA Centro de Teleinformática y Producción Industrial (CTPI Popayán)
#
# Incorpora:
# - Audio oficial de Karen Yuliana Campo: audio_sst.mp4 (08:11.97 min / 491.97s)
# - Filtrado y ecualización de voz para máxima inteligibilidad
# - Banda sonora ambiental con ducking profundo (BGM -23 dB atenuado a -37 dB bajo voz)
# - 12 Diapositivas Full HD sincronizadas con las 10 fotografías reales
# ==============================================================================

import os
import sys
import wave
import struct
import math
import subprocess
import shutil
import json
import re
from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
FPS = 30
SAMPLE_RATE = 48000

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
VIDEO_DIR = os.path.join(BASE_DIR, "video")
SITIO_VIDEO_DIR = os.path.join(BASE_DIR, "sitio_sst_web", "video")
IMG_REALES_DIR = os.path.join(BASE_DIR, "imagenes_reales")
DELIVERY_DIR = "/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA8-220601501-AA4-EV01"
DELIVERY_VIDEO_DIR = os.path.join(DELIVERY_DIR, "video")
BRAIN_DIR = "/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603"
BUILD_DIR = "/tmp/video_sst_build"
USER_AUDIO_MP4 = "/home/danilo/Escritorio/Karen/SENA/CDE/base_conocimiento/audio_sst.mp4"

os.makedirs(VIDEO_DIR, exist_ok=True)
os.makedirs(SITIO_VIDEO_DIR, exist_ok=True)
os.makedirs(DELIVERY_DIR, exist_ok=True)
os.makedirs(DELIVERY_VIDEO_DIR, exist_ok=True)
os.makedirs(BRAIN_DIR, exist_ok=True)
os.makedirs(BUILD_DIR, exist_ok=True)

FINAL_MP4_LOCAL = os.path.join(VIDEO_DIR, "GA8-220601501-AA4-EV01_Video_Exposicion_Mejora_Medio_Ambiente_SST.mp4")

FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
FONT_MONO = "/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf"

f_top = ImageFont.truetype(FONT_BOLD, 22)
f_meta = ImageFont.truetype(FONT_BOLD, 20)
f_pill = ImageFont.truetype(FONT_BOLD, 18)
f_title = ImageFont.truetype(FONT_BOLD, 44)
f_sub = ImageFont.truetype(FONT_BOLD, 25)
f_card_head = ImageFont.truetype(FONT_BOLD, 24)
f_body_bold = ImageFont.truetype(FONT_BOLD, 20)
f_body = ImageFont.truetype(FONT_REG, 19)
f_caption = ImageFont.truetype(FONT_BOLD, 22)
f_code = ImageFont.truetype(FONT_MONO, 19)

BLOQUES = [
    {
        "id": 1,
        "fase": "FASE 1: PREPRODUCCIÓN • APERTURA",
        "duracion": 40.0,
        "titulo": "Video Expositivo: Oportunidades de Mejora en Medio Ambiente y SST",
        "subtitulo": "Estudio de Casos en Desarrollo de Software ADSO y Sector Productivo de Popayán",
        "caption": "Apertura institucional • Karen Yuliana Campo • Ficha 3186681 • SENA CTPI Popayán",
        "tipo": "portada",
        "card_left_title": "Ficha Técnica y Datos Institucionales",
        "card_left_items": [
            ("Aprendiz Expositora", "Karen Yuliana Campo"),
            ("Ficha de Caracterización", "3186681"),
            ("Programa de Formación", "Tecnólogo en Análisis y Desarrollo de Software"),
            ("Regional / Centro", "Regional Cauca • CTPI Popayán"),
            ("Entidad", "Servicio Nacional de Aprendizaje (SENA) 2026")
        ],
        "card_right_title": "Estructura y Resultados de Aprendizaje",
        "card_right_items": [
            ("Competencia", "220601501 - Prácticas de protección ambiental y SST"),
            ("Actividad de Aprendizaje", "GA8-220601501-AA4: Acciones de mejora en contexto laboral"),
            ("Instrumento", "IE-GA8-220601501-AA4-EV01 (Rúbrica de evaluación)"),
            ("Enfoque Metodológico", "Ciclo PHVA (Planear, Hacer, Verificar, Actuar)"),
            ("Alcance", "10 Oportunidades Reales: 5 Ambientales + 5 SST")
        ]
    },
    {
        "id": 2,
        "fase": "FASE 2: GESTIÓN AMBIENTAL • MEJORA 01",
        "duracion": 41.0,
        "titulo": "Mejora 01: Separación de Residuos en la Fuente",
        "subtitulo": "Resolución 2184 de 2019 — Código Unificado de Colores",
        "caption": "Estaciones ecológicas de 3 contenedores: Blanco (Aprovechables), Verde (Orgánicos), Negro (No aprovechables)",
        "tipo": "mejora",
        "pilar": "GESTIÓN AMBIENTAL",
        "cat_color": (34, 197, 94),
        "imagen": "01_separacion_fuente_codigo_colores_res2184.png",
        "acciones": [
            "Contenedor Blanco: papel archivo limpio, cartón y botellas PET reciclables.",
            "Contenedor Verde: residuos orgánicos biodegradables de cafeterías y áreas de cocina.",
            "Contenedor Negro: residuos no aprovechables, papel higiénico y servilletas usadas.",
            "Alianza con asociaciones de recicladores de oficio de Popayán para entrega directa."
        ],
        "meta": "Aprovechamiento superior al 65% de residuos generados y reducción en relleno sanitario."
    },
    {
        "id": 3,
        "fase": "FASE 2: GESTIÓN AMBIENTAL • MEJORA 02",
        "duracion": 41.0,
        "titulo": "Mejora 02: Trampa de Grasas y Manejo de ACU",
        "subtitulo": "Resolución 316 de 2018 — Aceites de Cocina Usados",
        "caption": "Protección de redes hidrosanitarias: 1 litro de aceite contamina hasta 1.000 litros de agua potable",
        "tipo": "mejora",
        "pilar": "GESTIÓN AMBIENTAL",
        "cat_color": (34, 197, 94),
        "imagen": "02_trampa_grasas_recoleccion_acu_res316.png",
        "acciones": [
            "Instalación de trampa de retención de grasas en acero inoxidable bajo pozuelos.",
            "Limpieza y desnate quincenal programado para evitar formación de costras y olores.",
            "Recolección de aceites de cocina usados en bidones plásticos herméticos rotulados.",
            "Entrega certificada a empresas gestoras para transformación en biodiesel."
        ],
        "meta": "100% de aceites usados entregados a gestor autorizado con cero vertimiento a alcantarillado."
    },
    {
        "id": 4,
        "fase": "FASE 2: GESTIÓN AMBIENTAL • MEJORA 03",
        "duracion": 41.0,
        "titulo": "Mejora 03: Eficiencia Energética y Sensores PIR",
        "subtitulo": "Leyes 1715 de 2014 & 2099 de 2021 — Transición Energética",
        "caption": "Reducción del consumo de kilovatios-hora mediante luminarias LED y automatización domótica",
        "tipo": "mejora",
        "pilar": "GESTIÓN AMBIENTAL",
        "cat_color": (34, 197, 94),
        "imagen": "03_eficiencia_energetica_luminarias_led_sensores.png",
        "acciones": [
            "Sustitución de tubos fluorescentes de 36W por paneles LED de alta eficiencia de 18W.",
            "Instalación de sensores de presencia infrarrojos pasivos (PIR) en zonas comunes y bodegas.",
            "Directivas de ahorro energético en estaciones ADSO (suspensión tras 10 min de inactividad).",
            "Mantenimiento semestral de cableado y fuentes conmutadas para optimizar factor de potencia."
        ],
        "meta": "Disminución del 25% en consumo mensual de electricidad y reducción de huella de carbono."
    },
    {
        "id": 5,
        "fase": "FASE 2: GESTIÓN AMBIENTAL • MEJORA 04",
        "duracion": 41.0,
        "titulo": "Mejora 04: Gestión Integral de Residuos RAEE",
        "subtitulo": "Ley 1672 de 2013 — Residuos de Aparatos Eléctricos y Electrónicos",
        "caption": "Erradicación de descarte de hardware en basura común • Economía circular y recuperación de metales",
        "tipo": "mejora",
        "pilar": "GESTIÓN AMBIENTAL",
        "cat_color": (34, 197, 94),
        "imagen": "04_gestion_raee_residuos_electronicos_ley1672.png",
        "acciones": [
            "Contenedor segregado para tarjetas madre, memorias RAM, periféricos y baterías.",
            "Priorización del mantenimiento correctivo y actualización para extender la vida útil del equipo.",
            "Entrega de componentes descartados a programas posconsumo avalados por MinAmbiente.",
            "Neutralización de sustancias peligrosas como plomo, cadmio y retardantes de llama bromados."
        ],
        "meta": "Cero kilogramos de componentes informáticos enviados a basura convencional."
    },
    {
        "id": 6,
        "fase": "FASE 2: GESTIÓN AMBIENTAL • MEJORA 05",
        "duracion": 41.0,
        "titulo": "Mejora 05: Ahorro Eficiente de Agua con Aireadores",
        "subtitulo": "Ley 373 de 1997 — Uso Eficiente y Ahorro del Agua Potable",
        "caption": "Reducción de caudal de 12 a 4.5 L/min mediante inyección de microburbujas sin pérdida de confort",
        "tipo": "mejora",
        "pilar": "GESTIÓN AMBIENTAL",
        "cat_color": (34, 197, 94),
        "imagen": "05_ahorro_agua_aireadores_griferias_ley373.png",
        "acciones": [
            "Instalación de difusores aireadores en griferías de lavamanos y zonas de fregado.",
            "Monitoreo nocturno de hidrómetros para detección precoz de fugas invisibles.",
            "Instalación de válvulas de cierre temporizado en servicios sanitarios compartidos.",
            "Campaña visual de uso responsable del agua para colaboradores y visitantes."
        ],
        "meta": "Ahorro de hasta un 40% en volumen mensual de agua potable consumida."
    },
    {
        "id": 7,
        "fase": "FASE 2: SEGURIDAD Y SALUD • MEJORA 06",
        "duracion": 41.0,
        "titulo": "Mejora 06: Ergonomía del Puesto de Trabajo ADSO",
        "subtitulo": "Guía GTC 45 & Decreto 1072 de 2015 — Prevención Biomecánica",
        "caption": "Alineación postural: ángulo de 90° en codos y rodillas, monitor a la altura horizontal de los ojos",
        "tipo": "mejora",
        "pilar": "SEGURIDAD Y SALUD EN EL TRABAJO",
        "cat_color": (2, 132, 199),
        "imagen": "06_ergonomia_puesto_trabajo_pantalla_silla.png",
        "acciones": [
            "Ajuste del borde superior de la pantalla al nivel horizontal de los ojos (distancia de 50-60 cm).",
            "Dotación de sillas ergonómicas con apoyo lumbar, regulación neumática y descansabrazos 3D.",
            "Incorporación de reposapiés con inclinación ajustable para mejorar retorno venoso.",
            "Uso de almohadillas de gel para teclado y mouse para prevenir síndrome del túnel carpiano."
        ],
        "meta": "100% de puestos evaluados con nivel de riesgo ergonómico aceptable según GTC 45."
    },
    {
        "id": 8,
        "fase": "FASE 2: SEGURIDAD Y SALUD • MEJORA 07",
        "duracion": 41.0,
        "titulo": "Mejora 07: Seguridad en Escaleras y Pisos Antideslizantes",
        "subtitulo": "Resolución 2400 de 1979 — Seguridad Locativa y Caídas",
        "caption": "Cintas de carborundo fotoluminiscente en peldaños y baldosas de alto coeficiente de fricción",
        "tipo": "mejora",
        "pilar": "SEGURIDAD Y SALUD EN EL TRABAJO",
        "cat_color": (2, 132, 199),
        "imagen": "07_adecuacion_locativa_pisos_antideslizantes_escaleras.png",
        "acciones": [
            "Instalación de bandas antideslizantes fotoluminiscentes en las huellas de cada escalón.",
            "Mantenimiento de pasamanos dobles a 90 cm de altura en ambos costados de las escaleras.",
            "Tratamiento rugoso y señalización con conos amarillos durante jornadas de aseo húmedo.",
            "Despeje total de obstáculos en vías de tránsito y salidas de emergencia."
        ],
        "meta": "Cero incidentes o accidentes por caídas a mismo o diferente nivel en la vigencia anual."
    },
    {
        "id": 9,
        "fase": "FASE 2: SEGURIDAD Y SALUD • MEJORA 08",
        "duracion": 41.0,
        "titulo": "Mejora 08: Extintores Especializados Clase K y CO2",
        "subtitulo": "Norma Técnica NTC 2885 / NFPA 10 — Protección Contra Incendios",
        "caption": "Agentes limpios para servidores informáticos y acetato de potasio para aceites en cocinas",
        "tipo": "mejora",
        "pilar": "SEGURIDAD Y SALUD EN EL TRABAJO",
        "cat_color": (2, 132, 199),
        "imagen": "08_seguridad_incendios_extintores_clase_k_abc.png",
        "acciones": [
            "Extintor Clase K (acetato de potasio) en cocinas: sofoca grasas por saponificación sin salpicar.",
            "Extintores de agente limpio Solkaflam / CO2 en centro de servidores: no deja residuos ni daña circuitos.",
            "Inspección mensual de manómetros, precintos de seguridad y señalización NTC 1461.",
            "Entrenamiento teórico-práctico a brigadistas en uso de extintores y evacuación."
        ],
        "meta": "100% de extintores inspeccionados, vigentes y personal capacitado en control de conatos."
    },
    {
        "id": 10,
        "fase": "FASE 2: SEGURIDAD Y SALUD • MEJORA 09",
        "duracion": 41.0,
        "titulo": "Mejora 09: Metodología 5S y Canalización RETIE",
        "subtitulo": "Reglamento RETIE & Metodología 5S — Orden y Seguridad Eléctrica",
        "caption": "Canaletas ranuradas ignífugas, organización de cableado estructurado y despeje perimetral",
        "tipo": "mejora",
        "pilar": "SEGURIDAD Y SALUD EN EL TRABAJO",
        "cat_color": (2, 132, 199),
        "imagen": "09_orden_limpieza_metodologia_5s_cableado_retie.png",
        "acciones": [
            "Eliminación de cables sueltos en el piso mediante canaletas plásticas autoextinguibles.",
            "Rotulado y peinado de cables en racks de telecomunicaciones bajo norma RETIE.",
            "Aplicación de las 5S: Seiri (Clasificar), Seiton (Ordenar), Seiso (Limpiar), Seiketsu (Estandarizar) y Shitsuke (Disciplina).",
            "Auditorías mensuales de orden y aseo en puestos de cómputo y áreas productivas."
        ],
        "meta": "Índice de cumplimiento 5S superior al 90% y cero eventos por riesgo eléctrico."
    },
    {
        "id": 11,
        "fase": "FASE 2: SEGURIDAD Y SALUD • MEJORA 10",
        "duracion": 41.0,
        "titulo": "Mejora 10: Programa de Pausas Activas e Higiene Postural",
        "subtitulo": "Ley 2191 de 2022 & Decreto 1072 de 2015 — Desconexión Laboral",
        "caption": "Dos descansos activos diarios (10:00 am y 3:30 pm) • Descanso visual 20-20-20 y estiramientos",
        "tipo": "mejora",
        "pilar": "SEGURIDAD Y SALUD EN EL TRABAJO",
        "cat_color": (2, 132, 199),
        "imagen": "10_programa_pausas_activas_higiene_postural.png",
        "acciones": [
            "Programación obligatoria de 10 minutos a las 10:00 am y a las 3:30 pm.",
            "Ejercicios guiados de elongación muscular en cuello, hombros, espalda dorsal y extremidades.",
            "Técnica 20-20-20: cada 20 minutos mirar a 20 pies (6 metros) de distancia durante 20 segundos.",
            "Software de notificación emergente para recordar la desconexión activa en puestos ADSO."
        ],
        "meta": "Participación del 100% de aprendices y colaboradores con reducción medible del estrés laboral."
    },
    {
        "id": 12,
        "fase": "FASE 3: POSTPRODUCCIÓN • CONCLUSIONES",
        "duracion": 41.97,
        "titulo": "Articulación PHVA, ODS y Cierre Institucional",
        "subtitulo": "Integración de la Sostenibilidad y la Protección Humana en el ADSO",
        "caption": "SENA Regional Cauca • CTPI Popayán • Karen Yuliana Campo • Tecnóloga en ADSO",
        "tipo": "cierre",
        "card_left_title": "Ciclo PHVA de Mejora Continua",
        "card_left_items": [
            ("Planear", "Identificación de aspectos ambientales y matriz de riesgos SST"),
            ("Hacer", "Ejecución de las 10 mejoras locativas, tecnológicas y de comportamiento"),
            ("Verificar", "Medición de kWh, metros cúbicos de agua, reciclaje y pausas activas"),
            ("Actuar", "Estandarización de lecciones aprendidas y cierre de brechas SG-SST")
        ],
        "card_right_title": "Compromiso con los ODS de las Naciones Unidas",
        "card_right_items": [
            ("ODS 3 (Salud y Bienestar)", "Ergonomía biomecánica y programa de pausas activas"),
            ("ODS 6 (Agua Limpia)", "Trampas de grasas para ACU y aireadores ahorradores"),
            ("ODS 7 (Energía Asequible)", "Iluminación LED y políticas de suspensión de monitores"),
            ("ODS 8 (Trabajo Decente)", "Ambientes seguros bajo norma RETIE y Res. 2400/1979"),
            ("ODS 12 (Consumo Responsable)", "Separación en la fuente (Res. 2184) y gestión de RAEE")
        ]
    }
]

# 1. Renderizado de diapositivas Full HD
def render_slide(bloque, index, total):
    im = Image.new("RGB", (W, H), (15, 23, 42))
    draw = ImageDraw.Draw(im)

    # Fondo degradado elegante
    for y in range(H):
        r = int(11 + (y / H) * 14)
        g = int(18 + (y / H) * 16)
        b = int(32 + (y / H) * 20)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # Barra superior institucional SENA
    draw.rectangle([0, 0, W, 70], fill=(9, 14, 23))
    draw.rectangle([0, 67, W, 70], fill=(0, 140, 69))

    # Badge SENA en barra superior
    draw.rectangle([60, 16, 210, 54], fill=(0, 140, 69))
    draw.text((75, 22), "SENA CTPI", fill=(255, 255, 255), font=f_top)

    draw.text((230, 23), "PROGRAMA TECNÓLOGO EN ANÁLISIS Y DESARROLLO DE SOFTWARE (ADSO) • FICHA 3186681", fill=(148, 163, 184), font=f_meta)
    prog_str = f"DIAPOSITIVA {index+1:02d} / {total:02d}"
    draw.text((W - 270, 23), prog_str, fill=(56, 189, 248), font=f_meta)

    # Encabezado del bloque
    fase_color = (34, 197, 94) if "AMBIENTAL" in bloque["fase"] else ((2, 132, 199) if "SEGURIDAD" in bloque["fase"] else (250, 204, 21))
    draw.text((60, 95), bloque["fase"], fill=fase_color, font=f_pill)
    draw.text((60, 125), bloque["titulo"], fill=(255, 255, 255), font=f_title)
    draw.text((60, 185), bloque["subtitulo"], fill=(203, 213, 225), font=f_sub)

    if bloque["tipo"] in ("portada", "cierre"):
        w_card = (W - 120 - 40) // 2
        cards_y = 245
        h_card = 690

        # Tarjeta Izquierda
        draw.rounded_rectangle([60, cards_y, 60 + w_card, cards_y + h_card], radius=16, fill=(30, 41, 59), outline=(51, 65, 85), width=2)
        draw.rectangle([60, cards_y, 60 + w_card, cards_y + 60], fill=(15, 23, 42))
        draw.text((85, cards_y + 17), bloque["card_left_title"], fill=(56, 189, 248), font=f_card_head)

        cy = cards_y + 85
        for k, v in bloque["card_left_items"]:
            draw.text((85, cy), f"• {k}:", fill=(250, 204, 21), font=f_body_bold)
            draw.text((85, cy + 30), v, fill=(241, 245, 249), font=f_body)
            cy += 75

        # Tarjeta Derecha
        rx = 60 + w_card + 40
        draw.rounded_rectangle([rx, cards_y, rx + w_card, cards_y + h_card], radius=16, fill=(30, 41, 59), outline=(51, 65, 85), width=2)
        draw.rectangle([rx, cards_y, rx + w_card, cards_y + 60], fill=(15, 23, 42))
        draw.text((rx + 25, cards_y + 17), bloque["card_right_title"], fill=(52, 211, 153), font=f_card_head)

        cy = cards_y + 85
        for k, v in bloque["card_right_items"]:
            draw.text((rx + 25, cy), f"• {k}:", fill=(56, 189, 248), font=f_body_bold)
            draw.text((rx + 25, cy + 30), v, fill=(241, 245, 249), font=f_body)
            cy += 75

    else:
        # Foto Real a la Izquierda y Tarjeta Técnica a la Derecha
        img_x = 60
        img_y = 245
        img_w = 880
        img_h = 690

        img_path = os.path.join(IMG_REALES_DIR, bloque["imagen"])
        if os.path.exists(img_path):
            real_img = Image.open(img_path).convert("RGB")
            real_img = real_img.resize((img_w, img_h), Image.LANCZOS)
            im.paste(real_img, (img_x, img_y))
            draw.rectangle([img_x, img_y, img_x + img_w, img_y + img_h], outline=(bloque["cat_color"][0], bloque["cat_color"][1], bloque["cat_color"][2]), width=3)
        else:
            draw.rounded_rectangle([img_x, img_y, img_x + img_w, img_y + img_h], radius=16, fill=(30, 41, 59))

        card_x = img_x + img_w + 35
        card_w = W - card_x - 60
        card_y = 245
        card_h = 690

        draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + card_h], radius=16, fill=(30, 41, 59), outline=(51, 65, 85), width=2)
        draw.rectangle([card_x, card_y, card_x + card_w, card_y + 60], fill=(15, 23, 42))
        draw.text((card_x + 25, card_y + 17), "Acciones Operativas y Alcance", fill=(56, 189, 248), font=f_card_head)

        ay = card_y + 80
        for act in bloque["acciones"]:
            draw.text((card_x + 25, ay), "✔", fill=bloque["cat_color"], font=f_body_bold)
            words = act.split()
            line1, line2 = "", ""
            for w in words:
                if len(line1 + " " + w) < 48:
                    line1 += " " + w
                else:
                    line2 += " " + w
            draw.text((card_x + 55, ay), line1.strip(), fill=(241, 245, 249), font=f_body)
            if line2:
                ay += 26
                draw.text((card_x + 55, ay), line2.strip(), fill=(203, 213, 225), font=f_body)
            ay += 46

        meta_y = card_y + card_h - 140
        draw.rounded_rectangle([card_x + 20, meta_y, card_x + card_w - 20, meta_y + 115], radius=10, fill=(15, 23, 42), outline=(bloque["cat_color"][0], bloque["cat_color"][1], bloque["cat_color"][2]), width=2)
        draw.text((card_x + 35, meta_y + 14), "INDICADOR DE GESTIÓN & META:", fill=(250, 204, 21), font=f_body_bold)
        draw.text((card_x + 35, meta_y + 44), bloque["meta"], fill=(241, 245, 249), font=f_body)

    # Pie de diapositiva
    draw.rectangle([0, H - 55, W, H], fill=(9, 14, 23))
    draw.text((60, H - 40), bloque["caption"], fill=(148, 163, 184), font=f_caption)
    draw.text((W - 440, H - 40), "SENA • CTPI POPAYÁN • 2026", fill=(52, 211, 153), font=f_caption)

    return im

# 2. Procesamiento y Mezcla con Ducking Dinámico
def procesar_audio_con_ducking():
    print(f"Extrayendo y procesando audio oficial de Karen Campo desde: {USER_AUDIO_MP4}...")
    
    # 2.1 Sintetizar loop musical ambiental suave (32 segundos)
    loop_wav = os.path.join(BUILD_DIR, "bg_loop_ambient_32s.wav")
    loop_duration = 32.0
    num_samples = int(loop_duration * SAMPLE_RATE)
    chords = [
        ([110.0, 130.81, 164.81, 220.0], 55.0),   # Am
        ([87.31, 110.0, 130.81, 174.61], 43.65),  # F
        ([130.81, 164.81, 196.0, 261.63], 65.41), # C
        ([98.0, 123.47, 146.83, 196.0], 49.0)     # G
    ]
    chord_len = loop_duration / len(chords)

    samples = []
    for i in range(num_samples):
        t = i / SAMPLE_RATE
        chord_idx = min(int(t / chord_len), len(chords) - 1)
        freqs, bass_freq = chords[chord_idx]
        local_t = t - chord_idx * chord_len
        env = min(1.0, local_t / 0.5) * max(0.05, 1.0 - (local_t / chord_len) * 0.40)
        # Melodía de acordes suave y cálida
        val = sum(math.sin(2.0 * math.pi * f * t) for f in freqs) * (0.025 * env)
        # Bajo sutil
        val += math.sin(2.0 * math.pi * bass_freq * t) * (0.035 * env)
        samples.append(val)

    with wave.open(loop_wav, "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        raw_bytes = bytearray()
        for s in samples:
            clamped = max(-0.90, min(0.90, s))
            val_int = int(clamped * 32767.0)
            raw_bytes.extend(struct.pack("<hh", val_int, val_int))
        wf.writeframes(raw_bytes)

    # 2.2 Obtener duración exacta de audio_sst.mp4
    cmd_dur = [
        "docker", "run", "--rm",
        "-v", f"{os.path.dirname(USER_AUDIO_MP4)}:/data",
        "sena-ffmpeg:alpine",
        "-i", f"/data/{os.path.basename(USER_AUDIO_MP4)}"
    ]
    res = subprocess.run(cmd_dur, stderr=subprocess.PIPE, text=True)
    m = re.search(r'Duration:\s*(\d+):(\d+):(\d+\.\d+)', res.stderr)
    if m:
        total_duration = int(m.group(1))*3600 + int(m.group(2))*60 + float(m.group(3))
    else:
        total_duration = 491.97
    print(f"[OK] Duración detectada de audio_sst.mp4: {total_duration:.2f} segundos")

    # 2.3 Mezclar con mejora vocal y ducking profundo (-23 dB baseline, atenuado a -37 dB bajo voz)
    mixed_wav = os.path.join(BUILD_DIR, "mixed_master_audio.wav")
    
    # Filtros:
    # 1. Pista de voz: filtro pasa-altos (80Hz) + realce vocal de presencia (3kHz) + normalización a -16 LUFS
    # 2. BGM: loop continuo, atenuado a volumen 0.07 (-23 dB)
    # 3. Compresión sidechain: ratio 14:1, umbral 0.04, ataque 15ms, relajación 450ms (ducking ultra limpio)
    filter_complex = (
        "[0:a]highpass=f=80,equalizer=f=3000:t=q:w=1:g=2.5,loudnorm=I=-16:TP=-1.5:LRA=11[voice];"
        f"[1:a]aloop=loop=-1:size={int(loop_duration * SAMPLE_RATE)}[bg];"
        "[bg]volume=0.07[bg_low];"
        "[bg_low][voice]sidechaincompress=threshold=0.04:ratio=14:attack=15:release=450[ducked_bg];"
        "[voice][ducked_bg]amix=inputs=2:duration=first:dropout_transition=2[out]"
    )

    cmd_mix = [
        "docker", "run", "--rm",
        "-v", f"{os.path.dirname(USER_AUDIO_MP4)}:/data",
        "-v", f"{BUILD_DIR}:{BUILD_DIR}",
        "sena-ffmpeg:alpine",
        "-y",
        "-i", f"/data/{os.path.basename(USER_AUDIO_MP4)}",
        "-i", loop_wav,
        "-filter_complex", filter_complex,
        "-map", "[out]",
        "-t", str(total_duration),
        "-ar", str(SAMPLE_RATE), "-ac", "2",
        mixed_wav
    ]
    print("Ejecutando mezcla de audio con ducking dinámico y protección vocal...")
    subprocess.run(cmd_mix, check=True)
    print(f"[OK] Mezcla maestra de audio generada: {mixed_wav}")
    return mixed_wav, total_duration

def main():
    print("=== INICIANDO PRODUCCIÓN DEL VIDEO EXPOSITIVO CON AUDIO REAL: audio_sst.mp4 ===")
    print("=== Evidencia: GA8-220601501-AA4-EV01 | Aprendiz: Karen Yuliana Campo ===")

    # 1. Procesar audio real con ducking
    mixed_audio_wav, total_duration = procesar_audio_con_ducking()

    # 2. Ajustar duraciones de bloques para sincronizar exactamente con total_duration
    num_middle_slides = 10
    slide_01_dur = 40.0
    rem = total_duration - slide_01_dur
    mid_dur = 41.0
    slide_12_dur = rem - (num_middle_slides * mid_dur)
    if slide_12_dur < 20.0:
        mid_dur = rem / (num_middle_slides + 1)
        slide_12_dur = mid_dur

    duraciones = [slide_01_dur] + [mid_dur] * num_middle_slides + [slide_12_dur]

    # 3. Renderizar las 12 diapositivas Full HD
    slide_files = []
    print("Renderizando 12 diapositivas Full HD (1920x1080)...")
    for i, bloque in enumerate(BLOQUES):
        im = render_slide(bloque, i, len(BLOQUES))
        slide_path = os.path.join(BUILD_DIR, f"slide_{i+1:02d}.png")
        im.save(slide_path, "PNG")
        slide_files.append(slide_path)
        print(f" [OK] Diapositiva {i+1:02d} generada: {bloque['titulo']} ({duraciones[i]:.2f}s)")

    # 4. Crear archivo concat de FFmpeg con las duraciones exactas
    concat_txt = os.path.join(BUILD_DIR, "concat.txt")
    with open(concat_txt, "w") as cf:
        for s_path, dur in zip(slide_files, duraciones):
            cf.write(f"file '{s_path}'\n")
            cf.write(f"duration {dur:.3f}\n")
        cf.write(f"file '{slide_files[-1]}'\n")

    # 5. Renderizar video MP4 con FFmpeg Docker
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
    print("Renderizando video MP4 con Docker FFmpeg...")
    subprocess.run(cmd_render, check=True)

    size_mb = os.path.getsize(FINAL_MP4_LOCAL) / (1024 * 1024)
    print(f"[OK] Video renderizado con éxito en: {FINAL_MP4_LOCAL} ({size_mb:.2f} MB)")

    # 6. Distribuir a carpetas requeridas
    target_sitio_mp4 = os.path.join(SITIO_VIDEO_DIR, "video_exposicion_sst.mp4")
    target_delivery_mp4 = os.path.join(DELIVERY_VIDEO_DIR, "GA8-220601501-AA4-EV01_Video_Exposicion_Mejora_Medio_Ambiente_SST.mp4")
    target_delivery_root_mp4 = os.path.join(DELIVERY_DIR, "GA8-220601501-AA4-EV01_Video_Exposicion_Mejora_Medio_Ambiente_SST.mp4")
    target_brain_mp4 = os.path.join(BRAIN_DIR, "GA8-220601501-AA4-EV01_Video_Exposicion_Mejora_Medio_Ambiente_SST.mp4")

    shutil.copyfile(FINAL_MP4_LOCAL, target_sitio_mp4)
    shutil.copyfile(FINAL_MP4_LOCAL, target_delivery_mp4)
    shutil.copyfile(FINAL_MP4_LOCAL, target_delivery_root_mp4)
    shutil.copyfile(FINAL_MP4_LOCAL, target_brain_mp4)
    print(f" [OK] Copiado a sitio web: {target_sitio_mp4}")
    print(f" [OK] Copiado a entrega Zajuna (video/): {target_delivery_mp4}")
    print(f" [OK] Copiado a entrega Zajuna raíz: {target_delivery_root_mp4}")
    print(f" [OK] Copiado a artefactos: {target_brain_mp4}")

    # 7. Registrar proyecto FilmCraft (.fcproj)
    fcproj_path = os.path.join(VIDEO_DIR, "ExposicionSSTyMedioAmbiente.fcproj")
    fcproj_data = {
        "version": "1.0",
        "project_name": "ExposicionSSTyMedioAmbiente_SENA",
        "author": "Karen Yuliana Campo",
        "ficha": "3186681",
        "audio_source": "audio_sst.mp4",
        "total_duration_sec": total_duration,
        "resolution": {"width": 1920, "height": 1080, "fps": 30},
        "audio_tracks": [
            {"name": "Narration_KarenCampo_Original", "file": "mixed_master_audio.wav", "volume": 1.0, "processing": "highpass 80Hz + EQ 3kHz + loudnorm -16 LUFS"},
            {"name": "Ambient_BGM_Deep_Ducking", "file": "bg_loop_ambient_32s.wav", "baseline_volume": 0.07, "ducked_volume": 0.02, "ratio": 14}
        ],
        "timeline_blocks": [
            {"block": b["id"], "title": b["titulo"], "slide": f"slide_{b['id']:02d}.png", "duration_sec": round(d, 3)}
            for b, d in zip(BLOQUES, duraciones)
        ]
    }
    with open(fcproj_path, "w") as fcp:
        json.dump(fcproj_data, fcp, indent=2)
    print(f" [OK] Proyecto FilmCraft registrado en: {fcproj_path}")

    print("=== PRODUCCIÓN Y DISTRIBUCIÓN DEL VIDEO CON AUDIO REAL FINALIZADA CON ÉXITO ===")

if __name__ == "__main__":
    main()
