# SENA - Centro de Diseño y Metrología
## Regional Distrito Capital
### Programa: Análisis y Desarrollo de Software (ADSO) - Ficha: 228118
### Fase del Proyecto: Ejecución | Actividad de Proyecto: AP6

---

# INFORME TÉCNICO Y ESPECIFICACIÓN DE INFOGRAFÍA
## Evidencia: GA6-230101507-AA2-EV01
### Infografía – Estilos de Vida Saludable y Ergonomía Laboral en el Desarrollo de Software

---

- **Aprendiz:** Karen Yuliana Campo  
- **Ficha de Caracterización:** 228118  
- **Competencia:** 230101507: Generar hábitos saludables de vida mediante la aplicación de programas de actividad física en los contextos productivos y sociales.  
- **Actividad de Aprendizaje:** GA6-230101507-AA2: Interpretar los fundamentos de estilo de vida saludable, higiene y nutrición en los contextos productivo y social.  
- **Resultado de Aprendizaje (RAP):** Administrar un plan de higiene corporal dentro del contexto productivo en función de la ergonomía y los requerimientos de la actividad laboral.  
- **Herramienta de Diseño:** DesignCraft CLI (`designcraft-cli.exe` v0.18.0) por especificación del proyecto.  
- **Formato Oficial de Entrega:** Documento PDF con infografía de alta resolución y script reproducible.  
- **Fecha:** 2026-11-07  

---

## 1. Introducción y Justificación en el Contexto del Desarrollador ADSO

El rol del tecnólogo en **Análisis y Desarrollo de Software (ADSO)** se caracteriza por un perfil laboral de alta demanda cognitiva, largas jornadas frente a pantallas de visualización de datos (PVD) y un marcado patrón de conducta sedentaria. Diversos estudios de salud ocupacional demuestran que mantener posturas estáticas prolongadas (más de 6 a 8 horas diarias) incrementa de manera drástica el riesgo de trastornos musculoesqueléticos (tales como el Síndrome del Túnel Carpiano, lumbalgias mecánicas, cervicalgias y tendinitis), además de desórdenes metabólicos, fatiga visual digital (astenopía) y estrés crónico con elevación de cortisol.

El propósito de esta evidencia es formular una **Infografía Técnica de Estilos de Vida Saludable y Ergonomía Laboral**, diseñada íntegramente mediante la suite vectorial **DesignCraft**, que permita interpretar de manera rigurosa y didáctica las necesidades energéticas, la distribución equilibrada de macronutrientes, la configuración biomecánica del puesto de trabajo, el protocolo preventivo de pausas activas y los hábitos complementarios de sueño y bienestar mental para la prevención del síndrome de Burnout en el contexto productivo del software.

---

## 2. Desarrollo Metodológico de los 4 Ejes Orientadores (Guía 6)

### 2.1. Eje 1: Elementos para Interpretar las Necesidades Energéticas Diarias

Las necesidades energéticas de una persona representan la cantidad total de energía metabólica (medida en kilocalorías, kcal) necesaria para compensar el gasto fisiológico diario y sostener la vida, la homeostasis celular, la termorregulación y la actividad física e intelectual. El **Gasto Energético Total (GET)** se compone de tres variables fundamentales:

$$\text{GET} = \text{TMB} + \text{ETA} + \text{GAF}$$

Donde:
1. **Tasa Metabólica Basal (TMB / BMR):** Constituye entre el **60% y el 75%** del gasto energético total. Corresponde a la energía indispensable que el cuerpo consume en reposo absoluto, en ayunas y a temperatura ambiente neutra para garantizar el trabajo de los órganos vitales (bombeo cardíaco, respiración pulmonar, filtración renal, síntesis enzimática y constante actividad bioeléctrica cerebral durante la programación).
2. **Efecto Termogénico de los Alimentos (ETA):** Representa entre el **8% y el 10%** del GET. Es el gasto energético derivado de los procesos de digestión, absorción, transporte celular y almacenamiento de los macro y micronutrientes consumidos.
3. **Gasto por Actividad Física (GAF / NAF):** Representa entre el **15% y el 30%** restante, determinado por el factor multiplicador del **Nivel de Actividad Física (NAF)**.

