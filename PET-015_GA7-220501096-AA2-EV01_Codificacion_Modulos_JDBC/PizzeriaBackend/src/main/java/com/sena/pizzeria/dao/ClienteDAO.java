package com.sena.pizzeria.dao;

import com.sena.pizzeria.model.Cliente;
import com.sena.pizzeria.util.ConexionBD;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

/**
 * Objeto de Acceso a Datos (DAO) para la entidad Cliente.
 * Implementa operaciones CRUD completas utilizando PreparedStatement para máxima seguridad.
 * 
 * @author Karen Yuliana Campo
 * @version 1.0.0
 */
public class ClienteDAO {

    private static final String SQL_INSERT = "INSERT INTO CLIENTES (Nombre, Telefono, Direccion) VALUES (?, ?, ?)";
    private static final String SQL_SELECT_BY_ID = "SELECT ID_Cliente, Nombre, Telefono, Direccion FROM CLIENTES WHERE ID_Cliente = ?";
    private static final String SQL_SELECT_ALL = "SELECT ID_Cliente, Nombre, Telefono, Direccion FROM CLIENTES ORDER BY ID_Cliente ASC";
    private static final String SQL_UPDATE = "UPDATE CLIENTES SET Nombre = ?, Telefono = ?, Direccion = ? WHERE ID_Cliente = ?";
    private static final String SQL_DELETE = "DELETE FROM CLIENTES WHERE ID_Cliente = ?";

    /**
     * Inserción (Create): Registra un nuevo cliente en la base de datos.
     */
    public boolean insertar(Cliente cliente) {
        Connection conn = null;
        PreparedStatement stmt = null;
        ResultSet rs = null;

        try {
            conn = ConexionBD.getConexion();
            stmt = conn.prepareStatement(SQL_INSERT, Statement.RETURN_GENERATED_KEYS);
            stmt.setString(1, cliente.getNombre());
            stmt.setString(2, cliente.getTelefono());
            stmt.setString(3, cliente.getDireccion());

            int filasAfectadas = stmt.executeUpdate();
            if (filasAfectadas > 0) {
                rs = stmt.getGeneratedKeys();
                if (rs.next()) {
                    cliente.setIdCliente(rs.getInt(1));
                }
                return true;
            }
        } catch (SQLException e) {
            System.err.println("Error al insertar cliente: " + e.getMessage());
        } finally {
            ConexionBD.cerrar(stmt, rs);
            ConexionBD.cerrar(conn);
        }
        return false;
    }

    /**
     * Consulta por ID (Read): Recupera un cliente por su identificador primario.
     */
    public Cliente consultarPorId(int idCliente) {
        Connection conn = null;
        PreparedStatement stmt = null;
        ResultSet rs = null;

        try {
            conn = ConexionBD.getConexion();
            stmt = conn.prepareStatement(SQL_SELECT_BY_ID);
            stmt.setInt(1, idCliente);
            rs = stmt.executeQuery();

            if (rs.next()) {
                return mapearCliente(rs);
            }
        } catch (SQLException e) {
            System.err.println("Error al consultar cliente por ID: " + e.getMessage());
        } finally {
            ConexionBD.cerrar(stmt, rs);
            ConexionBD.cerrar(conn);
        }
        return null;
    }

    /**
     * Consulta General (Read): Retorna la lista de todos los clientes registrados.
     */
    public List<Cliente> listarTodos() {
        List<Cliente> clientes = new ArrayList<>();
        Connection conn = null;
        PreparedStatement stmt = null;
        ResultSet rs = null;

        try {
            conn = ConexionBD.getConexion();
            stmt = conn.prepareStatement(SQL_SELECT_ALL);
            rs = stmt.executeQuery();

            while (rs.next()) {
                clientes.add(mapearCliente(rs));
            }
        } catch (SQLException e) {
            System.err.println("Error al listar clientes: " + e.getMessage());
        } finally {
            ConexionBD.cerrar(stmt, rs);
            ConexionBD.cerrar(conn);
        }
        return clientes;
    }

    /**
     * Actualización (Update): Modifica los datos de un cliente existente.
     */
    public boolean actualizar(Cliente cliente) {
        Connection conn = null;
        PreparedStatement stmt = null;

        try {
            conn = ConexionBD.getConexion();
            stmt = conn.prepareStatement(SQL_UPDATE);
            stmt.setString(1, cliente.getNombre());
            stmt.setString(2, cliente.getTelefono());
            stmt.setString(3, cliente.getDireccion());
            stmt.setInt(4, cliente.getIdCliente());

            return stmt.executeUpdate() > 0;
        } catch (SQLException e) {
            System.err.println("Error al actualizar cliente: " + e.getMessage());
        } finally {
            ConexionBD.cerrar(stmt, null);
            ConexionBD.cerrar(conn);
        }
        return false;
    }

    /**
     * Eliminación (Delete): Remueve un cliente por su ID.
     */
    public boolean eliminar(int idCliente) {
        Connection conn = null;
        PreparedStatement stmt = null;

        try {
            conn = ConexionBD.getConexion();
            stmt = conn.prepareStatement(SQL_DELETE);
            stmt.setInt(1, idCliente);

            return stmt.executeUpdate() > 0;
        } catch (SQLException e) {
            System.err.println("Error al eliminar cliente: " + e.getMessage());
        } finally {
            ConexionBD.cerrar(stmt, null);
            ConexionBD.cerrar(conn);
        }
        return false;
    }

    private Cliente mapearCliente(ResultSet rs) throws SQLException {
        return new Cliente(
                rs.getInt("ID_Cliente"),
                rs.getString("Nombre"),
                rs.getString("Telefono"),
                rs.getString("Direccion")
        );
    }
}
