/**
 * Pizzería Bella Italia - Frontend Application Logic
 * Con Control de Acceso por Roles (RBAC): Cliente vs Administrador
 * Evidencia: GA6-220501096-AA3-EV03
 * Aprendiz: Karen Yuliana Campo
 */

// Catálogo base de pizzas
const PIZZAS = [
  {
    id: 1,
    nombre: 'Pizza Hawaiana',
    tamano: 'Familiar',
    porciones: 8,
    precio: 45000,
    categoria: 'Tradicional',
    colorTheme: 'gold',
    descripcion: 'Jamón dulce ahumado, piña caramelizada en miel orgánica y doble porción de queso mozzarella fundido sobre salsa napolitana artesanal.',
    ingredientes: ['Jamón dulce premium', 'Piña caramelizada', 'Doble queso mozzarella', 'Salsa napolitana de la casa']
  },
  {
    id: 2,
    nombre: 'Pizza Pepperoni',
    tamano: 'Mediana',
    porciones: 6,
    precio: 32000,
    categoria: 'Especial',
    colorTheme: 'red',
    descripcion: 'Pepperoni americano crocante, queso mozzarella de primera calidad, salsa de tomates San Marzano y un toque de orégano silvestre.',
    ingredientes: ['Pepperoni americano', 'Queso mozzarella fundido', 'Orégano silvestre', 'Base fina artesanal']
  },
  {
    id: 3,
    nombre: 'Pizza Pollo & Champiñón',
    tamano: 'Familiar',
    porciones: 8,
    precio: 38000,
    categoria: 'Gourmet',
    colorTheme: 'green',
    descripcion: 'Pechuga de pollo desmechada marinada, champiñones frescos salteados al ajillo, queso parmesano gratinado y salsa bechamel suave.',
    ingredientes: ['Pechuga marinada', 'Champiñones al ajillo', 'Parmesano gratinado', 'Salsa bechamel suave']
  },
  {
    id: 4,
    nombre: 'Pizza Cuatro Quesos',
    tamano: 'Personal',
    porciones: 4,
    precio: 22000,
    categoria: 'Gourmet',
    colorTheme: 'blue',
    descripcion: 'Exquisita combinación de cuatro quesos europeos: mozzarella, gorgonzola, provolone dulce y queso parmesano madurado.',
    ingredientes: ['Mozzarella', 'Gorgonzola italiano', 'Provolone dulce', 'Parmesano madurado']
  }
];

// Cuentas de usuario registradas
const USUARIOS = [
  {
    correo: 'admin@pizzeriabellaitalia.com',
    clave: 'admin123',
    nombre: 'Karen Campo',
    rol: 'Administrador'
  },
  {
    correo: 'carlos@cliente.com',
    clave: 'cliente123',
    nombre: 'Carlos Mendoza',
    rol: 'Cliente'
  }
];

// Estado global de la aplicación
let estadoApp = {
  usuarioActual: null,
  carrito: [],
  categoriaActiva: 'todas',
  busquedaTexto: '',
  filtroEstadoAdmin: 'todas',
  pedidos: JSON.parse(localStorage.getItem('pizzeria_pedidos') || '[]')
};

// ==========================================
// INICIALIZACIÓN
// ==========================================
document.addEventListener('DOMContentLoaded', () => {
  vincularEventos();
  renderizarCatalogo();
  actualizarVistaCarrito();
});

// Función global para chips de demo en el login
window.cargarDemo = function(tipo) {
  const emailInput = document.getElementById('loginEmail');
  const passInput = document.getElementById('loginPassword');
  if (tipo === 'admin') {
    emailInput.value = 'admin@pizzeriabellaitalia.com';
    passInput.value = 'admin123';
  } else {
    emailInput.value = 'carlos@cliente.com';
    passInput.value = 'cliente123';
  }
  mostrarToast(`Credenciales de ${tipo.toUpperCase()} cargadas.`);
};

// ==========================================
// GESTIÓN DE VISTAS (SPA)
// ==========================================
window.mostrarVista = function(vistaId) {
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
  const vistaTarget = document.getElementById(vistaId);
  if (vistaTarget) {
    vistaTarget.classList.add('active');
  }

  // Actualizar botones de la barra de navegación
  document.querySelectorAll('.nav-btn').forEach(btn => {
    if (btn.dataset.view === vistaId) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });

  if (vistaId === 'ordersView') {
    renderizarSeccionOrdenes();
  }

  window.scrollTo({ top: 0, behavior: 'smooth' });
};

