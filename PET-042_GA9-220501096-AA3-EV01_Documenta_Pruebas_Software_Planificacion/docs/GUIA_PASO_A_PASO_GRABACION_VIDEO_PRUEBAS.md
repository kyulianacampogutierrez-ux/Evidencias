# GUÍA TÉCNICA PASO A PASO Y GUION DE GRABACIÓN DE VIDEO DEMOSTRATIVO
## Evidencia: GA9-220501096-AA3-EV01 - Documenta pruebas de software, de acuerdo a la planificación

---

### DATOS GENERALES DE LA EVIDENCIA
* **Aprendiz:** Karen Yuliana Campo
* **Ficha de Formación:** 3186681
* **Programa:** Tecnología en Análisis y Desarrollo de Software (ADSO)
* **Centro:** Centro de Teleinformática y Producción Industrial (CTPI) - SENA Regional Cauca
* **Proyecto Formativo:** Pizzería Gourmet Bella Italia Popayán
* **Duración Sugerida del Video:** Entre 3 a 5 minutos (máximo 7 minutos).
* **Formato de Entrega:** Video cargado en YouTube (en modo Oculto o Público) o en Google Drive (con permisos públicos de visualización) y enlace consignado en el informe técnico y en el archivo de texto institucional.

---

## 1. PREPARACIÓN Y CONFIGURACIÓN DEL ENTORNO DE GRABACIÓN

