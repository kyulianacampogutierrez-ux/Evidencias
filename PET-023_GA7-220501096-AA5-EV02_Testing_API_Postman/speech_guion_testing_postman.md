# Guion Técnico de Sustentación en Video: Testing de API REST con Postman

- **Evidencia:** GA7-220501096-AA5-EV02: API (Testing de Servicios Web con Postman)
- **Aprendiz:** Karen Yuliana Campo
- **Ficha de Caracterización:** 228118
- **Programa:** Análisis y Desarrollo de Software (ADSO) - Modalidad Virtual
- **Centro:** Centro de Teleinformática y Producción Industrial (CTPI) - Popayán, Cauca
- **Duración Estimada:** 3 a 5 minutos

---

### Segmento 1: Introducción y Presentación Personal (0:00 - 0:45)
> "Cordial saludo, instructor y compañeros del SENA. Mi nombre es **Karen Yuliana Campo**, aprendiz de la tecnología en Análisis y Desarrollo de Software (ADSO) con ficha de caracterización **228118**, perteneciente al Centro de Teleinformática y Producción Industrial (CTPI) de la Regional Cauca en la ciudad de Popayán.  
> En esta oportunidad presento la evidencia **GA7-220501096-AA5-EV02: API**, correspondiente a la Fase de Ejecución. El propósito de esta sesión práctica es demostrar el proceso de pruebas funcionales y de seguridad sobre el microservicio web REST de autenticación y registro de usuarios desarrollado en la evidencia anterior, utilizando la herramienta profesional de testing **Postman**."

---

### Segmento 2: Configuración del Entorno y Herramienta Postman (0:45 - 1:30)
> "Para llevar a cabo las pruebas, hemos preparado una colección estandarizada en formato Postman v2.1 y un archivo de entorno con variables parametrizadas como `base_url`, `test_user`, `test_password` y la variable dinámica `jwt_token`.  
> Nuestro microservicio se encuentra ejecutándose localmente en el puerto `8083`. A continuación, evaluaremos los tres endpoints principales:
> 1. `POST /api/auth/register` para el registro seguro con sal y hashing criptográfico.
> 2. `POST /api/auth/login` para la validación de credenciales con mensajes específicos de éxito y error según la Guía 7.
> 3. `GET /api/auth/profile` como recurso protegido que exige validación del token Bearer JWT."

---

### Segmento 3: Ejecución de Casos de Prueba de Registro (1:30 - 2:30)
> "Iniciamos ejecutando la primera petición: **Registro de Nuevo Usuario**. Enviamos un cuerpo JSON con los datos del usuario operador. Al dar clic en *Send*, Postman recibe una respuesta HTTP con código `201 Created`. En la pestaña de *Test Results* observamos que se aprueban todas las aserciones: el código de estado es 201, se confirma el registro exitoso y se verifica que los datos sensibles como el salt y el hash no sean expuestos en la respuesta pública.  
> Seguidamente, ejecutamos la prueba de **Usuario Duplicado**. Al reintentar enviar el mismo usuario, el microservicio responde con código `409 Conflict`, evitando inconsistencias en la base de datos. Asimismo, al omitir propiedades obligatorias en la prueba de **Parámetros Incompletos**, el servicio responde con `400 Bad Request`."

---

### Segmento 4: Pruebas de Login y Endpoint Protegido (2:30 - 3:45)
> "Pasamos a la prueba crítica de autenticación: **Login Exitoso**. Enviamos las credenciales de mi usuario `karencampo` con la clave correcta. La respuesta devuelve el código `HTTP 200 OK` y el mensaje exacto exigido por la norma curricular: *'Autenticación satisfactoria'*, acompañado del token JWT. Mediante un script automatizado en Postman (`pm.environment.set`), este token se captura de forma automática y se asigna a las variables de entorno.  
> A continuación, evaluamos el caso negativo: **Login Fallido**. Si enviamos una clave incorrecta o un usuario no registrado, el servidor responde con el código semántico `HTTP 401 Unauthorized` y el mensaje exacto: *'Error en la autenticación'*.  
> Finalmente, probamos el endpoint privado `/api/auth/profile`. Cuando enviamos la petición con la cabecera `Authorization: Bearer {{jwt_token}}`, obtenemos un `200 OK` con los datos del perfil activo. Si removemos la cabecera de autorización, el servidor deniega el acceso de inmediato con un `401 Unauthorized`."

---

### Segmento 5: Conclusiones y Cierre (3:45 - 4:15)
> "Como conclusión, hemos verificado el 100% de los casos de prueba previstos mediante la suite automatizada de Postman. Todos los endpoints cumplen a cabalidad con los estándares de la arquitectura REST, códigos HTTP semánticos y las directrices de seguridad de la Guía de Aprendizaje 7.  
> Muchísimas gracias por su atención."
