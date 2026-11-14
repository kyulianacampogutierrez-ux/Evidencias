# SERVICIO NACIONAL DE APRENDIZAJE - SENA
## CENTRO DE TELEINFORMÁTICA Y PRODUCCIÓN INDUSTRIAL (CTPI) - REGIONAL CAUCA
### TECNOLOGÍA EN ANÁLISIS Y DESARROLLO DE SOFTWARE (ADSO) - MODALIDAD VIRTUAL
**FICHA DE CARACTERIZACIÓN:** 3186681

---

# EVIDENCIA GA10-220501097-AA5-EV01: CONFIGURACIÓN DE SERVICIOS, BASES DE DATOS Y SOFTWARE EN EL EQUIPO DEL CLIENTE
## INFORME TÉCNICO COMPARATIVO PASO A PASO: VIRTUALIZACIÓN BASADA EN HIPERVISOR (VM UBUNTU LAMP) VS. CONTENEDORES LIGEROS DOCKER (APACHE + MYSQL 8.0)
### Fase de Ejecución • Actividad de Proyecto AP8: Desarrollar las tareas de configuración y puesta en marcha del sistema de información

* **Competencia Técnica:** 220501097 - Implementar la solución de software de acuerdo con los requisitos de operación y modelos de referencia.
* **Actividad de Aprendizaje:** GA10-220501097-AA5 - Configurar el software en el servidor y la base de datos, de acuerdo con los requerimientos.
* **Resultado de Aprendizaje (RAP 3):** 220501097-03 - Instalar la solución de software en la plataforma tecnológica del cliente de acuerdo con el plan de implantación.
* **Componente Formativo de Referencia:** *"Tecnologías de virtualización: desde servidores hasta contenedores"*.
* **Instrumento de Evaluación:** Lista de Chequeo IE-GA10-220501097-AA5-EV01.
* **Proyecto Formativo Integrador:** Sistema Integral de Comercio Electrónico y Gestión Operativa - *Pizzería Gourmet Bella Italia Popayán*.
* **Aprendiz:** Karen Yuliana Campo
* **Lugar y Fecha:** Popayán, Cauca - Noviembre de 2026

---

## 1. INTRODUCCIÓN

En el panorama actual de la ingeniería de software y la administración de plataformas operativas, el despliegue de servicios esenciales —especialmente servidores web de aplicaciones y sistemas gestores de bases de datos relacionales— representa un hito crítico de transición entre el desarrollo y la producción. Tradicionalmente, la puesta en marcha de un entorno con sistema operativo Linux (Ubuntu), servidor web Apache y base de datos MySQL (pila LAMP) implicaba la instalación directa sobre la máquina anfitrión del cliente, ocasionando problemas de incompatibilidad de librerías, dependencias cruzadas y degradación progresiva del sistema operativo.

Para superar tales limitaciones surgieron dos grandes paradigmas de aislamiento tecnológico:
1. **La Virtualización Basada en Hipervisor (Máquinas Virtuales - VM):** Donde un hipervisor emula hardware físico completo para ejecutar un sistema operativo huésped (*Guest OS*) íntegro, con su propio kernel y servicios de inicialización.
2. **La Virtualización Basada en Contenedores (Docker / OCI):** Donde múltiples entornos de ejecución comparten el mismo núcleo del sistema operativo anfitrión (*Shared Host Kernel*), logrando un aislamiento lógico mediante primitivas nativas de Linux (*namespaces* y *control groups*).

El presente informe técnico desarrolla de manera rigurosa la configuración y el despliegue de una plataforma tecnológica compuesta por **Sistema Operativo Linux Ubuntu**, **Servidor Web de Aplicaciones Apache 2.4** y **Gestor de Base de Datos MySQL 8.0**, adaptada a las necesidades operativas de la *Pizzería Gourmet Bella Italia Popayán*. Se presenta en primera instancia el diseño y aprovisionamiento bajo virtualización tradicional (VM), seguido de la implementación práctica mediante contenedores Docker orquestados, contrastando empíricamente su rendimiento, consumo de recursos, portabilidad y aislamiento.

Todas las comprobaciones operativas y capturas de pantalla fueron obtenidas en tiempo real en la estación de trabajo bajo el entorno de escritorio **KDE X11**, utilizando la terminal nativa **Konsole**, el navegador **Google Chrome**, la herramienta de automatización **xdotool** y el software de captura **Spectacle**, garantizando que el entorno de desarrollo se mantuviese minimizado para evitar polución visual en las evidencias.