### 1.1 Herramientas Gratuitas Recomendadas para Grabar
1. **OBS Studio (Recomendada para PC/Laptop):**
   * Descarga gratuita desde [obsproject.com](https://obsproject.com/).
   * Configuración: Añadir una fuente de **Captura de Pantalla** y verificar que la entrada de audio del micrófono marque niveles verdes y amarillos (sin saturar en rojo).
2. **Clipchamp (Integrado en Windows 11 o vía web en Chrome):**
   * Permite grabar pantalla y cámara simultáneamente de forma sencilla y recortar silencios.
3. **Barra de Juegos de Windows (Xbox Game Bar):**
   * Presionar `Windows + Alt + R` para iniciar/detener grabación rápida de la ventana activa.

### 1.2 Parámetros Técnicos del Video
* **Resolución recomendada:** 1920x1080 (Full HD) a 30 o 60 fps. (Mínimo 1280x720 HD).
* **Audio:** Micrófono de diadema o manos libres con voz clara, modulada y sin eco ni música de fondo alta.
* **Cámara web:** Opcional pero muy bien valorada por los instructores SENA (puedes aparecer en una pequeña esquina "Picture-in-Picture" durante la introducción y despedida).

---

## 2. CHECKLIST PREVIO A LA GRABACIÓN (Antes de presionar "REC")

Realiza estos pasos 5 minutos antes de empezar a grabar:

- [ ] **Paso 1: Abrir la Terminal:**
  Abre tu terminal en la carpeta principal del proyecto:
  `/home/danilo/Escritorio/Karen/SENA`
  Verifica que el comando de prueba funcione correctamente antes de grabar:
  ```bash
  ./CDE/docker-test.sh Evidencias/PET-042_GA9-220501096-AA3-EV01_Documenta_Pruebas_Software_Planificacion/pruebas/ejecutar_pruebas_evidencia.js
  ```
  *(Al ejecutarlo, debe salirte en verde "pass 12, fail 0").* Deja la pantalla de la terminal limpia escribiendo `clear`.

- [ ] **Paso 2: Abrir VS Code / Editor:**
  Abre el archivo de pruebas en el editor:
  `CDE/Evidencias/PET-042_GA9-220501096-AA3-EV01_Documenta_Pruebas_Software_Planificacion/pruebas/ejecutar_pruebas_evidencia.js`
  Ten a la mano visibles las líneas donde están las aserciones de cálculo de impuestos (CP01) y contraseñas OWASP (CP05).

- [ ] **Paso 3: Abrir el PDF de la Evidencia o el Diagrama SVG/PNG:**
  Ten abierto en una pestaña del visor de documentos o navegador la infografía:
  `diagrama_ciclo_tdd_formatos_pruebas.png` o el informe en PDF con la portada lista.

- [ ] **Paso 4: Silenciar notificaciones:**
  Cierra WhatsApp Web, Telegram, Discord o notificaciones de correo para evitar ruidos o interrupciones en la pantalla.

---

## 3. GUION TÉCNICO ESCENA POR ESCENA (MINUTO A MINUTO)

Sigue esta estructura temporal para que tu exposición sea fluida, técnica y demuestre total apropiación del componente formativo **"Las pruebas de software"**:

```
+------------------------------------------------------------------------------------+
|                                CRONOGRAMA DEL VIDEO                                |
+------------------+-----------------------+-----------------------------------------+
| Minutos          | Escena / Bloque       | Contenido Principal                     |
+------------------+-----------------------+-----------------------------------------+
| 0:00 - 0:45 min  | Escena 1: Presentación| Identificación, contexto y teoría       |
| 0:45 - 1:45 min  | Escena 2: Formatos    | Estándar IEEE 829 y los 12 Casos CP     |
| 1:45 - 3:15 min  | Escena 3: Ejecución   | Demostración en vivo en Docker (Node)   |
| 3:15 - 4:15 min  | Escena 4: Bitácora/Bug| Ciclo TDD, bugs corregidos (Mera 2016)  |
| 4:15 - 5:00 min  | Escena 5: Conclusiones| Métricas de calidad y despedida formal  |
+------------------+-----------------------+-----------------------------------------+
```

---

### ESCENA 1: INTRODUCCIÓN Y FUNDAMENTACIÓN TEÓRICA (0:00 - 0:45 min)

* **Qué mostrar en pantalla:** Portada del informe técnico o la infografía `diagrama_ciclo_tdd_formatos_pruebas.png`. (Si tienes cámara, tu rostro en la esquina).
* **Acción en pantalla:** El cursor señala la portada institucional del SENA y los 7 principios de pruebas.

> **GUION VERBAL (Qué decir con seguridad):**
>  
> *"Un cordial saludo para los instructores y compañeros del Servicio Nacional de Aprendizaje SENA.  
> Mi nombre es **Karen Yuliana Campo**, aprendiz de la Tecnología en Análisis y Desarrollo de Software (ADSO), con número de ficha **3186681**, perteneciente al Centro de Teleinformática y Producción Industrial (CTPI) de la Regional Cauca.  
>  
> En el día de hoy presento la evidencia **GA9-220501096-AA3-EV01: Documenta pruebas de software, de acuerdo a la planificación**, aplicada a nuestro proyecto formativo: el sistema de gestión integral de pedidos, inventarios y facturación para la **Pizzería Gourmet Bella Italia Popayán**.  
>  
> Para el desarrollo de esta evidencia nos hemos basado de manera rigurosa en el componente formativo institucional **'Las pruebas de software'**, articulando la visión de autores como **Sanz (2005)** sobre la verificación sistemática para hallar fallos, y los **siete principios universales de las pruebas planteados por Mera (2016)**, tales como la importancia de las pruebas tempranas y la paradoja del pesticida, apoyándonos en el estándar de documentación **IEEE 829** y la metodología **TDD (Test-Driven Development)**."*

---

### ESCENA 2: ARQUITECTURA DE PRUEBAS Y FORMATOS IEEE 829 (0:45 - 1:45 min)

* **Qué mostrar en pantalla:** Cambias la ventana hacia el informe en PDF o Markdown en la sección **4. ESPECIFICACIÓN DE CASOS DE PRUEBA DILIGENCIADOS**.
* **Acción en pantalla:** Haces scroll pausado mostrando la tabla de los 12 casos de prueba y resaltas el formato IEEE 829 de CP01 y CP05.

> **GUION VERBAL (Qué decir):**
>  
> *"Como observamos en nuestro informe técnico estructurado bajo la norma **IEEE 829**, hemos planificado y documentado **doce casos de prueba** divididos en cinco módulos críticos del software:  
>  
> 1. Primero, el **Módulo de Facturación**, donde validamos el cálculo matemático del Subtotal y del **Impuesto Nacional al Consumo del 8%** según la normativa tributaria colombiana, las tarifas de domicilio con flete gratuito para Popayán y la restricción ante carritos vacíos.  
> 2. Segundo, el **Módulo de Autenticación y Seguridad**, donde evaluamos el cumplimiento de contraseñas robustas bajo el estándar internacional **OWASP ASVS**, la sintaxis estricta de correos bajo **RFC 5322**, y el control de acceso basado en roles **RBAC**.  
> 3. Tercero, el **Módulo de Clientes**, donde verificamos la normalización de números móviles colombianos según MinTIC y la sanitización de entradas contra inyecciones **Cross-Site Scripting (XSS)**.  
> 4. Cuarto, el **Módulo de Inventarios**, donde controlamos el descuento de materias primas por porción en gramos y prevenimos ventas por desabastecimiento.  
> 5. Y quinto, el **Módulo de Persistencia**, donde garantizamos transaccionalidad ACID en PostgreSQL asignando códigos secuenciales como `ORD-2026`."*

---

### ESCENA 3: DEMOSTRACIÓN EN VIVO DE EJECUCIÓN AUTOMATIZADA (1:45 - 3:15 min)

* **Qué mostrar en pantalla:** Minimizas el visor de PDF y abres la **Terminal** en primer plano.
* **Acción en pantalla:**
  1. Muestras la terminal limpia.
  2. Escribes y ejecutas el comando:
     `./CDE/docker-test.sh Evidencias/PET-042_GA9-220501096-AA3-EV01_Documenta_Pruebas_Software_Planificacion/pruebas/ejecutar_pruebas_evidencia.js`
  3. Dejas que la terminal ejecute los tests y se vean todos los chulos verdes `✔`.
  4. Muestras brevemente el código en VS Code destacando las aserciones con `node:test` y `assert.strictEqual`.

> **GUION VERBAL (Qué decir):**
>  
> *"A continuación, procederé a realizar la ejecución en vivo de la batería completa de pruebas automatizadas en nuestro contenedor Docker estandarizado.  
>  
> Como pueden apreciar en la terminal, ejecutamos el runner nativo de pruebas de Node.js.  
>  
> *(Ejecutas el comando y esperas 2 segundos mientras salen los resultados)*  
>  
> ¡Excelente! Observamos que las **seis suites de pruebas** se han ejecutado satisfactoriamente en tan solo 58 milisegundos. Tenemos **12 pruebas superadas, 0 pruebas fallidas (100% PASS rate)**.  
>  
> Si pasamos un instante al código fuente en nuestro editor, vemos cómo implementamos las aserciones nativas con `assert.strictEqual`. Por ejemplo, en el caso de prueba **CP01**, para dos pizzas gourmet de 35.000 pesos y una bebida de 8.000, el subtotal arroja exactamente 78.000 pesos, y al aplicar el 8% de Impoconsumo, el sistema calcula de manera exacta 6.240 pesos, para un total de 84.240 pesos sin discrepancias de punto flotante.  
>  
> Igualmente, en el **CP05**, probamos contra patrones OWASP que contraseñas débiles como '123456' sean rechazadas, y solo se admitan contraseñas seguras que incluyan mayúsculas, minúsculas, números y caracteres especiales."*

---

### ESCENA 4: BITÁCORA DE EJECUCIÓN Y REPORTE DE BUGS (3:15 - 4:15 min)

* **Qué mostrar en pantalla:** Vuelves al informe técnico en la sección **6. REPORTE DE INCIDENTES Y DEFECTOS CORREGIDOS (IEEE 829 DEFECT REPORT)** y a la infografía del Ciclo TDD.
* **Acción en pantalla:** Señalas los tres defectos resueltos y explicas el ciclo Red-Green-Refactor.

> **GUION VERBAL (Qué decir):**
>  
> *"Tal como lo señala **Mera (2016)** en el principio de 'Pruebas Tempranas' y en la disciplina de **TDD**, las pruebas no solo sirven para validar lo que ya funciona, sino primordialmente para descubrir defectos antes del despliegue a producción.  
>  
> En nuestra bitácora de ejecución documentamos tres incidencias clave que fueron resueltas durante el ciclo Rojo-Verde-Refactor:  
>  
> * Primero, el **Bug BUG-FAC-001**, donde el cálculo de decimales en JavaScript generaba centavos residuales. Se refactorizó aplicando redondeo matemático formal compatible con facturación electrónica.  
> * Segundo, el **Bug BUG-SEG-002**, donde corregimos la expresión regular de correos electrónicos para evitar que usuarios ingresaran correos sin extensión de dominio.  
> * Y tercero, el **Bug BUG-INV-003**, donde blindamos la sincronización de inventarios dentro de una transacción atómica de base de datos para evitar que un fallo de red descontara ingredientes sin que la orden existiera."*

---

### ESCENA 5: CONCLUSIONES Y CIERRE (4:15 - 5:00 min)

* **Qué mostrar en pantalla:** Vista final del informe técnico con la sección de conclusiones y referencias bibliográficas en Normas APA 7ma Edición. (O tu cámara web despidiéndote).

> **GUION VERBAL (Qué decir):**
>  
> *"Para concluir, la realización de esta evidencia nos permite certificar que el software de la Pizzería Gourmet Bella Italia Popayán cumple con altos estándares de fiabilidad, mantenibilidad y seguridad según el modelo **ISO/IEC 25000**.  
>  
> La adopción de formatos normalizados **IEEE 829** y la automatización en entornos reproducibles garantizan que cualquier cambio futuro en el código pueda ser verificado sin riesgo de regresiones operativas.  
>  
> El informe completo en formato PDF, la matriz de pruebas, el script de automatización y el enlace a este video han sido debidamente empaquetados y subidos al repositorio y a la plataforma institucional Zajuna.  
>  
> Muchas gracias por su atención y quedo atenta a sus comentarios y retroalimentación."*

---

## 4. INSTRUCCIONES DE SUBIDA Y ENTREGA DEL VIDEO

Una vez finalizada la grabación:

1. **Revisión del Video:**
   * Reproduce el archivo MP4 grabado y verifica que el audio se escuche nítido y la terminal sea legible.
2. **Subida a YouTube (Opción Recomendada):**
   * Ingresa a [YouTube Studio](https://studio.youtube.com/) con tu cuenta de Google / SENA.
   * Clic en **Crear** > **Subir videos**.
   * Título: `Karen Campo - Evidencia GA9-220501096-AA3-EV01 - Documentación de Pruebas de Software`.
   * En Visibilidad, selecciona **Oculto (Unlisted)**: de esta forma solo quienes tengan el enlace (los instructores) podrán verlo, sin que aparezca en búsquedas públicas.
   * Copia el enlace generado (ejemplo: `https://youtu.be/...`).
3. **Subida a Google Drive (Opción Alternativa):**
   * Sube el video a tu unidad de Google Drive.
   * Clic derecho > **Compartir** > Cambiar a **Cualquier persona con el enlace (Lector)**.
   * Copia el enlace generado.
4. **Actualizar el archivo de entrega:**
   * Pega el enlace en el archivo:
     `ENTREGA_ZAJUNA_GA9-220501096-AA3-EV01/enlace_video_y_repositorio.txt`
   * ¡Y listo! Tu entrega estará 100% completa, profesional y respaldada.
