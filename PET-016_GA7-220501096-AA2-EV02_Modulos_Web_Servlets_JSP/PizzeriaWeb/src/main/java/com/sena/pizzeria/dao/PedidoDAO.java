package com.sena.pizzeria.dao;

import com.sena.pizzeria.model.DetallePedido;
import com.sena.pizzeria.model.Pedido;
import com.sena.pizzeria.util.ConexionBD;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.List;

/**
 * Objeto de Acceso a Datos (DAO) para la entidad Pedido y sus Detalles.
 * Maneja transacciones ACID para asegurar la consistencia entre PEDIDOS y DETALLE_PEDIDO.
 * 
 * @author Karen Yuliana Campo
 * @version 1.0.0
 */
public class PedidoDAO {

    private static final String SQL_INSERT_PEDIDO = "INSERT INTO PEDIDOS (Fecha, Total, ID_Cliente, Estado) VALUES (?, ?, ?, ?)";
    private static final String SQL_INSERT_DETALLE = "INSERT INTO DETALLE_PEDIDO (Cantidad, Subtotal, ID_Pedido, ID_Pizza) VALUES (?, ?, ?, ?)";
    private static final String SQL_SELECT_BY_ID = "SELECT ID_Pedido, Fecha, Total, ID_Cliente, Estado FROM PEDIDOS WHERE ID_Pedido = ?";
    private static final String SQL_SELECT_ALL = "SELECT ID_Pedido, Fecha, Total, ID_Cliente, Estado FROM PEDIDOS ORDER BY ID_Pedido DESC";
    private static final String SQL_SELECT_DETALLES = "SELECT ID_Detalle, Cantidad, Subtotal, ID_Pedido, ID_Pizza FROM DETALLE_PEDIDO WHERE ID_Pedido = ?";
    private static final String SQL_UPDATE_ESTADO = "UPDATE PEDIDOS SET Estado = ? WHERE ID_Pedido = ?";
    private static final String SQL_DELETE = "DELETE FROM PEDIDOS WHERE ID_Pedido = ?";

    /**
     * Inserción Transaccional: Registra un pedido y todos sus ítems en DETALLE_PEDIDO en una sola transacción.
     */
    public boolean registrarPedido(Pedido pedido) {
        Connection conn = null;
        PreparedStatement stmtPedido = null;
        PreparedStatement stmtDetalle = null;
        ResultSet rs = null;

        try {
            conn = ConexionBD.getConexion();
            conn.setAutoCommit(false); // Iniciar transacción ACID

            stmtPedido = conn.prepareStatement(SQL_INSERT_PEDIDO, Statement.RETURN_GENERATED_KEYS);
            stmtPedido.setTimestamp(1, Timestamp.valueOf(pedido.getFecha()));
            stmtPedido.setDouble(2, pedido.getTotal());
            stmtPedido.setInt(3, pedido.getIdCliente());
            stmtPedido.setString(4, pedido.getEstado());

            int filas = stmtPedido.executeUpdate();
            if (filas == 0) {
                conn.rollback();
                return false;
            }

            rs = stmtPedido.getGeneratedKeys();
            int idGenerado = 0;
            if (rs.next()) {
                idGenerado = rs.getInt(1);
                pedido.setIdPedido(idGenerado);
            }

            // Insertar líneas de detalle si existen
            if (pedido.getDetalles() != null && !pedido.getDetalles().isEmpty()) {
                stmtDetalle = conn.prepareStatement(SQL_INSERT_DETALLE);
                for (DetallePedido detalle : pedido.getDetalles()) {
                    detalle.setIdPedido(idGenerado);
                    stmtDetalle.setInt(1, detalle.getCantidad());
                    stmtDetalle.setDouble(2, detalle.getSubtotal());
                    stmtDetalle.setInt(3, idGenerado);
                    stmtDetalle.setInt(4, detalle.getIdPizza());
                    stmtDetalle.addBatch();
                }
                stmtDetalle.executeBatch();
            }

            conn.commit(); // Confirmar transacción exitosa
            return true;

        } catch (SQLException e) {
            System.err.println("Error en transacción de pedido: " + e.getMessage());
            if (conn != null) {
                try {
                    conn.rollback();
                } catch (SQLException ex) {
                    System.err.println("Error en rollback: " + ex.getMessage());
                }
            }
            return false;
        } finally {
            ConexionBD.cerrar(stmtDetalle, null);
            ConexionBD.cerrar(stmtPedido, rs);
            ConexionBD.cerrar(conn);
        }
    }