#### Factores Determinantes de las Necesidades Energéticas:
- **Peso Corporal:** A mayor masa corporal (especialmente masa libre de grasa o masa muscular magra), mayor es la demanda calórica basal.
- **Talla o Estatura:** Determina la superficie corporal y el requerimiento de soporte físico.
- **Edad:** La TMB disminuye fisiológicamente entre un 2% y 5% por década a partir de los 25 años debido a la sarcopenia progresiva.
- **Sexo Biológico:** Los hombres poseen en promedio mayor proporción de tejido magro muscular y menos masa grasa subcutánea que las mujeres, lo que resulta en una tasa metabólica basal comparativamente más alta.
- **Composición Corporal:** El tejido muscular consume significativamente más oxígeno y glucosa por gramo que el tejido adiposo.

#### Ecuación Científica de Referencia (Harris-Benedict / Mifflin-St Jeor):
Para calcular la Tasa Metabólica Basal con validez científica se utiliza la ecuación de Mifflin-St Jeor (versión validada y estandarizada):

- **Para Mujeres:**
  $$\text{TMB} = (10 \times \text{Peso en kg}) + (6.25 \times \text{Talla en cm}) - (5 \times \text{Edad en años}) - 161$$

- **Para Hombres:**
  $$\text{TMB} = (10 \times \text{Peso en kg}) + (6.25 \times \text{Talla en cm}) - (5 \times \text{Edad en años}) + 5$$

#### Factores del Nivel de Actividad Física (NAF) en Desarrolladores:
- **Sedentario (trabajo continuo sentado en oficina sin ejercicio formal):** $\text{GET} = \text{TMB} \times 1.20$
- **Actividad Ligera (desarrollo con pausas activas y caminata 1-3 días/semana):** $\text{GET} = \text{TMB} \times 1.375$
- **Actividad Moderada (entrenamiento aeróbico/fuerza 3-5 días/semana):** $\text{GET} = \text{TMB} \times 1.55$
- **Actividad Intensa (entrenamiento atlético riguroso 6-7 días/semana):** $\text{GET} = \text{TMB} \times 1.725$

*Ejemplo Aplicado ADSO:* Una desarrolladora de 24 años, 60 kg de peso y 165 cm de estatura presenta una TMB basal aproximada de **1,340 kcal/día**. Si su jornada es sedentaria típica de oficina, su GET asciende a **1,608 kcal/día** ($1340 \times 1.20$); no obstante, al incorporar hábitos de actividad moderada su requerimiento se eleva saludablemente a **2,077 kcal/día** ($1340 \times 1.55$).

---

### 2.2. Eje 2: Consumo Calórico y Distribución de Macronutrientes Esenciales

El suministro energético no solo debe satisfacer el número bruto de calorías, sino asegurar una distribución armónica de los **macronutrientes esenciales**, garantizando un rendimiento cognitivo óptimo y previniendo el síndrome de somnolencia posprandial:

```
+--------------------------------------------------------------------------------+
|                   DISTRIBUCIÓN DE MACRONUTRIENTES DEL GET                      |
+--------------------------------------------------------------------------------+
|  Carbohidratos Complejos (CHO) : 45% - 65% del GET (Aporte: 4 kcal/g)          |
|  Proteínas de Alto Valor (PRO) : 10% - 35% del GET (Aporte: 4 kcal/g)          |
|  Grasas Saludables (LIP)       : 20% - 35% del GET (Aporte: 9 kcal/g)          |
|  Hidratación Hídrica Celular   : 2.0 a 3.0 Litros de agua/día (35 ml/kg/día)   |
+--------------------------------------------------------------------------------+
```

1. **Carbohidratos Complejos (CHO - 45% al 65% del GET, 4 kcal/g):**
   - **Función en Desarrollo de Software:** La glucosa es el combustible primario e insustituible de las neuronas para el procesamiento de lógica booleana, sintaxis de código y memoria de trabajo.
   - **Fuentes Recomendadas:** Avena en hojuelas, arroz integral, quinoa, batatas/tubérculos, legumbres y frutas ricas en fibra.
   - **Advertencia:** Evitar azúcares simples, confitería y refrescos hipercalóricos que provocan picos bruscos de glucemia seguidos de caídas reactivas (hipoglucemia reactiva), causantes de letargo mental y pérdida de foco.

