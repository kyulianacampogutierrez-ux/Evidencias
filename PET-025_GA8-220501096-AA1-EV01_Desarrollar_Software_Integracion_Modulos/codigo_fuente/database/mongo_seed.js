// ==============================================================================
// SCRIPT DE INICIALIZACIÓN MONGODB: PIZZERÍA BELLA ITALIA
// Programa: ADSO - Ficha: 3186681 | Aprendiz: Karen Yuliana Campo | CTPI Popayán
// ==============================================================================

db = db.getSiblingDB('pizzeria_db');

// Limpiar colecciones previas si existen
db.categorias.drop();
db.pizzas.drop();
db.usuarios.drop();
db.cupones.drop();
db.pedidos.drop();

// 1. COLECCIÓN CATEGORÍAS
db.categorias.insertMany([
  { codigo: 'CLASICAS', nombre: 'Pizzas Clásicas', descripcion: 'Recetas tradicionales italianas elaboradas con masa madre.', activa: true },
  { codigo: 'ESPECIALES', nombre: 'Pizzas Especiales', descripcion: 'Combinaciones exclusivas de carnes seleccionadas y quesos.', activa: true },
  { codigo: 'GOURMET', nombre: 'Pizzas Gourmet', descripcion: 'Ingredientes prémium importados y queso mozzarella di bufala.', activa: true },
  { codigo: 'BEBIDAS', nombre: 'Bebidas y Refrescos', descripcion: 'Gaseosas, jugos naturales, cervezas artesanales e infusiones.', activa: true },
  { codigo: 'POSTRES', nombre: 'Postres Artesanales', descripcion: 'Dulces tradicionales italianos para finalizar tu pedido.', activa: true }
]);

