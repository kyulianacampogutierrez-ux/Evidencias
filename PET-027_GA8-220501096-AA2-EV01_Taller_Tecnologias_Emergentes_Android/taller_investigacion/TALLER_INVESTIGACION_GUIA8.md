# TALLER: INTEGRACIÓN, TECNOLOGÍAS EMERGENTES Y DISRUPTIVAS MÓVILES (ANDROID 14+)
## GA8-220501096-AA2-EV01

---

### METADATOS INSTITUCIONALES DEL PROYECTO
- **Programa de Formación:** Tecnología en Análisis y Desarrollo de Software (ADSO)
- **Número de Ficha:** 3186681
- **Aprendiz:** Karen Yuliana Campo
- **Centro de Formación:** Centro de Teleinformática y Producción Industrial (CTPI Popayán)
- **Regional:** Regional Cauca - Servicio Nacional de Aprendizaje (SENA)
- **Proyecto Formativo:** Sistema Integral de Comercio Electrónico y Gestión Operativa - *Pizzería Gourmet Bella Italia Popayán*
- **Competencia:** 220501096 - Desarrollar la solución de software de acuerdo con el diseño y metodologías de desarrollo.
- **Resultado de Aprendizaje (RAP):** Desarrollar la aplicación móvil de acuerdo con las tecnologías seleccionadas y especificaciones técnicas.
- **Evidencia Evaluada:** GA8-220501096-AA2-EV01: Taller. Integración, tecnologías emergentes y disruptivas.
- **Fecha de Elaboración:** Noviembre de 2026

---

## 1. INTRODUCCIÓN Y JUSTIFICACIÓN TÉCNICA

El desarrollo de aplicaciones para dispositivos móviles representa uno de los pilares más determinantes de la industria informática contemporánea. En el marco del proyecto formativo **Pizzería Gourmet Bella Italia Popayán**, la experiencia del cliente final y la agilidad de los operadores en punto de venta exigen canales móviles de alta fidelidad, reactividad inmediata y máxima seguridad en el procesamiento de transacciones.

El presente taller aborda dos dimensiones fundamentales:
1. **Dimensión Teórica e Investigativa:** Profundización en los conceptos estructurales de la plataforma Android, su pila arquitectónica basada en el Kernel Linux, el formato ejecutable APK frente a AAB, las especificaciones del Android SDK, la evolución de los lenguajes de programación (Java y Kotlin frente a tecnologías emergentes como React Native), los entornos de desarrollo integrado (IDEs), el aislamiento de procesos mediante arquitectura multiusuario de Linux, el Principio de Menor Privilegio (PoLP) y los cuatro componentes esenciales de una aplicación.
2. **Dimensión Práctica y de Ingeniería:** Implementación y compilación de dos aplicaciones móviles funcionales orientadas a **Android 14 (API Level 34)**:
   - **Aplicación Móvil Nativa (Java/Gradle):** Construida desde cero con arquitectura Android pura, Activity principal interactiva, catálogo de especialidades artesanales, validación del cupón `SENA2026 (-15%)` y simulación de pedidos.
   - **Aplicación Móvil Híbrida/Multiplataforma (React Native / Expo):** Generada a partir del ecosistema JavaScript/TypeScript de la pizzería.
   - **Entorno de Compilación Aislado mediante Docker:** Cumpliendo estrictamente con la directriz de ingeniería de **cero polución en la máquina anfitriona**, prescindiendo de la instalación de Android Studio y emuladores pesados en el host, implementando una imagen Dockerizada basada en OpenJDK 17, Gradle 8.5/9.x y las herramientas oficiales de línea de comandos de Android SDK (`cmdline-tools`, `platforms;android-34`, `build-tools;34.0.0`).

