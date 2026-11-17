#!/usr/bin/env python3
# ==============================================================================
# GENERADOR Y EDITOR DEL VIDEO EXPOSITIVO: PROYECTO DE VIDA (GA9-240201526-AA1-EV01)
# Combina el video real de Karen Yuliana Campo (cámara en vivo) con las fotografías
# reales de su familia (mamá y hermano), pareja y mascotas, infografías y música.
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | SENA Regional Cauca - CTPI Popayán
# ==============================================================================

import os
import sys
import shutil
import subprocess
import math
import wave
import struct
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
VIDEO_DIR = os.path.join(BASE_DIR, 'video')
IMG_DIR = os.path.join(BASE_DIR, 'imagenes')
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
ENTREGA_DIR = '/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA9-240201526-AA1-EV01'
ARTIFACT_DIR = '/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603'
RAW_VIDEO = '/home/danilo/Escritorio/Karen/SENA/CDE/base_conocimiento/WhatsApp Video 2026-11-16 at 7.59.04 PM.mp4'

os.makedirs(VIDEO_DIR, exist_ok=True)
os.makedirs(ENTREGA_DIR, exist_ok=True)

BUILD_DIR = '/tmp/video_vida_build'
SLIDES_DIR = os.path.join(BUILD_DIR, 'slides')
os.makedirs(SLIDES_DIR, exist_ok=True)

# Tipografías disponibles
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

font_title = get_font(FONT_BOLD, 26)
font_subtitle = get_font(FONT_BOLD, 19)
font_card_title = get_font(FONT_BOLD, 16)
font_badge = get_font(FONT_BOLD, 13)
font_text = get_font(FONT_REGULAR, 15)
font_subtext = get_font(FONT_REGULAR, 13)
font_small = get_font(FONT_REGULAR, 11)

# Fotos reales
FOTO_KAREN = os.path.join(IMG_DIR, '01_foto_karen_yuliana_campo_retrato.jpg')
FOTO_FAMILIA = os.path.join(IMG_DIR, '02_foto_familia_mama_hermano_karen.jpg')
FOTO_PAREJA = os.path.join(IMG_DIR, '03_foto_pareja_mascotas_karen.jpg')

# 8 Segmentos sincronizados exactamente con el video grabado por Karen (326.57 seg total)
SEGMENTS = [
    {
        "id": 1,
        "name": "slide_01_apertura.png",
        "duration": 38.00,
        "badge": "PROYECTO DE VIDA • ÉTICA Y CULTURA DE PAZ",
        "badge_color": (0, 140, 69), # Verde SENA
        "title": "Mi Proyecto de Vida: Amor Familiar, Propósito y Paz",
        "subtitle": "Evidencia: GA9-240201526-AA1-EV01 | SENA Regional Cauca - CTPI Popayán"
    },
    {
        "id": 2,
        "name": "slide_02_malala.png",
        "duration": 35.00,
        "badge": "INSPIRACIÓN ÉTICA Y DERECHOS HUMANOS",
        "badge_color": (147, 51, 234), # Morado
        "title": "La Voz de Malala Yousafzai y la Cultura de Paz",
        "subtitle": "La educación y la tecnología como puentes para cerrar brechas sociales"
    },
    {
        "id": 3,
        "name": "slide_03_trascendencia.png",
        "duration": 38.00,
        "badge": "NIVEL 1: IDENTIDAD TRASCENDENTE",
        "badge_color": (2, 132, 199), # Azul
        "title": "Espiritualidad, Fe y Propósito Superior",
        "subtitle": "Gratitud diaria, humildad y vocación de servicio al prójimo"
    },
    {
        "id": 4,
        "name": "slide_04_mision_vision.png",
        "duration": 51.00,
        "badge": "NIVEL 2: ROLES, MISIÓN Y VISIÓN DE VIDA",
        "badge_color": (16, 185, 129), # Esmeralda
        "title": "Diseño de Interfaces (UI/UX) e Inteligencia Artificial",
        "subtitle": "Crear experiencias digitales accesibles y éticas que transformen comunidades"
    },
    {
        "id": 5,
        "name": "slide_05_familia_valores.png",
        "duration": 39.00,
        "badge": "NIVEL 3: VALORES Y EL PILAR FAMILIAR",
        "badge_color": (234, 88, 12), # Naranja
        "title": "El Amor de Mamá y el Apoyo de mi Compañero de Vida",
        "subtitle": "Perseverancia materna en el estudio y compañerismo incondicional"
    },
    {
        "id": 6,
        "name": "slide_06_capacidades_dofa.png",
        "duration": 45.00,
        "badge": "NIVEL 4: CAPACIDADES TÉCNICAS Y MATRIZ DOFA",
        "badge_color": (13, 148, 136), # Teal
        "title": "Capacidades en Interfaces, IA y Autodiagnóstico",
        "subtitle": "Fortalezas analíticas, empatía de usuario y superación de la autoexigencia"
    },
    {
        "id": 7,
        "name": "slide_07_habitos_hogar.png",
        "duration": 50.00,
        "badge": "NIVELES 5 Y 6: HÁBITOS, CONVIVENCIA Y MEDIO AMBIENTE",
        "badge_color": (217, 70, 239), # Fucsia
        "title": "El Calor del Hogar: Estudio Diario y Tiempo en Familia",
        "subtitle": "Convivencia armónica con mamá, hermano, pareja, 3 mascotas y cuidado ambiental"
    },
    {
        "id": 8,
        "name": "slide_08_ikigai_cierre.png",
        "duration": 30.57,
        "badge": "ESQUEMA IKIGAI Y CIERRE INSTITUCIONAL",
        "badge_color": (0, 140, 69), # Verde SENA
        "title": "Mi Ikigai: Tecnología con Corazón Humano",
        "subtitle": "Compromiso de vida con Colombia para la construcción de una cultura de paz"
    }
]

