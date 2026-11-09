# Servicio Web REST: Registro y Autenticación de Usuarios

> **Programa:** Tecnología en Análisis y Desarrollo de Software (ADSO) - Modalidad Virtual  
> **Ficha de Caracterización:** 228118  
> **Actividad de Aprendizaje:** GA7-220501096-AA5 - Crear servicios web, de acuerdo con el diseño  
> **Evidencia:** GA7-220501096-AA5-EV01: Diseño y desarrollo de servicios web - caso  
> **Aprendiz:** Karen Yuliana Campo  
> **Centro:** Centro de Teleinformática y Producción Industrial (CTPI) - Popayán, Cauca  

---

## 📌 Especificación de Endpoints RESTful

### 1. Registro de Usuarios
- **Método / Ruta:** `POST /api/auth/register`
- **Cabeceras:** `Content-Type: application/json`
- **Cuerpo de Petición (Request Body):**
```json
{
  "usuario": "karencampo",
  "password": "PasswordSeguro123*",
  "email": "karen.campo@sena.edu.co",
  "nombre": "Karen Yuliana Campo",
  "rol": "ADMINISTRADOR"
}
```
- **Respuesta Exitosa (`201 Created`):**
```json
{
  "success": true,
  "mensaje": "Usuario registrado satisfactoriamente",
  "user": {
    "id": 2,
    "usuario": "karencampo",
    "email": "karen.campo@sena.edu.co",
    "nombre": "Karen Yuliana Campo",
    "rol": "ADMINISTRADOR",
    "fechaRegistro": "2026-11-08T22:45:00.000Z"
  }
}
```

---

### 2. Inicio de Sesión (Login)
- **Método / Ruta:** `POST /api/auth/login`
- **Cabeceras:** `Content-Type: application/json`
- **Cuerpo de Petición (Request Body):**
```json
{
  "usuario": "karencampo",
  "password": "PasswordSeguro123*"
}
```
- **Respuesta Exitosa (`200 OK`):**
```json
{
  "success": true,
  "mensaje": "Autenticación satisfactoria",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "tokenType": "Bearer",
  "expiresIn": "24h",
  "user": {
    "id": 2,
    "usuario": "karencampo",
    "nombre": "Karen Yuliana Campo",
    "email": "karen.campo@sena.edu.co",
    "rol": "ADMINISTRADOR"
  }
}
```
- **Respuesta Fallida (`401 Unauthorized`):**
```json
{
  "success": false,
  "error": "UNAUTHORIZED",
  "mensaje": "Error en la autenticación: Credenciales inválidas. Contraseña incorrecta."
}
```

---

### 3. Consulta de Perfil Protegido
- **Método / Ruta:** `GET /api/auth/profile`
- **Cabeceras:** `Authorization: Bearer <TOKEN_JWT>`
- **Respuesta Exitosa (`200 OK`):**
```json
{
  "success": true,
  "mensaje": "Acceso autorizado al perfil",
  "perfil": {
    "sub": 2,
    "usuario": "karencampo",
    "email": "karen.campo@sena.edu.co",
    "rol": "ADMINISTRADOR",
    "exp": 1731195600
  }
}
```

---

## 🚀 Despliegue y Ejecución

```bash
# Iniciar el servicio en el puerto 8083
node server.js
```
O con Docker:
```bash
docker run -d --name auth-service-caso -p 8083:8083 -v $(pwd):/app -w /app node:20-alpine node server.js
```