> ### 📌 OBSERVACIÓN TÉCNICA Y ALCANCE DE LAS ENTREGAS:
> 1. **No se instaló Android Studio por su gran tamaño:** Debido al elevado peso en disco (más de 25 GB) y alto consumo de memoria RAM de Android Studio, se utilizó **Visual Studio Code** como editor ligero y ágil, gestionando la compilación a través de un entorno hermético en **Docker** (OpenJDK 17, Gradle y Android SDK Command-line Tools).
> 2. **Aplicación Nativa para Cumplimiento de la Guía:** Se desarrolló y compiló una **aplicación nativa en Java orientada a Android 14 (API 34)** para dar estricta solución técnica a cada uno de los puntos requeridos en la evidencia formativa.
> 3. **Aplicación React Native para el Proyecto Formativo:** Para la solución integral del proyecto formativo (*Pizzería Gourmet Bella Italia Popayán*), se compiló una aplicación moderna en **React Native**, generando la **APK Release Standalone** con el bundle JavaScript completamente embebido (`index.android.bundle`), eliminando la dependencia del servidor de desarrollo Metro.
> 4. **Se adjuntan ambas APKs:** En la entrega y dentro de `KARENCAMPO_AA2_EV01.zip` se adjuntan:
>    - `pizzeria-bella-italia-nativa.apk` (12 MB) - Solución nativa Java Android 14+.
>    - `pizzeria-bella-italia-rn.apk` (61 MB) - Solución React Native Release Standalone.

---

## 2. SECCIÓN 1: INVESTIGACIÓN CONCEPTUAL DEL ECOSISTEMA ANDROID

### 2.1 ¿Qué es Android?
**Android** es un sistema operativo móvil de código abierto (basado en el proyecto AOSP - *Android Open Source Project*) desarrollado principalmente por Google y la *Open Handset Alliance*. Diseñado específicamente para dispositivos con pantalla táctil como teléfonos inteligentes, tabletas, televisores inteligentes (*Android TV*), automóviles (*Android Auto*) y dispositivos portátiles (*Wear OS*).

#### Pila Arquitectónica de Android (Capas de Software):
1. **Kernel Linux:** Base del sistema operativo. Provee abstracción de hardware, gestión de memoria virtual, controladores de dispositivos (cámara, Wi-Fi, Bluetooth, pantalla), gestión de procesos, seguridad y aislamiento de red. En versiones recientes (Android 14) opera sobre núcleos Linux 5.15 LTS y 6.1 LTS.
2. **Capa de Abstracción de Hardware (HAL - Hardware Abstraction Layer):** Interfaces estandarizadas en C/C++ que exponen las capacidades de los componentes físicos a la capa del marco de trabajo Java, sin que este deba conocer los detalles específicos del silicio o del fabricante (Qualcomm, MediaTek, Google Tensor).
3. **Android Runtime (ART) y Librerías Nativas C/C++:** 
   - **ART:** Entorno de ejecución que sustituyó a la máquina virtual Dalvik a partir de Android 5.0. Utiliza un modelo híbrido de compilación anticipada (**AOT - Ahead-Of-Time**), compilación en tiempo de ejecución (**JIT - Just-In-Time**) y perfiles guiados (*Profile-Guided Compilation*), optimizando el consumo de batería y la velocidad de apertura de aplicaciones mediante la ejecución de archivos bytecode DEX (*Dalvik Executable*).
   - **Librerías Nativas:** Motores gráficos (Vulkan, OpenGL ES), WebKit/Blink, SQLite, libc y SSL/BoringSSL.
4. **Marco de Trabajo de la Aplicación (Java API Framework / Android Jetpack):** Conjunto integral de clases y servicios reutilizables que permiten a los desarrolladores acceder a las funciones del teléfono: `ActivityManager`, `PackageManager`, `NotificationManager`, `LocationManager`, `TelephonyManager` y librerías modernas de Jetpack (Room, Compose, Navigation, WorkManager).
5. **Capa de Aplicaciones de Usuario:** Nivel superior donde residen las aplicaciones del sistema (Teléfono, Contactos, Navegador) y las aplicaciones de terceros desarrolladas por ingenieros de software, como la aplicación de la *Pizzería Bella Italia*.

---

### 2.2 Definición del Concepto de APK y Estructura Interna
Un **APK (Android Package Kit o Android Application Package)** es el formato de archivo empaquetado y firmado que utiliza el sistema operativo Android para distribuir e instalar aplicaciones móviles. Es técnicamente un archivo comprimido basado en el estándar ZIP con una extensión `.apk`.