def create_base_canvas():
    """Genera el lienzo maestro 1920x1080 con fondo elegante y caja para el video de Karen."""
    img = Image.new("RGB", (1920, 1080), (11, 19, 43)) # Azul noche profundo
    draw = ImageDraw.Draw(img)

    # Gradiente sutil
    for y in range(1080):
        r = int(11 + (y / 1080) * 16)
        g = int(19 + (y / 1080) * 22)
        b = int(43 + (y / 1080) * 25)
        draw.line([(0, y), (1920, y)], fill=(r, g, b))

    # Barra superior institucional (y: 0 a 80)
    draw.rectangle([0, 0, 1920, 80], fill=(15, 23, 42))
    draw.rectangle([0, 77, 1920, 80], fill=(0, 140, 69)) # Línea verde SENA

    # Insignia SENA
    draw.rectangle([45, 18, 120, 62], fill=(0, 140, 69))
    draw.text((54, 25), "SENA", fill=(255, 255, 255), font=font_subtitle)

    # Texto cabecera
    draw.text((135, 20), "CENTRO DE TELEINFORMÁTICA Y PRODUCCIÓN INDUSTRIAL (CTPI) • POPAYÁN, CAUCA", fill=(241, 245, 249), font=font_card_title)
    draw.text((135, 46), "TECNÓLOGO EN ANÁLISIS Y DESARROLLO DE SOFTWARE (ADSO) • FICHA: 3186681", fill=(148, 163, 184), font=font_subtext)

    # Badge de Karen en cabecera derecha
    draw.rectangle([1480, 20, 1875, 60], fill=(30, 41, 59), outline=(51, 65, 85))
    draw.text((1495, 28), "APRENDIZ: KAREN YULIANA CAMPO", fill=(56, 189, 248), font=font_badge)

    # Barra inferior informativa (y: 1000 a 1080)
    draw.rectangle([0, 1000, 1920, 1080], fill=(15, 23, 42))
    draw.rectangle([0, 1000, 1920, 1003], fill=(0, 140, 69))
    draw.text((45, 1018), "EVIDENCIA: GA9-240201526-AA1-EV01 • PRESENTACIÓN DEL PROYECTO DE VIDA", fill=(250, 204, 21), font=font_badge)
    draw.text((45, 1045), "COMPETENCIA: 240201526 — ÉTICA Y CULTURA DE PAZ (ENRIQUE LOW MURTRA)", fill=(148, 163, 184), font=font_small)
    draw.text((1450, 1028), "SENA REGIONAL CAUCA • 2026", fill=(226, 232, 240), font=font_badge)

    # Contenedor Marco del Video de Karen (Izquierda)
    # Video original es 480x854. Se posicionará en x: 60, y: 113
    frame_box = [48, 98, 552, 982]
    draw.rounded_rectangle(frame_box, radius=12, fill=(17, 24, 39), outline=(0, 140, 69), width=3)

    # Cabecera de la cámara en vivo
    draw.rounded_rectangle([48, 98, 552, 138], radius=8, fill=(0, 140, 69))
    draw.text((65, 108), "● CÁMARA EN VIVO: KAREN YULIANA CAMPO", fill=(255, 255, 255), font=font_badge)

    # Panel lateral derecho (x: 580 a 1872, y: 98 a 982 -> ancho 1292, alto 884)
    panel_box = [580, 98, 1872, 982]
    draw.rounded_rectangle(panel_box, radius=12, fill=(15, 23, 42, 240), outline=(51, 65, 85), width=2)

    return img

def add_header_to_panel(draw, seg):
    # Badge
    draw.rounded_rectangle([610, 120, 1050, 158], radius=6, fill=seg["badge_color"])
    draw.text((625, 128), seg["badge"], fill=(255, 255, 255), font=font_badge)

    # Título y subtítulo
    draw.text((610, 172), seg["title"], fill=(255, 255, 255), font=font_title)
    draw.text((610, 212), seg["subtitle"], fill=(148, 163, 184), font=font_text)
    draw.line([(610, 242), (1842, 242)], fill=(51, 65, 85), width=2)

