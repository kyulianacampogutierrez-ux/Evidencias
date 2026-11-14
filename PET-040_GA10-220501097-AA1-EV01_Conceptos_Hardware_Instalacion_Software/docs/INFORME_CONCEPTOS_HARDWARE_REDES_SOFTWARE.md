# SERVICIO NACIONAL DE APRENDIZAJE - SENA
## CENTRO DE TELEINFORMÁTICA Y PRODUCCIÓN INDUSTRIAL (CTPI) - REGIONAL CAUCA
### TECNOLOGÍA EN ANÁLISIS Y DESARROLLO DE SOFTWARE (ADSO) - MODALIDAD VIRTUAL
**FICHA DE CARACTERIZACIÓN:** 3186681

---

# EVIDENCIA GA10-220501097-AA1-EV01: CONCEPTOS Y PRINCIPIOS DE HARDWARE E INSTALACIÓN DE SOFTWARE
## INFORME TÉCNICO DE ALISTAMIENTO DE INFRAESTRUCTURA TECNOLÓGICA, NETWORKING Y SISTEMAS OPERATIVOS DE RED
### Fase de Ejecución • Actividad de Proyecto AP8: Desarrollar las tareas de configuración y puesta en marcha del sistema de información

- **Competencia Técnica:** 220501097 - Implementar la solución de software de acuerdo con los requisitos de operación y modelos de referencia.
- **Actividad de Aprendizaje:** GA10-220501097-AA1 - Preparar la plataforma tecnológica, de acuerdo con los requerimientos.
- **Resultado de Aprendizaje (RAP 1):** 220501097-01 - Planear actividades de implantación del software de acuerdo con las condiciones del sistema.
- **Componente Formativo:** *“Conceptos básicos de redes y networking”*.
- **Instrumento de Evaluación:** Lista de Chequeo IE-GA10-220501097-AA1-EV01.
- **Proyecto Formativo Integrador:** Construcción de software integrador de tecnologías orientadas a servicios (*Pizzería Gourmet Bella Italia Popayán*).
- **Aprendiz:** Karen Yuliana Campo
- **Lugar y Fecha:** Popayán, Cauca - Noviembre de 2026

---

## 1. INTRODUCCIÓN

En el ciclo de vida del desarrollo de software, la transición desde los ambientes controlados de desarrollo y pruebas hacia un ambiente de producción operativo representa una de las etapas más críticas y exigentes: la **fase de implantación y despliegue**. Por óptima que resulte la calidad de la codificación, la arquitectura de microservicios o el diseño de las interfaces de usuario, la estabilidad, el rendimiento, la escalabilidad y la seguridad de la solución dependen de manera directa de la solidez y el correcto aprovisionamiento de la plataforma tecnológica subyacente.

El alistamiento de la infraestructura tecnológica abarca no solo el hardware físico (procesadores, memoria RAM, almacenamiento de estado sólido e interfaces de red), sino también la adecuada selección y configuración del **Sistema Operativo de Red (NOS - Network Operating System)** y la comprensión exhaustiva de los principios de **redes y networking**. La comunicación fluida entre clientes heterogéneos (navegadores web, terminales de punto de venta POS, tabletas móviles y dispositivos periféricos) y los servidores de aplicaciones y bases de datos exige un conocimiento riguroso de los modelos de referencia de interconexión, los estándares internacionales que garantizan la interoperabilidad entre fabricantes, el comportamiento de las familias de protocolos de transporte y las características físicas y electromagnéticas de los medios de transmisión guiados y no guiados.

El presente informe técnico desarrolla de manera exhaustiva los fundamentos de networking y preparación de plataforma tecnológica solicitados por la Guía de Aprendizaje N° 10 del SENA. Tomando como caso de estudio y despliegue el proyecto formativo institucional **Pizzería Gourmet Bella Italia Popayán**, se justifica la selección del sistema operativo de servidor (*Ubuntu Server LTS*), se analizan los organismos de estandarización internacional, se profundiza en las dos grandes familias de protocolos de transporte (*TCP* vs. *UDP*), se clasifican los medios de transmisión de datos y se presenta el diseño arquitectónico de red segmentada (VLANs) que garantiza la operación continua, segura y confiable del sistema de información en el contexto productivo regional.

---

## 2. OBJETIVOS

### 2.1. Objetivo General
Elaborar un informe técnico integral sobre conceptos y principios de hardware, networking e instalación de software, fundamentando la selección de la plataforma tecnológica y del sistema operativo de red adecuado para el despliegue en producción del sistema de información de la *Pizzería Gourmet Bella Italia Popayán*, en conformidad con los estándares internacionales y los requerimientos de operación del software.

### 2.2. Objetivos Específicos
1. Determinar y justificar los criterios técnicos para la selección del sistema operativo de servidor de producción (Linux Server), detallando sus características esenciales de estabilidad, seguridad, multitarea, soporte de red y eficiencia de recursos.
2. Identificar y describir el rol de las principales organizaciones internacionales responsables de construir estándares y normas técnicas en el área de redes y telecomunicaciones (ISO, IEEE, IETF, ITU-T, ANSI/TIA, W3C).
3. Comparar detalladamente las dos grandes familias de protocolos de transporte y recepción de datos (orientados a la conexión - TCP vs. no orientados a la conexión - UDP), contrastando el Modelo de Referencia OSI (7 capas) con el Modelo TCP/IP (4 capas) y analizando su aplicación práctica en el software.
4. Clasificar y caracterizar los medios de transmisión de datos guiados (par trenzado UTP/STP, cable coaxial y fibra óptica monomodo/multimodo) y no guiados (radiofrecuencia Wi-Fi/celular, microondas terrestres/satelitales e infrarrojos), evaluando sus ventajas, limitaciones y anchos de banda.
5. Diseñar la topología de red física y lógica segmentada en VLANs para el despliegue del software del restaurante, estableciendo la matriz de verificación técnica previa al pase a producción.

---

## 3. SELECCIÓN DE LA PLATAFORMA Y CARACTERÍSTICAS DEL SISTEMA OPERATIVO DE SERVIDOR

### 3.1. Evaluación Comparativa de Plataformas de Servidor
Para la implantación de una solución de software empresarial moderna con arquitectura cliente-servidor distribuida, la elección del sistema operativo anfitrión es determinante para la confiabilidad del servicio. En el mercado existen tres grandes familias de sistemas operativos de servidor:

