#!/usr/bin/env python3
"""
Generador del Video Elevator Pitch Tipo TikTok (9:16 Vertical HD 1080x1920)
Evidencia: GA10-240201529-AA2-EV01 - Pitch idea de negocio
Aprendiz: Karen Yuliana Campo - SENA ADSO Ficha 3186681
Duración: 54 segundos (Límite máximo de guía: 59 segundos)
"""

import os
import sys
import math
import wave
import struct
import subprocess
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
FPS = 30
TOTAL_DURATION = 54.0
TOTAL_FRAMES = int(FPS * TOTAL_DURATION) # 1620 frames
SAMPLE_RATE = 44100
TOTAL_AUDIO_SAMPLES = int(SAMPLE_RATE * TOTAL_DURATION)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
VIDEO_DIR = os.path.join(BASE_DIR, "video")
TMP_DIR = "/tmp/pitch_build"
os.makedirs(VIDEO_DIR, exist_ok=True)
os.makedirs(TMP_DIR, exist_ok=True)

FINAL_MP4 = os.path.join(VIDEO_DIR, "GA10-240201529-AA2-EV01_Pitch_Idea_Negocio.mp4")
MASTER_AUDIO_WAV = os.path.join(TMP_DIR, "master_audio.wav")

FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

# Load Fonts
f_brand_tag = ImageFont.truetype(FONT_BOLD, 26)
f_badge = ImageFont.truetype(FONT_BOLD, 26)
f_hud = ImageFont.truetype(FONT_BOLD, 24)
f_scene_badge = ImageFont.truetype(FONT_BOLD, 30)
f_headline = ImageFont.truetype(FONT_BOLD, 52)
f_card_title = ImageFont.truetype(FONT_BOLD, 34)
f_card_desc = ImageFont.truetype(FONT_REG, 26)
f_pill = ImageFont.truetype(FONT_BOLD, 24)
f_action_count = ImageFont.truetype(FONT_BOLD, 22)
f_tiktok_user = ImageFont.truetype(FONT_BOLD, 32)
f_tiktok_caption = ImageFont.truetype(FONT_REG, 24)
f_subtitle_box = ImageFont.truetype(FONT_BOLD, 32)

# Source assets
LOGO_PATH = "/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-028_GA8-220501096-AA2-EV02_Modulos_Moviles_APK/codigo_fuente/app_react_native/android/app/src/main/res/drawable-xxxhdpi/splashscreen_logo.png"
CATALOG_PATH = "/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-018_GA7-220501096-AA3-EV02_Modulos_Probados_Historias_Usuario/capturas_pruebas/02_hu02_pizzas_catalogo_filtros.png"
CANVAS_IMG_PATH = "/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-053_GA10-240201529-AA2-EV02_Modelo_Canvas_Emprendimiento/diagramas/matriz_modelo_canvas_pizzeria_bella_italia.png"

resample_filter = getattr(getattr(Image, 'Resampling', Image), 'LANCZOS', Image.ANTIALIAS)

logo_img = Image.open(LOGO_PATH).convert("RGBA").resize((220, 220), resample_filter) if os.path.exists(LOGO_PATH) else None
catalog_img = Image.open(CATALOG_PATH).convert("RGBA").resize((700, 360), resample_filter) if os.path.exists(CATALOG_PATH) else None
canvas_thumb = Image.open(CANVAS_IMG_PATH).convert("RGBA").resize((680, 440), resample_filter) if os.path.exists(CANVAS_IMG_PATH) else None

