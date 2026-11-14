-- ==============================================================================
-- BASE DE DATOS: PIZZERÍA GOURMET BELLA ITALIA POPAYÁN
-- ESQUEMA TÉCNICO INICIALIZADO - EVIDENCIA GA10-220501097-AA10-EV01
-- ==============================================================================

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

CREATE DATABASE IF NOT EXISTS pizzeria_manual_tecnico_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE pizzeria_manual_tecnico_db;

-- 1. Tabla de Roles y Permisos RBAC
CREATE TABLE IF NOT EXISTS tbl_roles_permisos (
  id_rol INT AUTO_INCREMENT PRIMARY KEY,
  nombre_rol VARCHAR(50) NOT NULL UNIQUE,
  descripcion VARCHAR(255) NOT NULL,
  nivel_acceso INT NOT NULL DEFAULT 1,
  fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO tbl_roles_permisos (id_rol, nombre_rol, descripcion, nivel_acceso) VALUES
(1, 'SuperAdministrador', 'Control total de configuración, usuarios e inventario', 10),
(2, 'CajeroFacturador', 'Gestión de cobro, arqueo de caja y emisión de facturas DIAN', 5),
(3, 'JefeCocina', 'Visualización de comandas, control de tiempos y recetas', 3),
(4, 'Domiciliario', 'Recepción de despachos, geolocalización y confirmación de entrega', 2)
ON DUPLICATE KEY UPDATE nombre_rol=VALUES(nombre_rol);

-- 2. Tabla de Usuarios
CREATE TABLE IF NOT EXISTS tbl_usuarios (
  id_usuario INT AUTO_INCREMENT PRIMARY KEY,
  id_rol INT NOT NULL,
  nombre_completo VARCHAR(120) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  telefono VARCHAR(20) NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  estado ENUM('ACTIVO', 'INACTIVO', 'BLOQUEADO') DEFAULT 'ACTIVO',
  ultimo_acceso DATETIME NULL,
  fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_usuario_rol FOREIGN KEY (id_rol) REFERENCES tbl_roles_permisos(id_rol) ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO tbl_usuarios (id_usuario, id_rol, nombre_completo, email, telefono, password_hash) VALUES
(1, 1, 'Karen Yuliana Campo', 'karen.campo@pizzeriabellaitalia.com', '3157894512', '$2y$12$e8Yk1.7B5R6y19/Y9iI69uvG3l5R2tGv889YF2tN1/1P.Q8N3/O5W'),
(2, 2, 'Danilo Administrador', 'danilo@pizzeriabellaitalia.com', '3128906734', '$2y$12$a4b8c9d0e1f2g3h4i5j6k7l8m9n0o1p2q3r4s5t6u7v8w9x0y1z2a'),
(3, 3, 'Marco Rossi (Chef)', 'chef@pizzeriabellaitalia.com', '3189998877', '$2y$12$b5c9d0e1f2g3h4i5j6k7l8m9n0o1p2q3r4s5t6u7v8w9x0y1z2a3b'),
(4, 4, 'Carlos Domicilios', 'carlos.domi@pizzeriabellaitalia.com', '3201112233', '$2y$12$c6d0e1f2g3h4i5j6k7l8m9n0o1p2q3r4s5t6u7v8w9x0y1z2a3b4c')
ON DUPLICATE KEY UPDATE email=VALUES(email);

-- 3. Tabla de Categorías del Menú
CREATE TABLE IF NOT EXISTS tbl_categorias (
  id_categoria INT AUTO_INCREMENT PRIMARY KEY,
  nombre_categoria VARCHAR(60) NOT NULL UNIQUE,
  descripcion VARCHAR(255) NOT NULL,
  icono_url VARCHAR(255) NULL,
  orden_visualizacion INT DEFAULT 0,
  activo BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO tbl_categorias (id_categoria, nombre_categoria, descripcion, orden_visualizacion) VALUES
(1, 'Pizzas Tradicionales', 'Recetas clásicas italianas con masa fermentada 48 horas', 1),
(2, 'Pizzas Gourmet Popayán', 'Combinaciones premium con ingredientes típicos del Cauca', 2),
(3, 'Calzones Horneados', 'Masa rellena sellada a la piedra con queso mozzarella', 3),
(4, 'Bebidas Artesanales', 'Gaseosas italianas, cervezas artesanales y jugos naturales', 4)
ON DUPLICATE KEY UPDATE nombre_categoria=VALUES(nombre_categoria);

-- 4. Tabla de Productos del Menú
CREATE TABLE IF NOT EXISTS tbl_productos_menu (
  id_producto INT AUTO_INCREMENT PRIMARY KEY,
  id_categoria INT NOT NULL,
  sku VARCHAR(30) NOT NULL UNIQUE,
  nombre_producto VARCHAR(100) NOT NULL,
  descripcion TEXT NOT NULL,
  precio_unitario DECIMAL(12,2) NOT NULL,
  tiempo_coccion_min INT NOT NULL DEFAULT 15,
  disponible BOOLEAN DEFAULT TRUE,
  stock_disponible INT DEFAULT 100,
  imagen_url VARCHAR(255) NULL,
  CONSTRAINT fk_producto_categoria FOREIGN KEY (id_categoria) REFERENCES tbl_categorias(id_categoria) ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO tbl_productos_menu (id_producto, id_categoria, sku, nombre_producto, descripcion, precio_unitario, tiempo_coccion_min) VALUES
(1, 1, 'PIZ-MARG-01', 'Pizza Margherita Tradizionale', 'Salsa de tomate San Marzano, mozzarella fior di latte, albahaca fresca y AOVE', 35000.00, 12),
(2, 2, 'PIZ-CAUCA-02', 'Pizza Gourmet Pipíán del Cauca', 'Base artesanal con pipián tradicional de Popayán, queso campesino de Silvia y hogao gourmet', 48000.00, 16),
(3, 3, 'CALZ-NAPO-03', 'Calzone Napolitano Ripieno', 'Relleno de ricotta fresca, jamón serrano, mozzarella y toque de pimienta negra', 42000.00, 18),
(4, 4, 'BEB-LIMON-04', 'Limonada de Coco Caucana', 'Bebida refrescante a base de leche de coco natural y limones frescos de la región', 12000.00, 5)
ON DUPLICATE KEY UPDATE sku=VALUES(sku);

-- 5. Tabla de Pedidos
CREATE TABLE IF NOT EXISTS tbl_pedidos (
  id_pedido INT AUTO_INCREMENT PRIMARY KEY,
  codigo_orden VARCHAR(30) NOT NULL UNIQUE,
  id_cliente INT NOT NULL,
  canal_origen ENUM('WEB', 'MOVIL', 'SALON', 'TELEFONO') DEFAULT 'WEB',
  estado_pedido ENUM('RECIBIDO', 'EN_COCINA', 'EN_REPARTO', 'ENTREGADO', 'CANCELADO') DEFAULT 'RECIBIDO',
  subtotal_cop DECIMAL(12,2) NOT NULL,
  iva_cop DECIMAL(12,2) NOT NULL,
  total_cop DECIMAL(12,2) NOT NULL,
  direccion_entrega VARCHAR(200) NOT NULL,
  coordenadas_gps VARCHAR(50) NULL,
  fecha_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_pedido_cliente FOREIGN KEY (id_cliente) REFERENCES tbl_usuarios(id_usuario) ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO tbl_pedidos (id_pedido, codigo_orden, id_cliente, canal_origen, estado_pedido, subtotal_cop, iva_cop, total_cop, direccion_entrega) VALUES
(1, 'ORD-202611-001', 1, 'WEB', 'ENTREGADO', 70000.00, 13300.00, 83300.00, 'Carrera 4 # 6-25, Centro Histórico, Popayán'),
(2, 'ORD-202611-002', 2, 'MOVIL', 'ENTREGADO', 48000.00, 9120.00, 57120.00, 'Calle 5 # 10-33, Barrio La Estancia, Popayán')
ON DUPLICATE KEY UPDATE codigo_orden=VALUES(codigo_orden);

-- 6. Tabla de Detalle del Pedido
CREATE TABLE IF NOT EXISTS tbl_detalle_pedido (
  id_detalle INT AUTO_INCREMENT PRIMARY KEY,
  id_pedido INT NOT NULL,
  id_producto INT NOT NULL,
  cantidad INT NOT NULL DEFAULT 1,
  precio_unitario DECIMAL(12,2) NOT NULL,
  subtotal_linea DECIMAL(12,2) NOT NULL,
  notas_chef VARCHAR(150) NULL,
  CONSTRAINT fk_detalle_pedido FOREIGN KEY (id_pedido) REFERENCES tbl_pedidos(id_pedido) ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT fk_detalle_producto FOREIGN KEY (id_producto) REFERENCES tbl_productos_menu(id_producto) ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO tbl_detalle_pedido (id_detalle, id_pedido, id_producto, cantidad, precio_unitario, subtotal_linea, notas_chef) VALUES
(1, 1, 1, 2, 35000.00, 70000.00, 'Masa bien tostada en borde'),
(2, 2, 2, 1, 48000.00, 48000.00, 'Sin picante extra')
ON DUPLICATE KEY UPDATE id_detalle=VALUES(id_detalle);

-- 7. Tabla de Facturación Electrónica DIAN
CREATE TABLE IF NOT EXISTS tbl_facturas_dian (
  id_factura INT AUTO_INCREMENT PRIMARY KEY,
  id_pedido INT NOT NULL UNIQUE,
  numero_factura VARCHAR(40) NOT NULL UNIQUE,
  cufe VARCHAR(100) NOT NULL UNIQUE,
  qr_code_url VARCHAR(255) NOT NULL,
  monto_total DECIMAL(12,2) NOT NULL,
  estado_dian ENUM('ACEPTADA', 'RECHAZADA', 'CONTINGENCIA') DEFAULT 'ACEPTADA',
  fecha_emision TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_factura_pedido FOREIGN KEY (id_pedido) REFERENCES tbl_pedidos(id_pedido) ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO tbl_facturas_dian (id_factura, id_pedido, numero_factura, cufe, qr_code_url, monto_total) VALUES
(1, 1, 'FE-POPY-0001', 'fe9a2b4c6e8f0123456789abcdef0123456789abcdef0123456789abcdef01', 'https://dian.gov.co/qr/fe9a2b4c6e', 83300.00),
(2, 2, 'FE-POPY-0002', 'fe8c1d3e5a7b90123456789abcdef0123456789abcdef0123456789abcdef02', 'https://dian.gov.co/qr/fe8c1d3e5a', 57120.00)
ON DUPLICATE KEY UPDATE numero_factura=VALUES(numero_factura);

-- 8. Tabla de Auditoría y Trazabilidad Forense
CREATE TABLE IF NOT EXISTS tbl_auditoria_logs (
  id_log BIGINT AUTO_INCREMENT PRIMARY KEY,
  id_usuario INT NULL,
  accion VARCHAR(50) NOT NULL,
  tabla_afectada VARCHAR(50) NOT NULL,
  id_registro_afectado INT NULL,
  ip_origen VARCHAR(45) NOT NULL,
  fecha_evento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  detalles_json JSON NULL,
  CONSTRAINT fk_log_usuario FOREIGN KEY (id_usuario) REFERENCES tbl_usuarios(id_usuario) ON UPDATE CASCADE ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO tbl_auditoria_logs (id_log, id_usuario, accion, tabla_afectada, id_registro_afectado, ip_origen, detalles_json) VALUES
(1, 1, 'INICIALIZACION_SISTEMA', 'tbl_usuarios', 1, '127.0.0.1', '{"evento": "Despliegue inicial de software", "version": "1.0.0"}')
ON DUPLICATE KEY UPDATE id_log=VALUES(id_log);

SET FOREIGN_KEY_CHECKS = 1;
