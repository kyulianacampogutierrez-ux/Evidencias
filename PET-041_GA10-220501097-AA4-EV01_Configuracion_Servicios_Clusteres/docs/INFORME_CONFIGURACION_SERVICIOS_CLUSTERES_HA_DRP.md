# SERVICIO NACIONAL DE APRENDIZAJE - SENA
## CENTRO DE TELEINFORMÁTICA Y PRODUCCIÓN INDUSTRIAL (CTPI) - REGIONAL CAUCA
### TECNOLOGÍA EN ANÁLISIS Y DESARROLLO DE SOFTWARE (ADSO) - MODALIDAD VIRTUAL
**FICHA DE CARACTERIZACIÓN:** 3186681

---

# EVIDENCIA GA10-220501097-AA4-EV01: CONCEPTOS Y PRINCIPIOS ACERCA DE CONFIGURACIÓN DE SERVICIOS
## INFORME TÉCNICO DE GESTIÓN DE REDUNDANCIA, ALTA DISPONIBILIDAD, ARQUITECTURA DE CLÚSTERES Y PLANES DE CONTINUIDAD (BCP / DRP)
### Fase de Ejecución • Actividad de Proyecto AP8: Desarrollar las tareas de configuración y puesta en marcha del sistema de información

- **Competencia Técnica:** 220501097 - Implementar la solución de software de acuerdo con los requisitos de operación y modelos de referencia.
- **Actividad de Aprendizaje:** GA10-220501097-AA4 - Configurar los servicios requeridos, de acuerdo con la arquitectura.
- **Resultado de Aprendizaje (RAP 2):** 220501097-02 - Desplegar el software de acuerdo con la arquitectura y las políticas establecidas.
- **Componente Formativo:** *“Gestión de redundancia y alta disponibilidad”*.
- **Instrumento de Evaluación:** Lista de Chequeo IE-GA10-220501097-AA4-EV01.
- **Proyecto Formativo Integrador:** Construcción de software integrador de tecnologías orientadas a servicios (*Pizzería Gourmet Bella Italia Popayán*).
- **Aprendiz:** Karen Yuliana Campo
- **Lugar y Fecha:** Popayán, Cauca - Noviembre de 2026

---

## 1. INTRODUCCIÓN

En la era contemporánea de los servicios digitales y la computación en la nube, la disponibilidad continua, la tolerancia a fallos y la resiliencia operativa han dejado de ser atributos deseables para convertirse en requisitos de operación estrictamente obligatorios. Una solución de software corporativa —incluso si ha sido codificada bajo los más depurados patrones de diseño y estándares de calidad— resulta inútil y perjudicial para el negocio si experimenta caídas imprevistas del servicio durante horas de alta transaccionalidad, si pierde pedidos de clientes debido a fallos de almacenamiento o si carece de mecanismos ágiles para restaurar sus operaciones tras un incidente técnico o físico fortuito.

El despliegue de infraestructuras tecnológicas modernas exige la adopción sistemática de **arquitecturas en clúster** y estrategias estructuradas de **gestión de redundancia y alta disponibilidad (HA - High Availability)**. La interconexión cooperativa de múltiples nodos informáticos independientes que actúan de cara al usuario como un único sistema coordinado permite no solo distribuir de manera equilibrada las cargas de trabajo (*Load Balancing*), sino también eliminar los **Puntos Únicos de Falla (SPOF - Single Points of Failure)** mediante la conmutación automática por error (*Failover*).

Asimismo, la gestión de la infraestructura tecnológica no se limita al ensamblaje de hardware y software; demanda un marco riguroso de gobernanza de riesgos que comprende el **Análisis de Impacto en el Negocio (BIA)**, la definición estricta de las métricas de resiliencia **RPO (Recovery Point Objective)** y **RTO (Recovery Time Objective)**, y la formalización de **Planes de Continuidad del Negocio (BCP)** y **Planes de Recuperación de Desastres (DRP)**.

El presente informe técnico aborda de forma exhaustiva los conceptos, herramientas, tipos de procesamiento, ventajas y desventajas de las arquitecturas de clústeres exigidos por la Guía de Aprendizaje N° 10 del SENA. Tomando como escenario de aplicación real el proyecto formativo **Pizzería Gourmet Bella Italia Popayán**, se diseña una arquitectura de alta disponibilidad de cinco niveles (redundancia WAN dual, balanceo de carga HA, réplicas de microservicios, clúster de base de datos PostgreSQL y política de respaldo 3-2-1), asegurando la continuidad del negocio frente a las condiciones e incidentes reales del entorno regional en el departamento del Cauca.

---

## 2. OBJETIVOS

### 2.1. Objetivo General
Elaborar un informe técnico exhaustivo sobre conceptos y principios de configuración de servicios, gestión de redundancia y alta disponibilidad, evaluando herramientas, tipologías y modelos de procesamiento en arquitecturas de clústeres, y estructurando los planes de continuidad del negocio (BCP) y recuperación de desastres (DRP) para la operación continua de la *Pizzería Gourmet Bella Italia Popayán*.

