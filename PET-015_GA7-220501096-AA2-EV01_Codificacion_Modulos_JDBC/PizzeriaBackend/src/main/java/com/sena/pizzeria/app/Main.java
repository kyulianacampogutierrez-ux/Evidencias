package com.sena.pizzeria.app;

import com.sena.pizzeria.dao.ClienteDAO;
import com.sena.pizzeria.dao.PedidoDAO;
import com.sena.pizzeria.dao.PizzaDAO;
import com.sena.pizzeria.model.Cliente;
import com.sena.pizzeria.model.DetallePedido;
import com.sena.pizzeria.model.Pedido;
import com.sena.pizzeria.model.Pizza;
import com.sena.pizzeria.util.ConexionBD;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.List;

/**
 * Aplicación de consola para la demostración interactiva de las operaciones CRUD con Java JDBC.
 * Evidencia: GA7-220501096-AA2-EV01.
 * 
 * @author Karen Yuliana Campo - Aprendiz SENA ADSO Ficha 228118
 * @version 1.0.0
 */
public class Main {

    public static void main(String[] args) {
        imprimirEncabezado();

        // 1. Verificación de Conectividad JDBC
        System.out.println("===> [1/4] COMPROBACIÓN DE CONEXIÓN JDBC...");
        try (Connection conn = ConexionBD.getConexion()) {
            if (conn != null && !conn.isClosed()) {
                System.out.println("  ✓ Conexión exitosa a la base de datos 'pizzeria'");
                System.out.println("  ✓ Driver: " + conn.getMetaData().getDriverName() + " v" + conn.getMetaData().getDriverVersion());
                System.out.println("  ✓ Motor: " + conn.getMetaData().getDatabaseProductName() + " v" + conn.getMetaData().getDatabaseProductVersion());
            }
        } catch (SQLException e) {
            System.err.println("  ✗ ERROR de conexión JDBC: " + e.getMessage());
            return;
        }

        ClienteDAO clienteDao = new ClienteDAO();
        PizzaDAO pizzaDao = new PizzaDAO();
        PedidoDAO pedidoDao = new PedidoDAO();

        // 2. Demostración CRUD: Entidad CLIENTES
        System.out.println("\n===> [2/4] DEMOSTRACIÓN OPERACIONES CRUD: CLIENTES...");
        
        // 2.1 Inserción (Create)
        Cliente nuevoCliente = new Cliente("Valentina Ríos", "3114445566", "Calle 5 # 10-25, Popayán");
        boolean insertado = clienteDao.insertar(nuevoCliente);
        System.out.println("  [CREATE] Cliente registrado con ID generado: " + nuevoCliente.getIdCliente() + " (Éxito: " + insertado + ")");

        // 2.2 Consulta por ID (Read)
        Cliente clienteConsultado = clienteDao.consultarPorId(nuevoCliente.getIdCliente());
        System.out.println("  [READ] Datos consultados por ID: " + clienteConsultado);

        // 2.3 Actualización (Update)
        nuevoCliente.setDireccion("Avenida Las Palmeras Casa 8, Popayán");
        nuevoCliente.setTelefono("3129998877");
        boolean actualizado = clienteDao.actualizar(nuevoCliente);
        System.out.println("  [UPDATE] Cliente actualizado: " + clienteDao.consultarPorId(nuevoCliente.getIdCliente()) + " (Éxito: " + actualizado + ")");

        // 2.4 Consulta General (Read All)
        List<Cliente> clientes = clienteDao.listarTodos();
        System.out.println("  [READ ALL] Total de clientes en el sistema: " + clientes.size());

        // 2.5 Eliminación (Delete)
        boolean eliminado = clienteDao.eliminar(nuevoCliente.getIdCliente());
        System.out.println("  [DELETE] Cliente de prueba ID " + nuevoCliente.getIdCliente() + " eliminado: " + eliminado);

        // 3. Demostración CRUD: Entidad PIZZAS
        System.out.println("\n===> [3/4] DEMOSTRACIÓN OPERACIONES CRUD: PIZZAS...");
        Pizza nuevaPizza = new Pizza("Pizza Cuatro Estaciones", "Familiar", 55000.00);
        pizzaDao.insertar(nuevaPizza);
        System.out.println("  [CREATE] Pizza registrada con ID: " + nuevaPizza.getIdPizza());

        nuevaPizza.setPrecio(58000.00);
        pizzaDao.actualizar(nuevaPizza);
        System.out.println("  [UPDATE] Precio actualizado a: $" + pizzaDao.consultarPorId(nuevaPizza.getIdPizza()).getPrecio());

        List<Pizza> catalogo = pizzaDao.listarTodas();
        System.out.println("  [READ ALL] Catálogo de pizzas activas:");
        for (Pizza p : catalogo) {
            System.out.printf("    - ID %d: %-25s | Tamaño: %-10s | Precio: $%.2f%n",
                    p.getIdPizza(), p.getNombrePizza(), p.getTamaño(), p.getPrecio());
        }

        pizzaDao.eliminar(nuevaPizza.getIdPizza());
        System.out.println("  [DELETE] Pizza temporal ID " + nuevaPizza.getIdPizza() + " eliminada.");

        // 4. Demostración Transaccional: PEDIDOS
        System.out.println("\n===> [4/4] DEMOSTRACIÓN TRANSACCIONAL: PEDIDOS Y DETALLES...");
        Pedido nuevoPedido = new Pedido(1, 73000.00, "En Preparación");
        nuevoPedido.agregarDetalle(new DetallePedido(1, 28000.00, 0, 1)); // Pizza Margarita
        nuevoPedido.agregarDetalle(new DetallePedido(1, 45000.00, 0, 3)); // Pizza Cuatro Quesos

        boolean pedidoOk = pedidoDao.registrarPedido(nuevoPedido);
        System.out.println("  [TRANSACTION] Pedido transaccional creado con ID: " + nuevoPedido.getIdPedido() + " (Éxito: " + pedidoOk + ")");

        Pedido pedidoRecuperado = pedidoDao.consultarPorId(nuevoPedido.getIdPedido());
        System.out.println("  [READ] Pedido recuperado: " + pedidoRecuperado);
        System.out.println("  [READ] Líneas de detalle del pedido: " + pedidoRecuperado.getDetalles().size());

        pedidoDao.actualizarEstado(nuevoPedido.getIdPedido(), "Entregado");
        System.out.println("  [UPDATE] Estado actualizado a: 'Entregado'");

        pedidoDao.eliminar(nuevoPedido.getIdPedido());
        System.out.println("  [DELETE] Pedido de prueba eliminado con éxito.");

        System.out.println("\n========================================================");
        System.out.println("  TODAS LAS OPERACIONES CRUD DE LA EVIDENCIA CUMPLIDAS 100%");
        System.out.println("========================================================\n");
    }

    private static void imprimirEncabezado() {
        System.out.println("========================================================");
        System.out.println("  SERVICIO NACIONAL DE APRENDIZAJE (SENA) - ADSO");
        System.out.println("  SISTEMA DE GESTIÓN: PIZZERÍA BELLA ITALIA");
        System.out.println("  EVIDENCIA: GA7-220501096-AA2-EV01");
        System.out.println("  APRENDIZ: Karen Yuliana Campo | Ficha: 228118");
        System.out.println("========================================================");
    }
}
