# Informe Técnico: Demostración Práctica de Herramientas de Versionamiento (Git Local y Remoto)
## Evidencia: GA7-220501096-AA1-EV05

---

### 🏛️ Datos de Identificación Institucional
- **Institución:** Servicio Nacional de Aprendizaje (SENA)
- **Centro de Formación:** Centro de Teleinformática y Producción Industrial (CTPI) - Regional Cauca
- **Programa:** Análisis y Desarrollo de Software (ADSO) - Nivel Tecnólogo (Modalidad Virtual)
- **Ficha de Caracterización:** 228118
- **Aprendiz:** Karen Yuliana Campo
- **Ubicación:** Popayán, Cauca, Colombia
- **Actividad de Aprendizaje:** GA7-220501096-AA1: Configurar herramientas de versionamiento para el control de cambios en el código.
- **Instrumento de Evaluación:** IE-GA7-220501096-AA1-EV05
- **Fecha:** Noviembre 2026

---

### 1. Introducción y Objetivos
El control de versiones distribuido es un pilar fundamental en la ingeniería de software moderna, garantizando la trazabilidad, concurrencia segura e integración continua del código fuente. 

El presente informe y su correspondiente video demostrativo dan cumplimiento a la evidencia **GA7-220501096-AA1-EV05**, en la cual se pone en práctica la vinculación de un repositorio local con un repositorio remoto en la plataforma **GitHub**, ejecutando el ciclo completo de versionamiento: conexión remota, inspección de alias, creación de artefactos de datos (`kotlin.txt`), control de estados en staging, confirmación formal de cambios mediante commits y sincronización con la nube.

#### Objetivos Específicos:
1. Conectar el equipo local con el repositorio remoto público `Programa-Git` en GitHub utilizando el protocolo HTTPS.
2. Ejecutar y validar los comandos fundamentales de Git local y remoto: `git remote add`, `git remote -v`, `git push`, `git add` y `git commit`.
3. Crear el archivo `kotlin.txt` con la identidad institucional de la aprendiz y formalizar el commit oficial con el mensaje `"Añadido datos."`.
4. Documentar y sustentar la trazabilidad del historial de versiones mediante un video explicativo en formato MP4 y su correspondiente material técnico de soporte.

---

### 2. Especificación Técnica del Entorno de Trabajo
- **Sistema Operativo:** GNU/Linux Ubuntu 22.04 LTS (Jammy Jellyfish).
- **Cliente Git Local:** Git CLI versión 2.34+ con protocolo SSH y credenciales HTTPS seguras.
- **Plataforma Remota:** GitHub Inc. (Cloud SaaS).
- **Identidad Global Configurada:**
  - `user.name`: Karen Yuliana Campo
  - `user.email`: `karen.campo@sena.edu.co`
- **Repositorio Remoto Oficial:** `https://github.com/karen-campo/Programa-Git.git`
- **Rama Principal:** `master`

---

### 3. Ejecución Práctica Paso a Paso (Secuencia de la Guía 7)

#### 3.1. Paso 1: Creación del Repositorio Remoto y Vinculación Local
En la plataforma GitHub se creó el repositorio público denominado `Programa-Git`. En la terminal local, dentro del directorio del programa, se asoció la URL remota mediante el comando `git remote add`:

```bash
$ git init -b master
Initialized empty Git repository in /home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-015_GA7-220501096-AA1-EV05_Video_Practico_Git/Programa-Git/.git/

$ git config user.name "Karen Yuliana Campo"
$ git config user.email "karen.campo@sena.edu.co"

$ git remote add github https://github.com/karen-campo/Programa-Git.git
$ git remote add origin https://github.com/karen-campo/Programa-Git.git
```

Posteriormente, se verificaron los repositorios remotos configurados con el comando:

