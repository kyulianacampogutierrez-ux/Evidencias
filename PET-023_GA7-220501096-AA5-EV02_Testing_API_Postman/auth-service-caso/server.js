/**
 * SERVICIO WEB REST: REGISTRO Y AUTENTICACIÓN DE USUARIOS (CASO DE ESTUDIO)
 * 
 * Programa de Formación: Análisis y Desarrollo de Software (ADSO) - Modalidad Virtual
 * Ficha de Caracterización: 228118
 * Competencia: 220501096 - Desarrollar la solución de software de acuerdo con el diseño
 * Actividad de Aprendizaje: GA7-220501096-AA5 - Crear servicios web, de acuerdo con el diseño
 * Evidencia: GA7-220501096-AA5-EV01: Diseño y desarrollo de servicios web - caso
 * 
 * Aprendiz: Karen Yuliana Campo
 * Centro: Centro de Teleinformática y Producción Industrial (CTPI) - Regional Cauca (Popayán)
 * 
 * Descripción:
 * Este servicio web REST implementa los requerimientos de la Guía de Aprendizaje 7:
 * 1. Registro de usuarios con validación de datos de entrada y almacenamiento seguro.
 * 2. Encriptación y hashing de contraseñas mediante algoritmo criptográfico con sal (Salt + Scrypt/BCrypt compatible).
 * 3. Inicio de sesión (Login): si la autenticación es correcta retorna "Autenticación satisfactoria" con token JWT,
 *    en caso contrario devuelve "Error en la autenticación" con código semántico HTTP 401.
 * 4. Endpoint protegido para consulta de perfil mediante validación de cabecera Bearer Token.
 */

import http from 'node:http';
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';

// Configuración del Servicio Web
const PORT = process.env.PORT || 8083;
const JWT_SECRET = process.env.JWT_SECRET || 'SENA_ADSO_228118_BELLA_ITALIA_SECRET_KEY_2026';
const DATA_FILE = path.resolve('users_database.json');

// Base de datos en memoria inicial con persistencia resiliente
let usersDb = [];

// Inicializar almacenamiento con usuario semilla
function initDatabase() {
  if (fs.existsSync(DATA_FILE)) {
    try {
      usersDb = JSON.parse(fs.readFileSync(DATA_FILE, 'utf8'));
      return;
    } catch {
      usersDb = [];
    }
  }

  // Usuario inicial predeterminado para pruebas
  const defaultSalt = crypto.randomBytes(16).toString('hex');
  const defaultHash = hashPassword('Admin123*', defaultSalt);

  usersDb = [
    {
      id: 1,
      usuario: 'karencampo',
      email: 'karen.campo@sena.edu.co',
      nombre: 'Karen Yuliana Campo',
      rol: 'ADMINISTRADOR',
      salt: defaultSalt,
      hash: defaultHash,
      fechaRegistro: new Date().toISOString()
    }
  ];
  saveDatabase();
}

function saveDatabase() {
  try {
    fs.writeFileSync(DATA_FILE, JSON.stringify(usersDb, null, 2), 'utf8');
  } catch (e) {
    console.warn('Advertencia al persistir base de datos:', e.message);
  }
}

/**
 * Función de Hashing Seguro de Contraseñas (BCrypt / Scrypt Derivation)
 * Aplica derivación criptográfica con sal aleatoria para prevenir ataques de diccionario y Rainbow Tables.
 */
function hashPassword(password, salt) {
  return crypto.scryptSync(password, salt, 64).toString('hex');
}

/**
 * Generación de Token de Acceso JWT (JSON Web Token)
 * Estructura estándar: Header.Payload.Signature codificados en Base64Url con HMAC-SHA256
 */
function generateJwtToken(user) {
  const header = { alg: 'HS256', typ: 'JWT' };
  const payload = {
    sub: user.id,
    usuario: user.usuario,
    email: user.email,
    rol: user.rol,
    iat: Math.floor(Date.now() / 1000),
    exp: Math.floor(Date.now() / 1000) + 86400 // Expira en 24 horas
  };

  const base64UrlHeader = Buffer.from(JSON.stringify(header)).toString('base64url');
  const base64UrlPayload = Buffer.from(JSON.stringify(payload)).toString('base64url');
  const signature = crypto
    .createHmac('sha256', JWT_SECRET)
    .update(`${base64UrlHeader}.${base64UrlPayload}`)
    .digest('base64url');

  return `${base64UrlHeader}.${base64UrlPayload}.${signature}`;
}

