#!/usr/bin/env python3
# ==============================================================================
# GENERADOR MAESTRO DEL VIDEO TUTORIAL Y PLAN DE CAPACITACIÓN (FULL HD 1080P)
# Evidencia: GA10-220501097-AA12-EV01 - Elabora plan de capacitación y UAT
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | SENA Regional Cauca - CTPI Popayán
#
# Combina:
# - Voz original de Karen Yuliana Campo (audio_capacitacion.mp4)
# - Voces nítidas y vocalizadas para los participantes (Chef Mario, Carlos, Andrea, Don Giuseppe, Juan)
# - 8 Diapositivas Full HD (1920x1080) con capturas reales del software "Bella Italia Popayán"
# - Música de piano ambiental suave con ducking profundo (-30 dB bajo voz)
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
CAPTURAS_DIR = os.path.join(BASE_DIR, 'capturas')
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
ENTREGA_DIR = '/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA10-220501097-AA12-EV01'
ARTIFACT_DIR = '/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603'
BUILD_DIR = '/tmp/video_cap_build'

os.makedirs(VIDEO_DIR, exist_ok=True)
os.makedirs(ENTREGA_DIR, exist_ok=True)
os.makedirs(BUILD_DIR, exist_ok=True)
os.makedirs(os.path.join(BUILD_DIR, 'slides'), exist_ok=True)

# Tipografías del sistema
FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

def get_font(bold=False, size=24):
    path = FONT_BOLD if bold else FONT_REG
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

# Colores institucionales
COLOR_BG_DARK = (15, 23, 42)       # Slate 900
COLOR_PANEL_BG = (248, 250, 252)   # Slate 50
COLOR_SENA_GREEN = (0, 140, 69)    # Verde SENA
COLOR_ACCENT_BLUE = (14, 165, 233) # Sky 500
COLOR_TEXT_DARK = (30, 41, 59)     # Slate 800
COLOR_TEXT_MUTED = (100, 116, 139) # Slate 500