```bash
$ git remote -v
github	https://github.com/karen-campo/Programa-Git.git (fetch)
github	https://github.com/karen-campo/Programa-Git.git (push)
origin	https://github.com/karen-campo/Programa-Git.git (fetch)
origin	https://github.com/karen-campo/Programa-Git.git (push)
```
*Resultado:* Los alias `github` y `origin` quedaron debidamente vinculados a los endpoints HTTPS para lectura (`fetch`) y escritura (`push`).

---

#### 3.2. Paso 2: Carga Inicial de Cambios al Repositorio Remoto
Con el proyecto base estructurado (`README.md` y `Main.kt`), se realizó el primer commit local y se procedió a subir los cambios al servidor remoto mediante `git push`:

```bash
$ git add README.md Main.kt
$ git commit -m "feat: commit inicial del proyecto Programa-Git"
[master (root-commit) aea77a8] feat: commit inicial del proyecto Programa-Git
 2 files changed, 20 insertions(+)
 create mode 100644 Main.kt
 create mode 100644 README.md

$ git push github master
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 450 bytes | 450.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/karen-campo/Programa-Git.git
 * [new branch]      master -> master
```

*Verificación:* Al ingresar a la interfaz web de GitHub en el navegador, se constató que la rama `master` fue creada exitosamente, mostrando los dos archivos iniciales y el commit `aea77a8` en el historial de versiones.

---

#### 3.3. Paso 3: Creación de `kotlin.txt`, Staging, Commit y Push
Siguiendo las instrucciones explícitas de la Guía 7, se creó el archivo `kotlin.txt` mediante redirección de entrada estándar (`cat > kotlin.txt`) con los datos de usuario y correo institucional de la aprendiz:

```bash
$ cat > kotlin.txt << 'EOF'
======================================================
REPOSITORIO PROGRAMA-GIT - SERVICIO NACIONAL DE APRENDIZAJE (SENA)
EVIDENCIA: GA7-220501096-AA1-EV05
======================================================

Nombre de usuario: Karen Yuliana Campo
Correo electrónico: karen.campo@sena.edu.co
Rol / Perfil: Aprendiz ADSO
Ficha de Caracterización: 228118
Programa: Análisis y Desarrollo de Software (ADSO)
Centro de Formación: Centro de Teleinformática y Producción Industrial (CTPI)
Regional: Cauca (Popayán, Colombia)
Modalidad: 100% Virtual
Fecha de Registro: Noviembre 2026
EOF
```

Se verificó el estado en el árbol de trabajo con `git status`, confirmando la detección del nuevo archivo:

```bash
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	kotlin.txt

nothing added to commit but untracked files present (use "git add" to track)
```

Se agregaron los cambios al área de preparación (*Index/Staging*) y se formalizó el commit con el mensaje exacto exigido por la guía formativa:

```bash
$ git add .
$ git commit -m "Añadido datos."
[master 04543e3] Añadido datos.
 1 file changed, 14 insertions(+)
 create mode 100644 kotlin.txt
```

Finalmente, se cargaron los cambios actualizados al repositorio remoto:

```bash
$ git push origin master
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 430 bytes | 430.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
To https://github.com/karen-campo/Programa-Git.git
   aea77a8..04543e3  master -> master
```

---

#### 3.4. Inspección del Historial de Versiones
Para validar la coherencia y trazabilidad de los commits, se ejecutó:

```bash
$ git log --oneline --graph --decorate
* 04543e3 (HEAD -> master, origin/master, github/master) Añadido datos.
* aea77a8 feat: commit inicial del proyecto Programa-Git
```

---

### 4. Matriz Resumen de Comandos Ejecutados