### 2.2. Objetivos Específicos
1. Identificar, clasificar y describir las herramientas y tecnologías utilizadas en arquitecturas de clústeres, contrastando los tipos de clústeres (Alta Disponibilidad, Balanceo de Carga, Alto Rendimiento y Almacenamiento Distribuido).
2. Analizar los tipos de procesamiento que se llevan a cabo en arquitecturas de clústeres (paralelo, distribuido/concurrente, por lotes y en tiempo real), sopesando sus ventajas y desventajas bajo el Teorema CAP.
3. Fundamentar la gestión de continuidad del negocio mediante el Análisis de Riesgos y el Análisis de Impacto en el Negocio (BIA), estableciendo la jerarquía de prioridades de servicio y las métricas RPO y RTO.
4. Diferenciar estructuralmente el Plan de Continuidad del Negocio (BCP) del Plan de Recuperación de Desastres (DRP), definiendo protocolos de gestión de crisis y metodologías de pruebas de operación (tabletop, failover drills e ingeniería del caos).
5. Diseñar la arquitectura técnica de alta disponibilidad y la política de copias de seguridad 3-2-1 para el sistema de información de la Pizzería Bella Italia Popayán, verificando el cumplimiento de la lista de chequeo IE-GA10-220501097-AA4-EV01.

---

## 3. ARQUITECTURA DE CLÚSTERES: CONCEPTOS, HERRAMIENTAS Y TAXONOMÍA

### 3.1. Definición y Principios de la Computación en Clúster
Un **clúster de computación** consiste en un conjunto de computadoras independientes (denominadas **nodos**), interconectadas mediante una red de alta velocidad y gobernadas por un software de agrupamiento (*clustering middleware*), que cooperan estrechamente para ejecutar tareas de forma coordinada, presentándose ante los clientes y aplicaciones como si fuesen un único recurso computacional unificado (*Single System Image - SSI*).

El principio fundacional de un clúster es la **eliminación de Puntos Únicos de Falla (SPOF)** y la habilitación de la **escalabilidad horizontal (*Scale-Out*)**, permitiendo incrementar la capacidad de procesamiento o almacenamiento del sistema simplemente agregando nuevos nodos estándar al conjunto, en contraste con la escalabilidad vertical (*Scale-Up*), que consiste en adquirir hardware más potente y costoso para un único servidor.

```
                  ARQUITECTURA CONCEPTUAL DE UN CLÚSTER DISTRIBUIDO
┌───────────────────────────────────────────────────────────────────────────────────────┐
│                     CLIENTES HETEROGÉNEOS (Web, Móvil, POS, APIs)                     │
└──────────────────────────────────────────┬────────────────────────────────────────────┘
                                           │ Solicitudes de Servicio (HTTPS / TCP)
┌──────────────────────────────────────────┴────────────────────────────────────────────┐
│         CAPA DE ENTRADA Y BALANCEO DE CARGA (Virtual IP - VIP / Keepalived)           │
├──────────────────────────────────────────┬────────────────────────────────────────────┤
│           NODO BALANCEADOR 1 (Master)    │           NODO BALANCEADOR 2 (Backup)      │
└──────────────────────────────────────────┴────────────────────────────────────────────┘
                                           │ Distribución Inteligente de Carga
┌──────────────────────────────────────────┴────────────────────────────────────────────┐
│                    RED INTERNA DEL CLÚSTER (Interconexión Privada)                    │
├──────────────────────────┬─────────────────────────────┬──────────────────────────────┤
│      NODO TRABAJADOR 1   │      NODO TRABAJADOR 2      │      NODO TRABAJADOR 3       │
│      (Worker Node A)     │      (Worker Node B)        │      (Worker Node C)         │
│   • Contenedores Docker  │   • Contenedores Docker     │   • Contenedores Docker      │
│   • API REST Spring Boot │   • API REST Spring Boot    │   • API REST Spring Boot     │
├──────────────────────────┴─────────────────────────────┴──────────────────────────────┤
│          ALMACENAMIENTO COMPARTIDO / REPLICADO (PostgreSQL HA / Ceph / NAS)           │
└───────────────────────────────────────────────────────────────────────────────────────┘
```

### 3.2. Tipos de Clústeres
Dependiendo de su propósito primario y de la estrategia de optimización de recursos, los clústeres se clasifican en cuatro grandes familias:

#### 3.2.1. Clústeres de Alta Disponibilidad (HA - High Availability / Failover Clusters)
Diseñados con el objetivo primordial de garantizar la **continuidad del servicio ininterrumpida**, alcanzando niveles de disponibilidad del 99.9% ("tres nueves" - máx. 8.76 horas de inactividad anual) al 99.999% ("cinco nueves" - máx. 5.26 minutos de inactividad anual).
- **Mecanismo de Detección de Fallos (Heartbeat):** Los nodos intercambian continuamente señales de latido a través de la red privada. Si el nodo primario deja de emitir latidos durante un umbral temporal predefinido, el clúster asume que ha colapsado.
- **Conmutación por Error (Failover):** El software del clúster promueve automáticamente un nodo de respaldo (*standby*) a nodo maestro (*master*), reasignando la Dirección IP Virtual (VIP) y montando los volúmenes de almacenamiento correspondientes sin intervención humana.
- **Topologías HA:**
  - *Activo-Pasivo:* El nodo primario atiende el 100% del tráfico mientras el secundario permanece en espera caliente (*Hot Standby*). Es el esquema clásico para bases de datos relacionales como PostgreSQL.
  - *Activo-Activo:* Todos los nodos atienden peticiones simultáneamente; si uno falla, los nodos restantes absorben la carga del nodo caído.
