<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="com.sena.pizzeria.model.Pedido" %>
<%@ page import="com.sena.pizzeria.model.Cliente" %>
<%@ page import="com.sena.pizzeria.model.Pizza" %>
<%@ page import="com.sena.pizzeria.dao.PedidoDAO" %>
<%@ page import="com.sena.pizzeria.dao.ClienteDAO" %>
<%@ page import="com.sena.pizzeria.dao.PizzaDAO" %>
<%@ page import="java.util.List" %>
<%
    List<Pedido> pedidos = (List<Pedido>) request.getAttribute("pedidos");
    List<Cliente> clientes = (List<Cliente>) request.getAttribute("clientes");
    List<Pizza> pizzas = (List<Pizza>) request.getAttribute("pizzas");

    if (pedidos == null) {
        pedidos = new PedidoDAO().listarTodos();
    }
    if (clientes == null) {
        clientes = new ClienteDAO().listarTodos();
    }
    if (pizzas == null) {
        pizzas = new PizzaDAO().listarTodas();
    }
%>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pizzería Bella Italia | Gestión de Pedidos</title>
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
            <li><a href="index.jsp">Panel Principal</a></li>
            <li><a href="clientes">Clientes</a></li>
            <li><a href="pizzas">Catálogo de Pizzas</a></li>
            <li><a href="pedidos" class="active">Gestión de Pedidos</a></li>
        </ul>
    </nav>

    <!-- Contenedor -->
    <main class="container">
        
        <!-- Notificaciones -->
        <% if (request.getParameter("creado") != null) { %>
            <div class="alert alert-success">
                <span>✓</span> <strong>¡Pedido creado con éxito!</strong> Transacción atómica completada en <code>PEDIDOS</code> y <code>DETALLE_PEDIDO</code>.
            </div>
        <% } %>

        <% if (request.getParameter("eliminado") != null) { %>
            <div class="alert alert-success">
                <span>✓</span> <strong>¡Pedido eliminado!</strong> Se han purgado los registros en cascada.
            </div>
        <% } %>

        <!-- Formulario de Registro de Pedido con POST -->
        <div class="card">
            <h2 class="card-title">📦 Registrar Nueva Orden de Pedido</h2>
            <p class="card-subtitle">
                Los datos se envían vía <strong>HTTP POST</strong> hacia <code>PedidoServlet</code>, ejecutando una transacción ACID en MariaDB.
            </p>

            <form action="pedidos" method="post">
                <div class="form-grid">
                    <div class="form-group">
                        <label for="idCliente">Seleccionar Cliente:</label>
                        <select id="idCliente" name="idCliente" class="form-control" required>
                            <option value="">-- Seleccione un cliente --</option>
                            <% for (Cliente c : clientes) { %>
                                <option value="<%= c.getIdCliente() %>">
                                    <%= c.getNombre() %> (Tel: <%= c.getTelefono() %>)
                                </option>
                            <% } %>
                        </select>
                    </div>

                    <div class="form-group">
                        <label for="idPizza">Especialidad de Pizza:</label>
                        <select id="idPizza" name="idPizza" class="form-control" required>
                            <option value="">-- Seleccione una pizza --</option>
                            <% for (Pizza p : pizzas) { %>
                                <option value="<%= p.getIdPizza() %>">
                                    <%= p.getNombrePizza() %> - <%= p.getTamaño() %> ($<%= String.format("%,.0f", p.getPrecio()) %> COP)
                                </option>
                            <% } %>
                        </select>
                    </div>

                    <div class="form-group">
                        <label for="cantidad">Cantidad de Unidades:</label>
                        <input type="number" id="cantidad" name="cantidad" value="1" min="1" max="20" class="form-control" required>
                    </div>

                    <div class="form-group">
                        <label for="estado">Estado Inicial:</label>
                        <select id="estado" name="estado" class="form-control" required>
                            <option value="En Preparación" selected>En Preparación</option>
                            <option value="En Horno">En Horno</option>
                            <option value="En Reparto">En Reparto</option>
                            <option value="Entregado">Entregado</option>
                        </select>
                    </div>
                </div>

                <button type="submit" class="btn btn-primary">Registrar Orden de Venta</button>
            </form>
        </div>

        <!-- Tabla de Pedidos Registrados -->
        <div class="card">
            <h2 class="card-title">📋 Registro Histórico de Pedidos (<%= pedidos.size() %> Órdenes)</h2>
            <p class="card-subtitle">Órdenes sincronizadas con la base de datos MariaDB.</p>

            <div style="overflow-x: auto;">
                <table class="table">
                    <thead>
                        <tr>
                            <th style="width: 80px;">No. Orden</th>
                            <th>Fecha y Hora</th>
                            <th>Cliente ID</th>
                            <th>Valor Total</th>
                            <th>Estado Actual</th>
                            <th style="width: 120px; text-align: center;">Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        <% for (Pedido ped : pedidos) { %>
                            <tr>
                                <td><span class="badge badge-blue">#<%= ped.getIdPedido() %></span></td>
                                <td><%= ped.getFecha() != null ? ped.getFecha().toString().replace("T", " ") : "N/D" %></td>
                                <td>Cliente #<%= ped.getIdCliente() %></td>
                                <td><strong>$<%= String.format("%,.2f", ped.getTotal()) %> COP</strong></td>
                                <td>
                                    <% if ("Entregado".equals(ped.getEstado())) { %>
                                        <span class="badge badge-success">Entregado</span>
                                    <% } else { %>
                                        <span class="badge badge-warning"><%= ped.getEstado() %></span>
                                    <% } %>
                                </td>
                                <td style="text-align: center;">
                                    <a href="pedidos?action=eliminar&id=<%= ped.getIdPedido() %>" 
                                       onclick="return confirm('¿Desea anular este pedido?');"
                                       class="btn btn-danger btn-sm">Anular</a>
                                </td>
                            </tr>
                        <% } %>
                    </tbody>
                </table>
            </div>
        </div>

    </main>

    <!-- Pie de Página Institucional -->
    <footer>
        <p>Servicio Nacional de Aprendizaje (SENA) • ADSO Ficha 228118 • Karen Yuliana Campo</p>
    </footer>

</body>
</html>