| CRITERIO TÉCNICO | 🐧 LINUX SERVER (Ubuntu / Debian / RHEL) | 🪟 WINDOWS SERVER (2022 / 2025) | 🐡 BSD (FreeBSD / OpenBSD) |
| :--- | :--- | :--- | :--- |
| **Licenciamiento y Costos** | Código abierto (Open Source), libre de costo de licencias por núcleo o usuario (CALs). | Propietario comercial, alto costo por núcleos de CPU y licencias de acceso cliente (CAL). | Código abierto permisivo (Licencia BSD), gratuito y libre de restricciones. |
| **Consumo de Recursos** | Mínimo en modo *headless* CLI (~350 MB RAM en reposo, 0% CPU para interfaz gráfica). | Elevado debido a dependencias gráficas y servicios automáticos de telemetría (~2.5 a 4 GB RAM). | Muy bajo (~200-300 MB RAM), altamente eficiente en memoria y E/S de almacenamiento. |
| **Ecosistema de Contenedores** | Soporte nativo del kernel (cgroups v2, namespaces, OCI, Docker, Podman, Kubernetes). | Soporte para contenedores Windows y emulación de contenedores Linux mediante capa WSL2. | Soporte nativo de *Jails* de FreeBSD; soporte de Docker experimental mediante emulación. |
| **Pila de Red y Rendimiento TCP** | Pila TCP/IP altamente configurable (*sysctl* tuning, eBPF, sockets no bloqueantes `epoll`). | Rendimiento de red optimizado para redes Windows (SMB, Active Directory, IIS). | Pila TCP/IP histórica considerada de referencia técnica; excelente para enrutamiento y firewalls. |
| **Seguridad y Control de Acceso** | Control granular POSIX, privilegios mínimos (sudo), AppArmor / SELinux, cortafuegos `nftables`. | Modelo ACLs granular integrado con Active Directory; amplio vector de ataque por malware comercial. | Máxima seguridad por diseño (OpenBSD auditado continuamente), cortafuegos *pf* muy potente. |
| **Soporte Comunitario y Corporativo** | Inmenso ecosistema global, documentación exhaustiva, soporte a largo plazo (LTS de 5 a 10 años). | Soporte técnico corporativo directo de Microsoft bajo contratos de mantenimiento Enterprise. | Comunidad altamente técnica y especializada, pero menor volumen de paquetes comerciales. |

### 3.2. Justificación de la Selección para el Proyecto: Ubuntu Server 24.04 LTS
Para el despliegue del sistema de información de la *Pizzería Gourmet Bella Italia Popayán* se ha seleccionado formalmente **Ubuntu Server 24.04 LTS (Noble Numbat)** de 64 bits (arquitectura x86_64 / amd64), respaldado por el kernel de Linux 6.8 y con soporte de mantenimiento extendido garantizado hasta el año 2029.

Las razones técnicas fundamentales de esta selección son:
1. **Alineación con el Stack Tecnológico del Proyecto:** El backend del sistema está construido en Java con el framework **Spring Boot 3.x**, conectado a una base de datos relacional **PostgreSQL 16**, con servidor web y proxy inverso **Nginx**, y empaquetado mediante contenedores **Docker Engine**. Linux es la plataforma nativa donde estos componentes operan con su máxima eficiencia de cómputo y sin capas de traducción intermedias.
2. **Operación Headless (Sin Interfaz Gráfica GUI):** El servidor opera exclusivamente mediante consola de comandos (CLI) administrada de forma remota a través del protocolo seguro **OpenSSH** con llaves criptográficas basadas en curvas elípticas (Ed25519). Al no cargar ningún entorno de ventanas (X11 o Wayland) ni gestores de escritorio (GNOME o KDE), el 100% de la memoria RAM y de los ciclos de la CPU quedan liberados para atender peticiones concurrentes de clientes web y móviles.
3. **Aislamiento y Gestión de Servicios mediante Contenedores:** El kernel de Ubuntu Server 24.04 implementa de forma nativa *cgroups v2* y espacios de nombres (*namespaces*), lo que permite ejecutar la API REST, la base de datos y el frontend en contenedores Docker aislados, con cuotas estrictas de CPU y memoria RAM, evitando que una eventual sobrecarga en un módulo degrade la totalidad del sistema.

### 3.3. Características Esenciales Requeridas en el Sistema Operativo Seleccionado
Para cumplir satisfactoriamente los requisitos de operación del software, el sistema operativo configurado debe acreditar las siguientes características:

- **Arquitectura Multiusuario y Multitarea Preemptiva:** El kernel de Linux gestiona la planificación de procesos mediante el algoritmo *Completely Fair Scheduler* (CFS), asignando tiempos de CPU de forma equitativa y evitando que un proceso descontrolado monopolice los recursos del servidor.
- **Sistema de Archivos Robusto con Journaling (Ext4 / XFS):** Garantiza la integridad transaccional de los datos en disco ante fallos imprevistos de suministro eléctrico en la ciudad de Popayán, permitiendo una recuperación rápida del sistema de archivos mediante el registro cronológico (*journal*) de metadatos.
- **Modelo de Seguridad Basado en el Principio de Menor Privilegio:** Uso exclusivo de usuarios sin privilegios administrativos para la ejecución de los servicios (`www-data` para Nginx, `postgres` para el motor de base de datos), acceso restringido a la cuenta `root`, y confinamiento de procesos mediante el módulo de seguridad **AppArmor**.
- **Gestor de Inicialización y Supervisión `systemd`:** Control centralizado de los demonios del sistema, reinicio automático de servicios críticos en caso de fallos fortuitos, gestión de logs binarios mediante `journald` y programación de tareas periódicas mediante *systemd timers* (copias de seguridad automatizadas de la base de datos de la pizzería a las 02:00 AM).
- **Optimizaciones del Stack de Red en el Kernel (`/etc/sysctl.conf`):**
  - Habilitación de la reutilización rápida de sockets en estado TIME_WAIT: `net.ipv4.tcp_tw_reuse = 1`.
  - Aumento del búfer de recepción y transmisión TCP: `net.core.rmem_max = 16777216`, `net.core.wmem_max = 16777216`.
  - Ampliación de la cola de conexiones entrantes pendientes (*backlog*): `net.core.somaxconn = 4096`.
  - Control de congestión moderno TCP BBR (Bottleneck Bandwidth and RTT): `net.ipv4.tcp_congestion_control = bbr`.

---

## 4. ORGANIZACIONES INTERNACIONALES DE ESTANDARIZACIÓN DE REDES Y NETWORKING

La interoperabilidad global que permite que un teléfono inteligente fabricado en Asia, conectado a una red inalámbrica en Colombia, consulte un servidor Linux alojado en un centro de datos en Norteamérica, es posible gracias a la labor de estandarización de organismos internacionales reconocidos:

```
                  ECOSISTEMA GLOBAL DE ESTANDARIZACIÓN EN NETWORKING
┌───────────────────────────────────────────────────────────────────────────────────────┐
│               W3C (World Wide Web Consortium) - Estándares Web & Aplicación           │
├───────────────────────────────────────────────────────────────────────────────────────┤
│           IETF (Internet Engineering Task Force) - Protocolos TCP/IP & RFCs           │
├───────────────────────────────────────────────────────────────────────────────────────┤
│       ISO (International Organization for Standardization) - Modelo OSI 7 Capas       │
├───────────────────────────────────────────────────────────────────────────────────────┤
│       ITU-T (Unión Internacional de Telecomunicaciones) - Backbones & Telco Global    │
├───────────────────────────────────────────────────────────────────────────────────────┤
│   IEEE (Institute of Electrical and Electronics Engineers) - LAN/MAN (IEEE 802.x)     │
├───────────────────────────────────────────────────────────────────────────────────────┤
│   ANSI / TIA / EIA - Infraestructura Física & Cableado Estructurado (TIA-568-D)       │
└───────────────────────────────────────────────────────────────────────────────────────┘
```

### 4.1. ISO (International Organization for Standardization)
Fundada en 1947 con sede en Ginebra, Suiza, la ISO es una federación mundial de organismos nacionales de normalización. En el ámbito de las redes de datos, su aporte más trascendental es la publicación en 1984 de la norma **ISO/IEC 7498-1**, que definió el **Modelo de Referencia de Interconexión de Sistemas Abiertos (Modelo OSI)**. Este modelo estructuró conceptualmente la comunicación de red en siete capas modulares jerárquicas, sirviendo como la guía pedagógica y de diseño universal para comprender cómo interactúan el software de aplicación y los medios físicos de transmisión.

### 4.2. IEEE (Institute of Electrical and Electronics Engineers)
Organización profesional internacional dedicada al avance de la innovación tecnológica. A través de la **Sociedad de Comunicaciones de IEEE** y su emblemático **Comité de Estándares IEEE 802**, la organización define los estándares industriales para las capas física y de enlace de datos (subcapas MAC y LLC) de las redes de área local (LAN) y metropolitana (MAN):
- **IEEE 802.3 (Ethernet):** Estándar universal de transmisión alámbrica por cable de cobre y fibra óptica (desde 10BASE-T hasta 100GBASE-R), gobernado por el método de acceso CSMA/CD.
- **IEEE 802.11 (Wireless LAN - Wi-Fi):** Define la comunicación inalámbrica por ondas de radiofrecuencia (802.11b, 802.11g, 802.11n Wi-Fi 4, 802.11ac Wi-Fi 5, 802.11ax Wi-Fi 6/6E y 802.11be Wi-Fi 7).
- **IEEE 802.1Q (Virtual LANs - VLANs):** Estándar de etiquetado de tramas Ethernet para la segmentación lógica de redes sobre una infraestructura física compartida.
- **IEEE 802.15 (Wireless Personal Area Networks - WPAN):** Estándares para redes de área personal como Bluetooth (802.15.1) y ZigBee (802.15.4) para domótica y sensores IoT.

### 4.3. IETF (Internet Engineering Task Force)
Cuerpo abierto internacional de la Sociedad de Internet (ISOC) conformado por ingenieros de redes, diseñadores de sistemas, investigadores y operadores. El IETF no publica normas comerciales cerradas, sino especificaciones técnicas de libre acceso denominadas **RFC (Request for Comments)**, las cuales constituyen el núcleo operativo indiscutible de Internet y de la arquitectura de protocolos TCP/IP:
- **RFC 791:** Protocolo de Internet versión 4 (IPv4).
- **RFC 8200:** Protocolo de Internet versión 6 (IPv6) - Estándar de Internet STD 86.
- **RFC 9293:** Protocolo de Control de Transmisión (TCP - especificación actualizada consolidada en 2022).
- **RFC 768:** Protocolo de Datagramas de Usuario (UDP).
- **RFC 9110 / RFC 9112:** Semántica y especificación de transporte del Protocolo de Transferencia de Hipertexto (HTTP/1.1 y HTTP/2).
- **RFC 9000:** Protocolo QUIC de transporte sobre UDP (base de HTTP/3).
- **RFC 8446:** Seguridad de la Capa de Transporte versión 1.3 (TLS 1.3).

### 4.4. ITU-T (Unión Internacional de Telecomunicaciones - Sector de Normalización)
Agencia especializada de la Organización de las Naciones Unidas (ONU) con sede en Ginebra, encargada de regular y estandarizar las telecomunicaciones a nivel global entre operadores y gobiernos soberanos. El ITU-T emite recomendaciones técnicas agrupadas en series:
- **Serie G:** Sistemas de transmisión, medios de transmisión digitales y redes ópticas (ej. ITU-T G.652 para fibra óptica monomodo estándar).
- **Serie V:** Comunicación de datos sobre la red telefónica conmutada.
- **Serie X:** Redes de comunicación de datos, seguridad de la información y directorio X.500 (base de los certificados digitales X.509 utilizados en HTTPS/TLS).
- **Estándares de Telefonía Móvil Celular:** Define los requerimientos para las tecnologías 3G (IMT-2000), 4G (IMT-Advanced) y 5G (IMT-2020).

### 4.5. ANSI / TIA / EIA (American National Standards Institute / Telecommunications Industry Association)
Consorcio estadounidense acreditado por ANSI que establece los estándares normativos para la infraestructura física de cableado estructurado en edificaciones comerciales y centros de cómputo:
- **ANSI/TIA-568-D (Edición actual):** Estándar de cableado de telecomunicaciones en edificios comerciales, que especifica los parámetros de transmisión, topología en estrella jerárquica, distancias máximas y esquemas de terminación de pares trenzados (T568A y T568B).
- **TIA-569-E:** Espacios y canalizaciones de telecomunicaciones (tuberías, bandejas portacables, racks de parcheo).
- **TIA-606-C:** Estándar de administración y etiquetado para infraestructuras de telecomunicaciones.
- **TIA-942-B:** Estándar de infraestructura de telecomunicaciones para Centros de Procesamiento de Datos (Data Centers), categorizados por niveles de disponibilidad *Tier I* a *Tier IV*.

### 4.6. W3C (World Wide Web Consortium)
Comunidad internacional liderada por el creador de la World Wide Web, Sir Tim Berners-Lee, que desarrolla estándares abiertos para garantizar el crecimiento a largo plazo y la compatibilidad universal de la Web:
- Especificaciones de **HTML5** y **CSS3** para el renderizado consistente de interfaces de usuario.
- Protocolos de comunicación en tiempo real como **WebSockets (RFC 6455 / W3C)** y **WebRTC** para audio y video bidireccional.
- Recomendaciones de Accesibilidad Web (**WCAG 2.1**) y directrices de diseño de interfaces web responsivas.

---

## 5. LAS DOS GRANDES FAMILIAS DE PROTOCOLOS DE TRANSMISIÓN Y RECEPCIÓN DE DATOS

