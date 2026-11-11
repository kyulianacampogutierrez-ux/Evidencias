# Evidencia de Aprendizaje: Diagramas de Arquitectura UML 2.5 - Guía 8

* **Programa:** Tecnología en Análisis y Desarrollo de Software (ADSO) - Modalidad Virtual
* **Ficha:** 228118
* **Centro de Formación:** Centro de Teleinformática y Producción Industrial (CTPI Popayán)
* **Regional:** Regional Cauca
* **Aprendiz:** Karen Yuliana Campo
* **Proyecto Formativo:** Sistema Web & Móvil de Gestión de Pedidos - Pizzería Gourmet Bella Italia
* **Stack Tecnológico:**
  - Base de Datos: MongoDB 6 NoSQL (`pizzeria_db`)
  - Backend: Go 1.22 con Fiber v2 y autenticación JWT Bearer (Puerto 8085)
  - Frontend Web: Vite + React 18 + Tailwind CSS + shadcn/ui + TanStack Query (Puerto 5173)
  - Frontend Móvil: React Native con Expo SDK 58 (Puerto 8081 / LAN 192.168.20.21)
  - Despliegue: Docker Compose (Aislamiento total sin afectar el sistema anfitrión)
* **Estándar Gráfico:** UML 2.5 (ISO/IEC 19505)
* **Herramientas de Autoría:** DesignCraft CLI (`/usr/bin/designcraft-cli`) y FigCraft CLI (`/usr/bin/figcraft-cli`)

---

## 1. Justificación de Cumplimiento del Estándar UML 2.5

Atendiendo a la rigurosa retroalimentación técnica y a las exigencias curriculares del SENA, los diagramas han sido rediseñados desde cero siguiendo la especificación oficial **ISO/IEC 19505 / UML 2.5**:

1. **Diagrama de Clases UML 2.5 (`assets/diagrama_clases.png`):**
   - **Estructura Normalizada:** Cajas de 3 compartimentos formales (Nombre y Estereotipo, Atributos con visibilidad `+`/`-` y Tipos BSON/Go, Métodos con signatura completa de parámetros y retornos).
   - **Composición Fuerte (`◆`):** Rombos sólidos en relaciones de dependencia de ciclo de vida (`Pedido` a `ItemPedido`, `Pedido` a `TrackingPaso`, `Usuario` a `Direccion`, `Pizza` a `PreciosTamano`).
   - **Agregación Débil (`◇`):** Rombos vacíos (`Pedido` a `Cupon`).
   - **Multiplicidades Precisas:** Rotulación explícita de extremos (`1`, `1..*`, `0..1`, `*`).
   - **Realización de Interfaces (`..▷`):** Flechas discontinuas con punta triangular cerrada para la implementación de repositorios Go (`UsuarioMongoRepo` ..▷ `IUsuarioRepository`, etc.).
   - **Dependencias (`<<use>>`):** Flechas discontinuas con punta abierta entre capas de servicios y repositorios.

2. **Diagrama de Paquetes UML 2.5 (`assets/diagrama_paquetes.png`):**
   - **Símbolo Oficial:** Carpetas de dos cuerpos con pestaña superior rotulada (`package`).
   - **Organización en 5 Capas Limpias (Clean Architecture):**
     - *Capa 1: Presentación (Frontend Web & Móvil)*
     - *Capa 2: Transporte HTTP, Enrutamiento & Middlewares (Go Fiber REST)*
     - *Capa 3: Aplicación & Casos de Uso (Servicios Go Core)*
     - *Capa 4: Dominio del Sistema (Entidades BSON & DTOs)*
     - *Capa 5: Persistencia NoSQL MongoDB & Infraestructura*
   - **Dependencias Direccionales:** Flechas punteadas con estereotipos `<<use>>` y `<<import>>` respetando la regla de inversión de dependencias.

3. **Diagrama de Componentes UML 2.5 (`assets/diagrama_componentes.png`):**
   - **Símbolo Oficial de Componente:** Icono de dos pestañas rectangulares en la esquina superior derecha.
   - **Puertos de Comunicación:** Cuadrados de contorno perimetral (`p_out`, `p_in`, `p_lan`, `p_mongo`).
   - **Interfaces Provistas (Lollipops `-O`):** Círculos cerrados con línea sólida que representan contratos de API expuestos (`IAuthRestAPI`, `ICatalogoAPI`, `IPedidosAPI`, `ITrackingAPI`, `IMongoWireProtocol`).
   - **Interfaces Requeridas (Sockets `-()`):** Arcos semicirculares que indican consumo de servicios externos.
   - **Conectores de Ensamble (`-O)───()`):** Acoplamiento directo de piruleta y zócalo entre los contenedores Docker (`sena-frontend-vite`, `sena-rn-dev`, `sena-backend-go`, `sena-mongodb`).

---

## 2. Estructura de Entregables en la Carpeta

```text
Evidencias/DIAGRAMAS_ARQUITECTURA_GUIA8/
├── assets/
│   ├── diagrama_clases.png          # Render 2400x1350 px (Ultra HD)
│   ├── diagrama_paquetes.png        # Render 2400x1350 px (Ultra HD)
│   ├── diagrama_componentes.png     # Render 2400x1350 px (Ultra HD)
│   ├── diagrama_clases.svg          # Vector SVG estándar UML 2.5
│   ├── diagrama_paquetes.svg        # Vector SVG estándar UML 2.5
│   └── diagrama_componentes.svg     # Vector SVG estándar UML 2.5
├── designcraft/
│   ├── diagrama_clases.designcraft       # Archivo de proyecto nativo
│   ├── diagrama_paquetes.designcraft     # Archivo de proyecto nativo
│   └── diagrama_componentes.designcraft  # Archivo de proyecto nativo
├── figcraft/
│   ├── diagrama_clases.figcraft          # Archivo de proyecto nativo
│   ├── diagrama_paquetes.figcraft        # Archivo de proyecto nativo
│   └── diagrama_componentes.figcraft     # Archivo de proyecto nativo
├── Abrir_Diagramas_DesignCraft.bat   # Lanzador Windows para ArtCraft DesignCraft
├── Abrir_Diagramas_FigCraft.bat      # Lanzador Windows para ArtCraft FigCraft
├── Abrir_Diagramas_Linux.sh          # Lanzador para entornos Linux / Ubuntu
└── README.md                         # Ficha técnica institucional
```

---

## 3. Instrucciones de Apertura y Validación

* **En Windows con ArtCraft Suite:**
  Hacer doble clic en `Abrir_Diagramas_DesignCraft.bat` o `Abrir_Diagramas_FigCraft.bat`.
* **En Linux / WSL:**
  Ejecutar en la terminal `./Abrir_Diagramas_Linux.sh` o visualizar directamente los archivos PNG en la carpeta `assets/`.
* **Regeneración Automatizada:**
  Para regenerar los diagramas ejecutando las directivas del compilador de vectores y DesignCraft CLI:
  ```bash
  python3 scripts/generar_diagramas_uml_profesionales.py
  ```