# Helper to draw rounded rectangle
def draw_rounded_card(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

# 1. Synthesize Audio
def build_audio():
    if os.path.exists(MASTER_AUDIO_WAV) and os.path.getsize(MASTER_AUDIO_WAV) > 1000000:
        print(f"--- [PITCH] 1. Usando pista de audio existente en {MASTER_AUDIO_WAV} ---")
        return
    print("--- [PITCH] 1. Sintetizando locución en español y banda sonora... ---")
    clips_def = [
        (0.6, "sc1", "Cansado de pedir pizza en Popayán y que llegue fría, grasosa o con una masa pesada que no te deja dormir?", 155),
        (8.2, "sc2", "Llegó Bella Italia Popayán! La auténtica pizza artesanal con masa madre de 48 horas de fermentación y horneada a 450 grados en solo 90 segundos.", 155),
        (20.3, "sc3", "Unimos técnica italiana con insumos de nuestra tierra: quesos campesinos de Silvia y hortalizas orgánicas del Cauca para una textura crocante y digestión ligera.", 155),
        (32.3, "sc4", "Con nuestra aplicación web desarrollada en el SENA pides en segundos y recibes tu pizza a más de 70 grados en menos de 30 minutos gracias a baúles térmicos.", 155),
        (43.3, "sc5", "Visítanos en el Centro Histórico de Popayán o pide a nuestro WhatsApp oficial. Bella Italia Popayán: Pasión italiana con corazón caucano! Haz tu pedido ya!", 155)
    ]

    voice_data = []
    speech_mask = [0.0] * TOTAL_AUDIO_SAMPLES

    for start_time, cid, text, speed in clips_def:
        wpath = os.path.join(TMP_DIR, f"{cid}.wav")
        subprocess.run(["espeak-ng", "-v", "es", "-s", str(speed), "-p", "52", "-w", wpath, text], check=True)
        with wave.open(wpath, 'rb') as w:
            n_ch = w.getnchannels()
            n_fr = w.getnframes()
            raw = w.readframes(n_fr)
            samples = []
            fmt = f"<{n_fr * n_ch}h"
            raw_shorts = struct.unpack(fmt, raw)
            for idx in range(0, len(raw_shorts), n_ch):
                samples.append(raw_shorts[idx] / 32768.0)
        
        start_sample = int(start_time * SAMPLE_RATE)
        voice_data.append((start_sample, samples))
        for si in range(len(samples)):
            idx = start_sample + si
            if idx < TOTAL_AUDIO_SAMPLES:
                speech_mask[idx] = 1.0

    # Smooth ducking mask
    smooth_mask = [0.0] * TOTAL_AUDIO_SAMPLES
    curr = 0.0
    for i in range(TOTAL_AUDIO_SAMPLES):
        target = speech_mask[i]
        if target > curr:
            curr = min(1.0, curr + 1.0 / (0.05 * SAMPLE_RATE))
        else:
            curr = max(0.0, curr - 1.0 / (0.2 * SAMPLE_RATE))
        smooth_mask[i] = curr

    chords = [
        ([110.0, 130.81, 164.81, 220.0], 55.0), # Am
        ([87.31, 110.0, 130.81, 174.61], 43.65), # F
        ([130.81, 164.81, 196.0, 261.63], 65.41), # C
        ([98.0, 123.47, 146.83, 196.0], 49.0) # G
    ]

    master_l = [0.0] * TOTAL_AUDIO_SAMPLES
    master_r = [0.0] * TOTAL_AUDIO_SAMPLES

    bpm = 120.0
    beat_len = 60.0 / bpm
    bar_len = beat_len * 4

    for i in range(TOTAL_AUDIO_SAMPLES):
        t = i / SAMPLE_RATE
        bar_num = int(t / bar_len)
        chord_notes, bass_freq = chords[bar_num % 4]
        
        pos_in_bar = (t % bar_len) / bar_len
        beat_idx = int(pos_in_bar * 4)
        
        kick = 0.0
        if beat_idx in [0, 2]:
            dt_kick = t % beat_len
            if dt_kick < 0.15:
                kick_freq = 140.0 * math.exp(-35.0 * dt_kick) + 45.0
                kick = math.sin(2 * math.pi * kick_freq * dt_kick) * math.exp(-18.0 * dt_kick) * 0.45
                
        snare = 0.0
        if beat_idx in [1, 3]:
            dt_snare = t % beat_len
            if dt_snare < 0.2:
                noise = ((math.sin(i * 12.9898) * 43758.5453) % 1.0 - 0.5) * 2.0
                tone = math.sin(2 * math.pi * 180.0 * dt_snare) * 0.3
                snare = (noise * 0.7 + tone * 0.3) * math.exp(-22.0 * dt_snare) * 0.3
                
        hh_dt = t % (beat_len / 2.0)
        hihat = 0.0
        if hh_dt < 0.05:
            noise = ((math.sin(i * 37.1234) * 21953.1) % 1.0 - 0.5) * 2.0
            hihat = noise * math.exp(-80.0 * hh_dt) * 0.12
            
        bass_dt = t % (beat_len / 2.0)
        bass = math.sin(2 * math.pi * bass_freq * t) * math.exp(-4.0 * bass_dt) * 0.25
        bass += math.sin(2 * math.pi * (bass_freq * 2) * t) * 0.08
        
        chord_val = 0.0
        for note in chord_notes:
            chord_val += math.sin(2 * math.pi * note * t) * 0.05
        chord_val *= (0.7 + 0.3 * math.sin(2 * math.pi * 2.0 * t))
        
        arp_sub = int((t % beat_len) / (beat_len / 4.0))
        arp_note = chord_notes[arp_sub % len(chord_notes)] * 2.0
        arp_dt = t % (beat_len / 4.0)
        arp = math.sin(2 * math.pi * arp_note * t) * math.exp(-25.0 * arp_dt) * 0.08
        
        music_mix_l = (kick + snare * 0.9 + hihat * 0.7 + bass + chord_val * 0.9 + arp * 0.7) * 0.4
        music_mix_r = (kick + snare * 0.9 + hihat * 1.1 + bass + chord_val * 1.1 + arp * 1.0) * 0.4
        
        duck = 1.0 - (smooth_mask[i] * 0.75)
        fade = 1.0
        if t > (TOTAL_DURATION - 2.0):
            fade = max(0.0, (TOTAL_DURATION - t) / 2.0)
            
        master_l[i] = music_mix_l * duck * fade
        master_r[i] = music_mix_r * duck * fade

    for start_sample, samples in voice_data:
        for si, sval in enumerate(samples):
            idx = start_sample + si
            if idx < TOTAL_AUDIO_SAMPLES:
                v = sval * 1.25
                master_l[idx] += v
                master_r[idx] += v

    with wave.open(MASTER_AUDIO_WAV, 'w') as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SAMPLE_RATE)
        out_bytes = bytearray()
        for i in range(TOTAL_AUDIO_SAMPLES):
            sl = int(max(-32767, min(32767, master_l[i] * 28000)))
            sr = int(max(-32767, min(32767, master_r[i] * 28000)))
            out_bytes.extend(struct.pack('<hh', sl, sr))
        w.writeframes(out_bytes)

    print(f"Banda sonora master guardada: {MASTER_AUDIO_WAV}")

