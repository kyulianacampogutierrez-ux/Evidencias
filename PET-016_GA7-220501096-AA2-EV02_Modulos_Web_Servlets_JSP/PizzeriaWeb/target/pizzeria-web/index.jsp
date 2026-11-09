<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="com.sena.pizzeria.dao.ClienteDAO" %>
<%@ page import="com.sena.pizzeria.dao.PizzaDAO" %>
<%@ page import="com.sena.pizzeria.dao.PedidoDAO" %>
<%
    ClienteDAO clienteDAO = new ClienteDAO();
    PizzaDAO pizzaDAO = new PizzaDAO();
    PedidoDAO pedidoDAO = new PedidoDAO();

    int totalClientes = clienteDAO.listarTodos().size();
    int totalPizzas = pizzaDAO.listarTodas().size();
    int totalPedidos = pedidoDAO.listarTodos().size();
%>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pizzería Bella Italia | Inicio - SENA ADSO</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>

    <!-- Navegación Superior -->
    <nav class="navbar">
        <a href="index.jsp" class="brand">
            <span class="brand-badge">SENA</span>
            <span class="brand-title">🍕 Pizzería Bella Italia</span>
        </a>
        <ul class="nav-links">
            <li><a href="index.jsp" class="active">Panel Principal</a></li>
            <li><a href="clientes">Clientes</a></li>
            <li><a href="pizzas">Catálogo de Pizzas</a></li>
            <li><a href="pedidos">Gestión de Pedidos</a></li>
        </ul>
    </nav>

    <!-- Contenido Principal -->
    <main class="container">
        
        <!-- Tarjeta de Bienvenida Formativa -->
        <div class="card" style="border-left: 6px solid var(--primary); background: linear-gradient(135deg, #FFFFFF 0%, #F0FDF4 100%);">
            <h1 class="card-title">Sistema de Información Web - Pizzería Bella Italia</h1>
            <p class="card-subtitle">
                Arquitectura MVC desarrollada con <strong>Java Servlets</strong>, vistas dinámicas <strong>JSP</strong>, persistencia <strong>JDBC</strong> y motor de base de datos relacional MariaDB/MySQL.
            </p>
            <div style="font-size: 13px; color: var(--muted); display: flex; gap: 24px; flex-wrap: wrap;">
                <span>👤 <strong>Aprendiz:</strong> Karen Yuliana Campo</span>
                <span>🎓 <strong>Programa:</strong> ADSO (Ficha 228118)</span>
                <span>📍 <strong>Regional:</strong> Cauca (Popayán)</span>
                <span>📋 <strong>Evidencia:</strong> GA7-220501096-AA2-EV02</span>
            </div>
        </div>

        <!-- Métricas KPI en Vivo -->
        <div class="kpi-grid">
            <div class="kpi-card">
                <div class="kpi-label">Clientes Registrados</div>
                <div class="kpi-num"><%= totalClientes %></div>
                <p style="font-size: 12px; color: var(--muted); margin-top: 4px;">Acceso vía ClienteServlet & JDBC</p>
            </div>

            <div class="kpi-card blue">
                <div class="kpi-label">Catálogo de Pizzas</div>
                <div class="kpi-num"><%= totalPizzas %></div>
                <p style="font-size: 12px; color: var(--muted); margin-top: 4px;">Especialidades listas para pedido</p>
            </div>

            <div class="kpi-card warning">
                <div class="kpi-label">Pedidos Registrados</div>
                <div class="kpi-num"><%= totalPedidos %></div>
                <p style="font-size: 12px; color: var(--muted); margin-top: 4px;">Transacciones con detalle</p>
            </div>
        </div>

        <!-- Accesos Rápidos a Módulos Web -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
            
            <div class="card">
                <h2 class="card-title">👥 Módulo de Clientes</h2>
                <p class="card-subtitle">Administración completa del directorio de clientes, registro mediante formulario POST y consultas en tiempo real.</p>
                <a href="clientes" class="btn btn-primary">Abrir Módulo de Clientes →</a>
            </div>

            <div class="card">
                <h2 class="card-title">🍕 Catálogo de Productos</h2>
                <p class="card-subtitle">Gestión del menú de pizzas, tamaños (Personal, Mediana, Grande, Familiar) y fijación de precios.</p>
                <a href="pizzas" class="btn btn-primary">Ver Menú de Pizzas →</a>
            </div>

            <div class="card">
                <h2 class="card-title">📦 Flujo de Pedidos</h2>
                <p class="card-subtitle">Generación de órdenes de venta con transacciones atómicas, selección de cliente y cálculo automático de subtotales.</p>
                <a href="pedidos" class="btn btn-primary">Gestionar Pedidos →</a>
            </div>

        </div>

    </main>

    <!-- Pie de Página Institucional -->
    <footer>
        <p>Servicio Nacional de Aprendizaje (SENA) • Centro de Teleinformática y Producción Industrial (CTPI)</p>
        <p style="font-size: 11px; margin-top: 4px;">Análisis y Desarrollo de Software (ADSO) • Popayán, Cauca</p>
    </footer>

</body>
</html>