// ==========================================
// VINCULACIÓN DE EVENTOS
// ==========================================
function vincularEventos() {
  // Login Form
  const loginForm = document.getElementById('loginForm');
  loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = document.getElementById('loginEmail').value.trim();
    const pass = document.getElementById('loginPassword').value.trim();

    const usuario = USUARIOS.find(u => u.correo.toLowerCase() === email.toLowerCase() && u.clave === pass);
    if (!usuario) {
      mostrarToast('Usuario o contraseña incorrectos.', 'error');
      return;
    }

    iniciarSesion(usuario);
  });

  // Logout
  document.getElementById('btnLogout').addEventListener('click', () => {
    cerrarSesion();
  });

  // Navegación
  document.querySelectorAll('.nav-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      mostrarVista(btn.dataset.view);
    });
  });

  // Filtros de categoría de pizza
  document.querySelectorAll('.filter-btn[data-category]').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.filter-btn[data-category]').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      estadoApp.categoriaActiva = btn.dataset.category;
      renderizarCatalogo();
    });
  });

  // Buscador de pizzas
  const searchInput = document.getElementById('inputSearchPizza');
  searchInput.addEventListener('input', (e) => {
    estadoApp.busquedaTexto = e.target.value.toLowerCase().trim();
    renderizarCatalogo();
  });

  // Formulario de Checkout
  const checkoutForm = document.getElementById('checkoutForm');
  checkoutForm.addEventListener('submit', (e) => {
    e.preventDefault();
    procesarPedido();
  });
}

// ==========================================
// AUTENTICACIÓN Y ADAPTACIÓN POR ROL
// ==========================================
function iniciarSesion(usuario) {
  estadoApp.usuarioActual = usuario;

  // Actualizar perfil de usuario en Navbar
  document.getElementById('userName').textContent = usuario.nombre;
  document.getElementById('userRole').textContent = usuario.rol;
  document.getElementById('userAvatar').textContent = usuario.nombre.split(' ').map(n => n[0]).join('').slice(0, 2);

  // Adaptar textos del Navbar según el Rol
  const navOrdersLabel = document.getElementById('navOrdersLabel');
  if (usuario.rol === 'Administrador') {
    navOrdersLabel.textContent = '📊 Gestión de Órdenes';
  } else {
    navOrdersLabel.textContent = '🛍️ Mis Pedidos';
  }

  // Prellenar datos del cliente en el checkout si es Carlos
  if (usuario.rol === 'Cliente') {
    document.getElementById('clientName').value = usuario.nombre;
    document.getElementById('clientPhone').value = '3101234567';
    document.getElementById('clientAddress').value = 'Calle 12 # 34-56 (Barrio El Prado)';
  }

  document.getElementById('navLinks').style.display = 'flex';
  document.getElementById('userProfile').style.display = 'flex';

  mostrarToast(`¡Bienvenida/o, ${usuario.nombre} (${usuario.rol})!`, 'success');
  mostrarVista('menuView');
}

function cerrarSesion() {
  estadoApp.usuarioActual = null;
  document.getElementById('navLinks').style.display = 'none';
  document.getElementById('userProfile').style.display = 'none';
  mostrarToast('Sesión cerrada correctamente.');
  mostrarVista('loginView');
}