def generate_slide_01():
    img = create_base_canvas()
    draw = ImageDraw.Draw(img)
    seg = SEGMENTS[0]
    add_header_to_panel(draw, seg)

    # Insertar Foto 1 (Retrato de Karen) a la derecha
    if os.path.exists(FOTO_KAREN):
        foto = Image.open(FOTO_KAREN).convert("RGB")
        foto = foto.resize((440, 440), Image.LANCZOS)
        # Marco foto
        draw.rounded_rectangle([1360, 270, 1820, 730], radius=12, fill=(30, 41, 59), outline=(0, 140, 69), width=3)
        img.paste(foto, (1370, 280))
        draw.text((1370, 745), "Karen Yuliana Campo • Popayán", fill=(226, 232, 240), font=font_card_title)
        draw.text((1370, 775), "Aprendiz Tecnóloga en ADSO", fill=(56, 189, 248), font=font_text)

    # Tarjetas informativas en panel central
    y_pos = 270
    cards = [
        ("🌸 PROPÓSITO HUMANO Y ÉTICA", "Construcción consciente desde el amor del hogar, los valores familiares y la vocación tecnológica para la paz.", (0, 140, 69)),
        ("💻 ESPECIALIZACIÓN VOCACIONAL", "Pasión por el Diseño de Interfaces de Usuario (UI/UX) y la Inteligencia Artificial (IA) con sentido social.", (56, 189, 248)),
        ("🤝 PILAR FUNDAMENTAL: FAMILIA", "El ejemplo de superación e insistencia de mi madre y el respaldo incondicional de mi compañero de vida.", (250, 204, 21)),
        ("🕊️ CONSTRUCCIÓN DE PAZ", "La tecnología como herramienta humanista para cerrar brechas de equidad y transformar a Colombia.", (168, 85, 247))
    ]
    for tit, desc, col in cards:
        draw.rounded_rectangle([610, y_pos, 1330, y_pos + 105], radius=8, fill=(30, 41, 59), outline=(51, 65, 85))
        draw.rounded_rectangle([610, y_pos, 616, y_pos + 105], radius=2, fill=col)
        draw.text((630, y_pos + 15), tit, fill=col, font=font_card_title)
        draw.text((630, y_pos + 48), desc, fill=(226, 232, 240), font=font_text)
        y_pos += 120

    return img

def generate_slide_02():
    img = create_base_canvas()
    draw = ImageDraw.Draw(img)
    seg = SEGMENTS[1]
    add_header_to_panel(draw, seg)

    # Tarjeta de reflexión Malala
    draw.rounded_rectangle([610, 270, 1842, 430], radius=10, fill=(30, 41, 59), outline=(147, 51, 234), width=2)
    draw.text((635, 290), '📖 REFLEXIÓN ÉTICA DESDE "YO SOY MALALA" (MALALA YOUSAFZAI)', fill=(192, 132, 252), font=font_card_title)
    draw.text((635, 325), '"Si me dieran la palabra frente al mundo... ¿qué le diría para hacerlo un lugar mejor?"', fill=(250, 204, 21), font=font_subtitle)
    draw.text((635, 368), 'Yo le diría al mundo que la educación, el afecto y la tecnología no deben ser privilegios, sino puentes para sanar brechas sociales.', fill=(241, 245, 249), font=font_text)
    draw.text((635, 395), 'La paz se construye garantizando que cada mujer y niña tenga la libertad y el derecho de estudiar y escribir su propia historia.', fill=(226, 232, 240), font=font_text)

    # 3 Pilares de transformación
    y_pos = 460
    pillars = [
        ("📚 DERECHO UNIVERSAL A LA EDUCACIÓN", "Erradicar cualquier forma de violencia y exclusión que impida el acceso al conocimiento y a la formación técnica."),
        ("👩‍💻 INCLUSIÓN FEMENINA EN STEM", "Fomentar la participación activa de las mujeres en el desarrollo de software y la innovación tecnológica."),
        ("🕊️ CULTURA DE PAZ Y NO VIOLENCIA", "Reconocer la dignidad intrínseca de cada ser humano, aplicando la empatía y el diálogo como principios éticos.")
    ]
    for tit, desc in pillars:
        draw.rounded_rectangle([610, y_pos, 1842, y_pos + 115], radius=8, fill=(24, 33, 47), outline=(51, 65, 85))
        draw.text((635, y_pos + 20), tit, fill=(56, 189, 248), font=font_card_title)
        draw.text((635, y_pos + 55), desc, fill=(226, 232, 240), font=font_text)
        y_pos += 135

    return img

def generate_slide_03():
    img = create_base_canvas()
    draw = ImageDraw.Draw(img)
    seg = SEGMENTS[2]
    add_header_to_panel(draw, seg)

    draw.rounded_rectangle([610, 270, 1842, 400], radius=10, fill=(30, 41, 59), outline=(2, 132, 199), width=2)
    draw.text((635, 290), '✨ ANTE LO TRASCENDENTE: DIOS, EL UNIVERSO Y LA VIDA', fill=(56, 189, 248), font=font_card_title)
    draw.text((635, 325), 'Me reconozco como una persona inmensamente bendecida, con un propósito claro de servicio y amor al prójimo.', fill=(250, 204, 21), font=font_subtitle)
    draw.text((635, 365), 'La fe se vive en las acciones diarias: actuar con honestidad, cuidar a quienes nos rodean y no pasar indiferentes ante el dolor ajeno.', fill=(226, 232, 240), font=font_text)

    y_pos = 430
    items = [
        ("🙏 GRATITUD DIARIA", "Agradecer por cada amanecer, por las oportunidades de formación en el SENA y por el amor que sostiene mi hogar."),
        ("🤝 VOCACIÓN DE SERVICIO", "Entender que la tecnología y el conocimiento profesional cobran sentido cuando mejoran la calidad de vida de los demás."),
        ("🌟 LLAMADO A LA ESPERANZA", "Ser un instrumento de bien, promoviendo reconciliación, empatía y oportunidades en mi región caucana.")
    ]
    for tit, desc in items:
        draw.rounded_rectangle([610, y_pos, 1842, y_pos + 125], radius=8, fill=(24, 33, 47), outline=(51, 65, 85))
        draw.text((635, y_pos + 22), tit, fill=(52, 211, 153), font=font_card_title)
        draw.text((635, y_pos + 60), desc, fill=(226, 232, 240), font=font_text)
        y_pos += 145

    return img

