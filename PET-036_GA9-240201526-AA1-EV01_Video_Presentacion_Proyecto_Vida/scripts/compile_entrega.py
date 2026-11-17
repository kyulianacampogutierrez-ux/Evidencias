#!/usr/bin/env python3
# ==============================================================================
# EMPAQUETADOR DE ENTREGA ZAJUNA
# Evidencia: GA9-240201526-AA1-EV01 - Presentación del Proyecto de Vida
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681
# ==============================================================================

import os
import shutil
import zipfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
ENTREGA_DIR = '/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA9-240201526-AA1-EV01'
ARTIFACT_DIR = '/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603'

os.makedirs(ENTREGA_DIR, exist_ok=True)

# 1. Generar enlace_repositorio.txt
repo_content = """================================================================================
SERVICIO NACIONAL DE APRENDIZAJE - SENA
CENTRO DE TELEINFORMÁTICA Y PRODUCCIÓN INDUSTRIAL (CTPI) - REGIONAL CAUCA
TECNÓLOGO EN ANÁLISIS Y DESARROLLO DE SOFTWARE (ADSO) - FICHA: 3186681
================================================================================
EVIDENCIA: GA9-240201526-AA1-EV01: Presentación del proyecto de vida
COMPETENCIA: 240201526 - Promover la interacción idónea consigo mismo, con los demás
y con la naturaleza en los contextos laboral y social (Ética y Cultura de Paz)
APRENDIZ: Karen Yuliana Campo
================================================================================

ENLACE AL REPOSITORIO OFICIAL GITHUB:
https://github.com/kyulianacampogutierrez-ux/Evidencias/tree/main/PET-036_GA9-240201526-AA1-EV01_Video_Presentacion_Proyecto_Vida

CARPETA LOCAL DE ARTEFACTOS Y GUION TÉCNICO:
file:///home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA9-240201526-AA1-EV01/

ARCHIVOS DE GUION TÉCNICO Y LITERARIO:
- PDF: GA9-240201526-AA1-EV01_Guion_Video_Presentacion_Proyecto_Vida.pdf
- Word DOCX: GA9-240201526-AA1-EV01_Guion_Video_Presentacion_Proyecto_Vida.docx
- Markdown: GUION_TECNICO_VIDEO_PRESENTACION_PROYECTO_VIDA.md
- Guía y Cuestionario: GUIA_PREGUNTAS_FOTOS_PROYECTO_VIDA.md
================================================================================
"""

repo_path = os.path.join(BASE_DIR, 'enlace_repositorio.txt')
with open(repo_path, 'w', encoding='utf-8') as f:
    f.write(repo_content)
shutil.copy(repo_path, ENTREGA_DIR)
shutil.copy(repo_path, ARTIFACT_DIR)

# 2. Generar ZIP KARENCAMPO_AA1_EV01_ETICA_GUIA9.zip
zip_name = 'KARENCAMPO_AA1_EV01_ETICA_GUIA9.zip'
zip_local = os.path.join(BASE_DIR, zip_name)
zip_entrega = os.path.join(ENTREGA_DIR, zip_name)
zip_artifact = os.path.join(ARTIFACT_DIR, zip_name)

files_to_zip = [
    ('docs/GA9-240201526-AA1-EV01_Guion_Video_Presentacion_Proyecto_Vida.pdf', 'GA9-240201526-AA1-EV01_Guion_Video_Presentacion_Proyecto_Vida.pdf'),
    ('docs/GA9-240201526-AA1-EV01_Guion_Video_Presentacion_Proyecto_Vida.docx', 'GA9-240201526-AA1-EV01_Guion_Video_Presentacion_Proyecto_Vida.docx'),
    ('docs/GUION_TECNICO_VIDEO_PRESENTACION_PROYECTO_VIDA.md', 'GUION_TECNICO_VIDEO_PRESENTACION_PROYECTO_VIDA.md'),
    ('docs/GUIA_PREGUNTAS_FOTOS_PROYECTO_VIDA.md', 'GUIA_PREGUNTAS_FOTOS_PROYECTO_VIDA.md'),
    ('enlace_repositorio.txt', 'enlace_repositorio.txt')
]

with zipfile.ZipFile(zip_local, 'w', zipfile.ZIP_DEFLATED) as z:
    for rel_path, arcname in files_to_zip:
        abs_p = os.path.join(BASE_DIR, rel_path)
        if os.path.exists(abs_p):
            z.write(abs_p, arcname)

shutil.copy(zip_local, zip_entrega)
shutil.copy(zip_local, zip_artifact)

print(f"[OK] Paquete ZIP generado: {zip_local} ({os.path.getsize(zip_local)/1024:.1f} KB)")
print(f"[OK] Distribuido a: {zip_entrega}")