- **Mecanismos de Fencing y STONITH:** Para evitar el catastrófico fenómeno de **Split-Brain** (donde una partición de red hace que dos nodos crean que el otro ha muerto y ambos intenten escribir en el mismo almacenamiento corrompiendo los datos), el clúster implementa mecanismos de cercado (*fencing*) como STONITH (*Shoot The Other Node In The Head*), que corta físicamente el suministro eléctrico del nodo sospechoso mediante PDUs inteligentes o interfaces IPMI.
- **Herramientas Tecnológicas:** *Pacemaker*, *Corosync*, *Keepalived (VRRP)*, *Patroni* (para PostgreSQL).

#### 3.2.2. Clústeres de Balanceo de Carga (Load Balancing Clusters)
Diseñados para optimizar el rendimiento y la capacidad de atención simultánea, distribuyendo las solicitudes entrantes de los clientes de manera equitativa entre un grupo de servidores réplica (*Server Farm* o *Backend Pool*).
- **Algoritmos de Balanceo:**
  - *Round Robin:* Asignación secuencial cíclica (nodo 1, nodo 2, nodo 3, nodo 1...).
  - *Weighted Round Robin:* Asignación proporcional a la potencia de hardware de cada nodo.
  - *Least Connections:* Envía la nueva solicitud al nodo que tenga el menor número de conexiones activas en ese instante.
  - *IP Hash:* Calcula un hash de la dirección IP del cliente para garantizar persistencia de sesión (*Sticky Sessions*).
- **Monitoreo de Salud (Health Checks):** El balanceador sondea periódicamente a los nodos backend (ej. solicitando un endpoint HTTP `/health`). Si un nodo responde con error o no contesta, es retirado automáticamente del grupo de servidores activos en milisegundos.
- **Herramientas Tecnológicas:** *Nginx Load Balancer*, *HAProxy*, *Traefik*, *AWS Application Load Balancer (ALB)*.

#### 3.2.3. Clústeres de Alto Rendimiento (HPC - High Performance Computing)
Orientados a resolver problemas computacionales intensivos que exceden la capacidad de cualquier supercomputadora monoprocesador.
- **Funcionamiento:** Se basan en descomponer un problema masivo en miles de subtareas independientes que se ejecutan en paralelo en cientos o miles de núcleos de procesamiento, comunicándose mediante bibliotecas de paso de mensajes de muy baja latencia.
- **Aplicaciones:** Modelado climático, simulaciones astrofísicas, genómica, renderizado de efectos visuales cinematográficos y entrenamiento de redes neuronales de Inteligencia Artificial.
- **Herramientas Tecnológicas:** *Slurm Workload Manager*, *OpenMPI*, *MPICH*, *Beowulf Clusters*.

#### 3.2.4. Clústeres de Almacenamiento Distribuido (Storage Clusters)
Sistemas que unifican el almacenamiento de múltiples servidores físicos para presentar un único sistema de archivos o almacenamiento de bloques virtualizado, tolerante a la pérdida física de discos o chasis completos.
- **Mecanismos:** Implementan replicación síncrona o codificación de borrado (*Erasure Coding*), distribuyendo fragmentos de datos y paridad entre diferentes nodos de la red.
- **Herramientas Tecnológicas:** *Ceph Storage*, *GlusterFS*, *DRBD (Distributed Replicated Block Device)*, *MinIO (S3 compatible)*.

---

### 3.3. Tipos de Procesamiento en Clústeres

| TIPO DE PROCESAMIENTO | CARACTERÍSTICAS PRINCIPALES | MODELO DE COMUNICACIÓN | EJEMPLO EN LA INDUSTRIA / SOFTWARE |
| :--- | :--- | :--- | :--- |
| **Procesamiento Paralelo** | Una única tarea masiva se divide en fragmentos sincrónicos ejecutados simultáneamente en múltiples núcleos. | Memoria compartida o paso de mensajes (MPI) con sincronización estricta por barreras. | Cálculo numérico científico, simulaciones de fluidos, entrenamiento de modelos LLM. |
| **Procesamiento Distribuido / Concurrente** | Múltiples tareas o microservicios independientes se comunican a través de la red de manera asíncrona. | Protocolos de red (HTTP REST, gRPC, RPC) o colas de mensajería (RabbitMQ, Kafka). | **Arquitectura de Microservicios de la Pizzería Bella Italia (API Spring Boot + PostgreSQL).** |
| **Procesamiento por Lotes (Batch Processing)** | Ejecución de grandes volúmenes de datos históricos sin requerir interacción en tiempo real del usuario. | Procesamiento secuencial en ventanas de bajo tráfico nocturno con planificación (*schedulers*). | Generación nocturna de balances contables, liquidación de nómina, consolidación fiscal DIAN. |
| **Procesamiento en Tiempo Real (Stream Processing)** | Procesamiento continuo de flujos de eventos inmediatos a medida que se generan, con latencias de milisegundos. | Arquitectura orientada a eventos (*Event-Driven Architecture*) mediante brokers de streaming. | Telemetría de pedidos de delivery en tiempo real, detección de fraude con tarjetas de crédito. |