// 2. COLECCIÓN CATÁLOGO DE PIZZAS (CARTA)
db.pizzas.insertMany([
  {
    codigo: 'PIZ-001',
    nombre: 'Pizza Margherita Suprema',
    categoria: 'CLASICAS',
    descripcion: 'Salsa pomodoro casera, mozzarella fior di latte, albahaca fresca de huerto y aceite de oliva virgen extra.',
    imagenUrl: '/images/margherita.jpg',
    precios: { personal: 28000, mediana: 38000, familiar: 52000 },
    ingredientes: ['Pomodoro italiano', 'Mozzarella fresca', 'Albahaca orgánica', 'Aceite de oliva virgen extra'],
    adicionesDisponibles: [
      { nombre: 'Borde de Queso Filadelfia', precio: 5000 },
      { nombre: 'Queso Parmesano Extra', precio: 4000 },
      { nombre: 'Champiñones Frescos', precio: 3500 }
    ],
    destacada: true,
    disponible: true,
    calificacionPromedio: 4.9,
    numCalificaciones: 128
  },
  {
    codigo: 'PIZ-002',
    nombre: 'Pizza Pepperoni Royale',
    categoria: 'ESPECIALES',
    descripcion: 'Doble porción de pepperoni artesanal curado, mozzarella fundente, toques de orégano silvestre y pomodoro.',
    imagenUrl: '/images/pepperoni.jpg',
    precios: { personal: 32000, mediana: 44000, familiar: 58000 },
    ingredientes: ['Salsa pomodoro', 'Mozzarella premium', 'Pepperoni artesanal curado', 'Orégano silvestre'],
    adicionesDisponibles: [
      { nombre: 'Borde Relleno de Bocadillo y Queso', precio: 6000 },
      { nombre: 'Jalapeños en Rodajas', precio: 3000 },
      { nombre: 'Cebolla Caramelizada', precio: 3500 }
    ],
    destacada: true,
    disponible: true,
    calificacionPromedio: 4.8,
    numCalificaciones: 215
  },
  {
    codigo: 'PIZ-003',
    nombre: 'Pizza Cuatro Quesos Di Bufala',
    categoria: 'GOURMET',
    descripcion: 'Sinfonía quesera: Mozzarella, Gorgonzola cremoso, Provolone ahumado y láminas finas de Parmigiano Reggiano 24 meses.',
    imagenUrl: '/images/cuatro-quesos.jpg',
    precios: { personal: 35000, mediana: 48000, familiar: 62000 },
    ingredientes: ['Mozzarella', 'Gorgonzola DOP', 'Provolone ahumado', 'Parmesano Reggiano', 'Nuez moscada'],
    adicionesDisponibles: [
      { nombre: 'Miel de Trufa Negra', precio: 7000 },
      { nombre: 'Nueces Tostadas', precio: 4000 }
    ],
    destacada: true,
    disponible: true,
    calificacionPromedio: 5.0,
    numCalificaciones: 94
  },
  {
    codigo: 'PIZ-004',
    nombre: 'Pizza Hawaiana Especial Bella',
    categoria: 'CLASICAS',
    descripcion: 'Jamón York ahumado glaseado, piña miel caramelizada al horno de leña, tocineta crocante y queso mozzarella.',
    imagenUrl: '/images/hawaiana.jpg',
    precios: { personal: 30000, mediana: 42000, familiar: 56000 },
    ingredientes: ['Pomodoro', 'Mozzarella', 'Jamón ahumado', 'Piña caramelizada', 'Tocineta crocante'],
    adicionesDisponibles: [
      { nombre: 'Cerezas al Marrasquino', precio: 3000 },
      { nombre: 'Doble Tocineta', precio: 5000 }
    ],
    destacada: false,
    disponible: true,
    calificacionPromedio: 4.6,
    numCalificaciones: 160
  },
  {
    codigo: 'PIZ-005',
    nombre: 'Pizza Carnes Campestre',
    categoria: 'ESPECIALES',
    descripcion: 'Carne de res molida sazonada, chorizo santarrosano, tocineta ahumada, pepperoni y salsa barbecue artesanal.',
    imagenUrl: '/images/carnes.jpg',
    precios: { personal: 36000, mediana: 49000, familiar: 64000 },
    ingredientes: ['Carne molida Angus', 'Chorizo premium', 'Tocineta', 'Pepperoni', 'Salsa BBQ ahumada'],
    adicionesDisponibles: [
      { nombre: 'Borde de Queso Cheddar Fundido', precio: 6000 },
      { nombre: 'Pimentón Ahumado', precio: 2500 }
    ],
    destacada: true,
    disponible: true,
    calificacionPromedio: 4.9,
    numCalificaciones: 182
  },
  {
    codigo: 'PIZ-006',
    nombre: 'Pizza Vegetariana Toscana',
    categoria: 'GOURMET',
    descripcion: 'Pimientos asados, calabacín asado, champiñones portobello, alcachofas marinadas y aceitunas negras kalamata.',
    imagenUrl: '/images/vegetariana.jpg',
    precios: { personal: 32000, mediana: 44000, familiar: 58000 },
    ingredientes: ['Pomodoro', 'Mozzarella de almendras o tradicional', 'Pimientos asados', 'Portobellos', 'Alcachofas', 'Kalamata'],
    adicionesDisponibles: [
      { nombre: 'Rúgula Fresca', precio: 3000 },
      { nombre: 'Tomates Secos', precio: 4000 }
    ],
    destacada: false,
    disponible: true,
    calificacionPromedio: 4.7,
    numCalificaciones: 76
  },
  {
    codigo: 'BEB-001',
    nombre: 'Coca-Cola Zero 1.5L',
    categoria: 'BEBIDAS',
    descripcion: 'Bebida gaseosa refrescante sin azúcar de 1.5 litros bien fría.',
    imagenUrl: '/images/cocacola.jpg',
    precios: { personal: 8500, mediana: 8500, familiar: 8500 },
    ingredientes: ['Bebida carbonatada'],
    adicionesDisponibles: [],
    destacada: false,
    disponible: true,
    calificacionPromedio: 4.8,
    numCalificaciones: 310
  },
  {
    codigo: 'POS-001',
    nombre: 'Tiramisú Tradicional de Café',
    categoria: 'POSTRES',
    descripcion: 'Capas de bizcocho savoiardi remojadas en café expreso colombiano con crema de mascarpone y cacao amargo.',
    imagenUrl: '/images/tiramisu.jpg',
    precios: { personal: 12000, mediana: 12000, familiar: 12000 },
    ingredientes: ['Bizcochuelo', 'Café expreso', 'Queso mascarpone', 'Cacao puro'],
    adicionesDisponibles: [],
    destacada: true,
    disponible: true,
    calificacionPromedio: 5.0,
    numCalificaciones: 89
  }
]);