#### Anatomía y Estructura Interna de un Archivo APK:
- `AndroidManifest.xml` (en formato binario compilado AXML): Define la identidad de la aplicación, nombre de paquete, versión, permisos requeridos (`INTERNET`, `POST_NOTIFICATIONS`), actividades, servicios, receptores y proveedores declarados.
- `classes.dex` (y `classes2.dex`, etc. en caso de multidex): Contiene el código fuente compilado en bytecode Dalvik/ART ejecutable por el motor virtual de Android.
- `res/`: Contiene los recursos gráficos y multimedia compilados que no están en assets (layouts XML binarios, imágenes drawables, valores de texto en strings).
- `resources.arsc`: Tabla de recursos compilados que mapea los IDs numéricos hexadecimales generados por la clase `R` (`R.id.btnValidar`, `R.string.app_name`) con los recursos concretos.
- `assets/`: Archivos raw y estáticos empaquetados por la aplicación (fuentes tipográficas, modelos de machine learning, bundles JavaScript en React Native).
- `lib/`: Librerías compartidas nativas compiladas en código máquina C/C++ (`.so`) organizadas por arquitectura ABI (`arm64-v8a`, `armeabi-v7a`, `x86_64`).
- `META-INF/`: Directorio crítico que contiene los metadatos de firma digital (`CERT.SF`, `CERT.RSA`, `MANIFEST.MF`) que garantizan la integridad, no repudio y autenticidad del autor de la aplicación.

#### Esquemas de Firma Digital en Android:
- **v1 (JAR Signature):** Firma básica de archivos individuales dentro del ZIP.
- **v2 (Full APK Signature - Android 7.0+):** Protege la totalidad del archivo binario APK contra modificaciones no autorizadas en bloques de metadatos.
- **v3 (Android 9.0+) y v4 (Android 11+):** Permiten la rotación de claves criptográficas y streaming de instalación ultra-rápida.

*Nota Técnica sobre AAB (Android App Bundle):* Desde agosto de 2021, Google Play Store exige la publicación en formato `.aab` para distribución en tienda, delegando en los servidores de Google la generación dinámica de APKs optimizados para cada dispositivo del usuario (*Split APKs*). No obstante, el formato final descargado, montado y ejecutado en el dispositivo físico continúa siendo invariablemente el formato `.apk`.

---

### 2.3 ¿Qué es el Android SDK?
El **Android SDK (Software Development Kit)** es el conjunto completo de herramientas, bibliotecas de desarrollo, compiladores, emuladores y documentación técnica proporcionado por Google para diseñar, codificar, probar y empaquetar software para la plataforma Android.

#### Componentes Principales del SDK:
1. **Command-Line Tools (`cmdline-tools`):** Herramientas de consola autónomas, encabezadas por `sdkmanager`, que permiten consultar, descargar y actualizar componentes del SDK sin requerir una interfaz gráfica (indispensable para entornos de integración continua CI/CD y contenedores Docker como el utilizado en esta evidencia).
2. **Android Platforms (`platforms;android-XX`):** Archivos `android.jar` que contienen las definiciones de la API de cada versión de Android. Para esta entrega se implementa la plataforma **`android-34`**, correspondiente a Android 14.
3. **Build-Tools (`build-tools;XX.Y.Z`):** Utilidades de bajo nivel para la compilación y empaquetado:
   - `aapt` / `aapt2` (*Android Asset Packaging Tool*): Compila recursos XML y genera el índice `resources.arsc` y la clase `R.java`.
   - `d8` / `r8`: Compilador de bytecode Java (`.class`) a Dalvik Executable (`.dex`), así como optimizador, ofuscador y reductor de código (*tree-shaking*).
   - `zipalign`: Herramienta de alineación de memoria a 4 bytes para optimizar el mapeo de memoria en ejecución (`mmap`).
   - `apksigner`: Firma criptográfica de paquetes con esquemas v2/v3/v4.
4. **Platform-Tools:** Herramientas de comunicación con dispositivos y emuladores, primordialmente **ADB (*Android Debug Bridge*)** y *fastboot*.

