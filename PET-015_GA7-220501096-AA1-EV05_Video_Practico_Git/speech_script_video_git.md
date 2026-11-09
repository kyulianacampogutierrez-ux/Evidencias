# Guion Técnico y Discurso de Grabación: Video Demostrativo de Git
## Evidencia: GA7-220501096-AA1-EV05 - Herramientas de Versionamiento (GIT) Instalada y Configurada

- **Programa de Formación:** Análisis y Desarrollo de Software (ADSO) - Modalidad 100% Virtual
- **Ficha de Caracterización:** 228118
- **Aprendiz:** Karen Yuliana Campo
- **Centro de Formación:** Centro de Teleinformática y Producción Industrial (CTPI) - Regional Cauca, Popayán
- **Formato:** Video MP4 (1080p Full HD)
- **Duración Estimada:** 3 minutos y 45 segundos a 4 minutos y 30 segundos
- **Herramienta de Grabación Recomendada:** OBS Studio / SimpleScreenRecorder / Presentador Web Interactivo

---

### ⏱️ Estructura Cronológica del Video

| Bloque | Tiempo Estimado | Contenido y Acción en Pantalla |
|---|---|---|
| **Bloque 1: Introducción y Presentación** | 0:00 - 0:45 (45s) | Cámara activa, presentación formal de la aprendiz Karen Yuliana Campo, ficha 228118, objetivo de la evidencia y componentes a demostrar. |
| **Bloque 2: Paso 1 - Vinculación Remota** | 0:45 - 1:40 (55s) | Repositorio público `Programa-Git` en GitHub, comando `git remote add github <url>`, inspección con `git remote -v`. |
| **Bloque 3: Paso 2 - Primer Push y Verificación** | 1:40 - 2:30 (50s) | Subida de cambios al repositorio remoto con `git push github master`, inspección en el portal web de GitHub y visualización de commits. |
| **Bloque 4: Paso 3 - Ciclo kotlin.txt y Commit** | 2:30 - 3:35 (65s) | Creación de `kotlin.txt` (`cat > kotlin.txt`), revisión de estado con `git status`, staging con `git add .`, commit con mensaje `"Añadido datos."`, y push al remoto. |
| **Bloque 5: Inspección de Historial y Conclusión** | 3:35 - 4:15 (40s) | Visualización del grafo de historial con `git log --graph --oneline`, verificación final en GitHub y despedida profesional. |

---

### 📜 Discurso Completo Paso a Paso (Transcripción para Teleprompter)

#### 🎙️ Bloque 1: Presentación Institucional (0:00 - 0:45)
> "¡Un cordial saludo a los instructores y compañeros del Servicio Nacional de Aprendizaje (SENA)!  
> Mi nombre es **Karen Yuliana Campo**, aprendiz del tecnólogo en **Análisis y Desarrollo de Software (ADSO)** con ficha de caracterización **228118**, perteneciente al Centro de Teleinformática y Producción Industrial de la Regional Cauca, adelantando mi formación en modalidad cien por ciento virtual desde la ciudad de Popayán.  
> 
> En este video práctico daremos cumplimiento a la evidencia **GA7-220501096-AA1-EV05: Herramientas de versionamiento (GIT) instalada y configurada**, correspondiente a la Actividad de Aprendizaje 1 de la Guía 7.  
> Demostraremos en tiempo real la conexión del entorno local con el repositorio remoto de GitHub, la ejecución de los comandos fundamentales de versionamiento, la creación del archivo de control `kotlin.txt` y la sincronización de ramas con confirmación de historial."

---

#### 🎙️ Bloque 2: Paso 1 - Creación y Vinculación Remota del Repositorio (0:45 - 1:40)
*(Acción en pantalla: Mostrar la consola de comandos abierta en la carpeta del proyecto y el navegador en GitHub)*

> "Para dar inicio al **Paso 1**, nos encontramos en nuestro directorio de trabajo local donde tenemos el proyecto base denominado `Programa-Git`. Previamente hemos inicializado nuestro repositorio con `git init`, configurando nuestra identidad global con mi nombre `Karen Yuliana Campo` y mi correo institucional `karen.campo@sena.edu.co`.  
> 
> En GitHub hemos creado el nuevo repositorio público llamado `Programa-Git`. Para vincular este repositorio remoto a nuestro proyecto local mediante el protocolo HTTPS, ejecutamos en la terminal:  
> `git remote add github https://github.com/karen-campo/Programa-Git.git`  
> 
> Inmediatamente procedemos a verificar los orígenes remotos configurados ejecutando:  
> `git remote -v`  
> Como podemos observar en la salida, el alias `github` ha quedado registrado correctamente tanto para la operación de recuperación `fetch` como para la operación de envío `push`."

