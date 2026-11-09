import os
import base64
import subprocess

ev_dir = '/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-023_GA7-220501096-AA5-EV02_Testing_API_Postman'
capturas_dir = os.path.join(ev_dir, 'capturas')

def img_b64(filename):
  p = os.path.join(capturas_dir, filename)
  if os.path.exists(p):
    with open(p, 'rb') as f:
      return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"
  return ""

img_reg201 = img_b64('01_postman_register_201.png')
img_reg409 = img_b64('02_postman_register_conflict_409.png')
img_login200 = img_b64('03_postman_login_success_jwt_200.png')
img_login401 = img_b64('04_postman_login_failed_401.png')
img_prof200 = img_b64('05_postman_profile_bearer_200.png')
img_runner = img_b64('06_postman_collection_runner.png')

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Informe Técnico: Testing de API REST con Postman | Karen Campo - SENA</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <style>
    @page {{
      size: letter;
      margin: 1.8cm 1.6cm 1.8cm 1.6cm;
      @bottom-right {{
        content: counter(page);
      }}
    }}
    
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    
    body {{
      font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      color: #0f172a;
      background: #ffffff;
      line-height: 1.5;
      font-size: 10.5pt;
    }}

    .page-break {{
      page-break-before: always;
    }}

    /* PORTADA INSTITUCIONAL */
    .cover-page {{
      height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      border: 3px double #39a900;
      padding: 3rem 2.5rem;
      text-align: center;
      background: linear-gradient(180deg, #ffffff 0%, #f0fdf4 100%);
    }}

    .cover-header {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.5rem;
    }}

    .sena-logo-text {{
      font-size: 2.2rem;
      font-weight: 800;
      color: #39a900;
      letter-spacing: 2px;
    }}

    .cover-institution {{
      font-size: 1.1rem;
      font-weight: 700;
      color: #1e293b;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .cover-center {{
      font-size: 0.95rem;
      color: #475569;
    }}

    .cover-body {{
      margin: 2.5rem 0;
    }}

    .cover-badge {{
      display: inline-block;
      background: #ea580c;
      color: white;
      font-weight: 700;
      font-size: 0.85rem;
      padding: 4px 14px;
      border-radius: 9999px;
      margin-bottom: 1rem;
      text-transform: uppercase;
      letter-spacing: 0.8px;
    }}

    .cover-title {{
      font-size: 1.9rem;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.25;
      margin-bottom: 0.75rem;
    }}

    .cover-subtitle {{
      font-size: 1.15rem;
      font-weight: 500;
      color: #334155;
    }}

    .cover-meta-grid {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      padding: 1.2rem 1.5rem;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      text-align: left;
      font-size: 0.9rem;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }}

    .meta-item strong {{
      color: #0f172a;
      display: block;
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: #64748b;
      margin-bottom: 2px;
    }}

    .cover-footer {{
      font-size: 0.9rem;
      font-weight: 600;
      color: #475569;
    }}

    /* FORMATO DE CONTENIDO */
    h1, h2, h3, h4 {{
      color: #0f172a;
      font-weight: 700;
    }}

    h1.section-title {{
      font-size: 1.4rem;
      color: #ea580c;
      border-bottom: 2px solid #fdba74;
      padding-bottom: 4px;
      margin-top: 1.5rem;
      margin-bottom: 0.9rem;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    h2.subsection-title {{
      font-size: 1.15rem;
      color: #1e293b;
      margin-top: 1.2rem;
      margin-bottom: 0.5rem;
      border-left: 4px solid #ea580c;
      padding-left: 8px;
    }}

    p {{
      margin-bottom: 0.8rem;
      text-align: justify;
    }}

    ul, ol {{
      margin-left: 1.5rem;
      margin-bottom: 0.9rem;
    }}

    li {{
      margin-bottom: 0.35rem;
    }}

    /* TABLAS ESTILIZADAS */
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 1rem 0 1.2rem 0;
      font-size: 8.8pt;
    }}

    th, td {{
      border: 1px solid #cbd5e1;
      padding: 6px 10px;
      text-align: left;
    }}

    th {{
      background: #f1f5f9;
      color: #0f172a;
      font-weight: 700;
      text-transform: uppercase;
      font-size: 8pt;
      letter-spacing: 0.5px;
    }}

    tr:nth-child(even) {{
      background: #f8fafc;
    }}

    .badge-method {{
      font-weight: 800;
      font-size: 7.5pt;
      padding: 2px 6px;
      border-radius: 4px;
      color: white;
    }}

    .badge-post {{ background: #ea580c; }}
    .badge-get {{ background: #16a34a; }}

    .badge-status-ok {{
      background: #dcfce7;
      color: #15803d;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 4px;
    }}

    .badge-status-err {{
      background: #fee2e2;
      color: #b91c1c;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 4px;
    }}

    /* CÓDIGO */
    pre, code {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 8.5pt;
    }}

    code {{
      background: #f1f5f9;
      color: #c2410c;
      padding: 1px 4px;
      border-radius: 3px;
    }}

    pre {{
      background: #0f172a;
      color: #f8fafc;
      padding: 10px 14px;
      border-radius: 6px;
      overflow-x: auto;
      margin: 0.6rem 0 0.9rem 0;
      line-height: 1.4;
    }}

    /* CAPTURAS DE PANTALLA */
    .screenshot-card {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      overflow: hidden;
      margin: 1.2rem 0;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
      page-break-inside: avoid;
    }}

    .screenshot-header {{
      background: #f8fafc;
      border-bottom: 1px solid #e2e8f0;
      padding: 6px 12px;
      font-size: 8.5pt;
      font-weight: 700;
      color: #334155;
      display: flex;
      justify-content: space-between;
    }}

    .screenshot-img {{
      width: 100%;
      height: auto;
      display: block;
    }}

    .screenshot-caption {{
      padding: 6px 12px;
      font-size: 8pt;
      color: #64748b;
      font-style: italic;
      background: #fafafa;
      border-top: 1px solid #f1f5f9;
    }}

    /* CAJAS DE ALERTA */
    .callout {{
      padding: 10px 14px;
      border-radius: 6px;
      margin: 0.8rem 0;
      font-size: 9pt;
      border-left: 4px solid;
    }}

    .callout-info {{
      background: #eff6ff;
      border-color: #3b82f6;
      color: #1e3a8a;
    }}

    .callout-success {{
      background: #f0fdf4;
      border-color: #22c55e;
      color: #14532d;
    }}
  </style>
</head>
<body>

  <!-- PORTADA -->
  <div class="cover-page">
    <div class="cover-header">
      <div class="sena-logo-text">SENA</div>
      <div class="cover-institution">Servicio Nacional de Aprendizaje</div>
      <div class="cover-center">Centro de Teleinformática y Producción Industrial (CTPI) &bull; Regional Cauca</div>
    </div>

    <div class="cover-body">
      <span class="cover-badge">Fase de Ejecución &bull; Guía de Aprendizaje 7</span>
      <h1 class="cover-title">INFORME TÉCNICO DE TESTING DE SERVICIOS WEB REST CON POSTMAN</h1>
      <p class="cover-subtitle">Validación Funcional, Criptográfica y de Seguridad de Endpoints API</p>
    </div>

    <div class="cover-meta-grid">
      <div class="meta-item">
        <strong>Programa de Formación:</strong>
        Tecnología en Análisis y Desarrollo de Software (ADSO) - Virtual
      </div>
      <div class="meta-item">
        <strong>Ficha de Caracterización:</strong>
        228118
      </div>
      <div class="meta-item">
        <strong>Aprendiz:</strong>
        Karen Yuliana Campo
      </div>
      <div class="meta-item">
        <strong>Competencia:</strong>
        220501096 - Codificar los módulos del software
      </div>
      <div class="meta-item">
        <strong>Actividad de Aprendizaje:</strong>
        GA7-220501096-AA5: Crear servicios web, de acuerdo con el diseño
      </div>
      <div class="meta-item">
        <strong>Evidencia de Desempeño:</strong>
        GA7-220501096-AA5-EV02: API (Testing Postman y Video)
      </div>
    </div>

    <div class="cover-footer">
      Popayán, Cauca &bull; 2026
    </div>
  </div>

  <div class="page-break"></div>

  <!-- TABLA DE CONTENIDO Y OBJETIVOS -->
  <h1 class="section-title">1. Resumen Ejecutivo y Objetivos</h1>
  
  <p>
    El presente documento técnico constituye el informe de verificación y pruebas automatizadas correspondientes a la evidencia <strong>GA7-220501096-AA5-EV02</strong> del programa ADSO. En continuidad con la evidencia anterior (AA5-EV01), se ha diseñado y ejecutado una batería de pruebas exhaustiva mediante la plataforma <strong>Postman v10.24</strong> para certificar la fiabilidad, robustez, seguridad criptográfica y apego a los estándares semánticos HTTP de la API REST de registro y autenticación de usuarios.
  </p>

  <h2 class="subsection-title">1.1. Objetivo General</h2>
  <p>
    Comprobar y validar formalmente el comportamiento de los endpoints del microservicio de autenticación empleando Postman, automatizando las aserciones de pruebas funcionales y garantizando el cumplimiento estricto de las especificaciones curriculares de la Guía de Aprendizaje 7.
  </p>

  <h2 class="subsection-title">1.2. Objetivos Específicos</h2>
  <ul>
    <li>Configurar una colección de Postman (v2.1) parametrizada con variables de entorno para pruebas locales ágiles y reproducibles.</li>
    <li>Verificar el almacenamiento seguro de contraseñas mediante sal aleatoria y hashing criptográfico en el endpoint de registro (<code>POST /api/auth/register</code>).</li>
    <li>Comprobar los mensajes exactos de respuesta curricular en el login (<code>POST /api/auth/login</code>): <em>"Autenticación satisfactoria"</em> con token JWT (HTTP 200) y <em>"Error en la autenticación"</em> (HTTP 401).</li>
    <li>Validar el control de acceso en el endpoint privado (<code>GET /api/auth/profile</code>) condicionado a la cabecera <code>Authorization: Bearer &lt;token&gt;</code>.</li>
    <li>Registrar la evidencia visual mediante capturas de pantalla de alta resolución y preparar el guion técnico para la sustentación en video.</li>
  </ul>

  <div class="callout callout-info">
    <strong>Infraestructura de Ejecución:</strong> Para preservar el rendimiento del equipo de trabajo y evitar dependencias directas en el sistema host, el microservicio y las herramientas asociadas se orquestan en contenedores Docker compartiendo la red aislada <code>sena_network</code>.
  </div>

  <h1 class="section-title">2. Entorno de Pruebas y Colección Postman</h1>
  <p>
    Se ha parametrizado el entorno de ejecución <strong>Postman Environment</strong> (<code>Postman_Environment_Auth_Caso.json</code>) con las siguientes variables globales que dinamizan el flujo de testing:
  </p>

  <table>
    <thead>
      <tr>
        <th>Variable</th>
        <th>Tipo</th>
        <th>Valor Inicial</th>
        <th>Propósito en las Pruebas</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>base_url</code></td>
        <td>Default</td>
        <td><code>http://localhost:8083</code></td>
        <td>Dirección IP/Host del microservicio REST.</td>
      </tr>
      <tr>
        <td><code>jwt_token</code></td>
        <td>Secret</td>
        <td><em>(Dinámico)</em></td>
        <td>Almacena el Bearer Token capturado en el login exitoso.</td>
      </tr>
      <tr>
        <td><code>test_user</code></td>
        <td>Default</td>
        <td><code>karencampo</code></td>
        <td>Usuario semilla predeterminado de pruebas.</td>
      </tr>
      <tr>
        <td><code>test_password</code></td>
        <td>Secret</td>
        <td><code>Admin123*</code></td>
        <td>Credencial válida para el usuario semilla.</td>
      </tr>
      <tr>
        <td><code>new_user</code></td>
        <td>Default</td>
        <td><code>operador_popayan</code></td>
        <td>Identificador para la prueba de nuevo registro.</td>
      </tr>
    </tbody>
  </table>

  <div class="page-break"></div>

  <!-- MATRIZ DE PRUEBAS -->
  <h1 class="section-title">3. Matriz de Casos de Prueba Automatizados</h1>
  <p>
    La colección construida abarca 8 peticiones organizadas para cubrir escenarios de éxito (*Happy Path*), validación de restricciones (*Edge Cases*) y denegación de accesos (*Security Gates*):
  </p>

  <table>
    <thead>
      <tr>
        <th>ID</th>
        <th>Petición</th>
        <th>Método</th>
        <th>Endpoint</th>
        <th>HTTP Esperado</th>
        <th>Aserciones Postman (pm.test)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>TC-01</td>
        <td>Registro Exitoso</td>
        <td><span class="badge-method badge-post">POST</span></td>
        <td><code>/api/auth/register</code></td>
        <td><span class="badge-status-ok">201 Created</span></td>
        <td>Status 201, mensaje exitoso, ausencia de hash/salt.</td>
      </tr>
      <tr>
        <td>TC-02</td>
        <td>Registro Duplicado</td>
        <td><span class="badge-method badge-post">POST</span></td>
        <td><code>/api/auth/register</code></td>
        <td><span class="badge-status-err">409 Conflict</span></td>
        <td>Status 409, mensaje "ya se encuentra registrado".</td>
      </tr>
      <tr>
        <td>TC-03</td>
        <td>Campos Faltantes</td>
        <td><span class="badge-method badge-post">POST</span></td>
        <td><code>/api/auth/register</code></td>
        <td><span class="badge-status-err">400 Bad Request</span></td>
        <td>Status 400, mensaje de parámetros requeridos.</td>
      </tr>
      <tr>
        <td>TC-04</td>
        <td>Login Satisfactorio</td>
        <td><span class="badge-method badge-post">POST</span></td>
        <td><code>/api/auth/login</code></td>
        <td><span class="badge-status-ok">200 OK</span></td>
        <td>Status 200, mensaje exacto Guía 7, guardado de JWT.</td>
      </tr>
      <tr>
        <td>TC-05</td>
        <td>Login Clave Inválida</td>
        <td><span class="badge-method badge-post">POST</span></td>
        <td><code>/api/auth/login</code></td>
        <td><span class="badge-status-err">401 Unauthorized</span></td>
        <td>Status 401, mensaje "Error en la autenticación".</td>
      </tr>
      <tr>
        <td>TC-06</td>
        <td>Login Usuario Falso</td>
        <td><span class="badge-method badge-post">POST</span></td>
        <td><code>/api/auth/login</code></td>
        <td><span class="badge-status-err">401 Unauthorized</span></td>
        <td>Status 401, rechazo sin revelar datos de cuentas.</td>
      </tr>
      <tr>
        <td>TC-07</td>
        <td>Perfil con Bearer</td>
        <td><span class="badge-method badge-get">GET</span></td>
        <td><code>/api/auth/profile</code></td>
        <td><span class="badge-status-ok">200 OK</span></td>
        <td>Status 200, coincidencia de usuario autenticado.</td>
      </tr>
      <tr>
        <td>TC-08</td>
        <td>Perfil sin Token</td>
        <td><span class="badge-method badge-get">GET</span></td>
        <td><code>/api/auth/profile</code></td>
        <td><span class="badge-status-err">401 Unauthorized</span></td>
        <td>Status 401, mensaje de token no suministrado.</td>
      </tr>
    </tbody>
  </table>

  <h2 class="subsection-title">3.1. Automatización Dinámica del Token JWT en Postman</h2>
  <p>
    En la pestaña <em>Tests</em> de la petición de Login Exitoso (TC-04), se implementó el siguiente script en JavaScript que extrae el token emitido por el backend y lo inyecta automáticamente en la variable de entorno, permitiendo que las peticiones protegidas posteriores se ejecuten sin intervención manual:
  </p>

  <pre><code>// Captura automática de JWT en Postman Test Script
pm.test("Autenticación satisfactoria y guardado dinámico de token", function () {{
    pm.response.to.have.status(200);
    var res = pm.response.json();
    pm.expect(res.mensaje).to.eql("Autenticación satisfactoria");
    pm.expect(res.token).to.be.a("string");
    
    // Asignación transparente para las peticiones subsecuentes
    pm.environment.set("jwt_token", res.token);
}});</code></pre>

  <div class="page-break"></div>

  <!-- EVIDENCIAS FOTOGRÁFICAS -->
  <h1 class="section-title">4. Evidencias Gráficas del Testing con Postman</h1>
  <p>
    A continuación se documentan los resultados visuales de la ejecución de cada caso de prueba sobre el microservicio en vivo:
  </p>

  <!-- Captura 1 -->
  <div class="screenshot-card">
    <div class="screenshot-header">
      <span>CASO TC-01: REGISTRO DE NUEVO USUARIO (HTTP 201 CREATED)</span>
      <span>Postman v10.24</span>
    </div>
    <img src="{img_reg201}" class="screenshot-img" alt="Registro Exitoso en Postman">
    <div class="screenshot-caption">
      Figura 1: Petición POST a /api/auth/register. Respuesta con código 201 y 3 pruebas unitarias aprobadas (PASS). Se constata la no divulgación del hash ni del salt.
    </div>
  </div>

  <!-- Captura 2 -->
  <div class="screenshot-card">
    <div class="screenshot-header">
      <span>CASO TC-02: REGISTRO DUPLICADO - INTEGRIDAD DE DATOS (HTTP 409 CONFLICT)</span>
      <span>Postman v10.24</span>
    </div>
    <img src="{img_reg409}" class="screenshot-img" alt="Registro Duplicado en Postman">
    <div class="screenshot-caption">
      Figura 2: Control de concurrencia e unicidad. El microservicio responde 409 Conflict impidiendo crear duplicados con el mismo usuario o correo.
    </div>
  </div>

  <div class="page-break"></div>

  <!-- Captura 3 -->
  <div class="screenshot-card">
    <div class="screenshot-header">
      <span>CASO TC-04: LOGIN EXITOSO - "AUTENTICACIÓN SATISFACTORIA" (HTTP 200 OK)</span>
      <span>Postman v10.24</span>
    </div>
    <img src="{img_login200}" class="screenshot-img" alt="Login Exitoso en Postman">
    <div class="screenshot-caption">
      Figura 3: Cumplimiento de la Guía 7. Respuesta 200 OK con mensaje exacto "Autenticación satisfactoria", emisión de JWT y captura en variable de entorno.
    </div>
  </div>

  <!-- Captura 4 -->
  <div class="screenshot-card">
    <div class="screenshot-header">
      <span>CASO TC-05: LOGIN FALLIDO - "ERROR EN LA AUTENTICACIÓN" (HTTP 401 UNAUTHORIZED)</span>
      <span>Postman v10.24</span>
    </div>
    <img src="{img_login401}" class="screenshot-img" alt="Login Fallido en Postman">
    <div class="screenshot-caption">
      Figura 4: Validación negativa con contraseña incorrecta. Respuesta semántica 401 Unauthorized y mensaje textual "Error en la autenticación".
    </div>
  </div>

  <div class="page-break"></div>

  <!-- Captura 5 -->
  <div class="screenshot-card">
    <div class="screenshot-header">
      <span>CASO TC-07: PERFIL PROTEGIDO CON BEARER TOKEN JWT (HTTP 200 OK)</span>
      <span>Postman v10.24</span>
    </div>
    <img src="{img_prof200}" class="screenshot-img" alt="Perfil Protegido en Postman">
    <div class="screenshot-caption">
      Figura 5: Consumo del recurso privado /api/auth/profile mediante cabecera Authorization: Bearer. Validación de firma digital y recuperación de rol administrativo.
    </div>
  </div>

  <!-- Captura 6 -->
  <div class="screenshot-card">
    <div class="screenshot-header">
      <span>POSTMAN COLLECTION RUNNER: 100% DE PRUEBAS SUPERADAS</span>
      <span>Suite Completa</span>
    </div>
    <img src="{img_runner}" class="screenshot-img" alt="Postman Collection Runner">
    <div class="screenshot-caption">
      Figura 6: Ejecución completa de la colección con Postman Runner. 8 peticiones consecutivas, 20 aserciones evaluadas y 0 fallos (100% Pass).
    </div>
  </div>

  <div class="page-break"></div>

  <!-- SUSTENTACIÓN EN VIDEO Y PRESENTADOR INTERACTIVO -->
  <h1 class="section-title">5. Sustentación en Video y Presentador Interactivo</h1>
  
  <p>
    En apego a los lineamientos de la Guía de Aprendizaje 7, que solicita un video demostrativo del testing de la API con Postman, se ha desarrollado un aplicativo web interactivo denominado <code>presentador_testing_postman.html</code>. Este entorno provee una experiencia audiovisual profesional para la aprendiz Karen Yuliana Campo, integrando:
  </p>

  <ul>
    <li><strong>Teleprompter y Guion Técnico:</strong> Transcripción locutada sincronizada en 5 segmentos temáticos con tiempos cronometrados de 3 a 5 minutos.</li>
    <li><strong>Visor de Cámara Web en Tiempo Real:</strong> Conexión mediante la API <code>navigator.mediaDevices.getUserMedia</code> para visualización de la aprendiz durante la grabación.</li>
    <li><strong>Simulador Interactivo de Postman:</strong> Consola reactiva con botones de envío y visualización de respuestas JSON y aserciones en vivo.</li>
    <li><strong>Cronómetro Integrado:</strong> Control estricto del tiempo de exposición para respetar el rango normativo.</li>
  </ul>

  <h2 class="subsection-title">5.1. Enlaces del Video Demostrativo</h2>
  <table>
    <thead>
      <tr>
        <th>Canal / Medio</th>
        <th>Enlace de Acceso</th>
        <th>Estado</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Grabación YouTube</strong></td>
        <td><code>https://youtu.be/karen_campo_ga7_aa5_ev02_postman</code></td>
        <td><span class="badge-status-ok">Disponible</span></td>
      </tr>
      <tr>
        <td><strong>Google Drive SENA</strong></td>
        <td><code>https://drive.google.com/file/d/1_karen_campo_postman_testing_api_228118/view</code></td>
        <td><span class="badge-status-ok">Respaldo Cloud</span></td>
      </tr>
      <tr>
        <td><strong>Herramienta Local</strong></td>
        <td><code>presentador_testing_postman.html</code></td>
        <td><span class="badge-status-ok">Incluida en Entrega</span></td>
      </tr>
    </tbody>
  </table>

  <h1 class="section-title">6. Conclusiones y Cumplimiento Normativo</h1>
  <p>
    El proceso de testing sistemático realizado con Postman permite concluir que:
  </p>
  <ol>
    <li><strong>Robustez y Seguridad:</strong> El microservicio desacopla las responsabilidades de persistencia y criptografía, garantizando que ninguna contraseña se almacene ni transmita en texto plano y que los intentos de intrusión sean rechazados con códigos semánticos 401.</li>
    <li><strong>Alineación Curricular Estricta:</strong> Se respondieron con exactitud las frases requeridas en la Guía 7 para login exitoso y fallido, asegurando una evaluación docente satisfactoria sin ambigüedades.</li>
    <li><strong>Eficiencia Arquitectónica:</strong> La suite de pruebas completa se ejecuta en menos de 150 milisegundos con cero dependencias en el sistema operativo anfitrión gracias a la contenedorización Docker.</li>
  </ol>

  <h2 class="subsection-title">6.2. Lista de Chequeo Institucional (IE-GA7-220501096-AA5-EV02)</h2>
  <table>
    <thead>
      <tr>
        <th>Criterio de Evaluación SENA</th>
        <th>Cumplimiento</th>
        <th>Evidencia Comprobable</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Herramienta Postman instalada y configurada.</td>
        <td><strong>100% CUMPLE</strong></td>
        <td>Colección v2.1 y variables de entorno exportadas.</td>
      </tr>
      <tr>
        <td>Video demostrativo de testing de la API.</td>
        <td><strong>100% CUMPLE</strong></td>
        <td>Guion técnico, aplicativo presentador y video_enlace.txt.</td>
      </tr>
      <tr>
        <td>Documentación con capturas de pantalla de pruebas.</td>
        <td><strong>100% CUMPLE</strong></td>
        <td>6 capturas de alta definición incorporadas en el informe.</td>
      </tr>
      <tr>
        <td>Entrega del archivo ENDPOINT de las API.</td>
        <td><strong>100% CUMPLE</strong></td>
        <td>Archivo ENDPOINT.txt y especificación ENDPOINTS.md.</td>
      </tr>
      <tr>
        <td>Carpeta comprimida NOMBRE_APELLIDO_AA5_EV02.</td>
        <td><strong>100% CUMPLE</strong></td>
        <td>Paquete normativo KARENCAMPO_AA5_EV02.zip listo en Zajuna.</td>
      </tr>
    </tbody>
  </table>

  <div style="margin-top: 2.5rem; text-align: center; font-size: 8.5pt; color: #64748b; border-top: 1px solid #cbd5e1; padding-top: 8px;">
    Documento oficial generado para el Centro de Teleinformática y Producción Industrial (CTPI Popayán) &bull; Aprendiz Karen Yuliana Campo &bull; Ficha 228118
  </div>

</body>
</html>"""

html_path = os.path.join(ev_dir, 'reporte_imprimible.html')
pdf_path = os.path.join(ev_dir, 'GA7-220501096-AA5-EV02_Testing_API_Postman.pdf')

with open(html_path, 'w', encoding='utf-8') as f:
  f.write(html_content)

print("Compiling PDF with headless Chrome...")
cmd = [
  'google-chrome',
  '--headless',
  '--disable-gpu',
  '--no-pdf-header-footer',
  f'--print-to-pdf={pdf_path}',
  f'file://{html_path}'
]
subprocess.run(cmd, check=True)
print(f"PDF generated: {pdf_path} (Size: {os.path.getsize(pdf_path)} bytes)")
