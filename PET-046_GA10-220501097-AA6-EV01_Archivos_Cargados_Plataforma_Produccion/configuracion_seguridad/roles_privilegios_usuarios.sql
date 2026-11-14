-- ==============================================================================
-- CONFIGURACIÓN DE ROLES, USUARIOS Y PRIVILEGIOS DE SEGURIDAD (PoLP)
-- Evidencia: GA10-220501097-AA6-EV01 - Archivos Cargados en Plataforma Producción
-- Principio de Menor Privilegio (Principle of Least Privilege)
-- Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | SENA CTPI Popayán
-- ==============================================================================

USE pizzeria_produccion_db;

-- 1. Rol de Administrador de Infraestructura y Mantenimiento (DBA)
CREATE USER IF NOT EXISTS 'karen_admin'@'%' IDENTIFIED BY 'AdminPopayanSecure2026!';
GRANT ALL PRIVILEGES ON pizzeria_produccion_db.* TO 'karen_admin'@'%' WITH GRANT OPTION;

-- 2. Rol Operativo de la Aplicación Web (Solo Operaciones DML Necesarias)
CREATE USER IF NOT EXISTS 'pizzeria_app_user'@'%' IDENTIFIED BY 'AppBellaItalia2026!';
-- Restringir DROP, ALTER y comandos DDL destructivos en tiempo de ejecución
GRANT SELECT, INSERT, UPDATE ON pizzeria_produccion_db.productos_pizza TO 'pizzeria_app_user'@'%';
GRANT SELECT, INSERT, UPDATE ON pizzeria_produccion_db.usuarios_clientes TO 'pizzeria_app_user'@'%';
GRANT SELECT, INSERT, UPDATE ON pizzeria_produccion_db.pedidos_gourmet TO 'pizzeria_app_user'@'%';
GRANT INSERT ON pizzeria_produccion_db.auditoria_despliegue_produccion TO 'pizzeria_app_user'@'%';

-- 3. Rol de Auditoría Institucional SENA (Solo Lectura - Read-Only)
CREATE USER IF NOT EXISTS 'auditor_sena'@'%' IDENTIFIED BY 'AuditoriaSena2026!';
GRANT SELECT ON pizzeria_produccion_db.* TO 'auditor_sena'@'%';

-- Aplicar cambios inmediatamente
FLUSH PRIVILEGES;

-- Verificación de Privilegios
SHOW GRANTS FOR 'pizzeria_app_user'@'%';
SHOW GRANTS FOR 'auditor_sena'@'%';
