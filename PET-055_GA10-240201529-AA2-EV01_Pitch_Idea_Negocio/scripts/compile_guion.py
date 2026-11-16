#!/usr/bin/env python3
# ==============================================================================
# COMPILADOR DE GUION TÉCNICO FORMAL SEPARADO (PDF / DOCX)
# Evidencia: GA10-240201529-AA2-EV01 - Pitch idea de negocio
# Documento: Guion Técnico y Storyboard TikTok (52s)
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán
# ==============================================================================

import os
import shutil
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
ENTREGA_DIR = '/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA10-240201529-AA2-EV01'
ARTIFACT_DIR = '/home/danilo/.gemini/antigravity/brain/abb27f79-dee2-489b-8c72-e5eac1b56603'

os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(ENTREGA_DIR, exist_ok=True)

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Guion Técnico y Storyboard - Elevator Pitch TikTok | Karen Campo</title>
  <style>
    @page {
      size: letter;
      margin: 1.2cm 1.4cm 1.2cm 1.4cm;
      @bottom-right {
        content: counter(page);
      }
    }
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      font-family: 'Segoe UI', system-ui, -apple-system, BlinkMacSystemFont, "Roboto", sans-serif;
      color: #1e293b;
      line-height: 1.5;
      font-size: 10pt;
    }
    .page {
      page-break-after: always;
      position: relative;
    }
    .page:last-child {
      page-break-after: avoid;
    }

    /* Header & Footer */
    .header-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid #008C45;
      padding-bottom: 8px;
      margin-bottom: 18px;
    }
    .header-title {
      font-size: 8.5pt;
      font-weight: 700;
      color: #008C45;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .header-meta {
      font-size: 8pt;
      color: #64748b;
      text-align: right;
    }

    h1.doc-title {
      font-size: 18pt;
      color: #0f172a;
      line-height: 1.2;
      margin-bottom: 12px;
      font-weight: 800;
    }
    h2.section-title {
      font-size: 12.5pt;
      color: #008C45;
      border-left: 4px solid #008C45;
      padding-left: 10px;
      margin-top: 18px;
      margin-bottom: 10px;
      font-weight: 700;
    }
    h3.sub-title {
      font-size: 10.5pt;
      color: #1e293b;
      margin-top: 12px;
      margin-bottom: 6px;
      font-weight: 700;
    }
    p {
      margin-bottom: 9px;
      text-align: justify;
    }

    /* Tables */
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 12px 0 16px;
      font-size: 8.5pt;
    }
    th {
      background: #008C45;
      color: #ffffff;
      font-weight: 700;
      padding: 7px 10px;
      text-align: left;
      border: 1px solid #007037;
    }
    td {
      padding: 6px 10px;
      border: 1px solid #cbd5e1;
      vertical-align: top;
    }
    tr:nth-child(even) td {
      background: #f8fafc;
    }

    /* Callouts */
    .callout {
      background: #f0fdf4;
      border-left: 4px solid #16a34a;
      padding: 10px 14px;
      margin: 12px 0;
      border-radius: 0 8px 8px 0;
      font-size: 9pt;
    }
    .callout-amber {
      background: #fffbeb;
      border-left: 4px solid #f59e0b;
      padding: 10px 14px;
      margin: 12px 0;
      border-radius: 0 8px 8px 0;
      font-size: 9pt;
    }
    blockquote {
      background: #f8fafc;
      border-left: 3px solid #008C45;
      padding: 10px 14px;
      margin: 10px 0;
      font-style: italic;
      color: #334155;
    }

    /* Cover Page */
    .cover-container {
      height: 92vh;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      border: 2px solid #008C45;
      padding: 38px;
      background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
      border-radius: 8px;
    }
    .cover-top {
      border-bottom: 3px solid #008C45;
      padding-bottom: 16px;
    }
    .cover-inst {
      font-size: 13pt;
      font-weight: 800;
      color: #008C45;
      letter-spacing: 0.5px;
    }
    .cover-subinst {
      font-size: 9.5pt;
      color: #475569;
      font-weight: 600;
    }
    .cover-center {
      margin: 28px 0;
    }
    .badge-pill {
      display: inline-block;
      background: #dcfce7;
      color: #166534;
      padding: 5px 12px;
      border-radius: 14px;
      font-size: 8.5pt;
      font-weight: 700;
      margin-bottom: 14px;
    }
    .cover-title {
      font-size: 21pt;
      color: #0f172a;
      font-weight: 800;
      line-height: 1.25;
      margin-bottom: 12px;
    }
    .cover-desc {
      font-size: 10.5pt;
      color: #334155;
      line-height: 1.5;
    }
    .meta-box {
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      padding: 16px 20px;
      margin-top: 16px;
      display: grid;
      grid-template-columns: 140px 1fr;
      row-gap: 6px;
      font-size: 9pt;
    }
    .meta-label {
      font-weight: 700;
      color: #64748b;
    }
    .meta-value {
      font-weight: 600;
      color: #0f172a;
    }
    .cover-bottom {
      border-top: 1px solid #cbd5e1;
      padding-top: 14px;
      font-size: 8.5pt;
      color: #64748b;
      display: flex;
      justify-content: space-between;
    }
  </style>