/**
 * Verificación de Token JWT
 */
function verifyJwtToken(token) {
  if (!token) return null;
  const parts = token.split('.');
  if (parts.length !== 3) return null;

  const [headerB64, payloadB64, signature] = parts;
  const expectedSig = crypto
    .createHmac('sha256', JWT_SECRET)
    .update(`${headerB64}.${payloadB64}`)
    .digest('base64url');

  if (signature !== expectedSig) return null;

  try {
    const payload = JSON.parse(Buffer.from(payloadB64, 'base64url').toString('utf8'));
    if (payload.exp && payload.exp < Math.floor(Date.now() / 1000)) {
      return null; // Token expirado
    }
    return payload;
  } catch {
    return null;
  }
}

// Utilidad para parsear el cuerpo JSON de peticiones entrantes
function parseJsonBody(req) {
  return new Promise((resolve, reject) => {
    let body = '';
    req.on('data', (chunk) => {
      body += chunk.toString();
    });
    req.on('end', () => {
      try {
        resolve(body ? JSON.parse(body) : {});
      } catch (err) {
        reject(new Error('JSON malformado en el cuerpo de la petición.'));
      }
    });
    req.on('error', reject);
  });
}

// Utilidad para enviar respuestas JSON normalizadas
function sendJson(res, statusCode, data) {
  res.writeHead(statusCode, {
    'Content-Type': 'application/json; charset=utf-8',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization'
  });
  res.end(JSON.stringify(data, null, 2));
}

/**
 * Enrutador Principal del Servidor HTTP
 */