---

#### 🎙️ Bloque 3: Paso 2 - Carga Inicial y Verificación en GitHub (1:40 - 2:30)
*(Acción en pantalla: Ejecutar el push y cambiar de ventana al navegador web para actualizar GitHub)*

> "Avanzamos al **Paso 2** de la guía. En nuestro repositorio local ya contamos con un commit inicial que incluye la estructura base del programa (`README.md` y `Main.kt`).  
> Ahora transferiremos estos cambios locales hacia la rama remota de GitHub. Para ello ejecutamos el comando:  
> `git push github master`  
> 
> El cliente Git procesa la compresión de objetos y la transferencia cifrada vía TLS. Una vez completado, nos dirigimos a la interfaz web de GitHub y recargamos la página.  
> Podemos constatar que el repositorio remoto ya contiene los archivos cargados, reflejando el primer commit en el historial de versiones con su respectivo hash criptográfico SHA-1."

---

#### 🎙️ Bloque 4: Paso 3 - Adición de `kotlin.txt` y Commit Oficial (2:30 - 3:35)
*(Acción en pantalla: Crear el archivo mediante cat en consola, verificar con status, agregar, commitear y pushear)*

> "Continuamos con el **Paso 3** propuesto en la guía formativa. Procedemos a crear en el directorio raíz un archivo llamado `kotlin.txt` que contendrá mi información de usuario y correo institucional.  
> Lo generamos directamente desde consola con:  
> `cat > kotlin.txt`  
> 
> Ingresamos el nombre completo: `Karen Yuliana Campo`, mi correo institucional: `karen.campo@sena.edu.co`, mi ficha de formación `228118` y la regional Cauca.  
> Al verificar el estado de los archivos con:  
> `git status`  
> Git detecta que `kotlin.txt` es un archivo no rastreado (*Untracked files*).  
> 
> Preparamos los cambios en el *Staging Area* ejecutando:  
> `git add .`  
> 
> A continuación, formalizamos el cambio realizando un commit con el mensaje exacto solicitado por la Guía de Aprendizaje 7:  
> `git commit -m "Añadido datos."`  
> 
> Git confirma la creación del commit `04543e3` con 1 archivo cambiado y 14 inserciones.  
> Finalmente, cargamos estos nuevos cambios al servidor remoto mediante:  
> `git push origin master`  
> (o utilizando el alias remoto `github`)."

---

#### 🎙️ Bloque 5: Inspección del Grafo de Historial y Cierre (3:35 - 4:15)
*(Acción en pantalla: Ejecutar git log y mostrar el árbol de commits sincronizado)*

> "Para finalizar y validar la integridad de la evidencia, ejecutamos en la terminal:  
> `git log --oneline --graph --decorate`  
> 
> Podemos apreciar con total claridad la trazabilidad del repositorio:  
> En la base tenemos el commit inicial del proyecto, y en la cúspide el commit `"Añadido datos."`, en el cual la rama local `master` se encuentra perfectamente alineada con la rama remota `github/master`.  
> 
> Al consultar nuevamente el portal de GitHub, evidenciamos que el archivo `kotlin.txt` se encuentra disponible con su contenido íntegro y que el historial refleja con exactitud la secuencia cronológica de cambios.  
> 
> De esta forma queda demostrada la correcta instalación, configuración y operatividad de Git y GitHub bajo estándares profesionales para el desarrollo colaborativo en el marco del programa ADSO.  
> ¡Muchas gracias por su atención y hasta una próxima oportunidad!"

---

### 📋 Checklist de Grabación para la Aprendiz
- [ ] Iluminación adecuada en rostro y micrófono calibrado sin eco.
- [ ] Cámara web ubicada en la esquina superior derecha o inferior derecha para no tapar la terminal.
- [ ] Terminal con tamaño de fuente legible (16px a 18px, tema oscuro de buen contraste).
- [ ] Ventana de navegador con GitHub abierta en `https://github.com/karen-campo/Programa-Git`.
- [ ] Tiempo objetivo: Entre 3m30s y 5m00s.