# 2. Render Single Frame
def render_frame(frame_idx):
    t = frame_idx / FPS
    
    # Background: dark slate gradient with soft warmth
    im = Image.new("RGBA", (W, H), (15, 23, 42, 255))
    draw = ImageDraw.Draw(im)

    # Ambient radial glows
    glow_color = (245, 158, 11, 20) if t < 20.0 else ((16, 185, 129, 20) if t < 32.0 else (59, 130, 246, 20))
    draw.ellipse([-200, 200, 600, 1000], fill=glow_color)
    draw.ellipse([600, 800, 1400, 1600], fill=glow_color)

    # 1. Top HUD (TikTok Bar)
    # Progress Bar at Y=0..8
    prog_w = int((frame_idx / TOTAL_FRAMES) * W)
    draw.rectangle([0, 0, W, 8], fill=(51, 65, 85, 255))
    draw.rectangle([0, 0, prog_w, 8], fill=(245, 158, 11, 255))

    # Top Badges (Y: 25..85)
    draw_rounded_card(draw, [50, 30, 480, 85], 25, (30, 41, 59, 220), (245, 158, 11, 200), 2)
    draw.text((70, 42), "SENA | ADSO - FICHA 3186681", font=f_hud, fill=(241, 245, 249))

    # Timer Badge
    time_str = f"{int(t):02d}:{int((t % 1)*10):01d} / 54s"
    draw_rounded_card(draw, [840, 30, 1030, 85], 25, (220, 38, 38, 220), (254, 202, 202, 180), 2)
    draw.ellipse([860, 50, 875, 65], fill=(255, 255, 255))
    draw.text((885, 42), time_str, font=f_hud, fill=(255, 255, 255))

    # Italian flag ribbon strip
    draw.rectangle([50, 105, 170, 113], fill=(0, 140, 69, 255))
    draw.rectangle([170, 105, 290, 113], fill=(244, 245, 240, 255))
    draw.rectangle([290, 105, 410, 113], fill=(205, 33, 42, 255))

    # Determine Active Scene
    if t < 8.0:
        # ESCENA 1: EL PROBLEMA (0s - 8s)
        draw_rounded_card(draw, [50, 140, 480, 200], 18, (239, 68, 68, 40), (239, 68, 68, 255), 2)
        draw.text((70, 152), "PASO 1: EL PROBLEMA REAL", font=f_scene_badge, fill=(248, 113, 113))

        draw.text((50, 225), "¿PIZZAS FRÍAS Y MASAS", font=f_headline, fill=(255, 255, 255))
        draw.text((50, 285), "INDIGESTAS EN POPAYÁN?", font=f_headline, fill=(239, 68, 68))

        # Problem Cards
        cards = [
            ("DEMORAS EXCESIVAS (>60 MIN)", "Pedidos de delivery que tardan más de 60 minutos\ny llegan completamente fríos al cliente.", (239, 68, 68)),
            ("MASAS INDUSTRIALES PESADAS", "Harinas refinadas y levaduras químicas rápidas\nque causan acidez, inflamación y pesadez.", (245, 158, 11)),
            ("INGREDIENTES ULTRAPROCESADOS", "Salsas artificiales y quesos análogos sin sabor\nauténtico ni trazabilidad sanitaria.", (234, 179, 8))
        ]
        y_pos = 380
        for title, desc, col in cards:
            draw_rounded_card(draw, [50, y_pos, 880, y_pos + 160], 20, (30, 41, 59, 230), col, 2)
            draw.text((80, y_pos + 25), title, font=f_card_title, fill=col)
            draw.text((80, y_pos + 75), desc, font=f_card_desc, fill=(226, 232, 240))
            y_pos += 185

        # Graphic Box: Problem Alert Banner
        draw_rounded_card(draw, [50, 950, 880, 1260], 25, (15, 23, 42, 240), (239, 68, 68, 180), 2)
        draw.text((80, 980), "EVALUACIÓN DEL MERCADO GASTRONÓMICO", font=f_pill, fill=(248, 113, 113))
        draw.text((80, 1030), "• Más del 72% de clientes en Popayán reportan insatisfacción\n  con el tiempo de entrega y temperatura.", font=f_card_desc, fill=(255, 255, 255))
        draw.text((80, 1110), "• Cero opciones de pizza artesanal con fermentación lenta\n  en los sectores residenciales y universitarios.", font=f_card_desc, fill=(255, 255, 255))
        draw.text((80, 1190), "• Urgencia de una solución gourmet rápida y saludable.", font=f_card_desc, fill=(253, 224, 71))

        subtitle_text = "¿Cansado de pedir pizza en Popayán y que llegue fría,\ngrasosa o con una masa pesada que no te deja dormir?"

    elif t < 20.0:
        # ESCENA 2: LA SOLUCIÓN - BELLA ITALIA (8s - 20s)
        draw_rounded_card(draw, [50, 140, 510, 200], 18, (16, 185, 129, 40), (16, 185, 129, 255), 2)
        draw.text((70, 152), "PASO 2: SOLUCIÓN GOURMET", font=f_scene_badge, fill=(52, 211, 153))

        draw.text((50, 225), "¡LLEGÓ PIZZERÍA GOURMET", font=f_headline, fill=(255, 255, 255))
        draw.text((50, 285), "BELLA ITALIA POPAYÁN!", font=f_headline, fill=(245, 158, 11))

        # Logo stamp
        if logo_img:
            im.paste(logo_img, (670, 140), logo_img)

        # 3 Value Propositions
        solutions = [
            ("MASA MADRE 48H FERMENTACIÓN", "Fermentación biológica lenta: alvéolos aireados,\ncorteza crocante y digestión 100% ultraligera.", (245, 158, 11)),
            ("HORNO NAPOLITANO A 450°C", "Piedra volcánica refractaria: horneado perfecto\nen solo 90 segundos a fuego vivo.", (239, 68, 68)),
            ("ESTILO NAPOLITANO CONTEMPORÁNEO", "Tradición de Nápoles adaptada a los estándares\nmás exigentes del consumidor moderno.", (16, 185, 129))
        ]
        y_pos = 380
        for title, desc, col in solutions:
            draw_rounded_card(draw, [50, y_pos, 880, y_pos + 160], 20, (30, 41, 59, 230), col, 2)
            draw.text((80, y_pos + 25), title, font=f_card_title, fill=col)
            draw.text((80, y_pos + 75), desc, font=f_card_desc, fill=(226, 232, 240))
            y_pos += 185

        # Badges Row
        draw_rounded_card(draw, [50, 950, 310, 1020], 15, (245, 158, 11, 40), (245, 158, 11), 2)
        draw.text((75, 968), "Masa Madre 48h", font=f_pill, fill=(255, 255, 255))

        draw_rounded_card(draw, [330, 950, 590, 1020], 15, (239, 68, 68, 40), (239, 68, 68), 2)
        draw.text((360, 968), "Horno a 450°C", font=f_pill, fill=(255, 255, 255))

        draw_rounded_card(draw, [610, 950, 880, 1020], 15, (16, 185, 129, 40), (16, 185, 129), 2)
        draw.text((645, 968), "90 Segundos", font=f_pill, fill=(255, 255, 255))

        # Graphic preview
        if catalog_img:
            im.paste(catalog_img, (90, 1050), catalog_img)

        subtitle_text = "¡Llegó Bella Italia Popayán! La auténtica pizza artesanal con\nmasa madre de 48h de fermentación y horneada a 450°C en 90s."

    elif t < 32.0:
        # ESCENA 3: VALOR DIFERENCIAL Y LOCAL (20s - 32s)
        draw_rounded_card(draw, [50, 140, 520, 200], 18, (245, 158, 11, 40), (245, 158, 11, 255), 2)
        draw.text((70, 152), "PASO 3: TRADICIÓN + CAUCA", font=f_scene_badge, fill=(251, 191, 36))

        draw.text((50, 225), "TRADICIÓN ITALIANA CON", font=f_headline, fill=(255, 255, 255))
        draw.text((50, 285), "EL CORAZÓN CAUCANO", font=f_headline, fill=(16, 185, 129))

        diff_cards = [
            ("QUESOS ARTESANALES DE SILVIA", "Alianza con productores lecheros de Silvia (Cauca):\nMozzarella fior di latte fresco de alta pureza.", (16, 185, 129)),
            ("HUERTAS ORGÁNICAS LOCALES", "Albahaca fresca y hortalizas cosechadas por\nfamilias campesinas de Timbío y Popayán.", (245, 158, 11)),
            ("POMODORO SAN MARZANO", "Salsa de tomate natural sin conservantes, con acidez\nbalanceada y aceite de oliva extra virgen.", (239, 68, 68))
        ]
        y_pos = 380
        for title, desc, col in diff_cards:
            draw_rounded_card(draw, [50, y_pos, 880, y_pos + 160], 20, (30, 41, 59, 230), col, 2)
            draw.text((80, y_pos + 25), title, font=f_card_title, fill=col)
            draw.text((80, y_pos + 75), desc, font=f_card_desc, fill=(226, 232, 240))
            y_pos += 185

        # Impact highlight card
        draw_rounded_card(draw, [50, 950, 880, 1260], 25, (15, 23, 42, 240), (16, 185, 129, 180), 2)
        draw.text((80, 980), "IMPACTO SOCIAL Y SOSTENIBILIDAD REGIONAL", font=f_pill, fill=(52, 211, 153))
        draw.text((80, 1030), "• Compra directa al campo caucano a precio justo (Fair Trade).", font=f_card_desc, fill=(255, 255, 255))
        draw.text((80, 1100), "• Empaques 100% biodegradables de caña de azúcar.", font=f_card_desc, fill=(255, 255, 255))
        draw.text((80, 1170), "• Sabor inigualable con identidad gastronómica caucana.", font=f_card_desc, fill=(253, 224, 71))

        subtitle_text = "Unimos técnica italiana con insumos de nuestra tierra: quesos\ncampesinos de Silvia y hortalizas orgánicas del Cauca."

    elif t < 43.0:
        # ESCENA 4: INNOVACIÓN TECNOLÓGICA SENA ADSO (32s - 43s)
        draw_rounded_card(draw, [50, 140, 520, 200], 18, (59, 130, 246, 40), (59, 130, 246, 255), 2)
        draw.text((70, 152), "PASO 4: TECNOLOGÍA ADSO", font=f_scene_badge, fill=(96, 165, 250))

        draw.text((50, 225), "PLATAFORMA WEB ADSO +", font=f_headline, fill=(255, 255, 255))
        draw.text((50, 285), "LOGÍSTICA INTELIGENTE", font=f_headline, fill=(59, 130, 246))

        tech_cards = [
            ("APP WEB REACTIVA SENA ADSO", "Ecosistema de pedidos en tiempo real con catálogo,\ncarrito y tracking interactivo en 3 simples clics.", (59, 130, 246)),
            ("BAÚLES TÉRMICOS INTELIGENTES", "Mochilas térmicas con aislamiento cerámico:\nla pizza llega a tu mesa a más de 70°C.", (245, 158, 11)),
            ("PROMESA DELIVERY < 30 MIN", "Ruta de despacho optimizada en Popayán con\ngarantía de entrega puntual o postre gratis.", (16, 185, 129))
        ]
        y_pos = 380
        for title, desc, col in tech_cards:
            draw_rounded_card(draw, [50, y_pos, 880, y_pos + 160], 20, (30, 41, 59, 230), col, 2)
            draw.text((80, y_pos + 25), title, font=f_card_title, fill=col)
            draw.text((80, y_pos + 75), desc, font=f_card_desc, fill=(226, 232, 240))
            y_pos += 185

        # Visual thumb
        if canvas_thumb:
            im.paste(canvas_thumb, (100, 950), canvas_thumb)

        subtitle_text = "Con nuestra app web desarrollada en ADSO pides en segundos y\nrecibes tu pizza a más de 70°C en menos de 30 minutos."

    else:
        # ESCENA 5: CALL TO ACTION (CTA) (43s - 54s)
        draw_rounded_card(draw, [50, 140, 500, 200], 18, (245, 158, 11, 40), (245, 158, 11, 255), 2)
        draw.text((70, 152), "PASO 5: LLAMADO A LA ACCIÓN", font=f_scene_badge, fill=(251, 191, 36))

        draw.text((50, 225), "¡VIVE LA EXPERIENCIA", font=f_headline, fill=(255, 255, 255))
        draw.text((50, 285), "BELLA ITALIA HOY!", font=f_headline, fill=(245, 158, 11))

        contact_cards = [
            ("SEDE CENTRO HISTÓRICO POPAYÁN", "Calle 4ta No. 3-45 - Ambiente colonial italiano acogedor,\nhorno a la vista y servicio impecable.", (245, 158, 11)),
            ("CANAL WHATSAPP OFICIAL", "Línea directa de pedidos: (+57) 312 890 4521\nRespuesta inmediata por bot y equipo de atención.", (16, 185, 129)),
            ("CERTIFICACIÓN HOMONIMIA RUES", "Nombre registrado: Pizzería Gourmet Bella Italia Popayán SAS\nCámara de Comercio de Popayán - CIIU 5611.", (59, 130, 246)),
            ("APRENDIZ LÍDER DE PROYECTO", "Karen Yuliana Campo - SENA Regional Cauca CTPI\nTecnólogo en Análisis y Desarrollo de Software.", (168, 85, 247))
        ]
        y_pos = 360
        for title, desc, col in contact_cards:
            draw_rounded_card(draw, [50, y_pos, 880, y_pos + 140], 18, (30, 41, 59, 230), col, 2)
            draw.text((80, y_pos + 20), title, font=f_card_title, fill=col)
            draw.text((80, y_pos + 65), desc, font=f_card_desc, fill=(226, 232, 240))
            y_pos += 155

        # Big CTA Button
        draw_rounded_card(draw, [50, 990, 880, 1100], 25, (245, 158, 11), (255, 255, 255), 3)
        draw.text((160, 1025), "¡HAZ TU PEDIDO YA Y DISFRUTA!", font=f_headline, fill=(15, 23, 42))

        # Brand claim
        draw.text((150, 1140), "«Pasión italiana con corazón caucano»", font=f_scene_badge, fill=(255, 255, 255))
        draw.text((220, 1190), "Popayán, Cauca • Ficha SENA 3186681", font=f_pill, fill=(148, 163, 184))

        subtitle_text = "Visítanos en el Centro Histórico de Popayán o pide a nuestro WhatsApp.\n¡Bella Italia: Pasión italiana con corazón caucano! ¡Pide ya!"

    # 2. TikTok Right Sidebar Actions (Y: 650..1250, X: 920..1040)
    # Profile avatar
    draw.ellipse([930, 650, 1030, 750], fill=(245, 158, 11))
    draw.text((955, 680), "KC", font=f_headline, fill=(15, 23, 42))
    draw.ellipse([965, 735, 995, 765], fill=(239, 68, 68))
    draw.text((973, 738), "+", font=f_badge, fill=(255, 255, 255))

    # Likes
    draw.ellipse([945, 790, 1015, 860], fill=(30, 41, 59, 220))
    draw.text((965, 805), "❤️", font=f_scene_badge, fill=(239, 68, 68))
    draw.text((950, 870), "24.5K", font=f_action_count, fill=(255, 255, 255))

    # Comments
    draw.ellipse([945, 915, 1015, 985], fill=(30, 41, 59, 220))
    draw.text((965, 930), "💬", font=f_scene_badge, fill=(255, 255, 255))
    draw.text((955, 995), "1,890", font=f_action_count, fill=(255, 255, 255))

    # Bookmarks
    draw.ellipse([945, 1040, 1015, 1110], fill=(30, 41, 59, 220))
    draw.text((965, 1055), "⭐", font=f_scene_badge, fill=(245, 158, 11))
    draw.text((955, 1120), "5,410", font=f_action_count, fill=(255, 255, 255))

    # Share
    draw.ellipse([945, 1165, 1015, 1235], fill=(30, 41, 59, 220))
    draw.text((965, 1180), "↗️", font=f_scene_badge, fill=(255, 255, 255))
    draw.text((962, 1245), "920", font=f_action_count, fill=(255, 255, 255))

    # Spinning Vinyl Icon
    vinyl_angle = (frame_idx * 6) % 360
    draw.ellipse([940, 1300, 1020, 1380], fill=(15, 23, 42), outline=(245, 158, 11), width=4)
    draw.ellipse([965, 1325, 995, 1355], fill=(239, 68, 68))

    # 3. Subtitles Overlay (Y: 1420..1580)
    draw_rounded_card(draw, [50, 1420, 1030, 1570], 25, (0, 0, 0, 210), (245, 158, 11, 230), 2)
    draw.text((80, 1445), subtitle_text, font=f_subtitle_box, fill=(255, 255, 255))

    # 4. TikTok Bottom Bar (User info, caption, sound) (Y: 1590..1870)
    draw.text((50, 1600), "@karen_campo_adso", font=f_tiktok_user, fill=(255, 255, 255))
    draw.ellipse([375, 1608, 400, 1633], fill=(59, 130, 246))
    draw.text((381, 1609), "✓", font=f_hud, fill=(255, 255, 255))

    caption = "Pizzería Gourmet Bella Italia Popayán | Pasión italiana con corazón caucano 🍕✨\n#SENA #ADSO #Pitch #Emprendimiento #Popayán #MasaMadre48h"
    draw.text((50, 1650), caption, font=f_tiktok_caption, fill=(226, 232, 240))

    # Sound marquee
    draw_rounded_card(draw, [50, 1730, 620, 1780], 20, (30, 41, 59, 200), (71, 85, 105), 1)
    draw.text((70, 1742), "🎵 Bella Italia Popayán - Audio Oficial Original (54s)", font=f_hud, fill=(245, 158, 11))

    # Footer platform icons
    draw.rectangle([0, 1890, W, 1920], fill=(15, 23, 42, 255))

    return im.convert("RGB")

