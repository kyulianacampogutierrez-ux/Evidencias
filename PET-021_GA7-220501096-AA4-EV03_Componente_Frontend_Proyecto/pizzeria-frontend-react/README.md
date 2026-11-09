# Pizzería Bella Italia - Frontend React SPA

> **Proyecto Formativo SENA:** Sistema de Gestión y Pedidos en Línea  
> **Programa:** Tecnología en Análisis y Desarrollo de Software (ADSO) - Ficha 228118  
> **Evidencia:** GA7-220501096-AA4-EV03: Componente front-end del proyecto formativo y proyectos de clase  
> **Aprendiz:** Karen Yuliana Campo  
> **Centro:** Centro de Teleinformática y Producción Industrial (CTPI) - Regional Cauca (Popayán)

---

## 🚀 Arquitectura y Tecnologías
- **Framework:** React 18 con Vite
- **Estado Global:** Context API (`CartContext` y `AuthContext`)
- **Diseño y Estilos:** CSS3 modular, variables CSS, retícula 8dp y responsive design
- **Integración Backend:** REST API Spring Boot 3 (`http://localhost:8082/api`)
- **Contenedores:** Docker Compose con red de microservicios `sena_network`

---

## 📦 Estructura del Código
```
pizzeria-frontend-react/
├── index.html
├── package.json
├── src/
│   ├── App.jsx
│   ├── main.jsx
│   ├── components/
│   │   ├── Navbar.jsx
│   │   ├── HeroBanner.jsx
│   │   ├── KPIStats.jsx
│   │   ├── CategoryFilter.jsx
│   │   ├── PizzaMenuGrid.jsx
│   │   ├── PizzaCard.jsx
│   │   ├── CartDrawer.jsx
│   │   ├── CartItem.jsx
│   │   ├── CustomerFormModal.jsx
│   │   ├── OrderStatusTracker.jsx
│   │   └── OrderHistoryTable.jsx
│   ├── context/
│   │   ├── CartContext.jsx
│   │   └── AuthContext.jsx
│   ├── services/
│   │   └── api.js
│   └── styles/
│       ├── App.css
│       └── index.css
```

---

## ⚙️ Instrucciones de Ejecución

### 1. Con Node.js / Vite local
```bash
npm install
npm run dev
```

### 2. Con Docker (Contenedor Node)
```bash
docker run -it --rm -v $(pwd):/app -w /app -p 5173:5173 node:20-alpine sh -c "npm install && npm run dev -- --host"
```
Acceder a la aplicación en el navegador: `http://localhost:5173`.
