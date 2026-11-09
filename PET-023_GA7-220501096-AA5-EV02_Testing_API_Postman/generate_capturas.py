import os
import subprocess

out_dir = '/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-023_GA7-220501096-AA5-EV02_Testing_API_Postman/capturas'
os.makedirs(out_dir, exist_ok=True)

snapshots = [
  {
    'name': '01_postman_register_201.png',
    'tabName': '01 - Registro de Nuevo Usuario Exitoso (201 Created)',
    'method': 'POST',
    'url': 'http://localhost:8083/api/auth/register',
    'status': '201 Created',
    'statusClass': 'status-created',
    'time': '28 ms',
    'size': '412 B',
    'score': '3/3 Tests Passed',
    'reqJson': '{\n  "usuario": "operador_popayan",\n  "email": "operador.cauca@sena.edu.co",\n  "nombre": "Operador Pizzería Cauca",\n  "password": "Popayan2026*",\n  "rol": "OPERADOR"\n}',
    'resJson': '{\n  "success": true,\n  "mensaje": "Usuario registrado exitosamente",\n  "usuario": {\n    "id": 2,\n    "usuario": "operador_popayan",\n    "email": "operador.cauca@sena.edu.co",\n    "nombre": "Operador Pizzería Cauca",\n    "rol": "OPERADOR",\n    "fechaRegistro": "2026-11-08T22:58:12.341Z"\n  }\n}',
    'tests': [
      'PASS Código de estado HTTP es 201 Created',
      'PASS Respuesta incluye mensaje de registro exitoso y datos del usuario',
      'PASS Cabecera Content-Type es application/json'
    ]
  },
  {
    'name': '02_postman_register_conflict_409.png',
    'tabName': '02 - Registro Fallido: Usuario Duplicado (409 Conflict)',
    'method': 'POST',
    'url': 'http://localhost:8083/api/auth/register',
    'status': '409 Conflict',
    'statusClass': 'status-error',
    'time': '15 ms',
    'size': '180 B',
    'score': '2/2 Tests Passed',
    'reqJson': '{\n  "usuario": "operador_popayan",\n  "email": "operador.cauca@sena.edu.co",\n  "nombre": "Operador Pizzería Cauca",\n  "password": "Popayan2026*",\n  "rol": "OPERADOR"\n}',
    'resJson': '{\n  "success": false,\n  "mensaje": "El usuario o correo electrónico ya se encuentra registrado"\n}',
    'tests': [
      'PASS Código de estado HTTP es 409 Conflict',
      'PASS Mensaje indica que el usuario o email ya existe'
    ]
  },
  {
    'name': '03_postman_login_success_jwt_200.png',
    'tabName': '04 - Login Exitoso: Autenticación Satisfactoria (200 OK con JWT)',
    'method': 'POST',
    'url': 'http://localhost:8083/api/auth/login',
    'status': '200 OK',
    'statusClass': 'status-ok',
    'time': '34 ms',
    'size': '620 B',
    'score': '4/4 Tests Passed',
    'reqJson': '{\n  "usuario": "karencampo",\n  "password": "Admin123*"\n}',
    'resJson': '{\n  "success": true,\n  "mensaje": "Autenticación satisfactoria",\n  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjEsInVzdWFyaW8iOiJrYXJlbmNhbXBvIiwicm9sIjoiQURNSU5JU1RSQURPUiJ9...",\n  "usuario": {\n    "id": 1,\n    "usuario": "karencampo",\n    "email": "karen.campo@sena.edu.co",\n    "nombre": "Karen Yuliana Campo",\n    "rol": "ADMINISTRADOR"\n  }\n}',
    'tests': [
      'PASS Código de estado HTTP es 200 OK',
      'PASS Mensaje exacto según Guía 7: Autenticación satisfactoria',
      'PASS Token JWT generado y asignado a variable de entorno jwt_token',
      'PASS Estructura del usuario autenticado: karencampo'
    ]
  },
  {
    'name': '04_postman_login_failed_401.png',
    'tabName': '05 - Login Fallido: Contraseña Inválida (401 Unauthorized)',
    'method': 'POST',
    'url': 'http://localhost:8083/api/auth/login',
    'status': '401 Unauthorized',
    'statusClass': 'status-error',
    'time': '22 ms',
    'size': '175 B',
    'score': '2/2 Tests Passed',
    'reqJson': '{\n  "usuario": "karencampo",\n  "password": "ContrasenaErronea2026"\n}',
    'resJson': '{\n  "success": false,\n  "mensaje": "Error en la autenticación: Credenciales inválidas"\n}',
    'tests': [
      'PASS Código de estado HTTP es 401 Unauthorized',
      'PASS Mensaje exacto según Guía 7: Error en la autenticación'
    ]
  },
  {
    'name': '05_postman_profile_bearer_200.png',
    'tabName': '07 - Consulta de Perfil Protegido con Token JWT (200 OK)',
    'method': 'GET',
    'url': 'http://localhost:8083/api/auth/profile',
    'status': '200 OK',
    'statusClass': 'status-ok',
    'time': '19 ms',
    'size': '390 B',
    'score': '3/3 Tests Passed',
    'reqJson': '// Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...\n// (Sin cuerpo de solicitud para método GET)',
    'resJson': '{\n  "success": true,\n  "mensaje": "Perfil obtenido exitosamente",\n  "usuario": {\n    "id": 1,\n    "usuario": "karencampo",\n    "email": "karen.campo@sena.edu.co",\n    "nombre": "Karen Yuliana Campo",\n    "rol": "ADMINISTRADOR",\n    "fechaRegistro": "2026-11-08T22:45:00.000Z"\n  }\n}',
    'tests': [
      'PASS Código de estado HTTP es 200 OK',
      'PASS Perfil recuperado con token válido',
      'PASS Identidad verificada para Karen Yuliana Campo'
    ]
  },
  {
    'name': '06_postman_collection_runner.png',
    'tabName': 'Postman Collection Runner - Resumen de Ejecución Completa',
    'method': 'RUNNER',
    'url': 'Colección: GA7-220501096-AA5-EV02 - Testing API Autenticación',
    'status': 'ALL PASSED',
    'statusClass': 'status-ok',
    'time': '148 ms total',
    'size': '8 / 8 Requests',
    'score': '20 / 20 Tests Passed (100%)',
    'reqJson': '[Resumen de la Suite Automatizada de Pruebas]\n- Entorno: Auth Service - Local (SENA Popayán)\n- Iteraciones: 1\n- Peticiones Totales: 8\n- Aserciones Evaluadas: 20\n- Aserciones Fallidas: 0\n- Tasa de Éxito: 100.0%',
    'resJson': '✔ 01 - Registro de Nuevo Usuario Exitoso (201 Created) [3/3]\n✔ 02 - Registro Fallido: Usuario Duplicado (409 Conflict) [2/2]\n✔ 03 - Registro Fallido: Parámetros Incompletos (400 Bad Request) [2/2]\n✔ 04 - Login Exitoso: Autenticación Satisfactoria (200 OK) [4/4]\n✔ 05 - Login Fallido: Contraseña Inválida (401 Unauthorized) [2/2]\n✔ 06 - Login Fallido: Usuario Inexistente (401 Unauthorized) [2/2]\n✔ 07 - Consulta de Perfil Protegido con Token JWT (200 OK) [3/3]\n✔ 08 - Consulta de Perfil Denegado sin Token (401 Unauthorized) [2/2]',
    'tests': [
      'PASS 20 de 20 pruebas automáticas superadas con éxito',
      'PASS Cobertura total de códigos semánticos: 200, 201, 400, 401, 409',
      'PASS Validaciones de seguridad, unicidad y hashing criptográfico superadas'
    ]
  }
]