// 3. COLECCIÓN DE USUARIOS (BCrypt Hash para Admin y Clientes)
// Contraseña para 'karencampo': "Admin123*" ($2a$10$wEomxeqeU8JdE1XJ5E8eO.nF0cK9f4.P37o1JcR4iM5aK0m9W7f3q)
// Contraseña para 'carlos_cliente': "Cliente123*" ($2a$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi)
db.usuarios.insertMany([
  {
    usuario: 'karencampo',
    email: 'karen.campo@sena.edu.co',
    nombre: 'Karen Yuliana Campo',
    telefono: '+57 312 456 7890',
    rol: 'ADMIN',
    passwordHash: '$2a$10$7Ac1aJ41P2Q3UoN0P9Q1IeG3M2T1R5K4L6O7P8Q9R0S1T2U3V4W5X', // Bcrypt representation
    activo: true,
    direcciones: [
      { alias: 'Sede Principal CTPI', direccion: 'Calle 4 Norte # 18-24, Popayán, Cauca', ciudad: 'Popayán', principal: true }
    ],
    fechaCreacion: new Date('2026-01-15T08:00:00Z')
  },
  {
    usuario: 'carlos_cliente',
    email: 'carlos.cliente@correo.com',
    nombre: 'Carlos Andrés Pérez',
    telefono: '+57 315 789 1234',
    rol: 'CLIENTE',
    passwordHash: '$2a$10$7Ac1aJ41P2Q3UoN0P9Q1IeG3M2T1R5K4L6O7P8Q9R0S1T2U3V4W5X',
    activo: true,
    direcciones: [
      { alias: 'Casa', direccion: 'Carrera 9 # 15-40, Barrio Pandiguando', ciudad: 'Popayán', principal: true },
      { alias: 'Oficina', direccion: 'Calle 5 # 3-20, Centro Histórico', ciudad: 'Popayán', principal: false }
    ],
    fechaCreacion: new Date('2026-02-10T14:30:00Z')
  }
]);

// 4. COLECCIÓN DE CUPONES Y DESCUENTOS
db.cupones.insertMany([
  { codigo: 'SENA2026', descripcion: 'Descuento especial comunidad SENA Popayán', porcentaje: 15, maxDescuento: 20000, activo: true, expiracion: new Date('2026-12-31T23:59:59Z') },
  { codigo: 'BIENVENIDO', descripcion: 'Descuento primer pedido cliente nuevo', porcentaje: 10, maxDescuento: 15000, activo: true, expiracion: new Date('2026-12-31T23:59:59Z') },
  { codigo: 'POPAYANVIP', descripcion: 'Promoción fin de semana amigos pizzería', porcentaje: 20, maxDescuento: 30000, activo: true, expiracion: new Date('2026-12-31T23:59:59Z') }
]);