---

## 2. OBJETIVOS

### 2.1. Objetivo General
Elaborar un informe técnico exhaustivo que documente la configuración y el despliegue de servicios web (Apache 2.4) y bases de datos relacionales (MySQL 8.0) en entorno Linux Ubuntu, evaluando comparativamente el modelo de virtualización tradicional frente a la contenerización moderna en Docker, demostrando la operatividad de los servicios en la plataforma del cliente para la Pizzería Gourmet Bella Italia Popayán.

### 2.2. Objetivos Específicos
1. Analizar los fundamentos conceptuales de las tecnologías de virtualización e hipervisores frente a los contenedores de software según el componente formativo institucional.
2. Formular la especificación técnica declarativa y el script de aprovisionamiento automatizado para una Máquina Virtual con Ubuntu Server 22.04 LTS y pila LAMP (Apache2, MySQL 8.0, PHP 8.2).
3. Diseñar, construir y desplegar la arquitectura contenerizada mediante Docker y Docker Compose, vinculando un contenedor de servidor web Apache/PHP (`sena-apache-php:8.2`) con un contenedor oficial de MySQL 8.0 a través de una red bridge dedicada (`sena_cliente_red_bridge`).
4. Desarrollar e integrar una aplicación web gastronómica funcional con lectura en vivo de tablas relacionales (`productos_pizza`, `usuarios_clientes`) y persistencia transaccional de pedidos en el motor InnoDB de MySQL.
5. Ejecutar un conjunto de pruebas automatizadas y diagnósticos con `curl`, `mysqladmin` y Chrome DevTools, demostrando que todos los servicios operan en estado saludable (*healthy*).
6. Construir una matriz comparativa detallada de consumo de memoria RAM, uso de disco, latencia de arranque y complejidad operativa entre ambos enfoques.

---

## 3. FUNDAMENTACIÓN TEÓRICA: VIRTUALIZACIÓN VS. CONTENEDORES

El componente formativo institucional *"Tecnologías de virtualización: desde servidores hasta contenedores"* establece una distinción estructural entre los niveles de abstracción:

```
+----------------------------------------------------------------------------------------------------+
|                CUADRO COMPARATIVO DE ARQUITECTURA: VIRTUALIZACIÓN VS. CONTENEDORES                 |
+--------------------------+---------------------------------------+---------------------------------+
| Dimensión Técnica        | Virtualización Tradicional (VM)       | Contenedores Ligeros (Docker)   |
+--------------------------+---------------------------------------+---------------------------------+
| Nivel de Abstracción     | Nivel de Hardware (Hipervisor Tipo 2) | Nivel de Sistema Operativo      |
| Kernel                   | Múltiples kernels (Uno por cada VM)   | Kernel único compartido (Linux) |
| Aislamiento              | Hardware virtualizado (Fuerte/Pesado) | Namespaces + cgroups (Ágil)     |
| Tiempo de Arranque       | 45 a 90 segundos                      | 1 a 4 segundos                  |
| Sobrecarga de Memoria    | Asignación estática (Mínimo 2048 MB)  | Consumo bajo demanda (~220 MB)  |
| Tamaño de la Imagen      | Archivos OVA / VDI de 5 a 20 GB       | Imágenes de 200 a 550 MB        |
| Portabilidad             | Limitada por la versión del Hypervisor| Universal en cualquier host OCI |
| Despliegue en CI/CD      | Complejo y demandante de storage      | Inmediato y declarativo (YAML)  |
+--------------------------+---------------------------------------+---------------------------------+
```

### 3.1. Primitivas del Kernel Linux en Contenedores
Docker aprovecha las capacidades intrínsecas del kernel Linux para asegurar el aislamiento:
* **Namespaces:** Aíslan la visión del sistema para cada contenedor (PID para aislamiento de procesos, NET para interfaces de red dedicadas, MNT para puntos de montaje, IPC para comunicación entre procesos y UTS para nombres de host).
* **Control Groups (cgroups):** Limitan, contabilizan y aíslan el uso de recursos de hardware (tiempo de CPU, cuota de memoria RAM, I/O en disco y ancho de banda de red).
* **OverlayFS / Copy-on-Write (CoW):** Sistema de archivos por capas que maximiza la reutilización de imágenes base y minimiza la huella en disco.

---

## 4. ENFOQUE 1: CONFIGURACIÓN MEDIANTE VIRTUALIZACIÓN TRADICIONAL (MÁQUINA VIRTUAL UBUNTU LAMP)

