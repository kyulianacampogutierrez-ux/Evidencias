-- ==============================================================================
-- DUMP DE MIGRACIÓN DE DATOS - PIZZERÍA GOURMET BELLA ITALIA POPAYÁN
-- Base de Datos: pizzeria_bella_italia_db
-- Versión de Exportación: 1.0 (Migración a Servidor del Cliente)
-- Generado por: Karen Yuliana Campo (Ficha 3186681)
-- ==============================================================================

CREATE TABLE IF NOT EXISTS usuarios_clientes (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_completo VARCHAR(120) NOT NULL,
    telefono_movil VARCHAR(15) NOT NULL,
    direccion_popayan VARCHAR(180) NOT NULL,
    email VARCHAR(100) UNIQUE,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO usuarios_clientes (nombre_completo, telefono_movil, direccion_popayan, email) VALUES
('Karen Yuliana Campo', '3186681000', 'Calle 5 # 10-30 Barrio Bolívar', 'karen.campo@sena.edu.co'),
('Carlos Alberto Martínez', '3157891234', 'Carrera 9 # 4-25 Centro Popayán', 'carlos.martinez@gmail.com'),
('María Elena Gómez', '3104567890', 'Calle 67N # 9-40 Barrio Prados del Norte', 'maria.gomez@gmail.com');

CREATE TABLE IF NOT EXISTS pedidos_gourmet (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    codigo_orden VARCHAR(25) NOT NULL,
    producto_pizza VARCHAR(100) NOT NULL,
    subtotal_cop DECIMAL(10,2) NOT NULL,
    impoconsumo_8_cop DECIMAL(10,2) NOT NULL,
    total_cop DECIMAL(10,2) NOT NULL,
    estado_pedido VARCHAR(30) DEFAULT 'EN_PREPARACION',
    FOREIGN KEY (id_usuario) REFERENCES usuarios_clientes(id_usuario)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO pedidos_gourmet (id_usuario, codigo_orden, producto_pizza, subtotal_cop, impoconsumo_8_cop, total_cop) VALUES
(1, 'ORD-2026-1082', 'Bella Italia Especial Gourmet', 48000.00, 3840.00, 51840.00),
(2, 'ORD-2026-1083', 'Margherita D.O.C. Tradicional', 38000.00, 3040.00, 41040.00);
