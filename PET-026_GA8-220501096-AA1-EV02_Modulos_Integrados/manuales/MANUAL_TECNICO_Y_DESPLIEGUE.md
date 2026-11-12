# MANUAL TÉCNICO DE INSTALACIÓN, CONFIGURACIÓN Y DESPLIEGUE
## Sistema de Gestión, Carta y Pedidos - Pizzería Gourmet Bella Italia Popayán
### Evidencia GA8-220501096-AA1-EV02: Módulos Integrados

---

**Aprendiz:** Karen Yuliana Campo  
**Ficha:** 3186681 — ADSO  
**Centro:** Centro de Teleinformática y Producción Industrial (CTPI) — SENA Regional Cauca  

---

## 1. Topología de Despliegue y URLs de Servicios

Los módulos integrados del sistema se encuentran orquestados y accesibles a través de los siguientes puertos y endpoints:

| Módulo / Servicio | Tecnología | Puerto Host | URL de Acceso Local / LAN | Estado |
|---|---|---|---|---|
| **Frontend Web SPA** | React 18 + Vite | `5173` | `http://localhost:5173` | Activo |
| **Backend RESTful Principal** | Go 1.22 + Fiber v2 | `8085` | `http://localhost:8085` | Activo |
| **Microservicio Auth Secundario** | Node.js Express | `8083` | `http://localhost:8083` | Activo |
| **Microservicio Auditoría** | Spring Boot 3 + Java 17 | `8082` | `http://localhost:8082` | Activo |
| **Aplicación Móvil Metro Bundler** | React Native Expo | `8081` | `http://localhost:8081` | Activo |
| **Base de Datos NoSQL Principal** | MongoDB 6 Jammy | `27017` | `mongodb://localhost:27017` | Saludable |
| **Base de Datos Relacional** | MariaDB 10.5 | `3306` | `localhost:3306` | Saludable |

---

## 2. Prerrequisitos del Entorno

Para realizar el despliegue del software se requiere contar con:
* **Docker Engine:** Versión 24.0 o superior con soporte para Docker Compose v2.
* **Sistema Operativo:** Linux (Ubuntu 22.04 LTS o compatible), Windows 10/11 con WSL2 o macOS.
* **Memoria RAM:** Mínimo 4 GB (Recomendado 8 GB).
* **Puertos de Red Disponibles:** 5173, 8085, 8083, 8082, 8081, 27017 y 3306.

---

## 3. Configuración de Servidores y Variables de Entorno

### 3.1 Backend Go Fiber v2 (`PizzeriaBackendGo`)
El microservicio central se configura mediante las siguientes variables de entorno:

```env
PORT=8085
MONGO_URI=mongodb://sena-mongodb:27017
MONGO_DB=pizzeria_db
JWT_SECRET=SENA_ADSO_3186681_BELLA_ITALIA_GO_FIBER_2026
ALLOW_ORIGINS=*
NODE_ENV=production
```

### 3.2 Base de Datos MongoDB 6 (`sena-mongodb`)
* **Motor de Almacenamiento:** WiredTiger con compresión Snappy y journaling activo.
* **Base de datos inicial:** `pizzeria_db`.
* **Colecciones Principales:**
  * `usuarios`: Índices únicos en campo `usuario` y hashing Bcrypt.
  * `pizzas`: Índice único en `codigo`, índice de texto en `nombre` y `descripcion`.
  * `cupones`: Índice único en `codigo`, campo booleano `activo`.
  * `pedidos`: Índice único en `numeroPedido`, índice cronológico en `fechaCreacion`.

---

## 4. Procedimiento de Puesta en Marcha Paso a Paso

### Paso 1: Clonar el Repositorio de Control de Versiones
```bash
git clone https://github.com/kyulianacampogutierrez-ux/Evidencias.git
cd Evidencias/CDE
```

### Paso 2: Despliegue de la Infraestructura Multi-Contenedor
Ejecutar el archivo de orquestación `docker-compose.yml`:
```bash
docker compose up -d
```

### Paso 3: Verificación de Contenedores y Salud de Servicios
Verificar que los 6 contenedores principales reporten estado `Up`:
```bash
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
```

### Paso 4: Comprobación del Endpoint de Salud (Healthcheck)
```bash
curl -s http://localhost:8085/health | jq .
```
Respuesta esperada:
```json
{
  "database": "MongoDB 6.0 Conectado y Saludable",
  "microservicio": "Pizzeria Bella Italia Backend Go",
  "status": "UP"
}
```

### Paso 5: Ejecución del Test Suite Automatizado
Para ejecutar la batería de 189 pruebas TDD integradas en contenedor:
```bash
./docker-test.sh
```

---

## 5. Mantenimiento y Respaldo de Base de Datos

* **Backup de MongoDB:**
  ```bash
  docker exec sena-mongodb mongodump --db pizzeria_db --out /data/db/backup_$(date +%Y%m%d)
  ```
* **Restauración de MongoDB:**
  ```bash
  docker exec sena-mongodb mongorestore --db pizzeria_db /data/db/backup_20261110/pizzeria_db
  ```
