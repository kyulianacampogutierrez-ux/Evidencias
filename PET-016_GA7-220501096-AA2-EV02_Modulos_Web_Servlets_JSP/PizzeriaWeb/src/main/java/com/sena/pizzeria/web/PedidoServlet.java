package com.sena.pizzeria.web;

import com.sena.pizzeria.dao.ClienteDAO;
import com.sena.pizzeria.dao.PedidoDAO;
import com.sena.pizzeria.dao.PizzaDAO;
import com.sena.pizzeria.model.Cliente;
import com.sena.pizzeria.model.DetallePedido;
import com.sena.pizzeria.model.Pedido;
import com.sena.pizzeria.model.Pizza;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.util.List;

/**
 * Controlador Servlet para la creación y despacho de Pedidos (Arquitectura MVC).
 * Procesa peticiones HTTP GET y POST para gestionar órdenes de compra y asociar detalles.
 * 
 * @author Karen Yuliana Campo
 * @version 1.0.0
 */
@WebServlet(name = "PedidoServlet", urlPatterns = {"/pedidos"})
public class PedidoServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    private PedidoDAO pedidoDAO;
    private ClienteDAO clienteDAO;
    private PizzaDAO pizzaDAO;

    @Override
    public void init() throws ServletException {
        super.init();
        this.pedidoDAO = new PedidoDAO();
        this.clienteDAO = new ClienteDAO();
        this.pizzaDAO = new PizzaDAO();
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String action = request.getParameter("action");
        if ("eliminar".equals(action)) {
            try {
                int idPedido = Integer.parseInt(request.getParameter("id"));
                pedidoDAO.eliminar(idPedido);
                response.sendRedirect(request.getContextPath() + "/pedidos?eliminado=ok");
                return;
            } catch (Exception e) {
                request.setAttribute("error", "Error al eliminar pedido: " + e.getMessage());
            }
        }

        cargarVistaPedidos(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        request.setCharacterEncoding("UTF-8");

        try {
            int idCliente = Integer.parseInt(request.getParameter("idCliente"));
            int idPizza = Integer.parseInt(request.getParameter("idPizza"));
            int cantidad = Integer.parseInt(request.getParameter("cantidad"));
            String estado = request.getParameter("estado");
            if (estado == null || estado.trim().isEmpty()) {
                estado = "En Preparación";
            }

            // Consultar precio de la pizza para cálculo de subtotal y total
            Pizza pizza = pizzaDAO.consultarPorId(idPizza);
            if (pizza == null) {
                throw new IllegalArgumentException("Pizza seleccionada no válida");
            }

            double subtotal = pizza.getPrecio() * cantidad;
            double total = subtotal;

            Pedido nuevoPedido = new Pedido(idCliente, total, estado);
            nuevoPedido.agregarDetalle(new DetallePedido(cantidad, subtotal, 0, idPizza));

            boolean registrado = pedidoDAO.registrarPedido(nuevoPedido);
            if (registrado) {
                response.sendRedirect(request.getContextPath() + "/pedidos?creado=ok");
            } else {
                throw new RuntimeException("No se pudo completar la transacción del pedido");
            }

        } catch (Exception e) {
            request.setAttribute("error", "Error al registrar el pedido: " + e.getMessage());
            cargarVistaPedidos(request, response);
        }
    }

    private void cargarVistaPedidos(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        List<Pedido> pedidos = pedidoDAO.listarTodos();
        List<Cliente> clientes = clienteDAO.listarTodos();
        List<Pizza> pizzas = pizzaDAO.listarTodas();

        request.setAttribute("pedidos", pedidos);
        request.setAttribute("clientes", clientes);
        request.setAttribute("pizzas", pizzas);

        request.getRequestDispatcher("/pedidos.jsp").forward(request, response);
    }
}