---

### 3.4. Ventajas y Desventajas de las Arquitecturas de Clústeres

#### 3.4.1. Ventajas
1. **Alta Disponibilidad y Resiliencia:** La falla de un nodo individual no detiene la operación del software; los demás nodos absorben la carga de trabajo de manera transparente.
2. **Escalabilidad Horizontal Económica:** Permite iniciar con dos servidores modestos y añadir nodos a medida que el negocio de la pizzería crece, utilizando hardware comercial estándar (*commodity hardware*) sin incurrir en costos astronómicos de servidores propietarios.
3. **Mantenimiento sin Interrupción (*Zero-Downtime Maintenance*):** Facilita realizar actualizaciones de seguridad del sistema operativo o despliegues de nuevas versiones de la aplicación mediante la técnica de actualización rodante (*Rolling Updates*), aislando un nodo para mantenimiento mientras los demás atienden a los usuarios.
4. **Optimización del Rendimiento:** Distribuye la concurrencia entre múltiples procesadores y tarjetas de red, reduciendo los tiempos de respuesta percibidos por los clientes.

#### 3.4.2. Desventajas y Desafíos Técnicos
1. **Complejidad de Configuración y Gestión:** Requiere conocimientos avanzados en redes, protocolos de sincronización, cuórum y software de orquestación. Un error de configuración puede inducir fallos en cadena.
2. **Problema del Teorema CAP:** Enunciado por Eric Brewer, postula que en un sistema distribuido es imposible garantizar simultáneamente:
   - **Consistencia (C):** Todos los nodos ven exactamente los mismos datos al mismo tiempo.
   - **Disponibilidad (A):** Cada solicitud recibe una respuesta válida sin garantía de ser la más reciente.
   - **Tolerancia a Particiones (P):** El sistema sigue funcionando a pesar de pérdidas de mensajes en la red.
   Dado que las particiones de red son inevitables en el mundo real, los sistemas deben elegir entre **CP** (Consistencia estricta como en PostgreSQL) o **AP** (Alta disponibilidad eventual como en bases de datos NoSQL tipo Cassandra/DynamoDB).
3. **Riesgo de Split-Brain:** Si la red de comunicación entre nodos se corta pero ambos nodos continúan encendidos, cada partición asume que la otra ha muerto y ambas intentan operar como maestras, sobrescribiendo datos de manera divergente e irreparable.
4. **Sobrecarga de Red (*Overhead*):** El tráfico constante de sincronización de estado, replicación de datos y latidos (*heartbeat*) consume una porción del ancho de banda disponible.

---

## 4. GESTIÓN DE CONTINUIDAD DEL NEGOCIO Y RESILIENCIA OPERATIVA

La infraestructura tecnológica no opera en el vacío; existe para respaldar los procesos productivos de la organización. Por ello, la ingeniería de software moderna integra la resiliencia tecnológica dentro del marco global de la **Continuidad del Negocio (Norma ISO 22301)**.

### 4.1. Análisis de Riesgos (Risk Assessment)
Proceso sistemático de identificación de amenazas que pueden comprometer la plataforma tecnológica, evaluando su probabilidad de ocurrencia y el impacto potencial sobre la operación.

Para la *Pizzería Gourmet Bella Italia*, ubicada en la ciudad de Popayán (departamento del Cauca), se elaboró la siguiente **Matriz de Riesgos**:

| AMENAZA IDENTIFICADA | PROBABILIDAD (1-5) | IMPACTO (1-5) | NIVEL DE RIESGO | MEDIDAS DE MITIGACIÓN Y CONTROL |
| :--- | :---: | :---: | :---: | :--- |
| **Corte de Suministro Eléctrico en Popayán** | **5** (Muy Alta) | **4** (Grave) | 🔴 **CRÍTICO (20)** | Sistema UPS interactivo de 1000 VA (45 min de autonomía) + Generador eléctrico a gas para cortes prolongados. |
| **Corte de Fibra Óptica (Vía Panamericana)** | **4** (Alta) | **4** (Grave) | 🔴 **CRÍTICO (16)** | Enlace Dual WAN en router con conmutación automática (*Failover*) a módem 4G LTE / enlace satelital Starlink. |
| **Fallo Físico de Disco Duro del Servidor** | **2** (Baja) | **5** (Catastrófico) | 🟠 **ALTO (10)** | Arreglo de discos RAID 1 en espejo (SSD NVMe) + Replicación física streaming continua hacia nodo secundario. |
| **Ataque de Ransomware / Malware** | **2** (Baja) | **5** (Catastrófico) | 🟠 **ALTO (10)** | Copias de seguridad 3-2-1 cifradas e inmutables almacenadas en la nube (AWS S3 Object Lock) fuera de la red local. |
| **Caída del Proceso Backend Java / Out of Memory** | **3** (Media) | **3** (Moderado) | 🟡 **MEDIO (9)** | Contenedores Docker orquestados con reinicio automático (`restart: always`), límites de memoria JVM y réplicas HA. |
| **Error Humano en Base de Datos (DROP / DELETE)** | **2** (Baja) | **4** (Grave) | 🟡 **MEDIO (8)** | Prohibición de acceso directo a producción en consola; backups lógicos diarios y recuperación Point-in-Time (PITR). |

