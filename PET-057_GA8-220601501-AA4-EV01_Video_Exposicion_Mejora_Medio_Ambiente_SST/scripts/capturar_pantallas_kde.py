#!/usr/bin/env python3
# ==============================================================================
# SCRIPT DE CAPTURAS DE PANTALLA REALES EN KDE PLASMA X11 (KONSOLE Y CHROME)
# Evidencia: GA8-220601501-AA4-EV01 - Karen Yuliana Campo | Ficha: 3186681
# ==============================================================================

import os
import sys
import time
import shutil
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
CAPTURAS_DIR = os.path.join(BASE_DIR, "capturas")
SITIO_CAPTURAS_DIR = os.path.join(BASE_DIR, "sitio_sst_web", "capturas")
ZAJUNA_CAPTURAS_DIR = "/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA8-220601501-AA4-EV01/capturas"
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
    profile_dir = "/tmp/chrome_sst_profile"
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
    time.sleep(0.8)

def main():
    print("=== INICIANDO CAPTURAS REALES EN KDE PLASMA X11 ===")
    
    # 1. Konsole: Despliegue Docker Compose SST
    cmd1 = """
    cd /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-057_GA8-220601501-AA4-EV01_Video_Exposicion_Mejora_Medio_Ambiente_SST/docker_sst_web
    echo "=========================================================================="
    echo "  SENA CTPI POPAYAN - DESPLIEGUE DOCKER SERVICIO SST Y MEDIO AMBIENTE"
    echo "  Evidencia: GA8-220601501-AA4-EV01 | Aprendiz: Karen Yuliana Campo"
    echo "=========================================================================="
    docker compose ps
    echo ""
    echo "--- ESTADO DE CONTENEDOR DOCKER HTTPD (PUERTO 8105) ---"
    docker ps --filter "name=sena-sst-ambiental-web" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
    echo ""
    echo "--- ARCHIVO DE VIDEO EXPOSITIVO MP4 GENERADO ---"
    ls -lh ../video/
    echo ""
    echo "--- 10 IMAGENES REALES DE MEJORA EN MEDIO AMBIENTE Y SST ---"
    ls -lh ../imagenes_reales/
    """
    run_konsole_capture("SENA CTPI - Despliegue Docker SST", cmd1, "paso_01_despliegue_docker_sst_konsole.png")
    
    # 2. Konsole: Verificación HTTP 200 y JSON
    cmd2 = """
    echo "=========================================================================="
    echo "  VERIFICACION DE SALUD HTTP Y STREAMING SST (PUERTO 8105)"
    echo "=========================================================================="
    curl -I http://localhost:8105/
    echo ""
    echo "--- VERIFICACION STREAMING DE VIDEO EXPOSITIVO SST ---"
    curl -I http://localhost:8105/video/video_exposicion_sst.mp4
    echo ""
    echo "--- METADATOS Y DATASET JSON DE 10 OPORTUNIDADES DE MEJORA ---"
    curl -s http://localhost:8105/datos_mejora_sst_ambiental.json | head -n 40
    """
    run_konsole_capture("SENA CTPI - Salud Servicios SST", cmd2, "paso_02_verificacion_salud_servicios_sst_konsole.png")
    
    # 3. Chrome: Portal Web y Reproductor de Video
    run_chrome_capture("http://localhost:8105/", None, "paso_03_chrome_portal_sst_video_reproductor.png")
    
    # 4. Chrome: Galería de las 10 Mejoras con Fotos Reales
    run_chrome_capture("http://localhost:8105/", "switchTab('tab-mejoras')", "paso_04_chrome_galeria_imagenes_reales_mejora.png")
    
    # 5. Chrome: Guion Técnico Completo a Dos Columnas
    run_chrome_capture("http://localhost:8105/", "switchTab('tab-guion')", "paso_05_chrome_guion_tecnico_completo.png")
    
    # 6. Chrome: Ciclo PHVA, Indicadores y Metas
    run_chrome_capture("http://localhost:8105/", "switchTab('tab-phva')", "paso_06_chrome_dataset_indicadores_phva.png")
    
    print("=== TODAS LAS CAPTURAS DE PANTALLA EN KDE FUERON OBTENIDAS CON ÉXITO ===")

if __name__ == '__main__':
    main()
