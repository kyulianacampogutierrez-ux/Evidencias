# SENA - Centro de Diseño y Metrología
## Regional Distrito Capital
### Programa: Análisis y Desarrollo de Software (ADSO) - Ficha: 228118
### Fase del Proyecto: Ejecución | Actividad de Proyecto: AP6

---

# INFORME TÉCNICO Y ESPECIFICACIÓN DE FOLLETO EDITORIAL
## Evidencia: GA6-230101507-AA4-EV01
### Folleto de Lesiones Más Comunes en el Trabajo y la Importancia de las Pausas Activas

---

- **Aprendiz:** Karen Yuliana Campo  
- **Ficha de Caracterización:** 228118  
- **Competencia:** 230101507: Generar hábitos saludables de vida mediante la aplicación de programas de actividad física en los contextos productivos y sociales.  
- **Actividad de Aprendizaje:** GA6-230101507-AA4: Identificar la higiene postural y pausas activas correctas en el desempeño del área ocupacional, de acuerdo con la naturaleza de la función productiva.  
- **Resultado de Aprendizaje (RAP):** 230101507-04: Implementar un plan de ergonomía y pausas activas según las características de la función productiva.  
- **Herramienta de Diseño:** DesignCraft CLI (`designcraft-cli.exe` v0.18.0) por requerimiento explícito del proyecto.  
- **Formato Oficial de Entrega:** Documento PDF con folleto tríptico completo de alta resolución.  
- **Fecha:** 2026-11-07  

---

## 1. Introducción y Justificación Ocupacional en el Rol de Desarrollo de Software

El trabajo del tecnólogo en **Análisis y Desarrollo de Software (ADSO)** implica una exposición diaria continua a movimientos repetitivos de miembros superiores (digitación a alta velocidad y manejo de mouse), fijación estática de la mirada sobre pantallas de visualización de datos (PVD) y posturas sedentes prolongadas (entre 8 y 10 horas diarias). Según estadísticas de salud ocupacional de la OIT y el Ministerio de Salud, más del 70% de los trabajadores de tecnologías de la información sufren desórdenes musculoesqueléticos acumulativos (DME) durante su trayectoria profesional.

El objetivo de esta evidencia es construir un **Folleto Tríptico Editorial de Prevención y Salud Ocupacional**, programado y maquetado íntegramente en la herramienta vectorial **DesignCraft**, que identifique con claridad las 5 lesiones laborales más comunes derivadas del trabajo repetitivo, su sintomatología, y formule un protocolo estructurado de **Pausas Activas Laborales** y pautas de higiene postural para blindar la salud del desarrollador.

### 🎨 Estándar de Diseño Visual y Recursos Gráficos
- **Fondo Claro y Luminoso:** Canvas `#F8FAFC`, tarjetas en `#FFFFFF` puro con bordes sutiles. Cero fondos oscuros o barras densas que oscurezcan el contenido.
- **Ilustraciones Anatómicas Vectoriales Dedicadas:**
  - 🖐️ **Túnel Carpiano:** Diagrama anatómico de mano con trayecto del nervio mediano y zona de compresión.
  - 🦴 **Cervicalgia / Text Neck:** Comparativa de tensión cervical a 0° (5 kg) vs flexión a 60° (27 kg de sobrecarga).
  - 🪑 **Lumbalgia Postural:** Diagrama biomecánico de columna con apoyo en lordosis L1-L5.
  - 🎾 **Epicondilitis:** Diagrama del tendón extensor en el codo y comparativa con mouse vertical a 57°.
  - 👁️ **Fatiga Visual:** Diagrama de descanso ocular con la regla 20-20-20.
  - 🧘 **Batería de 6 Pausas (Grilla 2x3):** 6 ilustraciones dedicadas para cada estiramiento (cuello, muñecas, tronco, apertura pectoral, retorno venoso y descanso visual).
  - 🖥️ **Puesto Ergonómico:** Infografía completa del desarrollador con todos los ángulos a 90°.
  - 👩‍💻 **Hero Portada:** Desarrolladora activa, saludable y sonriente con insignias de bienestar.


