<?php
/**
 * ==============================================================================
 * APLICACIÓN WEB DE PRUEBA Y AUDITORÍA DE SERVICIOS EN CLIENTE (APACHE + MYSQL)
 * Evidencia: GA10-220501097-AA5-EV01 - Configuración de Servicios, BD y Software
 * Aprendiz: Karen Yuliana Campo | Ficha: 3186681
 * SENA CTPI Popayán - Regional Cauca | Proyecto: Pizzería Gourmet Bella Italia
 * ==============================================================================
 */

// Configuración de Base de Datos
$db_host = getenv('DB_HOST') ?: 'servidor_mysql';
$db_port = getenv('DB_PORT') ?: '3306';
$db_name = getenv('DB_NAME') ?: 'pizzeria_bella_italia_db';
$db_user = getenv('DB_USER') ?: 'karen_admin';
$db_pass = getenv('DB_PASS') ?: 'SenaPopayan2026!';

$conn_error = null;
$conn = null;
$mysql_version = 'Desconocida';
$pedido_mensaje = null;

try {
    $conn = @new mysqli($db_host, $db_user, $db_pass, $db_name, (int)$db_port);
    if ($conn->connect_error) {
        throw new Exception($conn->connect_error);
    }
    $conn->set_charset("utf8mb4");
    $mysql_version = $conn->server_info;
} catch (Exception $e) {
    $conn_error = $e->getMessage();
}

// Procesar nuevo pedido mediante POST
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['accion']) && $_POST['accion'] === 'crear_pedido') {
    $nombre = trim($_POST['nombre'] ?? '');
    $telefono = trim($_POST['telefono'] ?? '');
    $direccion = trim($_POST['direccion'] ?? '');
    $id_producto = (int)($_POST['id_producto'] ?? 1);

    if (!empty($nombre) && !empty($telefono) && $conn && !$conn_error) {
        // Buscar o crear usuario
        $stmt_user = $conn->prepare("SELECT id_usuario FROM usuarios_clientes WHERE telefono_movil = ?");
        $stmt_user->bind_param("s", $telefono);
        $stmt_user->execute();
        $res_user = $stmt_user->get_result();

        if ($row_user = $res_user->fetch_assoc()) {
            $id_usuario = $row_user['id_usuario'];
        } else {
            $stmt_ins = $conn->prepare("INSERT INTO usuarios_clientes (nombre_completo, telefono_movil, direccion_popayan, email) VALUES (?, ?, ?, ?)");
            $email = strtolower(str_replace(' ', '.', $nombre)) . '@gmail.com';
            $stmt_ins->bind_param("ssss", $nombre, $telefono, $direccion, $email);
            $stmt_ins->execute();
            $id_usuario = $stmt_ins->insert_id;
        }

        // Obtener precio de la pizza
        $stmt_prod = $conn->prepare("SELECT precio_cop, nombre_pizza FROM productos_pizza WHERE id_producto = ?");
        $stmt_prod->bind_param("i", $id_producto);
        $stmt_prod->execute();
        $prod_data = $stmt_prod->get_result()->fetch_assoc();

        if ($prod_data) {
            $subtotal = $prod_data['precio_cop'];
            $impoconsumo = $subtotal * 0.08;
            $total = $subtotal + $impoconsumo;
            $cod_orden = 'ORD-' . date('Ymd') . '-' . rand(100, 999);

            $stmt_ped = $conn->prepare("INSERT INTO pedidos_gourmet (id_usuario, codigo_orden, id_producto, subtotal_cop, impoconsumo_8_cop, total_cop) VALUES (?, ?, ?, ?, ?, ?)");
            $stmt_ped->bind_param("isiddd", $id_usuario, $cod_orden, $id_producto, $subtotal, $impoconsumo, $total);
            $stmt_ped->execute();

            $pedido_mensaje = [
                'tipo' => 'exito',
                'texto' => "¡Pedido transaccional $cod_orden registrado con éxito en MySQL 8.0! Pizza: {$prod_data['nombre_pizza']} | Total Liquidado: $" . number_format($total, 0, ',', '.') . " COP."
            ];
        }
    }
}

// Consultar pizzas activas
$pizzas = [];
if ($conn && !$conn_error) {
    $res = $conn->query("SELECT * FROM productos_pizza ORDER BY id_producto ASC");
    if ($res) {
        while ($row = $res->fetch_assoc()) {
            $pizzas[] = $row;
        }
    }
}