// ==========================================
// RENDERIZADO DEL CATÁLOGO
// ==========================================
function renderizarCatalogo() {
  const grid = document.getElementById('pizzaGrid');
  grid.innerHTML = '';

  const pizzasFiltradas = PIZZAS.filter(pizza => {
    const coincideCategoria = estadoApp.categoriaActiva === 'todas' || pizza.categoria === estadoApp.categoriaActiva;
    const coincideBusqueda = estadoApp.busquedaTexto === '' || 
      pizza.nombre.toLowerCase().includes(estadoApp.busquedaTexto) ||
      pizza.descripcion.toLowerCase().includes(estadoApp.busquedaTexto);
    return coincideCategoria && coincideBusqueda;
  });

  if (pizzasFiltradas.length === 0) {
    grid.innerHTML = `
      <div style="grid-column: 1/-1; text-align: center; padding: 48px; background: #1e293b; border-radius: 16px;">
        <span style="font-size: 3rem;">🔍</span>
        <h3 style="margin-top: 12px;">No se encontraron pizzas</h3>
        <p style="color: #94a3b8;">Prueba con otro término de búsqueda o selecciona otra categoría.</p>
      </div>
    `;
    return;
  }

  pizzasFiltradas.forEach(pizza => {
    const card = document.createElement('article');
    card.className = 'pizza-card';
    card.innerHTML = `
      <div class="card-visual-header ${pizza.colorTheme}">
        <span class="pizza-category-tag">${pizza.categoria}</span>
        <span class="pizza-size-badge">🍕 ${pizza.tamano} (${pizza.porciones} porciones)</span>
      </div>
      <div class="pizza-card-body">
        <h3 class="pizza-title">${pizza.nombre}</h3>
        <p class="pizza-description">${pizza.descripcion}</p>
        <div class="pizza-footer">
          <div class="pizza-price-box">
            <span class="price-label">Precio</span>
            <span class="price-value">$${formatearMoneda(pizza.precio)}</span>
          </div>
          <button class="btn btn-primary" onclick="agregarPizza(${pizza.id})">
            + Agregar al Pedido
          </button>
        </div>
      </div>
    `;
    grid.appendChild(card);
  });
}

// ==========================================
// GESTIÓN DEL CARRITO
// ==========================================
window.agregarPizza = function(id) {
  const pizza = PIZZAS.find(p => p.id === id);
  if (!pizza) return;

  const itemExistente = estadoApp.carrito.find(item => item.id === id);
  if (itemExistente) {
    itemExistente.cantidad++;
  } else {
    estadoApp.carrito.push({
      id: pizza.id,
      nombre: pizza.nombre,
      tamano: pizza.tamano,
      precio: pizza.precio,
      cantidad: 1
    });
  }

  actualizarVistaCarrito();
  mostrarToast(`¡${pizza.nombre} agregada al carrito!`, 'success');
};

window.cambiarCantidad = function(id, delta) {
  const item = estadoApp.carrito.find(i => i.id === id);
  if (!item) return;

  item.cantidad += delta;
  if (item.cantidad <= 0) {
    estadoApp.carrito = estadoApp.carrito.filter(i => i.id !== id);
  }

  actualizarVistaCarrito();
};

window.eliminarItem = function(id) {
  estadoApp.carrito = estadoApp.carrito.filter(i => i.id !== id);
  actualizarVistaCarrito();
  mostrarToast('Producto eliminado del carrito.', 'warning');
};

function actualizarVistaCarrito() {
  const totalItems = estadoApp.carrito.reduce((acc, curr) => acc + curr.cantidad, 0);
  const subtotal = estadoApp.carrito.reduce((acc, curr) => acc + (curr.precio * curr.cantidad), 0);
  const envio = (subtotal === 0 || subtotal >= 80000) ? 0 : 4000;
  const total = subtotal + envio;

  // Actualizar Badge del Navbar
  document.getElementById('cartBadge').textContent = totalItems;

  const listContainer = document.getElementById('cartItemsList');
  document.getElementById('cartCountSubtitle').textContent = `${totalItems} producto${totalItems === 1 ? '' : 's'}`;

  if (estadoApp.carrito.length === 0) {
    listContainer.innerHTML = `
      <div style="text-align: center; padding: 32px; color: #64748b;">
        <span style="font-size: 2.5rem;">🛒</span>
        <p style="margin-top: 8px; font-weight: 600;">El carrito de compras está vacío.</p>
        <button class="btn btn-outline btn-sm" style="margin-top: 12px; color: #0f172a; border-color: #cbd5e1;" onclick="mostrarVista('menuView')">
          Ver Catálogo de Pizzas
        </button>
      </div>
    `;
    document.getElementById('btnConfirmOrder').disabled = true;
  } else {
    document.getElementById('btnConfirmOrder').disabled = false;
    listContainer.innerHTML = '';
    estadoApp.carrito.forEach(item => {
      const row = document.createElement('div');
      row.className = 'cart-item-row';
      row.innerHTML = `
        <div class="cart-item-info">
          <div class="cart-item-name">${item.nombre}</div>
          <div class="cart-item-detail">${item.tamano} • $${formatearMoneda(item.precio)} c/u</div>
        </div>
        <div class="quantity-controls">
          <button class="qty-btn" type="button" onclick="cambiarCantidad(${item.id}, -1)">−</button>
          <span class="qty-number">${item.cantidad}</span>
          <button class="qty-btn" type="button" onclick="cambiarCantidad(${item.id}, 1)">+</button>
        </div>
        <div class="cart-item-subtotal">$${formatearMoneda(item.precio * item.cantidad)}</div>
        <button class="btn-remove-item" type="button" title="Eliminar" onclick="eliminarItem(${item.id})">✕</button>
      `;
      listContainer.appendChild(row);
    });
  }

  // Actualizar cifras
  document.getElementById('summarySubtotal').textContent = `$${formatearMoneda(subtotal)} COP`;
  document.getElementById('summaryShipping').textContent = envio === 0 ? '¡GRATIS!' : `$${formatearMoneda(envio)} COP`;
  document.getElementById('summaryGrandTotal').textContent = `$${formatearMoneda(total)} COP`;

  const freeAlert = document.getElementById('freeShippingAlert');
  if (subtotal >= 80000) {
    freeAlert.style.backgroundColor = '#ecfdf5';
    freeAlert.style.color = '#047857';
    freeAlert.textContent = '🎉 ¡Felicitaciones! Tienes ENVÍO TOTALMENTE GRATIS en esta orden.';
  } else {
    const restante = 80000 - subtotal;
    freeAlert.style.backgroundColor = '#fffbeb';
    freeAlert.style.color = '#b45309';
    freeAlert.textContent = `🛵 ¡Agrega $${formatearMoneda(restante)} COP más para obtener ENVÍO GRATIS!`;
  }
}