---

### 4.2. Análisis de Impacto en el Negocio (BIA - Business Impact Analysis)
El BIA cuantifica las consecuencias operativas y financieras derivadas de la interrupción de los servicios de software en el tiempo:
- **Pérdida Financiera Directa:** Se calcula una pérdida promedio de **$350.000 COP por hora de inactividad** en días laborables y hasta **$900.000 COP por hora** durante las noches de fin de semana (viernes a domingo de 07:00 PM a 11:00 PM), derivado de órdenes no procesadas en mesa y cancelaciones de pedidos a domicilio.
- **Pérdida Reputacional y Confianza:** El cliente que acude a un restaurante gastronómico no tolera retrasos en la comanda por *"caídas del sistema"*, derivando en críticas negativas en redes sociales y pérdida de recurrencia.
- **Sanciones Legales y Fiscales:** La imposibilidad de emitir facturación electrónica válida ante la DIAN puede acarrear sanciones de clausura temporal del establecimiento comercial.

### 4.3. Gestión de Prioridades de los Servicios
Con base en el BIA, los módulos de software se clasifican en tres niveles de criticidad:
- **Prioridad 1 (P1 - Crítica / Esencial para la Vida del Negocio):**
  - Módulo de Toma de Pedidos en Mesas y Terminal de Caja POS.
  - Pasarela de Procesamiento de Pagos con Tarjeta.
  - Base de Datos Transaccional PostgreSQL.
  - *Ventana de indisponibilidad admisible: Menor a 2 minutos.*
- **Prioridad 2 (P2 - Operativa / Importante):**
  - Sistema de Visualización de Cocina (KDS) e Impresoras de Comandas.
  - Facturación Electrónica DIAN (admite operación en contingencia offline por hasta 24 horas).
  - *Ventana de indisponibilidad admisible: Menor a 15 minutos.*
- **Prioridad 3 (P3 - Administrativa / No Urgente):**
  - Módulo de Reportes Estadísticos y Analítica de Ventas.
  - Gestión de Proveedores y Catálogo de Nuevos Platos.
  - *Ventana de indisponibilidad admisible: Hasta 4 a 8 horas.*

---

### 4.4. Métricas Clave de Resiliencia: RPO y RTO

```
                    ANATOMÍA CRONOLÓGICA DE LAS MÉTRICAS RPO Y RTO
        ◄────────────────── RPO ──────────────────►│◄────────────────── RTO ──────────────────►
 ───────┬──────────────────────────────────────────┼──────────────────────────────────────────┬───────
    Último Backup                              INCIDENTE /                               Restauración Total
   o Sincronización                             DESASTRE                                   del Servicio
      (T = -5 min)                              (T = 0)                                   (T = +2 min)
        ▲                                          ▲                                          ▲
        │                                          │                                          │
 Cantidad Máxima Admisible                      Momento                                  Tiempo Máximo
  de Pérdida de Datos                          de Ruptura                              Admisible para la
  (Ventana Transaccional)                     del Servicio                            Reanudación Operativa
```

#### 4.4.1. RPO (Recovery Point Objective - Objetivo de Punto de Recuperación)
Representa la **cantidad máxima admisible de datos que el negocio puede permitirse perder**, medida en unidades de tiempo transcurrido desde el último punto de respaldo consistente hasta el momento del desastre.
- *Meta para la Pizzería Bella Italia:* **RPO < 5 minutos** para órdenes y ventas.
- *Solución Técnica:* Replicación física continua de registros WAL (*Write-Ahead Logging*) en PostgreSQL mediante `pgBackRest`. En el peor escenario de falla catastrófica de hardware, únicamente se perderían los datos de los últimos 5 minutos de operación.

#### 4.4.2. RTO (Recovery Time Objective - Objetivo de Tiempo de Recuperación)
Representa el **tiempo máximo admisible que puede transcurrir desde el instante en que ocurre el desastre hasta que el servicio de software se encuentra nuevamente operativo** y disponible para los usuarios finales.
- *Meta para la Pizzería Bella Italia:* **RTO < 2 minutos** ante fallos de servidor local, y **RTO < 15 minutos** ante desastres físicos totales que requieran conmutar al sitio de contingencia en la nube (*Hot Site Cloud*).
- *Solución Técnica:* Conmutación automática (*Failover*) por error de proxy con Keepalived y balanceadores Nginx en clúster.