#### Parámetros Críticos de Configuración en `build.gradle`:
- `compileSdk` (34): Especifica contra qué versión de la API de Android se compila el código fuente. Permite utilizar las clases y métodos más modernos de Android 14.
- `minSdk` (34): Establece el nivel mínimo de versión de Android requerido para instalar y ejecutar la aplicación. En este taller, se configuró en 34 para garantizar compatibilidad estricta con Android 14 en adelante.
- `targetSdk` (34): Indica la versión de Android para la cual se probó y optimizó la aplicación, habilitando los comportamientos modernos de seguridad y gestión de memoria del sistema operativo.

---

### 2.4 Lenguajes Utilizados para Desarrollar Aplicaciones Android
El ecosistema de desarrollo de Android admite múltiples paradigmas y lenguajes de programación:

1. **Kotlin (Oficial - Preferido / Kotlin-First):**
   - Declarado por Google en el Google I/O 2019 como el lenguaje principal y recomendado para el desarrollo de Android.
   - 100% interoperable con Java, con seguridad frente a nulos en tiempo de compilación (*Null Safety*), corrutinas para programación asíncrona no bloqueante y sintaxis concisa y expresiva.
2. **Java (Clásico / Fundacional):**
   - Lenguaje sobre el cual se cimentó Android desde su versión 1.0. Robusto, tipado estático, ampliamente documentado en el sector educativo e industrial. Para Android 14 se utiliza la especificación **OpenJDK 17**, con soporte para registros, patrones y mejoras en la máquina virtual.
3. **C / C++ (NDK - Native Development Kit):**
   - Utilizado mediante JNI (*Java Native Interface*) para módulos que demandan cómputo extremo en tiempo real: motores gráficos de videojuegos (Unreal Engine, Unity), codificación/decodificación de video, visión artificial y procesamiento de audio de baja latencia.
4. **Lenguajes Web y Frameworks Híbridos/Multiplataforma:**
   - **JavaScript / TypeScript (React Native / Expo):** Permite escribir lógica de negocio una sola vez y renderizar componentes visuales verdaderamente nativos mediante puentes de comunicación asíncronos y la arquitectura *Fabric / TurboModules* con motor JavaScript Hermes.
   - **Dart (Flutter):** Compila directamente a código máquina nativo utilizando su propio motor de renderizado gráfico Skia/Impeller.

---

### 2.5 Entornos de Desarrollo Integrado (IDEs) Existentes
Para la codificación, depuración y construcción de aplicaciones Android existen diversas herramientas:

1. **Android Studio:** El IDE oficial respaldado por Google, basado en IntelliJ IDEA de JetBrains. Incluye asistentes gráficos de diseño de interfaces, perfiles de consumo de memoria y CPU, analizador de APKs y gestor de dispositivos virtuales (AVD). *Desventaja:* Elevado consumo de memoria RAM (mínimo 8-16 GB) y dependencia de entornos de escritorio pesados.
2. **Visual Studio Code (VS Code):** Editor liviano y altamente extensible. Mediante extensiones como *Android Tools*, *Extension Pack for Java*, *Gradle for Java* y *React Native Tools*, ofrece un entorno de desarrollo altamente ágil, ideal para arquitecturas híbridas y desarrollo web/móvil simultáneo.
3. **IntelliJ IDEA Community / Ultimate:** Plataforma de cabecera para desarrollos complejos en Java y Kotlin, con soporte nativo de Gradle y plugins de Android.
4. **Entornos de Integración Continua (CI/CD) Headless con Gradle y Docker (Enfoque de esta Evidencia):** 
   - Prescinde totalmente de interfaces gráficas e instalaciones invasivas en el host.
   - Utiliza la herramienta de automatización de compilación **Gradle** orquestada dentro de contenedores **Docker**, garantizando compilaciones idénticas, reproducibles e inmutables en cualquier servidor de integración continua (GitHub Actions, GitLab CI, Jenkins).

---

### 2.6 Concepto de Android Multiusuario
El concepto de **multiusuario en Android** combina dos niveles de aislamiento:

