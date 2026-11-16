#!/usr/bin/env python3
"""
Generador del Video Elevator Pitch Tipo TikTok (9:16 Vertical HD 1080x1920)
Versión Creativa, Dinámica y de Ultra Alta Legibilidad (Sin Saturación de Texto)
Ensamblado y exportado con FilmCraft CLI usando el preset oficial "TikTok 1080×1920".

Evidencia: GA10-240201529-AA2-EV01 - Pitch idea de negocio
Aprendiz: Karen Yuliana Campo - SENA ADSO Ficha 3186681
Duración: 54 segundos (Límite máximo de guía: 59 segundos)
"""

import os
import sys
import json
import math
import wave
import struct
import shutil
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
VISUAL_STREAM_MP4 = os.path.join(TMP_DIR, "visual_stream.mp4")
FILMCRAFT_PROJ = os.path.join(TMP_DIR, "PizzeriaBellaItaliaPitch.fcproj")
FILMCRAFT_EXPORT_MP4 = os.path.join(TMP_DIR, "filmcraft_tiktok_export.mp4")

FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

# Ultra-legible typography sizes optimized for mobile viewing
f_hud = ImageFont.truetype(FONT_BOLD, 26)
f_cat = ImageFont.truetype(FONT_BOLD, 30)
f_head_xl = ImageFont.truetype(FONT_BOLD, 64)
f_head_huge = ImageFont.truetype(FONT_BOLD, 74)
f_card_title = ImageFont.truetype(FONT_BOLD, 38)
f_card_sub = ImageFont.truetype(FONT_BOLD, 26)
f_sub_white = ImageFont.truetype(FONT_BOLD, 42)
f_sub_active = ImageFont.truetype(FONT_BOLD, 44)
f_cta_btn = ImageFont.truetype(FONT_BOLD, 52)
f_pill_txt = ImageFont.truetype(FONT_BOLD, 28)
f_tiktok_user = ImageFont.truetype(FONT_BOLD, 32)
f_tiktok_caption = ImageFont.truetype(FONT_REG, 24)
f_action_count = ImageFont.truetype(FONT_BOLD, 22)
f_badge = ImageFont.truetype(FONT_BOLD, 26)

# Source assets
LOGO_PATH = "/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-028_GA8-220501096-AA2-EV02_Modulos_Moviles_APK/codigo_fuente/app_react_native/android/app/src/main/res/drawable-xxxhdpi/splashscreen_logo.png"
CATALOG_PATH = "/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-018_GA7-220501096-AA3-EV02_Modulos_Probados_Historias_Usuario/capturas_pruebas/02_hu02_pizzas_catalogo_filtros.png"

resample_filter = getattr(getattr(Image, 'Resampling', Image), 'LANCZOS', Image.ANTIALIAS)
logo_img = Image.open(LOGO_PATH).convert("RGBA").resize((280, 280), resample_filter) if os.path.exists(LOGO_PATH) else None
catalog_img = Image.open(CATALOG_PATH).convert("RGBA").resize((740, 360), resample_filter) if os.path.exists(CATALOG_PATH) else None


