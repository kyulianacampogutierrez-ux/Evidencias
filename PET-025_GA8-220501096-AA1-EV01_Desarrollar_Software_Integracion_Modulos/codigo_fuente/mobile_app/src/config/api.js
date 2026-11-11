// Configuración del Endpoint de la API REST para la App Móvil React Native
// Conexión hacia el backend Go Fiber en la red local Wi-Fi (IP de la máquina host)
export const HOST_IP = '192.168.20.21';
export const API_BASE_URL = `http://${HOST_IP}:8085/api`;

export async function fetchPizzasMobile() {
  try {
    const res = await fetch(`${API_BASE_URL}/pizzas`);
    return await res.json();
  } catch (e) {
    console.warn('Error conectando con API:', e.message);
    return { success: false, pizzas: [] };
  }
}

export async function loginMobile(usuario, password) {
  try {
    const res = await fetch(`${API_BASE_URL}/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ usuario, password }),
    });
    return await res.json();
  } catch (e) {
    return { success: false, mensaje: e.message };
  }
}

export async function fetchOrderMobile(numeroPedido) {
  try {
    const res = await fetch(`${API_BASE_URL}/pedidos/${numeroPedido}`);
    return await res.json();
  } catch (e) {
    return { success: false, mensaje: e.message };
  }
}

export async function updateOrderStatusMobile(token, numeroPedido, nuevoEstado) {
  try {
    const res = await fetch(`${API_BASE_URL}/admin/pedidos/${numeroPedido}/estado`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({ estado: nuevoEstado }),
    });
    return await res.json();
  } catch (e) {
    return { success: false, mensaje: e.message };
  }
}