def generate_slide_04():
    img = create_base_canvas()
    draw = ImageDraw.Draw(img)
    seg = SEGMENTS[3]
    add_header_to_panel(draw, seg)

    # 4 Roles
    draw.rounded_rectangle([610, 270, 1842, 420], radius=10, fill=(30, 41, 59), outline=(16, 185, 129), width=2)
    draw.text((635, 288), "👥 MIS ROLES FUNDAMENTALES EN ESTE AQUÍ Y AHORA", fill=(52, 211, 153), font=font_card_title)
    roles = [
        ("Hija Orgullosa", "Amor, lealtad y gratitud hacia mi madre"),
        ("Compañera de Vida", "Apoyo mutuo, complicidad y respeto diario"),
        ("Hermana Afectuosa", "Acompañamiento y unión fraternal"),
        ("Aprendiz ADSO", "Dedicación y excelencia técnica en el SENA"),
        ("Líder Social", "Compromiso con la cultura de paz en Popayán")
    ]
    rx = 635
    for r_tit, r_sub in roles:
        draw.rounded_rectangle([rx, 325, rx + 225, 400], radius=6, fill=(15, 23, 42), outline=(51, 65, 85))
        draw.text((rx + 10, 335), r_tit, fill=(56, 189, 248), font=font_badge)
        draw.text((rx + 10, 360), r_sub, fill=(203, 213, 225), font=font_small)
        rx += 240

    # Misión y Visión con insignias
    draw.rounded_rectangle([610, 450, 1210, 890], radius=10, fill=(24, 33, 47), outline=(51, 65, 85))
    draw.text((635, 475), "🎯 MISIÓN PERSONAL", fill=(250, 204, 21), font=font_subtitle)
    draw.text((635, 520), "Diseñar interfaces digitales (UI/UX) intuitivas,", fill=(241, 245, 249), font=font_text)
    draw.text((635, 550), "accesibles y humanas, integrando modelos de", fill=(241, 245, 249), font=font_text)
    draw.text((635, 580), "Inteligencia Artificial para resolver necesidades", fill=(241, 245, 249), font=font_text)
    draw.text((635, 610), "reales en el tejido productivo y social de mi región.", fill=(241, 245, 249), font=font_text)

    draw.rounded_rectangle([635, 660, 1180, 850], radius=6, fill=(15, 23, 42))
    draw.text((650, 680), "● Enfoque UI/UX: Empatía con el usuario final.", fill=(56, 189, 248), font=font_subtext)
    draw.text((650, 720), "● Enfoque IA: Automatización ética e inteligente.", fill=(168, 85, 247), font=font_subtext)
    draw.text((650, 760), "● Código Limpio: Arquitectura robusta y escalable.", fill=(52, 211, 153), font=font_subtext)
    draw.text((650, 800), "● Accesibilidad: Software inclusivo para todos.", fill=(250, 204, 21), font=font_subtext)

    draw.rounded_rectangle([1240, 450, 1842, 890], radius=10, fill=(24, 33, 47), outline=(51, 65, 85))
    draw.text((1265, 475), "🚀 VISIÓN A 5 AÑOS", fill=(56, 189, 248), font=font_subtitle)
    draw.text((1265, 520), "Consolidarme como desarrolladora líder en diseño", fill=(241, 245, 249), font=font_text)
    draw.text((1265, 550), "UI/UX e Inteligencia Artificial con enfoque social,", fill=(241, 245, 249), font=font_text)
    draw.text((1265, 580), "liderando proyectos de innovación desde Popayán", fill=(241, 245, 249), font=font_text)
    draw.text((1265, 610), "e inspirando a más mujeres a incursionar en STEM.", fill=(241, 245, 249), font=font_text)

    draw.rounded_rectangle([1265, 660, 1815, 850], radius=6, fill=(15, 23, 42))
    draw.text((1280, 680), "● Titulación Tecnológica en ADSO - SENA CTPI.", fill=(52, 211, 153), font=font_subtext)
    draw.text((1280, 720), "● Certificaciones profesionales en Cloud e IA.", fill=(250, 204, 21), font=font_subtext)
    draw.text((1280, 760), "● Creación de soluciones para emprendimientos locales.", fill=(56, 189, 248), font=font_subtext)
    draw.text((1280, 800), "● Referente femenino en tecnología en el Cauca.", fill=(244, 114, 182), font=font_subtext)

    return img

