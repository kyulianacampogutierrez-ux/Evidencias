# Evidencia: Diseño y Desarrollo de Servicios Web – Proyecto (GA7-220501096-AA5-EV03)

* **Programa:** Tecnología en Análisis y Desarrollo de Software (ADSO) - Modalidad 100% Virtual
* **Ficha de Caracterización:** 228118
* **Centro de Formación:** Centro de Teleinformática y Producción Industrial (CTPI Popayán)
* **Regional:** Regional Cauca
* **Aprendiz:** Karen Yuliana Campo
* **Proyecto Formativo:** Pizzería Gourmet Bella Italia Popayán
* **Stack Tecnológico:**
  - Base de Datos: MongoDB 6 NoSQL (Base de datos: `pizzeria_db`)
  - Backend: Go 1.22 con framework Fiber v2 y autenticación JWT Bearer (Puerto 8085)
  - Control de Acceso: RBAC con roles `ADMIN` y `CLIENTE`, y hashing de contraseñas Bcrypt
  - Modelado Estructural: UML 2.5 (Clases, Paquetes, Componentes) en Draw.io y DesignCraft
  - Especificación: OpenAPI 3.0.3 (YAML) y Colección Postman v2.1
  - Despliegue: Docker Compose en red bridge aislada `sena-network`

---

## 1. Estructura de Entregables de la Evidencia

```text
PET-024_GA7-220501096-AA5-EV03_Diseno_Servicios_Web_Proyecto/
├── GA7-220501096-AA5-EV03_Diseno_Servicios_Web_Proyecto.pdf  # Informe técnico oficial SENA (12 páginas)
├── KARENCAMPO_AA5_EV03.zip                                  # Paquete normativo comprimido
├── enlace_repositorio.txt                                   # Enlace oficial del repositorio Git/GitHub
├── reporte_imprimible.html                                  # Plantilla HTML con diagramas base64
├── compile_pdf.py                                           # Script de compilación headless Chrome
├── README.md                                                # Ficha técnica descriptiva
├── codigo_fuente/                                           # Código fuente completo en Go Fiber v2
│   ├── main.go
│   ├── go.mod / go.sum
│   ├── init-mongo.js
│   ├── config/ (database.go)
│   ├── handlers/ (auth, pizza, pedido, pago, cupon, admin)
│   ├── middleware/ (jwt.go)
│   ├── models/ (usuario, pizza, pedido, pago, cupon, categoria)
│   └── routes/ (routes.go)
├── diagramas/                                               # Diagramas UML 2.5 en Ultra HD
│   ├── diagrama_clases.drawio / .png / .svg
│   ├── diagrama_paquetes.drawio / .png / .svg
│   └── diagrama_componentes.drawio / .png / .svg
├── postman/                                                 # Testing automatizado de APIs
│   ├── Postman_Collection_Proyecto_Pizzeria.json
│   └── Postman_Environment_Proyecto_Pizzeria.json
└── docs/                                                    # Documentación de interfaces
    ├── ENDPOINTS.md
    ├── ENDPOINT.txt
    └── openapi.yaml
```

---

## 2. Carpeta de Entrega para Zajuna (Escritorio)

En cumplimiento de los lineamientos institucionales SENA, los archivos listos para entrega directa se encuentran disponibles en:
`/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA7-220501096-AA5-EV03/`

* `KARENCAMPO_AA5_EV03.zip` (Paquete normativo comprimido de 4.06 MB)
* `GA7-220501096-AA5-EV03_Diseno_Servicios_Web_Proyecto.pdf` (Documento formal de 12 páginas)
* `enlace_repositorio.txt` (Enlace de control de versiones Git)
* `ENDPOINTS.md` (Documentación técnica de endpoints)

---

## 3. Instrucciones de Ejecución y Pruebas

Para levantar el ecosistema completo de servicios en Docker Compose:
```bash
docker compose up -d sena-mongodb sena-backend-go
```

Para ejecutar las pruebas automatizadas del proyecto formativo:
```bash
./docker-test.sh
```