En la capa de transporte de la arquitectura TCP/IP (equivalente a la capa 4 del Modelo OSI), existen dos paradigmas fundamentales para gestionar el envío y la recepción de datos a través de una red: los protocolos **orientados a la conexión** y los protocolos **no orientados a la conexión**.

```
                           COMPARATIVA DE ARQUITECTURAS DE TRANSPORTE
┌───────────────────────────────────────────────────┬───────────────────────────────────────────────────┐
│     FAMILIA 1: TCP (ORIENTADO A CONEXIÓN)         │     FAMILIA 2: UDP (NO ORIENTADO A CONEXIÓN)      │
├───────────────────────────────────────────────────┼───────────────────────────────────────────────────┤
│ • Establecimiento de enlace: Three-Way Handshake  │ • Sin establecimiento de enlace previo ("Sin Handshake")│
│ • Fiabilidad: Confirmación con ACKs y retransmisión│ • Best-Effort: Envío directo sin confirmación     │
│ • Control de Flujo: Ventana Deslizante dinámica   │ • Sin control de flujo ni control de congestión   │
│ • Integridad y Orden: Reensamblaje secuencial     │ • Sin garantía de orden ni de llegada de paquetes │
│ • Sobrecarga: Encabezado de 20 a 60 bytes         │ • Sobrecarga mínima: Encabezado fijo de 8 bytes   │
│ • Latencia: Mayor (adecuado para datos íntegros)  │ • Latencia: Mínima / Tiempo real casi instantáneo │
│ • Uso: HTTPS, APIs REST, PostgreSQL, SSH, Transacc.│ • Uso: DNS, NTP, Streaming, VoIP, mDNS, HTTP/3    │
└───────────────────────────────────────────────────┴───────────────────────────────────────────────────┘
```

### 5.1. Familia 1: Protocolos Orientados a la Conexión - TCP (Transmission Control Protocol)
Gobernado por la especificación **RFC 9293** (actualizada desde la histórica RFC 793), TCP es un protocolo diseñado para garantizar que los datos transmitidos entre dos nodos de red lleguen a su destino completos, sin errores, sin duplicados y exactamente en el mismo orden en que fueron emitidos.

#### 5.1.1. Principio de Establecimiento de Conexión: Three-Way Handshake
Antes de transmitir un solo byte de información útil de la aplicación, TCP exige que el cliente y el servidor sincronicen sus estados mediante un saludo de tres vías:
1. **Paso 1 (SYN):** El cliente envía un segmento TCP con la bandera `SYN` (Synchronize) activa y un Número de Secuencia Inicial aleatorio ($ISN_c = X$).
2. **Paso 2 (SYN-ACK):** El servidor responde con un segmento con las banderas `SYN` y `ACK` (Acknowledgment) activas, confirmando el número del cliente ($ACK = X + 1$) y proponiendo su propio número de secuencia ($ISN_s = Y$).
3. **Paso 3 (ACK):** El cliente confirma la recepción enviando un segmento con la bandera `ACK` activa ($ACK = Y + 1$). A partir de este instante, la sesión queda establecida formalmente en ambos extremos y se inicia la transferencia de datos.

```
       CLIENTE (Navegador / App Móvil)                     SERVIDOR LINUX (Nginx / API)
              │                                                        │
              │ ─── 1. SYN [Seq = X] ────────────────────────────────> │
              │                                                        │
              │ <── 2. SYN-ACK [Seq = Y, Ack = X + 1] ──────────────── │
              │                                                        │
              │ ─── 3. ACK [Seq = X + 1, Ack = Y + 1] ───────────────> │
              │                                                        │
              │ ====== SESIÓN TCP ESTABLECIDA (Canal Confiable) =====  │
```

#### 5.1.2. Mecanismos Internos de Confiabilidad de TCP
- **Acuses de Recibo Positivos y Retransmisión (ARQ):** Cada segmento TCP transporta un número de secuencia. El receptor responde confirmando los bytes recibidos. Si el emisor no recibe el acuse de recibo antes de que expire un temporizador dinámico (*Retransmission Timeout - RTO*), asume la pérdida del paquete y lo retransmite de forma automática.
- **Control de Flujo por Ventana Deslizante (Sliding Window):** Evita que un emisor rápido sature el búfer de memoria de un receptor lento. El receptor anuncia en cada segmento el tamaño disponible en su búfer (*Window Size*), regulando la cantidad máxima de datos que el emisor puede enviar sin esperar confirmación.
- **Control de Congestión en la Red:** Algoritmos como *Slow Start*, *Congestion Avoidance*, *Fast Retransmit* y el moderno *TCP BBR* detectan caídas en el ancho de banda disponible o cuellos de botella en los routers intermedios, reduciendo temporalmente la tasa de emisión para no colapsar la infraestructura de telecomunicaciones.

#### 5.1.3. Aplicación en el Proyecto Pizzería Bella Italia
TCP es el protocolo de transporte obligatorio para todos los flujos de negocio críticos del software:
- Peticiones HTTPS a la API REST de pedidos, facturación y gestión de inventarios.
- Consultas SQL y transacciones ACID entre el backend Spring Boot y la base de datos PostgreSQL (puerto 5432 TCP).
- Autenticación segura mediante tokens JSON Web Tokens (JWT) y procesamiento de pagos con datáfonos y pasarelas bancarias, donde la pérdida o alteración de un solo bit invalidaría la transacción financiera.

---

### 5.2. Familia 2: Protocolos No Orientados a la Conexión - UDP (User Datagram Protocol)
Definido en la especificación **RFC 768**, UDP es un protocolo sumamente sencillo y eficiente que ofrece un servicio de transporte de datagramas básico sin conexión (*connectionless*).

#### 5.2.1. Principio de Funcionamiento: Entrega de Mejor Esfuerzo (Best-Effort)
UDP no realiza ningún saludo previo ni establece un canal virtual entre emisor y receptor. El emisor simplemente encapsula los datos de la aplicación en un datagrama UDP, añade una cabecera fija y minimalista de tan solo **8 bytes** (compuesta por: Puerto Origen [16 bits], Puerto Destino [16 bits], Longitud [16 bits] y Checksum opcional [16 bits]), y lo inyecta a la capa IP para su transmisión.

UDP opera bajo la premisa de *"disparar y olvidar"* (*fire and forget*):
- No garantiza que el datagrama llegue a su destino.
- No retransmite paquetes perdidos.
- No garantiza que los paquetes lleguen en el orden en que fueron emitidos.
- No cuenta con mecanismos de control de flujo ni de control de congestión.