def generate_slide_05():
    img = create_base_canvas()
    draw = ImageDraw.Draw(img)
    seg = SEGMENTS[4]
    add_header_to_panel(draw, seg)

    # Dos columnas con las fotos reales de Familia y Pareja
    # Tarjeta Izquierda: Mamá y Hermano
    card_w = 590
    draw.rounded_rectangle([610, 260, 1205, 930], radius=10, fill=(30, 41, 59), outline=(234, 88, 12), width=2)
    if os.path.exists(FOTO_FAMILIA):
        f_fam = Image.open(FOTO_FAMILIA).convert("RGB")
        f_fam = f_fam.resize((560, 430), Image.LANCZOS)
        img.paste(f_fam, (625, 275))

    draw.text((625, 720), "MI MADRE Y MI HERMANO • PILAR DE SUPERACIÓN", fill=(250, 204, 21), font=font_card_title)
    draw.text((625, 755), '"A pesar de no contar con un título profesional, mi mamá', fill=(241, 245, 249), font=font_subtext)
    draw.text((625, 780), 'se ha destacado por inculcarme y ser insistente en que', fill=(241, 245, 249), font=font_subtext)
    draw.text((625, 805), 'estudie, me prepare y no me rinda ante las dificultades."', fill=(241, 245, 249), font=font_subtext)
    draw.text((625, 845), 'Valores: Perseverancia, disciplina, dignidad y amor.', fill=(52, 211, 153), font=font_badge)

    # Tarjeta Derecha: Pareja y Mascotas
    draw.rounded_rectangle([1245, 260, 1840, 930], radius=10, fill=(30, 41, 59), outline=(56, 189, 248), width=2)
    if os.path.exists(FOTO_PAREJA):
        f_par = Image.open(FOTO_PAREJA).convert("RGB")
        f_par = f_par.resize((560, 430), Image.LANCZOS)
        img.paste(f_par, (1260, 275))

    draw.text((1260, 720), "MI PAREJA Y COMPAÑERO DE VIDA • APOYO TOTAL", fill=(56, 189, 248), font=font_card_title)
    draw.text((1260, 755), '"Mi compañero de vida está conmigo siempre para apoyarme', fill=(241, 245, 249), font=font_subtext)
    draw.text((1260, 780), 'en mis metas, celebrando cada logro y brindándome la fuerza', fill=(241, 245, 249), font=font_subtext)
    draw.text((1260, 805), 'y complicidad necesaria para seguir adelante."', fill=(241, 245, 249), font=font_subtext)
    draw.text((1260, 845), 'Valores: Lealtad, respeto, empatía y trabajo en equipo.', fill=(250, 204, 21), font=font_badge)

    return img

def generate_slide_06():
    img = create_base_canvas()
    draw = ImageDraw.Draw(img)
    seg = SEGMENTS[5]
    add_header_to_panel(draw, seg)

    # Matriz DOFA interactiva
    # Fortalezas
    draw.rounded_rectangle([610, 270, 1205, 570], radius=10, fill=(20, 83, 45, 230), outline=(34, 197, 94), width=2)
    draw.text((635, 290), "💪 FORTALEZAS (F)", fill=(74, 222, 128), font=font_subtitle)
    draw.text((635, 335), "● Pasión por el diseño de interfaces limpias (UI/UX).", fill=(241, 245, 249), font=font_text)
    draw.text((635, 375), "● Curiosidad y pensamiento lógico para la IA.", fill=(241, 245, 249), font=font_text)
    draw.text((635, 415), "● Empatía profunda para el trabajo en equipo.", fill=(241, 245, 249), font=font_text)
    draw.text((635, 455), "● Respaldo incondicional de mi madre y mi pareja.", fill=(241, 245, 249), font=font_text)
    draw.text((635, 495), "● Disciplina de estudio constante y perseverancia.", fill=(241, 245, 249), font=font_text)

    # Debilidades
    draw.rounded_rectangle([1245, 270, 1840, 570], radius=10, fill=(127, 29, 29, 230), outline=(239, 68, 68), width=2)
    draw.text((1270, 290), "⚠️ DEBILIDADES A MITIGAR (D)", fill=(248, 113, 113), font=font_subtitle)
    draw.text((1270, 335), "● Tendencia a la autoexigencia excesiva ante plazos.", fill=(241, 245, 249), font=font_text)
    draw.text((1270, 375), "● Dificultad inicial para desconectarse del código.", fill=(241, 245, 249), font=font_text)
    draw.text((1270, 425), "Estrategia de Superación:", fill=(250, 204, 21), font=font_card_title)
    draw.text((1270, 465), "Aplicación de método Pomodoro, pausas activas,", fill=(241, 245, 249), font=font_text)
    draw.text((1270, 500), "tiempo en familia y descanso consciente.", fill=(241, 245, 249), font=font_text)

    # Oportunidades
    draw.rounded_rectangle([610, 600, 1205, 900], radius=10, fill=(30, 58, 138, 230), outline=(59, 130, 246), width=2)
    draw.text((635, 620), "🌟 OPORTUNIDADES (O)", fill=(96, 165, 250), font=font_subtitle)
    draw.text((635, 665), "● Formación de alta calidad en el SENA CTPI.", fill=(241, 245, 249), font=font_text)
    draw.text((635, 705), "● Creciente demanda global de diseñadores UI/UX.", fill=(241, 245, 249), font=font_text)
    draw.text((635, 745), "● Auge de la Inteligencia Artificial generativa y ética.", fill=(241, 245, 249), font=font_text)
    draw.text((635, 785), "● Proyectos de impacto social para el Cauca.", fill=(241, 245, 249), font=font_text)

    # Amenazas
    draw.rounded_rectangle([1245, 600, 1840, 900], radius=10, fill=(120, 53, 15, 230), outline=(245, 158, 11), width=2)
    draw.text((1270, 620), "🛡️ AMENAZAS Y ENTORNO (A)", fill=(251, 191, 36), font=font_subtitle)
    draw.text((1270, 665), "● Alta competitividad y cambios tecnológicos acelerados.", fill=(241, 245, 249), font=font_text)
    draw.text((1270, 705), "● Brechas de conectividad e infraestructura local.", fill=(241, 245, 249), font=font_text)
    draw.text((1270, 755), "Estrategia de Blindaje:", fill=(52, 211, 153), font=font_card_title)
    draw.text((1270, 795), "Autoaprendizaje autónomo y certificación continua.", fill=(241, 245, 249), font=font_text)

    return img

