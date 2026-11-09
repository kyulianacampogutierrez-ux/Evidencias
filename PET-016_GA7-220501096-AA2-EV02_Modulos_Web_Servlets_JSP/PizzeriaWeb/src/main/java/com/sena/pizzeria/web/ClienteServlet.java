package com.sena.pizzeria.web;

import com.sena.pizzeria.dao.ClienteDAO;
import com.sena.pizzeria.model.Cliente;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.util.List;

/**
 * Controlador Servlet para la gestión de Clientes (Arquitectura MVC).
 * Procesa peticiones HTTP GET y POST para listar, crear, editar y eliminar clientes.
 * 
 * @author Karen Yuliana Campo
 * @version 1.0.0
 */
@WebServlet(name = "ClienteServlet", urlPatterns = {"/clientes"})
public class ClienteServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    private ClienteDAO clienteDAO;

    @Override
    public void init() throws ServletException {
        super.init();
        this.clienteDAO = new ClienteDAO();
    }

    /**
     * Manejo de peticiones GET: Consulta y despacho de vistas JSP.
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String action = request.getParameter("action");
        if (action == null) {
            action = "listar";
        }

        try {
            switch (action) {
                case "eliminar":
                    eliminarCliente(request, response);
                    break;
                case "editar":
                    mostrarFormularioEdicion(request, response);
                    break;
                case "listar":
                default:
                    listarClientes(request, response);
                    break;
            }
        } catch (Exception e) {
            request.setAttribute("error", "Error procesando solicitud: " + e.getMessage());
            listarClientes(request, response);
        }
    }

    /**
     * Manejo de peticiones POST: Procesamiento de formularios HTML (Crear o Actualizar).
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        request.setCharacterEncoding("UTF-8");

        String idStr = request.getParameter("idCliente");
        String nombre = request.getParameter("nombre");
        String telefono = request.getParameter("telefono");
        String direccion = request.getParameter("direccion");

        try {
            if (idStr != null && !idStr.trim().isEmpty() && !idStr.equals("0")) {
                // Actualización de cliente existente
                int idCliente = Integer.parseInt(idStr);
                Cliente cliente = new Cliente(idCliente, nombre, telefono, direccion);
                clienteDAO.actualizar(cliente);
            } else {
                // Creación de nuevo cliente
                Cliente nuevoCliente = new Cliente(nombre, telefono, direccion);
                clienteDAO.insertar(nuevoCliente);
            }
            response.sendRedirect(request.getContextPath() + "/clientes?mensaje=ok");
        } catch (Exception e) {
            request.setAttribute("error", "Error al guardar cliente: " + e.getMessage());
            listarClientes(request, response);
        }
    }

    private void listarClientes(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        List<Cliente> clientes = clienteDAO.listarTodos();
        request.setAttribute("clientes", clientes);
        request.getRequestDispatcher("/clientes.jsp").forward(request, response);
    }

    private void mostrarFormularioEdicion(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        int idCliente = Integer.parseInt(request.getParameter("id"));
        Cliente cliente = clienteDAO.consultarPorId(idCliente);
        request.setAttribute("clienteEditar", cliente);
        listarClientes(request, response);
    }

    private void eliminarCliente(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        int idCliente = Integer.parseInt(request.getParameter("id"));
        clienteDAO.eliminar(idCliente);
        response.sendRedirect(request.getContextPath() + "/clientes?eliminado=ok");
    }
}
