# Pizzería Bella Italia - Aplicación Móvil (React Native)

**Programa:** Tecnología en Análisis y Desarrollo de Software (ADSO) - Modalidad Virtual  
**Ficha:** 228118  
**Aprendiz:** Karen Yuliana Campo  
**Centro:** Centro de Teleinformática y Producción Industrial (CTPI) - Popayán, Regional Cauca  
**Actividad de Aprendizaje:** Guía de Aprendizaje 8 - Módulos Móviles del Proyecto  

---

## 1. Descripción del Proyecto Móvil

Esta aplicación móvil multiplataforma desarrollada en **React Native** complementa el ecosistema de **Pizzería Bella Italia**, comunicándose de forma asíncrona con el backend REST construido en **Go + Fiber v2** y la base de datos documental **MongoDB**.

### Módulos Implementados:
1. **Inicio:** Pantalla principal con ofertas destacadas, cupones de descuento comunitarios (`SENA2026`) e información del horno artesanal a la leña.
2. **Carta & Menú:** Catálogo interactivo de pizzas categorizadas con precios dinámicos y descripciones.
3. **Carrito de Compras:** Selección de pizzas, cálculo automático de totales y selección de medios de pago (Tarjetas, PSE / Nequi / Daviplata, Efectivo contra entrega).
4. **Estados (Tracking en Vivo):** Stepper visual animado que muestra el ciclo del pedido: `RECIBIDO` → `EN_PREPARACION` → `EN_HORNO` → `EN_CAMINO` → `ENTREGADO`.
5. **Módulo de Clientes & Administrador:** Perfil del aprendiz / cliente autenticado y métricas de MongoDB en tiempo real.

---

## 2. Ejecución y Despliegue

```bash
# Instalar dependencias
npm install

# Iniciar servidor de desarrollo Expo
npm start

# Ejecutar en emulador o dispositivo Android
npm run android

# Ejecutar en entorno Web
npm run web
```