def draw_rounded_card(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


# 1. Synthesize Audio
def build_audio():
    if os.path.exists(MASTER_AUDIO_WAV) and os.path.getsize(MASTER_AUDIO_WAV) > 1000000:
        print(f"--- [PITCH] 1. Usando pista de audio existente en {MASTER_AUDIO_WAV} ---")
        return
    print("--- [PITCH] 1. Sintetizando locución en español y banda sonora musical... ---")
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


# 2. Dynamic Karaoke Subtitle Resolver (TikTok retention caption skill)
def get_dynamic_caption(t):
    """
    Returns (prefix_text, highlight_text, suffix_text) for active word pop-in.
    Safe 3-5 word pages with high visual pop.
    """
    if t < 2.6:
        return ("¿Cansado de pedir pizza en ", "POPAYÁN", "...")
    elif t < 5.2:
        return ("...y que llegue ", "FRÍA Y GRASOSA", "?")
    elif t < 8.0:
        return ("¿O con una masa ", "SÚPER PESADA", "?")
    elif t < 11.5:
        return ("¡Llegó ", "BELLA ITALIA POPAYÁN", "!")
    elif t < 15.5:
        return ("Masa madre con ", "48H DE FERMENTACIÓN", "")
    elif t < 20.0:
        return ("¡Horneada a 450°C en ", "SOLO 90 SEGUNDOS", "!")
    elif t < 24.0:
        return ("Quesos campesinos de ", "SILVIA, CAUCA", "")
    elif t < 28.0:
        return ("Hortalizas orgánicas ", "DE NUESTRA TIERRA", "")
    elif t < 32.0:
        return ("¡Textura crocante y ", "DIGESTIÓN LIGERA", "!")
    elif t < 36.0:
        return ("Web App desarrollada en ", "SENA ADSO", "")
    elif t < 39.5:
        return ("Pide en segundos con ", "TRACKING EN TIEMPO REAL", "")
    elif t < 43.0:
        return ("Llega a más de 70°C en ", "MENOS DE 30 MINUTOS", "")
    elif t < 47.0:
        return ("Visítanos en el ", "CENTRO HISTÓRICO", "")
    elif t < 50.5:
        return ("O pide al ", "WHATSAPP OFICIAL", "")
    else:
        return ("¡Pasión italiana con ", "CORAZÓN CAUCANO", "!")


# 3. Render Single Frame
def render_frame(frame_idx):
    t = frame_idx / FPS
    
    # Base background: Deep rich dark slate
    im = Image.new("RGBA", (W, H), (11, 15, 25, 255))
    draw = ImageDraw.Draw(im)

    # Ambient glowing aura based on scene
    if t < 8.0:
        aura_col = (239, 68, 68, 32) # Crimson danger
    elif t < 20.0:
        aura_col = (245, 158, 11, 35) # Gold oven heat
    elif t < 32.0:
        aura_col = (16, 185, 129, 32) # Emerald regional
    elif t < 43.0:
        aura_col = (59, 130, 246, 35) # Electric Blue tech
    else:
        aura_col = (245, 158, 11, 40) # Golden celebration

    draw.ellipse([-150, 200, 750, 1100], fill=aura_col)
    draw.ellipse([450, 700, 1350, 1600], fill=aura_col)

    # Dynamic floating golden embers (heat of artisanal pizza oven)
    for p in range(14):
        ember_x = int((p * 83 + math.sin(t * 2.5 + p) * 40) % (W - 120)) + 60
        ember_y = int((H - ((t * 80 + p * 140) % H)))
        ember_rad = int(3 + (p % 4))
        draw.ellipse([ember_x - ember_rad, ember_y - ember_rad, ember_x + ember_rad, ember_y + ember_rad], fill=(255, 200, 50, 150))

    # Top HUD Bar (Progress & Institution)
    prog_w = int((frame_idx / TOTAL_FRAMES) * W)
    draw.rectangle([0, 0, W, 10], fill=(30, 41, 59, 255))
    draw.rectangle([0, 0, prog_w, 10], fill=(245, 158, 11, 255))

    # Top Badges (Y: 28..82)
    draw_rounded_card(draw, [55, 28, 490, 82], 25, (15, 23, 42, 235), (245, 158, 11, 220), 2)
    draw.text((75, 40), "SENA | ADSO - FICHA 3186681", font=f_hud, fill=(241, 245, 249))

    # Live Timer Badge
    time_str = f"{int(t):02d}:{int((t % 1)*10):01d} / 54s"
    draw_rounded_card(draw, [840, 28, 1025, 82], 25, (220, 38, 38, 235), (254, 202, 202, 200), 2)
    draw.ellipse([858, 48, 874, 64], fill=(255, 255, 255))
    draw.text((885, 40), time_str, font=f_hud, fill=(255, 255, 255))

    # Italian flag ribbon strip
    draw.rectangle([55, 96, 175, 104], fill=(0, 140, 69, 255))
    draw.rectangle([175, 96, 295, 104], fill=(244, 245, 240, 255))
    draw.rectangle([295, 96, 415, 104], fill=(205, 33, 42, 255))

    # MAIN CONTENT BY SCENE (Bounded between X: 55..880 to avoid TikTok action bar)
    if t < 8.0:
        # ESCENA 1: EL PROBLEMA REAL EN POPAYÁN
        draw_rounded_card(draw, [55, 120, 500, 180], 25, (239, 68, 68, 60), (239, 68, 68), 3)
        draw.text((80, 133), "🚨 PASO 1 • EL PROBLEMA", font=f_cat, fill=(255, 255, 255))

        draw.text((55, 200), "¿PIZZAS FRÍAS Y", font=f_head_huge, fill=(255, 255, 255))
        draw.text((55, 280), "MASAS PESADAS?", font=f_head_huge, fill=(239, 68, 68))

        # 3 Clean, Punchy Power Cards
        p_cards = [
            ("⏱️  DEMORAS DE 60+ MIN", "Llegan frías y arruinan tu cena", (239, 68, 68)),
            ("🤢  MASA ULTRA PESADA", "Levadura química sin fermentar", (245, 158, 11)),
            ("🥶  PIZZAS GRASOSAS", "Ingredientes de baja calidad", (59, 130, 246))
        ]
        y_pos = 385
        for title, sub, col in p_cards:
            draw_rounded_card(draw, [55, y_pos, 880, y_pos + 130], 22, (18, 25, 42, 245), col, 3)
            draw.text((80, y_pos + 22), title, font=f_card_title, fill=col)
            draw.text((80, y_pos + 76), sub, font=f_card_sub, fill=(241, 245, 249))
            y_pos += 155

        # Creative Visual Stat Banner
        draw_rounded_card(draw, [55, 870, 880, 1340], 25, (15, 23, 42, 240), (239, 68, 68, 200), 3)
        draw_rounded_card(draw, [85, 900, 480, 950], 18, (239, 68, 68, 80), (239, 68, 68), 2)
        draw.text((105, 912), "DIAGNÓSTICO EN POPAYÁN", font=f_pill_txt, fill=(254, 202, 202))

        # Big percentage highlight
        draw.text((85, 980), "72%", font=f_head_huge, fill=(239, 68, 68))
        draw.text((250, 990), "DE CLIENTES INSATISFECHOS\nCON TIEMPOS Y CALIDAD", font=f_card_title, fill=(255, 255, 255))

        draw.rectangle([85, 1100, 850, 1104], fill=(51, 65, 85))
        draw.text((85, 1130), "❌ Masas comerciales producen acidez y pesadez", font=f_card_title, fill=(255, 255, 255))
        draw.text((85, 1205), "⚡ ¡Popayán merece una auténtica pizza artesanal!", font=f_card_title, fill=(253, 224, 71))
        draw.text((85, 1275), "CERO FERMENTACIÓN BIOLÓGICA EN LA CIUDAD", font=f_card_sub, fill=(148, 163, 184))

    elif t < 20.0:
        # ESCENA 2: LA SOLUCIÓN GOURMET - BELLA ITALIA
        draw_rounded_card(draw, [55, 120, 520, 180], 25, (16, 185, 129, 60), (16, 185, 129), 3)
        draw.text((80, 133), "🔥 PASO 2 • SOLUCIÓN GOURMET", font=f_cat, fill=(52, 211, 153))

        draw.text((55, 200), "¡LLEGÓ BELLA ITALIA!", font=f_head_huge, fill=(255, 255, 255))
        draw.text((55, 280), "PIZZA ARTESANAL", font=f_head_huge, fill=(245, 158, 11))

        # 3 Value Badges
        s_cards = [
            ("🌾  MASA MADRE 48 HORAS", "Fermentación biológica ultraligera", (245, 158, 11)),
            ("🌋  HORNO A 450 GRADOS", "Piedra volcánica a fuego vivo", (239, 68, 68)),
            ("⚡  LISTA EN 90 SEGUNDOS", "Corteza crocante y alvéolos aireados", (16, 185, 129))
        ]
        y_pos = 385
        for title, sub, col in s_cards:
            draw_rounded_card(draw, [55, y_pos, 880, y_pos + 130], 22, (18, 25, 42, 245), col, 3)
            draw.text((80, y_pos + 22), title, font=f_card_title, fill=col)
            draw.text((80, y_pos + 76), sub, font=f_card_sub, fill=(241, 245, 249))
            y_pos += 155

        # Creative Logo & Quality Showcase
        draw_rounded_card(draw, [55, 870, 880, 1340], 25, (15, 23, 42, 240), (245, 158, 11, 200), 3)
        if logo_img:
            im.paste(logo_img, (85, 930), logo_img)
        draw.text((390, 940), "ESTILO NAPOLITANO", font=f_head_xl, fill=(255, 255, 255))
        draw.text((390, 1015), "100% ARTESANAL", font=f_head_xl, fill=(245, 158, 11))
        draw.text((390, 1110), "• Cero levadura química industrial", font=f_card_title, fill=(52, 211, 153))
        draw.text((390, 1175), "• Sourdough de digestión perfecta", font=f_card_title, fill=(255, 255, 255))
        draw.text((390, 1240), "• Borde inflado napolitano (canotto)", font=f_card_title, fill=(253, 224, 71))

    elif t < 32.0:
        # ESCENA 3: TRADICIÓN ITALIANA + CORAZÓN CAUCANO
        draw_rounded_card(draw, [55, 120, 540, 180], 25, (245, 158, 11, 60), (245, 158, 11), 3)
        draw.text((80, 133), "🌿 PASO 3 • TRADICIÓN + CAUCA", font=f_cat, fill=(251, 191, 36))

        draw.text((55, 200), "TÉCNICA ITALIANA CON", font=f_head_xl, fill=(255, 255, 255))
        draw.text((55, 280), "CORAZÓN CAUCANO", font=f_head_xl, fill=(16, 185, 129))

        d_cards = [
            ("🧀  QUESOS DE SILVIA, CAUCA", "Fior di latte fresco de productores locales", (16, 185, 129)),
            ("🍅  HUERTAS DEL CAUCA", "Albahaca y pomodoro orgánico campesino", (245, 158, 11)),
            ("💚  COMERCIO JUSTO DIRECTO", "Compra directa sin intermediarios", (52, 211, 153))
        ]
        y_pos = 385
        for title, sub, col in d_cards:
            draw_rounded_card(draw, [55, y_pos, 880, y_pos + 130], 22, (18, 25, 42, 245), col, 3)
            draw.text((80, y_pos + 22), title, font=f_card_title, fill=col)
            draw.text((80, y_pos + 76), sub, font=f_card_sub, fill=(241, 245, 249))
            y_pos += 155

        # Creative Regional Banner
        draw_rounded_card(draw, [55, 870, 880, 1340], 25, (15, 23, 42, 240), (16, 185, 129, 200), 3)
        draw_rounded_card(draw, [85, 900, 570, 950], 18, (16, 185, 129, 80), (16, 185, 129), 2)
        draw.text((105, 912), "COMPROMISO SOCIAL Y SOSTENIBLE", font=f_pill_txt, fill=(167, 243, 208))

        draw.text((85, 980), "✨ 100% Digestión ultraligera garantizada", font=f_card_title, fill=(255, 255, 255))
        draw.text((85, 1060), "🌱 Empaques ecológicos de caña de azúcar", font=f_card_title, fill=(255, 255, 255))
        draw.text((85, 1140), "❤️ Sabor único con identidad gastronómica caucana", font=f_card_title, fill=(253, 224, 71))
        draw.rectangle([85, 1225, 850, 1229], fill=(51, 65, 85))
        draw.text((85, 1260), "SILVIA • TIMBÍO • CAJIBÍO • POPAYÁN", font=f_card_title, fill=(52, 211, 153))

    elif t < 43.0:
        # ESCENA 4: INNOVACIÓN TECNOLÓGICA SENA ADSO
        draw_rounded_card(draw, [55, 120, 530, 180], 25, (59, 130, 246, 60), (59, 130, 246), 3)
        draw.text((80, 133), "🚀 PASO 4 • TECNOLOGÍA ADSO", font=f_cat, fill=(96, 165, 250))

        draw.text((55, 200), "WEB APP SENA ADSO +", font=f_head_xl, fill=(255, 255, 255))
        draw.text((55, 280), "DELIVERY TÉRMICO", font=f_head_xl, fill=(59, 130, 246))

        t_cards = [
            ("📱  PIDE EN 3 CLICS", "Plataforma web con tracking en tiempo real", (59, 130, 246)),
            ("🌡️  BAÚL TÉRMICO > 70°C", "Llega caliente y crocante a tu mesa", (245, 158, 11)),
            ("⏱️  ENTREGA EN < 30 MIN", "Garantía de puntualidad o postre gratis", (16, 185, 129))
        ]
        y_pos = 385
        for title, sub, col in t_cards:
            draw_rounded_card(draw, [55, y_pos, 880, y_pos + 130], 22, (18, 25, 42, 245), col, 3)
            draw.text((80, y_pos + 22), title, font=f_card_title, fill=col)
            draw.text((80, y_pos + 76), sub, font=f_card_sub, fill=(241, 245, 249))
            y_pos += 155

        # Creative App Showcase Graphic
        draw_rounded_card(draw, [55, 870, 880, 1340], 25, (15, 23, 42, 240), (59, 130, 246, 200), 3)
        if catalog_img:
            im.paste(catalog_img, (95, 900), catalog_img)
        draw_rounded_card(draw, [95, 1270, 840, 1320], 18, (59, 130, 246, 80), (59, 130, 246), 2)
        draw.text((120, 1282), "⚡ SOFTWARE DESARROLLADO POR APRENDIZ SENA ADSO", font=f_pill_txt, fill=(191, 219, 254))

    else:
        # ESCENA 5: CALL TO ACTION (CTA)
        draw_rounded_card(draw, [55, 120, 540, 180], 25, (245, 158, 11, 60), (245, 158, 11), 3)
        draw.text((80, 133), "📍 PASO 5 • LLAMADO A LA ACCIÓN", font=f_cat, fill=(251, 191, 36))

        draw.text((55, 200), "¡VIVE LA EXPERIENCIA", font=f_head_huge, fill=(255, 255, 255))
        draw.text((55, 280), "BELLA ITALIA HOY!", font=f_head_huge, fill=(245, 158, 11))

        c_cards = [
            ("🏛️  SEDE CENTRO HISTÓRICO", "Calle 4ta No. 3-45 • Popayán, Cauca", (245, 158, 11)),
            ("📲  WHATSAPP OFICIAL", "(+57) 312 890 4521 • Pedidos al instante", (16, 185, 129)),
            ("📋  MARCA REGISTRADA RUES", "Cámara de Comercio Popayán • Matrícula Activa", (59, 130, 246))
        ]
        y_pos = 385
        for title, sub, col in c_cards:
            draw_rounded_card(draw, [55, y_pos, 880, y_pos + 130], 22, (18, 25, 42, 245), col, 3)
            draw.text((80, y_pos + 22), title, font=f_card_title, fill=col)
            draw.text((80, y_pos + 76), sub, font=f_card_sub, fill=(241, 245, 249))
            y_pos += 155

        # Giant Golden CTA Button (pulsing slightly with time)
        pulse = int(math.sin(t * 6.0) * 4)
        draw_rounded_card(draw, [55 - pulse, 870 - pulse, 880 + pulse, 1010 + pulse], 28, (245, 158, 11), (255, 255, 255), 4)
        draw.text((110, 915), "🍕 ¡HAZ TU PEDIDO YA! 🍕", font=f_cta_btn, fill=(15, 23, 42))

        # Brand Signature Card
        draw_rounded_card(draw, [55, 1040, 880, 1340], 25, (15, 23, 42, 240), (245, 158, 11, 200), 2)
        draw.text((85, 1070), "«Pasión italiana con corazón caucano»", font=f_card_title, fill=(255, 255, 255))
        draw.text((85, 1145), "👩‍💻 Desarrollado por: Karen Yuliana Campo", font=f_card_title, fill=(253, 224, 71))
        draw.text((85, 1215), "Tecnóloga en Análisis y Desarrollo de Software", font=f_card_title, fill=(52, 211, 153))
        draw.text((85, 1275), "SENA CTPI Regional Cauca • Ficha 3186681", font=f_card_sub, fill=(148, 163, 184))

    # TikTok Right Sidebar Actions (Y: 650..1250, X: 920..1040)
    # Profile avatar
    draw.ellipse([930, 650, 1030, 750], fill=(245, 158, 11))
    draw.text((955, 680), "KC", font=f_head_xl, fill=(15, 23, 42))
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
    draw.ellipse([940, 1300, 1020, 1380], fill=(15, 23, 42), outline=(245, 158, 11), width=4)
    draw.ellipse([965, 1325, 995, 1355], fill=(239, 68, 68))

    # Ultra High-Contrast Karaoke Dynamic Subtitles (Y: 1410..1560)
    # Designed as per caption-animation skill: active word pop-in & karaoke highlight
    draw_rounded_card(draw, [55, 1410, 1025, 1560], 25, (0, 0, 0, 240), (245, 158, 11, 240), 3)
    pfx, highlight, sfx = get_dynamic_caption(t)
    
    # Calculate text positioning
    # Left margin
    x_cur = 85
    y_sub = 1460
    
    draw.text((x_cur, y_sub), pfx, font=f_sub_white, fill=(255, 255, 255))
    pfx_len = draw.textlength(pfx, font=f_sub_white)
    x_cur += pfx_len

    draw.text((x_cur, y_sub - 1), highlight, font=f_sub_active, fill=(253, 224, 71)) # Bright golden active pop
    hl_len = draw.textlength(highlight, font=f_sub_active)
    x_cur += hl_len

    if sfx:
        draw.text((x_cur, y_sub), sfx, font=f_sub_white, fill=(255, 255, 255))

    # TikTok Bottom Bar (User info, caption, audio) (Y: 1590..1870)
    draw.text((55, 1600), "@karen_campo_adso", font=f_tiktok_user, fill=(255, 255, 255))
    draw.ellipse([380, 1608, 405, 1633], fill=(59, 130, 246))
    draw.text((386, 1609), "✓", font=f_hud, fill=(255, 255, 255))

    caption = "Pizzería Gourmet Bella Italia Popayán | Pasión italiana con corazón caucano 🍕✨\n#SENA #ADSO #Pitch #Emprendimiento #Popayán #MasaMadre48h"
    draw.text((55, 1650), caption, font=f_tiktok_caption, fill=(226, 232, 240))

    # Audio track marquee
    draw.text((55, 1720), "🎵  Bella Italia - Original Soundtrack (SENA Popayán)", font=f_tiktok_caption, fill=(245, 158, 11))

    return im


def main():
    print("=================================================================")
    print("  GENERADOR DE VIDEO PITCH BELLA ITALIA - FILMCRAFT CLI TIKTOK   ")
    print("  Evidencia: GA10-240201529-AA2-EV01 | Aprendiz: Karen Campo     ")
    print("=================================================================")

    # Step 1: Synthesize audio
    build_audio()

    # Step 2: Render visual stream to MP4
    print("--- [PITCH] 2. Renderizando flujo visual de alta legibilidad (1080x1920, 30fps)... ---")
    raw_video_cmd = [
        "docker", "run", "--rm", "-i",
        "-u", f"{os.getuid()}:{os.getgid()}",
        "-v", f"{TMP_DIR}:/data",
        "sena-ffmpeg:alpine",
        "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{W}x{H}",
        "-pix_fmt", "rgba",
        "-r", str(FPS),
        "-i", "-",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "20",
        "-pix_fmt", "yuv420p",
        "/data/visual_stream.mp4"
    ]

    print("Iniciando codificación del stream visual...")
    proc = subprocess.Popen(raw_video_cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

    print(f"Generando {TOTAL_FRAMES} frames...")
    for f in range(TOTAL_FRAMES):
        frame_im = render_frame(f)
        proc.stdin.write(frame_im.tobytes())
        if f % 150 == 0 or f == TOTAL_FRAMES - 1:
            print(f"Progreso visual: frame {f}/{TOTAL_FRAMES} ({f/TOTAL_FRAMES*100:.1f}%)")

    proc.stdin.flush()
    proc.stdin.close()
    stderr_out = proc.stderr.read().decode('utf-8', errors='ignore')
    proc.wait()

    if proc.returncode != 0:
        print("Error en codificación visual:\n", stderr_out)
        sys.exit(1)

    print(f"Stream visual listo en {VISUAL_STREAM_MP4}")

    # Step 3: Use FilmCraft CLI to assemble the project and export with "TikTok 1080×1920" preset
    print("--- [PITCH] 3. Ensamblando y exportando con FilmCraft CLI (Preset: 'TikTok 1080×1920')... ---")

    script_jsonl = os.path.join(TMP_DIR, "filmcraft_assembly.jsonl")
    with open(script_jsonl, "w") as f:
        # Create project
        f.write(json.dumps({"id": "file.newProject", "params": {"name": "PizzeriaBellaItaliaPitch"}}) + "\n")
        # Create sequence
        f.write(json.dumps({
            "id": "file.newSequence",
            "params": {
                "name": "PitchTikTokSequence",
                "width": 1080,
                "height": 1920,
                "fps": 30.0,
                "sampleRate": 44100,
                "mix": "Stereo"
            }
        }) + "\n")
        # Import visual video and audio track
        f.write(json.dumps({"id": "file.import", "params": {"paths": [VISUAL_STREAM_MP4, MASTER_AUDIO_WAV]}}) + "\n")
        # Place visual stream on V1
        f.write(json.dumps({
            "id": "timeline.place",
            "params": {
                "item": 8,
                "track": "V1",
                "seconds": 0.0,
                "video": True,
                "audio": False
            }
        }) + "\n")
        # Place master audio on A1
        f.write(json.dumps({
            "id": "timeline.place",
            "params": {
                "item": 9,
                "audioTrack": "A1",
                "seconds": 0.0,
                "video": False,
                "audio": True
            }
        }) + "\n")
        # Save project
        f.write(json.dumps({"id": "file.saveAs", "params": {"path": FILMCRAFT_PROJ}}) + "\n")

    print("Ejecutando ensamble de timeline en FilmCraft CLI...")
    res = subprocess.run(["filmcraft-cli", "run", script_jsonl], capture_output=True, text=True)
    if res.returncode != 0:
        print("Error en FilmCraft CLI assembly:\n", res.stderr, res.stdout)
        sys.exit(1)
    print("Timeline ensamblado exitosamente en FilmCraft:")
    print(res.stdout)

    # Step 4: Export with FilmCraft CLI using the official TikTok preset
    print("Exportando con FilmCraft CLI preset 'TikTok 1080×1920'...")
    export_cmd = [
        "filmcraft-cli",
        "--project", FILMCRAFT_PROJ,
        "export", FILMCRAFT_EXPORT_MP4,
        "--preset", "TikTok 1080×1920",
        "--range", "entire"
    ]
    res_export = subprocess.run(export_cmd, capture_output=True, text=True)
    if res_export.returncode != 0:
        print("Error en FilmCraft export:\n", res_export.stderr, res_export.stdout)
        sys.exit(1)
    print("Exportación de FilmCraft finalizada con éxito:")
    print(res_export.stdout)

    # Step 5: Distribute to destination directories
    print("--- [PITCH] 4. Distribuyendo video final MP4 a todas las carpetas... ---")
    shutil.copy2(FILMCRAFT_EXPORT_MP4, FINAL_MP4)

    # Delivery folder
    zajuna_dir = "/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA10-240201529-AA2-EV01"
    zajuna_video_dir = os.path.join(zajuna_dir, "video")
    os.makedirs(zajuna_video_dir, exist_ok=True)
    shutil.copy2(FINAL_MP4, os.path.join(zajuna_video_dir, "GA10-240201529-AA2-EV01_Pitch_Idea_Negocio.mp4"))
    shutil.copy2(FINAL_MP4, os.path.join(zajuna_dir, "GA10-240201529-AA2-EV01_Pitch_Idea_Negocio.mp4"))

    # Web portal for live streaming
    sitio_video_dir = os.path.join(BASE_DIR, "sitio_pitch_web", "video")
    os.makedirs(sitio_video_dir, exist_ok=True)
    shutil.copy2(FINAL_MP4, os.path.join(sitio_video_dir, "pitch_bella_italia.mp4"))

    # Brain artifacts directory
    brain_dir = "/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603"
    shutil.copy2(FINAL_MP4, os.path.join(brain_dir, "GA10-240201529-AA2-EV01_Pitch_Idea_Negocio.mp4"))

    size_mb = os.path.getsize(FINAL_MP4) / (1024 * 1024)
    print("=================================================================")
    print("  VIDEO PITCH TIKTOK GENERADO Y EXPORTADO EXITOSAMENTE CON       ")
    print("  FILMCRAFT CLI ('TikTok 1080×1920')                             ")
    print(f"  Ruta local:   {FINAL_MP4}")
    print(f"  Tamaño:       {size_mb:.2f} MB")
    print(f"  Duración:     {TOTAL_DURATION} s (<= 59 s requeridos)")
    print("=================================================================")


if __name__ == "__main__":
    main()