def generate_slide_07():
    img = create_base_canvas()
    draw = ImageDraw.Draw(img)
    seg = SEGMENTS[6]
    add_header_to_panel(draw, seg)

    # Foto 3 destacada a la derecha
    if os.path.exists(FOTO_PAREJA):
        foto = Image.open(FOTO_PAREJA).convert("RGB")
        foto = foto.resize((560, 610), Image.LANCZOS)
        draw.rounded_rectangle([1255, 260, 1835, 890], radius=10, fill=(30, 41, 59), outline=(217, 70, 239), width=3)
        img.paste(foto, (1265, 270))

    # Tarjetas de hábitos y entorno a la izquierda
    y_pos = 260
    habits = [
        ("📚 1. ESTUDIO DIARIO RIGUROSO", "Dedicación constante a la programación, diseño de interfaces y buenas prácticas de código limpio (Clean Code).", (56, 189, 248)),
        ("❤️ 2. TIEMPO INVALUABLE EN FAMILIA", "Compartir con mi mamá, mi hermano y mi pareja; celebrar la vida y mantener una comunicación asertiva sin violencia.", (250, 204, 21)),
        ("🐾 3. AMOR Y CUIDADO DE MIS MASCOTAS", "Nuestras 3 mascotas llenan el hogar de alegría, paz y ternura, recordándonos el valor de la lealtad y el cuidado mutuo.", (244, 114, 182)),
        ("🌱 4. COMPROMISO CON EL MEDIO AMBIENTE", "Separación adecuada de residuos en el hogar, ahorro de energía en equipos de cómputo y consumo responsable en Popayán.", (52, 211, 153))
    ]
    for tit, desc, col in habits:
        draw.rounded_rectangle([610, y_pos, 1225, y_pos + 130], radius=8, fill=(30, 41, 59), outline=(51, 65, 85))
        draw.rounded_rectangle([610, y_pos, 616, y_pos + 130], radius=2, fill=col)
        draw.text((635, y_pos + 18), tit, fill=col, font=font_card_title)
        draw.text((635, y_pos + 55), desc, fill=(226, 232, 240), font=font_text)
        y_pos += 150

    return img