</head>
<body>

  <!-- PORTADA -->
  <div class="page">
    <div class="cover-container">
      <div class="cover-top">
        <div class="cover-inst">SERVICIO NACIONAL DE APRENDIZAJE (SENA)</div>
        <div class="cover-subinst">CENTRO DE TELEINFORMÁTICA Y PRODUCCIÓN INDUSTRIAL (CTPI) • REGIONAL CAUCA</div>
      </div>

      <div class="cover-center">
        <span class="badge-pill">DOCUMENTO TÉCNICO SEPARADO • GUÍA DE APRENDIZAJE 10</span>
        <h1 class="cover-title">GUION TÉCNICO Y STORYBOARD<br>ELEVATOR PITCH TIKTOK (52s)</h1>
        <p class="cover-desc">
          Partitura audiovisual, guion literario y desglose técnico segundo a segundo para el Elevator Pitch vertical (9:16) del emprendimiento <strong>Pizzería Gourmet Bella Italia Popayán</strong>, cumpliendo con la regla de brevedad ($\le 59$ segundos), diseño dinámico de alto impacto y cero saturación de texto.
        </p>

        <div class="meta-box">
          <div class="meta-label">Programa:</div>
          <div class="meta-value">Tecnólogo en Análisis y Desarrollo de Software (ADSO)</div>

          <div class="meta-label">Ficha:</div>
          <div class="meta-value">3186681</div>

          <div class="meta-label">Competencia:</div>
          <div class="meta-value">240201529 — Cultura Emprendedora y Empresarial</div>

          <div class="meta-label">Actividad:</div>
          <div class="meta-value">GA10-240201529-AA2 — Definir la idea de negocio según oportunidades</div>

          <div class="meta-label">Evidencia:</div>
          <div class="meta-value">GA10-240201529-AA2-EV01 — Pitch idea de negocio</div>

          <div class="meta-label">Emprendimiento:</div>
          <div class="meta-value">Pizzería Gourmet Bella Italia Popayán S.A.S. (CIIU 5611)</div>

          <div class="meta-label">Aprendiz:</div>
          <div class="meta-value">Karen Yuliana Campo</div>

          <div class="meta-label">Duración:</div>
          <div class="meta-value">51.82 segundos exactos (Límite: 59 segundos)</div>

          <div class="meta-label">Formato:</div>
          <div class="meta-value">Vertical 9:16 (1080x1920 Full HD, H.264 / AAC 192k)</div>
        </div>
      </div>

      <div class="cover-bottom">
        <div>Popayán, Cauca — Colombia</div>
        <div>Noviembre de 2026</div>
      </div>
    </div>
  </div>

  <!-- PÁGINA 2: FICHA TÉCNICA Y GUION LITERARIO -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">GUION TÉCNICO ELEVATOR PITCH • SENA ADSO 3186681</div>
      <div class="header-meta">Karen Yuliana Campo | Noviembre 2026</div>
    </div>

    <h2 class="section-title">1. FICHA TÉCNICA DE PRODUCCIÓN AUDIOVISUAL</h2>
    <table>
      <thead>
        <tr>
          <th>Parámetro Técnico</th>
          <th>Especificación de Producción</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Título de la Pieza</strong></td>
          <td>Elevator Pitch Oficial: Pizzería Gourmet Bella Italia Popayán</td>
        </tr>
        <tr>
          <td><strong>Formato y Relación</strong></td>
          <td>Video Vertical 9:16 (Optimizado para TikTok, Instagram Reels y YouTube Shorts)</td>
        </tr>
        <tr>
          <td><strong>Resolución</strong></td>
          <td>1080 x 1920 píxeles (Full HD Vertical) a 30 FPS (1554 fotogramas generados)</td>
        </tr>
        <tr>
          <td><strong>Duración Exacta</strong></td>
          <td><strong>51.82 segundos</strong> (Cumple estrictamente la regla de $\le 59$ segundos de Guía 10)</td>
        </tr>
        <tr>
          <td><strong>Códecs de Salida</strong></td>
          <td>Video: H.264 / AVC (VBR 1 pass 10 Mbps) | Audio: AAC Estéreo (48.0 kHz, 320 kbps, -14 LUFS)</td>
        </tr>
        <tr>
          <td><strong>Motor de Ensamble NLE</strong></td>
          <td><strong>FilmCraft CLI</strong> (v0.20.1) con preset de exportación nativo <em>"TikTok 1080×1920"</em> y directrices del pack <code>iart-ai/tiktok-video-skills</code> (safe zone 900x1400, active word pop-in karaoke y patrón de interrupción cada 2.5s)</td>
        </tr>
        <tr>
          <td><strong>Diseño Sonoro</strong></td>
          <td>Locución oficial en vivo grabada por Karen Yuliana Campo + banda sonora lo-fi rítmica suave (120 BPM) con <em>audio ducking</em> dinámico (-18 dB durante voz para máxima inteligibilidad)</td>
        </tr>
        <tr>
          <td><strong>Enfoque Visual</strong></td>
          <td>Minimalismo de alto impacto: tipografía extra-grande (68-74px), badges coloridos, cero saturación de texto y lectura instantánea</td>
        </tr>
      </tbody>
    </table>

    <h2 class="section-title">2. GUION LITERARIO COMPLETO (LOCUCIÓN EN ESPAÑOL)</h2>
    <p>
      La narrativa del pitch fue concebida para atrapar la atención en los primeros 3 segundos (*hook*), plantear una solución gastronómica irresistible, vincular el corazón campesino del Cauca, demostrar innovación digital ADSO y culminar en una llamada a la acción con canales directos:
    </p>

    <blockquote>
      <strong>[00:00 - 00:07.5] Escena 1 (Problema / Hook):</strong><br>
      "¿Cansado de pedir pizza en Popayán y que llegue fría, grasosa o con una masa pesada que no te deja dormir?"
    </blockquote>

    <blockquote>
      <strong>[00:07.5 - 00:18.5] Escena 2 (Solución Gourmet):</strong><br>
      "¡Llegó Bella Italia Popayán! La auténtica pizza artesanal con masa madre de 48 horas de fermentación y horneada a 450 grados en solo 90 segundos."
    </blockquote>

    <blockquote>
      <strong>[00:18.5 - 00:29.0] Escena 3 (Tradición + Corazón Caucano):</strong><br>
      "Unimos técnica italiana con insumos de nuestra tierra: quesos campesinos de Silvia y hortalizas orgánicas del Cauca para una textura crocante y digestión ligera."
    </blockquote>

    <blockquote>
      <strong>[00:29.0 - 00:39.5] Escena 4 (Innovación Tecnológica ADSO):</strong><br>
      "Con nuestra aplicación web desarrollada en el SENA pides en segundos y recibes tu pizza a más de 70 grados en menos de 30 minutos gracias a baúles térmicos."
    </blockquote>

    <blockquote>
      <strong>[00:39.5 - 00:51.8] Escena 5 (Llamado a la Acción / CTA):</strong><br>
      "Visítanos en el Centro Histórico de Popayán o pide a nuestro WhatsApp oficial. ¡Bella Italia Popayán: Pasión italiana con corazón caucano! ¡Haz tu pedido ya!"
    </blockquote>
  </div>

  <!-- PÁGINA 3: GUION TÉCNICO ESCENA POR ESCENA -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">DESGLOSE TÉCNICO SEGUNDO A SEGUNDO (1/2)</div>
      <div class="header-meta">GA10-240201529-AA2-EV01 • Ficha 3186681</div>
    </div>

    <h2 class="section-title">3. GUION TÉCNICO DETALLADO POR ESCENAS</h2>

    <h3 class="sub-title">ESCENA 1: EL PROBLEMA REAL EN POPAYÁN (00:00 - 00:07.5 • 7.5 SEGUNDOS)</h3>
    <table>
      <tr>
        <th style="width: 25%;">Parámetro</th>
        <th style="width: 75%;">Detalle Técnico y Visual</th>
      </tr>
      <tr>
        <td><strong>Paso Guía 10</strong></td>
        <td>Paso 1: Identificación del Problema de Mercado en Popayán</td>
      </tr>
      <tr>
        <td><strong>Locución Audio</strong></td>
        <td>"¿Cansado de pedir pizza en Popayán y que llegue fría, grasosa o con una masa pesada que no te deja dormir?"</td>
      </tr>
      <tr>
        <td><strong>Banda Sonora</strong></td>
        <td>Beat electrónico a 120 BPM con efecto de reloj ticking (sensación de urgencia)</td>
      </tr>
      <tr>
        <td><strong>Titular On-Screen</strong></td>
        <td><strong>¿PIZZAS FRÍAS Y MASAS PESADAS?</strong> (Tipografía 68px blanca y roja)</td>
      </tr>
      <tr>
        <td><strong>Badges de Impacto</strong></td>
        <td>
          • ⏱️ <strong>DEMORAS DE 60+ MIN:</strong> Llegan frías y arruinan tu cena<br>
          • 🤢 <strong>MASA ULTRA PESADA:</strong> Levadura química sin fermentar<br>
          • 🥶 <strong>PIZZAS GRASOSAS:</strong> Ingredientes de baja calidad
        </td>
      </tr>
      <tr>
        <td><strong>Subtítulo TikTok</strong></td>
        <td>Caja negra con borde dorado: texto en amarillo neón (#FDE047, 38px) 100% legible</td>
      </tr>
    </table>

    <h3 class="sub-title">ESCENA 2: LA SOLUCIÓN GOURMET BELLA ITALIA (00:07.5 - 00:18.5 • 11 SEGUNDOS)</h3>
    <table>
      <tr>
        <th style="width: 25%;">Parámetro</th>
        <th style="width: 75%;">Detalle Técnico y Visual</th>
      </tr>
      <tr>
        <td><strong>Paso Guía 10</strong></td>
        <td>Paso 2: Formulación de la Solución Diferenciada e Innovadora</td>
      </tr>
      <tr>
        <td><strong>Locución Audio</strong></td>
        <td>"¡Llegó Bella Italia Popayán! La auténtica pizza artesanal con masa madre de 48 horas de fermentación y horneada a 450 grados en solo 90 segundos."</td>
      </tr>
      <tr>
        <td><strong>Banda Sonora</strong></td>
        <td>Entrada de bajo enérgico y acordes brillantes de piano eléctrico (sensación de optimismo)</td>
      </tr>
      <tr>
        <td><strong>Titular On-Screen</strong></td>
        <td><strong>¡LLEGÓ BELLA ITALIA! PIZZA ARTESANAL</strong> (Tipografía 74px dorada y blanca)</td>
      </tr>
      <tr>
        <td><strong>Badges de Impacto</strong></td>
        <td>
          • 🌾 <strong>MASA MADRE 48 HORAS:</strong> Fermentación biológica ultraligera<br>
          • 🌋 <strong>HORNO A 450 GRADOS:</strong> Piedra volcánica a fuego vivo<br>
          • ⚡ <strong>LISTA EN 90 SEGUNDOS:</strong> Corteza crocante y alvéolos aireados
        </td>
      </tr>
      <tr>
        <td><strong>Elemento Central</strong></td>
        <td>Logo circular oficial Bella Italia (260x260px) con estampa tricolor italiana</td>
      </tr>
      <tr>
        <td><strong>Subtítulo TikTok</strong></td>
        <td>Subtítulo en amarillo neón destacando la masa madre de 48h y el horno a 450°C</td>
      </tr>
    </table>
  </div>

  <!-- PÁGINA 4: DESGLOSE TÉCNICO ESCENAS 3, 4 Y 5 -->
  <div class="page">
    <div class="header-bar">
      <div class="header-title">DESGLOSE TÉCNICO SEGUNDO A SEGUNDO (2/2)</div>
      <div class="header-meta">GA10-240201529-AA2-EV01 • Ficha 3186681</div>
    </div>

    <h3 class="sub-title">ESCENA 3: TRADICIÓN ITALIANA + CORAZÓN CAUCANO (00:18.5 - 00:29.0 • 10.5 SEGUNDOS)</h3>
    <table>
      <tr>
        <th style="width: 25%;">Parámetro</th>
        <th style="width: 75%;">Detalle Técnico y Visual</th>
      </tr>
      <tr>
        <td><strong>Paso Guía 10</strong></td>
        <td>Paso 3: Alianza Productiva Local y Sostenibilidad Regional</td>
      </tr>
      <tr>
        <td><strong>Locución Audio</strong></td>
        <td>"Unimos técnica italiana con insumos de nuestra tierra: quesos campesinos de Silvia y hortalizas orgánicas del Cauca para una textura crocante y digestión ligera."</td>
      </tr>
      <tr>
        <td><strong>Titular On-Screen</strong></td>
        <td><strong>TRADICIÓN ITALIANA CON CORAZÓN CAUCANO</strong> (Tipografía 68px verde menta)</td>
      </tr>
      <tr>
        <td><strong>Badges de Impacto</strong></td>
        <td>
          • 🧀 <strong>QUESOS DE SILVIA, CAUCA:</strong> Fior di latte fresco de cooperativa local<br>
          • 🍅 <strong>HUERTAS DEL CAUCA:</strong> Albahaca y pomodoro orgánico campesino<br>
          • 💚 <strong>COMERCIO JUSTO LOCAL:</strong> Compra directa sin intermediarios
        </td>
      </tr>
      <tr>
        <td><strong>Subtítulo TikTok</strong></td>
        <td>Subtítulo sincronizado con mención a Silvia y hortalizas orgánicas del Cauca</td>
      </tr>
    </table>

    <h3 class="sub-title">ESCENA 4: INNOVACIÓN TECNOLÓGICA SENA ADSO (00:29.0 - 00:39.5 • 10.5 SEGUNDOS)</h3>
    <table>
      <tr>
        <th style="width: 25%;">Parámetro</th>
        <th style="width: 75%;">Detalle Técnico y Visual</th>
      </tr>
      <tr>
        <td><strong>Paso Guía 10</strong></td>
        <td>Paso 4: Ventaja Tecnológica, Ecosistema Digital y Logística Térmica</td>
      </tr>
      <tr>
        <td><strong>Locución Audio</strong></td>
        <td>"Con nuestra aplicación web desarrollada en el SENA pides en segundos y recibes tu pizza a más de 70 grados en menos de 30 minutos gracias a baúles térmicos."</td>
      </tr>
      <tr>
        <td><strong>Titular On-Screen</strong></td>
        <td><strong>WEB APP SENA ADSO + DELIVERY TÉRMICO</strong> (Tipografía 68px azul eléctrico)</td>
      </tr>
      <tr>
        <td><strong>Badges de Impacto</strong></td>
        <td>
          • 📱 <strong>PIDE EN 3 CLICS:</strong> Plataforma web con tracking en tiempo real<br>
          • 🌡️ <strong>BAÚL TÉRMICO > 70°C:</strong> Llega caliente y crocante a tu mesa<br>
          • ⏱️ <strong>ENTREGA EN < 30 MIN:</strong> Garantía de puntualidad o postre gratis
        </td>
      </tr>
      <tr>
        <td><strong>Elemento Central</strong></td>
        <td>Captura del catálogo interactivo web y móvil ADSO mostrando carrito y tracking</td>
      </tr>
    </table>

    <h3 class="sub-title">ESCENA 5: CALL TO ACTION (CTA) Y CIERRE (00:39.5 - 00:51.8 • 12.3 SEGUNDOS)</h3>
    <table>
      <tr>
        <th style="width: 25%;">Parámetro</th>
        <th style="width: 75%;">Detalle Técnico y Visual</th>
      </tr>
      <tr>
        <td><strong>Paso Guía 10</strong></td>
        <td>Paso 5: Llamado a la Acción, Canales de Contacto y Validación de Homonimia</td>
      </tr>
      <tr>
        <td><strong>Locución Audio</strong></td>
        <td>"Visítanos en el Centro Histórico de Popayán o pide a nuestro WhatsApp oficial. ¡Bella Italia Popayán: Pasión italiana con corazón caucano! ¡Haz tu pedido ya!"</td>
      </tr>
      <tr>
        <td><strong>Titular On-Screen</strong></td>
        <td><strong>¡VIVE LA EXPERIENCIA BELLA ITALIA HOY!</strong> (Tipografía 74px dorada brillante)</td>
      </tr>
      <tr>
        <td><strong>Botón Central CTA</strong></td>
        <td>Botón dorado gigante: <strong>🍕 ¡HAZ TU PEDIDO YA! 🍕</strong></td>
      </tr>
      <tr>
        <td><strong>Badges de Contacto</strong></td>
        <td>
          • 🏛️ <strong>SEDE CENTRO HISTÓRICO:</strong> Calle 4ta No. 3-45 • Popayán, Cauca<br>
          • 📲 <strong>WHATSAPP OFICIAL:</strong> (+57) 312 890 4521 • Pedidos al instante<br>
          • 📋 <strong>MARCA REGISTRADA RUES:</strong> Cámara de Comercio Popayán • CIIU 5611
        </td>
      </tr>
      <tr>
        <td><strong>Firma de Aprendiz</strong></td>
        <td>Karen Yuliana Campo • Tecnólogo en ADSO • Ficha 3186681</td>
      </tr>
    </table>

    <div style="margin-top: 25px; border-top: 1px solid #cbd5e1; padding-top: 12px; font-size: 8.5pt; color: #475569; display: flex; justify-content: space-between;">
      <div><strong>Autora:</strong> Karen Yuliana Campo — SENA Regional Cauca CTPI</div>
      <div><strong>Evidencia:</strong> GA10-240201529-AA2-EV01 — Guion Técnico</div>
    </div>
  </div>

</body>
</html>
"""

html_temp_path = os.path.join(DOCS_DIR, 'temp_guion_print.html')
pdf_output_path = os.path.join(DOCS_DIR, 'GA10-240201529-AA2-EV01_Guion_Tecnico_Pitch.pdf')
docx_output_path = os.path.join(DOCS_DIR, 'GA10-240201529-AA2-EV01_Guion_Tecnico_Pitch.docx')

def main():
    print("=== COMPILANDO GUION TÉCNICO SEPARADO (PDF Y DOCX) ===")
    with open(html_temp_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    # 1. Compile PDF
    print("Compilando PDF de Guion Técnico...")
    subprocess.run([
        "google-chrome",
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_output_path}",
        html_temp_path
    ], check=True)
    pdf_size_kb = os.path.getsize(pdf_output_path) / 1024
    print(f"[OK] PDF Guion generado: {pdf_output_path} ({pdf_size_kb:.1f} KB)")

    # 2. Compile DOCX via LibreOffice (HTML -> ODT -> DOCX)
    print("Compilando DOCX de Guion Técnico...")
    subprocess.run([
        "libreoffice", "--headless",
        "--convert-to", "odt:writer8",
        html_temp_path,
        "--outdir", DOCS_DIR
    ], check=True)
    temp_odt = os.path.join(DOCS_DIR, 'temp_guion_print.odt')
    subprocess.run([
        "libreoffice", "--headless",
        "--convert-to", "docx:MS Word 2007 XML",
        temp_odt,
        "--outdir", DOCS_DIR
    ], check=True)
    temp_docx = os.path.join(DOCS_DIR, 'temp_guion_print.docx')
    if os.path.exists(temp_docx):
        shutil.move(temp_docx, docx_output_path)
    if os.path.exists(temp_odt):
        os.remove(temp_odt)
    if os.path.exists(html_temp_path):
        os.remove(html_temp_path)

    docx_size_kb = os.path.getsize(docx_output_path) / 1024
    print(f"[OK] DOCX Guion generado: {docx_output_path} ({docx_size_kb:.1f} KB)")

    # 3. Distribute to Zajuna and Brain
    shutil.copy(pdf_output_path, ENTREGA_DIR)
    shutil.copy(docx_output_path, ENTREGA_DIR)
    shutil.copy(pdf_output_path, ARTIFACT_DIR)
    shutil.copy(docx_output_path, ARTIFACT_DIR)
    
    # Also copy the markdown file
    md_guion = os.path.join(DOCS_DIR, 'GUION_TECNICO_PITCH_TIKTOK.md')
    if os.path.exists(md_guion):
        shutil.copy(md_guion, ENTREGA_DIR)
        shutil.copy(md_guion, ARTIFACT_DIR)

    print("=== GUION TÉCNICO SEPARADO COMPILADO Y DISTRIBUIDO ===")

if __name__ == '__main__':
    main()