#### 1. Aislamiento por Procesos y Usuarios del Kernel Linux (Sandbox de Aplicaciones):
En un sistema operativo Linux tradicional, los usuarios son personas que inician sesión. En Android, **cada aplicación instalada es tratada como un usuario independiente del sistema operativo**. 
- A cada paquete se le asigna un Identificador de Usuario único (**UID**) del tipo `u0_a123` y un Identificador de Grupo (**GID**).
- Cada aplicación corre en su propio proceso de Linux con un espacio de memoria virtual completamente aislado.
- El sistema de archivos privado de la aplicación (`/data/user/0/<nombre_paquete>/`) posee permisos de lectura y escritura restringidos exclusivamente para ese UID (`chmod 700`). Ninguna otra aplicación puede acceder directamente a sus bases de datos SQLite o preferencias compartidas, a menos que se exponga explícitamente mediante un `ContentProvider`.

#### 2. Soporte Multiusuario a Nivel de Personas y Perfiles:
A partir de Android 5.0+, el sistema soporta perfiles de usuario físico múltiples en un mismo dispositivo:
- **Usuario Principal (Propietario / Owner):** Primer usuario configurado en el terminal.
- **Usuario Secundario / Invitado (Guest):** Entorno temporal sin acceso a los datos, llamadas ni fotos del usuario principal.
- **Perfil de Trabajo (Work Profile):** Espacio corporativo cifrado gestionado por políticas MDM (*Mobile Device Management*), separando aplicaciones de trabajo de las personales.

---

### 2.7 Principio de Mínimo Privilegio (PoLP - Principle of Least Privilege)
El **Principio de Mínimo Privilegio** establece que todo módulo, proceso o usuario del sistema debe disponer únicamente de los recursos, datos y permisos que sean estrictamente necesarios para cumplir su función legítima, ni uno más, ni por más tiempo del estrictamente requerido.

#### Aplicación y Evolución en Android:
1. **Permisos en Tiempo de Instalación (Android 1.0 a 5.1):**
   - El usuario aceptaba en bloque todos los permisos solicitados por la aplicación al momento de descargarla de la tienda. Si la aplicación solicitaba acceso a la cámara o a los contactos, no había forma de denegarlo individualmente.
2. **Permisos en Tiempo de Ejecución (Runtime Permissions - Android 6.0 Marshmallow en adelante):**
   - La aplicación solo puede solicitar permisos considerados peligrosos (*Dangerous Permissions*: Ubicación, Cámara, Micrófono, Contactos) en el momento exacto en que el usuario ejecuta una acción que los requiere. El usuario puede concederlos o denegarlos libremente en cualquier momento desde los ajustes del sistema.
3. **Seguridad Granular Avanzada en Android 14 (API 34):**
   - **Acceso Selectivo a Fotos y Videos:** El usuario ya no está forzado a dar acceso a toda su galería; puede otorgar acceso exclusivamente a una o dos fotos seleccionadas mediante el nuevo *Photo Picker* del sistema.
   - **Permiso Explícito de Notificaciones (`POST_NOTIFICATIONS`):** Ninguna aplicación puede enviar notificaciones push sin la autorización activa del usuario.
   - **Transparencia en Compartición de Datos:** El sistema alerta explícitamente si una aplicación comparte la ubicación con redes de publicidad externas.
   - **Bloqueo de Instalación de Aplicaciones Legadas:** Android 14 bloquea de forma predeterminada la instalación de aplicaciones con `targetSdk` inferior a 23, mitigando ataques de malware que intentaban burlar el sistema de permisos en tiempo de ejecución.

---

### 2.8 Componentes Esenciales de una Aplicación Android
Toda aplicación para Android se estructura alrededor de cuatro bloques de construcción fundamentales, orquestados por el sistema operativo mediante **Intents**:

| Componente | Definición y Propósito | Ejemplo en Pizzería Bella Italia |
| :--- | :--- | :--- |
| **Activity** | Representa una pantalla individual con interfaz gráfica de usuario (UI) interactiva. Gestiona eventos de toque y responde a su ciclo de vida (`onCreate`, `onStart`, `onResume`, `onPause`, `onStop`, `onDestroy`). | `MainActivity`: Pantalla de inicio con el banner gourmet, bienvenida y botones de navegación. |
| **Service** | Componente sin interfaz visual que ejecuta operaciones en segundo plano de larga duración. Puede ser de primer plano (*Foreground Service*, con notificación visible obligatoria) o en segundo plano (*Background Service* gestionado por WorkManager). | `ServicioRastreoDomicilio`: Mantiene activa la actualización por GPS de la ubicación del repartidor de pizza. |
| **BroadcastReceiver** | Componente reactivo que escucha y responde a anuncios o transmisiones globales del sistema operativo o de otras apps. No tiene interfaz gráfica, pero puede disparar notificaciones o iniciar servicios. | `ReceptorConectividad`: Detecta si el dispositivo recuperó la conexión a Internet para sincronizar órdenes pendientes. |
| **ContentProvider** | Mecanismo estandarizado para almacenar y compartir conjuntos estructurados de datos entre diferentes aplicaciones mediante una interfaz URI (`content://...`). | `ProveedorCatalogoPizzas`: Permite que un widget de pantalla consulte de forma segura el menú sin acceder a la base de datos interna. |