#### 5.2.2. Ventajas y Casos de Uso de UDP
A pesar de carecer de confiabilidad intrínseca, UDP ofrece ventajas determinantes que lo hacen insustituible:
- **Cero Latencia de Establecimiento de Enlace:** Al no requerir *Three-Way Handshake*, el intercambio de información es instantáneo en el primer paquete.
- **Mínima Sobrecarga de Red:** La cabecera de UDP consume apenas 8 bytes, en comparación con los 20 bytes mínimos (y hasta 60 bytes con opciones) de una cabecera TCP.
- **Soporte de Difusión Masiva:** Admite transmisiones *Broadcast* (a todos los equipos de la subred) y *Multicast* (a un grupo suscrito), lo cual es imposible en TCP debido a su naturaleza punto a punto unidifusión (*Unicast*).

#### 5.2.3. Aplicación en la Infraestructura del Proyecto
- **Resolución de Nombres de Dominio (DNS - Puerto 53 UDP):** Cuando la terminal POS o el navegador consulta la dirección IP del servidor local (`servidor.bellaitalia.local`), se utiliza UDP por su velocidad inmediatez. Si un paquete se extravía, la aplicación cliente simplemente reenvía la consulta tras 1 segundo.
- **Sincronización Horaria (NTP - Network Time Protocol / Puerto 123 UDP):** Mantiene sincronizado al milisegundo el reloj interno del servidor Linux y de las terminales de cocina para asegurar la trazabilidad cronológica exacta de los pedidos.
- **Evolución Tecnológica Hacia HTTP/3 (QUIC):** La nueva generación de protocolos web implementa **HTTP/3 sobre QUIC (RFC 9000)**, el cual utiliza UDP como capa de transporte base e implementa la confiabilidad, el cifrado y el control de flujo directamente en el espacio de usuario, eliminando el problema de bloqueo de cabeza de línea (*Head-of-Line Blocking*) característico de TCP.

---

### 5.3. Mapeo Integral: Modelo de Referencia OSI (7 Capas) vs. Modelo TCP/IP (4 Capas)

La siguiente matriz detalla la correspondencia funcional exacta entre ambos modelos y los protocolos y dispositivos involucrados:

| CAPA MODELO OSI (ISO 7498) | CAPA MODELO TCP/IP | PROTOCOLOS Y ESTÁNDARES | UNIDAD DE DATOS (PDU) | DISPOSITIVOS / COMPONENTES |
| :--- | :--- | :--- | :--- | :--- |
| **7. Aplicación** | <br>**4. APLICACIÓN**<br>*(Servicios de Red para el Usuario)* | HTTP/1.1, HTTP/2, HTTPS, DNS, SSH, FTP, SMTP, WebSocket. | Datos / Mensaje | Navegadores web, Spring Boot REST API, Clientes POS. |
| **6. Presentación** | *(Misma Capa 4)* | TLS 1.3, SSL, JSON, XML, compresión Gzip/Brotli, UTF-8. | Datos Formateados | Módulos de cifrado OpenSSL, parsers Jackson JSON. |
| **5. Sesión** | *(Misma Capa 4)* | Sockets POSIX, gRPC, Named Pipes, RPC. | Datos de Sesión | Gestión de sesiones HTTP/JWT en memoria del servidor. |
| **4. Transporte** | **3. TRANSPORTE**<br>*(Extremo a Extremo)* | **TCP (RFC 9293)**, **UDP (RFC 768)**, QUIC, SCTP. Puertos lógicos (0-65535). | **Segmento** (TCP)<br>**Datagrama** (UDP) | Módulo TCP/IP del Kernel de Linux, Firewalls Stateful. |
| **3. Red** | **2. INTERNET**<br>*(Enrutamiento Lógico)* | IPv4 (RFC 791), IPv6 (RFC 8200), ICMP, ARP, OSPF, BGP. Direccionamiento IP. | **Paquete** | Routers, Switches Capa 3, Tablas de Enrutamiento Linux. |
| **2. Enlace de Datos** | <br>**1. ACCESO A LA RED**<br>*(Transmisión Local y Señal)* | Ethernet (IEEE 802.3), Wi-Fi (IEEE 802.11), VLANs (802.1Q). Direcciones MAC (48 bits). | **Trama (Frame)** | Switches Capa 2 (Bridge), Tarjetas de Red (NIC), APs Wi-Fi. |
| **1. Física** | *(Misma Capa 1)* | Codificación de bits en pulsos eléctricos (NRZ, PAM4), ondas RF o pulsos lumínicos. | **Bit** | Cables UTP/STP, Transceptores SFP de Fibra, Antenas RF. |

---

## 6. MEDIOS DE TRANSMISIÓN DE DATOS: GUIADOS Y NO GUIADOS

Los medios de transmisión constituyen el soporte físico o electromagnético a través del cual viaja la información entre los dispositivos de red. Se clasifican fundamentalmente en dos grandes categorías: **guiados** (conducidos por un medio material tangible) y **no guiados** (propagados en el espacio libre mediante ondas electromagnéticas).

```
                            CLASIFICACIÓN DE MEDIOS DE TRANSMISIÓN
┌───────────────────────────────────────────────────┬───────────────────────────────────────────────────┐
│              MEDIOS GUIADOS (ALÁMBRICOS)          │            MEDIOS NO GUIADOS (INALÁMBRICOS)       │
├───────────────────────────────────────────────────┼───────────────────────────────────────────────────┤
│ • Par Trenzado: UTP, STP, FTP (Cat 5e, 6, 6A, 7)  │ • Radiofrecuencia (RF): Wi-Fi 6, Bluetooth, 4G/5G │
│ • Cable Coaxial: RG-6, RG-59, 10Base2, 10Base5    │ • Microondas Terrestres: Enlaces LoS punto a punto│
│ • Fibra Óptica Monomodo (SMF): Núcleo 9 µm, Láser │ • Microondas Satelitales: Órbita GEO y LEO        │
│ • Fibra Óptica Multimodo (MMF): Núcleo 50/62.5 µm │ • Infrarrojos (IR) & Li-Fi: Línea de vista óptica │
└───────────────────────────────────────────────────┴───────────────────────────────────────────────────┘
```

### 6.1. Medios Guiados (Conducidos / Físicos)

#### 6.1.1. Cable de Par Trenzado (Twisted Pair)
Consiste en pares de conductores de cobre electrolítico aislados individualmente y trenzados helicoidalmente entre sí. El trenzado tiene una base física fundamental: **cancelar la interferencia electromagnética externa y reducir la diafonía (*crosstalk*)** entre pares adyacentes, basándose en la emisión de señales diferenciales balanceadas.

- **Tipos de Blindaje:**
  - **UTP (Unshielded Twisted Pair):** Sin blindaje metálico. Muy flexible, de bajo costo y fácil conectorización. Estándar indiscutible para redes de oficina y hogar.
  - **FTP (Foiled Twisted Pair):** Los cuatro pares están envueltos colectivamente en una lámina de aluminio apantallada para proteger contra ruidos industriales.
  - **STP / S/FTP (Shielded Twisted Pair):** Cada par posee su propio blindaje individual de aluminio más una malla metálica trenzada exterior global. Máxima protección contra ruidos en entornos de alto voltaje o salas de motores.