// Consultar pedidos recientes
$pedidos_recientes = [];
if ($conn && !$conn_error) {
    $res_ped = $conn->query("
        SELECT p.codigo_orden, u.nombre_completo, pr.nombre_pizza, p.total_cop, p.estado_orden, p.fecha_pedido
        FROM pedidos_gourmet p
        JOIN usuarios_clientes u ON p.id_usuario = u.id_usuario
        JOIN productos_pizza pr ON p.id_producto = pr.id_producto
        ORDER BY p.id_pedido DESC LIMIT 4
    ");
    if ($res_ped) {
        while ($row = $res_ped->fetch_assoc()) {
            $pedidos_recientes[] = $row;
        }
    }
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pizzería Gourmet Bella Italia Popayán | Despliegue Apache & MySQL en Cliente</title>
  <style>
    :root {
      --primary: #064e3b;
      --secondary: #047857;
      --accent: #b91c1c;
      --gold: #d97706;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text: #0f172a;
      --border: #e2e8f0;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.5;
    }
    header {
      background: linear-gradient(135deg, #064e3b 0%, #047857 50%, #022c22 100%);
      color: #ffffff;
      padding: 24px 20px;
      border-bottom: 5px solid #d97706;
      box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    }
    .header-content {
      max-width: 1200px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 15px;
    }
    .brand h1 { font-size: 24px; font-weight: 800; }
    .brand p { font-size: 13.5px; opacity: 0.92; }
    .header-badges {
      display: flex;
      gap: 10px;
    }
    .badge-pill {
      background: rgba(255,255,255,0.18);
      border: 1px solid rgba(255,255,255,0.3);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 12.5px;
      font-weight: 600;
    }

    .container {
      max-width: 1200px;
      margin: 25px auto;
      padding: 0 20px;
    }

    /* Panel de Estado de Servicios */
    .status-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
      margin-bottom: 25px;
    }
    .status-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 18px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.04);
      border-left: 5px solid #10b981;
    }
    .status-card.error { border-left-color: #ef4444; }
    .status-card h4 {
      font-size: 13px;
      color: #64748b;
      text-transform: uppercase;
      margin-bottom: 6px;
    }
    .status-card .val {
      font-size: 18px;
      font-weight: 700;
      color: #0f172a;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .status-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: #10b981;
      display: inline-block;
    }
    .status-dot.red { background: #ef4444; }

    /* Catálogo Gourmet */
    .section-title {
      font-size: 20px;
      color: var(--primary);
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .pizza-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 20px;
      margin-bottom: 30px;
    }
    .pizza-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 10px;
      overflow: hidden;
      box-shadow: 0 4px 10px rgba(0,0,0,0.05);
      transition: transform 0.2s;
    }
    .pizza-card:hover { transform: translateY(-3px); }
    .pizza-img {
      height: 110px;
      background: #fef3c7;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 48px;
    }
    .pizza-body { padding: 16px; }
    .pizza-title { font-size: 17px; font-weight: 700; color: #0f172a; margin-bottom: 6px; }
    .pizza-desc { font-size: 13px; color: #64748b; min-height: 40px; margin-bottom: 12px; }
    .pizza-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 10px;
      border-top: 1px solid #f1f5f9;
    }
    .pizza-price { font-size: 18px; font-weight: 800; color: var(--secondary); }
    .btn-select {
      background: var(--primary);
      color: #fff;
      border: none;
      padding: 6px 14px;
      border-radius: 6px;
      font-weight: 600;
      cursor: pointer;
    }
    .btn-select:hover { background: var(--secondary); }

    /* Formulario y Tabla */
    .two-cols {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-bottom: 30px;
    }
    @media (max-width: 850px) { .two-cols { grid-template-columns: 1fr; } }
    .box {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.04);
    }
    .form-group { margin-bottom: 14px; }
    .form-group label { display: block; font-size: 13px; font-weight: 600; margin-bottom: 5px; }
    .form-group input, .form-group select {
      width: 100%;
      padding: 9px 12px;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      font-size: 13.5px;
    }
    .btn-submit {
      width: 100%;
      background: #b91c1c;
      color: #fff;
      border: none;
      padding: 12px;
      border-radius: 6px;
      font-size: 15px;
      font-weight: 700;
      cursor: pointer;
    }
    .btn-submit:hover { background: #991b1b; }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 12.5px;
    }
    th, td {
      padding: 9px 10px;
      text-align: left;
      border-bottom: 1px solid #f1f5f9;
    }
    th { background: #f8fafc; font-weight: 700; color: var(--primary); }
    .badge-status {
      display: inline-block;
      padding: 3px 8px;
      border-radius: 12px;
      font-size: 11px;
      font-weight: 600;
      background: #dcfce7;
      color: #166534;
    }

    footer {
      background: #0f172a;
      color: #94a3b8;
      padding: 20px;
      text-align: center;
      font-size: 13px;
      margin-top: 40px;
    }
    footer strong { color: #f8fafc; }
  </style>
</head>
<body>

  <header>
    <div class="header-content">
      <div class="brand">
        <h1>🍕 Pizzería Gourmet Bella Italia Popayán</h1>
        <p>Sistema de Gestión y Despliegue en Servidor Apache 2.4 &amp; Base de Datos MySQL 8.0</p>
      </div>
      <div class="header-badges">
        <span class="badge-pill">SENA CTPI Popayán</span>
        <span class="badge-pill">ADSO Ficha 3186681</span>
        <span class="badge-pill">Karen Yuliana Campo</span>
      </div>
    </div>
  </header>

  <div class="container">

    <!-- Mensaje de alerta / confirmación -->
    <?php if ($pedido_mensaje): ?>
      <div style="background: #dcfce7; border: 1px solid #86efac; color: #14532d; padding: 12px 18px; border-radius: 8px; margin-bottom: 20px; font-weight: 600;">
        <?php echo $pedido_mensaje['texto']; ?>
      </div>
    <?php endif; ?>

    <!-- Panel de Diagnóstico de Salud de los Servicios -->
    <div class="status-grid">
      <div class="status-card">
        <h4>Servidor Web de Aplicaciones</h4>
        <div class="val">
          <span class="status-dot"></span>
          Apache/2.4 (Ubuntu/Debian)
        </div>
        <small style="color: #64748b;">Puerto HTTP: 8090 (Host) | PHP <?php echo phpversion(); ?></small>
      </div>

      <div class="status-card <?php echo $conn_error ? 'error' : ''; ?>">
        <h4>Gestor de Base de Datos</h4>
        <div class="val">
          <span class="status-dot <?php echo $conn_error ? 'red' : ''; ?>"></span>
          <?php echo $conn_error ? 'Error de Conexión' : 'MySQL ' . htmlspecialchars($mysql_version); ?>
        </div>
        <small style="color: #64748b;">Puerto: 3308 | DB: <?php echo htmlspecialchars($db_name); ?></small>
      </div>

      <div class="status-card">
        <h4>Sistema Operativo / Kernel</h4>
        <div class="val">
          <span class="status-dot"></span>
          Linux (Contenedor Aislado)
        </div>
        <small style="color: #64748b;"><?php echo htmlspecialchars(substr(php_uname('s') . ' ' . php_uname('r'), 0, 32)); ?></small>
      </div>

      <div class="status-card">
        <h4>Aislamiento Tecnológico</h4>
        <div class="val">
          <span class="status-dot"></span>
          Docker / Cero Host Pollution
        </div>
        <small style="color: #64748b;">Red Bridge: sena_cliente_red_bridge</small>
      </div>
    </div>

    <!-- Catálogo de Pizzas Gourmet desde MySQL -->
    <h2 class="section-title">🍽️ Catálogo de Pizzas Gourmet (Leído en Tiempo Real de MySQL)</h2>
    <div class="pizza-grid">
      <?php if (!empty($pizzas)): ?>
        <?php foreach ($pizzas as $p): ?>
          <div class="pizza-card">
            <div class="pizza-img">🍕</div>
            <div class="pizza-body">
              <div class="pizza-title"><?php echo htmlspecialchars($p['nombre_pizza']); ?></div>
              <div class="pizza-desc"><?php echo htmlspecialchars($p['descripcion_ingredientes']); ?></div>
              <div class="pizza-footer">
                <span class="pizza-price">$<?php echo number_format($p['precio_cop'], 0, ',', '.'); ?> COP</span>
                <button class="btn-select" onclick="seleccionarPizza(<?php echo $p['id_producto']; ?>, '<?php echo addslashes($p['nombre_pizza']); ?>')">Elegir</button>
              </div>
            </div>
          </div>
        <?php endforeach; ?>
      <?php else: ?>
        <p style="color: #64748b;">No hay productos cargados en la base de datos.</p>
      <?php endif; ?>
    </div>

    <!-- Sección de Checkout y Transacciones Recientes -->
    <div class="two-cols">
      <!-- Formulario de Checkout -->
      <div class="box" id="sec-checkout">
        <h3 style="color: var(--primary); margin-bottom: 14px;">🛒 Registrar Pedido Transaccional en MySQL</h3>
        <form method="POST" action="">
          <input type="hidden" name="accion" value="crear_pedido">

          <div class="form-group">
            <label for="id_producto">Especialidad de Pizza Seleccionada:</label>
            <select name="id_producto" id="id_producto" required>
              <?php foreach ($pizzas as $p): ?>
                <option value="<?php echo $p['id_producto']; ?>">
                  <?php echo htmlspecialchars($p['nombre_pizza']); ?> - $<?php echo number_format($p['precio_cop'], 0, ',', '.'); ?> COP
                </option>
              <?php endforeach; ?>
            </select>
          </div>

          <div class="form-group">
            <label for="nombre">Nombre Completo del Cliente:</label>
            <input type="text" id="nombre" name="nombre" required value="Karen Campo" placeholder="Ej. Carlos Martínez">
          </div>

          <div class="form-group">
            <label for="telefono">Teléfono Móvil (MinTIC Colombia):</label>
            <input type="tel" id="telefono" name="telefono" required value="3186681000" placeholder="Ej. 3187654321">
          </div>

          <div class="form-group">
            <label for="direccion">Dirección de Entrega en Popayán:</label>
            <input type="text" id="direccion" name="direccion" required value="Calle 5 # 10-30 Barrio Bolívar" placeholder="Ej. Cra 9 # 4-25 Centro">
          </div>

          <button type="submit" class="btn-submit">Confirmar y Guardar en MySQL</button>
        </form>
      </div>

      <!-- Tabla de Pedidos Persistidos -->
      <div class="box">
        <h3 style="color: var(--primary); margin-bottom: 14px;">📋 Últimas Órdenes Registradas en Servidor</h3>
        <table>
          <thead>
            <tr>
              <th>Código</th>
              <th>Cliente</th>
              <th>Pizza</th>
              <th>Total</th>
              <th>Estado</th>
            </tr>
          </thead>
          <tbody>
            <?php if (!empty($pedidos_recientes)): ?>
              <?php foreach ($pedidos_recientes as $ped): ?>
                <tr>
                  <td><strong><?php echo htmlspecialchars($ped['codigo_orden']); ?></strong></td>
                  <td><?php echo htmlspecialchars($ped['nombre_completo']); ?></td>
                  <td><?php echo htmlspecialchars($ped['nombre_pizza']); ?></td>
                  <td>$<?php echo number_format($ped['total_cop'], 0, ',', '.'); ?></td>
                  <td><span class="badge-status"><?php echo htmlspecialchars($ped['estado_orden']); ?></span></td>
                </tr>
              <?php endforeach; ?>
            <?php else: ?>
              <tr><td colspan="5" style="text-align:center; color: #64748b;">No hay órdenes registradas.</td></tr>
            <?php endif; ?>
          </tbody>
        </table>
        <div style="margin-top: 15px; text-align: right;">
          <a href="info.php" target="_blank" style="font-size: 12px; color: var(--secondary); text-decoration: none; font-weight: 600;">🔗 Ver Configuración de Módulos (phpinfo) &rarr;</a>
        </div>
      </div>
    </div>

  </div>

  <footer>
    <p><strong>Pizzería Gourmet Bella Italia Popayán</strong> • SENA CTPI Popayán - Regional Cauca</p>
    <p>Tecnología en Análisis y Desarrollo de Software (ADSO) • Ficha: 3186681 • Aprendiz: Karen Yuliana Campo</p>
    <p style="margin-top: 6px; font-size: 11.5px; opacity: 0.8;">Evidencia GA10-220501097-AA5-EV01 • Servidor Apache 2.4 &amp; MySQL 8.0 en Linux</p>
  </footer>

  <script>
    function seleccionarPizza(id, nombre) {
      document.getElementById('id_producto').value = id;
      document.getElementById('sec-checkout').scrollIntoView({ behavior: 'smooth' });
    }
  </script>
</body>
</html>
