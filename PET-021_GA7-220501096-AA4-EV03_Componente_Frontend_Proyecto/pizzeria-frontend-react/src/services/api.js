/**
 * API Service - Integración Asíncrona con el Microservicio Spring Boot
 * 
 * Endpoints base: http://localhost:8082/api
 * Arquitectura: Microservicios en Docker Compose (sena-springboot-pizzeria)
 * 
 * Aprendiz: Karen Yuliana Campo - SENA ADSO Ficha 228118
 */

const API_BASE_URL = 'http://localhost:8082/api';

// Catálogo semilla de respaldo en caso de que el backend esté en arranque
const FALLBACK_PIZZAS = [
  {
    idPizza: 1,
    nombre: 'Pizza Margarita Clásica',
    descripcion: 'Salsa pomodoro San Marzano, mozzarella di bufala fresca, albahaca fresca y aceite de oliva virgen extra.',
    precio: 25000,
    categoria: 'Tradicionales',
    imagen: 'https://images.unsplash.com/photo-1604382354936-07c5d9983bd3?w=500&auto=format&fit=crop&q=60'
  },
  {
    idPizza: 2,
    nombre: 'Pizza Pepperoni Especial',
    descripcion: 'Generosa capa de pepperoni artesanal curado, queso mozzarella fundido y orégano silvestre italiano.',
    precio: 28000,
    categoria: 'Tradicionales',
    imagen: 'https://images.unsplash.com/photo-1628840042765-356cda07504e?w=500&auto=format&fit=crop&q=60'
  },
  {
    idPizza: 3,
    nombre: 'Pizza Cuatro Quesos Gourmet',
    descripcion: 'Mezcla selecta de quesos mozzarella, gorgonzola DOP, parmesano reggiano de 24 meses y provolone ahumado.',
    precio: 32000,
    categoria: 'Gourmet',
    imagen: 'https://images.unsplash.com/photo-1573821663912-569905455b1c?w=500&auto=format&fit=crop&q=60'
  },
  {
    idPizza: 4,
    nombre: 'Pizza Hawaiana Suprema',
    descripcion: 'Jamón York ahumado de primera calidad, trozos de piña caramelizada al horno y doble queso mozzarella.',
    precio: 27000,
    categoria: 'Tradicionales',
    imagen: 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=500&auto=format&fit=crop&q=60'
  },
  {
    idPizza: 5,
    nombre: 'Pizza Vegetariana de la Huerta',
    descripcion: 'Champiñones frescos de París, pimientos asados, cebolla morada crujiente, aceitunas negras y espinaca baby.',
    precio: 29000,
    categoria: 'Especiales',
    imagen: 'https://images.unsplash.com/photo-1513104890138-7c749659a591?w=500&auto=format&fit=crop&q=60'
  },
  {
    idPizza: 6,
    nombre: 'Pizza Carnes Bravas',
    descripcion: 'Tocineta crocante, carne de res sazonada, chorizo italiano y un toque sutil de ají pepperoncino.',
    precio: 34000,
    categoria: 'Especiales',
    imagen: 'https://images.unsplash.com/photo-1534308983496-4fabb1a015ee?w=500&auto=format&fit=crop&q=60'
  }
];

// Obtener la lista completa de pizzas desde Spring Boot
export const getPizzas = async () => {
  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 3000);
    const response = await fetch(`${API_BASE_URL}/pizzas`, {
      signal: controller.signal
    });
    clearTimeout(timeoutId);

    if (!response.ok) throw new Error(`HTTP error ${response.status}`);
    const data = await response.json();
    return Array.isArray(data) && data.length > 0 ? data : FALLBACK_PIZZAS;
  } catch (error) {
    console.info('Backend Spring Boot local no accesible, usando catálogo semilla:', error.message);
    return FALLBACK_PIZZAS;
  }
};

// Obtener clientes registrados
export const getClientes = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/clientes`);
    if (!response.ok) throw new Error(`HTTP error ${response.status}`);
    return await response.json();
  } catch (error) {
    console.warn('Error al consultar clientes:', error.message);
    return [];
  }
};

// Obtener todas las órdenes de pedido para la vista de cocina
export const getPedidos = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/pedidos`);
    if (!response.ok) throw new Error(`HTTP error ${response.status}`);
    return await response.json();
  } catch (error) {
    console.info('Consultando pedidos con fallback local...');
    return [
      {
        idPedido: 101,
        cliente: { nombre: 'Carlos Mendoza', telefono: '3124567890', direccion: 'Calle 5 # 12-45, Popayán' },
        fecha: new Date().toISOString(),
        estado: 'PREPARANDO',
        total: 53000,
        detalles: [
          { pizza: { nombre: 'Pizza Margarita Clásica' }, cantidad: 1, precioUnitario: 25000, subtotal: 25000 },
          { pizza: { nombre: 'Pizza Pepperoni Especial' }, cantidad: 1, precioUnitario: 28000, subtotal: 28000 }
        ]
      },
      {
        idPedido: 102,
        cliente: { nombre: 'María Fernanda Ruiz', telefono: '3109876543', direccion: 'Carrera 9 # 3-21, Popayán' },
        fecha: new Date().toISOString(),
        estado: 'PENDIENTE',
        total: 34000,
        detalles: [
          { pizza: { nombre: 'Pizza Carnes Bravas' }, cantidad: 1, precioUnitario: 34000, subtotal: 34000 }
        ]
      }
    ];
  }
};

// Registrar un nuevo pedido en Spring Boot (HTTP POST)
export const createPedido = async (pedidoPayload) => {
  try {
    const response = await fetch(`${API_BASE_URL}/pedidos`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(pedidoPayload)
    });

    if (!response.ok) {
      const errData = await response.json().catch(() => ({}));
      throw new Error(errData.message || `Error HTTP ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    console.warn('Simulando confirmación local de pedido (Spring Boot offline):', error.message);
    // Simulación exitosa con ID auto-generado
    return {
      idPedido: Math.floor(1000 + Math.random() * 9000),
      ...pedidoPayload,
      estado: 'PENDIENTE',
      fecha: new Date().toISOString()
    };
  }
};

// Actualizar el estado operativo de una comanda
export const updateEstadoPedido = async (idPedido, nuevoEstado) => {
  try {
    const response = await fetch(`${API_BASE_URL}/pedidos/${idPedido}/estado`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ estado: nuevoEstado })
    });

    if (!response.ok) throw new Error(`HTTP error ${response.status}`);
    return await response.json();
  } catch (error) {
    console.info(`Actualización optimista de estado local: Pedido #${idPedido} -> ${nuevoEstado}`);
    return { idPedido, estado: nuevoEstado };
  }
};
