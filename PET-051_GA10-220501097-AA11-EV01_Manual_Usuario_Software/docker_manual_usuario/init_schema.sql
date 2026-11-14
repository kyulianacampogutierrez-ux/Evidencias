-- ==============================================================================
-- BASE DE DATOS: PIZZERÍA GOURMET BELLA ITALIA POPAYÁN
-- ESQUEMA DE DATOS PARA MANUAL DE USUARIO - EVIDENCIA GA10-220501097-AA11-EV01
-- ==============================================================================

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

CREATE DATABASE IF NOT EXISTS pizzeria_manual_usuario_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE pizzeria_manual_usuario_db;

-- 1. Roles y Permisos
CREATE TABLE IF NOT EXISTS tbl_roles_permisos (
  id_rol INT AUTO_INCREMENT PRIMARY KEY,
  nombre_rol VARCHAR(50) NOT NULL UNIQUE,
  descripcion VARCHAR(255) NOT NULL,
  nivel_acceso INT NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO tbl_roles_permisos (id_rol, nombre_rol, descripcion, nivel_acceso) VALUES
(1, 'ClienteComensal', 'Navegación de carta, pedidos online y seguimiento', 1),
(2, 'CajeroSalon', 'Gestión de caja, cobro presencial y facturación DIAN', 5),
(3, 'JefeCocina', 'Control de comandas en KDS, horneado y estados', 4),
(4, 'Domiciliario', 'Despacho geolocalizado en Popayán y entrega', 2),
(5, 'Administrador', 'Control total de carta, precios, usuarios e informes', 10)
ON DUPLICATE KEY UPDATE nombre_rol=VALUES(nombre_rol);

-- 2. Usuarios
CREATE TABLE IF NOT EXISTS tbl_usuarios (
  id_usuario INT AUTO_INCREMENT PRIMARY KEY,
  id_rol INT NOT NULL,
  nombre_completo VARCHAR(120) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  telefono VARCHAR(20) NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  estado ENUM('ACTIVO', 'INACTIVO', 'BLOQUEADO') DEFAULT 'ACTIVO',
  CONSTRAINT fk_usr_rol FOREIGN KEY (id_rol) REFERENCES tbl_roles_permisos(id_rol)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO tbl_usuarios (id_usuario, id_rol, nombre_completo, email, telefono, password_hash) VALUES
(1, 5, 'Karen Yuliana Campo (Admin)', 'admin@pizzeriabellaitalia.com', '3157894512', '$2y$12$e8Yk1.7B5R6y19/Y9iI69uvG3l5R2tGv889YF2tN1/1P.Q8N3/O5W'),
(2, 2, 'Danilo (Cajero Principal)', 'cajero@pizzeriabellaitalia.com', '3128906734', '$2y$12$a4b8c9d0e1f2g3h4i5j6k7l8m9n0o1p2q3r4s5t6u7v8w9x0y1z2a'),
(3, 3, 'Marco Rossi (Jefe Cocina)', 'cocina@pizzeriabellaitalia.com', '3189998877', '$2y$12$b5c9d0e1f2g3h4i5j6k7l8m9n0o1p2q3r4s5t6u7v8w9x0y1z2a3b'),
(4, 4, 'Carlos López (Domiciliario)', 'domicilios@pizzeriabellaitalia.com', '3201112233', '$2y$12$c6d0e1f2g3h4i5j6k7l8m9n0o1p2q3r4s5t6u7v8w9x0y1z2a3b4c'),
(5, 1, 'Santiago Pérez (Comensal)', 'santiago.perez@gmail.com', '3145556677', '$2y$12$d7e1f2g3h4i5j6k7l8m9n0o1p2q3r4s5t6u7v8w9x0y1z2a3b4c5d')
ON DUPLICATE KEY UPDATE email=VALUES(email);

-- 3. Categorías de Productos
CREATE TABLE IF NOT EXISTS tbl_categorias (
  id_categoria INT AUTO_INCREMENT PRIMARY KEY,
  nombre_categoria VARCHAR(60) NOT NULL UNIQUE,
  descripcion VARCHAR(255) NOT NULL,
  icono VARCHAR(50) DEFAULT 'pizza'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO tbl_categorias (id_categoria, nombre_categoria, descripcion, icono) VALUES
(1, 'Pizzas Clásicas Italianas', 'Recetas con fermentación lenta 48h', 'pizza-slice'),
(2, 'Especialidades Gourmet Popayán', 'Ingredientes típicos del Cauca (Pipián, Queso de Silvia)', 'star'),
(3, 'Calzones & Focaccias', 'Masas horneadas rellenas a la piedra', 'bread-slice'),
(4, 'Bebidas & Postres', 'Gaseosas italianas, cervezas artesanales y tiramisú', 'wine-glass')
ON DUPLICATE KEY UPDATE nombre_categoria=VALUES(nombre_categoria);

-- 4. Productos del Menú
CREATE TABLE IF NOT EXISTS tbl_productos_menu (
  id_producto INT AUTO_INCREMENT PRIMARY KEY,
  id_categoria INT NOT NULL,
  nombre_producto VARCHAR(100) NOT NULL,
  descripcion TEXT NOT NULL,
  precio_unitario DECIMAL(12,2) NOT NULL,
  tiempo_estimado_min INT DEFAULT 15,
  disponible BOOLEAN DEFAULT TRUE,
  CONSTRAINT fk_prod_cat FOREIGN KEY (id_categoria) REFERENCES tbl_categorias(id_categoria)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO tbl_productos_menu (id_producto, id_categoria, nombre_producto, descripcion, precio_unitario, tiempo_estimado_min) VALUES
(1, 1, 'Pizza Margherita di Popayán', 'Tomate San Marzano, mozzarella fior di latte y albahaca fresca', 35000.00, 12),
(2, 2, 'Pizza Gourmet Pipián Caucano', 'Pipián tradicional payanés, queso campesino de Silvia y hogao de la casa', 48000.00, 16),
(3, 3, 'Calzone Ripieno Napolitano', 'Ricotta fresca, jamón serrano, mozzarella y albahaca', 42000.00, 18),
(4, 4, 'Tiramisú Tradicional Café Caucano', 'Savoiardi bañados en café de exportación del Cauca y mascarpone', 16000.00, 5)
ON DUPLICATE KEY UPDATE nombre_producto=VALUES(nombre_producto);

-- 5. Pedidos de Usuarios
CREATE TABLE IF NOT EXISTS tbl_pedidos (
  id_pedido INT AUTO_INCREMENT PRIMARY KEY,
  codigo_orden VARCHAR(30) NOT NULL UNIQUE,
  id_cliente INT NOT NULL,
  canal ENUM('WEB', 'APP_MOVIL', 'SALON_MESA') DEFAULT 'WEB',
  estado ENUM('PENDIENTE', 'RECIBIDO', 'EN_PREPARACION', 'LISTO_DESPACHO', 'EN_CAMINO', 'ENTREGADO') DEFAULT 'RECIBIDO',
  total_cop DECIMAL(12,2) NOT NULL,
  direccion_entrega VARCHAR(200) NOT NULL,
  fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_ped_usr FOREIGN KEY (id_cliente) REFERENCES tbl_usuarios(id_usuario)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO tbl_pedidos (id_pedido, codigo_orden, id_cliente, canal, estado, total_cop, direccion_entrega) VALUES
(1, 'ORD-202611-101', 5, 'WEB', 'ENTREGADO', 83000.00, 'Calle 4 # 8-15, Centro, Popayán'),
(2, 'ORD-202611-102', 5, 'WEB', 'EN_PREPARACION', 48000.00, 'Carrera 9 # 14-22, Barrio Modelo, Popayán')
ON DUPLICATE KEY UPDATE codigo_orden=VALUES(codigo_orden);

SET FOREIGN_KEY_CHECKS = 1;