    /**
     * Consulta por ID: Recupera un pedido junto con sus detalles asociados.
     */
    public Pedido consultarPorId(int idPedido) {
        Connection conn = null;
        PreparedStatement stmt = null;
        ResultSet rs = null;

        try {
            conn = ConexionBD.getConexion();
            stmt = conn.prepareStatement(SQL_SELECT_BY_ID);
            stmt.setInt(1, idPedido);
            rs = stmt.executeQuery();

            if (rs.next()) {
                Pedido pedido = mapearPedido(rs);
                pedido.setDetalles(cargarDetalles(conn, idPedido));
                return pedido;
            }
        } catch (SQLException e) {
            System.err.println("Error al consultar pedido: " + e.getMessage());
        } finally {
            ConexionBD.cerrar(stmt, rs);
            ConexionBD.cerrar(conn);
        }
        return null;
    }

    /**
     * Consulta General: Lista todos los pedidos registrados.
     */
    public List<Pedido> listarTodos() {
        List<Pedido> pedidos = new ArrayList<>();
        Connection conn = null;
        PreparedStatement stmt = null;
        ResultSet rs = null;

        try {
            conn = ConexionBD.getConexion();
            stmt = conn.prepareStatement(SQL_SELECT_ALL);
            rs = stmt.executeQuery();

            while (rs.next()) {
                pedidos.add(mapearPedido(rs));
            }
        } catch (SQLException e) {
            System.err.println("Error al listar pedidos: " + e.getMessage());
        } finally {
            ConexionBD.cerrar(stmt, rs);
            ConexionBD.cerrar(conn);
        }
        return pedidos;
    }

    /**
     * Actualización: Modifica el estado del pedido (ej. 'En Preparación' -> 'Entregado').
     */
    public boolean actualizarEstado(int idPedido, String nuevoEstado) {
        Connection conn = null;
        PreparedStatement stmt = null;

        try {
            conn = ConexionBD.getConexion();
            stmt = conn.prepareStatement(SQL_UPDATE_ESTADO);
            stmt.setString(1, nuevoEstado);
            stmt.setInt(2, idPedido);

            return stmt.executeUpdate() > 0;
        } catch (SQLException e) {
            System.err.println("Error al actualizar estado del pedido: " + e.getMessage());
        } finally {
            ConexionBD.cerrar(stmt, null);
            ConexionBD.cerrar(conn);
        }
        return false;
    }

    /**
     * Eliminación: Remueve un pedido y en cascada sus detalles.
     */
    public boolean eliminar(int idPedido) {
        Connection conn = null;
        PreparedStatement stmt = null;

        try {
            conn = ConexionBD.getConexion();
            stmt = conn.prepareStatement(SQL_DELETE);
            stmt.setInt(1, idPedido);

            return stmt.executeUpdate() > 0;
        } catch (SQLException e) {
            System.err.println("Error al eliminar pedido: " + e.getMessage());
        } finally {
            ConexionBD.cerrar(stmt, null);
            ConexionBD.cerrar(conn);
        }
        return false;
    }

    private List<DetallePedido> cargarDetalles(Connection conn, int idPedido) throws SQLException {
        List<DetallePedido> detalles = new ArrayList<>();
        try (PreparedStatement stmt = conn.prepareStatement(SQL_SELECT_DETALLES)) {
            stmt.setInt(1, idPedido);
            try (ResultSet rs = stmt.executeQuery()) {
                while (rs.next()) {
                    detalles.add(new DetallePedido(
                            rs.getInt("ID_Detalle"),
                            rs.getInt("Cantidad"),
                            rs.getDouble("Subtotal"),
                            rs.getInt("ID_Pedido"),
                            rs.getInt("ID_Pizza")
                    ));
                }
            }
        }
        return detalles;
    }

    private Pedido mapearPedido(ResultSet rs) throws SQLException {
        Timestamp ts = rs.getTimestamp("Fecha");
        return new Pedido(
                rs.getInt("ID_Pedido"),
                ts != null ? ts.toLocalDateTime() : null,
                rs.getDouble("Total"),
                rs.getInt("ID_Cliente"),
                rs.getString("Estado")
        );
    }
}