SLIDES_CONFIG = [
    {
        "id": "slide_01",
        "duration": 38.9,
        "badge": "SESIÓN DE CAPACITACIÓN & TUTORIAL",
        "title": "SISTEMA DE GESTIÓN GASTRONÓMICA 'BELLA ITALIA'",
        "subtitle": "Capacitación Operativa en Salón Comercial (POS) y Cocina a Leña (KDS)",
        "bullets": [
            "• Bienvenida formal al equipo de trabajo de Pizzería Bella Italia Popayán.",
            "• Transición digital integral: erradicación definitiva de comandas de papel.",
            "• Exactitud matemática en cobros, control de inventarios y facturación fiscal.",
            "• Facilitadora: Karen Yuliana Campo — Analista y Desarrolladora ADSO."
        ],
        "image": "paso_02_navegador_chrome_landing_page.png",
        "caption": "Plataforma de Producción — Pizzería Gourmet Bella Italia Popayán"
    },
    {
        "id": "slide_02",
        "duration": 40.6,
        "badge": "DISEÑO INSTRUCCIONAL (45 MINUTOS)",
        "title": "CRONOGRAMA Y METODOLOGÍA DEL TALLER",
        "subtitle": "Estructura Pedagógica de 4 Bloques — Modelo Vivencial 'Aprender Haciendo'",
        "bullets": [
            "• Bloque I (00-05 min): Encuadre, motivación y entrega de Guías Rápidas.",
            "• Bloque II (05-20 min): Proyección de Video Tutorial y demostración funcional.",
            "• Bloque III (20-35 min): Taller práctico Hands-On con simulación de roles cruzados.",
            "• Bloque IV (35-45 min): Pruebas UAT, resolución de dudas FAQ y firma de acta."
        ],
        "image": "paso_05_chrome_manual_usuario_flujos_operativos.png",
        "caption": "Diagrama de Flujos Operativos y Transaccionales del Sistema"
    },
    {
        "id": "slide_03",
        "duration": 26.3,
        "badge": "MÓDULO 1: CONTROL DE ACCESO (RBAC)",
        "title": "LOGIN TÁCTIL CON PIN DE 4 DÍGITOS",
        "subtitle": "Seguridad, Identificación de Operadores y Apertura de Turnos",
        "bullets": [
            "• Autenticación individual por código PIN numérico de 4 dígitos.",
            "• Redirección automática según perfil: Cajero abre POS, Chef abre KDS.",
            "• Apertura formal de turno registrando fecha, hora y base inicial de caja.",
            "• Seguridad robusta con tokens JWT y encriptación bcrypt en servidor local."
        ],
        "image": "paso_04_chrome_manual_usuario_portada_roles.png",
        "caption": "Interfaz de Autenticación por Roles — Cajero, Cocina y Administración"
    },
    {
        "id": "slide_04",
        "duration": 25.4,
        "badge": "MÓDULO 2: PUNTO DE VENTA (POS)",
        "title": "CAPTURA DE PEDIDOS Y RECETAS CAUCANAS",
        "subtitle": "Selección de Mesas, Fotografía HD y Modificadores de Receta",
        "bullets": [
            "• Mapa visual de mesas del salón comercial con estados interactivos en tiempo real.",
            "• Carta gastronómica interactiva con ingredientes autóctonos caucanos de alta gama.",
            "• Modificadores ágiles: Masa madre 48h, Pipián payanés y quesos de Silvia.",
            "• Botón 'Enviar a Cocina': transmisión instantánea vía WebSockets en < 1 segundo."
        ],
        "image": "paso_03_chrome_menu_gourmet_interactivo.png",
        "caption": "Terminal POS de Salón — Menú Digital Interactivo y Modificadores"
    },
    {
        "id": "slide_05",
        "duration": 32.4,
        "badge": "MÓDULO 3: PANTALLA DE COCINA (KDS)",
        "title": "GESTIÓN DE COMANDAS Y HORNO A LEÑA 400°C",
        "subtitle": "Semáforo Inteligente de Tiempos y Alertas Visuales Acústicas",
        "bullets": [
            "• Recepción instantánea de comandas con alerta sonora y semáforo cromático.",
            "• Control de cocción: Verde (0-10 min), Amarillo (10-15 min), Rojo (> 15 min).",
            "• Toques táctiles intuitivos: 'En Horno' y 'Listo para Despacho'.",
            "• Actualizaciones dinámicas en vivo ante cambios o anulaciones de platos."
        ],
        "image": "paso_06_chrome_manual_usuario_guias_paso_a_paso.png",
        "caption": "Sistema de Pantalla de Cocina (KDS) — Semáforo de Tiempo y Despacho"
    },
    {
        "id": "slide_06",
        "duration": 19.4,
        "badge": "MÓDULO 4: FACTURACIÓN DIAN & PAGOS",
        "title": "LIQUIDACIÓN ÁGIL Y TICKET TÉRMICO 80MM",
        "subtitle": "Soporte de Pagos Mixtos (Wompi + Efectivo) y Factura Fiscal con CUFE y QR",
        "bullets": [
            "• Cobro rápido con soporte de pagos combinados (Efectivo + Pasarela QR).",
            "• Cálculo automático y exacto de cambio, previniendo descuadres de turno.",
            "• Expedición de factura legal con código CUFE y código QR tributario DIAN.",
            "• Impresión térmica en 2 segundos y liberación inmediata de mesa a 'Disponible'."
        ],
        "image": "paso_04_chrome_formulario_checkout_pedido.png",
        "caption": "Módulo de Liquidación, Facturación Electrónica DIAN y Arqueo"
    },
    {
        "id": "slide_07",
        "duration": 12.0,
        "badge": "PRUEBAS DE ACEPTACIÓN DE USUARIO (UAT)",
        "title": "VERIFICACIÓN EMPÍRICA POR EL CLIENTE",
        "subtitle": "5 Casos de Prueba Críticos Ejecutados con 100% de Conformidad",
        "bullets": [
            "• UAT-01: Autenticación segura y control de roles RBAC — [APROBADO 100%]",
            "• UAT-02: Toma y personalización de pedidos en POS — [APROBADO 100%]",
            "• UAT-03: Notificación sonora y semáforo en monitor KDS — [APROBADO 100%]",
            "• UAT-04: Facturación electrónica DIAN y pagos mixtos — [APROBADO 100%]",
            "• UAT-05: Cuadre de caja y arqueo ciego sin descuadres — [APROBADO 100%]"
        ],
        "image": "paso_05_chrome_manual_usuario_flujos_operativos.png",
        "caption": "Matriz UAT de Aceptación — Verificada y Calificada Conforme por el Cliente"
    },
    {
        "id": "slide_08",
        "duration": 16.11,
        "badge": "CIERRE FORMAL & PASO A PRODUCCIÓN",
        "title": "ACTA DE ENTREGA A ENTERA SATISFACCIÓN",
        "subtitle": "Pizzería Gourmet Bella Italia Popayán • Fase de Implantación Culminada",
        "bullets": [
            "• Suscripción solemne del Acta de Conformidad por Don Giuseppe Rossi y Karen Campo.",
            "• Garantía técnica legal de 6 meses y disponibilidad SLA garantizada del 99.5%.",
            "• Mesa de ayuda y canal de soporte técnico continuo vía WhatsApp y servidor LAN.",
            "• SENA CTPI Popayán — Tecnólogo en Análisis y Desarrollo de Software (ADSO)."
        ],
        "image": "paso_02_navegador_chrome_landing_page.png",
        "caption": "Proyecto Aprobado Formalmente para Operación Productiva y Comercial"
    }
]

