package com.sena.pizzeria;

import com.sena.pizzeria.dao.ClienteDAO;
import com.sena.pizzeria.dao.PedidoDAO;
import com.sena.pizzeria.dao.PizzaDAO;
import com.sena.pizzeria.model.Cliente;
import com.sena.pizzeria.model.DetallePedido;
import com.sena.pizzeria.model.Pedido;
import com.sena.pizzeria.model.Pizza;
import com.sena.pizzeria.util.ConexionBD;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Pruebas unitarias y de integración para validar las operaciones CRUD y la conectividad JDBC.
 * Evidencia: GA7-220501096-AA2-EV01.
 * 
 * @author Karen Yuliana Campo
 */
public class PizzeriaCRUDTest {

    @Test
    @DisplayName("TC01 - Conexión activa a la base de datos MariaDB/MySQL")
    void testConexionBD() throws SQLException {
        try (Connection conn = ConexionBD.getConexion()) {
            assertNotNull(conn, "La conexión JDBC no debe ser nula");
            assertFalse(conn.isClosed(), "La conexión JDBC debe estar abierta");
        }
    }

    @Test
    @DisplayName("TC02 - Ciclo CRUD completo sobre la entidad CLIENTES")
    void testClienteCRUD() {
        ClienteDAO dao = new ClienteDAO();
        Cliente cliente = new Cliente("Test Unitario", "3001112233", "Calle Falsa 123");

        // 1. Inserción
        boolean insertado = dao.insertar(cliente);
        assertTrue(insertado, "La inserción del cliente debe ser exitosa");
        assertTrue(cliente.getIdCliente() > 0, "Debe haberse generado un ID autoincremental");

        // 2. Consulta
        Cliente recuperado = dao.consultarPorId(cliente.getIdCliente());
        assertNotNull(recuperado, "El cliente debe poder recuperarse por ID");
        assertEquals("Test Unitario", recuperado.getNombre());

        // 3. Actualización
        recuperado.setTelefono("3119990000");
        boolean actualizado = dao.actualizar(recuperado);
        assertTrue(actualizado, "La actualización del cliente debe ser exitosa");
        Cliente actualizadoDb = dao.consultarPorId(cliente.getIdCliente());
        assertEquals("3119990000", actualizadoDb.getTelefono());

        // 4. Listado
        List<Cliente> lista = dao.listarTodos();
        assertFalse(lista.isEmpty(), "La lista de clientes no debe estar vacía");

        // 5. Eliminación
        boolean eliminado = dao.eliminar(cliente.getIdCliente());
        assertTrue(eliminado, "La eliminación del cliente debe ser exitosa");
        assertNull(dao.consultarPorId(cliente.getIdCliente()), "El cliente ya no debe existir en la BD");
    }

    @Test
    @DisplayName("TC03 - Ciclo CRUD completo sobre la entidad PIZZAS")
    void testPizzaCRUD() {
        PizzaDAO dao = new PizzaDAO();
        Pizza pizza = new Pizza("Pizza Test TDD", "Personal", 19500.00);

        // 1. Inserción
        boolean insertada = dao.insertar(pizza);
        assertTrue(insertada, "La inserción de la pizza debe ser exitosa");
        assertTrue(pizza.getIdPizza() > 0, "Debe generarse un ID de pizza");

        // 2. Consulta
        Pizza recuperada = dao.consultarPorId(pizza.getIdPizza());
        assertNotNull(recuperada, "La pizza debe existir en el catálogo");
        assertEquals("Pizza Test TDD", recuperada.getNombrePizza());

        // 3. Actualización
        recuperada.setPrecio(21000.00);
        boolean actualizada = dao.actualizar(recuperada);
        assertTrue(actualizada, "La actualización de la pizza debe ser exitosa");
        assertEquals(21000.00, dao.consultarPorId(pizza.getIdPizza()).getPrecio());

        // 4. Eliminación
        boolean eliminada = dao.eliminar(pizza.getIdPizza());
        assertTrue(eliminada, "La pizza temporal debe eliminarse");
        assertNull(dao.consultarPorId(pizza.getIdPizza()));
    }

    @Test
    @DisplayName("TC04 - Registro transaccional de PEDIDOS con sus DETALLES")
    void testPedidoTransaccionalCRUD() {
        PedidoDAO dao = new PedidoDAO();
        Pedido pedido = new Pedido(1, 42000.00, "En Preparación");
        pedido.agregarDetalle(new DetallePedido(1, 42000.00, 0, 2));

        // 1. Registro Transaccional
        boolean registrado = dao.registrarPedido(pedido);
        assertTrue(registrado, "El pedido con detalles debe guardarse en la transacción");
        assertTrue(pedido.getIdPedido() > 0, "Debe generarse un ID de pedido");

        // 2. Consulta con detalles
        Pedido recuperado = dao.consultarPorId(pedido.getIdPedido());
        assertNotNull(recuperado);
        assertFalse(recuperado.getDetalles().isEmpty(), "El pedido debe contener sus líneas de detalle");

        // 3. Actualización de estado
        boolean estadoCambiado = dao.actualizarEstado(pedido.getIdPedido(), "Entregado");
        assertTrue(estadoCambiado);

        // 4. Eliminación
        boolean eliminado = dao.eliminar(pedido.getIdPedido());
        assertTrue(eliminado);
    }
}
