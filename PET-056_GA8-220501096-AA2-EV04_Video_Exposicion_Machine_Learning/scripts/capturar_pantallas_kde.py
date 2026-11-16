#!/usr/bin/env python3
"""
Script de Automatización de Capturas de Pantalla en KDE Plasma X11
Evidencia: GA8-220501096-AA2-EV04 - Video exposición sobre machine learning
Aprendiz: Karen Yuliana Campo - SENA ADSO Ficha 3186681
"""

import os
import sys
import time
import shutil
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
CAPTURAS_DIR = os.path.join(BASE_DIR, "capturas")
SITIO_CAPTURAS_DIR = os.path.join(BASE_DIR, "sitio_ml_web", "capturas")
ZAJUNA_CAPTURAS_DIR = "/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA8-220501096-AA2-EV04/capturas"
BRAIN_DIR = "/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603"

os.makedirs(CAPTURAS_DIR, exist_ok=True)
os.makedirs(SITIO_CAPTURAS_DIR, exist_ok=True)
os.makedirs(ZAJUNA_CAPTURAS_DIR, exist_ok=True)
os.makedirs(BRAIN_DIR, exist_ok=True)

def minimize_code():
    subprocess.run("for w in $(xdotool search --class code 2>/dev/null); do xdotool windowminimize $w 2>/dev/null; done", shell=True)
    time.sleep(0.5)

def capture_window(wid, out_path):
    subprocess.run(["xdotool", "windowactivate", "--sync", wid])
    time.sleep(0.6)
    subprocess.run(["import", "-window", wid, out_path], check=True)
    print(f"[OK] Captura guardada: {out_path}")
    fname = os.path.basename(out_path)
    shutil.copy(out_path, os.path.join(SITIO_CAPTURAS_DIR, fname))
    shutil.copy(out_path, os.path.join(ZAJUNA_CAPTURAS_DIR, fname))
    shutil.copy(out_path, os.path.join(BRAIN_DIR, fname))

def run_konsole_capture(title, cmd_str, out_filename):
    minimize_code()
    out_path = os.path.join(CAPTURAS_DIR, out_filename)
    script_content = f"""
    printf '\\033]0;%s\\007' '{title}'
    {cmd_str}
    sleep 8
    """
    p = subprocess.Popen([
        "konsole",
        "--geometry", "1250x780+80+60",
        "-e", "bash", "-c", script_content
    ])
    time.sleep(2.0)
    
    res = subprocess.run(["xdotool", "search", "--class", "konsole"], capture_output=True, text=True)
    wids = res.stdout.strip().split()
    if wids:
        capture_window(wids[-1], out_path)
    else:
        print("[ERROR] No se encontró ventana de Konsole")
    p.terminate()
    time.sleep(0.5)

def run_chrome_capture(url, js_eval, out_filename):
    minimize_code()
    out_path = os.path.join(CAPTURAS_DIR, out_filename)
    profile_dir = "/tmp/chrome_ml_profile"
    os.makedirs(profile_dir, exist_ok=True)
    
    p = subprocess.Popen([
        "google-chrome",
        f"--user-data-dir={profile_dir}",
        "--window-size=1380,940",
        "--window-position=60,40",
        "--no-first-run",
        "--no-default-browser-check",
        url
    ])
    time.sleep(3.5)
    
    res = subprocess.run(["xdotool", "search", "--class", "google-chrome"], capture_output=True, text=True)
    wids = res.stdout.strip().split()
    if wids:
        wid = wids[-1]
        subprocess.run(["xdotool", "windowactivate", "--sync", wid])
        time.sleep(0.5)
        
        if js_eval:
            subprocess.run(["xdotool", "key", "ctrl+shift+j"])
            time.sleep(1.0)
            subprocess.run(["xdotool", "type", js_eval])
            time.sleep(0.3)
            subprocess.run(["xdotool", "key", "Return"])
            time.sleep(0.5)
            subprocess.run(["xdotool", "key", "ctrl+shift+j"])
            time.sleep(1.0)
            
        capture_window(wid, out_path)
    else:
        print("[ERROR] No se encontró ventana de Chrome")
    p.terminate()
    time.sleep(1.0)

def main():
    print("=== INICIANDO CAPTURA DE PANTALLAS EN KDE PLASMA X11 (GA8-220501096-AA2-EV04) ===")
    
    # 1. Konsole Docker Despliegue
    cmd_1 = """
    cd /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-056_GA8-220501096-AA2-EV04_Video_Exposicion_Machine_Learning/docker_ml_web
    echo '========================================================================'
    echo '  EVIDENCIA GA8-220501096-AA2-EV04: VIDEO EXPOSICIÓN SOBRE MACHINE LEARNING'
    echo '  ESTADO DE CONTENEDOR DOCKER Y ARCHIVOS DE ENTREGA - PUERTO 8104'
    echo '========================================================================'
    docker compose ps
    echo ''
    echo '--- VIDEO EXPOSITIVO GENERADO (5.81 min / MP4 1080p 16:9) ---'
    ls -lh ../video/GA8-220501096-AA2-EV04_Video_Exposicion_Machine_Learning.mp4
    echo ''
    echo '--- GUION TÉCNICO INDIVIDUAL Y ARTEFACTOS ---'
    ls -lh ../docs/
    """
    run_konsole_capture("SENA ADSO - Despliegue Docker Machine Learning", cmd_1, "paso_01_despliegue_docker_ml_konsole.png")
    
    # 2. Konsole Verificación de Salud
    cmd_2 = """
    echo '========================================================================'
    echo '  VERIFICACIÓN DE SALUD HTTP Y STREAMING DE VIDEO ML (PUERTO 8104)'
    echo '========================================================================'
    curl -I http://localhost:8104/
    echo ''
    echo '--- VERIFICACIÓN STREAMING VIDEO EXPOSICIÓN MP4 ---'
    curl -I http://localhost:8104/video/video_exposicion_ml.mp4
    echo ''
    echo '--- CONSULTA DATASET ESTRUCTURADO JSON (8 NÚCLEOS) ---'
    curl -s http://localhost:8104/datos_exposicion_ml.json | head -n 25
    """
    run_konsole_capture("SENA ADSO - Verificación de Salud HTTP y Dataset", cmd_2, "paso_02_verificacion_salud_servicios_ml_konsole.png")
    
    # 3. Chrome Portal Web con Reproductor de Video
    js_v = "document.getElementById('mlVideo').currentTime = 15; document.getElementById('mlVideo').pause();"
    run_chrome_capture("http://localhost:8104/", js_v, "paso_03_chrome_portal_ml_video_reproductor.png")
    
    # 4. Chrome Diapositivas Interactivas (Modelo Conexionista)
    js_slide = "openTab('tab-slides'); setSlideIndex(6);"
    run_chrome_capture("http://localhost:8104/", js_slide, "paso_04_chrome_diapositiva_modelos_ia_conexionista.png")
    
    # 5. Chrome Guion Técnico Completo
    js_guion = "openTab('tab-guion');"
    run_chrome_capture("http://localhost:8104/", js_guion, "paso_05_chrome_guion_tecnico_completo.png")
    
    # 6. Chrome Dataset y Consecuencias Éticas
    js_data = "openTab('tab-dataset');"
    run_chrome_capture("http://localhost:8104/", js_data, "paso_06_chrome_dataset_consecuencias_eticas.png")

    print("=== TODAS LAS CAPTURAS DE PANTALLA EN KDE FUERON COMPLETADAS EXITOSAMENTE ===")

if __name__ == "__main__":
    main()