#### El Rol de los `Intents`:
Los **Intents** son objetos de mensajería asíncrona que actúan como el pegamento de comunicación entre componentes:
- **Intents Explícitos:** Especifican exactamente la clase de destino a invocar (p. ej., `new Intent(this, DetallePizzaActivity.class)`).
- **Intents Implícitos:** Solicitan una acción general al sistema sin indicar qué aplicación específica debe resolverla (p. ej., abrir un número telefónico en la app de llamadas, compartir el recibo de la pizzería por WhatsApp o abrir una ubicación en Google Maps).

---


---

## 3. SECCIÓN 2: DESARROLLO PRÁCTICO DEL TALLER (CREACIÓN DE LA APLICACIÓN ANDROID)

### 3.1 Justificación de la Arquitectura Dockerizada (Cero Polución del Host)
En estricto cumplimiento de las directrices técnicas del proyecto y la solicitud del aprendiz, **se prescindió absolutamente de la instalación de Android Studio y emuladores en la máquina anfitriona**. 

#### Motivos de Ingeniería para el Enfoque Docker:
1. **Inmutabilidad y Reproducibilidad:** Una imagen de Docker encapsula con exactitud quirúrgica la versión de OpenJDK (17.0.21), el binario de compilación Gradle (8.5 / 9.x) y los paquetes del Android SDK (`platforms;android-34`, `build-tools;34.0.0`). Cualquier desarrollador del equipo o servidor de integración continua ejecutará la compilación bajo condiciones 100% idénticas.
2. **Eficiencia de Recursos del Sistema:** Android Studio y los emuladores basados en QEMU consumen entre 8 GB y 16 GB de RAM, además de ocupar más de 25 GB en disco duro. El contenedor de compilación Docker optimizado ocupa menos de 2 GB y consume recursos únicamente durante los segundos en que se ejecuta la tarea de compilación.
3. **Alineación con Estándares de la Industria (DevOps y CI/CD):** En las grandes empresas tecnológicas y factorías de software, los artefactos de producción (`.apk` y `.aab`) nunca se compilan de forma manual en el IDE del desarrollador; se generan de forma desatendida mediante pipelines de integración continua en contenedores headless.

---

### 3.2 Configuración del Contenedor de Compilación (`pizzeria-android-builder:34`)
Se diseñó un `Dockerfile` especializado con las siguientes capas:

```dockerfile
FROM eclipse-temurin:17-jdk

LABEL maintainer="Karen Yuliana Campo <karencampo@sena.edu.co>"
LABEL description="Entorno Dockerizado de Compilación Android 14 (API 34) con OpenJDK 17 y Gradle 8.5"

ENV DEBIAN_FRONTEND=noninteractive
ENV ANDROID_HOME=/opt/android-sdk
ENV ANDROID_SDK_ROOT=/opt/android-sdk
ENV GRADLE_HOME=/opt/gradle-8.5
ENV PATH="${PATH}:${GRADLE_HOME}/bin:${ANDROID_HOME}/cmdline-tools/latest/bin:${ANDROID_HOME}/platform-tools:${ANDROID_HOME}/build-tools/34.0.0"

# Dependencias del sistema y Node.js para bundling
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl unzip git bash ca-certificates gnupg \
    && mkdir -p /etc/apt/keyrings \
    && curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg \
    && echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_20.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list \
    && apt-get update && apt-get install -y --no-install-recommends nodejs \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Descarga de Gradle 8.5
RUN curl -fsSL -o /tmp/gradle-8.5-bin.zip https://services.gradle.org/distributions/gradle-8.5-bin.zip \
    && unzip -q /tmp/gradle-8.5-bin.zip -d /opt \
    && rm /tmp/gradle-8.5-bin.zip \
    && ln -s /opt/gradle-8.5/bin/gradle /usr/local/bin/gradle

# Android Command-Line Tools e instalación de API 34
RUN mkdir -p ${ANDROID_HOME}/cmdline-tools \
    && curl -fsSL -o /tmp/cmdline-tools.zip https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip \
    && unzip -q /tmp/cmdline-tools.zip -d ${ANDROID_HOME}/cmdline-tools \
    && mv ${ANDROID_HOME}/cmdline-tools/cmdline-tools ${ANDROID_HOME}/cmdline-tools/latest \
    && rm /tmp/cmdline-tools.zip \
    && yes | sdkmanager --licenses \
    && sdkmanager --install "platform-tools" "platforms;android-34" "build-tools;34.0.0"

WORKDIR /workspace
```

