-- ==============================================================================
-- BASE DE DATOS: PIZZERÍA GOURMET BELLA ITALIA POPAYÁN
-- Evidencia: GA10-220501097-AA5-EV01 - Configuración de Servicios, BD y Software
-- Servidor de Base de Datos: MySQL 8.0 en Linux (Ubuntu/Debian)
-- Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán - Regional Cauca
-- ==============================================================================

CREATE DATABASE IF NOT EXISTS pizzeria_bella_italia_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE pizzeria_bella_italia_db;

-- 1. Tabla de Catálogo Gourmet
CREATE TABLE IF NOT EXISTS productos_pizza (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre_pizza VARCHAR(100) NOT NULL,
    descripcion_ingredientes TEXT NOT NULL,
    categoria VARCHAR(40) NOT NULL,
    precio_cop DECIMAL(10,2) NOT NULL,
    disponible BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2. Tabla de Usuarios y Clientes
CREATE TABLE IF NOT EXISTS usuarios_clientes (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_completo VARCHAR(120) NOT NULL,
    telefono_movil VARCHAR(15) NOT NULL,
    direccion_popayan VARCHAR(180) NOT NULL,
    email VARCHAR(100) UNIQUE,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 3. Tabla de Pedidos y Transacciones
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

-- 4. Tabla de Auditoría de Servicios de la Plataforma
CREATE TABLE IF NOT EXISTS auditoria_servicios (
    id_auditoria INT AUTO_INCREMENT PRIMARY KEY,
    servicio_auditado VARCHAR(50) NOT NULL,
    estado_salud VARCHAR(20) NOT NULL,
    version_software VARCHAR(80) NOT NULL,
    ip_origen VARCHAR(45) NOT NULL,
    fecha_chequeo TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Inserción de Datos Iniciales (Seed Data)
INSERT INTO productos_pizza (nombre_pizza, descripcion_ingredientes, categoria, precio_cop, disponible) VALUES
('Margherita D.O.C.', 'Tomates San Marzano, mozzarella di bufala fior di latte, albahaca fresca y aceite de oliva virgen extra de primera prensa.', 'TRADICIONAL_ITALIANA', 38000.00, TRUE),
('Prosciutto e Funghi', 'Jamón serrano curado 12 meses, champiñones frescos salteados al ajillo, salsa pomodoro y queso mozzarella fundido.', 'ESPECIAL_GOURMET', 44000.00, TRUE),
('Quattro Formaggi', 'Sinfonía noble de queso gorgonzola D.O.P., fontina alpina, provolone ahumado y láminas de parmigiano reggiano.', 'PREMIUM_SELECCION', 46000.00, TRUE),
('Bella Italia Especial', 'Pepperoni madurado artesanal, tocineta ahumada crujiente, tomates secos marinados al romero y reducción de balsámico.', 'POPAYAN_TOP_CHEF', 48000.00, TRUE);

INSERT INTO usuarios_clientes (nombre_completo, telefono_movil, direccion_popayan, email) VALUES
('Karen Yuliana Campo', '3186681000', 'Calle 5 # 10-30 Barrio Bolívar, Popayán', 'karen.campo@sena.edu.co'),
('Carlos Alberto Martínez', '3157891234', 'Carrera 9 # 4-25 Centro Histórico, Popayán', 'carlos.martinez@popayan.gov.co'),
('María Elena Gómez', '3104567890', 'Calle 67N # 9-40 Barrio Prados del Norte, Popayán', 'maria.gomez@gmail.com');

INSERT INTO pedidos_gourmet (id_usuario, codigo_orden, id_producto, cantidad, subtotal_cop, impoconsumo_8_cop, total_cop, estado_orden) VALUES
(1, 'ORD-2026-POPAYAN-001', 4, 1, 48000.00, 3840.00, 51840.00, 'CONFIRMADO_EN_PREPARACION'),
(2, 'ORD-2026-POPAYAN-002', 1, 1, 38000.00, 3040.00, 41040.00, 'DESPACHADO_A_DOMICILIO');

INSERT INTO auditoria_servicios (servicio_auditado, estado_salud, version_software, ip_origen) VALUES
('Servidor Web Apache', 'HEALTHY', 'Apache/2.4 (Debian/Ubuntu Linux)', '172.28.0.10'),
('Base de Datos MySQL', 'HEALTHY', 'MySQL Community Server 8.0', '172.28.0.20');