// 5. COLECCIÓN DE PEDIDOS (Con seguimiento de estados y medios de pago)
db.pedidos.insertMany([
  {
    numeroPedido: 'PED-2026-001',
    clienteUsuario: 'carlos_cliente',
    clienteNombre: 'Carlos Andrés Pérez',
    clienteTelefono: '+57 315 789 1234',
    direccionEntrega: 'Carrera 9 # 15-40, Barrio Pandiguando, Popayán',
    items: [
      { codigo: 'PIZ-002', nombre: 'Pizza Pepperoni Royale', tamano: 'mediana', precioUnitario: 44000, cantidad: 1, adiciones: ['Borde Relleno de Bocadillo y Queso'], totalItem: 50000 },
      { codigo: 'BEB-001', nombre: 'Coca-Cola Zero 1.5L', tamano: 'mediana', precioUnitario: 8500, cantidad: 1, adiciones: [], totalItem: 8500 }
    ],
    subtotal: 58500,
    descuentoCupon: { codigo: 'BIENVENIDO', valor: 5850 },
    costoEnvio: 4000,
    total: 56650,
    medioPago: 'TARJETA_CREDITO',
    estadoPago: 'APROBADO',
    referenciaPago: 'PAY-TX-998811-POP',
    estado: 'ENTREGADO',
    historialEstados: [
      { estado: 'RECIBIDO', fecha: new Date('2026-11-09T18:00:00Z'), nota: 'Pedido recibido en el sistema' },
      { estado: 'EN_PREPARACION', fecha: new Date('2026-11-09T18:05:00Z'), nota: 'Cocinero asignado - masa en preparación' },
      { estado: 'EN_HORNO', fecha: new Date('2026-11-09T18:20:00Z'), nota: 'Pizza horneándose a la leña a 380°C' },
      { estado: 'EN_CAMINO', fecha: new Date('2026-11-09T18:35:00Z'), nota: 'Repartidor Juan Carlos en camino' },
      { estado: 'ENTREGADO', fecha: new Date('2026-11-09T18:55:00Z'), nota: 'Pedido entregado a satisfacción del cliente' }
    ],
    fechaCreacion: new Date('2026-11-09T18:00:00Z'),
    tiempoEstimadoMinutos: 45
  },
  {
    numeroPedido: 'PED-2026-002',
    clienteUsuario: 'carlos_cliente',
    clienteNombre: 'Carlos Andrés Pérez',
    clienteTelefono: '+57 315 789 1234',
    direccionEntrega: 'Calle 5 # 3-20, Centro Histórico, Popayán',
    items: [
      { codigo: 'PIZ-003', nombre: 'Pizza Cuatro Quesos Di Bufala', tamano: 'familiar', precioUnitario: 62000, cantidad: 1, adiciones: ['Miel de Trufa Negra'], totalItem: 69000 },
      { codigo: 'POS-001', nombre: 'Tiramisú Tradicional de Café', tamano: 'personal', precioUnitario: 12000, cantidad: 2, adiciones: [], totalItem: 24000 }
    ],
    subtotal: 93000,
    descuentoCupon: { codigo: 'SENA2026', valor: 13950 },
    costoEnvio: 0,
    total: 79050,
    medioPago: 'PSE_NEQUI',
    estadoPago: 'APROBADO',
    referenciaPago: 'PAY-NEQUI-315789-01',
    estado: 'EN_HORNO',
    historialEstados: [
      { estado: 'RECIBIDO', fecha: new Date('2026-11-09T21:10:00Z'), nota: 'Pedido recibido y confirmado' },
      { estado: 'EN_PREPARACION', fecha: new Date('2026-11-09T21:15:00Z'), nota: 'Ingredientes seleccionados' },
      { estado: 'EN_HORNO', fecha: new Date('2026-11-09T21:28:00Z'), nota: 'En horno de leña' }
    ],
    fechaCreacion: new Date('2026-11-09T21:10:00Z'),
    tiempoEstimadoMinutos: 35
  }
]);

print('==> BASE DE DATOS PIZZERIA_DB INICIALIZADA EXITOSAMENTE CON MONGODB <==');
print('Categorías: ' + db.categorias.countDocuments());
print('Pizzas: ' + db.pizzas.countDocuments());
print('Usuarios: ' + db.usuarios.countDocuments());
print('Cupones: ' + db.cupones.countDocuments());
print('Pedidos: ' + db.pedidos.countDocuments());