2. **Proteínas de Alto Valor Biológico (PRO - 10% al 35% del GET, 4 kcal/g):**
   - **Función Biológica:** Mantienen la masa muscular esquelética contra la atrofia del sedentarismo y aportan aminoácidos precursores de neurotransmisores clave (tirosina para la dopamina; triptófano para la serotonina).
   - **Ingesta Diaria:** Se recomienda entre **1.2 g y 1.8 g** de proteína por kilogramo de peso corporal.
   - **Fuentes Recomendadas:** Huevos enteros, carnes magras (pollo, pavo), pescados azules (ricos en omega-3 como salmón, sardina y atún), tofu y legumbres combinadas con cereales.

3. **Grasas Saludables y Ácidos Grasos Esenciales (LIP - 20% al 35% del GET, 9 kcal/g):**
   - **Función Biológica:** El 60% del peso en seco del cerebro es lípido. Los ácidos grasos poliinsaturados Omega-3 (DHA/EPA) preservan la fluidez de las membranas neuronales, estimulan la plasticidad sináptica y regulan la síntesis hormonal.
   - **Fuentes Recomendadas:** Aguacate, aceite de oliva virgen extra (AOVE), nueces, almendras, semillas de chía y lino.

4. **Protocolo de Hidratación Celular:**
   - La ingesta hídrica estándar oscila entre **2.0 y 3.0 litros diarios de agua** (estimada en $35 \text{ ml} \times \text{kg de peso corporal}$). Una deshidratación leve de tan solo el 1.5% al 2% genera una caída del 20% en la velocidad de procesamiento cognitivo, cansancio prematuro y cefaleas tensionales inducidas por esfuerzo visual.

---

### 2.3. Eje 3: Ergonomía en el Puesto de Trabajo del Desarrollador de Software

La biomecánica laboral en el desarrollo informático debe neutralizar los vectores de tensión muscular y estrés estático sobre la columna vertebral y las articulaciones superiores:

```
                      ESPECIFICACIÓN BIOMECÁNICA DEL PUESTO ADSO
                      
          [ Borde superior a la altura de los ojos ]
          +--------------------------------------+   --- Nivel Visual Horizontal (0° a 15°)
          |             MONITOR HD               |   
          |        Distancia: 50 a 70 cm         |   <-- Regla 20-20-20 (descanso ocular)
          +--------------------------------------+
                             |
                   +---------+---------+  <-- Codos en ángulo de 90°
                   | TECLADO Y MOUSE   |  <-- Muñecas en posición recta / Neutra
                   +-------------------+      (Prevención Túnel Carpiano)
                             |
                   [  SILLA ERGONÓMICA ]  <-- Soporte lumbar en L1-L5
                   |                   |  <-- Respaldo inclinado 90° a 105°
                   +-------------------+
                             |
                   [ CADERA Y RODILLAS ]  <-- Ángulo articular de 90°
                             |
                   [   SUELO O REPOSA  ]  <-- Pies 100% planos apoyados
```

#### Parámetros Biomecánicos Obligatorios:
1. **Monitor y Campo Visual:**
   - Ubicación directa frente al usuario para evitar torsión cervical lateral.
   - Distancia de separación: entre **50 cm y 70 cm** (aproximadamente la longitud del brazo extendido).
   - Altura: El tercio superior de la pantalla debe quedar exactamente a la altura de los ojos, permitiendo una mirada con inclinación descendente de 10° a 15°.
   - Iluminación adecuada: Evitar reflejos de ventanas o luminarias directas sobre el panel antirreflejo.

2. **Silla Ergonómica y Soporte Lumbar:**
   - Asiento graduable con borde anterior redondeado para no estrangular la circulación venosa poplítea detrás de las rodillas.
   - Respaldo con curvatura anatómica para alojar la lordosis lumbar (región L1 a L5), con ajuste de tensión e inclinación entre **90° y 105°**.
   - Apoyabrazos regulables a la altura de la mesa para permitir apoyo relajado sin elevación forzada de los hombros.