def generate_slide_08():
    img = create_base_canvas()
    draw = ImageDraw.Draw(img)
    seg = SEGMENTS[7]
    add_header_to_panel(draw, seg)

    # Diagrama IKIGAI en el centro del panel
    draw.rounded_rectangle([610, 260, 1842, 680], radius=12, fill=(30, 41, 59), outline=(0, 140, 69), width=3)
    draw.text((635, 280), "🌸 DIAGRAMA IKIGAI: RAZÓN DE SER DE KAREN YULIANA CAMPO", fill=(250, 204, 21), font=font_subtitle)

    # 4 Cuadrantes convergentes
    draw.rounded_rectangle([635, 325, 915, 510], radius=8, fill=(15, 23, 42), outline=(244, 114, 182))
    draw.text((650, 340), "1. LO QUE AMO", fill=(244, 114, 182), font=font_badge)
    draw.text((650, 375), "● Crear interfaces UI/UX.", fill=(241, 245, 249), font=font_subtext)
    draw.text((650, 405), "● Inteligencia Artificial.", fill=(241, 245, 249), font=font_subtext)
    draw.text((650, 435), "● Tiempo en familia.", fill=(241, 245, 249), font=font_subtext)
    draw.text((650, 465), "● Aprender cada día.", fill=(241, 245, 249), font=font_subtext)

    draw.rounded_rectangle([935, 325, 1215, 510], radius=8, fill=(15, 23, 42), outline=(56, 189, 248))
    draw.text((950, 340), "2. EN LO QUE SOY BUENA", fill=(56, 189, 248), font=font_badge)
    draw.text((950, 375), "● Pensamiento lógico.", fill=(241, 245, 249), font=font_subtext)
    draw.text((950, 405), "● Empatía de usuario.", fill=(241, 245, 249), font=font_subtext)
    draw.text((950, 435), "● Trabajo en equipo.", fill=(241, 245, 249), font=font_subtext)
    draw.text((950, 465), "● Resiliencia ante errores.", fill=(241, 245, 249), font=font_subtext)

    draw.rounded_rectangle([1235, 325, 1515, 510], radius=8, fill=(15, 23, 42), outline=(52, 211, 153))
    draw.text((1250, 340), "3. LO QUE EL MUNDO NECESITA", fill=(52, 211, 153), font=font_badge)
    draw.text((1250, 375), "● Software accesible.", fill=(241, 245, 249), font=font_subtext)
    draw.text((1250, 405), "● Inclusión de mujeres STEM.", fill=(241, 245, 249), font=font_subtext)
    draw.text((1250, 435), "● Ética en el uso de la IA.", fill=(241, 245, 249), font=font_subtext)
    draw.text((1250, 465), "● Construcción de paz.", fill=(241, 245, 249), font=font_subtext)

    draw.rounded_rectangle([1535, 325, 1815, 510], radius=8, fill=(15, 23, 42), outline=(250, 204, 21))
    draw.text((1550, 340), "4. POR LO QUE ME PAGARÁN", fill=(250, 204, 21), font=font_badge)
    draw.text((1550, 375), "● Desarrollo de software.", fill=(241, 245, 249), font=font_subtext)
    draw.text((1550, 405), "● Diseño de productos UI/UX.", fill=(241, 245, 249), font=font_subtext)
    draw.text((1550, 435), "● Integración de modelos IA.", fill=(241, 245, 249), font=font_subtext)
    draw.text((1550, 465), "● Arquitectura frontend.", fill=(241, 245, 249), font=font_subtext)

    # Centro Ikigai
    draw.rounded_rectangle([635, 535, 1815, 650], radius=8, fill=(2, 132, 199, 230), outline=(255, 255, 255), width=2)
    draw.text((655, 550), "⭐ MI IKIGAI (PROPÓSITO CENTRAL DE VIDA):", fill=(250, 204, 21), font=font_card_title)
    draw.text((655, 585), '"Crear interfaces e Inteligencia Artificial con corazón humano para transformar vidas, honrar el esfuerzo', fill=(255, 255, 255), font=font_text)
    draw.text((655, 615), 'de mi madre, el apoyo de mi compañero y sembrar semillas de paz duradera en Colombia."', fill=(255, 255, 255), font=font_text)

    # Tarjeta de cierre institucional
    draw.rounded_rectangle([610, 710, 1842, 920], radius=10, fill=(15, 23, 42), outline=(51, 65, 85))
    draw.text((635, 735), "SISTEMA INTEGRADO DE FORMACIÓN PROFESIONAL • SENA CTPI POPAYÁN", fill=(0, 140, 69), font=font_card_title)
    draw.text((635, 775), "Evidencia GA9-240201526-AA1-EV01: Presentación del proyecto de vida", fill=(241, 245, 249), font=font_subtitle)
    draw.text((635, 815), "Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | Tecnólogo en Análisis y Desarrollo de Software", fill=(56, 189, 248), font=font_text)
    draw.text((635, 855), "¡Muchas gracias por su atención! — Popayán, Cauca 2026", fill=(250, 204, 21), font=font_card_title)

    return img

def render_slides():
    print("Generando las 8 diapositivas dinámicas en Full HD...")
    generators = [
        (generate_slide_01, "slide_01_apertura.png"),
        (generate_slide_02, "slide_02_malala.png"),
        (generate_slide_03, "slide_03_trascendencia.png"),
        (generate_slide_04, "slide_04_mision_vision.png"),
        (generate_slide_05, "slide_05_familia_valores.png"),
        (generate_slide_06, "slide_06_capacidades_dofa.png"),
        (generate_slide_07, "slide_07_habitos_hogar.png"),
        (generate_slide_08, "slide_08_ikigai_cierre.png"),
    ]
    for gen_fn, fname in generators:
        img = gen_fn()
        out_p = os.path.join(SLIDES_DIR, fname)
        img.save(out_p, "PNG")
        print(f" [OK] Generada: {fname}")

def generate_ambient_music(output_wav_path, duration_seconds=32.0):
    """Genera música de fondo suave (acústica/piano con reverberación) en WAV 48kHz estéreo."""
    sample_rate = 48000
    total_samples = int(sample_rate * duration_seconds)
    chords = [
        [261.63, 329.63, 392.00, 493.88], # Cmaj7
        [220.00, 261.63, 329.63, 392.00], # Am7
        [174.61, 220.00, 261.63, 329.63], # Fmaj7
        [196.00, 246.94, 293.66, 349.23], # G7
        [164.81, 196.00, 246.94, 293.66], # Em7
        [220.00, 261.63, 329.63, 392.00], # Am7
        [174.61, 220.00, 261.63, 329.63], # Fmaj7
        [196.00, 261.63, 293.66, 392.00], # Gsus4 -> C
    ]
    chord_len = total_samples // len(chords)
    data = []

    for idx, chord in enumerate(chords):
        for s in range(chord_len):
            t = (idx * chord_len + s) / sample_rate
            env = math.sin(math.pi * (s / chord_len)) ** 0.6
            sample_val = 0.0
            for note in chord:
                w1 = math.sin(2.0 * math.pi * note * t)
                w2 = 0.3 * math.sin(2.0 * math.pi * (note * 2.0) * t)
                w3 = 0.1 * math.sin(2.0 * math.pi * (note * 3.0) * t)
                sample_val += (w1 + w2 + w3)
            sample_val = (sample_val / len(chord)) * env * 0.18
            val_int = int(max(min(sample_val, 1.0), -1.0) * 32767)
            data.append(struct.pack('<hh', val_int, val_int))

    with wave.open(output_wav_path, 'wb') as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(data))
    print(f"[OK] BGM Loop generado: {output_wav_path}")

