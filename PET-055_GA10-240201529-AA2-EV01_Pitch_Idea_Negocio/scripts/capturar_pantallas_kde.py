#!/usr/bin/env python3
"""
Script de Automatización de Capturas de Pantalla en KDE Plasma X11
Evidencia: GA10-240201529-AA2-EV01 - Pitch idea de negocio
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
ZAJUNA_CAPTURAS_DIR = "/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA10-240201529-AA2-EV01/capturas"
BRAIN_DIR = "/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603"

os.makedirs(CAPTURAS_DIR, exist_ok=True)
os.makedirs(ZAJUNA_CAPTURAS_DIR, exist_ok=True)

def minimize_code():
    subprocess.run("for w in $(xdotool search --class code 2>/dev/null); do xdotool windowminimize $w 2>/dev/null; done", shell=True)
    time.sleep(0.5)

def capture_window(wid, out_path):
    subprocess.run(["xdotool", "windowactivate", "--sync", wid])
    time.sleep(0.6)
    subprocess.run(["import", "-window", wid, out_path], check=True)
    print(f"[OK] Captura guardada: {out_path}")
    # Copy to Zajuna and Brain
    fname = os.path.basename(out_path)
    shutil.copy(out_path, os.path.join(ZAJUNA_CAPTURAS_DIR, fname))
    shutil.copy(out_path, os.path.join(BRAIN_DIR, fname))

def run_konsole_capture(title, cmd_str, out_filename):
    minimize_code()
    out_path = os.path.join(CAPTURAS_DIR, out_filename)
    script_content = f"""
    printf '\\033]0;%s\\007' '{title}'
    {cmd_str}
    sleep 10
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
    profile_dir = "/tmp/chrome_pitch_profile"
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
        
        # If JS eval needed, use Chrome automation or xdotool
        if js_eval:
            subprocess.run(["xdotool", "key", "ctrl+shift+j"])
            time.sleep(1.0)
            subprocess.run(["xdotool", "type", js_eval])
            time.sleep(0.3)
            subprocess.run(["xdotool", "key", "Return"])
            time.sleep(0.5)
            subprocess.run(["xdotool", "key", "ctrl+shift+j"]) # close devtools
            time.sleep(1.0)
            
        capture_window(wid, out_path)
    else:
        print("[ERROR] No se encontró ventana de Chrome")
    p.terminate()
    time.sleep(1.0)

def main():
    print("=== INICIANDO CAPTURA DE PANTALLAS EN KDE PLASMA X11 ===")
    
    # 1. Konsole Docker Despliegue
    cmd_1 = """
    cd /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-055_GA10-240201529-AA2-EV01_Pitch_Idea_Negocio/docker_pitch_web
    echo '========================================================================'
    echo '  EVIDENCIA GA10-240201529-AA2-EV01: PITCH IDEA DE NEGOCIO'
    echo '  ESTADO DE CONTENEDOR DOCKER Y ARCHIVOS DE ENTREGA - PUERTO 8103'
    echo '========================================================================'
    docker compose ps
    echo ''
    echo '--- VIDEO ELEVATOR PITCH GENERADO (54s / MP4 1080x1920) ---'
    ls -lh ../video/GA10-240201529-AA2-EV01_Pitch_Idea_Negocio.mp4
    echo ''
    echo '--- ESTRUCTURA DE ARCHIVOS DE LA EVIDENCIA ---'
    ls -la ..
    """
    run_konsole_capture("SENA ADSO - Despliegue Docker Pitch", cmd_1, "paso_01_despliegue_docker_pitch_konsole.png")
    
    # 2. Konsole Verificación de Salud
    cmd_2 = """
    echo '========================================================================'
    echo '  VERIFICACIÓN DE SALUD HTTP Y STREAMING DE VIDEO (PUERTO 8103)'
    echo '========================================================================'
    curl -I http://localhost:8103/
    echo ''
    echo '--- VERIFICACIÓN STREAMING VIDEO MP4 ---'
    curl -I http://localhost:8103/video/pitch_bella_italia.mp4
    echo ''
    echo '--- CONSULTA DATASET ESTRUCTURADO JSON ---'
    curl -s http://localhost:8103/datos_pitch.json | head -n 22
    """
    run_konsole_capture("SENA ADSO - Verificación de Salud y Endpoints", cmd_2, "paso_02_verificacion_salud_servicios_konsole.png")
    
    # 3. Chrome Escena 1 (Problema)
    js_sc1 = "document.getElementById('pitchVideo').currentTime = 3; document.getElementById('pitchVideo').pause();"
    run_chrome_capture("http://localhost:8103/", js_sc1, "paso_03_chrome_pitch_video_reproductor_escena1.png")
    
    # 4. Chrome Escena 2 (Solución Masa Madre)
    js_sc2 = "document.getElementById('pitchVideo').currentTime = 14; document.getElementById('pitchVideo').pause();"
    run_chrome_capture("http://localhost:8103/", js_sc2, "paso_04_chrome_pitch_video_reproductor_escena2.png")
    
    # 5. Chrome Guion Técnico
    js_guion = "showTab('guion');"
    run_chrome_capture("http://localhost:8103/", js_guion, "paso_05_chrome_pitch_guion_tecnico_tabla.png")
    
    # 6. Chrome Homonimia
    js_hom = "showTab('homonimia');"
    run_chrome_capture("http://localhost:8103/", js_hom, "paso_06_chrome_pitch_certificacion_homonimia.png")

    print("=== TODAS LAS CAPTURAS COMPLETADAS EXITOSAMENTE ===")

if __name__ == "__main__":
    main()
