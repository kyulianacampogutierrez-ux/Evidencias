package com.sena.pizzeria.util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

/**
 * Gestor centralizado de conexiones JDBC para la base de datos de la Pizzería.
 * Aplica el patrón Singleton/Factory y soporta configuración dinámica vía variables de entorno.
 * 
 * @author Karen Yuliana Campo
 * @version 1.0.0
 */
public class ConexionBD {

    private static final String DEFAULT_HOST = "localhost";
    private static final String DEFAULT_PORT = "3306";
    private static final String DEFAULT_DATABASE = "pizzeria";
    private static final String DEFAULT_USER = "karen";
    private static final String DEFAULT_PASSWORD = "choco";

    private static final String MARIADB_DRIVER = "org.mariadb.jdbc.Driver";
    private static final String MYSQL_DRIVER = "com.mysql.cj.jdbc.Driver";

    static {
        // Carga dinámica de los controladores JDBC
        try {
            Class.forName(MARIADB_DRIVER);
        } catch (ClassNotFoundException e) {
            try {
                Class.forName(MYSQL_DRIVER);
            } catch (ClassNotFoundException ex) {
                System.err.println("Advertencia: No se encontró controlador JDBC en el classpath: " + ex.getMessage());
            }
        }
    }

    /**
     * Obtiene una nueva conexión activa con la base de datos.
     * Lee variables de entorno si están presentes (DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS).
     *
     * @return Conexión activa a MariaDB / MySQL
     * @throws SQLException si ocurre un error en la autenticación o conexión de red
     */
    public static Connection getConexion() throws SQLException {
        String host = System.getenv("DB_HOST");
        if (host == null || host.trim().isEmpty()) {
            host = DEFAULT_HOST;
        }

        String port = System.getenv("DB_PORT");
        if (port == null || port.trim().isEmpty()) {
            port = DEFAULT_PORT;
        }

        String database = System.getenv("DB_NAME");
        if (database == null || database.trim().isEmpty()) {
            database = DEFAULT_DATABASE;
        }

        String user = System.getenv("DB_USER");
        if (user == null || user.trim().isEmpty()) {
            user = DEFAULT_USER;
        }

        String password = System.getenv("DB_PASS");
        if (password == null) {
            password = DEFAULT_PASSWORD;
        }

        String url = String.format("jdbc:mariadb://%s:%s/%s?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=America/Bogota",
                host, port, database);

        try {
            return DriverManager.getConnection(url, user, password);
        } catch (SQLException e) {
            // Reintento con protocolo jdbc:mysql
            String fallbackUrl = String.format("jdbc:mysql://%s:%s/%s?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=America/Bogota",
                    host, port, database);
            return DriverManager.getConnection(fallbackUrl, user, password);
        }
    }

    /**
     * Cierra de forma segura una conexión JDBC.
     */
    public static void cerrar(Connection conexion) {
        if (conexion != null) {
            try {
                conexion.close();
            } catch (SQLException e) {
                System.err.println("Error al cerrar conexión: " + e.getMessage());
            }
        }
    }

    /**
     * Cierra de forma segura Statement y ResultSet.
     */
    public static void cerrar(Statement statement, ResultSet resultSet) {
        if (resultSet != null) {
            try {
                resultSet.close();
            } catch (SQLException ignored) {
            }
        }
        if (statement != null) {
            try {
                statement.close();
            } catch (SQLException ignored) {
            }
        }
    }
}