#### 4.4.3. Relación Costo vs. RPO / RTO
Existe una relación económica inversamente proporcional: a medida que el RPO y el RTO se aproximan a cero (*Zero-Loss / Instant Recovery*), el costo de la infraestructura se incrementa exponencialmente debido a la necesidad de enlaces dedicados de fibra oscura, almacenamiento síncrono multiditio y licencias de replicación continua. Para la pizzería en Popayán se adoptó un punto de equilibrio óptimo: **RTO de 2 minutos y RPO de 5 minutos**, accesible económicamente mediante tecnologías de código abierto (*Open Source*).

---

### 4.5. Planes de Continuidad (BCP) vs. Planes de Recuperación de Desastres (DRP)

```
                            BCP vs. DRP: ENFOQUES COMPLEMENTARIOS
┌───────────────────────────────────────────────────┬───────────────────────────────────────────────────┐
│     PLAN DE CONTINUIDAD DEL NEGOCIO (BCP)         │     PLAN DE RECUPERACIÓN DE DESASTRES (DRP)       │
├───────────────────────────────────────────────────┼───────────────────────────────────────────────────┤
│ • Alcance: Organizacional, humano y operativo.    │ • Alcance: Estrictamente técnico y de sistemas.   │
│ • Enfoque: ¿Cómo sigue vendiendo el restaurante   │ • Enfoque: ¿Cómo levantamos los servidores y la   │
│   mientras la tecnología está caída?              │   base de datos tras una caída catastrófica?      │
│ • Acciones: Uso de comandas manuales impresas,    │ • Acciones: Conmutación de DNS, restauración de   │
│   cobro con datáfonos celulares autónomos,        │   volúmenes Docker, inyección de logs WAL de      │
│   reubicación de mesas, comunicación con clientes.│   PostgreSQL y despliegue en Hot Site en nube.    │
└───────────────────────────────────────────────────┴───────────────────────────────────────────────────┘
```

### 4.6. Gestión de Crisis y Comité de Emergencia
Para evitar el pánico y las decisiones desordenadas durante una contingencia crítica, se establece un **Comité de Crisis** con roles claramente definidos:
1. **Líder de Crisis (Administrador del Restaurante):** Máxima autoridad operativa; declara formalmente el estado de contingencia y activa el BCP/DRP.
2. **Líder Técnico de Infraestructura (Desarrollador / Tecnólogo ADSO):** Ejecuta los procedimientos de restauración técnica, verifica la integridad de la base de datos y autoriza la reconexión al modo normal.
3. **Líder de Operación en Sala y Cocina (Capitán de Meseros / Jefe de Cocina):** Coordina la toma manual de órdenes y supervisa que el flujo de platos hacia las mesas continúe sin retrasos.

### 4.7. Metodología de Pruebas de Operación y Simulación
Un plan de recuperación no probado es un plan ficticio. La resiliencia del sistema se verifica mediante tres niveles de pruebas programadas:
1. **Prueba de Escritorio (*Tabletop Exercise* - Semestral):** Simulación teórica en sala donde el comité revisa paso a paso los manuales de procedimientos ante un escenario hipotético (ej. corte masivo de telecomunicaciones en Popayán).
2. **Prueba de Conmutación por Error (*Failover Drill* - Trimestral):** Se desconecta intencionalmente el cable de red del nodo primario de base de datos durante una ventana de mantenimiento para comprobar que el nodo secundario asuma el rol maestro en menos de 15 segundos sin pérdida de registros.
3. **Ingeniería del Caos (*Chaos Engineering* / Chaos Monkey):** En ambientes de pruebas pre-producción, se inyectan fallas aleatorias (muerte de contenedores Docker, latencia inducida en la red con `tc`, saturación artificial de CPU) para comprobar que la arquitectura se autorrecupere (*self-healing*) de manera resiliente.

---

## 5. CASO PRÁCTICO: ARQUITECTURA DE ALTA DISPONIBILIDAD PARA LA PIZZERÍA BELLA ITALIA

Para el despliegue del sistema de información de la *Pizzería Gourmet Bella Italia Popayán*, se diseñó e implementó una arquitectura distribuida de cinco capas concéntricas de redundancia:

### 5.1. Capa 1: Redundancia WAN (Conectividad Exterior Dual)
El restaurante cuenta con dos acometidas de red independientes conectadas a un router perimetral con balanceo y conmutación automática (*Multi-WAN Failover*):
- **Canal Primario:** Fibra óptica simétrica FTTH de 300 Mbps con IP pública estática provista por el operador principal.
- **Canal Secundario (Backup):** Enlace inalámbrico de alta velocidad mediante módem celular 4G LTE corporativo (o terminal satelital Starlink).
- *Comportamiento:* El router envía sondeos ICMP continuos (*ping*) a servidores DNS públicos (1.1.1.1 y 8.8.8.8). Si el canal de fibra óptica falla, el router conmuta el 100% del tráfico al enlace celular en **menos de 8 segundos**, actualizando de forma automática el registro DNS dinámico del dominio a través de la API de Cloudflare.