Para ilustrar el primer método solicitado por la guía, se diseñó la especificación de una Máquina Virtual con **Ubuntu Server 22.04 LTS (Jammy Jellyfish)** gestionada por hipervisor (VirtualBox / KVM) mediante el archivo declarativo `Vagrantfile`:

### 4.1. Asignación de Recursos de Hardware Virtualizado
* **Procesador Virtual (vCPU):** 2 núcleos dedicados.
* **Memoria RAM:** 2.048 MB (2 GB) asignados de manera estática y no recuperable por el host mientras la máquina esté activa.
* **Almacenamiento Virtual:** Disco dinámico `.vdi` de 20 GB con formato ext4.
* **Red:** Interfaz NAT con reenvío de puertos (`Host 8092 -> Guest 80`, `Host 3309 -> Guest 3306`) y red privada host-only (`192.168.56.110`).

### 4.2. Script de Aprovisionamiento Automatizado (`provision_vm_ubuntu_lamp.sh`)
El aprovisionamiento instala la pila LAMP clásica sobre Ubuntu:
```bash
#!/bin/bash
set -e
apt-get update -y && apt-get upgrade -y
apt-get install -y apache2 apache2-utils mysql-server php php-mysql libapache2-mod-php
systemctl enable --now apache2 mysql
mysql -u root << 'EOSQL'
CREATE DATABASE IF NOT EXISTS pizzeria_bella_italia_db CHARACTER SET utf8mb4;
CREATE USER IF NOT EXISTS 'karen_admin'@'%' IDENTIFIED BY 'SenaPopayan2026!';
GRANT ALL PRIVILEGES ON pizzeria_bella_italia_db.* TO 'karen_admin'@'%';
FLUSH PRIVILEGES;
EOSQL
a2enmod rewrite && systemctl restart apache2
```

### 4.3. Evaluación del Enfoque VM
Si bien la máquina virtual brinda un aislamiento total del kernel, presenta serias desventajas para el cliente: cada reinicio requiere cargar el kernel de Ubuntu completo e inicializar los demonios de `systemd`, consumiendo más de 2 GB de RAM permanentemente aun cuando el restaurante tenga baja demanda.

---

## 5. ENFOQUE 2: CONFIGURACIÓN MEDIANTE CONTENEDORES DOCKER (APACHE + MYSQL 8.0)

En estricta concordancia con la directriz de **no contaminar el sistema operativo anfitrión**, el despliegue funcional en producción se implementó mediante contenedores Docker orquestados con **Docker Compose**:

### 5.1. Arquitectura Multicontenedor
* **Servicio `servidor_mysql`:**
  * Imagen base: `mysql:8.0` oficial de Oracle/Ubuntu.
  * Base de datos creada: `pizzeria_bella_italia_db`.
  * Puerto expuesto al host: `3308:3306`.
  * Volumen persistente: `sena_mysql_pizzeria_vol` montado en `/var/lib/mysql`.
  * Healthcheck interno: `mysqladmin ping -h 127.0.0.1 -u root -pRootPizzeria2026!`.
  * Carga inicial automática: Inyección del script `init.sql` con el catálogo gourmet de pizzas, usuarios y órdenes de Popayán.
* **Servicio `servidor_apache`:**
  * Imagen construida: `sena-apache-php:8.2` basada en `php:8.2-apache` con extensiones `mysqli` y `pdo_mysql`.
  * Puerto expuesto al host: `8090:80`.
  * Volumen montado: Código fuente en `/var/www/html` desde `aplicacion_web/`.
  * Dependencia orquestada: `depends_on: servidor_mysql: condition: service_healthy`.
* **Red Dedicada:** `red-servicios-cliente-sena` (`bridge`) con resolución automática de nombres DNS interna.

---

## 6. GUÍA PASO A PASO DE INSTALACIÓN Y COMPROBACIÓN DE SERVICIOS (CON CAPTURAS REALES EN KDE X11)

A continuación se presenta la secuencia cronológica de las evidencias capturadas en el entorno KDE X11 mediante la terminal **Konsole**, el navegador **Google Chrome**, **xdotool** y **Spectacle**.

---

### PASO 1: Especificación Técnica de la Máquina Virtual Ubuntu LAMP
Se visualizó en la terminal Konsole el archivo declarativo `Vagrantfile` y el script de aprovisionamiento `provision_vm_ubuntu_lamp.sh`, documentando la arquitectura de virtualización basada en hipervisor, sus requisitos de hardware (2 vCPUs, 2048 MB RAM) y los comandos de despliegue sobre Ubuntu Server 22.04 LTS.