def main():
    print("=== INICIANDO PRODUCCIÓN DE VIDEO EXPOSITIVO: PROYECTO DE VIDA ===")
    print("Evidencia: GA9-240201526-AA1-EV01 | Aprendiz: Karen Yuliana Campo")

    # 1. Renderizar diapositivas
    render_slides()

    # 2. Generar BGM loop
    bg_music_wav = os.path.join(BUILD_DIR, 'bg_piano_ambient_32s.wav')
    generate_ambient_music(bg_music_wav, duration_seconds=32.0)

    # 3. Crear archivo de lista concat para las diapositivas
    # Concat demuxer de ffmpeg: file 'path' \n duration X
    concat_txt_path = os.path.join(BUILD_DIR, 'slides_concat.txt')
    with open(concat_txt_path, 'w', encoding='utf-8') as f:
        for seg in SEGMENTS:
            f.write(f"file '/build/slides/{seg['name']}'\n")
            f.write(f"duration {seg['duration']:.2f}\n")
        # Último archivo repetido para que concat respete el último duration
        f.write(f"file '/build/slides/{SEGMENTS[-1]['name']}'\n")

    print(f"[OK] Lista de sincronización de diapositivas creada en: {concat_txt_path}")

    # 4. Renderizado Final con Docker FFmpeg
    output_video_path = os.path.join(VIDEO_DIR, 'GA9-240201526-AA1-EV01_Video_Presentacion_Proyecto_Vida.mp4')

    print("Ejecutando composición y renderizado final con Docker FFmpeg...")
    docker_cmd = [
        "docker", "run", "--rm",
        "-v", f"{BUILD_DIR}:/build",
        "-v", f"{RAW_VIDEO}:/data/raw_karen.mp4:ro",
        "-v", f"{VIDEO_DIR}:/video_out",
        "jrottenberg/ffmpeg:6.1-alpine",
        "-y",
        "-f", "concat", "-safe", "0", "-i", "/build/slides_concat.txt",
        "-i", "/data/raw_karen.mp4",
        "-stream_loop", "-1", "-i", "/build/bg_piano_ambient_32s.wav",
        "-t", "326.57",
        "-filter_complex",
        "[0:v]fps=25[slides_v];"
        "[1:v]scale=480:854,fps=25[karen_v];"
        "[slides_v][karen_v]overlay=x=60:y=113[out_v];"
        "[1:a]highpass=f=80,equalizer=f=3000:t=q:w=1:g=2.5,loudnorm=I=-16:TP=-1.5:LRA=11,asplit=2[voice_main][voice_sc];"
        "[2:a]volume=0.07[bgm_base];"
        "[bgm_base][voice_sc]sidechaincompress=threshold=0.04:ratio=14:attack=15:release=450[ducked_bgm];"
        "[voice_main][ducked_bgm]amix=inputs=2:duration=first:dropout_transition=2[out_a]",
        "-map", "[out_v]",
        "-map", "[out_a]",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "22",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "/video_out/GA9-240201526-AA1-EV01_Video_Presentacion_Proyecto_Vida.mp4"
    ]

    print("Comando de renderizado lanzado. Procesando 5 minutos y 26 segundos de video Full HD...")
    subprocess.run(docker_cmd, check=True)

    sz_mb = os.path.getsize(output_video_path) / (1024 * 1024)
    print(f"[OK] Video final renderizado con éxito: {output_video_path} ({sz_mb:.2f} MB)")

    # 5. Distribución
    p_zajuna = os.path.join(ENTREGA_DIR, 'GA9-240201526-AA1-EV01_Video_Presentacion_Proyecto_Vida.mp4')
    p_brain = os.path.join(ARTIFACT_DIR, 'GA9-240201526-AA1-EV01_Video_Presentacion_Proyecto_Vida.mp4')

    shutil.copy(output_video_path, p_zajuna)
    shutil.copy(output_video_path, p_brain)
    print(f"[OK] Copiado a entrega Zajuna: {p_zajuna}")
    print(f"[OK] Copiado a artefactos: {p_brain}")

    # Reempaquetar ZIP
    compile_entrega_script = os.path.join(SCRIPT_DIR, 'compile_entrega.py')
    if os.path.exists(compile_entrega_script):
        subprocess.run(["python3", compile_entrega_script], check=True)

    print("=== PRODUCCIÓN Y DISTRIBUCIÓN DEL VIDEO FINALIZADA CON ÉXITO ===")

if __name__ == '__main__':
    main()