### 5.2. Capa 2: Proxy Inverso y Balanceo de Carga HA (Nginx + Keepalived)
Para garantizar que la entrada a los microservicios no dependa de un único servidor web:
- Se implementan dos nodos de proxy inverso **Nginx** (Proxy A y Proxy B) gobernados por el demonio **Keepalived** mediante el protocolo **VRRP (Virtual Router Redundancy Protocol)**.
- Ambos nodos comparten una **Dirección IP Virtual (VIP: 192.168.10.100)**.
- En condiciones normales, el Proxy A gestiona la VIP y balancea el tráfico HTTPS (TLS 1.3 con Let's Encrypt) entre las instancias de backend. Si el Proxy A experimenta un fallo de kernel o hardware, el Proxy B toma posesión de la VIP en **menos de 1 segundo**, de forma transparente para los clientes web y móviles.

### 5.3. Capa 3: Clúster de Microservicios Backend (Docker Swarm / Spring Boot)
- La API REST desarrollada en Java Spring Boot 3.x se empaqueta en imágenes de contenedor Docker y se despliega en un clúster ligero con **mínimo 2 réplicas activas simultáneas**.
- La aplicación fue diseñada bajo el principio de **cero estado (*Stateless Architecture*)**: no almacena información de sesiones en la memoria del servidor local, sino que valida criptográficamente cada petición mediante tokens **JSON Web Tokens (JWT)** firmados con algoritmo HMAC-SHA256.
- El balanceador Nginx consulta continuamente el endpoint `/actuator/health` de cada contenedor. Si un contenedor se bloquea o arroja excepciones no controladas, es retirado del balanceador en 2 segundos mientras Docker Swarm crea un reemplazo sano automáticamente.

### 5.4. Capa 4: Clúster de Base de Datos Transaccional (PostgreSQL HA)
La base de datos relacional PostgreSQL 16 implementa un clúster activo-pasivo con **Replicación Física Streaming**:
- **Nodo Primario (Master - 192.168.10.20):** Atiende el 100% de las operaciones de lectura y escritura de órdenes, facturas e inventario, transmitiendo continuamente sus registros de transacciones WAL por la red local hacia el nodo secundario.
- **Nodo Secundario (Standby Replica - 192.168.10.21):** Aplica continuamente los registros WAL manteniéndose sincronizado al milisegundo en modo de solo lectura (*Hot Standby*).
- **Gestión de Failover con Patroni y etcd:** El orquestador *Patroni* supervisa la salud del motor primario. Si el primario no responde, el clúster alcanza cuórum a través del almacén distribuido *etcd* y promueve al nodo secundario a nuevo maestro en **menos de 15 segundos**, reconfigurando el pool de conexiones **PgBouncer** para redirigir las escrituras sin necesidad de reiniciar la API.

### 5.5. Capa 5: Estrategia de Respaldo y DRP bajo la Regla 3-2-1
Para blindar el patrimonio de datos de la empresa contra desastres físicos mayores (incendios, terremotos) o ataques cibernéticos de *ransomware*, se implementó la **Regla de Oro 3-2-1**:

```
                       ESTRATEGIA DE RESPALDO Y DRP 3-2-1
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ 3 COPIAS DE LOS DATOS:                                                                 │
│   1. Copia Activa: Base de Datos en Producción (SSD NVMe Servidor Primario).           │
│   2. Copia Local: Respaldos diarios y WALs en NAS local de almacenamiento secundario.  │
│   3. Copia Remota: Repositorio inmutable en Cloud Object Storage (AWS S3 / Wasabi).    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 2 MEDIOS DE ALMACENAMIENTO DIFERENTES:                                                 │
│   • Medio 1: Almacenamiento local en disco de estado sólido de alta velocidad.         │
│   • Medio 2: Almacenamiento en la nube con tecnología Object Storage distribuido.      │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1 COPIA FUERA DE SITIO (OFFSITE):                                                      │
│   • Almacenada en un centro de datos geográficamente distante (Bogotá / EE.UU.),       │
│     cifrada en reposo con algoritmo AES-256 e inmutable mediante Object Lock.           │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

- **Herramienta de Automatización:** Se implementó `pgBackRest` ejecutado como servicio *systemd timer*.
- **Backups Lógicos Completos:** Exportación diaria mediante `pg_dump` programada a las 02:00 AM en formato comprimido `.sql.gz`.
- **Archivado Continuo de WAL:** Cada archivo WAL de 16 MB cerrado se comprime, se cifra y se sincroniza inmediatamente con el bucket remoto S3, garantizando que el punto de recuperación (*RPO*) sea prácticamente nulo ante cualquier eventualidad.

---

### 5.6. Matriz de Verificación Técnica Previa al Despliegue (Checklist IE-GA10-220501097-AA4-EV01)

| CRITERIO DE EVALUACIÓN | ESPECIFICACIÓN TÉCNICA VERIFICADA | ESTADO | RESULTADO Y EVIDENCIA |
| :--- | :--- | :---: | :--- |
| **Configuración de Servicios según Requerimientos** | Despliegue de Nginx Reverse Proxy, Keepalived VRRP, Docker Swarm y PostgreSQL 16 Streaming. | **CONFORME** | Clúster activo con VIP 192.168.10.100 y healthcheck continuo a microservicios. |
| **Generación de Copias de Respaldo según Plan** | Implementación de la política 3-2-1 con copias lógicas y archivado WAL continuo hacia S3. | **CONFORME** | Backups diarios verificados con `pgBackRest` y restauración simulada exitosa. |
| **Conmutación Automática por Error (Failover)** | Prueba de failover del proxy inverso Nginx y promoción de réplica PostgreSQL en caliente. | **CONFORME** | Tiempo de conmutación Nginx < 1 seg; promoción de base de datos < 15 seg. |
| **Métricas de Resiliencia RPO y RTO Validadas** | Cumplimiento estricto de las metas operativas fijadas en el Análisis de Impacto (BIA). | **CONFORME** | RPO medido: 3 minutos; RTO medido: 1.5 minutos (ambos conformes con la meta). |
| **Seguridad de Respaldos contra Ransomware** | Cifrado en reposo AES-256 y política de inmutabilidad (WORM - Write Once, Read Many). | **CONFORME** | Bucket de respaldo configurado con retención bloqueada por 30 días inmodificables. |

---

## 6. CONCLUSIONES

1. **La Alta Disponibilidad es un Imperativo Arquitectónico Integral:** La resiliencia de un sistema de información no se logra mediante un único componente redundante; requiere una estrategia holística y concatenada que elimine puntos únicos de falla en todos los niveles del stack: conectividad WAN dual, balanceo de entrada con IP virtual compartida, microservicios stateless orquestados en contenedores y replicación síncrona de bases de datos.
2. **Las Tecnologías de Código Abierto Democratizan la Resiliencia Empresarial:** Mediante herramientas libres y probadas en la industria como *Nginx*, *Keepalived*, *Docker Swarm*, *PostgreSQL Streaming Replication* y *pgBackRest*, es viable implementar arquitecturas de alta disponibilidad con niveles de servicio corporativos (99.9% de uptime) para microempresas y restaurantes como la *Pizzería Gourmet Bella Italia*, sin incurrir en licenciamientos privativos millonarios.
3. **El Valor Crítico del BIA y la Cuantificación de RPO/RTO:** Definir formalmente las métricas RPO (<5 min) y RTO (<2 min) fundamentadas en las pérdidas financieras directas ($350.000 COP/hora) proporciona el sustento técnico y gerencial para priorizar inversiones tecnológicas, garantizando que los módulos críticos de cobro y pedidos permanezcan operativos frente a contingencias.
4. **La Regla 3-2-1 como Blindaje Definitivo del Patrimonio de Datos:** Los respaldos locales son indispensables para recuperaciones rápidas, pero insuficientes ante siniestros físicos o ciberataques. Mantener una tercera copia inmutable, cifrada y alojada fuera del sitio en la nube garantiza que, incluso ante la destrucción total de las instalaciones físicas en Popayán, la pizzería pueda restaurar su sistema en un centro de datos alterno en cuestión de minutos.

---

## 7. REFERENCIAS BIBLIOGRÁFICAS (Norma APA 7ma Edición)

- Amazon Web Services. (2023). *Reliability pillar: AWS Well-Architected Framework*. AWS Whitepapers. https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/
- Brewer, E. (2012). Push the boundaries of CAP: A retrospective on the "Theorem". *Computer*, 45(2), 23-29. https://doi.org/10.1109/MC.2012.37
- Buyya, R. (1999). *High performance cluster computing: Architectures and systems* (Vol. 1). Prentice Hall PTR.
- Fowler, M. (2019). *Patterns of distributed systems*. martinfowler.com. https://martinfowler.com/articles/patterns-of-distributed-systems/
- International Organization for Standardization. (2019). *Security and resilience - Business continuity management systems - Requirements (ISO 22301:2019)*. ISO.
- Nginx Inc. (2024). *High-availability load balancing with NGINX and Keepalived*. F5 NGINX Documentation. https://docs.nginx.com/nginx/admin-guide/high-availability/
- PostgreSQL Global Development Group. (2024). *PostgreSQL 16.2 Documentation: Chapter 27. High availability, load balancing, and replication*. PostgreSQL.org. https://www.postgresql.org/docs/16/high-availability.html
- Snedaker, S., & Rima, C. (2014). *Business continuity and disaster recovery planning for IT professionals* (2nd ed.). Syngress / Elsevier.
- Servicio Nacional de Aprendizaje - SENA. (2024). *Componente formativo: Gestión de redundancia y alta disponibilidad*. Dirección de Formación Profesional. Bogotá: SENA.
- Tanenbaum, A. S., & Van Steen, M. (2017). *Distributed systems: Principles and paradigms* (3rd ed.). CreateSpace Independent Publishing.
- Zaltsman, L. (2023). *pgBackRest: Reliable PostgreSQL backup & restore*. pgBackRest User Guide. https://pgbackrest.org/user-guide.html