---

## 2. Estructura Editorial del Folleto Tríptico (6 Paneles Informativos)

El folleto se diseñó bajo el formato editorial estándar de tríptico horizontal desplegable en dos caras (exterior e interior) en alta resolución (1800 × 1000 píxeles por cara, compuestas por 475 comandos vectoriales nativos):

```
+----------------------------------------------------------------------------------------------------+
|                                    CARA EXTERIOR DEL FOLLETO                                       |
+-----------------------------------+--------------------------------+-------------------------------+
|  PANEL 1 (Solapa Interior)        |  PANEL 2 (Contraportada)       |  PANEL 3 (Portada Principal)  |
|  • Factores de Riesgo en IT       |  • Decálogo de Autocuidado     |  • Gran Título Institucional  |
|  • 8-10 horas de sedentarismo     |  • 10 Mandamientos Ergonómicos |  • Logotipo del SENA          |
|  • Señales de alarma temprana     |  • Datos del Aprendiz y Ficha  |  • Badges de Prevención       |
|  • Importancia de la prevención   |  • Metadatos Institucionales   |  • Karen Yuliana Campo ADSO   |
+-----------------------------------+--------------------------------+-------------------------------+

+----------------------------------------------------------------------------------------------------+
|                                    CARA INTERIOR DEL FOLLETO                                       |
+-----------------------------------+--------------------------------+-------------------------------+
|  PANEL 4 (Lesiones Ocupacionales) |  PANEL 5 (Pausas Activas)      |  PANEL 6 (Checklist Puesto)   |
|  • 1. Síndrome Túnel Carpiano     |  • Regla de Oro: 5 min / 45m   |  • Distancia Monitor (50-70cm)|
|  • 2. Cervicalgia / Text Neck     |  • E1: Cuello y Cervical (15s) |  • Ángulo Codos 90°           |
|  • 3. Lumbalgia Mecánica (L1-L5)  |  • E2: Flexores Muñeca (15s)   |  • Respaldo Lumbar (90°-105°) |
|  • 4. Epicondilitis (Codo Mouse)  |  • E3: Rotación Tronco (15s)   |  • Ángulo Rodillas / Pies 90° |
|  • 5. Astenopía / Fatiga Visual   |  • E4: Apertura Pectoral (20s) |  • Mouse Vertical & Gel Pad   |
|                                   |  • E5: Piernas y Gemelos (15r) |  • Checklist de Seguridad     |
|                                   |  • E6: Regla 20-20-20 Ocular   |                               |
+-----------------------------------+--------------------------------+-------------------------------+
```

---

## 3. Las 5 Lesiones Laborales Más Comunes en Desarrollo de Software

### 3.1. Síndrome del Túnel Carpiano (STC)
- **Causa Biomecánica:** Compresión sostenida del nervio mediano a su paso por el retináculo flexor en la muñeca, provocada por el apoyo continuo de la muñeca contra el borde de la mesa y la flexión/extensión forzada al escribir o usar el mouse.
- **Sintomatología:** Adormecimiento, parestesia (hormigueo) y dolor nocturno en los dedos pulgar, índice, medio y mitad del anular, con disminución progresiva de la fuerza de prensión.
- **Acciones Preventivas:** Uso de mouse vertical ergonómico (evita la pronación forzada del antebrazo), pad con soporte de gel y estiramientos activos de flexores palmares.

### 3.2. Cervicalgia Tensional y Síndrome de Cuello Adelantado (Text Neck)
- **Causa Biomecánica:** Mantener la cabeza inclinada hacia adelante para enfocar líneas de código en pantallas bajas o portátiles sin soporte. En posición neutra (0°), la cabeza de un adulto pesa aprox. 5 kg; sin embargo, con una flexión anterior de 60°, el esfuerzo sobre las vértebras cervicales (C1 a C7) equivale a cargar **27 kg de peso continuo**.
- **Sintomatología:** Contractura dolorosa de músculos trapecios, elevador de la escápula, rigidez articular y cefaleas tensionales occipitales.
- **Acciones Preventivas:** Elevar el monitor de modo que el tercio superior coincida con la línea horizontal de los ojos, manteniendo el cuello neutro.

