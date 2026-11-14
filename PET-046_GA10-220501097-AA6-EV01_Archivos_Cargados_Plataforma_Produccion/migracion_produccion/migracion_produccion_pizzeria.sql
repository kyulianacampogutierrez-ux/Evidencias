-- ==============================================================================
-- PLAN DE MIGRACIÓN DE DATOS A PLATAFORMA DE PRODUCCIÓN
-- Evidencia: GA10-220501097-AA6-EV01 - Archivos Cargados en Plataforma Producción
-- Base de Datos: pizzeria_produccion_db
-- Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | SENA CTPI Popayán
-- ==============================================================================

CREATE DATABASE IF NOT EXISTS pizzeria_produccion_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE pizzeria_produccion_db;

-- 1. Tabla de Catálogo Gourmet en Producción
CREATE TABLE IF NOT EXISTS productos_pizza (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre_pizza VARCHAR(100) NOT NULL,
    descripcion_ingredientes TEXT NOT NULL,
    categoria VARCHAR(40) NOT NULL,
    precio_cop DECIMAL(10,2) NOT NULL,
    disponible BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2. Tabla de Usuarios y Clientes en Producción
CREATE TABLE IF NOT EXISTS usuarios_clientes (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_completo VARCHAR(120) NOT NULL,
    telefono_movil VARCHAR(15) NOT NULL,
    direccion_popayan VARCHAR(180) NOT NULL,
    email VARCHAR(100) UNIQUE,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 3. Tabla de Pedidos y Transacciones en Producción
CREATE TABLE IF NOT EXISTS pedidos_gourmet (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    codigo_orden VARCHAR(30) UNIQUE NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT DEFAULT 1,
    subtotal_cop DECIMAL(10,2) NOT NULL,
    impoconsumo_8_cop DECIMAL(10,2) NOT NULL,
    total_cop DECIMAL(10,2) NOT NULL,
    metodo_pago VARCHAR(30) DEFAULT 'EFECTIVO_CONTRAENTREGA',
    estado_orden VARCHAR(30) DEFAULT 'EN_HORNO_LEÑA',
    fecha_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios_clientes(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES productos_pizza(id_producto) ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 4. Tabla de Auditoría de Cargas y Despliegue en Producción
CREATE TABLE IF NOT EXISTS auditoria_despliegue_produccion (
    id_auditoria INT AUTO_INCREMENT PRIMARY KEY,
    componente_desplegado VARCHAR(80) NOT NULL,
    plataforma_hosting VARCHAR(100) NOT NULL,
    dominio_asignado VARCHAR(120) NOT NULL,
    estado_salud VARCHAR(25) NOT NULL,
    fecha_publicacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Inserción de Datos Iniciales en Producción
INSERT INTO productos_pizza (nombre_pizza, descripcion_ingredientes, categoria, precio_cop, disponible) VALUES
('Margherita D.O.C.', 'Tomates San Marzano D.O.P., mozzarella di bufala campana, albahaca genovesa y aceite de oliva virgen extra.', 'TRADICIONAL_ITALIANA', 38000.00, TRUE),
('Prosciutto e Funghi', 'Prosciutto crudo madurado 12 meses, champiñones frescos salteados al romero y queso mozzarella fundido.', 'ESPECIAL_GOURMET', 44000.00, TRUE),
('Quattro Formaggi', 'Gorgonzola dulce D.O.P., fontina alpina, provolone ahumado artesanal y lascas de parmigiano reggiano.', 'PREMIUM_SELECCION', 46000.00, TRUE),
('Bella Italia Especial', 'Pepperoni madurado artesanal, tocineta crujiente, tomates secos al balsámico y reducción de frutos rojos.', 'POPAYAN_TOP_CHEF', 48000.00, TRUE);

INSERT INTO usuarios_clientes (nombre_completo, telefono_movil, direccion_popayan, email) VALUES
('Karen Yuliana Campo', '3186681000', 'Calle 5 # 10-30 Barrio Bolívar, Popayán', 'karen.campo@sena.edu.co'),
('Carlos Alberto Martínez', '3157891234', 'Carrera 9 # 4-25 Centro Histórico, Popayán', 'carlos.martinez@popayan.gov.co'),
('María Elena Gómez', '3104567890', 'Calle 67N # 9-40 Barrio Prados del Norte, Popayán', 'maria.gomez@gmail.com');

INSERT INTO pedidos_gourmet (id_usuario, codigo_orden, id_producto, cantidad, subtotal_cop, impoconsumo_8_cop, total_cop, estado_orden) VALUES
(1, 'ORD-PROD-2026-001', 4, 1, 48000.00, 3840.00, 51840.00, 'CONFIRMADO_EN_PREPARACION'),
(2, 'ORD-PROD-2026-002', 1, 1, 38000.00, 3040.00, 41040.00, 'DESPACHADO_A_DOMICILIO');

INSERT INTO auditoria_despliegue_produccion (componente_desplegado, plataforma_hosting, dominio_asignado, estado_salud) VALUES
('Plantilla Web HTML5/CSS3 Gourmet', 'Cloud cPanel Hosting Tradicional', 'pizzeriabellaitalia-popayan.rf.gd', 'SUCCESS_200_OK'),
('Base de Datos Relacional MySQL 8.0', 'Cluster MySQL Producción', 'localhost:3310', 'ACTIVE_HEALTHY');