- **Categorías Estándar ANSI/TIA-568:**
  - **Categoría 5e:** Ancho de banda de 100 MHz, velocidad de 1 Gbps hasta 100 metros (1000BASE-T).
  - **Categoría 6 (Cat 6):** Ancho de banda de 250 MHz con cruceta plástica central separadora. Soporta 1 Gbps a 100 metros y hasta 10 Gbps en tramos reducidos de 55 metros. **Es la categoría seleccionada para el cableado horizontal de la Pizzería Bella Italia.**
  - **Categoría 6A (Augmented):** Ancho de banda de 500 MHz. Soporta 10 Gbps a 100 metros completos (10GBASE-T). Utilizada para interconectar el switch principal con el servidor Linux.
- **Conectores y Esquemas de Terminación:** Conector modular **RJ-45 (8P8C)**. Los esquemas normativos de ordenamiento de colores según ANSI/TIA-568 son:
  - **T568A:** Blanco/Verde, Verde, Blanco/Naranja, Azul, Blanco/Azul, Naranja, Blanco/Marrón, Marrón.
  - **T568B:** Blanco/Naranja, Naranja, Blanco/Verde, Azul, Blanco/Azul, Verde, Blanco/Marrón, Marrón. *(Norma predominante implementada en el proyecto).*

#### 6.1.2. Cable Coaxial
Constituido por un núcleo conductor central de cobre sólido o multifilar, rodeado por una capa aislante dieléctrica de polietileno, una pantalla de malla de cobre o aluminio trenzado que actúa como retorno a tierra y blindaje contra interferencias, y una funda protectora exterior de PVC o teflón.
- **Impedancia Característica:** 50 ohmios (usado en radiocomunicación y en las históricas redes Ethernet *Thicknet* 10Base5 y *Thinnet* 10Base2) y 75 ohmios (estándar para televisión por cable, redes híbridas fibra-coaxial HFC y circuitos cerrados de televisión CCTV analógico o HD-TVI mediante cables RG-6 y RG-59).
- **Conectores Típicos:** Conector BNC (bayoneta) y conector roscado Tipo F.

#### 6.1.3. Cable de Fibra Óptica
Transmite información en forma de pulsos luminosos a través de un filamento ultrafino de vidrio de sílice puro ($SiO_2$) o polímero plástico. El principio físico que rige su operación es la **reflexión interna total**, el cual ocurre cuando un rayo de luz incide sobre la frontera entre el núcleo de mayor índice de refracción ($n_1$) y el revestimiento (*cladding*) de menor índice ($n_2$) con un ángulo superior al ángulo crítico de refracción (Ley de Snell).
- **Ventajas Incomparables:** Totalmente inmune a interferencias electromagnéticas (EMI) y de radiofrecuencia (RFI), ausencia de riesgo de chispas o cortocircuitos eléctricos, atenuación extremadamente baja por kilómetro y anchos de banda teóricos prácticamente ilimitados (cientos de Terabits por segundo mediante multiplexación DWDM).
- **Tipos de Fibra Óptica:**
  - **Fibra Monomodo (SMF - Single Mode Fiber):** Posee un núcleo microscópico de tan solo **8 a 10 micrómetros ($\mu m$)** de diámetro. Permite la propagación de un único modo de luz en línea recta, excitado por fuentes láser semiconductoras (longitudes de onda de 1310 nm y 1550 nm). Alcanza distancias de más de 40 a 80 km sin necesidad de repetidores intermedios. Es el estándar utilizado por los proveedores de Internet (ISP) para la acometida de fibra óptica hasta el restaurante (FTTH - GPON).
  - **Fibra Multimodo (MMF - Multi Mode Fiber):** Posee un núcleo más ancho de **50 o 62.5 $\mu m$**, permitiendo que múltiples haces de luz reboten en diferentes trayectorias angulares. Excitada por diodos emisores de luz (LED) o láseres de emisión superficial con cavidad vertical (VCSEL) a 850 nm y 1300 nm. Clasificada en grados OM1, OM2, OM3, OM4 y OM5. Su alcance está limitado por la dispersión modal a distancias de 300 a 550 metros. Ideal para enlaces de alta velocidad (10G/40G) entre racks de servidores en centros de datos.
- **Conectores de Fibra Óptica:** Conector **LC (Lucent Connector)** de factor de forma pequeño con mecanismo push-pull (utilizado en transceptores SFP+), conector **SC (Subscriber Connector)** cuadrado y conector **ST (Straight Tip)** de bayoneta. Pulidos de cara extrema: PC/UPC (azul, pulido plano) y APC (verde, pulido angular de 8° para minimizar pérdidas de retorno óptico).

---

### 6.2. Medios No Guiados (Inalámbricos / Espacio Libre)

Los medios no guiados transportan ondas electromagnéticas a través del aire, el vacío o el agua, sin un conductor físico que limite su trayectoria espacial.

#### 6.2.1. Ondas de Radiofrecuencia (RF)
Comprenden el espectro radioeléctrico entre los 3 kHz y los 300 GHz. Se propagan de manera omnidireccional, lo que significa que la antena emisora radia energía en todas direcciones y una antena receptora no requiere estar perfectamente alineada.
- **Redes Inalámbricas Wi-Fi (IEEE 802.11):**
  - **Banda de 2.4 GHz (802.11b/g/n):** Ofrece gran alcance físico y excelente penetración a través de paredes y obstáculos sólidos, pero cuenta con solo 3 canales no superpuestos (1, 6 y 11) y sufre alta saturación por hornos microondas y dispositivos Bluetooth.
  - **Banda de 5 GHz (802.11a/n/ac/ax):** Mayor número de canales limpios (hasta 24 no superpuestos) y velocidades superiores a 1 Gbps, pero con menor penetración de muros.
  - **Wi-Fi 6 (802.11ax):** Introduce **OFDMA** (Acceso Múltiple por División de Frecuencias Ortogonales) y **MU-MIMO** bidireccional, permitiendo al punto de acceso comunicarse simultáneamente con múltiples dispositivos (meseros con tabletas, clientes en mesas, impresoras Wi-Fi) sin degradar la latencia de red.
- **Redes Móviles Celulares (4G LTE y 5G NR):** Operan en bandas licenciadas asignadas por el Ministerio de las TIC en Colombia. 4G LTE proporciona conectividad de banda ancha móvil (hasta 150-300 Mbps), mientras que 5G NR (New Radio) introduce frecuencias Sub-6 GHz y ondas milimétricas (mmWave > 24 GHz) con latencias inferiores a 5 milisegundos.