### 3.3. Lumbalgia Mecánica Postural
- **Causa Biomecánica:** La postura sentada sin apoyo lumbar borra la lordosis fisiológica lumbar, transmitiendo hasta un **140% de incremento en la presión intradiscal sobre los discos L1 a L5**, en comparación con la bipedestación.
- **Sintomatología:** Dolor quemante o punzante en la región inferior de la espalda que se agudiza al ponerse de pie tras periodos prolongados sin cambio de posición.
- **Acciones Preventivas:** Silla ergonómica con soporte lumbar activo y pausas de bipedestación periódica.

### 3.4. Epicondilitis Lateral (Codo de Tenista / Codo de Mouse)
- **Causa Biomecánica:** Microdesgarros e inflamación en el tendón común de los músculos extensores radiales de la muñeca (situado en el epicóndilo lateral del húmero), producido por los clics incesantes y el arrastre repetitivo del mouse tradicional con la muñeca en dorsiflexión estática.
- **Sintomatología:** Dolor agudo al sujetar el mouse, escribir o incluso alzar una taza de café.
- **Acciones Preventivas:** Apoyar la totalidad del antebrazo sobre la superficie de trabajo y memorizar atajos de teclado (*shortcuts*) para disminuir la frecuencia de uso del ratón.

### 3.5. Astenopía o Fatiga Visual Digital
- **Causa Biomecánica:** Al concentrarse en código fuente, la frecuencia de parpadeo espontáneo desciende dramáticamente de **18 a solo 5 parpadeos por minuto**, lo que evapora la película lagrimal y expone la córnea a resequedad.
- **Sintomatología:** Sensación de arena en los ojos, hiperemia conjuntival (ojos rojos), fotofobia, visión borrosa transitoria y dificultad para enfocar de cerca y de lejos.
- **Acciones Preventivas:** Implementación de la **Regla 20-20-20**, uso de filtros de luz azul nocturnos y parpadeo consciente.

---

## 4. Protocolo y Batería de Pausas Activas para Desarrolladores ADSO

Las pausas activas son breves interrupciones de la jornada laboral dedicadas a realizar ejercicios de estiramiento muscular, movilidad articular y compensación biomecánica:

- **Frecuencia Estándar:** Cada **45 a 50 minutos** de digitación ininterrumpida.
- **Duración Cronometrada:** **5 minutos**.
- **Batería de 6 Ejercicios Específicos:**
  1. **E1 - Movilidad Cervical (30 s):** Inclinación lateral suave de la cabeza hacia el hombro derecho e izquierdo (15 s/lado) y flexión anterior hacia el pecho (15 s).
  2. **E2 - Estiramiento de Muñeca y Antebrazo (30 s):** Brazo extendido con palma al frente; con la otra mano traccionar suavemente los dedos hacia atrás (15 s) e invertir hacia abajo (15 s/brazo).
  3. **E3 - Descompresión de Columna y Tronco (30 s):** Sentada con espalda erguida, rotar el torso hacia el lado derecho sujetando el respaldo de la silla (15 s); repetir al lado izquierdo.
  4. **E4 - Retracción Escapular y Apertura Pectoral (20 s):** Entrecruzar los dedos detrás de la espalda baja y llevar los hombros hacia atrás, abriendo el tórax para revertir la postura cifótica.
  5. **E5 - Activación Muscular de Piernas (30 s):** Ponerse de pie y realizar 15 elevaciones de talones para reactivar la bomba neuromuscular de la pantorrilla y favorecer el retorno venoso.
  6. **E6 - Gimnasia Visual (Regla 20-20-20):** Desviar la mirada hacia un punto distante (6 metros) durante 20 segundos y ejecutar 10 parpadeos lentos y profundos.