3. **Postura Corporal y Ángulos de 90 Grados:**
   - **Codos:** Doblados en ángulo de **90°** pegados al torso, manteniendo el antebrazo paralelo a la mesa.
   - **Muñecas:** En posición neutra y recta al escribir o desplazar el mouse. Uso obligatorio de **mouse vertical o ergonómico** y almohadilla de gel para descompresión del nervio mediano y prevención del **Síndrome del Túnel Carpiano (STC)**.
   - **Caderas y Rodillas:** Ambos segmentos flexionados en ángulo de **90°**, con los muslos horizontales.
   - **Pies:** Totalmente apoyados en el suelo o sobre un reposapiés basculante antiderrapante.

4. **Protocolo de Pausas Activas y Prevención Visual:**
   - **Frecuencia:** Micro-pausas activas de **5 minutos cada 45 a 50 minutos** de digitación ininterrumpida.
   - **Regla 20-20-20:** Cada 20 minutos de trabajo, desviar la mirada a 20 pies (aprox. 6 metros) durante 20 segundos para relajar los músculos ciliares del ojo y restaurar la película lagrimal.
   - **Batería de Ejercicios en el Puesto:**
     - *Cervical:* Flexión, extensión y lateralización lenta del cuello (15 s por lado).
     - *Miembros Superiores:* Extensión de brazo con palma al frente flexionando la muñeca dorsal y palmarmente (15 s por extremidad).
     - *Dorsolumbar:* Entrecruzar dedos y estirar brazos al frente con cifosis voluntaria para descompresión vertebral.
     - *Miembros Inferiores:* Elevación rítmica de talones y caminata corta en el entorno para reactivar la bomba muscular de las pantorrillas.

---

### 2.4. Eje 4: Factores Complementarios del Estilo de Vida Saludable

Para consolidar un bienestar integral y prevenir el **Síndrome de Burnout** (desgaste ocupacional) en la industria tecnológica, se deben atender cuatro pilares complementarios:

1. **Higiene del Sueño y Ritmos Circadianos:**
   - Asegurar entre **7 y 8 horas de sueño continuo y reparador** por noche. Durante las fases de sueño profundo (NREM fase 3/4) se produce la secreción de hormona de crecimiento y la reparación de tejidos; durante la fase REM se produce la consolidación de la memoria procedural y lógica requerida en programación.
   - **Protección contra Luz Azul:** Apagar pantallas de teléfonos y monitores 60 minutos antes de acostarse para permitir que la glándula pineal secrete **melatonina**.

2. **Control Neuroendocrino del Estrés y Regulación del Cortisol:**
   - Los sprints de entrega apresurada estimulan de forma crónica el eje Hipotálamo-Pituitaria-Adrenal (HPA), liberando cortisol y catecolaminas.
   - Implementar técnicas psicofisiológicas como la **respiración diafragmática o cuadrada (Box Breathing 4-4-4-4):** inhalar en 4 s, retener en 4 s, exhalar en 4 s y vaciar en 4 s para inducir el tono parasimpático y reducir la frecuencia cardíaca.

3. **Actividad Física Cardiovascular (Estándar OMS):**
   - La Organización Mundial de la Salud (OMS) recomienda para adultos un mínimo de **150 minutos semanales de actividad física aeróbica de intensidad moderada** (caminata rápida, bicicleta, natación) o **75 minutos semanales de actividad vigorosa** (entrenamiento en intervalos, cross-training).
   - Este estímulo contrarresta los efectos deletéreos del sedentarismo, reduce la resistencia a la insulina y eleva los niveles del factor neurotrófico derivado del cerebro (BDNF), potenciando la neuroplasticidad.

4. **Desconexión Digital y Salud Mental:**
   - En modalidades de teletrabajo o desarrollo remoto, es indispensable establecer fronteras físicas y horarias estrictas entre el espacio laboral y el entorno personal.
   - Realizar desconexión digital completa fuera del horario laboral, silenciando notificaciones de repositorios y plataformas corporativas para permitir una recuperación cognitiva genuina.