---

### 3.3 Estructura del Proyecto Nativo Android 14 (`PizzeriaBellaItaliaNative`)
El proyecto se organizó bajo el estándar canónico de proyectos Android Gradle:

```
app_nativa_android/
├── build.gradle                   # Configuración raíz de plugins (AGP 8.2.2)
├── gradle.properties              # Parámetros de la JVM y AndroidX
├── settings.gradle                # Declaración de repositorios y módulos (:app)
└── app/
    ├── build.gradle               # compileSdk 34, minSdk 34, targetSdk 34
    └── src/
        └── main/
            ├── AndroidManifest.xml # Permisos INTERNET, POST_NOTIFICATIONS
            ├── java/co/edu/sena/pizzerianativa/
            │   ├── MainActivity.java           # Actividad interactiva principal
            │   ├── model/Pizza.java            # POJO de Pizza artesanal
            │   └── adapter/PizzaAdapter.java   # Adaptador de RecyclerView
            └── res/
                ├── layout/
                │   ├── activity_main.xml       # UI principal con Cards y RecyclerView
                │   └── item_pizza.xml          # Plantilla visual de cada pizza
                └── values/
                    ├── colors.xml              # Paleta corporativa Bella Italia
                    ├── strings.xml             # Textos y mensajes requeridos
                    └── themes.xml              # Tema Material Components
```

---

### 3.4 Implementación del Código Fuente Principal

#### 1. Archivo de Configuración de Módulo (`app/build.gradle`):
```groovy
plugins {
    id 'com.android.application'
}

android {
    namespace 'co.edu.sena.pizzerianativa'
    compileSdk 34

    defaultConfig {
        applicationId "co.edu.sena.pizzerianativa"
        minSdk 34
        targetSdk 34
        versionCode 1
        versionName "1.0.0"
        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
            signingConfig signingConfigs.debug
        }
        debug {
            applicationIdSuffix ".debug"
            debuggable true
        }
    }
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_17
        targetCompatibility JavaVersion.VERSION_17
    }
}

dependencies {
    implementation 'androidx.appcompat:appcompat:1.6.1'
    implementation 'com.google.android.material:material:1.11.0'
    implementation 'androidx.constraintlayout:constraintlayout:2.1.4'
    implementation 'androidx.cardview:cardview:1.0.0'
    implementation 'androidx.recyclerview:recyclerview:1.3.2'
}
```

#### 2. Manifiesto de la Aplicación (`AndroidManifest.xml`):
```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.POST_NOTIFICATIONS" />

    <application
        android:allowBackup="true"
        android:label="@string/app_name"
        android:supportsRtl="true"
        android:theme="@style/Theme.PizzeriaBellaItalia"
        android:usesCleartextTraffic="true">
        
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:label="@string/app_name"
            android:theme="@style/Theme.PizzeriaBellaItalia">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
```

#### 3. Actividad Principal (`MainActivity.java`):
Cumple integralmente con el requerimiento de la Guía 8:
- Muestra el mensaje institucional de bienvenida del proyecto formativo.
- Carga el catálogo de 4 pizzas gourmet mediante un `RecyclerView`.
- Valida interactivamente el cupón `SENA2026` aplicando el descuento del 15%.
- Simula la emisión de una orden de pedido hacia el backend de Popayán.