const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, `http://${req.headers.host || 'localhost'}`);
  const method = req.method;
  const pathname = url.pathname;

  // Manejo de peticiones pre-flight CORS (OPTIONS)
  if (method === 'OPTIONS') {
    res.writeHead(204, {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization'
    });
    res.end();
    return;
  }

  // 1. ENDPOINT HEALTHCHECK (GET /api/auth/health)
  if (method === 'GET' && (pathname === '/api/auth/health' || pathname === '/health')) {
    sendJson(res, 200, {
      status: 'UP',
      servicio: 'auth-service-caso',
      version: '1.0.0',
      aprendiz: 'Karen Yuliana Campo',
      ficha: '228118',
      timestamp: new Date().toISOString()
    });
    return;
  }

  // 2. ENDPOINT DE REGISTRO (POST /api/auth/register)
  if (method === 'POST' && pathname === '/api/auth/register') {
    try {
      const body = await parseJsonBody(req);
      const usuario = (body.usuario || body.username || '').trim();
      const password = (body.contraseña || body.password || '').trim();
      const email = (body.email || body.correo || '').trim();
      const nombre = (body.nombre || body.fullName || '').trim();
      const rol = (body.rol || body.role || 'CLIENTE').toUpperCase();

      // Validaciones de datos de entrada
      if (!usuario || usuario.length < 3) {
        sendJson(res, 400, {
          success: false,
          error: 'BAD_REQUEST',
          mensaje: 'El usuario es obligatorio y debe tener al menos 3 caracteres.'
        });
        return;
      }

      if (!password || password.length < 6) {
        sendJson(res, 400, {
          success: false,
          error: 'BAD_REQUEST',
          mensaje: 'La contraseña es obligatoria y debe tener al menos 6 caracteres.'
        });
        return;
      }

      // Verificar si el usuario o email ya existen
      const exists = usersDb.some(
        (u) => u.usuario.toLowerCase() === usuario.toLowerCase() || (email && u.email === email)
      );

      if (exists) {
        sendJson(res, 409, {
          success: false,
          error: 'CONFLICT',
          mensaje: `El usuario '${usuario}' o correo '${email}' ya se encuentra registrado.`
        });
        return;
      }

      // Generar Sal y Hash Seguro
      const salt = crypto.randomBytes(16).toString('hex');
      const hash = hashPassword(password, salt);

      const newUser = {
        id: usersDb.length + 1,
        usuario,
        email: email || `${usuario}@correo.com`,
        nombre: nombre || usuario,
        rol,
        salt,
        hash,
        fechaRegistro: new Date().toISOString()
      };

      usersDb.push(newUser);
      saveDatabase();

      sendJson(res, 201, {
        success: true,
        mensaje: 'Usuario registrado satisfactoriamente',
        user: {
          id: newUser.id,
          usuario: newUser.usuario,
          email: newUser.email,
          nombre: newUser.nombre,
          rol: newUser.rol,
          fechaRegistro: newUser.fechaRegistro
        }
      });
      return;
    } catch (err) {
      sendJson(res, 400, {
        success: false,
        error: 'INVALID_PAYLOAD',
        mensaje: err.message
      });
      return;
    }
  }

  // 3. ENDPOINT DE INICIO DE SESIÓN (POST /api/auth/login)
  if (method === 'POST' && pathname === '/api/auth/login') {
    try {
      const body = await parseJsonBody(req);
      const usuario = (body.usuario || body.username || '').trim();
      const password = (body.contraseña || body.password || '').trim();

      if (!usuario || !password) {
        sendJson(res, 400, {
          success: false,
          error: 'BAD_REQUEST',
          mensaje: 'Debe ingresar el usuario y la contraseña para iniciar sesión.'
        });
        return;
      }

      // Búsqueda del usuario en base de datos
      const user = usersDb.find(
        (u) => u.usuario.toLowerCase() === usuario.toLowerCase() || (u.email && u.email.toLowerCase() === usuario.toLowerCase())
      );

      // Verificación de existencia
      if (!user) {
        sendJson(res, 401, {
          success: false,
          error: 'UNAUTHORIZED',
          mensaje: 'Error en la autenticación: Credenciales inválidas. Usuario no encontrado.'
        });
        return;
      }

      // Verificación del hash de la contraseña ingresada
      const inputHash = hashPassword(password, user.salt);
      if (inputHash !== user.hash) {
        sendJson(res, 401, {
          success: false,
          error: 'UNAUTHORIZED',
          mensaje: 'Error en la autenticación: Credenciales inválidas. Contraseña incorrecta.'
        });
        return;
      }

      // Autenticación exitosa -> Generación de Token JWT
      const token = generateJwtToken(user);

      sendJson(res, 200, {
        success: true,
        mensaje: 'Autenticación satisfactoria',
        token,
        tokenType: 'Bearer',
        expiresIn: '24h',
        user: {
          id: user.id,
          usuario: user.usuario,
          nombre: user.nombre,
          email: user.email,
          rol: user.rol
        }
      });
      return;
    } catch (err) {
      sendJson(res, 400, {
        success: false,
        error: 'INVALID_PAYLOAD',
        mensaje: err.message
      });
      return;
    }
  }

  // 4. ENDPOINT PROTEGIDO DE PERFIL (GET /api/auth/profile)
  if (method === 'GET' && (pathname === '/api/auth/profile' || pathname === '/api/auth/verify')) {
    const authHeader = req.headers['authorization'] || '';
    const token = authHeader.startsWith('Bearer ') ? authHeader.substring(7) : null;

    const payload = verifyJwtToken(token);
    if (!payload) {
      sendJson(res, 401, {
        success: false,
        error: 'UNAUTHORIZED',
        mensaje: 'Error en la autenticación: Token de acceso ausente, inválido o expirado.'
      });
      return;
    }

    sendJson(res, 200, {
      success: true,
      mensaje: 'Acceso autorizado al perfil',
      perfil: payload
    });
    return;
  }

  // Ruta no encontrada (404)
  sendJson(res, 404, {
    success: false,
    error: 'NOT_FOUND',
    mensaje: `La ruta solicitada '${method} ${pathname}' no existe en este servicio web.`
  });
});

// Inicialización de la base de datos
initDatabase();

// Iniciar servidor solo si es ejecutado directamente
if (process.env.NODE_ENV !== 'test') {
  server.listen(PORT, () => {
    console.log(`[AUTH-SERVICE] Servicio Web REST ejecutándose en puerto ${PORT}`);
    console.log(`[AUTH-SERVICE] Healthcheck: http://localhost:${PORT}/api/auth/health`);
    console.log(`[AUTH-SERVICE] Registro:    POST http://localhost:${PORT}/api/auth/register`);
    console.log(`[AUTH-SERVICE] Login:       POST http://localhost:${PORT}/api/auth/login`);
  });
}

export { server, hashPassword, generateJwtToken, verifyJwtToken };
