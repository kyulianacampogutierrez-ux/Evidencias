#!/usr/bin/env python3
"""
Generador del Video Elevator Pitch Tipo TikTok (9:16 Vertical HD 1080x1920)
Versión Premium Gourmet, Ultra Minimalista, de Alta Legibilidad y Elegancia Visual.
Cumple rigurosamente con los lineamientos de iart-ai/tiktok-video-skills:
- Safe Area universal 900x1400 (despejada de falsos botones y de sobrecarga de texto).
- Subtítulos dinámicos estilo karaoke pop-in (caption-animation) con resaltado amarillo.
- Reducción drástica de texto (una sola idea central por escena).
- Ensamblado y exportado con FilmCraft CLI usando el preset oficial "TikTok 1080×1920".

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
TOTAL_DURATION = 51.82
TOTAL_FRAMES = int(FPS * TOTAL_DURATION) # 1554 frames
SAMPLE_RATE = 44100
TOTAL_AUDIO_SAMPLES = int(SAMPLE_RATE * TOTAL_DURATION)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
VIDEO_DIR = os.path.join(BASE_DIR, "video")
TMP_DIR = "/tmp/pitch_build"
os.makedirs(VIDEO_DIR, exist_ok=True)
os.makedirs(TMP_DIR, exist_ok=True)

USER_AUDIO_MP4 = "/home/danilo/Escritorio/Karen/SENA/CDE/base_conocimiento/audio_tiktok.mp4"
USER_VOICE_WAV = os.path.join(TMP_DIR, "user_voice_44k.wav")
FINAL_MP4 = os.path.join(VIDEO_DIR, "GA10-240201529-AA2-EV01_Pitch_Idea_Negocio.mp4")
MASTER_AUDIO_WAV = os.path.join(TMP_DIR, "master_audio.wav")
VISUAL_STREAM_MP4 = os.path.join(TMP_DIR, "visual_stream.mp4")
FILMCRAFT_PROJ = os.path.join(TMP_DIR, "PizzeriaBellaItaliaPitch.fcproj")
FILMCRAFT_EXPORT_MP4 = os.path.join(TMP_DIR, "filmcraft_tiktok_export.mp4")

FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

f_hud = ImageFont.truetype(FONT_BOLD, 24)
f_tag = ImageFont.truetype(FONT_BOLD, 24)
f_head = ImageFont.truetype(FONT_BOLD, 52)
f_subhead = ImageFont.truetype(FONT_BOLD, 36)
f_card_num = ImageFont.truetype(FONT_BOLD, 32)
f_card_txt = ImageFont.truetype(FONT_BOLD, 29)
f_card_sub = ImageFont.truetype(FONT_REG, 23)
f_chip = ImageFont.truetype(FONT_BOLD, 25)
f_chip_sm = ImageFont.truetype(FONT_BOLD, 22)
f_cta = ImageFont.truetype(FONT_BOLD, 42)
f_sub_white = ImageFont.truetype(FONT_BOLD, 35)
f_sub_yellow = ImageFont.truetype(FONT_BOLD, 37)

CATALOG_PATH = "/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-018_GA7-220501096-AA3-EV02_Modulos_Probados_Historias_Usuario/capturas_pruebas/02_hu02_pizzas_catalogo_filtros.png"
resample_filter = getattr(getattr(Image, 'Resampling', Image), 'LANCZOS', Image.ANTIALIAS)
catalog_img = Image.open(CATALOG_PATH).convert("RGBA").resize((740, 350), resample_filter) if os.path.exists(CATALOG_PATH) else None


def draw_rounded_card(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


# 1. Synthesize & Mix Audio with User's Voice Track
def build_audio():
    print("--- [PITCH] 1. Procesando locución oficial de Karen Campo y mezclando banda sonora... ---")
    if not os.path.exists(USER_VOICE_WAV) or os.path.getsize(USER_VOICE_WAV) < 100000:
        print("Extrayendo pista de voz de Karen Campo desde audio_tiktok.mp4...")
        cmd_extract = [
            "docker", "run", "--rm",
            "-v", "/home/danilo/Escritorio/Karen/SENA/CDE/base_conocimiento:/data",
            "-v", f"{TMP_DIR}:/tmp_dir",
            "sena-ffmpeg:alpine",
            "-y", "-i", "/data/audio_tiktok.mp4",
            "-ar", "44100", "-ac", "2",
            "/tmp_dir/user_voice_44k.wav"
        ]
        subprocess.run(cmd_extract, check=True)

    with wave.open(USER_VOICE_WAV, 'rb') as w:
        n_fr = w.getnframes()
        sr = w.getframerate()
        ch = w.getnchannels()
        raw = w.readframes(n_fr)
        data = struct.unpack(f"<{n_fr * ch}h", raw)

    voice_samples = [data[i] / 32768.0 for i in range(0, len(data), ch)]
    total_samples = len(voice_samples)

    # Peak normalize Karen's voice to 0.88 for crisp headroom & high intelligibility
    max_v = max(abs(x) for x in voice_samples)
    gain_v = 0.88 / max(max_v, 0.001)
    norm_voice = [x * gain_v for x in voice_samples]

    # Voice activity detection (50ms moving RMS window)
    win_sz = int(sr * 0.05)
    speech_mask = [0.0] * total_samples
    win_energy = sum(norm_voice[k] * norm_voice[k] for k in range(min(win_sz, total_samples)))
    for i in range(total_samples):
        if i >= win_sz:
            win_energy += norm_voice[i]*norm_voice[i] - norm_voice[i - win_sz]*norm_voice[i - win_sz]
        rms = math.sqrt(max(0.0, win_energy / win_sz))
        if rms > 0.025:
            speech_mask[i] = 1.0

    # Smooth ducking envelope: fast attack (20ms), gentle release (350ms)
    smooth_duck = [0.0] * total_samples
    curr = 0.0
    alpha_att = 1.0 / (0.02 * sr)
    alpha_rel = 1.0 / (0.35 * sr)
    for i in range(total_samples):
        tgt = speech_mask[i]
        if tgt > curr:
            curr = min(1.0, curr + alpha_att)
        else:
            curr = max(0.0, curr - alpha_rel)
        smooth_duck[i] = curr

    # Subtle Italian Gourmet Lo-Fi / Chillout Progression at 120 BPM
    # Am -> F -> C -> G
    chords = [
        ([110.0, 130.81, 164.81, 220.0], 55.0),    # Am
        ([87.31, 110.0, 130.81, 174.61], 43.65),   # F
        ([130.81, 164.81, 196.0, 261.63], 65.41),  # C
        ([98.0, 123.47, 146.83, 196.0], 49.0)      # G
    ]

    bpm = 120.0
    beat_len = 60.0 / bpm
    bar_len = beat_len * 4

    master_l = [0.0] * total_samples
    master_r = [0.0] * total_samples

    for i in range(total_samples):
        t = i / sr
        bar_num = int(t / bar_len)
        chord_notes, bass_freq = chords[bar_num % 4]
        pos_in_bar = (t % bar_len) / bar_len
        beat_idx = int(pos_in_bar * 4)

        kick = 0.0
        if beat_idx in [0, 2]:
            dt_k = t % beat_len
            if dt_k < 0.12:
                k_freq = 120.0 * math.exp(-40.0 * dt_k) + 42.0
                kick = math.sin(2 * math.pi * k_freq * dt_k) * math.exp(-22.0 * dt_k) * 0.35

        snare = 0.0
        if beat_idx in [1, 3]:
            dt_s = t % beat_len
            if dt_s < 0.15:
                noise = ((math.sin(i * 12.9898) * 43758.5453) % 1.0 - 0.5) * 2.0
                tone = math.sin(2 * math.pi * 175.0 * dt_s) * 0.25
                snare = (noise * 0.6 + tone * 0.4) * math.exp(-25.0 * dt_s) * 0.25

        dt_hh = t % (beat_len / 2.0)
        hihat = 0.0
        if dt_hh < 0.04:
            noise = ((math.sin(i * 37.1234) * 21953.1) % 1.0 - 0.5) * 2.0
            hihat = noise * math.exp(-90.0 * dt_hh) * 0.08

        dt_b = t % (beat_len / 2.0)
        bass = math.sin(2 * math.pi * bass_freq * t) * math.exp(-3.5 * dt_b) * 0.22
        bass += math.sin(2 * math.pi * bass_freq * 2.0 * t) * 0.06

        chord_val = 0.0
        for note in chord_notes:
            chord_val += math.sin(2 * math.pi * note * t) * 0.04
            chord_val += math.sin(2 * math.pi * (note * 2.0) * t) * 0.015
        chord_val *= (0.75 + 0.25 * math.sin(2 * math.pi * 2.5 * t))

        arp_sub = int((t % beat_len) / (beat_len / 4.0))
        arp_note = chord_notes[arp_sub % len(chord_notes)] * 2.0
        dt_arp = t % (beat_len / 4.0)
        arp = math.sin(2 * math.pi * arp_note * t) * math.exp(-28.0 * dt_arp) * 0.06

        music_l = (kick + snare * 0.85 + hihat * 0.7 + bass + chord_val * 0.9 + arp * 0.6) * 0.28
        music_r = (kick + snare * 0.85 + hihat * 1.1 + bass + chord_val * 1.1 + arp * 0.9) * 0.28

        # Dynamic ducking (music drops by 80% when Karen speaks, leaving her voice 100% prominent)
        duck_factor = 1.0 - (smooth_duck[i] * 0.80)
        fade_in = min(1.0, t / 0.3)
        fade_out = 1.0
        if t > (TOTAL_DURATION - 2.0):
            fade_out = max(0.0, (TOTAL_DURATION - t) / 2.0)

        bgm_l = music_l * duck_factor * fade_in * fade_out
        bgm_r = music_r * duck_factor * fade_in * fade_out

        v = norm_voice[i]
        master_l[i] = v + bgm_l
        master_r[i] = v + bgm_r

    with wave.open(MASTER_AUDIO_WAV, 'w') as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(sr)
        out_bytes = bytearray()
        for i in range(total_samples):
            sl = int(max(-32767, min(32767, master_l[i] * 32000)))
            sr_val = int(max(-32767, min(32767, master_r[i] * 32000)))
            out_bytes.extend(struct.pack('<hh', sl, sr_val))
        w.writeframes(out_bytes)

    print(f"Banda sonora master guardada: {MASTER_AUDIO_WAV}")


# 2. Dynamic Caption Resolver (matched precisely to Karen's spoken cadence)
def get_caption(t):
    if t < 2.5:
        return ("¿Cansado de pedir ", "PIZZA EN POPAYÁN", "?")
    elif t < 5.0:
        return ("...y que llegue ", "FRÍA O GRASOSA", "?")
    elif t < 7.5:
        return ("¿O con una ", "MASA SÚPER PESADA", "?")
    elif t < 11.0:
        return ("¡Llegó ", "BELLA ITALIA POPAYÁN", "!")
    elif t < 15.0:
        return ("Masa madre con ", "48H DE FERMENTACIÓN", "")
    elif t < 18.5:
        return ("¡Horneada a 450°C en ", "SOLO 90 SEGUNDOS", "!")
    elif t < 22.0:
        return ("Quesos frescos de ", "SILVIA, CAUCA", "")
    elif t < 25.5:
        return ("Hortalizas orgánicas ", "DE NUESTRA TIERRA", "")
    elif t < 29.0:
        return ("¡Textura crocante y ", "DIGESTIÓN LIGERA", "!")
    elif t < 32.5:
        return ("Web App desarrollada en ", "SENA ADSO", "")
    elif t < 36.0:
        return ("Pide en segundos con ", "TRACKING EN VIVO", "")
    elif t < 39.5:
        return ("Llega a más de 70°C en ", "< 30 MINUTOS", "")
    elif t < 43.5:
        return ("Visítanos en el ", "CENTRO HISTÓRICO", "")
    elif t < 47.5:
        return ("¡Pide ahora al ", "WHATSAPP OFICIAL", "!")
    else:
        return ("¡Pasión italiana con ", "CORAZÓN CAUCANO", "!")


def draw_gourmet_crest(draw, cx, cy, rad):
    draw.ellipse([cx - rad, cy - rad, cx + rad, cy + rad], fill=(22, 27, 34), outline=(245, 158, 11), width=4)
    draw.ellipse([cx - rad + 12, cy - rad + 12, cx + rad - 12, cy + rad - 12], outline=(245, 158, 11, 120), width=1)
    
    # Italian ribbon
    rib_w = 40
    draw.rectangle([cx - rib_w, cy - 65, cx - rib_w/3, cy - 55], fill=(0, 140, 69))
    draw.rectangle([cx - rib_w/3, cy - 65, cx + rib_w/3, cy - 55], fill=(255, 255, 255))
    draw.rectangle([cx + rib_w/3, cy - 65, cx + rib_w, cy - 55], fill=(205, 33, 42))

    f_crest_b = ImageFont.truetype(FONT_BOLD, 28)
    f_crest_sub = ImageFont.truetype(FONT_BOLD, 18)
    f_crest_yr = ImageFont.truetype(FONT_BOLD, 15)

    draw.text((cx - 86, cy - 35), "BELLA ITALIA", font=f_crest_b, fill=(245, 158, 11))
    draw.text((cx - 70, cy + 5), "PIZZA GOURMET", font=f_crest_sub, fill=(255, 255, 255))
    draw.text((cx - 78, cy + 32), "POPAYÁN • CAUCA", font=f_crest_yr, fill=(148, 163, 184))
    draw.text((cx - 45, cy + 56), "DESDE 2026", font=f_crest_yr, fill=(245, 158, 11))


# 3. Render Single Frame
def render_frame(frame_idx):
    t = frame_idx / FPS
    
    # 100% Solid matte dark background - Clean, sophisticated, ZERO white fog!
    im = Image.new("RGB", (W, H), (13, 17, 23))
    draw = ImageDraw.Draw(im)

    # Top progress bar
    prog_w = int((t / TOTAL_DURATION) * W)
    draw.rectangle([0, 0, W, 8], fill=(30, 41, 59))
    draw.rectangle([0, 0, prog_w, 8], fill=(245, 158, 11))

    # Top Header HUD
    draw_rounded_card(draw, [100, 24, 520, 74], 16, (22, 27, 34), (48, 54, 61), 1)
    draw.text((125, 36), "SENA | ADSO - FICHA 3186681", font=f_hud, fill=(226, 232, 240))

    time_str = f"{int(t):02d}:{int((t % 1)*10):01d} / 52s"
    draw_rounded_card(draw, [760, 24, 980, 74], 16, (22, 27, 34), (245, 158, 11), 1)
    draw.ellipse([780, 43, 792, 55], fill=(239, 68, 68))
    draw.text((805, 36), time_str, font=f_hud, fill=(248, 250, 252))

    BOX_L = 100
    BOX_R = 980

    if t < 7.5:
        # SCENE 1: EL PROBLEMA
        draw_rounded_card(draw, [BOX_L, 125, BOX_L + 340, 181], 16, (38, 20, 20), (220, 38, 38), 1)
        draw.text((BOX_L + 25, 139), "PASO 1 • EL PROBLEMA", font=f_tag, fill=(254, 202, 202))

        draw.text((BOX_L, 215), "¿PIZZAS FRÍAS Y", font=f_head, fill=(255, 255, 255))
        draw.text((BOX_L, 280), "MASA PESADA EN POPAYÁN?", font=f_head, fill=(248, 113, 113))

        draw_rounded_card(draw, [BOX_L, 380, BOX_R, 860], 24, (22, 27, 34), (48, 54, 61), 1)

        items = [
            ("01", "Demoras excesivas (> 60 min)", "Llegan frías y arruinan tu cena en familia"),
            ("02", "Masas pesadas sin fermentar", "Levaduras químicas causan acidez y digestión pesada"),
            ("03", "Ingredientes de baja calidad", "Grasa vegetal e insumos industriales sin frescura")
        ]
        y_c = 425
        for num, title, desc in items:
            draw_rounded_card(draw, [BOX_L + 35, y_c, BOX_L + 95, y_c + 54], 14, (38, 20, 20), (220, 38, 38), 1)
            draw.text((BOX_L + 48, y_c + 9), num, font=f_card_num, fill=(254, 202, 202))
            draw.text((BOX_L + 120, y_c + 3), title, font=f_card_txt, fill=(255, 255, 255))
            draw.text((BOX_L + 120, y_c + 45), desc, font=f_card_sub, fill=(148, 163, 184))
            y_c += 140

        draw_rounded_card(draw, [BOX_L, 900, BOX_R, 1050], 20, (18, 22, 30), (220, 38, 38), 1)
        draw.text((BOX_L + 35, 930), "72% de clientes en Popayán", font=f_subhead, fill=(248, 113, 113))
        draw.text((BOX_L + 35, 985), "insatisfechos con los tiempos y calidad de las pizzerías actuales.", font=f_card_sub, fill=(226, 232, 240))

    elif t < 18.5:
        # SCENE 2: LA SOLUCIÓN
        draw_rounded_card(draw, [BOX_L, 125, BOX_L + 370, 181], 16, (38, 30, 15), (245, 158, 11), 1)
        draw.text((BOX_L + 25, 139), "PASO 2 • SOLUCIÓN GOURMET", font=f_tag, fill=(253, 224, 71))

        draw.text((BOX_L, 215), "BELLA ITALIA POPAYÁN", font=f_head, fill=(255, 255, 255))
        draw.text((BOX_L, 280), "LA AUTÉNTICA PIZZA ARTESANAL", font=f_head, fill=(245, 158, 11))

        draw_rounded_card(draw, [BOX_L, 380, BOX_R, 860], 24, (22, 27, 34), (48, 54, 61), 1)
        draw_gourmet_crest(draw, BOX_L + 160, 620, 120)

        bx = BOX_L + 330
        draw.text((bx, 440), "ESTILO NAPOLITANO", font=f_subhead, fill=(255, 255, 255))
        draw.text((bx, 500), "• Masa madre viva de 48 horas", font=f_card_txt, fill=(253, 224, 71))
        draw.text((bx, 560), "• Horno a 450°C en piedra volcánica", font=f_card_txt, fill=(255, 255, 255))
        draw.text((bx, 620), "• Horneada en solo 90 segundos", font=f_card_txt, fill=(52, 211, 153))
        draw.text((bx, 680), "• Digestión 100% ligera garantizada", font=f_card_txt, fill=(226, 232, 240))
        draw.text((bx, 745), "Cero levaduras químicas industriales", font=f_card_sub, fill=(148, 163, 184))

        chips = ["Masa Madre 48h", "Horno 450°C", "Lista en 90s"]
        xc = BOX_L
        chip_w = int((BOX_R - BOX_L - 30) / 3)
        for ch in chips:
            draw_rounded_card(draw, [xc, 900, xc + chip_w, 970], 16, (18, 22, 30), (245, 158, 11), 1)
            cw = draw.textlength(ch, font=f_chip)
            draw.text((xc + (chip_w - cw)/2, 922), ch, font=f_chip, fill=(253, 224, 71))
            xc += chip_w + 15

    elif t < 29.0:
        # SCENE 3: CORAZÓN CAUCANO
        draw_rounded_card(draw, [BOX_L, 125, BOX_L + 370, 181], 16, (15, 35, 25), (16, 185, 129), 1)
        draw.text((BOX_L + 25, 139), "PASO 3 • IDENTIDAD CAUCANA", font=f_tag, fill=(167, 243, 208))

        draw.text((BOX_L, 215), "TÉCNICA ITALIANA CON", font=f_head, fill=(255, 255, 255))
        draw.text((BOX_L, 280), "CORAZÓN CAUCANO", font=f_head, fill=(52, 211, 153))

        draw_rounded_card(draw, [BOX_L, 380, BOX_R, 860], 24, (22, 27, 34), (48, 54, 61), 1)

        cauca_items = [
            ("01", "Quesos de Silvia, Cauca", "Fior di latte artesanal de productores lecheros locales"),
            ("02", "Huertas Orgánicas del Cauca", "Albahaca fresca y pomodoro campesino sin agroquímicos"),
            ("03", "Empaques 100% Ecológicos", "Elaborados con fibra de caña de azúcar biodegradable")
        ]
        y_c = 425
        for num, title, desc in cauca_items:
            draw_rounded_card(draw, [BOX_L + 35, y_c, BOX_L + 95, y_c + 54], 14, (15, 35, 25), (16, 185, 129), 1)
            draw.text((BOX_L + 48, y_c + 9), num, font=f_card_num, fill=(167, 243, 208))
            draw.text((BOX_L + 120, y_c + 3), title, font=f_card_txt, fill=(255, 255, 255))
            draw.text((BOX_L + 120, y_c + 45), desc, font=f_card_sub, fill=(148, 163, 184))
            y_c += 140

        draw_rounded_card(draw, [BOX_L, 900, BOX_R, 980], 18, (18, 22, 30), (16, 185, 129), 1)
        banner_txt = "Alianza y comercio justo directo con familias campesinas del Cauca"
        bw = draw.textlength(banner_txt, font=f_chip_sm)
        draw.text((BOX_L + (BOX_R - BOX_L - bw)/2, 928), banner_txt, font=f_chip_sm, fill=(167, 243, 208))

    elif t < 39.5:
        # SCENE 4: TECNOLOGÍA ADSO
        draw_rounded_card(draw, [BOX_L, 125, BOX_L + 360, 181], 16, (20, 30, 48), (59, 130, 246), 1)
        draw.text((BOX_L + 25, 139), "PASO 4 • INNOVACIÓN ADSO", font=f_tag, fill=(191, 219, 254))

        draw.text((BOX_L, 215), "WEB APP SENA ADSO +", font=f_head, fill=(255, 255, 255))
        draw.text((BOX_L, 280), "DELIVERY TÉRMICO GARANTIZADO", font=f_head, fill=(96, 165, 250))

        draw_rounded_card(draw, [BOX_L, 380, BOX_R, 860], 24, (22, 27, 34), (48, 54, 61), 1)
        if catalog_img:
            img_x = BOX_L + int((BOX_R - BOX_L - 740) / 2)
            im.paste(catalog_img, (img_x, 415))
        
        caption_txt = "Plataforma web desarrollada en formación ADSO • Ficha 3186681"
        cap_w = draw.textlength(caption_txt, font=f_card_sub)
        draw.text((BOX_L + (BOX_R - BOX_L - cap_w)/2, 795), caption_txt, font=f_card_sub, fill=(191, 219, 254))

        tech_chips = ["Pide en 3 clics", "Baúl térmico > 70°C", "Entrega < 30 min"]
        xc = BOX_L
        chip_w = int((BOX_R - BOX_L - 30) / 3)
        for ch in tech_chips:
            draw_rounded_card(draw, [xc, 900, xc + chip_w, 970], 16, (18, 22, 30), (59, 130, 246), 1)
            cw = draw.textlength(ch, font=f_chip)
            draw.text((xc + (chip_w - cw)/2, 922), ch, font=f_chip, fill=(191, 219, 254))
            xc += chip_w + 15

    else:
        # SCENE 5: CALL TO ACTION
        draw_rounded_card(draw, [BOX_L, 125, BOX_L + 380, 181], 16, (38, 30, 15), (245, 158, 11), 1)
        draw.text((BOX_L + 25, 139), "PASO 5 • LLAMADO A LA ACCIÓN", font=f_tag, fill=(253, 224, 71))

        draw.text((BOX_L, 215), "¡VIVE LA EXPERIENCIA", font=f_head, fill=(255, 255, 255))
        draw.text((BOX_L, 280), "BELLA ITALIA HOY!", font=f_head, fill=(245, 158, 11))

        # CTA Button
        draw_rounded_card(draw, [BOX_L, 380, BOX_R, 495], 24, (245, 158, 11), (255, 255, 255), 2)
        cta_txt = "HAZ TU PEDIDO POR WHATSAPP"
        cw = draw.textlength(cta_txt, font=f_cta)
        draw.text((BOX_L + (BOX_R - BOX_L - cw)/2, 418), cta_txt, font=f_cta, fill=(15, 23, 42))

        # Contact Card
        draw_rounded_card(draw, [BOX_L, 535, BOX_R, 960], 24, (22, 27, 34), (48, 54, 61), 1)

        contacts = [
            ("SEDE PRESENCIAL", "Calle 4ta No. 3-45 • Centro Histórico, Popayán"),
            ("WHATSAPP OFICIAL", "(+57) 312 890 4521 • Pedidos en vivo"),
            ("REGISTRO COMERCIAL", "Cámara de Comercio Popayán • RUES Aprobado"),
            ("APRENDIZ AUTORA", "Karen Yuliana Campo • Tecnóloga ADSO Ficha 3186681")
        ]
        y_c = 565
        for label, val in contacts:
            draw.text((BOX_L + 40, y_c), label, font=f_chip, fill=(245, 158, 11))
            draw.text((BOX_L + 40, y_c + 38), val, font=f_card_txt, fill=(255, 255, 255))
            y_c += 92

    # TikTok Subtitle Bar (Y: 1360..1470) - Clean pill, centered, active-word highlight
    pfx, highlight, sfx = get_caption(t)
    draw_rounded_card(draw, [BOX_L, 1360, BOX_R, 1470], 22, (22, 27, 34), (245, 158, 11), 2)
    
    pfx_w = draw.textlength(pfx, font=f_sub_white)
    hl_w = draw.textlength(highlight, font=f_sub_yellow)
    sfx_w = draw.textlength(sfx, font=f_sub_white)
    total_w = pfx_w + hl_w + sfx_w
    
    start_x = int(BOX_L + ((BOX_R - BOX_L) - total_w) / 2)
    if start_x < BOX_L + 25:
        start_x = BOX_L + 25
        
    y_sub = 1395
    draw.text((start_x, y_sub), pfx, font=f_sub_white, fill=(255, 255, 255))
    draw.text((start_x + pfx_w, y_sub - 1), highlight, font=f_sub_yellow, fill=(253, 224, 71))
    if sfx:
        draw.text((start_x + pfx_w + hl_w, y_sub), sfx, font=f_sub_white, fill=(255, 255, 255))

    return im


def main():
    print("=================================================================")
    print("  GENERADOR DE VIDEO PITCH BELLA ITALIA - FILMCRAFT CLI TIKTOK   ")
    print("  Evidencia: GA10-240201529-AA2-EV01 | Aprendiz: Karen Campo     ")
    print("=================================================================")

    build_audio()

    print("--- [PITCH] 2. Renderizando flujo visual premium minimalista (1080x1920, 30fps)... ---")
    raw_video_cmd = [
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
        # Convert to RGB bytes (3 bytes per pixel for rgb24)
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
        f.write(json.dumps({"id": "file.newProject", "params": {"name": "PizzeriaBellaItaliaPitch"}}) + "\n")
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
        f.write(json.dumps({"id": "file.import", "params": {"paths": [VISUAL_STREAM_MP4, MASTER_AUDIO_WAV]}}) + "\n")
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
        f.write(json.dumps({"id": "file.saveAs", "params": {"path": FILMCRAFT_PROJ}}) + "\n")

    print("Ejecutando ensamble de timeline en FilmCraft CLI...")
    res = subprocess.run(["filmcraft-cli", "run", script_jsonl], capture_output=True, text=True)
    if res.returncode != 0:
        print("Error en FilmCraft CLI assembly:\n", res.stderr, res.stdout)
        sys.exit(1)
    print("Timeline ensamblado exitosamente en FilmCraft:")
    print(res.stdout)

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

    print("--- [PITCH] 4. Distribuyendo video final MP4 a todas las carpetas... ---")
    shutil.copy2(FILMCRAFT_EXPORT_MP4, FINAL_MP4)

    zajuna_dir = "/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA10-240201529-AA2-EV01"
    zajuna_video_dir = os.path.join(zajuna_dir, "video")
    os.makedirs(zajuna_video_dir, exist_ok=True)
    shutil.copy2(FINAL_MP4, os.path.join(zajuna_video_dir, "GA10-240201529-AA2-EV01_Pitch_Idea_Negocio.mp4"))
    shutil.copy2(FINAL_MP4, os.path.join(zajuna_dir, "GA10-240201529-AA2-EV01_Pitch_Idea_Negocio.mp4"))

    sitio_video_dir = os.path.join(BASE_DIR, "sitio_pitch_web", "video")
    os.makedirs(sitio_video_dir, exist_ok=True)
    shutil.copy2(FINAL_MP4, os.path.join(sitio_video_dir, "pitch_bella_italia.mp4"))

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