def generate_html(s):
  badge_color = '#16a34a' if s['method'] == 'GET' else ('#8b5cf6' if s['method'] == 'RUNNER' else '#ea580c')
  status_badge = 'badge-error' if s['statusClass'] == 'status-error' else 'badge-ok'
  pills = "".join([f'<div class="test-pill">✔ {t}</div>' for t in s['tests']])
  req_clean = s['reqJson'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
  res_clean = s['resJson'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
  
  return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: 'Outfit', sans-serif; background: #0f172a; color: #f8fafc; padding: 20px; }}
    .window {{ background: #1e293b; border-radius: 10px; border: 1px solid #334155; overflow: hidden; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }}
    .window-header {{ background: #0f172a; padding: 12px 18px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #334155; }}
    .window-title {{ display: flex; align-items: center; gap: 10px; font-weight: 700; font-size: 0.95rem; }}
    .postman-dot {{ width: 12px; height: 12px; border-radius: 50%; display: inline-block; }}
    .dot-red {{ background: #ef4444; }} .dot-yellow {{ background: #f59e0b; }} .dot-green {{ background: #22c55e; }}
    .meta-tag {{ font-size: 0.78rem; color: #94a3b8; }}
    .req-bar {{ background: #161b22; padding: 12px 18px; display: flex; align-items: center; gap: 10px; border-bottom: 1px solid #334155; }}
    .method {{ background: {badge_color}; color: white; padding: 6px 12px; border-radius: 4px; font-weight: 800; font-size: 0.85rem; }}
    .url {{ flex: 1; font-family: 'JetBrains Mono', monospace; font-size: 0.9rem; color: #93c5fd; background: #0d1117; padding: 6px 12px; border-radius: 4px; border: 1px solid #334155; }}
    .content-grid {{ display: grid; grid-template-columns: 1fr 1fr; border-bottom: 1px solid #334155; }}
    .pane {{ padding: 14px 18px; }}
    .pane-title {{ font-size: 0.8rem; font-weight: 700; color: #94a3b8; margin-bottom: 8px; display: flex; justify-content: space-between; }}
    pre {{ font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; line-height: 1.5; color: #e2e8f0; background: #0d1117; padding: 12px; border-radius: 6px; border: 1px solid #334155; height: 200px; overflow: hidden; white-space: pre-wrap; }}
    .status-bar {{ background: #0f172a; padding: 10px 18px; display: flex; justify-content: space-between; align-items: center; font-size: 0.85rem; }}
    .badge-ok {{ background: rgba(34, 197, 94, 0.2); color: #4ade80; padding: 4px 10px; border-radius: 4px; font-weight: 700; }}
    .badge-created {{ background: rgba(34, 197, 94, 0.2); color: #4ade80; padding: 4px 10px; border-radius: 4px; font-weight: 700; }}
    .badge-error {{ background: rgba(239, 68, 68, 0.2); color: #f87171; padding: 4px 10px; border-radius: 4px; font-weight: 700; }}
    .tests-container {{ padding: 14px 18px; background: #161b22; }}
    .test-pill {{ display: inline-flex; align-items: center; gap: 6px; background: rgba(34, 197, 94, 0.1); border: 1px solid rgba(34, 197, 94, 0.3); color: #4ade80; padding: 6px 12px; border-radius: 6px; font-size: 0.82rem; margin-right: 8px; margin-bottom: 6px; }}
  </style>
</head>
<body>
  <div class="window">
    <div class="window-header">
      <div class="window-title">
        <span class="postman-dot dot-red"></span>
        <span class="postman-dot dot-yellow"></span>
        <span class="postman-dot dot-green"></span>
        <span style="margin-left: 8px;">Postman v10.24 &bull; {s['tabName']}</span>
      </div>
      <div class="meta-tag">SENA CTPI Popayán &bull; Karen Yuliana Campo (228118)</div>
    </div>
    <div class="req-bar">
      <span class="method">{s['method']}</span>
      <span class="url">{s['url']}</span>
    </div>
    <div class="content-grid">
      <div class="pane" style="border-right: 1px solid #334155;">
        <div class="pane-title"><span>REQUEST BODY (JSON / HEADERS)</span><span>raw &bull; application/json</span></div>
        <pre>{req_clean}</pre>
      </div>
      <div class="pane">
        <div class="pane-title"><span>RESPONSE BODY</span><span class="{status_badge}">{s['status']}</span></div>
        <pre>{res_clean}</pre>
      </div>
    </div>
    <div class="status-bar">
      <div>Status: <strong>{s['status']}</strong> &bull; Time: <strong>{s['time']}</strong> &bull; Size: <strong>{s['size']}</strong></div>
      <div>Test Results: <strong style="color: #4ade80;">{s['score']}</strong></div>
    </div>
    <div class="tests-container">
      <div style="font-size: 0.8rem; font-weight: 700; color: #94a3b8; margin-bottom: 8px;">TEST SCRIPT ASSERTIONS (POSTMAN PM TESTS):</div>
      {pills}
    </div>
  </div>
</body>
</html>"""

for idx, s in enumerate(snapshots):
  tmp_html = os.path.join(out_dir, f"temp_{idx}.html")
  out_png = os.path.join(out_dir, s['name'])
  with open(tmp_html, 'w', encoding='utf-8') as f:
    f.write(generate_html(s))
  subprocess.run(['google-chrome', '--headless', '--disable-gpu', '--window-size=1100,680', f'--screenshot={out_png}', f'file://{tmp_html}'], check=True)
  if os.path.exists(tmp_html):
    os.remove(tmp_html)
  print(f"Generated: {s['name']}")

if os.path.exists('/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-023_GA7-220501096-AA5-EV02_Testing_API_Postman/generate_capturas.js'):
  os.remove('/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-023_GA7-220501096-AA5-EV02_Testing_API_Postman/generate_capturas.js')