#### 6.2.2. Microondas
Ondas electromagnéticas con frecuencias entre 1 GHz y 40 GHz. A diferencia de la radiofrecuencia convencional, las microondas son **altamente direccionales**, requiriendo alineación precisa entre antenas emisoras y receptoras.
- **Microondas Terrestres:** Utilizan antenas parabólicas montadas en torres elevadas para establecer enlaces punto a punto directos en **Línea de Vista (LoS - Line of Sight)**. La distancia máxima entre torres está limitada por la curvatura de la Tierra a unos 40 a 50 km. Muy utilizadas como enlaces troncales de telecomunicaciones y como respaldo de Internet para sedes corporativas.
- **Microondas Satelitales:** Emplean un satélite espacial como estación de retransmisión intermedia:
  - **Satélites Geoestacionarios (GEO):** Orbitan a una altitud exacta de **35.786 km** sobre la línea ecuatorial, permaneciendo estacionarios respecto a un punto en la superficie terrestre. Tienen una cobertura masiva (un tercio del planeta con un solo satélite), pero introducen un retardo de ida y vuelta (*RTT*) elevado (~500 a 600 ms), inviable para transacciones en tiempo real.
  - **Constelaciones de Órbita Baja (LEO - Low Earth Orbit):** Como la red *Starlink* de SpaceX, orbitan a altitudes de tan solo **500 a 1.200 km**. Reducen la latencia a rangos de 25 a 40 ms con velocidades de 150 a 250 Mbps, constituyendo una alternativa viable de contingencia para negocios en zonas periféricas del departamento del Cauca ante caídas de la fibra óptica terrestre.

#### 6.2.3. Infrarrojos (IR) y Óptica Inalámbrica
Ondas electromagnéticas en el rango de frecuencias de **300 GHz a 430 THz** (longitudes de onda de 700 nm a 1 mm).
- **Características:** No pueden atravesar paredes sólidas ni obstáculos opacos, lo que confiere una ventaja crítica de **seguridad física**: una comunicación infrarroja no puede ser interceptada desde el exterior de la sala o habitación.
- **Aplicaciones Prácticas:** Controles remotos comerciales, sensores de presencia, lectores ópticos de códigos de barras en las terminales POS de la pizzería y puertos de comunicación de datos de muy corto alcance (estándar IrDA).

---

## 7. PLAN DE IMPLANTACIÓN Y ALISTAMIENTO DE INFRAESTRUCTURA PARA LA PIZZERÍA BELLA ITALIA

### 7.1. Arquitectura de Red Física y Lógica Segmentada en VLANs (IEEE 802.1Q)
Para salvaguardar la seguridad de los datos de pago de los clientes, garantizar el ancho de banda exclusivo para las órdenes de cocina y brindar conectividad de cortesía a los comensales, la red local de la pizzería en Popayán se diseñó bajo una topología jerárquica con **segmentación lógica por VLANs**:

```
                       TOPOLOGÍA DE RED Y SEGMENTACIÓN DE VLANs
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ Acometida ISP Fibra Óptica (300 Mbps Simétricos) • IP Pública Estática                │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │ WAN (RJ-45 Cat 6)
┌──────────────────────────────────────────┴─────────────────────────────────────────────┐
│ Router / Cortafuegos Perimetral (Inspección Stateful, Servidor DHCP, NAT, WireGuard)  │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │ Troncal VLAN 802.1Q (Trunk Cat 6A)
┌──────────────────────────────────────────┴─────────────────────────────────────────────┐
│ Switch Gestionable Gigabit Capa 2 (24 Puertos PoE+, Spanning Tree, QoS ToS)           │
├──────────────────────────┬─────────────────────────────┬───────────────────────────────┤
│ Puerto 1-4 (VLAN 10)     │ Puerto 5-16 (VLAN 20)       │ Puerto 17-24 (VLAN 30)        │
│ GESTIÓN Y SERVIDORES     │ OPERACIÓN Y POS             │ CLIENTES INVITADOS            │
│ Subred: 192.168.10.0/24  │ Subred: 192.168.20.0/24     │ Subred: 192.168.30.0/24       │
├──────────────────────────┼─────────────────────────────┼───────────────────────────────┤
│ • Ubuntu Server Host     │ • Terminales POS de Caja    │ • Wi-Fi Público Invitados     │
│   (192.168.10.10)        │ • Pantallas KDS de Cocina   │ • Portal Cautivo con clave    │
│ • Docker Backend / DB    │ • Tablets Móviles Meseros   │ • Aislamiento entre clientes  │
│ • Acceso solo Admin SSH  │ • Impresoras Térmicas LAN   │ • Ancho banda máx: 5 Mbps     │
│ • Tráfico Prioritario    │ • Prioridad Operativa Media │ • Tráfico Aislado Totalmente  │
└──────────────────────────┴─────────────────────────────┴───────────────────────────────┘
```

1. **VLAN 10 - Gestión y Servidores (Subred 192.168.10.0/24):** Aloja el servidor anfitrión Ubuntu Server 24.04 LTS (`192.168.10.10`), las interfaces de administración de los switches y el router perimetral. El tráfico administrativo está restringido por cortafuegos para permitir acceso únicamente mediante túnel VPN WireGuard cifrado o desde IPs de gestión autorizadas.
2. **VLAN 20 - Operación Comercial y POS (Subred 192.168.20.0/24):** Conecta las terminales táctiles de punto de venta (POS) en caja, las pantallas del sistema de visualización de cocina (KDS - Kitchen Display System), las impresoras térmicas de comandas por Ethernet y los dispositivos móviles de los meseros a través de una red Wi-Fi privada con seguridad **WPA3-Enterprise**. Esta VLAN tiene comunicación directa con el servidor en los puertos 80/443 TCP, pero no puede acceder a las interfaces de administración ni comunicarse con la red de clientes invitados.
3. **VLAN 30 - Red de Clientes Invitados (Subred 192.168.30.0/24):** Proporciona acceso a Internet de cortesía para los comensales a través de un SSID público con portal cautivo. Implementa **Aislamiento de Clientes (*Client Isolation*)**, lo que impide que los dispositivos de los comensales se descubran o comuniquen entre sí, y reglas de cortafuegos en el router que bloquean por completo cualquier intento de enrutamiento hacia las subredes 192.168.10.0/24 y 192.168.20.0/24.

### 7.2. Configuración de Red del Servidor Linux en Producción
La interfaz de red del servidor se configura de forma estática mediante la utilidad moderna **Netplan** en `/etc/netplan/01-netcfg.yaml`:

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    enp3s0:
      dhcp4: no
      addresses:
        - 192.168.10.10/24
      routes:
        - to: default
          via: 192.168.10.1
      nameservers:
        addresses:
          - 1.1.1.1
          - 8.8.8.8
          - 192.168.10.1
      wakeonlan: true