def render_slide(cfg, output_path):
    W, H = 1920, 1080
    im = Image.new('RGB', (W, H), COLOR_BG_DARK)
    draw = ImageDraw.Draw(im)

    # Header Institucional SENA
    draw.rectangle([(0, 0), (W, 75)], fill=(15, 23, 42))
    draw.rectangle([(0, 75), (W, 80)], fill=COLOR_SENA_GREEN)

    f_head_title = get_font(bold=True, size=24)
    f_head_meta = get_font(bold=False, size=19)
    draw.text((60, 24), "SERVICIO NACIONAL DE APRENDIZAJE • SENA CTPI POPAYÁN", fill=COLOR_SENA_GREEN, font=f_head_title)
    draw.text((W - 600, 26), "Tecnólogo ADSO | Ficha 3186681 | Regional Cauca", fill=(203, 213, 225), font=f_head_meta)

    # Panel Central Blanco/Claro
    panel_rect = [(60, 105), (W - 60, H - 75)]
    draw.rounded_rectangle(panel_rect, radius=16, fill=COLOR_PANEL_BG)

    # Badge Superior
    f_badge = get_font(bold=True, size=18)
    draw.rounded_rectangle([(95, 135), (95 + 440, 175)], radius=8, fill=COLOR_SENA_GREEN)
    draw.text((115, 143), cfg["badge"], fill=(255, 255, 255), font=f_badge)

    # Título y Subtítulo
    f_title = get_font(bold=True, size=38)
    f_sub = get_font(bold=False, size=22)
    draw.text((95, 195), cfg["title"], fill=COLOR_TEXT_DARK, font=f_title)
    draw.text((95, 245), cfg["subtitle"], fill=COLOR_TEXT_MUTED, font=f_sub)

    draw.line([(95, 285), (W - 95, 285)], fill=(226, 232, 240), width=2)

    # Lado Izquierdo: Viñetas informativas
    f_bullet = get_font(bold=False, size=23)
    f_bullet_bold = get_font(bold=True, size=23)
    y_text = 320
    for bullet in cfg["bullets"]:
        # Card para cada bullet
        draw.rounded_rectangle([(95, y_text - 6), (930, y_text + 58)], radius=10, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
        draw.text((115, y_text + 8), bullet, fill=COLOR_TEXT_DARK, font=f_bullet)
        y_text += 80

    # Lado Derecho: Imagen del Software con marco
    img_filename = cfg["image"]
    img_path = os.path.join(CAPTURAS_DIR, img_filename)
    if os.path.exists(img_path):
        try:
            soft_im = Image.open(img_path)
            # Escalar manteniendo proporción para caja de 830x550
            resample_filter = getattr(Image, 'Resampling', Image).LANCZOS if hasattr(Image, 'Resampling') else getattr(Image, 'ANTIALIAS', 1)
            soft_im.thumbnail((830, 560), resample_filter)
            iw, ih = soft_im.size
            ix = 980 + (830 - iw) // 2
            iy = 310 + (560 - ih) // 2

            # Marco exterior con sombra simulada
            draw.rounded_rectangle([(ix - 8, iy - 8), (ix + iw + 8, iy + ih + 8)], radius=12, fill=(255, 255, 255), outline=(203, 213, 225), width=2)
            im.paste(soft_im, (ix, iy))

            # Caption debajo de la imagen
            f_caption = get_font(bold=True, size=17)
            draw.text((ix + 10, iy + ih + 16), "📷 " + cfg["caption"], fill=COLOR_TEXT_MUTED, font=f_caption)
        except Exception as e:
            print(f"Error cargando imagen {img_path}: {e}")

    # Footer
    draw.rectangle([(0, H - 55), (W, H)], fill=(15, 23, 42))
    f_foot = get_font(bold=False, size=18)
    draw.text((60, H - 40), "Evidencia: GA10-220501097-AA12-EV01 | Plan de Capacitación y Pruebas UAT", fill=(148, 163, 184), font=f_foot)
    draw.text((W - 480, H - 40), "Aprendiz: Karen Yuliana Campo • Popayán 2026", fill=COLOR_SENA_GREEN, font=f_foot)

    im.save(output_path, "JPEG", quality=95)
    print(f"[OK] Slide generado: {output_path}")

def generate_ambient_music(output_wav_path, duration_seconds=215.0, sample_rate=48000):
    num_samples = int(duration_seconds * sample_rate)
    chords = [
        [261.63, 329.63, 392.00, 523.25], # C maj
        [220.00, 261.63, 329.63, 440.00], # A min
        [174.61, 220.00, 261.63, 349.23], # F maj
        [196.00, 246.94, 293.66, 392.00]  # G maj
    ]
    chord_duration = 4.0
    samples_per_chord = int(chord_duration * sample_rate)
    data = []

    for i in range(num_samples):
        chord_idx = (i // samples_per_chord) % len(chords)
        chord = chords[chord_idx]
        pos_in_chord = (i % samples_per_chord) / samples_per_chord
        env = math.sin(math.pi * pos_in_chord) ** 1.3

        sample_val = 0.0
        t = i / sample_rate
        for freq in chord:
            w1 = math.sin(2.0 * math.pi * freq * t)
            w2 = 0.4 * math.sin(4.0 * math.pi * freq * t)
            w3 = 0.15 * math.sin(6.0 * math.pi * freq * t)
            sample_val += (w1 + w2 + w3)
        sample_val = (sample_val / len(chord)) * env * 0.15
        val_int = int(max(min(sample_val, 1.0), -1.0) * 32767)
        data.append(struct.pack('<hh', val_int, val_int))

    with wave.open(output_wav_path, 'wb') as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(data))
    print(f"[OK] BGM Loop generado: {output_wav_path} ({duration_seconds:.1f}s)")

def main():
    print("=== INICIANDO PRODUCCIÓN DE VIDEO TUTORIAL (GA10-220501097-AA12-EV01) ===")
    print("Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | SENA Regional Cauca")

    # 1. Renderizar las 8 diapositivas Full HD
    slides_dir = os.path.join(BUILD_DIR, 'slides')
    for cfg in SLIDES_CONFIG:
        slide_out = os.path.join(slides_dir, f"{cfg['id']}.jpg")
        render_slide(cfg, slide_out)

    # 2. Generar BGM de fondo
    bgm_path = os.path.join(BUILD_DIR, 'bg_ambient_music.wav')
    generate_ambient_music(bgm_path, duration_seconds=215.0)

    # 3. Crear archivo concat para las diapositivas
    concat_txt_path = os.path.join(BUILD_DIR, 'slides_concat.txt')
    with open(concat_txt_path, 'w', encoding='utf-8') as f:
        for cfg in SLIDES_CONFIG:
            f.write(f"file '/build/slides/{cfg['id']}.jpg'\n")
            f.write(f"duration {cfg['duration']:.2f}\n")
        f.write(f"file '/build/slides/{SLIDES_CONFIG[-1]['id']}.jpg'\n")

    print(f"[OK] Concat script generado en: {concat_txt_path}")

    # 4. Renderizado Final Full HD con Docker FFmpeg
    output_mp4 = os.path.join(VIDEO_DIR, 'GA10-220501097-AA12-EV01_Video_Tutorial_Plan_Capacitacion.mp4')
    master_voice_path = '/tmp/audio_cap/master_build/master_voice.wav'

    print("Ejecutando renderizado de video Full HD 1080p con Docker FFmpeg...")
    docker_cmd = [
        "docker", "run", "--rm",
        "-v", f"{BUILD_DIR}:/build",
        "-v", f"{master_voice_path}:/audio/master_voice.wav:ro",
        "-v", f"{VIDEO_DIR}:/video_out",
        "jrottenberg/ffmpeg:6.1-alpine",
        "-y",
        "-f", "concat", "-safe", "0", "-i", "/build/slides_concat.txt",
        "-i", "/audio/master_voice.wav",
        "-i", "/build/bg_ambient_music.wav",
        "-t", "211.11",
        "-filter_complex",
        "[0:v]scale=1920:1080,fps=30[v_out];"
        "[1:a]volume=1.2,loudnorm=I=-16:TP=-1.5:LRA=11,asplit=2[voice_main][voice_sc];"
        "[2:a]volume=0.06[bgm_base];"
        "[bgm_base][voice_sc]sidechaincompress=threshold=0.035:ratio=14:attack=15:release=450[ducked_bgm];"
        "[voice_main][ducked_bgm]amix=inputs=2:duration=first:dropout_transition=2[a_out]",
        "-map", "[v_out]",
        "-map", "[a_out]",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "22",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "/video_out/GA10-220501097-AA12-EV01_Video_Tutorial_Plan_Capacitacion.mp4"
    ]

    subprocess.run(docker_cmd, check=True)

    sz_mb = os.path.getsize(output_mp4) / (1024 * 1024)
    print(f"[OK] Video Tutorial renderizado con éxito: {output_mp4} ({sz_mb:.2f} MB)")

    # 5. Distribución a carpeta Zajuna y Artifacts
    shutil.copy(output_mp4, ENTREGA_DIR)
    shutil.copy(output_mp4, ARTIFACT_DIR)
    print(f"[OK] Distribuido a Zajuna: {ENTREGA_DIR}")
    print(f"[OK] Distribuido a Artifacts: {ARTIFACT_DIR}")

if __name__ == '__main__':
    main()
