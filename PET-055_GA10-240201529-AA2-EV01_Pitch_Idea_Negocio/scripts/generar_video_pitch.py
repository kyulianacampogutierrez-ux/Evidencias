#!/usr/bin/env python3
"""
Generador del Video Elevator Pitch Tipo TikTok (9:16 Vertical HD 1080x1920)
Versión Creativa, Dinámica y de Alto Contraste (Sin saturación de texto)
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

# Load Fonts with Extra Large Sizes for Mobile Readability
f_hud = ImageFont.truetype(FONT_BOLD, 26)
f_cat = ImageFont.truetype(FONT_BOLD, 30)
f_head = ImageFont.truetype(FONT_BOLD, 68)
f_head_large = ImageFont.truetype(FONT_BOLD, 74)
f_badge_title = ImageFont.truetype(FONT_BOLD, 38)
f_badge_sub = ImageFont.truetype(FONT_BOLD, 26)
f_sub_box = ImageFont.truetype(FONT_BOLD, 38)
f_cta = ImageFont.truetype(FONT_BOLD, 50)
f_pill = ImageFont.truetype(FONT_BOLD, 26)
f_tiktok_user = ImageFont.truetype(FONT_BOLD, 32)
f_tiktok_caption = ImageFont.truetype(FONT_REG, 24)
f_action_count = ImageFont.truetype(FONT_BOLD, 22)
f_badge = ImageFont.truetype(FONT_BOLD, 26)

# Source assets
LOGO_PATH = "/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-028_GA8-220501096-AA2-EV02_Modulos_Moviles_APK/codigo_fuente/app_react_native/android/app/src/main/res/drawable-xxxhdpi/splashscreen_logo.png"
CATALOG_PATH = "/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-018_GA7-220501096-AA3-EV02_Modulos_Probados_Historias_Usuario/capturas_pruebas/02_hu02_pizzas_catalogo_filtros.png"

resample_filter = getattr(getattr(Image, 'Resampling', Image), 'LANCZOS', Image.ANTIALIAS)
logo_img = Image.open(LOGO_PATH).convert("RGBA").resize((260, 260), resample_filter) if os.path.exists(LOGO_PATH) else None
catalog_img = Image.open(CATALOG_PATH).convert("RGBA").resize((740, 360), resample_filter) if os.path.exists(CATALOG_PATH) else None

# Helper to draw rounded rectangle
def draw_rounded_card(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

# 1. Synthesize Audio (Uses cached if exists)
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

# 2. Render Single Frame (Creative, High-Contrast, Big Typography)
def render_frame(frame_idx):
    t = frame_idx / FPS
    
    # Base background: Deep night slate
    im = Image.new("RGBA", (W, H), (10, 15, 29, 255))
    draw = ImageDraw.Draw(im)

    # Ambient glowing aura based on scene
    if t < 8.0:
        aura_col = (239, 68, 68, 30) # Crimson
    elif t < 20.0:
        aura_col = (245, 158, 11, 35) # Gold
    elif t < 32.0:
        aura_col = (16, 185, 129, 30) # Emerald
    elif t < 43.0:
        aura_col = (59, 130, 246, 35) # Electric Blue
    else:
        aura_col = (245, 158, 11, 40) # Bright Gold

    draw.ellipse([-200, 150, 700, 1050], fill=aura_col)
    draw.ellipse([500, 750, 1400, 1650], fill=aura_col)

    # Dynamic floating golden embers (heat of pizza oven)
    for p in range(12):
        ember_x = int((p * 97 + math.sin(t * 2.0 + p) * 45) % (W - 100)) + 50
        ember_y = int((H - ((t * 70 + p * 150) % H)))
        ember_rad = int(3 + (p % 4))
        draw.ellipse([ember_x - ember_rad, ember_y - ember_rad, ember_x + ember_rad, ember_y + ember_rad], fill=(255, 200, 50, 140))

    # 1. Top HUD Bar (Progress & Institution)
    prog_w = int((frame_idx / TOTAL_FRAMES) * W)
    draw.rectangle([0, 0, W, 10], fill=(30, 41, 59, 255))
    draw.rectangle([0, 0, prog_w, 10], fill=(245, 158, 11, 255))

    # Top Badges (Y: 30..85)
    draw_rounded_card(draw, [50, 30, 480, 85], 25, (15, 23, 42, 230), (245, 158, 11, 220), 2)
    draw.text((70, 42), "SENA | ADSO - FICHA 3186681", font=f_hud, fill=(241, 245, 249))

    # Live Timer Badge
    time_str = f"{int(t):02d}:{int((t % 1)*10):01d} / 54s"
    draw_rounded_card(draw, [840, 30, 1030, 85], 25, (220, 38, 38, 230), (254, 202, 202, 200), 2)
    draw.ellipse([860, 50, 876, 66], fill=(255, 255, 255))
    draw.text((885, 42), time_str, font=f_hud, fill=(255, 255, 255))

    # Italian flag ribbon strip
    draw.rectangle([50, 102, 170, 110], fill=(0, 140, 69, 255))
    draw.rectangle([170, 102, 290, 110], fill=(244, 245, 240, 255))
    draw.rectangle([290, 102, 410, 110], fill=(205, 33, 42, 255))

    # SCENE CONTENT (Cards bound at X: 50..880 to avoid overlapping TikTok sidebar)
    if t < 8.0:
        # ESCENA 1: EL PROBLEMA REAL EN POPAYÁN
        draw_rounded_card(draw, [50, 125, 470, 185], 25, (239, 68, 68, 60), (239, 68, 68), 3)
        draw.text((75, 137), "🚨 PASO 1 • EL PROBLEMA", font=f_cat, fill=(255, 255, 255))

        draw.text((50, 205), "¿PIZZAS FRÍAS Y", font=f_head_large, fill=(255, 255, 255))
        draw.text((50, 285), "MASAS PESADAS?", font=f_head_large, fill=(239, 68, 68))

        # 3 Big Power Badges
        p_badges = [
            ("⏱️  DEMORAS DE 60+ MIN", "Llegan frías y arruinan tu cena", (239, 68, 68)),
            ("🤢  MASA ULTRA PESADA", "Levadura química sin fermentar", (245, 158, 11)),
            ("🥶  PIZZAS GRASOSAS", "Ingredientes de baja calidad", (59, 130, 246))
        ]
        y_pos = 380
        for title, sub, col in p_badges:
            draw_rounded_card(draw, [50, y_pos, 880, y_pos + 135], 22, (20, 28, 45, 245), col, 3)
            draw.text((75, y_pos + 22), title, font=f_badge_title, fill=col)
            draw.text((75, y_pos + 78), sub, font=f_badge_sub, fill=(241, 245, 249))
            y_pos += 160

        # Central Visual Graphic: Alert Banner
        draw_rounded_card(draw, [50, 890, 880, 1320], 25, (15, 23, 42, 240), (239, 68, 68, 200), 3)
        draw.text((80, 925), "EVALUACIÓN DEL MERCADO EN POPAYÁN", font=f_pill, fill=(248, 113, 113))
        draw.text((80, 990), "💥 72% de clientes insatisfechos con los tiempos.", font=f_badge_title, fill=(255, 255, 255))
        draw.text((80, 1070), "❌ Masas comerciales causan acidez y pesadez.", font=f_badge_title, fill=(255, 255, 255))
        draw.text((80, 1150), "⚡ ¡Popayán merece una auténtica pizza gourmet!", font=f_badge_title, fill=(253, 224, 71))
        draw.text((80, 1235), "CERO FERMENTACIÓN BIOLÓGICA EN LA CIUDAD", font=f_pill, fill=(148, 163, 184))

        subtitle_text = "¿Cansado de pedir pizza en Popayán y que llegue\nfría, grasosa o con una masa pesada que no te deja dormir?"

    elif t < 20.0:
        # ESCENA 2: LA SOLUCIÓN GOURMET - BELLA ITALIA
        draw_rounded_card(draw, [50, 125, 490, 185], 25, (16, 185, 129, 60), (16, 185, 129), 3)
        draw.text((75, 137), "🔥 PASO 2 • SOLUCIÓN GOURMET", font=f_cat, fill=(52, 211, 153))

        draw.text((50, 205), "¡LLEGÓ BELLA ITALIA!", font=f_head_large, fill=(255, 255, 255))
        draw.text((50, 285), "PIZZA ARTESANAL", font=f_head_large, fill=(245, 158, 11))

        # 3 Big Value Badges
        s_badges = [
            ("🌾  MASA MADRE 48 HORAS", "Fermentación biológica ultraligera", (245, 158, 11)),
            ("🌋  HORNO A 450 GRADOS", "Piedra volcánica a fuego vivo", (239, 68, 68)),
            ("⚡  LISTA EN 90 SEGUNDOS", "Corteza crocante y alvéolos aireados", (16, 185, 129))
        ]
        y_pos = 380
        for title, sub, col in s_badges:
            draw_rounded_card(draw, [50, y_pos, 880, y_pos + 135], 22, (20, 28, 45, 245), col, 3)
            draw.text((75, y_pos + 22), title, font=f_badge_title, fill=col)
            draw.text((75, y_pos + 78), sub, font=f_badge_sub, fill=(241, 245, 249))
            y_pos += 160

        # Central Visual Graphic: Logo + Badges
        draw_rounded_card(draw, [50, 890, 880, 1320], 25, (15, 23, 42, 240), (245, 158, 11, 200), 3)
        if logo_img:
            im.paste(logo_img, (80, 930), logo_img)
        draw.text((360, 950), "AUTÉNTICO ESTILO", font=f_head, fill=(255, 255, 255))
        draw.text((360, 1025), "NAPOLITANO", font=f_head, fill=(245, 158, 11))
        draw.text((360, 1115), "• 100% Sin levadura química", font=f_badge_title, fill=(52, 211, 153))
        draw.text((360, 1175), "• Sourdough de fermentación lenta", font=f_badge_title, fill=(255, 255, 255))
        draw.text((360, 1235), "• Borde inflado napolitano (canotto)", font=f_badge_title, fill=(253, 224, 71))

        subtitle_text = "¡Llegó Bella Italia Popayán! La auténtica pizza artesanal con\nmasa madre de 48h de fermentación y horneada a 450°C en 90s."

    elif t < 32.0:
        # ESCENA 3: TRADICIÓN ITALIANA + CORAZÓN CAUCANO
        draw_rounded_card(draw, [50, 125, 510, 185], 25, (245, 158, 11, 60), (245, 158, 11), 3)
        draw.text((75, 137), "🌿 PASO 3 • TRADICIÓN + CAUCA", font=f_cat, fill=(251, 191, 36))

        draw.text((50, 205), "TRADICIÓN ITALIANA CON", font=f_head, fill=(255, 255, 255))
        draw.text((50, 285), "CORAZÓN CAUCANO", font=f_head, fill=(16, 185, 129))

        d_badges = [
            ("🧀  QUESOS DE SILVIA, CAUCA", "Fior di latte fresco de productores locales", (16, 185, 129)),
            ("🍅  HUERTAS DEL CAUCA", "Albahaca y pomodoro orgánico campesino", (245, 158, 11)),
            ("💚  COMERCIO JUSTO LOCAL", "Compra directa sin intermediarios", (52, 211, 153))
        ]
        y_pos = 380
        for title, sub, col in d_badges:
            draw_rounded_card(draw, [50, y_pos, 880, y_pos + 135], 22, (20, 28, 45, 245), col, 3)
            draw.text((75, y_pos + 22), title, font=f_badge_title, fill=col)
            draw.text((75, y_pos + 78), sub, font=f_badge_sub, fill=(241, 245, 249))
            y_pos += 160

        # Central Visual Graphic: Regional Banner
        draw_rounded_card(draw, [50, 890, 880, 1320], 25, (15, 23, 42, 240), (16, 185, 129, 200), 3)
        draw.text((80, 925), "ALIANZA SOCIAL CAMPESINA Y SOSTENIBILIDAD", font=f_pill, fill=(52, 211, 153))
        draw.text((80, 990), "✨ 100% Digestión ultraligera garantizada.", font=f_badge_title, fill=(255, 255, 255))
        draw.text((80, 1070), "🌱 Empaques ecológicos de caña de azúcar.", font=f_badge_title, fill=(255, 255, 255))
        draw.text((80, 1150), "❤️ Sabor único con identidad gastronómica caucana.", font=f_badge_title, fill=(253, 224, 71))
        draw.text((80, 1235), "SILVIA • TIMBÍO • CAJIBÍO • POPAYÁN", font=f_pill, fill=(148, 163, 184))

        subtitle_text = "Unimos técnica italiana con insumos de nuestra tierra: quesos\ncampesinos de Silvia y hortalizas orgánicas del Cauca."

    elif t < 43.0:
        # ESCENA 4: INNOVACIÓN TECNOLÓGICA SENA ADSO
        draw_rounded_card(draw, [50, 125, 510, 185], 25, (59, 130, 246, 60), (59, 130, 246), 3)
        draw.text((75, 137), "🚀 PASO 4 • TECNOLOGÍA ADSO", font=f_cat, fill=(96, 165, 250))

        draw.text((50, 205), "WEB APP SENA ADSO +", font=f_head, fill=(255, 255, 255))
        draw.text((50, 285), "DELIVERY TÉRMICO", font=f_head, fill=(59, 130, 246))

        t_badges = [
            ("📱  PIDE EN 3 CLICS", "Plataforma web con tracking en tiempo real", (59, 130, 246)),
            ("🌡️  BAÚL TÉRMICO > 70°C", "Llega caliente y crocante a tu mesa", (245, 158, 11)),
            ("⏱️  ENTREGA EN < 30 MIN", "Garantía de puntualidad o postre gratis", (16, 185, 129))
        ]
        y_pos = 380
        for title, sub, col in t_badges:
            draw_rounded_card(draw, [50, y_pos, 880, y_pos + 135], 22, (20, 28, 45, 245), col, 3)
            draw.text((75, y_pos + 22), title, font=f_badge_title, fill=col)
            draw.text((75, y_pos + 78), sub, font=f_badge_sub, fill=(241, 245, 249))
            y_pos += 160

        # Central Visual Graphic: Catalog Image
        draw_rounded_card(draw, [50, 890, 880, 1320], 25, (15, 23, 42, 240), (59, 130, 246, 200), 3)
        if catalog_img:
            im.paste(catalog_img, (95, 930), catalog_img)
        draw.text((100, 1260), "⚡ SOFTWARE DESARROLLADO POR APRENDIZ SENA ADSO", font=f_pill, fill=(96, 165, 250))

        subtitle_text = "Con nuestra app web en ADSO pides en segundos y recibes\ntu pizza a más de 70°C en menos de 30 minutos."

    else:
        # ESCENA 5: CALL TO ACTION (CTA)
        draw_rounded_card(draw, [50, 125, 520, 185], 25, (245, 158, 11, 60), (245, 158, 11), 3)
        draw.text((75, 137), "📍 PASO 5 • LLAMADO A LA ACCIÓN", font=f_cat, fill=(251, 191, 36))

        draw.text((50, 205), "¡VIVE LA EXPERIENCIA", font=f_head_large, fill=(255, 255, 255))
        draw.text((50, 285), "BELLA ITALIA HOY!", font=f_head_large, fill=(245, 158, 11))

        c_badges = [
            ("🏛️  SEDE CENTRO HISTÓRICO", "Calle 4ta No. 3-45 • Popayán, Cauca", (245, 158, 11)),
            ("📲  WHATSAPP OFICIAL", "(+57) 312 890 4521 • Pedidos al instante", (16, 185, 129)),
            ("📋  MARCA REGISTRADA RUES", "Cámara de Comercio Popayán • CIIU 5611", (59, 130, 246))
        ]
        y_pos = 380
        for title, sub, col in c_badges:
            draw_rounded_card(draw, [50, y_pos, 880, y_pos + 135], 22, (20, 28, 45, 245), col, 3)
            draw.text((75, y_pos + 22), title, font=f_badge_title, fill=col)
            draw.text((75, y_pos + 78), sub, font=f_badge_sub, fill=(241, 245, 249))
            y_pos += 160

        # Giant Golden CTA Button
        draw_rounded_card(draw, [50, 890, 880, 1030], 28, (245, 158, 11), (255, 255, 255), 4)
        draw.text((120, 935), "🍕 ¡HAZ TU PEDIDO YA! 🍕", font=f_cta, fill=(15, 23, 42))

        # Brand Signature Card
        draw_rounded_card(draw, [50, 1060, 880, 1320], 25, (15, 23, 42, 240), (245, 158, 11, 200), 2)
        draw.text((80, 1090), "«Pasión italiana con corazón caucano»", font=f_badge_title, fill=(255, 255, 255))
        draw.text((80, 1160), "👩‍💻 Desarrollado por: Karen Yuliana Campo", font=f_badge_title, fill=(253, 224, 71))
        draw.text((80, 1225), "Tecnólogo en Análisis y Desarrollo de Software • Ficha 3186681", font=f_badge_sub, fill=(148, 163, 184))

        subtitle_text = "Visítanos en el Centro Histórico de Popayán o pide al WhatsApp.\n¡Bella Italia: Pasión italiana con corazón caucano! ¡Pide ya!"

    # 2. TikTok Right Sidebar Actions (Y: 650..1250, X: 920..1040)
    # Profile avatar
    draw.ellipse([930, 650, 1030, 750], fill=(245, 158, 11))
    draw.text((955, 680), "KC", font=f_head, fill=(15, 23, 42))
    draw.ellipse([965, 735, 995, 765], fill=(239, 68, 68))
    draw.text((973, 738), "+", font=f_badge, fill=(255, 255, 255))

    # Likes
    draw.ellipse([945, 790, 1015, 860], fill=(30, 41, 59, 220))
    draw.text((965, 805), "❤️", font=f_cat, fill=(239, 68, 68))
    draw.text((950, 870), "24.5K", font=f_action_count, fill=(255, 255, 255))

    # Comments
    draw.ellipse([945, 915, 1015, 985], fill=(30, 41, 59, 220))
    draw.text((965, 930), "💬", font=f_cat, fill=(255, 255, 255))
    draw.text((955, 995), "1,890", font=f_action_count, fill=(255, 255, 255))

    # Bookmarks
    draw.ellipse([945, 1040, 1015, 1110], fill=(30, 41, 59, 220))
    draw.text((965, 1055), "⭐", font=f_cat, fill=(245, 158, 11))
    draw.text((955, 1120), "5,410", font=f_action_count, fill=(255, 255, 255))

    # Share
    draw.ellipse([945, 1165, 1015, 1235], fill=(30, 41, 59, 220))
    draw.text((965, 1180), "↗️", font=f_cat, fill=(255, 255, 255))
    draw.text((962, 1245), "920", font=f_action_count, fill=(255, 255, 255))

    # Spinning Vinyl Icon
    vinyl_angle = (frame_idx * 6) % 360
    draw.ellipse([940, 1300, 1020, 1380], fill=(15, 23, 42), outline=(245, 158, 11), width=4)
    draw.ellipse([965, 1325, 995, 1355], fill=(239, 68, 68))

    # 3. High-Contrast TikTok Subtitles Overlay (Y: 1390..1570)
    draw_rounded_card(draw, [50, 1390, 1030, 1570], 25, (0, 0, 0, 235), (245, 158, 11, 240), 3)
    draw.text((80, 1425), subtitle_text, font=f_sub_box, fill=(253, 224, 71))

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
    draw.rectangle([0, 1890, W, 1920], fill=(10, 15, 29, 255))

    return im.convert("RGB")

# 3. Main Pipe Video Rendering
def main():
    build_audio()

    print("--- [PITCH] 2. Renderizando y codificando video MP4 vertical (1080x1920, 30fps, 54s)... ---")
    
    temp_mp4 = os.path.join(TMP_DIR, "output_pitch_creative.mp4")
    
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
        "/data/output_pitch_creative.mp4"
    ]

    print("Ejecutando pipeline FFmpeg...")
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

    print(f"Generando {TOTAL_FRAMES} frames de alta legibilidad...")
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
    
    # Replace final video
    subprocess.run(["cp", temp_mp4, FINAL_MP4], check=True)
    
    # Copy to Zajuna delivery folders
    zajuna_dir = "/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA10-240201529-AA2-EV01"
    zajuna_video_dir = os.path.join(zajuna_dir, "video")
    os.makedirs(zajuna_video_dir, exist_ok=True)
    subprocess.run(["cp", FINAL_MP4, zajuna_video_dir], check=True)
    subprocess.run(["cp", FINAL_MP4, zajuna_dir], check=True)

    # Copy also to sitio_pitch_web so Apache streams the updated video
    sitio_video_dir = os.path.join(BASE_DIR, "sitio_pitch_web", "video")
    os.makedirs(sitio_video_dir, exist_ok=True)
    subprocess.run(["cp", FINAL_MP4, os.path.join(sitio_video_dir, "pitch_bella_italia.mp4")], check=True)

    # Copy to brain artifact directory as well
    brain_dir = "/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603"
    subprocess.run(["cp", FINAL_MP4, brain_dir], check=True)

    # Check file stats
    size_mb = os.path.getsize(FINAL_MP4) / (1024 * 1024)
    print(f"=== RESULTADO FINAL ===")
    print(f"Ruta: {FINAL_MP4}")
    print(f"Tamaño: {size_mb:.2f} MB")
    print(f"Duración: {TOTAL_DURATION} s (<= 59 s requeridos)")
    print("Video renovado listo para entrega y reproducción.")

if __name__ == "__main__":
    main()
