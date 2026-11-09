package com.sena.pizzeria.web;

import com.sena.pizzeria.dao.PizzaDAO;
import com.sena.pizzeria.model.Pizza;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.util.List;

/**
 * Controlador Servlet para el catálogo de Pizzas (Arquitectura MVC).
 * Procesa peticiones HTTP GET y POST para listar, añadir y eliminar especialidades de pizzas.
 * 
 * @author Karen Yuliana Campo
 * @version 1.0.0
 */
@WebServlet(name = "PizzaServlet", urlPatterns = {"/pizzas"})
public class PizzaServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    private PizzaDAO pizzaDAO;

    @Override
    public void init() throws ServletException {
        super.init();
        this.pizzaDAO = new PizzaDAO();
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String action = request.getParameter("action");
        if ("eliminar".equals(action)) {
            try {
                int idPizza = Integer.parseInt(request.getParameter("id"));
                pizzaDAO.eliminar(idPizza);
                response.sendRedirect(request.getContextPath() + "/pizzas?eliminado=ok");
                return;
            } catch (Exception e) {
                request.setAttribute("error", "Error al eliminar pizza: " + e.getMessage());
            }
        }

        listarPizzas(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        request.setCharacterEncoding("UTF-8");

        String idStr = request.getParameter("idPizza");
        String nombrePizza = request.getParameter("nombrePizza");
        String tamaño = request.getParameter("tamaño");
        String precioStr = request.getParameter("precio");

        try {
            double precio = Double.parseDouble(precioStr);
            if (idStr != null && !idStr.trim().isEmpty() && !idStr.equals("0")) {
                int idPizza = Integer.parseInt(idStr);
                Pizza pizza = new Pizza(idPizza, nombrePizza, tamaño, precio);
                pizzaDAO.actualizar(pizza);
            } else {
                Pizza nuevaPizza = new Pizza(nombrePizza, tamaño, precio);
                pizzaDAO.insertar(nuevaPizza);
            }
            response.sendRedirect(request.getContextPath() + "/pizzas?guardado=ok");
        } catch (Exception e) {
            request.setAttribute("error", "Error al guardar pizza: " + e.getMessage());
            listarPizzas(request, response);
        }
    }

    private void listarPizzas(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        List<Pizza> pizzas = pizzaDAO.listarTodas();
        request.setAttribute("pizzas", pizzas);
        request.getRequestDispatcher("/pizzas.jsp").forward(request, response);
    }
}