// ==========================================
// PROCESAMIENTO DE ORDEN
// ==========================================
function procesarPedido() {
  if (estadoApp.carrito.length === 0) {
    mostrarToast('El carrito está vacío. Agrega una pizza antes de confirmar.', 'error');
    return;
  }

  const nombre = document.getElementById('clientName').value.trim();
  const telefono = document.getElementById('clientPhone').value.trim();
  const direccion = document.getElementById('clientAddress').value.trim();
  const notas = document.getElementById('clientNotes').value.trim();
  const metodoPago = document.querySelector('input[name="paymentMethod"]:checked').value;

  const subtotal = estadoApp.carrito.reduce((acc, curr) => acc + (curr.precio * curr.cantidad), 0);
  const envio = subtotal >= 80000 ? 0 : 4000;
  const total = subtotal + envio;
  const idOrden = `ORD-${Date.now().toString().slice(-6)}`;

  const nuevaOrden = {
    id: idOrden,
    fecha: new Date().toLocaleString('es-CO'),
    cliente: {
      nombre,
      telefono,
      direccion,
      notas,
      correo: estadoApp.usuarioActual?.correo || 'carlos@cliente.com'
    },
    metodoPago,
    items: [...estadoApp.carrito],
    subtotal,
    envio,
    total,
    estado: 'En Preparación'
  };

  // Guardar en estado persistente
  estadoApp.pedidos.unshift(nuevaOrden);
  localStorage.setItem('pizzeria_pedidos', JSON.stringify(estadoApp.pedidos));

  // Vaciar carrito
  estadoApp.carrito = [];
  actualizarVistaCarrito();

  // Abrir Modal de Éxito
  abrirModalExito(nuevaOrden);
}

function abrirModalExito(orden) {
  document.getElementById('modalOrderId').textContent = orden.id;
  document.getElementById('modalDeliveryDetails').textContent = `Destino: ${orden.cliente.direccion} • Cliente: ${orden.cliente.nombre} • Tel: ${orden.cliente.telefono}`;
  document.getElementById('modalOrderTotal').textContent = `$${formatearMoneda(orden.total)} COP`;

  document.getElementById('orderSuccessModal').classList.add('active');
}

window.cerrarModalYVerPedidos = function() {
  document.getElementById('orderSuccessModal').classList.remove('active');
  mostrarVista('ordersView');
};

window.cerrarModalYVolverMenu = function() {
  document.getElementById('orderSuccessModal').classList.remove('active');
  mostrarVista('menuView');
};

