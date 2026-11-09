<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="com.sena.pizzeria.model.Cliente" %>
<%@ page import="com.sena.pizzeria.dao.ClienteDAO" %>
<%@ page import="java.util.List" %>
<%
    List<Cliente> clientes = (List<Cliente>) request.getAttribute("clientes");
    if (clientes == null) {
        ClienteDAO dao = new ClienteDAO();
        clientes = dao.listarTodos();
    }
    Cliente clienteEditar = (Cliente) request.getAttribute("clienteEditar");
%>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pizzería Bella Italia | Directorio de Clientes</title>
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
            <li><a href="clientes" class="active">Clientes</a></li>
            <li><a href="pizzas">Catálogo de Pizzas</a></li>
            <li><a href="pedidos">Gestión de Pedidos</a></li>
        </ul>
    </nav>

    <!-- Contenedor -->
    <main class="container">
        
        <!-- Mensajes de Notificación -->
        <% if (request.getParameter("mensaje") != null) { %>
            <div class="alert alert-success">
                <span>✓</span> <strong>¡Operación exitosa!</strong> El cliente ha sido registrado/actualizado en la base de datos.
            </div>
        <% } %>

        <% if (request.getParameter("eliminado") != null) { %>
            <div class="alert alert-success">
                <span>✓</span> <strong>¡Eliminado!</strong> El cliente ha sido removido del sistema.
            </div>
        <% } %>

        <% if (request.getAttribute("error") != null) { %>
            <div class="alert alert-error">
                <span>⚠</span> <%= request.getAttribute("error") %>
            </div>
        <% } %>

        <!-- Formulario HTML de Registro / Edición con POST -->
        <div class="card">
            <h2 class="card-title">
                <%= (clienteEditar != null) ? "✏ Modificar Datos de Cliente" : "➕ Registrar Nuevo Cliente" %>
            </h2>
            <p class="card-subtitle">
                Los datos se envían mediante una petición <strong>HTTP POST</strong> procesada por <code>ClienteServlet</code> hacia la base de datos MariaDB.
            </p>

            <form action="clientes" method="post">
                <input type="hidden" name="idCliente" value="<%= (clienteEditar != null) ? clienteEditar.getIdCliente() : "0" %>">

                <div class="form-grid">
                    <div class="form-group">
                        <label for="nombre">Nombre Completo:</label>
                        <input type="text" id="nombre" name="nombre" class="form-control" required
                               placeholder="Ej: Carlos Mendoza"
                               value="<%= (clienteEditar != null) ? clienteEditar.getNombre() : "" %>">
                    </div>

                    <div class="form-group">
                        <label for="telefono">Teléfono / WhatsApp:</label>
                        <input type="tel" id="telefono" name="telefono" class="form-control" required
                               placeholder="Ej: 3101234567"
                               value="<%= (clienteEditar != null) ? clienteEditar.getTelefono() : "" %>">
                    </div>

                    <div class="form-group">
                        <label for="direccion">Dirección de Entrega:</label>
                        <input type="text" id="direccion" name="direccion" class="form-control" required
                               placeholder="Ej: Calle 12 # 34-56, Popayán"
                               value="<%= (clienteEditar != null) ? clienteEditar.getDireccion() : "" %>">
                    </div>
                </div>

                <div style="display: flex; gap: 10px; margin-top: 10px;">
                    <button type="submit" class="btn btn-primary">
                        <%= (clienteEditar != null) ? "Actualizar Cliente" : "Guardar Cliente" %>
                    </button>
                    <% if (clienteEditar != null) { %>
                        <a href="clientes" class="btn btn-secondary">Cancelar Edición</a>
                    <% } %>
                </div>
            </form>
        </div>

        <!-- Tabla de Clientes Registrados -->
        <div class="card">
            <h2 class="card-title">📋 Directorio General de Clientes (<%= clientes.size() %>)</h2>
            <p class="card-subtitle">Listado recuperado en tiempo real desde la tabla <code>CLIENTES</code> mediante <code>ClienteDAO</code>.</p>

            <div style="overflow-x: auto;">
                <table class="table">
                    <thead>
                        <tr>
                            <th style="width: 80px;">ID</th>
                            <th>Nombre Completo</th>
                            <th>Teléfono</th>
                            <th>Dirección de Entrega</th>
                            <th style="width: 180px; text-align: center;">Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        <% if (clientes.isEmpty()) { %>
                            <tr>
                                <td colspan="5" style="text-align: center; color: var(--muted); padding: 24px;">
                                    No hay clientes registrados en la base de datos.
                                </td>
                            </tr>
                        <% } else { %>
                            <% for (Cliente c : clientes) { %>
                                <tr>
                                    <td><span class="badge badge-blue">#<%= c.getIdCliente() %></span></td>
                                    <td><strong><%= c.getNombre() %></strong></td>
                                    <td><%= c.getTelefono() %></td>
                                    <td><%= c.getDireccion() %></td>
                                    <td style="text-align: center;">
                                        <a href="clientes?action=editar&id=<%= c.getIdCliente() %>" class="btn btn-secondary btn-sm">Editar</a>
                                        <a href="clientes?action=eliminar&id=<%= c.getIdCliente() %>" 
                                           onclick="return confirm('¿Está seguro de eliminar a este cliente?');"
                                           class="btn btn-danger btn-sm">Eliminar</a>
                                    </td>
                                </tr>
                            <% } %>
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
