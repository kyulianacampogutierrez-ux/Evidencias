-- ========================================================
-- SISTEMA PIZZERÍA BELLA ITALIA - ESQUEMA FÍSICO RELACIONAL
-- SERVICIO NACIONAL DE APRENDIZAJE (SENA) - ADSO
-- EVIDENCIA: GA7-220501096-AA2-EV01 (Conexión Java JDBC & CRUD)
-- APRENDIZ: Karen Yuliana Campo - Ficha 228118
-- ========================================================

CREATE DATABASE IF NOT EXISTS pizzeria CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE pizzeria;

-- 1. TABLA CLIENTES
CREATE TABLE IF NOT EXISTS CLIENTES (
  ID_Cliente INT NOT NULL AUTO_INCREMENT,
  Nombre VARCHAR(100) NOT NULL,
  Telefono VARCHAR(20) NOT NULL,
  Direccion VARCHAR(150) NOT NULL,
  PRIMARY KEY (ID_Cliente)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2. TABLA PIZZAS (CATÁLOGO DE PRODUCTOS)
CREATE TABLE IF NOT EXISTS PIZZAS (
  ID_Pizza INT NOT NULL AUTO_INCREMENT,
  Nombre_Pizza VARCHAR(50) NOT NULL,
  Tamaño VARCHAR(20) NOT NULL,
  Precio DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (ID_Pizza)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 3. TABLA PEDIDOS (ENCABEZADO DE VENTA)
CREATE TABLE IF NOT EXISTS PEDIDOS (
  ID_Pedido INT NOT NULL AUTO_INCREMENT,
  Fecha DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  Total DECIMAL(10,2) NOT NULL DEFAULT 0.00,
  ID_Cliente INT NOT NULL,
  Estado VARCHAR(30) NOT NULL DEFAULT 'En Preparación',
  PRIMARY KEY (ID_Pedido),
  CONSTRAINT FK_Pedido_Cliente FOREIGN KEY (ID_Cliente) REFERENCES CLIENTES(ID_Cliente) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 4. TABLA DETALLE_PEDIDO (LÍNEAS DE VENTA)
CREATE TABLE IF NOT EXISTS DETALLE_PEDIDO (
  ID_Detalle INT NOT NULL AUTO_INCREMENT,
  Cantidad INT NOT NULL DEFAULT 1,
  Subtotal DECIMAL(10,2) NOT NULL,
  ID_Pedido INT NOT NULL,
  ID_Pizza INT NOT NULL,
  PRIMARY KEY (ID_Detalle),
  CONSTRAINT FK_Detalle_Pedido FOREIGN KEY (ID_Pedido) REFERENCES PEDIDOS(ID_Pedido) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT FK_Detalle_Pizza FOREIGN KEY (ID_Pizza) REFERENCES PIZZAS(ID_Pizza) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ========================================================
-- DATOS INICIALES DE PRUEBA (SEED DATA)
-- ========================================================

-- Inserción inicial de clientes
INSERT INTO CLIENTES (Nombre, Telefono, Direccion) VALUES 
('Carlos Mendoza', '3101234567', 'Calle 12 # 34-56, Popayán'),
('Ana Ramirez', '3209876543', 'Carrera 45 # 12-89, Popayán'),
('Laura Gomez', '3155554433', 'Avenida Panamericana # 5-20'),
('David Martinez', '3187779900', 'Barrio Caldas Casa 14');

-- Inserción inicial de pizzas
INSERT INTO PIZZAS (Nombre_Pizza, Tamaño, Precio) VALUES 
('Pizza Margarita', 'Mediana', 28000.00),
('Pizza Pepperoni Clásica', 'Grande', 42000.00),
('Pizza Cuatro Quesos', 'Grande', 45000.00),
('Pizza Hawaiana Especial', 'Familiar', 52000.00),
('Pizza Napolitana', 'Mediana', 32000.00),
('Pizza Vegetariana Gourmet', 'Mediana', 34000.00);

-- Inserción inicial de pedidos
INSERT INTO PEDIDOS (Fecha, Total, ID_Cliente, Estado) VALUES 
('2026-11-08 12:30:00', 70000.00, 1, 'Entregado'),
('2026-11-08 14:15:00', 52000.00, 2, 'En Reparto'),
('2026-11-08 16:45:00', 45000.00, 3, 'En Preparación');

-- Inserción inicial de detalles
INSERT INTO DETALLE_PEDIDO (Cantidad, Subtotal, ID_Pedido, ID_Pizza) VALUES 
(1, 28000.00, 1, 1),
(1, 42000.00, 1, 2),
(1, 52000.00, 2, 4),
(1, 45000.00, 3, 3);
