# Repositorio Oficial de Evidencias de Aprendizaje - SENA ADSO

<p align="center">
  <img src="https://img.shields.io/badge/SENA-Regional_Cauca-39a900?style=for-the-badge&logo=sena" alt="SENA">
  <img src="https://img.shields.io/badge/Ficha-228118-0284c7?style=for-the-badge" alt="Ficha 228118">
  <img src="https://img.shields.io/badge/ADSO-Modalidad_Virtual-c2410c?style=for-the-badge" alt="ADSO">
  <img src="https://img.shields.io/badge/Tests-171%20Passing-22c55e?style=for-the-badge" alt="Tests 171 Passing">
</p>

---

## 📌 Información Institucional del Aprendiz

* **Aprendiz:** **Karen Yuliana Campo**
* **Programa:** Análisis y Desarrollo de Software (ADSO) - Modalidad 100% Virtual
* **Ficha de Caracterización:** **228118**
* **Centro de Formación:** Centro de Teleinformática y Producción Industrial (CTPI)
* **Regional:** Regional Cauca - Popayán
* **Metodología de Desarrollo:** Test-Driven Development (TDD Red-Green-Refactor) & Contenedores Docker

---

## 📂 Estructura y Catálogo de Evidencias

Este repositorio consolida todos los entregables, códigos fuente, microservicios, suites de pruebas automatizadas, reportes en formato PDF institucional y paquetes normativos ZIP correspondientes a las **Guías de Aprendizaje 6 y 7**.

### ☕ Guía de Aprendizaje 7 (Fase de Ejecución - AP7: Codificar los Módulos del Software)

| Evidencia | Descripción Técnica | Tecnologías / Entregables |
| :--- | :--- | :--- |
| **GA7-AA1-EV01** (PET-011) | Plan de trabajo para construcción de software | DesignCraft, Infografías vectoriales, PDF formal 8 págs. |
| **GA7-AA1-EV02** (PET-012) | Definir estándares de codificación | SOLID, Clean Code, Linters, DesignCraft, PDF formal. |
| **GA7-AA1-EV03** (PET-013) | Identifica herramientas de versionamiento | Git Local vs GitHub, comandos, tablas comparativas, PDF formal. |
| **GA7-AA1-EV04** (PET-014) | Instalación y configuración de versionamiento | Código LaTeX Overleaf, 24 capturas de pantalla reales, PDF formal. |
| **GA7-AA1-EV05** (PET-015) | Versionamiento (GIT) configurado (Video práctico) | Repositorio `Programa-Git`, `kotlin.txt`, presentador interactivo HTML. |
| **GA7-AA2-EV01** (PET-015) | Codificación de módulos del software (JDBC + DAO) | Java JDK 17, Maven, MariaDB 10.5 Docker, JUnit 5, POO, CRUD. |
| **GA7-AA2-EV02** (PET-016) | Módulos web codificados y probados (Servlets + JSP) | Java Servlets, JSP, Tomcat 10 Docker, WAR, Formularios GET/POST. |
| **GA7-AA3-EV01** (PET-017) | Codificación con Frameworks de Java (Spring Boot) | Spring Boot 3, Spring Data JPA, Hibernate, REST API, JUnit 5. |
| **GA7-AA3-EV02** (PET-018) | Módulos probados con HU y Casos de Uso | Matriz de pruebas HU-01..HU-04, validaciones, JUnit 5 10/10 tests. |
| **GA7-AA4-EV01** (PET-019) | Taller sobre componentes front-end (React-JS) | React vs JSX, Babel, Clases vs Hooks, SyntheticEvent, Virtual DOM. |
| **GA7-AA4-EV02** (PET-020) | Procedimientos para definición de componentes | Atomic Design, catálogo 11 componentes React, Props/State, WCAG 2.1 AA. |
| **GA7-AA4-EV03** (PET-021) | Componente front-end del proyecto (React SPA) | Aplicación React 18, 11 componentes, Context API, carrito y pedidos. |
| **GA7-AA5-EV01** (PET-022) | Diseño y desarrollo de servicios web - caso | Microservicio REST Node.js, Scrypt/BCrypt con salt, JWT, Auth API. |
| **GA7-AA5-EV02** (PET-023) | API (Testing de Servicios Web con Postman) | Colección Postman v2.1 (8 tests), 6 capturas HD, presentador interactivo, `ENDPOINT.txt`. |

---

### 🎨 Guía de Aprendizaje 6 (Fase de Ejecución y Transversales)

| Evidencia | Descripción Técnica | Tecnologías / Entregables |
| :--- | :--- | :--- |
| **GA6-AA3-EV02** (PET-001) | Diseño de mockups interactivos de la pizzería | 3 mockups vectoriales en DesignCraft (Login, Menú, Pedido). |
| **GA6-AA3-EV03** (PET-002) | Interfaces gráficas según requerimientos | Frontend web interactivo HTML/CSS/JS con RBAC Cliente y Admin. |
| **GA6-AA4-EV01** (PET-003) | Tutorial de componentes frontend | Página educativa interactiva con retícula 8dp y dark mode. |
| **GA6-AA4-EV02** (PET-004) | Especificación de componentes frontend | Árbol de 8 componentes modulares, HTML5 semántico y roles ARIA. |
| **GA6-AA4-EV03** (PET-005) | Diseño frontend del proyecto de pizzas | Aplicación SPA completa `FrontEnd_Pizzeria`, métricas KPI y cocina. |
| **GA6-230101507-AA2-EV01** (PET-006) | Infografía: Estilos de vida y ergonomía | Maquetación vectorial en DesignCraft CLI (507 comandos), PNG HD. |
| **GA6-230101507-AA3-EV01** (PET-007) | Ficha antropométrica de valoración física | Registro biométrico (IMC 22.04), 6 tests físicos y plan semanal. |
| **GA6-230101507-AA4-EV01** (PET-008) | Folleto de lesiones y pausas activas | Tríptico editorial en DesignCraft (475 comandos), 2 caras PNG 1800x1000. |
| **GA6-240202501-AA1-EV01** (PET-009) | Written Document: Personal Statement | Declaración profesional en inglés (567 palabras, B1.2+). |
| **GA6-240202501-AA1-EV02** (PET-010) | Video presentación oral: Tecnología evolutiva | Diapositivas DesignCraft / FigCraft, presentador interactivo HTML. |

---

## 🛠️ Entorno de Ejecución con Docker

Para garantizar reproducibilidad sin saturar el sistema operativo anfitrión:
* **MariaDB 10.5:** Puerto `3306` (`sena-pizzeria-db`)
* **Apache Tomcat 10:** Puerto `8080` (`sena-tomcat-pizzeria`)
* **Spring Boot 3 REST:** Puerto `8082` (`sena-springboot-pizzeria`)
* **Frontend React SPA:** Puerto `3000` (`sena-frontend-react`)
* **Test Runner TDD:** Contenedor Node 20 Alpine (`docker-test.sh`)

---

<p align="center">
  <em>Desarrollado con dedicación y rigor técnico para el SENA - CTPI Popayán &bull; 2026</em>
</p>