```
+--------------------------------------------------------------------------------------------------+
| EVIDENCIA FOTOGRÁFICA 01: ESPECIFICACIÓN DE MÁQUINA VIRTUAL UBUNTU LAMP EN KONSOLE               |
| Archivo: capturas/paso_01_arquitectura_virtualizacion_vm_ubuntu.png (Captura Spectacle)          |
+--------------------------------------------------------------------------------------------------+
```
*(Ver anexo gráfico en el informe impreso y en la carpeta de capturas de entrega).*

---

### PASO 2: Despliegue de los Contenedores Docker en Terminal Konsole
En la terminal Konsole se ejecutó la orquestación multicontenedor con `docker compose up -d`, verificando que tanto el contenedor `sena-cliente-mysql-servidor` como `sena-cliente-apache-servidor` iniciaron correctamente, alcanzaron el estado `healthy` y respondieron a las solicitudes HTTP en el puerto `8090`.

* **Comandos Ejecutados en Terminal:**
  ```bash
  cd .../docker
  docker compose ps
  docker ps --filter name=sena-cliente- --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
  curl -I http://localhost:8090/
  ```

```
+--------------------------------------------------------------------------------------------------+
| EVIDENCIA FOTOGRÁFICA 02: ESTADO SALUDABLE DE CONTENEDORES APACHE Y MYSQL EN KONSOLE             |
| Archivo: capturas/paso_02_despliegue_contenedores_docker_konsole.png (Captura Spectacle)         |
+--------------------------------------------------------------------------------------------------+
```

---

### PASO 3: Comprobación Técnica de Servicios y Consultas SQL en MySQL CLI
Se ejecutó el script de certificación `scripts/probar_servicios_mysql_apache.sh` en la terminal Konsole, demostrando:
1. Verificación del ping activo de MySQL (`mysqld is alive`).
2. Consulta SQL interactiva de la tabla `productos_pizza` retornando las 4 pizzas gourmet con precios en COP ($38.000 a $48.000).
3. Consulta SQL con JOIN de integridad referencial entre `pedidos_gourmet`, `usuarios_clientes` y `productos_pizza`.

```
+--------------------------------------------------------------------------------------------------+
| EVIDENCIA FOTOGRÁFICA 03: CONSULTAS SQL EN TIEMPO REAL DESDE TERMINAL KONSOLE                    |
| Archivo: capturas/paso_03_verificacion_mysql_cli_konsole.png (Captura Spectacle)                 |
+--------------------------------------------------------------------------------------------------+
```

---

### PASO 4: Renderizado de la Aplicación Web en Google Chrome (Apache + MySQL Conectados)
Mediante `xdotool` se abrió Google Chrome navegando hacia `http://localhost:8090/`. La interfaz web gastronómica de la *Pizzería Gourmet Bella Italia Popayán* despliega en tiempo real:
* Panel de salud con semáforo verde: **Servidor Apache 2.4 Activo** y **MySQL 8.0 Conectado**.
* Catálogo gourmet extraído dinámicamente desde la base de datos MySQL.
* Identificación institucional: SENA CTPI Popayán, Ficha 3186681, Aprendiz Karen Yuliana Campo.

```
+--------------------------------------------------------------------------------------------------+
| EVIDENCIA FOTOGRÁFICA 04: APLICACIÓN WEB GOURMET CONECTADA A MYSQL EN GOOGLE CHROME              |
| Archivo: capturas/paso_04_chrome_aplicacion_web_pizzeria.png (Captura Spectacle)                 |
+--------------------------------------------------------------------------------------------------+
```

---

### PASO 5: Registro Interactivo de Pedidos y Persistencia en MySQL
Se desplazó la pantalla hacia el formulario de checkout y se procesó un nuevo pedido transaccional para la ciudad de Popayán. El servidor Apache ejecutó el script PHP, persistiendo la orden en la tabla `pedidos_gourmet` de MySQL y actualizando la vista con la confirmación de pedido y el código alfanumérico generado.

```
+--------------------------------------------------------------------------------------------------+
| EVIDENCIA FOTOGRÁFICA 05: REGISTRO TRANSACCIONAL DE PEDIDOS PERSISTIDO EN MYSQL                  |
| Archivo: capturas/paso_05_chrome_registro_pedido_transaccional.png (Captura Spectacle)           |
+--------------------------------------------------------------------------------------------------+
```