// ==========================================
// GESTIÓN DE ÓRDENES POR ROL (CLIENTE VS ADMIN)
// ==========================================
function renderizarSeccionOrdenes() {
  const esAdmin = estadoApp.usuarioActual && estadoApp.usuarioActual.rol === 'Administrador';
  const kpiGrid = document.getElementById('adminKpiGrid');
  const adminFilterBar = document.getElementById('adminFilterBar');
  const title = document.getElementById('ordersViewTitle');
  const subtitle = document.getElementById('ordersViewSubtitle');
  const container = document.getElementById('ordersList');

  // Ajustes de visualización según el rol
  if (esAdmin) {
    title.textContent = '📊 Panel de Control: Gestión de Órdenes';
    subtitle.textContent = 'Manejo central de pedidos, asignación de cocina y despachos en tiempo real.';
    kpiGrid.style.display = 'grid';
    adminFilterBar.style.display = 'flex';
    actualizarMetricasKPI();
  } else {
    title.textContent = '🛍️ Mis Pedidos Realizados';
    subtitle.textContent = 'Seguimiento y estado de entrega de tus pizzas.';
    kpiGrid.style.display = 'none';
    adminFilterBar.style.display = 'none';
  }

  // Filtrar pedidos según rol
  let ordenesParaMostrar = [];
  if (esAdmin) {
    // Admin ve todo, con filtro opcional de estado
    if (estadoApp.filtroEstadoAdmin === 'todas') {
      ordenesParaMostrar = [...estadoApp.pedidos];
    } else {
      ordenesParaMostrar = estadoApp.pedidos.filter(p => (p.estado || '').includes(estadoApp.filtroEstadoAdmin));
    }
  } else {
    // Cliente solo ve sus propios pedidos
    const correoUsuario = estadoApp.usuarioActual?.correo?.toLowerCase();
    const nombreUsuario = estadoApp.usuarioActual?.nombre?.toLowerCase();
    ordenesParaMostrar = estadoApp.pedidos.filter(p => {
      const matchCorreo = p.cliente.correo && p.cliente.correo.toLowerCase() === correoUsuario;
      const matchNombre = p.cliente.nombre && p.cliente.nombre.toLowerCase() === nombreUsuario;
      return matchCorreo || matchNombre;
    });
  }

  container.innerHTML = '';

  if (ordenesParaMostrar.length === 0) {
    container.innerHTML = `
      <div style="text-align: center; padding: 48px; background: #1e293b; border-radius: 16px;">
        <span style="font-size: 3rem;">${esAdmin ? '📦' : '🛍️'}</span>
        <h3 style="margin-top: 12px;">${esAdmin ? 'No hay órdenes en esta categoría' : 'Aún no has realizado pedidos'}</h3>
        <p style="color: #94a3b8;">${esAdmin ? 'Las nuevas órdenes de los clientes se reflejarán aquí automáticamente.' : 'Explora nuestro catálogo y ordena tu pizza artesanal favorita.'}</p>
        ${!esAdmin ? '<button class="btn btn-primary" style="margin-top: 16px;" onclick="mostrarVista(\'menuView\')">Ver Menú</button>' : ''}
      </div>
    `;
    return;
  }

  ordenesParaMostrar.forEach(p => {
    const card = document.createElement('div');
    const estadoClass = obtenerClaseEstado(p.estado);
    card.className = `order-history-card ${estadoClass}`;

    const itemsResumen = p.items.map(i => `<span style="display: inline-block; background: #f1f5f9; padding: 2px 8px; border-radius: 6px; margin: 2px; font-weight: 600;">${i.cantidad}x ${i.nombre}</span>`).join(' ');

    let controlesAdminHtml = '';
    if (esAdmin) {
      controlesAdminHtml = `
        <div class="order-admin-controls">
          <span class="control-label">⚙️ Cambiar Estado (Admin):</span>
          <div class="status-actions-btns">
            <button class="btn-status-step ${p.estado === 'En Preparación' ? 'active' : ''}" onclick="cambiarEstadoOrden('${p.id}', 'En Preparación')">
              👨‍🍳 Cocina
            </button>
            <button class="btn-status-step ${p.estado === 'En Camino' ? 'active' : ''}" onclick="cambiarEstadoOrden('${p.id}', 'En Camino')">
              🛵 Despachar
            </button>
            <button class="btn-status-step ${p.estado === 'Entregado' ? 'active' : ''}" onclick="cambiarEstadoOrden('${p.id}', 'Entregado')">
              ✅ Entregar
            </button>
          </div>
        </div>
      `;
    }

    card.innerHTML = `
      <div style="flex: 1; min-width: 280px;">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 6px;">
          <strong style="font-size: 1.15rem; color: #0f172a;">${p.id}</strong>
          <span class="order-badge-status badge-${obtenerBadgeClass(p.estado)}">
            ${obtenerIconoEstado(p.estado)} ${p.estado}
          </span>
        </div>
        <small style="color: #64748b; display: block; margin-bottom: 8px;">
          📅 ${p.fecha} • Método de Pago: <strong>${p.metodoPago}</strong>
        </small>
        <div style="margin: 8px 0;">
          <span style="font-size: 0.8rem; font-weight: 700; color: #64748b; text-transform: uppercase;">Pizzas ordenadas:</span>
          <div style="margin-top: 4px;">${itemsResumen}</div>
        </div>
        <div style="font-size: 0.85rem; color: #334155; margin-top: 8px;">
          📍 <strong>Envío a:</strong> ${p.cliente.direccion} 
          <span style="color: #64748b;">(Cliente: ${p.cliente.nombre} • Tel: ${p.cliente.telefono})</span>
        </div>
        ${p.cliente.notas ? `<div style="font-size: 0.8rem; color: #d97706; margin-top: 4px; font-style: italic;">📝 Nota: "${p.cliente.notas}"</div>` : ''}
      </div>

      <div style="display: flex; flex-direction: column; align-items: flex-end; gap: 12px;">
        <div style="text-align: right;">
          <span style="font-size: 0.75rem; text-transform: uppercase; color: #64748b; font-weight: 800;">Total Facturado</span>
          <div style="font-family: var(--font-heading); font-size: 1.45rem; font-weight: 800; color: #e11d48;">
            $${formatearMoneda(p.total)} COP
          </div>
        </div>
        ${controlesAdminHtml}
      </div>
    `;

    container.appendChild(card);
  });
}