---

## 5. Higiene Postural y Configuración Ergonómica del Puesto ADSO

```
+----------------------------------------------------------------------------------------------------+
|                            PARÁMETROS BIOMECÁNICOS DEL ESCRITORIO ADSO                             |
+----------------------------------------------------------------------------------------------------+
|  • Monitor a la altura de los ojos : 50 a 70 cm de distancia (longitud del brazo extendido).       |
|  • Ángulo de Codos                 : 90° con antebrazos apoyados y paralelos a la mesa.            |
|  • Ángulo de Rodillas y Caderas    : 90° con muslos horizontales.                                  |
|  • Apoyo Lumbar                    : Respaldo anatómico ajustado a lordosis L1-L5 (90°-105°).      |
|  • Apoyo Plantar                   : Pies 100% planos sobre el suelo o sobre reposapiés.           |
|  • Periféricos Ergonómicos         : Mouse vertical de 57° y pad con descanso de silicona/gel.     |
+----------------------------------------------------------------------------------------------------+
```

---

## 6. Ficha Técnica de Diseño en DesignCraft

- **Software Empleado:** DesignCraft CLI versión 0.18.0 (`C:\Program Files\ArtCraft\DesignCraft\designcraft-cli.exe`).
- **Comandos Totales de Trazado:** 475 comandos vectoriales nativos divididos en:
  - `folleto_cara_exterior.script`: 206 comandos (Cara exterior: Solapa, Contraportada, Portada).
  - `folleto_cara_interior.script`: 269 comandos (Cara interior: 5 Lesiones, 6 Pausas Activas, Ergonomía).
- **Archivos Binarios Editables:**
  - `folleto_lesiones_pausas.designcraft`
  - `folleto_cara_exterior.designcraft`
  - `folleto_cara_interior.designcraft`
- **Renderizados en Alta Resolución HD:**
  - `folleto_cara_exterior.png` (1800 × 1000 px, 1.13 MB).
  - `folleto_cara_interior.png` (1800 × 1000 px, 1.38 MB).
- **Documento Formal Compilado en PDF:** `GA6-230101507-AA4-EV01_Folleto_Pausas_Activas.pdf`.
- **Automatización de Ejecución en Vivo:** `Abrir_Folleto_DesignCraft_En_Vivo.bat` (puerto 7979).

---

## 7. Lista de Chequeo Institucional SENA (IE-GA6-230101507-AA4-EV01)

| No. | Criterio de Evaluación Institucional | Estado | Evidencia de Cumplimiento |
| :---: | :--- | :---: | :--- |
| **01** | Aplica conceptos básicos de ergonomía y pausas activas según la función productiva. | **CUMPLE (100%)** | Puesto de trabajo adaptado a ADSO (monitor, ángulos de 90°, soporte lumbar y mouse vertical). |
| **02** | Discrimina ejercicios específicos para la prevención de riesgos ergonómicos en su labor. | **CUMPLE (100%)** | Batería de 6 pausas activas detalladas paso a paso con frecuencia de 5 min cada 45-50 min. |
| **03** | Identifica las lesiones más comunes producidas por el trabajo repetitivo o posturas inadecuadas. | **CUMPLE (100%)** | Fichas técnicas de STC, Cervicalgia, Lumbalgia, Epicondilitis y Astenopía visual. |
| **04** | Estructura el folleto con criterios editoriales de portada, desarrollo y recomendaciones. | **CUMPLE (100%)** | Folleto tríptico de 6 paneles informativos en 2 caras horizontales de 1800x1000 px. |
| **05** | Presenta el producto en el formato requerido (PDF) con calidad visual y diseño estructurado. | **CUMPLE (100%)** | Diseño elaborado en DesignCraft CLI e integrado en documento formal PDF institucional. |

---

*Documento elaborado por Karen Yuliana Campo en cumplimiento de las directrices de la Guía de Aprendizaje 6 del SENA.*