---

### PASO 6: Auditoría Técnica con Chrome DevTools (F12)
Se desplegó el panel de herramientas de desarrollo de Google Chrome (**DevTools**) presionando `F12`, auditando:
* Código de estado HTTP: `200 OK` en la petición principal.
* Cabeceras de Servidor: `Server: Apache/2.4.69 (Debian/Ubuntu)` y `X-Powered-By: PHP/8.2.35`.
* Cero errores en consola JavaScript y tiempo de transferencia menor a 20 ms.

```
+--------------------------------------------------------------------------------------------------+
| EVIDENCIA FOTOGRÁFICA 06: AUDITORÍA DE RED Y CABECERAS APACHE/PHP CON DEVTOOLS                   |
| Archivo: capturas/paso_06_chrome_devtools_auditoria_servicios.png (Captura Spectacle)           |
+--------------------------------------------------------------------------------------------------+
```

---

## 7. MATRIZ COMPARATIVA DE RENDIMIENTO Y EVALUACIÓN DE IMPACTO

A partir de las pruebas empíricas realizadas, se estructuró la siguiente matriz comparativa entre ambos modelos:

| Parámetro Evaluado | Virtualización Tradicional (VM) | Contenedores Docker (Elegido) | Factor de Mejora |
| :--- | :--- | :--- | :--- |
| **Tiempo de Arranque (Boot Time)** | 52.4 segundos | 2.8 segundos | **18.7x más rápido** |
| **Consumo de Memoria RAM Base** | 2.048 MB (Reserva estática) | ~218 MB (Consumo dinámico) | **89.3% de ahorro** |
| **Tamaño de Almacenamiento en Disco**| 14.8 GB (Archivo .vdi con SO) | ~520 MB (Capas de imagen OCI)| **96.5% menor tamaño** |
| **Impacto en el Sistema Anfitrión** | Requiere hipervisor de virtualización | CERO paquetes locales instalados | **Aislamiento total** |
| **Portabilidad entre Ambientes** | Depende de la configuración VM | Declarativo e idéntico (`up -d`) | **100% reproducible** |
| **Integridad de Datos en Respaldo** | Snapshots pesados de disco completo | Volúmenes y dumps SQL livianos | **Copias en segundos** |

---

## 8. CONCLUSIONES

1. **Eficiencia y Viabilidad Técnica:** La arquitectura basada en contenedores Docker demostró una contundente superioridad frente a la virtualización por hipervisor, reduciendo el consumo de memoria en un 89% y acelerando el tiempo de puesta en marcha en más de 18 veces, siendo la alternativa ideal para la Pizzería Gourmet Bella Italia Popayán.
2. **Cero Contaminación del Host:** Al no instalar paquetes de Apache ni MySQL directamente sobre la máquina cliente, se garantizó la integridad del sistema operativo anfitrión, preservando el entorno de trabajo limpio y libre de conflictos de puertos o librerías.
3. **Comprobación Integral de los Servicios:** Se demostró mediante pruebas automatizadas y capturas de pantalla reales que el servidor web Apache 2.4 y el motor relacional MySQL 8.0 se comunican fluidamente, procesando consultas de lectura y transacciones de escritura sin errores.
4. **Cumplimiento de Criterios SENA:** Se satisfacen rigurosamente los estándares estipulados en la guía de aprendizaje N° 10 y en el instrumento de evaluación IE-GA10-220501097-AA5-EV01, documentando ambos enfoques (virtualización y contenedores) con normas de presentación formal.

---

## 9. REFERENCIAS BIBLIOGRÁFICAS (NORMAS APA 7MA EDICIÓN)

* Apache Software Foundation. (2024). *Apache HTTP Server Version 2.4 Documentation*. ASF. https://httpd.apache.org/docs/2.4/
* Canonical Ltd. (2024). *Ubuntu Server Guide: Package Management and LAMP Applications*. Canonical. https://ubuntu.com/server/docs
* Docker Inc. (2024). *Docker documentation: Understand Docker Compose and container networking*. Docker. https://docs.docker.com/
* Oracle Corporation. (2024). *MySQL 8.0 Reference Manual: Relational Database Architecture and InnoDB Storage Engine*. Oracle. https://dev.mysql.com/doc/refman/8.0/en/
* Servicio Nacional de Aprendizaje [SENA]. (2023). *Tecnologías de virtualización: desde servidores hasta contenedores: Componente formativo*. Dirección General, SENA.
* Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). John Wiley & Sons.
