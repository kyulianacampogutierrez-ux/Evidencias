package com.sena.pizzeria.dao;

import com.sena.pizzeria.model.Pizza;
import com.sena.pizzeria.util.ConexionBD;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

/**
 * Objeto de Acceso a Datos (DAO) para la entidad Pizza.
 * Gestiona el catálogo de pizzas en la base de datos con sentencias parametrizadas.
 * 
 * @author Karen Yuliana Campo
 * @version 1.0.0
 */
public class PizzaDAO {

    private static final String SQL_INSERT = "INSERT INTO PIZZAS (Nombre_Pizza, Tamaño, Precio) VALUES (?, ?, ?)";
    private static final String SQL_SELECT_BY_ID = "SELECT ID_Pizza, Nombre_Pizza, Tamaño, Precio FROM PIZZAS WHERE ID_Pizza = ?";
    private static final String SQL_SELECT_ALL = "SELECT ID_Pizza, Nombre_Pizza, Tamaño, Precio FROM PIZZAS ORDER BY ID_Pizza ASC";
    private static final String SQL_UPDATE = "UPDATE PIZZAS SET Nombre_Pizza = ?, Tamaño = ?, Precio = ? WHERE ID_Pizza = ?";
    private static final String SQL_DELETE = "DELETE FROM PIZZAS WHERE ID_Pizza = ?";

    /**
     * Inserción (Create): Añade una nueva pizza al catálogo.
     */
    public boolean insertar(Pizza pizza) {
        Connection conn = null;
        PreparedStatement stmt = null;
        ResultSet rs = null;

        try {
            conn = ConexionBD.getConexion();
            stmt = conn.prepareStatement(SQL_INSERT, Statement.RETURN_GENERATED_KEYS);
            stmt.setString(1, pizza.getNombrePizza());
            stmt.setString(2, pizza.getTamaño());
            stmt.setDouble(3, pizza.getPrecio());

            int filasAfectadas = stmt.executeUpdate();
            if (filasAfectadas > 0) {
                rs = stmt.getGeneratedKeys();
                if (rs.next()) {
                    pizza.setIdPizza(rs.getInt(1));
                }
                return true;
            }
        } catch (SQLException e) {
            System.err.println("Error al insertar pizza: " + e.getMessage());
        } finally {
            ConexionBD.cerrar(stmt, rs);
            ConexionBD.cerrar(conn);
        }
        return false;
    }

    /**
     * Consulta por ID (Read): Busca una pizza por su ID.
     */
    public Pizza consultarPorId(int idPizza) {
        Connection conn = null;
        PreparedStatement stmt = null;
        ResultSet rs = null;

        try {
            conn = ConexionBD.getConexion();
            stmt = conn.prepareStatement(SQL_SELECT_BY_ID);
            stmt.setInt(1, idPizza);
            rs = stmt.executeQuery();

            if (rs.next()) {
                return mapearPizza(rs);
            }
        } catch (SQLException e) {
            System.err.println("Error al consultar pizza por ID: " + e.getMessage());
        } finally {
            ConexionBD.cerrar(stmt, rs);
            ConexionBD.cerrar(conn);
        }
        return null;
    }

    /**
     * Consulta General (Read): Retorna todas las pizzas registradas.
     */
    public List<Pizza> listarTodas() {
        List<Pizza> pizzas = new ArrayList<>();
        Connection conn = null;
        PreparedStatement stmt = null;
        ResultSet rs = null;

        try {
            conn = ConexionBD.getConexion();
            stmt = conn.prepareStatement(SQL_SELECT_ALL);
            rs = stmt.executeQuery();

            while (rs.next()) {
                pizzas.add(mapearPizza(rs));
            }
        } catch (SQLException e) {
            System.err.println("Error al listar pizzas: " + e.getMessage());
        } finally {
            ConexionBD.cerrar(stmt, rs);
            ConexionBD.cerrar(conn);
        }
        return pizzas;
    }

    /**
     * Actualización (Update): Modifica el nombre, tamaño o precio de una pizza.
     */
    public boolean actualizar(Pizza pizza) {
        Connection conn = null;
        PreparedStatement stmt = null;

        try {
            conn = ConexionBD.getConexion();
            stmt = conn.prepareStatement(SQL_UPDATE);
            stmt.setString(1, pizza.getNombrePizza());
            stmt.setString(2, pizza.getTamaño());
            stmt.setDouble(3, pizza.getPrecio());
            stmt.setInt(4, pizza.getIdPizza());

            return stmt.executeUpdate() > 0;
        } catch (SQLException e) {
            System.err.println("Error al actualizar pizza: " + e.getMessage());
        } finally {
            ConexionBD.cerrar(stmt, null);
            ConexionBD.cerrar(conn);
        }
        return false;
    }

    /**
     * Eliminación (Delete): Elimina una pizza por su ID.
     */
    public boolean eliminar(int idPizza) {
        Connection conn = null;
        PreparedStatement stmt = null;

        try {
            conn = ConexionBD.getConexion();
            stmt = conn.prepareStatement(SQL_DELETE);
            stmt.setInt(1, idPizza);

            return stmt.executeUpdate() > 0;
        } catch (SQLException e) {
            System.err.println("Error al eliminar pizza: " + e.getMessage());
        } finally {
            ConexionBD.cerrar(stmt, null);
            ConexionBD.cerrar(conn);
        }
        return false;
    }

    private Pizza mapearPizza(ResultSet rs) throws SQLException {
        return new Pizza(
                rs.getInt("ID_Pizza"),
                rs.getString("Nombre_Pizza"),
                rs.getString("Tamaño"),
                rs.getDouble("Precio")
        );
    }
}
