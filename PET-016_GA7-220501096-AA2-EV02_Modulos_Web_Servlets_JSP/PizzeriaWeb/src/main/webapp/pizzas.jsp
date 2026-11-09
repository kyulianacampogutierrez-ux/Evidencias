<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="com.sena.pizzeria.model.Pizza" %>
<%@ page import="com.sena.pizzeria.dao.PizzaDAO" %>
<%@ page import="java.util.List" %>
<%
    List<Pizza> pizzas = (List<Pizza>) request.getAttribute("pizzas");
    if (pizzas == null) {
        PizzaDAO dao = new PizzaDAO();
        pizzas = dao.listarTodas();
    }
%>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pizzería Bella Italia | Catálogo de Pizzas</title>
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
            <li><a href="pizzas" class="active">Catálogo de Pizzas</a></li>
            <li><a href="pedidos">Gestión de Pedidos</a></li>
        </ul>
    </nav>

    <!-- Contenedor -->
    <main class="container">
        
        <!-- Notificaciones -->
        <% if (request.getParameter("guardado") != null) { %>
            <div class="alert alert-success">
                <span>✓</span> <strong>¡Especialidad guardada!</strong> La pizza ha sido registrada en el catálogo.
            </div>
        <% } %>

        <% if (request.getParameter("eliminado") != null) { %>
            <div class="alert alert-success">
                <span>✓</span> <strong>¡Eliminado!</strong> La pizza ha sido removida del catálogo.
            </div>
        <% } %>

        <!-- Formulario para Añadir Nueva Especialidad con POST -->
        <div class="card">
            <h2 class="card-title">🍕 Nueva Especialidad de Pizza</h2>
            <p class="card-subtitle">
                Los datos se envían mediante una petición <strong>HTTP POST</strong> procesada por <code>PizzaServlet</code> hacia la tabla <code>PIZZAS</code>.
            </p>

            <form action="pizzas" method="post">
                <input type="hidden" name="idPizza" value="0">

                <div class="form-grid">
                    <div class="form-group">
                        <label for="nombrePizza">Nombre de la Especialidad:</label>
                        <input type="text" id="nombrePizza" name="nombrePizza" class="form-control" required
                               placeholder="Ej: Pizza Cuatro Quesos Gourmet">
                    </div>

                    <div class="form-group">
                        <label for="tamaño">Tamaño de Presentación:</label>
                        <select id="tamaño" name="tamaño" class="form-control" required>
                            <option value="Personal">Personal (4 Porciones)</option>
                            <option value="Mediana" selected>Mediana (8 Porciones)</option>
                            <option value="Grande">Grande (10 Porciones)</option>
                            <option value="Familiar">Familiar (12 Porciones)</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label for="precio">Precio Unitario ($ COP):</label>
                        <input type="number" id="precio" name="precio" step="500" min="10000" class="form-control" required
                               placeholder="Ej: 42000">
                    </div>
                </div>

                <button type="submit" class="btn btn-primary">Añadir al Catálogo</button>
            </form>
        </div>

        <!-- Catálogo de Pizzas Disponibles -->
        <div class="card">
            <h2 class="card-title">📜 Menú Oficial de Pizzas (<%= pizzas.size() %> Especialidades)</h2>
            <p class="card-subtitle">Productos activos con precios vigentes en el sistema de ventas.</p>

            <div style="overflow-x: auto;">
                <table class="table">
                    <thead>
                        <tr>
                            <th style="width: 80px;">Código</th>
                            <th>Especialidad</th>
                            <th>Tamaño</th>
                            <th>Precio Unitario</th>
                            <th style="width: 120px; text-align: center;">Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        <% for (Pizza p : pizzas) { %>
                            <tr>
                                <td><span class="badge badge-blue">#<%= p.getIdPizza() %></span></td>
                                <td><strong><%= p.getNombrePizza() %></strong></td>
                                <td><span class="badge badge-warning"><%= p.getTamaño() %></span></td>
                                <td><strong>$<%= String.format("%,.2f", p.getPrecio()) %> COP</strong></td>
                                <td style="text-align: center;">
                                    <a href="pizzas?action=eliminar&id=<%= p.getIdPizza() %>" 
                                       onclick="return confirm('¿Desea retirar esta pizza del catálogo?');"
                                       class="btn btn-danger btn-sm">Eliminar</a>
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