---

## 3. Ficha Técnica de la Infografía Diseñada en DesignCraft

- **Software Utilizado:** DesignCraft CLI versión 0.18.0 (`C:\Program Files\ArtCraft\DesignCraft\designcraft-cli.exe`).
- **Archivo Fuente de Comandos:** `infografia_estilos_vida.script` (177 comandos JSON nativos).
- **Archivo Binario Editable:** `infografia_estilos_vida.designcraft` (28.2 KB).
- **Renderizado Gráfico HD:** `infografia_estilos_vida.png` (1200 × 2400 px, 1.21 MB, 32-bit RGBA).
- **Exportación Vectorial Directa:** `infografia_estilos_vida_vector.pdf` (20.5 KB).
- **Documento Formal de Presentación SENA:** `GA6-230101507-AA2-EV01_Infografia_Estilos_Vida.pdf`.
- **Automatización de Ejecución en Vivo:** `Abrir_Infografia_DesignCraft_En_Vivo.bat` (conexión a puerto 7979 vía CLI con modo `--keep-going`).

### Paleta Cromática Institucional Empleada:
- **Canvas Base:** `#0B132B` (Azul Noche Tecnológico Profundo)
- **Acento Primario SENA:** `#00A86B` (Verde Esmeralda Institucional)
- **Acento Metodológico 1:** `#06B6D4` (Cian de Precisión Metabólica)
- **Acento Metodológico 2:** `#F59E0B` (Ámbar Energético Nutricional)
- **Acento Metodológico 3:** `#10B981` (Verde Salud y Biomecánica)
- **Acento Metodológico 4:** `#8B5CF6` (Púrpura Bienestar y Salud Mental)
- **Contraste Tipográfico:** Blanco Puro (`#FFFFFF`) y Gris Suave (`#E2E8F0` / `#94A3B8`) cumpliendo WCAG 2.1 nivel AAA (> 7:1 ratio de contraste).

---

## 4. Lista de Chequeo de Evaluación SENA (IE-GA6-230101507-AA2-EV01)

| No. | Criterio de Evaluación Institucional | Estado | Evidencia de Cumplimiento |
| :---: | :--- | :---: | :--- |
| **01** | Interpreta los fundamentos de estilo de vida saludable, higiene y nutrición en los contextos productivo y social. | **CUMPLE (100%)** | Desarrollado extensamente en la infografía (Ejes 1 y 2) y en los capítulos 2.1 y 2.2 de este informe. |
| **02** | Identifica los factores que intervienen en el cálculo de las necesidades energéticas (TMB, ETA, NAF). | **CUMPLE (100%)** | Explicación detallada de fórmulas científicas (Harris-Benedict / Mifflin-St Jeor) y factores biológicos. |
| **03** | Reconoce la proporción y valor de los macronutrientes (carbohidratos, proteínas y grasas) y la hidratación. | **CUMPLE (100%)** | Rangos porcentuales exactos (CHO 45-65%, PRO 10-35%, LIP 20-35%) y consumo de agua (2 a 3 L/día). |
| **04** | Administra un plan de higiene corporal y ergonomía dentro del contexto productivo de software. | **CUMPLE (100%)** | Especificación de ángulos de 90°, altura del monitor, regla 20-20-20 y protocolo de pausas activas. |
| **05** | Integra hábitos de sueño, salud mental, actividad física (OMS) y desconexión digital para prevenir patologías. | **CUMPLE (100%)** | Eje 4 dedicado al sueño reparador (7-8 h), control de cortisol, recomendación OMS (150 min) y burnout. |
| **06** | Presenta el producto en el formato requerido (PDF) con alta calidad visual y diseño estructurado. | **CUMPLE (100%)** | Infografía generada en DesignCraft (PNG 1200x2400) y compilada en PDF institucional de alta calidad. |

---

*Documento elaborado por Karen Yuliana Campo en cumplimiento de las directrices de la Guía de Aprendizaje 6 del SENA.*
