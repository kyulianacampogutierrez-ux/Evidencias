// ==============================================================================
// SERVICIO DE COMUNICACIÓN CON BACKEND REST GO + FIBER V2 + MONGODB
// Aprendiz: Karen Yuliana Campo | Ficha: 228118 | ADSO CTPI Popayán
// ==============================================================================

const API_BASE = 'http://localhost:8085/api';

function getAuthHeaders() {
  const token = localStorage.getItem('sena_pizza_jwt');
  const headers = { 'Content-Type': 'application/json' };
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }
  return headers;
}

export const api = {
  // 1. Healthcheck
  async getHealth() {
    const res = await fetch('http://localhost:8085/health');
    return res.json();
  },

  // 2. Carta & Categorías
  async getCategorias() {
    const res = await fetch(`${API_BASE}/categorias`);
    return res.json();
  },

  async getPizzas(categoria = '', q = '', destacadas = false) {
    const params = new URLSearchParams();
    if (categoria) params.append('categoria', categoria);
    if (q) params.append('q', q);
    if (destacadas) params.append('destacadas', 'true');
    const res = await fetch(`${API_BASE}/pizzas?${params.toString()}`);
    return res.json();
  },

  async getPizza(codigo) {
    const res = await fetch(`${API_BASE}/pizzas/${codigo}`);
    return res.json();
  },

  // 3. Autenticación
  async login(usuario, password) {
    const res = await fetch(`${API_BASE}/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ usuario, password }),
    });
    return res.json();
  },

  async register(data) {
    const res = await fetch(`${API_BASE}/auth/register`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });
    return res.json();
  },

  async getProfile() {
    const res = await fetch(`${API_BASE}/auth/profile`, {
      headers: getAuthHeaders(),
    });
    return res.json();
  },

  // 4. Cupones
  async validarCupon(codigo, subtotal) {
    const res = await fetch(`${API_BASE}/cupones/validar`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ codigo, subtotal }),
    });
    return res.json();
  },

  // 5. Pedidos & Tracking
  async crearPedido(datosPedido) {
    const res = await fetch(`${API_BASE}/pedidos`, {
      method: 'POST',
      headers: getAuthHeaders(),
      body: JSON.stringify(datosPedido),
    });
    return res.json();
  },

  async getMisPedidos() {
    const res = await fetch(`${API_BASE}/pedidos/mis-pedidos`, {
      headers: getAuthHeaders(),
    });
    return res.json();
  },

  async getPedido(numero) {
    const res = await fetch(`${API_BASE}/pedidos/${numero}`);
    return res.json();
  },

  // 6. Pasarela de Pagos
  async procesarPago(datosPago) {
    const res = await fetch(`${API_BASE}/pagos/procesar`, {
      method: 'POST',
      headers: getAuthHeaders(),
      body: JSON.stringify(datosPago),
    });
    return res.json();
  },

  // 7. Módulo Administrador
  async getAdminStats() {
    const res = await fetch(`${API_BASE}/admin/dashboard`, {
      headers: getAuthHeaders(),
    });
    return res.json();
  },

  async getAdminPedidos(estado = '') {
    const url = estado ? `${API_BASE}/admin/pedidos?estado=${estado}` : `${API_BASE}/admin/pedidos`;
    const res = await fetch(url, {
      headers: getAuthHeaders(),
    });
    return res.json();
  },

  async actualizarEstadoPedido(numero, estado, nota = '') {
    const res = await fetch(`${API_BASE}/admin/pedidos/${numero}/estado`, {
      method: 'PUT',
      headers: getAuthHeaders(),
      body: JSON.stringify({ estado, nota }),
    });
    return res.json();
  },

  async crearPizza(pizza) {
    const res = await fetch(`${API_BASE}/admin/pizzas`, {
      method: 'POST',
      headers: getAuthHeaders(),
      body: JSON.stringify(pizza),
    });
    return res.json();
  },

  async eliminarPizza(codigo) {
    const res = await fetch(`${API_BASE}/admin/pizzas/${codigo}`, {
      method: 'DELETE',
      headers: getAuthHeaders(),
    });
    return res.json();
  }
};