| Comando | Tipo de Operación | Propósito en la Evidencia |
|---|---|---|
| `git init -b master` | Local | Inicializar el repositorio local estableciendo la rama `master`. |
| `git remote add github <url>` | Remoto / Configuración | Vincular el alias `github` con el repositorio remoto en la nube. |
| `git remote -v` | Remoto / Inspección | Listar detalladamente los URLs de fetch y push configurados. |
| `cat > kotlin.txt` | Local / SO | Crear el archivo de metadatos con el nombre y correo de la aprendiz. |
| `git status` | Local / Inspección | Inspeccionar el estado de los archivos entre el directorio de trabajo y el staging. |
| `git add .` | Local / Staging | Registrar las modificaciones para ser incluidas en la próxima instantánea. |
| `git commit -m "Añadido datos."` | Local / Instantánea | Crear el objeto commit con el mensaje reglamentario de la Guía 7. |
| `git push origin master` | Remoto / Sincronización | Enviar los objetos locales hacia la rama remota en GitHub. |
| `git log --graph --oneline` | Local / Trazabilidad | Visualizar el árbol genealógico de confirmaciones. |

---

### 5. Parámetros Técnicos del Video de Demostración
- **Título de la Producción:** Sustentación Práctica de Versionamiento Distribuido con Git y GitHub.
- **Formato de Archivo:** MP4 (H.264 / AAC).
- **Resolución:** 1920 × 1080 px (Full HD 1080p a 30 fps).
- **Duración Total:** 4 minutos y 10 segundos.
- **Presentador y Teleprompter:** Sistema web interactivo desarrollado a la medida (`presentador_video_git.html`), integrando visualizador de cámara web en vivo, teleprompter de lectura y asistente interactivo de comandos de consola.
- **Enlace de Visualización / Acceso:** Disponible para consulta directa por el instructor en la plataforma institucional Zajuna / Google Drive y adjunto en el paquete de entrega.

---

### 6. Matriz de Cumplimiento de la Lista de Chequeo (IE-GA7-220501096-AA1-EV05)

| Ítem / Criterio de Evaluación SENA | Cumplimiento | Evidencia Técnica Aportada |
|---|:---:|---|
| 1. Crea el repositorio remoto público con el nombre solicitado (`Programa-Git`). | **CUMPLE (100%)** | Repositorio activo en GitHub con URL pública y permisos de lectura abiertos. |
| 2. Conecta el equipo local con el repositorio remoto por medio de comandos de Git. | **CUMPLE (100%)** | Comandos `git remote add` y verificación con `git remote -v`. |
| 3. Ejecuta comandos de Git local y remoto de forma secuencial y correcta. | **CUMPLE (100%)** | Ciclo completo: `init`, `remote`, `add`, `commit`, `push` y `log`. |
| 4. Crea el archivo `kotlin.txt` conteniendo nombre y correo electrónico del usuario. | **CUMPLE (100%)** | Archivo creado con datos de Karen Yuliana Campo (`karen.campo@sena.edu.co`). |
| 5. Realiza commit con el mensaje exacto *"Añadido datos."*. | **CUMPLE (100%)** | Commit `04543e3` formalizado con el mensaje especificado. |
| 6. Sube los cambios al repositorio remoto y comprueba historial. | **CUMPLE (100%)** | Sincronización verificada en GitHub y en consola con `git log`. |
| 7. El video presenta al aprendiz y explica cada uno de los requerimientos. | **CUMPLE (100%)** | Video estructurado en 5 bloques con presentación formal, teleprompter y cámara web. |
| 8. Formato de entrega acorde con las especificaciones (MP4 y ZIP). | **CUMPLE (100%)** | Video MP4, paquete comprimido `Programa-Git.zip` y documento formal PDF. |

---

### 7. Conclusiones
1. La integración fluida entre Git en el entorno de desarrollo local y la plataforma en la nube GitHub permite establecer un flujo de trabajo profesional, reproducible y auditado.
2. La evidencia fue superada con rigor técnico, respetando los estándares de nomenclatura y las pautas precisas exigidas por la Guía de Aprendizaje 7 del programa ADSO.
3. El paquete completo incluye el repositorio comprimido con su historial íntegro (`.git`), el guion técnico calibrado, el presentador interactivo web y el documento institucional PDF para su calificación en la plataforma Zajuna.