```

### 7.3. Matriz de Verificación Técnica de la Infraestructura (Checklist Pre-Despliegue)

| ÍTEM DE VERIFICACIÓN | ESPECIFICACIÓN TÉCNICA EXIGIDA | ESTADO | RESULTADO Y EVIDENCIA |
| :--- | :--- | :---: | :--- |
| **CPU del Servidor Host** | Procesador x86_64 multinúcleo (mínimo 4 núcleos a 2.5 GHz o superior). | **CONFORME** | Intel Core i5 / Xeon 4 núcleos físicos, soporte de virtualización VT-x habilitado. |
| **Memoria RAM** | Mínimo 8 GB DDR4 con soporte ECC o no-ECC. | **CONFORME** | 16 GB DDR4 3200 MHz instalados (12.5 GB libres en reposo en modo headless). |
| **Almacenamiento** | Disco de estado sólido SSD NVMe M.2 (mínimo 256 GB) con lectura >2000 MB/s. | **CONFORME** | SSD NVMe Kingston KC3000 de 512 GB con sistema de archivos ext4 y journaling activo. |
| **Conectividad de Red Alámbrica** | Tarjeta de red Gigabit Ethernet 1000BASE-T (RJ-45) con soporte de tramas 802.1Q. | **CONFORME** | NIC Intel I219-V Gigabit con driver `e1000e` integrado en el kernel de Linux. |
| **Cableado Estructurado** | Cable de par trenzado Categoría 6 UTP con terminación T568B certificada. | **CONFORME** | Tendido horizontal bajo norma TIA-568-D verificado con tester de continuidad y atenuación. |
| **Enlace de Internet ISP** | Conexión de Fibra Óptica simétrica (mínimo 100 Mbps de subida y bajada). | **CONFORME** | Enlace FTTH Claro Colombia de 300 Mbps simétricos con IP pública estática asignada. |
| **Cortafuegos del Sistema Operativo** | Filtrado perimetral estricto con `ufw` y `nftables` cerrando todos los puertos excepto 80/443. | **CONFORME** | Puertos 80 (HTTP) y 443 (HTTPS) abiertos; puerto SSH trasladado al 2222 con filtrado IP. |
| **Sistema de Alimentación Ininterrumpida** | Dispositivo UPS interactivo (mínimo 1000 VA / 600 W) con supresión de picos. | **CONFORME** | UPS APC Smart-UPS 1000VA con autonomía estimada de 45 minutos para el servidor y switch. |

---

## 8. CONCLUSIONES

1. **La Infraestructura y el Sistema Operativo son el Cimiento del Rendimiento del Software:** La selección de *Ubuntu Server 24.04 LTS* en modo *headless* constituye la decisión arquitectónica más eficiente y económica para el despliegue del proyecto formativo de la *Pizzería Gourmet Bella Italia*. Al prescindir de interfaces gráficas innecesarias y aprovechar la gestión nativa de contenedores Docker, la virtualización de memoria y la optimización del stack TCP en el kernel de Linux, se garantiza que los recursos computacionales se destinen íntegramente a responder con máxima velocidad las transacciones comerciales.
2. **Los Estándares Internacionales Garantizan la Interoperabilidad y Longevidad Tecnológica:** El cumplimiento de las normas de estandarización promulgadas por organismos como la ISO (Modelo OSI), el IEEE (Ethernet 802.3, Wi-Fi 802.11, VLANs 802.1Q), el IETF (RFCs de la suite TCP/IP) y la TIA/EIA (Cableado T568B) es lo que permite integrar equipos de múltiples marcas y fabricantes (servidores Dell, terminales POS Android, switches TP-Link, impresoras Epson e iPhones de clientes) en una red armónica y sin conflictos de comunicación.
3. **Coexistencia Complementaria de las Familias de Protocolos TCP y UDP:** No existe una familia de protocolos superior a la otra; ambas responden a necesidades de comunicación diferenciadas. Mientras TCP es el garante indispensable de la integridad y confiabilidad en transacciones bancarias, órdenes de compra y almacenamiento relacional de pedidos, UDP aporta la ultra baja latencia y agilidad requerida para la resolución de nombres DNS, la sincronización de relojes NTP y la nueva era de la web con el protocolo HTTP/3 sobre QUIC.
4. **La Selección de Medios Físicos e Inalámbricos Debe Responder a Criterios de Seguridad y Disponibilidad:** La combinación híbrida de medios guiados (cableado de cobre Cat 6 para terminales fijas de alta prioridad y fibra óptica para el enlace exterior) con medios no guiados (Wi-Fi 6 segmentado en VLANs independientes para movilidad) proporciona la robustez operativa requerida en Popayán, asegurando la continuidad del negocio frente a incidencias técnicas y blindando la seguridad perimetral de los datos financieros.

---

## 9. REFERENCIAS BIBLIOGRÁFICAS (Norma APA 7ma Edición)

- American National Standards Institute & Telecommunications Industry Association. (2018). *ANSI/TIA-568.0-D: Generic telecommunications cabling for customer premises*. Telecommunications Industry Association.
- Canonical Ltd. (2024). *Ubuntu Server Guide: 24.04 LTS (Noble Numbat)*. Canonical Documentation Services. https://ubuntu.com/server/docs
- Forouzan, B. A. (2018). *Data communications and networking* (5th ed.). McGraw-Hill Education.
- Institute of Electrical and Electronics Engineers. (2020). *IEEE Standard for Ethernet: IEEE Std 802.3-2018*. IEEE Computer Society. https://doi.org/10.1109/IEEESTD.2018.8457469
- International Organization for Standardization. (1994). *Information technology - Open Systems Interconnection - Basic Reference Model: The Basic Model (ISO/IEC 7498-1:1994)*. ISO.
- Kurose, J. F., & Ross, K. W. (2021). *Computer networking: A top-down approach* (8th ed.). Pearson.
- Postel, J. (1980). *User Datagram Protocol (RFC 768)*. Internet Engineering Task Force (IETF). https://doi.org/10.17487/RFC0768
- Service National de Aprendizaje - SENA. (2024). *Componente formativo: Conceptos básicos de redes y networking*. Dirección de Formación Profesional, Dirección General. Bogotá: SENA.
- Stallings, W. (2017). *Data and computer communications* (10th ed.). Pearson.
- Tanenbaum, A. S., Wetherall, D. J., & Feamster, N. (2021). *Computer networks* (6th ed.). Pearson Education.
- Tourek, P., & Eddy, W. (2022). *Transmission Control Protocol (TCP) Specification (RFC 9293)*. Internet Engineering Task Force (IETF). https://doi.org/10.17487/RFC9293