function actualizarMetricasKPI() {
  const totalFacturado = estadoApp.pedidos.reduce((acc, curr) => acc + curr.total, 0);
  const totalOrdenes = estadoApp.pedidos.length;
  const enPrep = estadoApp.pedidos.filter(p => (p.estado || '').includes('Preparación')).length;
  const enCamino = estadoApp.pedidos.filter(p => (p.estado || '').includes('Camino')).length;
  const entregadas = estadoApp.pedidos.filter(p => (p.estado || '').includes('Entregado')).length;

  document.getElementById('kpiTotalRevenue').textContent = `$${formatearMoneda(totalFacturado)} COP`;
  document.getElementById('kpiTotalOrders').textContent = totalOrdenes;
  document.getElementById('kpiPrepOrders').textContent = enPrep;
  document.getElementById('kpiShippingOrders').textContent = enCamino;
  document.getElementById('kpiDeliveredOrders').textContent = entregadas;
}

window.filtrarOrdenesAdmin = function(estado, btn) {
  document.querySelectorAll('#adminFilterBar .filter-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  estadoApp.filtroEstadoAdmin = estado;
  renderizarSeccionOrdenes();
};

window.cambiarEstadoOrden = function(idOrden, nuevoEstado) {
  const orden = estadoApp.pedidos.find(o => o.id === idOrden);
  if (!orden) return;

  orden.estado = nuevoEstado;
  localStorage.setItem('pizzeria_pedidos', JSON.stringify(estadoApp.pedidos));

  mostrarToast(`Orden ${idOrden} actualizada a: ${nuevoEstado}`, 'success');
  renderizarSeccionOrdenes();
};

function obtenerClaseEstado(estado) {
  if (estado.includes('Preparación')) return 'status-preparacion';
  if (estado.includes('Camino')) return 'status-camino';
  if (estado.includes('Entregado')) return 'status-entregado';
  return '';
}

function obtenerBadgeClass(estado) {
  if (estado.includes('Preparación')) return 'preparacion';
  if (estado.includes('Camino')) return 'camino';
  if (estado.includes('Entregado')) return 'entregado';
  return 'preparacion';
}

function obtenerIconoEstado(estado) {
  if (estado.includes('Preparación')) return '👨‍🍳';
  if (estado.includes('Camino')) return '🛵';
  if (estado.includes('Entregado')) return '✅';
  return '📦';
}

// ==========================================
// UTILIDADES
// ==========================================
function formatearMoneda(valor) {
  return valor.toLocaleString('es-CO');
}

function mostrarToast(mensaje, tipo = 'default') {
  const toast = document.getElementById('toast');
  toast.textContent = mensaje;
  toast.className = `toast show ${tipo}`;
  setTimeout(() => {
    toast.className = 'toast';
  }, 3200);
}