---

### 3.5 Proceso de Compilación y Generación de Artefactos APK en Docker
La compilación se ejecutó de forma desacoplada dentro del contenedor Docker:

```bash
docker run --rm \
  -v $(pwd)/app_nativa_android:/workspace \
  -w /workspace \
  pizzeria-android-builder:34 \
  gradle assembleDebug --no-daemon
```

#### Resultado de la Compilación Nativa:
- **Estado:** `BUILD SUCCESSFUL in 1m 7s`
- **Tareas ejecutadas:** 31 tareas accionables (`processDebugResources`, `compileDebugJavaWithJavac`, `dexBuilderDebug`, `mergeProjectDexDebug`, `packageDebug`).
- **Artefacto generado:** `pizzeria-bella-italia-nativa.apk` (12 MB).

#### Verificación Técnica con `aapt badging`:
```
package: name='co.edu.sena.pizzerianativa.debug' versionCode='1' versionName='1.0.0'
platformBuildVersionName='14' platformBuildVersionCode='34'
compileSdkVersion='34' compileSdkVersionCodename='14'
sdkVersion:'34'
targetSdkVersion:'34'
uses-permission: name='android.permission.INTERNET'
uses-permission: name='android.permission.ACCESS_NETWORK_STATE'
uses-permission: name='android.permission.POST_NOTIFICATIONS'
application-label:'Pizzería Bella Italia Popayán'
launchable-activity: name='co.edu.sena.pizzerianativa.MainActivity'
```

---

### 3.6 Comparativa Técnica: Arquitectura Nativa Java vs. React Native Multiplataforma

| Dimensión Técnica | Versión Nativa Android (Java + Gradle) | Versión Multiplataforma (React Native / Expo) |
| :--- | :--- | :--- |
| **Lenguaje de Programación** | Java 17 / Kotlin | JavaScript ES6+ / TypeScript |
| **Tiempo de Compilación** | 1 min 07 seg (compilación directa a DEX) | 2 a 4 min (requiere empaquetado JS + Hermes + Gradle) |
| **Tamaño del APK Resultante** | ~12 MB (solo código compilado y recursos) | ~35 a 55 MB (incluye motor JS Hermes y librerías C++ de Fabric) |
| **Consumo de Memoria RAM** | Muy bajo (~40 - 70 MB en runtime) | Moderado (~90 - 160 MB en runtime) |
| **Rendimiento de Interfaz (FPS)** | 60 - 120 FPS directos en el hilo UI nativo | 60 FPS consistentes gracias a la arquitectura Fabric |
| **Acceso a Hardware y APIs** | Acceso directo al 100% de APIs del SDK 34 | Depende de módulos nativos (*TurboModules* / Native Modules) |
| **Portabilidad a Otras Plataformas** | Exclusivo para Android | Código compartido >85% con iOS y Web |
| **Velocidad de Iteración en Desarrollo** | Requiere recompilación y relanzamiento | Soporte instantáneo de Fast Refresh / Hot Reload |

---

## 4. CONCLUSIONES

1. **Eficiencia y Limpieza Arquitectónica:** Se demostró fehacientemente que es posible configurar un entorno industrial completo de desarrollo y empaquetado para Android 14 (API 34) utilizando exclusivamente Docker, OpenJDK 17 y Gradle, garantizando cero impacto e instalación en el sistema anfitrión.
2. **Cumplimiento de Especificaciones de Guía 8:** Se desarrollaron a profundidad todos los puntos teóricos de la Sección 1 (Arquitectura Android, APK, SDK, Lenguajes, IDEs, Multiusuario, Principio de Mínimo Privilegio y Componentes Esenciales) y se implementó una aplicación nativa completa con su actividad interactiva, catálogo y eventos funcionales requeridos en la Sección 2.
3. **Perspectiva del Proyecto Bella Italia:** Disponer de una aplicación móvil nativa junto con la solución multiplataforma en React Native brinda al proyecto formativo una doble ventaja estratégica: máxima optimización y cercanía al hardware para terminales de punto de venta (versión nativa), y máxima velocidad de desarrollo y despliegue multiplataforma para clientes domiciliarios (versión React Native).