# 3. Main Pipe Video Rendering
def main():
    build_audio()

    print("--- [PITCH] 2. Renderizando y codificando video MP4 vertical (1080x1920, 30fps, 54s)... ---")
    
    # We pipe RGB24 frames directly into docker sena-ffmpeg:alpine
    # Output to TMP_DIR then move to FINAL_MP4
    temp_mp4 = os.path.join(TMP_DIR, "output_pitch.mp4")
    
    cmd = [
        "docker", "run", "--rm", "-i",
        "-u", f"{os.getuid()}:{os.getgid()}",
        "-v", f"{TMP_DIR}:/data",
        "sena-ffmpeg:alpine",
        "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{W}x{H}",
        "-pix_fmt", "rgb24",
        "-r", str(FPS),
        "-i", "-",
        "-i", "/data/master_audio.wav",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "22",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        "/data/output_pitch.mp4"
    ]

    print("Ejecutando pipeline FFmpeg...")
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

    # Pre-render 5 unique scene frames and interpolate or render direct
    # Notice: across each scene, only timer, progress bar, vinyl rotation and subtitles change!
    # Rendering 1620 frames at 0.04s per frame takes ~60 seconds.
    print(f"Generando {TOTAL_FRAMES} frames...")
    for f in range(TOTAL_FRAMES):
        frame_im = render_frame(f)
        proc.stdin.write(frame_im.tobytes())
        if f % 150 == 0 or f == TOTAL_FRAMES - 1:
            print(f"Progreso: frame {f}/{TOTAL_FRAMES} ({f/TOTAL_FRAMES*100:.1f}%)")

    proc.stdin.flush()
    proc.stdin.close()
    stderr_out = proc.stderr.read().decode('utf-8', errors='ignore')
    proc.wait()

    if proc.returncode != 0:
        print("Error en FFmpeg:\n", stderr_out)
        sys.exit(1)

    print(f"Video MP4 generado exitosamente en {temp_mp4}!")
    
    # Move to final location
    subprocess.run(["cp", temp_mp4, FINAL_MP4], check=True)
    
    # Copy to Zajuna delivery folders
    zajuna_dir = "/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA10-240201529-AA2-EV01"
    zajuna_video_dir = os.path.join(zajuna_dir, "video")
    os.makedirs(zajuna_video_dir, exist_ok=True)
    subprocess.run(["cp", FINAL_MP4, zajuna_video_dir], check=True)
    subprocess.run(["cp", FINAL_MP4, zajuna_dir], check=True)

    # Copy also to sitio_pitch_web so the Apache server can stream it!
    sitio_video_dir = os.path.join(BASE_DIR, "sitio_pitch_web", "video")
    os.makedirs(sitio_video_dir, exist_ok=True)
    subprocess.run(["cp", FINAL_MP4, os.path.join(sitio_video_dir, "pitch_bella_italia.mp4")], check=True)

    # Check file stats
    size_mb = os.path.getsize(FINAL_MP4) / (1024 * 1024)
    print(f"=== RESULTADO FINAL ===")
    print(f"Ruta: {FINAL_MP4}")
    print(f"Tamaño: {size_mb:.2f} MB")
    print(f"Duración: {TOTAL_DURATION} s (<= 59 s requeridos)")
    print("Video listo para entrega y reproducción.")

if __name__ == "__main__":
    main()
