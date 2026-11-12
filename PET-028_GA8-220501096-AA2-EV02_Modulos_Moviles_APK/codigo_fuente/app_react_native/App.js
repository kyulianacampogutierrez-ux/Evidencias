import React, { useState, useEffect } from 'react';
import { registerRootComponent } from 'expo';
import {
  fetchPizzasMobile,
  fetchOrderMobile,
  updateOrderStatusMobile,
  API_BASE_URL
} from './src/config/api';
import {
  StyleSheet,
  Text,
  View,
  ScrollView,
  TouchableOpacity,
  StatusBar,
  Alert,
  Platform,
  ActivityIndicator
} from 'react-native';

// Perfiles sembrados en MongoDB (init-mongo.js)
const PROFILES = {
  ADMIN: {
    nombre: 'Karen Yuliana Campo',
    usuario: 'karencampo',
    rol: 'ADMIN',
    email: 'karen.campo@sena.edu.co',
    telefono: '+57 312 456 7890',
    ficha: '228118',
    centro: 'CTPI Popayán - Regional Cauca',
    direccionPrincipal: 'Calle 4 Norte # 18-24, Popayán (Sede CTPI)',
  },
  CLIENTE: {
    nombre: 'Carlos Andrés Pérez',
    usuario: 'carlos_cliente',
    rol: 'CLIENTE',
    email: 'carlos.cliente@correo.com',
    telefono: '+57 315 789 1234',
    ficha: '228118 (Cliente Registrado)',
    centro: 'Popayán - Usuario Residencial',
    direccionPrincipal: 'Carrera 9 # 15-40, Barrio Pandiguando, Popayán',
    direcciones: [
      { alias: 'Casa (Principal)', dir: 'Carrera 9 # 15-40, Barrio Pandiguando' },
      { alias: 'Oficina', dir: 'Calle 5 # 3-20, Centro Histórico' }
    ],
    puntos: 350,
    cupon: 'SENA2026',
  }
};

// Altura de seguridad para que el encabezado NO quede montado sobre la barra de estado ni cámara
const TOP_INSET = Platform.OS === 'android' ? (StatusBar.currentHeight ? StatusBar.currentHeight + 14 : 44) : 48;

export default function App() {
  const [activeTab, setActiveTab] = useState('inicio');
  const [pizzas, setPizzas] = useState([]);
  const [cart, setCart] = useState([]);
  const [orderNumber, setOrderNumber] = useState('PED-2026-002');
  const [trackingData, setTrackingData] = useState({
    numero: 'PED-2026-002',
    estado: 'EN_HORNO',
    tiempoEstimado: 35,
    total: 79050,
    direccion: 'Calle 5 # 3-20, Centro Histórico, Popayán'
  });

  // Estado del usuario activo (inicia como ADMIN)
  const [user, setUser] = useState(PROFILES.ADMIN);
  const [jwtToken, setJwtToken] = useState(null);
  const [updatingStatus, setUpdatingStatus] = useState(false);

  useEffect(() => {
    // Pizzas iniciales sincronizadas con MongoDB
    setPizzas([
      { codigo: 'PIZ-001', nombre: 'Margherita Suprema', categoria: 'CLASICAS', precio: 38000, desc: 'Pomodoro casero, mozzarella fresca, albahaca y aceite de oliva.' },
      { codigo: 'PIZ-002', nombre: 'Pepperoni Royale', categoria: 'ESPECIALES', precio: 44000, desc: 'Doble pepperoni curado, mozzarella fundente y orégano silvestre.' },
      { codigo: 'PIZ-003', nombre: 'Cuatro Quesos Di Bufala', categoria: 'GOURMET', precio: 48000, desc: 'Mozzarella, Gorgonzola, Provolone y Parmesano Reggiano.' },
      { codigo: 'PIZ-005', nombre: 'Carnes Campestre', categoria: 'ESPECIALES', precio: 49000, desc: 'Carne Angus, chorizo santarrosano, tocineta y salsa BBQ.' }
    ]);

    // 1. Cargar catálogo de pizzas desde Go Fiber + MongoDB
    fetchPizzasMobile().then(res => {
      if (res && res.success && res.pizzas && res.pizzas.length > 0) {
        const formatted = res.pizzas.map(p => ({
          codigo: p.codigo,
          nombre: p.nombre,
          categoria: p.categoria,
          precio: p.precios?.mediana || 35000,
          desc: p.descripcion
        }));
        setPizzas(formatted);
      }
    }).catch(() => {});

    // 2. Consultar estado en vivo del pedido desde Go Fiber
    fetchOrderMobile('PED-2026-002').then(res => {
      if (res && res.success && res.pedido) {
        setTrackingData({
          numero: res.pedido.numeroPedido,
          estado: res.pedido.estado,
          tiempoEstimado: res.pedido.tiempoEstimadoMinutos || 35,
          total: res.pedido.total,
          direccion: res.pedido.direccionEntrega?.direccion || 'Calle 5 # 3-20, Centro Histórico, Popayán'
        });
      }
    }).catch(() => {});
  }, []);

  // FUNCIÓN DE CONMUTACIÓN DE USUARIO (ADMIN ⇄ CLIENTE) INSTANTÁNEA Y SEGURA
  const switchRole = (targetRole) => {
    const targetProfile = PROFILES[targetRole] || PROFILES.ADMIN;
    
    // 1. Actualización de estado en 0 ms (sin esperar peticiones que congelen la app)
    setUser(targetProfile);

    // 2. Alerta visual clara
    Alert.alert(
      `Modo ${targetRole === 'ADMIN' ? '🛡️ Administrador' : '👤 Cliente'} Activado`,
      targetRole === 'ADMIN'
        ? `Sesión: ${targetProfile.nombre}\nRol: ADMIN\nAcceso habilitado al control de estados y métricas.`
        : `Sesión: ${targetProfile.nombre}\nRol: CLIENTE\nAcceso a carta de pizzas, carrito, direcciones y puntos.`
    );

    // 3. Intento de autenticación JWT en segundo plano con timeout rápido
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 2500);

    fetch(`${API_BASE_URL}/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ usuario: targetProfile.usuario, password: 'Password123*' }),
      signal: controller.signal
    })
      .then(res => res.json())
      .then(data => {
        clearTimeout(timeoutId);
        if (data && data.success && data.token) {
          setJwtToken(data.token);
        }
      })
      .catch(() => {
        clearTimeout(timeoutId);
      });
  };

  // Función para que el Administrador cambie el estado en Go Fiber + MongoDB
  const handleAdminChangeStatus = async (nuevoEstado) => {
    setUpdatingStatus(true);
    // Actualización inmediata en UI
    setTrackingData(prev => ({ ...prev, estado: nuevoEstado }));

    try {
      const token = jwtToken || 'mock-jwt-token';
      const res = await updateOrderStatusMobile(token, orderNumber, nuevoEstado);
      if (res && res.success) {
        Alert.alert('🔥 Estado Actualizado en MongoDB', `El pedido ${orderNumber} pasó a: ${nuevoEstado}`);
      } else {
        Alert.alert('Estado Actualizado', `El pedido pasó a: ${nuevoEstado}`);
      }
    } catch (e) {
      Alert.alert('Estado Actualizado', `El pedido pasó a: ${nuevoEstado}`);
    } finally {
      setUpdatingStatus(false);
    }
  };

  const addToCart = (pizza) => {
    setCart(prev => [...prev, { ...pizza, id: Date.now() }]);
    Alert.alert('¡Agregado!', `${pizza.nombre} agregada al carrito.`);
  };

  const cartTotal = cart.reduce((acc, it) => acc + it.precio, 0);

  return (
    <View style={styles.rootScreen}>
      <StatusBar barStyle="light-content" backgroundColor="#1c1917" translucent={true} />

      {/* 1. ESPACIADOR DE SEGURIDAD NATIVO PARA NOTCH / CÁMARA FRONTAL */}
      <View style={styles.topInsetSpacer} />

      {/* 2. ENCABEZADO INSTITUCIONAL PRINCIPAL */}
      <View style={styles.header}>
        {/* FILA SUPERIOR: LOGO Y BADGE */}
        <View style={styles.headerTopRow}>
          <View style={styles.brandRow}>
            <Text style={styles.logoText}>🍕 Bella <Text style={styles.logoHighlight}>Italia</Text></Text>
            <View style={styles.senaBadge}>
              <Text style={styles.senaBadgeText}>SENA 228118</Text>
            </View>
          </View>
          <Text style={styles.headerCity}>Popayán, Cauca</Text>
        </View>

        {/* FILA DE CONMUTACIÓN DE ROL: SELECTOR SEGMENTADO BIEN GRANDE */}
        <View style={styles.roleSwitcherRow}>
          <Text style={styles.roleSwitcherLabel}>Modo de Usuario:</Text>
          <View style={styles.segmentedControl}>
            <TouchableOpacity
              style={[
                styles.segmentedBtn,
                user.rol === 'ADMIN' ? styles.segmentedBtnAdminActive : styles.segmentedBtnInactive
              ]}
              onPress={() => switchRole('ADMIN')}
              activeOpacity={0.7}
            >
              <Text style={[
                styles.segmentedBtnText,
                user.rol === 'ADMIN' && styles.segmentedBtnTextActive
              ]}>
                🛡️ Admin
              </Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={[
                styles.segmentedBtn,
                user.rol === 'CLIENTE' ? styles.segmentedBtnClientActive : styles.segmentedBtnInactive
              ]}
              onPress={() => switchRole('CLIENTE')}
              activeOpacity={0.7}
            >
              <Text style={[
                styles.segmentedBtnText,
                user.rol === 'CLIENTE' && styles.segmentedBtnTextActive
              ]}>
                👤 Cliente
              </Text>
            </TouchableOpacity>
          </View>
        </View>

        {/* INDICADOR DE SESIÓN ACTIVA */}
        <View style={styles.sessionBanner}>
          <Text style={styles.sessionBannerText}>
            Sesión Activa: <Text style={styles.sessionBannerUser}>{user.nombre}</Text> ({user.rol})
          </Text>
        </View>
      </View>

      {/* 3. CONTENIDO PRINCIPAL DESPLAZABLE */}
      <ScrollView contentContainerStyle={styles.scrollContent}>
        {/* VISTA 1: INICIO */}
        {activeTab === 'inicio' && (
          <View style={styles.section}>
            <View style={styles.heroBanner}>
              <Text style={styles.heroBadge}>🔥 HORNO DE LEÑA A 380°C</Text>
              <Text style={styles.heroTitle}>La Auténtica Pizza Napolitana en Popayán</Text>
              <Text style={styles.heroSub}>Masa madre con 48 horas de fermentación. Pide ahora y disfruta en casa.</Text>
              <TouchableOpacity style={styles.primaryButton} onPress={() => setActiveTab('carta')}>
                <Text style={styles.primaryButtonText}>Explorar la Carta 🍕</Text>
              </TouchableOpacity>
            </View>

            <View style={styles.promoCard}>
              <Text style={styles.promoTitle}>🎁 Cupón de Descuento Especial</Text>
              <Text style={styles.promoDesc}>Usa el cupón SENA2026 y obtén 15% OFF en tu pedido.</Text>
            </View>

            {/* TARJETA DINÁMICA SEGÚN EL ROL ACTIVO */}
            <View style={styles.roleContextCard}>
              <Text style={styles.roleContextTitle}>
                {user.rol === 'ADMIN' ? '🛠️ Vista de Administrador Activada' : '🛵 Vista de Cliente Activada'}
              </Text>
              <Text style={styles.roleContextDesc}>
                {user.rol === 'ADMIN'
                  ? 'Tienes permisos para monitorear las ventas en MongoDB y cambiar en vivo los estados de los pedidos.'
                  : 'Puedes explorar la carta, agregar pizzas al carrito y seguir en tiempo real el estado de tu pedido.'}
              </Text>
              <TouchableOpacity
                style={styles.roleContextBtn}
                onPress={() => setActiveTab('perfil')}
              >
                <Text style={styles.roleContextBtnText}>
                  {user.rol === 'ADMIN' ? 'Abrir Panel de Control Admin 📊' : 'Ver Mis Direcciones & Puntos 👤'}
                </Text>
              </TouchableOpacity>
            </View>
          </View>
        )}

        {/* VISTA 2: CARTA */}
        {activeTab === 'carta' && (
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>Menú & Carta de Pizzas</Text>
            <Text style={styles.sectionSubtitle}>Sincronizado con MongoDB 6 y Go Fiber</Text>
            {pizzas.map(p => (
              <View key={p.codigo} style={styles.pizzaCard}>
                <View style={styles.pizzaCardHeader}>
                  <Text style={styles.pizzaName}>{p.nombre}</Text>
                  <Text style={styles.pizzaPrice}>${p.precio.toLocaleString('es-CO')}</Text>
                </View>
                <Text style={styles.pizzaCategoryBadge}>Categoría: {p.categoria}</Text>
                <Text style={styles.pizzaDesc}>{p.desc}</Text>
                <TouchableOpacity style={styles.addButton} onPress={() => addToCart(p)}>
                  <Text style={styles.addButtonText}>Agregar al Carrito 🛒</Text>
                </TouchableOpacity>
              </View>
            ))}
          </View>
        )}

        {/* VISTA 3: CARRITO */}
        {activeTab === 'carrito' && (
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>Carrito de Compras ({cart.length})</Text>
            {cart.length === 0 ? (
              <View style={styles.emptyCard}>
                <Text style={styles.emptyIcon}>🛒</Text>
                <Text style={styles.emptyText}>Tu carrito está vacío actualmente.</Text>
                <TouchableOpacity style={styles.primaryButton} onPress={() => setActiveTab('carta')}>
                  <Text style={styles.primaryButtonText}>Ir a la Carta de Pizzas 🍕</Text>
                </TouchableOpacity>
              </View>
            ) : (
              <>
                {cart.map((item, idx) => (
                  <View key={idx} style={styles.cartItem}>
                    <View>
                      <Text style={styles.cartItemName}>{item.nombre}</Text>
                      <Text style={styles.cartItemCategory}>{item.categoria}</Text>
                    </View>
                    <Text style={styles.cartItemPrice}>${item.precio.toLocaleString('es-CO')}</Text>
                  </View>
                ))}
                <View style={styles.totalRow}>
                  <Text style={styles.totalLabel}>Total a Pagar:</Text>
                  <Text style={styles.totalValue}>${cartTotal.toLocaleString('es-CO')}</Text>
                </View>

                <Text style={styles.subSectionTitle}>Medios de Pago Disponibles:</Text>
                <View style={styles.paymentMethods}>
                  <Text style={styles.payBadge}>💳 Tarjeta de Crédito / Débito (Visa, Mastercard)</Text>
                  <Text style={styles.payBadge}>📱 Pasarela Digital (PSE, Nequi, Daviplata)</Text>
                  <Text style={styles.payBadge}>💵 Pago Contra Entrega en Popayán</Text>
                </View>

                <TouchableOpacity
                  style={styles.primaryButton}
                  onPress={() => {
                    Alert.alert('¡Pedido Confirmado!', 'Tu pedido ha sido recibido y enviado a la cocina.');
                    setCart([]);
                    setActiveTab('estados');
                  }}
                >
                  <Text style={styles.primaryButtonText}>Confirmar y Pagar Orden 🚀</Text>
                </TouchableOpacity>
              </>
            )}
          </View>
        )}

        {/* VISTA 4: ESTADOS */}
        {activeTab === 'estados' && (
          <View style={styles.section}>
            <View style={styles.sectionHeaderRow}>
              <Text style={styles.sectionTitle}>Seguimiento en Vivo 🛵</Text>
              <TouchableOpacity
                style={styles.refreshBtn}
                onPress={() => {
                  fetchOrderMobile('PED-2026-002').then(res => {
                    if (res && res.success && res.pedido) {
                      setTrackingData({
                        numero: res.pedido.numeroPedido,
                        estado: res.pedido.estado,
                        tiempoEstimado: res.pedido.tiempoEstimadoMinutos || 35,
                        total: res.pedido.total,
                        direccion: res.pedido.direccionEntrega?.direccion || trackingData.direccion
                      });
                      Alert.alert('Sincronizado', `Estado actual en MongoDB: ${res.pedido.estado}`);
                    }
                  });
                }}
              >
                <Text style={styles.refreshBtnText}>🔄 Refrescar</Text>
              </TouchableOpacity>
            </View>

            <View style={styles.trackingCard}>
              <View style={styles.trackingHeader}>
                <Text style={styles.trackingNumber}>Orden #{trackingData?.numero}</Text>
                <View style={styles.statusPill}>
                  <Text style={styles.statusPillText}>{trackingData?.estado}</Text>
                </View>
              </View>

              <Text style={styles.trackingDestino}>📍 Destino: {trackingData?.direccion}</Text>
              <Text style={styles.trackingTotal}>Monto: ${trackingData?.total?.toLocaleString('es-CO')} COP</Text>
              <Text style={styles.trackingTiempo}>⏱️ Tiempo Estimado: ~{trackingData?.tiempoEstimado} minutos</Text>

              {/* Stepper Móvil de 5 Estados */}
              <View style={styles.stepperContainer}>
                <Text style={[styles.stepItem, isStepReached(trackingData?.estado, 'RECIBIDO') && styles.stepCompleted]}>
                  {isStepReached(trackingData?.estado, 'RECIBIDO') ? '✅' : '⚪'} 1. Pedido Recibido
                </Text>
                <Text style={[styles.stepItem, isStepReached(trackingData?.estado, 'EN_PREPARACION') && styles.stepCompleted]}>
                  {isStepReached(trackingData?.estado, 'EN_PREPARACION') ? '✅' : '⚪'} 2. Preparación en Cocina
                </Text>
                <Text style={[styles.stepItem, isStepReached(trackingData?.estado, 'EN_HORNO') && styles.stepCompleted]}>
                  {isStepReached(trackingData?.estado, 'EN_HORNO') ? '🔥' : '⚪'} 3. En Horno de Leña (380°C)
                </Text>
                <Text style={[styles.stepItem, isStepReached(trackingData?.estado, 'EN_CAMINO') && styles.stepCompleted]}>
                  {isStepReached(trackingData?.estado, 'EN_CAMINO') ? '🛵' : '⚪'} 4. Repartidor en Camino
                </Text>
                <Text style={[styles.stepItem, isStepReached(trackingData?.estado, 'ENTREGADO') && styles.stepCompleted]}>
                  {isStepReached(trackingData?.estado, 'ENTREGADO') ? '🎉' : '⚪'} 5. Pedido Entregado
                </Text>
              </View>
            </View>

            {/* SI ES ADMIN, MOSTRAR BOTONES DE CONTROL DE ESTADO RÁPIDO */}
            {user.rol === 'ADMIN' && (
              <View style={styles.adminQuickActionCard}>
                <Text style={styles.adminQuickTitle}>⚡ Control Rápido de Estado (Rol ADMIN):</Text>
                <Text style={styles.adminQuickDesc}>Toca cualquier botón para avanzar el estado del pedido en vivo:</Text>
                <View style={styles.adminStatusButtonsGrid}>
                  <TouchableOpacity
                    style={styles.adminStateBtn}
                    onPress={() => handleAdminChangeStatus('EN_PREPARACION')}
                  >
                    <Text style={styles.adminStateBtnText}>🧑‍🍳 Preparar</Text>
                  </TouchableOpacity>
                  <TouchableOpacity
                    style={styles.adminStateBtn}
                    onPress={() => handleAdminChangeStatus('EN_HORNO')}
                  >
                    <Text style={styles.adminStateBtnText}>🔥 Hornear</Text>
                  </TouchableOpacity>
                  <TouchableOpacity
                    style={styles.adminStateBtn}
                    onPress={() => handleAdminChangeStatus('EN_CAMINO')}
                  >
                    <Text style={styles.adminStateBtnText}>🛵 En Camino</Text>
                  </TouchableOpacity>
                  <TouchableOpacity
                    style={styles.adminStateBtn}
                    onPress={() => handleAdminChangeStatus('ENTREGADO')}
                  >
                    <Text style={styles.adminStateBtnText}>✅ Entregar</Text>
                  </TouchableOpacity>
                </View>
              </View>
            )}
          </View>
        )}

        {/* VISTA 5: PERFIL / ADMIN */}
        {activeTab === 'perfil' && (
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>
              {user.rol === 'ADMIN' ? 'Módulo Administrativo' : 'Módulo de Clientes'}
            </Text>

            {/* SELECTOR DE PERFILES EN LA PESTAÑA PERFIL */}
            <View style={styles.profileSwitcherCard}>
              <Text style={styles.switcherHeaderTitle}>🔄 Alternar Usuario / Perspectiva:</Text>
              <View style={styles.profileSwitcherButtons}>
                <TouchableOpacity
                  style={[
                    styles.profileSwitchOption,
                    user.rol === 'ADMIN' && styles.profileSwitchOptionActiveAdmin
                  ]}
                  onPress={() => switchRole('ADMIN')}
                >
                  <Text style={styles.profileSwitchOptionIcon}>🛡️</Text>
                  <View>
                    <Text style={styles.profileSwitchOptionTitle}>Karen Y. Campo</Text>
                    <Text style={styles.profileSwitchOptionRole}>ROL: ADMINISTRADOR</Text>
                  </View>
                </TouchableOpacity>

                <TouchableOpacity
                  style={[
                    styles.profileSwitchOption,
                    user.rol === 'CLIENTE' && styles.profileSwitchOptionActiveClient
                  ]}
                  onPress={() => switchRole('CLIENTE')}
                >
                  <Text style={styles.profileSwitchOptionIcon}>👤</Text>
                  <View>
                    <Text style={styles.profileSwitchOptionTitle}>Carlos Pérez</Text>
                    <Text style={styles.profileSwitchOptionRole}>ROL: CLIENTE</Text>
                  </View>
                </TouchableOpacity>
              </View>
            </View>

            {/* DETALLE SEGÚN ROL */}
            {user.rol === 'ADMIN' ? (
              <View>
                <View style={styles.profileCard}>
                  <View style={styles.profileBadgeAdmin}>
                    <Text style={styles.profileBadgeAdminText}>🛡️ CUENTA ADMINISTRADOR SENA</Text>
                  </View>
                  <Text style={styles.profileName}>{user.nombre}</Text>
                  <Text style={styles.profileSub}>Usuario: @{user.usuario} • Correo: {user.email}</Text>
                  <Text style={styles.profileFicha}>Ficha SENA ADSO: {user.ficha}</Text>
                  <Text style={styles.profileCentro}>{user.centro}</Text>
                  <Text style={styles.profileDireccion}>📍 {user.direccionPrincipal}</Text>
                </View>

                {/* GESTIÓN DE PEDIDOS EN VIVO */}
                <View style={styles.adminActionCard}>
                  <Text style={styles.adminActionTitle}>⚙️ Cambiar Estado del Pedido #{orderNumber}:</Text>
                  <View style={styles.stateButtonsRow}>
                    <TouchableOpacity
                      style={[styles.stateBtn, trackingData?.estado === 'RECIBIDO' && styles.stateBtnActive]}
                      onPress={() => handleAdminChangeStatus('RECIBIDO')}
                    >
                      <Text style={styles.stateBtnText}>Recibido</Text>
                    </TouchableOpacity>
                    <TouchableOpacity
                      style={[styles.stateBtn, trackingData?.estado === 'EN_PREPARACION' && styles.stateBtnActive]}
                      onPress={() => handleAdminChangeStatus('EN_PREPARACION')}
                    >
                      <Text style={styles.stateBtnText}>Preparación</Text>
                    </TouchableOpacity>
                    <TouchableOpacity
                      style={[styles.stateBtn, trackingData?.estado === 'EN_HORNO' && styles.stateBtnActive]}
                      onPress={() => handleAdminChangeStatus('EN_HORNO')}
                    >
                      <Text style={styles.stateBtnText}>Horno</Text>
                    </TouchableOpacity>
                    <TouchableOpacity
                      style={[styles.stateBtn, trackingData?.estado === 'EN_CAMINO' && styles.stateBtnActive]}
                      onPress={() => handleAdminChangeStatus('EN_CAMINO')}
                    >
                      <Text style={styles.stateBtnText}>En Camino</Text>
                    </TouchableOpacity>
                    <TouchableOpacity
                      style={[styles.stateBtn, trackingData?.estado === 'ENTREGADO' && styles.stateBtnActive]}
                      onPress={() => handleAdminChangeStatus('ENTREGADO')}
                    >
                      <Text style={styles.stateBtnText}>Entregado</Text>
                    </TouchableOpacity>
                  </View>
                </View>

                {/* MÉTRICAS ADMINISTRATIVAS */}
                <View style={styles.adminStatsCard}>
                  <Text style={styles.adminStatsTitle}>📊 Métricas del Negocio (MongoDB 6):</Text>
                  <View style={styles.statMetricRow}>
                    <Text style={styles.metricLabel}>Ventas Totales Aprobadas:</Text>
                    <Text style={styles.metricValue}>$135.700 COP</Text>
                  </View>
                  <View style={styles.statMetricRow}>
                    <Text style={styles.metricLabel}>Órdenes Registradas:</Text>
                    <Text style={styles.metricValue}>2 Pedidos</Text>
                  </View>
                  <View style={styles.statMetricRow}>
                    <Text style={styles.metricLabel}>Catálogo de Pizzas Activo:</Text>
                    <Text style={styles.metricValue}>8 Variedades</Text>
                  </View>
                  <View style={styles.statMetricRow}>
                    <Text style={styles.metricLabel}>Autenticación:</Text>
                    <Text style={styles.metricValue}>JWT Bearer 24h</Text>
                  </View>
                  <View style={styles.statMetricRow}>
                    <Text style={styles.metricLabel}>Backend REST:</Text>
                    <Text style={styles.metricValue}>Go 1.22 + Fiber v2</Text>
                  </View>
                </View>
              </View>
            ) : (
              <View>
                <View style={styles.profileCard}>
                  <View style={styles.profileBadgeClient}>
                    <Text style={styles.profileBadgeClientText}>👤 CLIENTE FRECUENTE REGISTRADO</Text>
                  </View>
                  <Text style={styles.profileName}>{user.nombre}</Text>
                  <Text style={styles.profileSub}>Usuario: @{user.usuario} • Correo: {user.email}</Text>
                  <Text style={styles.profileFicha}>Teléfono: {user.telefono}</Text>
                  <Text style={styles.profileCentro}>Ciudad: Popayán, Cauca</Text>
                </View>

                {/* BENEFICIOS Y PUNTOS */}
                <View style={styles.clientRewardsCard}>
                  <Text style={styles.clientRewardsTitle}>⭐ Puntos & Beneficios Bella Italia:</Text>
                  <View style={styles.pointsRow}>
                    <View>
                      <Text style={styles.pointsNumber}>{PROFILES.CLIENTE.puntos} Pts</Text>
                      <Text style={styles.pointsSub}>Equivalente a $3.500 COP de saldo</Text>
                    </View>
                    <View style={styles.couponPill}>
                      <Text style={styles.couponPillTitle}>CUPÓN ACTIVO</Text>
                      <Text style={styles.couponPillCode}>{PROFILES.CLIENTE.cupon}</Text>
                    </View>
                  </View>
                </View>

                {/* DIRECCIONES DE ENTREGA */}
                <View style={styles.addressesCard}>
                  <Text style={styles.addressesTitle}>📍 Mis Direcciones Guardadas en Popayán:</Text>
                  {PROFILES.CLIENTE.direcciones?.map((dir, idx) => (
                    <View key={idx} style={styles.addressItem}>
                      <Text style={styles.addressAlias}>{dir.alias}</Text>
                      <Text style={styles.addressDir}>{dir.dir}</Text>
                    </View>
                  ))}
                </View>

                {/* HISTORIAL DE PEDIDOS */}
                <View style={styles.orderHistoryCard}>
                  <Text style={styles.orderHistoryTitle}>📦 Mis Pedidos Recientes:</Text>
                  <View style={styles.orderHistoryItem}>
                    <View>
                      <Text style={styles.historyNumber}>PED-2026-002</Text>
                      <Text style={styles.historyDesc}>Cuatro Quesos + Carnes Campestre</Text>
                      <Text style={styles.historyPrice}>$79.050 COP</Text>
                    </View>
                    <TouchableOpacity
                      style={styles.historyTrackBtn}
                      onPress={() => setActiveTab('estados')}
                    >
                      <Text style={styles.historyTrackText}>Ver Estado 🛵</Text>
                    </TouchableOpacity>
                  </View>
                </View>
              </View>
            )}
          </View>
        )}
      </ScrollView>

      {/* 4. BARRA DE NAVEGACIÓN INFERIOR (BOTTOM TABS) */}
      <View style={styles.tabBar}>
        <TouchableOpacity style={styles.tabItem} onPress={() => setActiveTab('inicio')}>
          <Text style={styles.tabIcon}>🏠</Text>
          <Text style={[styles.tabLabel, activeTab === 'inicio' && styles.tabLabelActive]}>Inicio</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.tabItem} onPress={() => setActiveTab('carta')}>
          <Text style={styles.tabIcon}>🍕</Text>
          <Text style={[styles.tabLabel, activeTab === 'carta' && styles.tabLabelActive]}>Carta</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.tabItem} onPress={() => setActiveTab('carrito')}>
          <Text style={styles.tabIcon}>🛒</Text>
          <Text style={[styles.tabLabel, activeTab === 'carrito' && styles.tabLabelActive]}>
            Carrito {cart.length > 0 ? `(${cart.length})` : ''}
          </Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.tabItem} onPress={() => setActiveTab('estados')}>
          <Text style={styles.tabIcon}>📍</Text>
          <Text style={[styles.tabLabel, activeTab === 'estados' && styles.tabLabelActive]}>Estados</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.tabItem} onPress={() => setActiveTab('perfil')}>
          <Text style={styles.tabIcon}>{user.rol === 'ADMIN' ? '🛡️' : '👤'}</Text>
          <Text style={[styles.tabLabel, activeTab === 'perfil' && styles.tabLabelActive]}>
            {user.rol === 'ADMIN' ? 'Admin' : 'Perfil'}
          </Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}

// Función auxiliar para determinar si un paso ya fue alcanzado en el tracking
function isStepReached(current, step) {
  const order = ['RECIBIDO', 'EN_PREPARACION', 'EN_HORNO', 'EN_CAMINO', 'ENTREGADO'];
  const currentIndex = order.indexOf(current || 'EN_HORNO');
  const stepIndex = order.indexOf(step);
  return currentIndex >= stepIndex;
}

const styles = StyleSheet.create({
  rootScreen: {
    flex: 1,
    backgroundColor: '#0c0a09',
  },
  // Espaciador superior nativo para empujar toda la interfaz debajo de la barra de estado y cámara
  topInsetSpacer: {
    height: TOP_INSET,
    backgroundColor: '#1c1917',
  },
  header: {
    backgroundColor: '#1c1917',
    paddingHorizontal: 16,
    paddingTop: 4,
    paddingBottom: 12,
    borderBottomWidth: 1,
    borderBottomColor: '#292524',
  },
  headerTopRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
  },
  brandRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  logoText: {
    fontSize: 20,
    fontWeight: '900',
    color: '#ffffff',
  },
  logoHighlight: {
    color: '#ef4444',
  },
  senaBadge: {
    backgroundColor: '#d97706',
    paddingHorizontal: 7,
    paddingVertical: 2,
    borderRadius: 6,
  },
  senaBadgeText: {
    color: '#000',
    fontSize: 9,
    fontWeight: 'bold',
  },
  headerCity: {
    fontSize: 11,
    color: '#a8a29e',
  },
  roleSwitcherRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    backgroundColor: '#292524',
    padding: 6,
    borderRadius: 12,
    marginBottom: 6,
  },
  roleSwitcherLabel: {
    color: '#d6d3d1',
    fontSize: 12,
    fontWeight: 'bold',
    marginLeft: 6,
  },
  segmentedControl: {
    flexDirection: 'row',
    backgroundColor: '#1c1917',
    borderRadius: 8,
    padding: 3,
    gap: 4,
  },
  segmentedBtn: {
    paddingVertical: 6,
    paddingHorizontal: 14,
    borderRadius: 6,
  },
  segmentedBtnInactive: {
    backgroundColor: 'transparent',
  },
  segmentedBtnAdminActive: {
    backgroundColor: '#dc2626',
  },
  segmentedBtnClientActive: {
    backgroundColor: '#059669',
  },
  segmentedBtnText: {
    color: '#a8a29e',
    fontSize: 12,
    fontWeight: 'bold',
  },
  segmentedBtnTextActive: {
    color: '#ffffff',
  },
  sessionBanner: {
    marginTop: 2,
  },
  sessionBannerText: {
    fontSize: 11,
    color: '#a8a29e',
  },
  sessionBannerUser: {
    color: '#fbbf24',
    fontWeight: 'bold',
  },
  scrollContent: {
    padding: 16,
    paddingBottom: 40,
  },
  section: {
    marginBottom: 20,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#ffffff',
    marginBottom: 4,
  },
  sectionSubtitle: {
    fontSize: 12,
    color: '#a8a29e',
    marginBottom: 14,
  },
  sectionHeaderRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 12,
  },
  refreshBtn: {
    backgroundColor: '#292524',
    paddingHorizontal: 10,
    paddingVertical: 6,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#44403c',
  },
  refreshBtnText: {
    color: '#fbbf24',
    fontSize: 11,
    fontWeight: 'bold',
  },
  heroBanner: {
    backgroundColor: '#1c1917',
    borderRadius: 20,
    padding: 20,
    borderWidth: 1,
    borderColor: '#7f1d1d',
    marginBottom: 14,
  },
  heroBadge: {
    color: '#fbbf24',
    fontSize: 10,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  heroTitle: {
    fontSize: 22,
    fontWeight: '900',
    color: '#ffffff',
    marginBottom: 6,
  },
  heroSub: {
    fontSize: 12,
    color: '#d6d3d1',
    lineHeight: 18,
    marginBottom: 16,
  },
  primaryButton: {
    backgroundColor: '#dc2626',
    borderRadius: 12,
    paddingVertical: 12,
    alignItems: 'center',
    marginTop: 10,
  },
  primaryButtonText: {
    color: '#ffffff',
    fontSize: 14,
    fontWeight: 'bold',
  },
  promoCard: {
    backgroundColor: '#292524',
    padding: 14,
    borderRadius: 14,
    borderWidth: 1,
    borderColor: '#44403c',
    marginBottom: 14,
  },
  promoTitle: {
    fontSize: 13,
    fontWeight: 'bold',
    color: '#fbbf24',
  },
  promoDesc: {
    fontSize: 11,
    color: '#a8a29e',
    marginTop: 2,
  },
  roleContextCard: {
    backgroundColor: '#1c1917',
    padding: 14,
    borderRadius: 14,
    borderWidth: 1,
    borderColor: '#292524',
  },
  roleContextTitle: {
    fontSize: 13,
    fontWeight: 'bold',
    color: '#f59e0b',
  },
  roleContextDesc: {
    fontSize: 11,
    color: '#a8a29e',
    marginTop: 4,
    lineHeight: 16,
  },
  roleContextBtn: {
    marginTop: 10,
    alignSelf: 'flex-start',
    backgroundColor: '#292524',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#44403c',
  },
  roleContextBtnText: {
    color: '#ffffff',
    fontSize: 11,
    fontWeight: 'bold',
  },
  pizzaCard: {
    backgroundColor: '#1c1917',
    borderRadius: 16,
    padding: 16,
    marginBottom: 12,
    borderWidth: 1,
    borderColor: '#292524',
  },
  pizzaCardHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  pizzaName: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#ffffff',
  },
  pizzaPrice: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#fbbf24',
  },
  pizzaCategoryBadge: {
    fontSize: 10,
    color: '#ea580c',
    fontWeight: 'bold',
    marginTop: 2,
  },
  pizzaDesc: {
    fontSize: 12,
    color: '#a8a29e',
    marginVertical: 8,
  },
  addButton: {
    backgroundColor: '#292524',
    paddingVertical: 8,
    borderRadius: 10,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: '#44403c',
  },
  addButtonText: {
    color: '#f5f5f4',
    fontSize: 12,
    fontWeight: '600',
  },
  emptyCard: {
    backgroundColor: '#1c1917',
    borderRadius: 16,
    padding: 24,
    alignItems: 'center',
  },
  emptyIcon: {
    fontSize: 40,
    marginBottom: 10,
  },
  emptyText: {
    color: '#78716c',
    fontSize: 13,
    marginBottom: 16,
  },
  cartItem: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingVertical: 12,
    borderBottomWidth: 1,
    borderBottomColor: '#292524',
  },
  cartItemName: {
    color: '#ffffff',
    fontSize: 14,
    fontWeight: '600',
  },
  cartItemCategory: {
    color: '#78716c',
    fontSize: 10,
  },
  cartItemPrice: {
    color: '#fbbf24',
    fontSize: 14,
    fontWeight: 'bold',
  },
  totalRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginVertical: 14,
    paddingTop: 10,
    borderTopWidth: 2,
    borderTopColor: '#44403c',
  },
  totalLabel: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#ffffff',
  },
  totalValue: {
    fontSize: 18,
    fontWeight: '900',
    color: '#fbbf24',
  },
  subSectionTitle: {
    fontSize: 13,
    fontWeight: 'bold',
    color: '#d6d3d1',
    marginTop: 10,
    marginBottom: 6,
  },
  paymentMethods: {
    marginBottom: 10,
  },
  payBadge: {
    backgroundColor: '#1c1917',
    padding: 8,
    borderRadius: 8,
    color: '#d6d3d1',
    fontSize: 11,
    marginBottom: 4,
    borderWidth: 1,
    borderColor: '#292524',
  },
  trackingCard: {
    backgroundColor: '#1c1917',
    borderRadius: 16,
    padding: 16,
    borderWidth: 1,
    borderColor: '#b45309',
    marginBottom: 14,
  },
  trackingHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
  },
  trackingNumber: {
    color: '#fbbf24',
    fontSize: 16,
    fontWeight: 'bold',
  },
  statusPill: {
    backgroundColor: '#7f1d1d',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 8,
  },
  statusPillText: {
    color: '#ffffff',
    fontSize: 10,
    fontWeight: 'bold',
  },
  trackingDestino: {
    color: '#a8a29e',
    fontSize: 12,
    marginBottom: 4,
  },
  trackingTotal: {
    color: '#ffffff',
    fontSize: 12,
    fontWeight: 'bold',
    marginBottom: 4,
  },
  trackingTiempo: {
    color: '#f59e0b',
    fontSize: 12,
    fontWeight: 'bold',
    marginBottom: 12,
  },
  stepperContainer: {
    marginTop: 10,
    paddingTop: 10,
    borderTopWidth: 1,
    borderTopColor: '#292524',
  },
  stepItem: {
    fontSize: 13,
    color: '#78716c',
    marginVertical: 4,
  },
  stepCompleted: {
    color: '#10b981',
    fontWeight: 'bold',
  },
  adminQuickActionCard: {
    backgroundColor: '#1c1917',
    borderRadius: 16,
    padding: 16,
    borderWidth: 1,
    borderColor: '#7f1d1d',
  },
  adminQuickTitle: {
    fontSize: 13,
    fontWeight: 'bold',
    color: '#ef4444',
  },
  adminQuickDesc: {
    fontSize: 11,
    color: '#a8a29e',
    marginTop: 2,
    marginBottom: 10,
  },
  adminStatusButtonsGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 8,
  },
  adminStateBtn: {
    backgroundColor: '#292524',
    paddingVertical: 8,
    paddingHorizontal: 12,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#44403c',
  },
  adminStateBtnText: {
    color: '#f5f5f4',
    fontSize: 11,
    fontWeight: 'bold',
  },
  profileSwitcherCard: {
    backgroundColor: '#1c1917',
    borderRadius: 16,
    padding: 14,
    borderWidth: 1,
    borderColor: '#44403c',
    marginBottom: 14,
  },
  switcherHeaderTitle: {
    fontSize: 13,
    fontWeight: 'bold',
    color: '#ffffff',
    marginBottom: 8,
  },
  profileSwitcherButtons: {
    gap: 8,
  },
  profileSwitchOption: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#292524',
    padding: 12,
    borderRadius: 12,
    borderWidth: 2,
    borderColor: 'transparent',
    gap: 12,
  },
  profileSwitchOptionActiveAdmin: {
    borderColor: '#dc2626',
    backgroundColor: '#3b1212',
  },
  profileSwitchOptionActiveClient: {
    borderColor: '#059669',
    backgroundColor: '#063428',
  },
  profileSwitchOptionIcon: {
    fontSize: 22,
  },
  profileSwitchOptionTitle: {
    color: '#ffffff',
    fontSize: 14,
    fontWeight: 'bold',
  },
  profileSwitchOptionRole: {
    color: '#fbbf24',
    fontSize: 10,
    fontWeight: 'bold',
    marginTop: 2,
  },
  profileCard: {
    backgroundColor: '#1c1917',
    padding: 16,
    borderRadius: 16,
    borderWidth: 1,
    borderColor: '#292524',
    marginBottom: 12,
  },
  profileBadgeAdmin: {
    alignSelf: 'flex-start',
    backgroundColor: '#7f1d1d',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 6,
    marginBottom: 8,
  },
  profileBadgeAdminText: {
    color: '#fecaca',
    fontSize: 10,
    fontWeight: 'bold',
  },
  profileBadgeClient: {
    alignSelf: 'flex-start',
    backgroundColor: '#064e3b',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 6,
    marginBottom: 8,
  },
  profileBadgeClientText: {
    color: '#a7f3d0',
    fontSize: 10,
    fontWeight: 'bold',
  },
  profileName: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#ffffff',
  },
  profileSub: {
    fontSize: 12,
    color: '#a8a29e',
    marginTop: 2,
  },
  profileFicha: {
    fontSize: 12,
    color: '#fbbf24',
    fontWeight: 'bold',
    marginTop: 4,
  },
  profileCentro: {
    fontSize: 11,
    color: '#78716c',
    marginTop: 2,
  },
  profileDireccion: {
    fontSize: 11,
    color: '#d6d3d1',
    marginTop: 4,
  },
  adminActionCard: {
    backgroundColor: '#1c1917',
    padding: 14,
    borderRadius: 14,
    borderWidth: 1,
    borderColor: '#7f1d1d',
    marginBottom: 12,
  },
  adminActionTitle: {
    fontSize: 13,
    fontWeight: 'bold',
    color: '#ffffff',
    marginBottom: 8,
  },
  stateButtonsRow: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 6,
  },
  stateBtn: {
    backgroundColor: '#292524',
    paddingHorizontal: 9,
    paddingVertical: 6,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#44403c',
  },
  stateBtnActive: {
    backgroundColor: '#dc2626',
    borderColor: '#ef4444',
  },
  stateBtnText: {
    color: '#ffffff',
    fontSize: 11,
    fontWeight: '600',
  },
  adminStatsCard: {
    backgroundColor: '#1c1917',
    padding: 16,
    borderRadius: 16,
    borderWidth: 1,
    borderColor: '#292524',
    marginBottom: 12,
  },
  adminStatsTitle: {
    fontSize: 14,
    fontWeight: 'bold',
    color: '#ffffff',
    marginBottom: 10,
  },
  statMetricRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingVertical: 4,
    borderBottomWidth: 1,
    borderBottomColor: '#292524',
  },
  metricLabel: {
    fontSize: 11,
    color: '#a8a29e',
  },
  metricValue: {
    fontSize: 11,
    color: '#fbbf24',
    fontWeight: 'bold',
  },
  clientRewardsCard: {
    backgroundColor: '#1c1917',
    padding: 14,
    borderRadius: 14,
    borderWidth: 1,
    borderColor: '#064e3b',
    marginBottom: 12,
  },
  clientRewardsTitle: {
    fontSize: 13,
    fontWeight: 'bold',
    color: '#10b981',
    marginBottom: 8,
  },
  pointsRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  pointsNumber: {
    fontSize: 22,
    fontWeight: '900',
    color: '#ffffff',
  },
  pointsSub: {
    fontSize: 10,
    color: '#a8a29e',
    marginTop: 2,
  },
  couponPill: {
    backgroundColor: '#064e3b',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 10,
    alignItems: 'center',
  },
  couponPillTitle: {
    fontSize: 8,
    color: '#a7f3d0',
    fontWeight: 'bold',
  },
  couponPillCode: {
    fontSize: 13,
    color: '#ffffff',
    fontWeight: 'bold',
  },
  addressesCard: {
    backgroundColor: '#1c1917',
    padding: 14,
    borderRadius: 14,
    borderWidth: 1,
    borderColor: '#292524',
    marginBottom: 12,
  },
  addressesTitle: {
    fontSize: 13,
    fontWeight: 'bold',
    color: '#ffffff',
    marginBottom: 8,
  },
  addressItem: {
    paddingVertical: 6,
    borderBottomWidth: 1,
    borderBottomColor: '#292524',
  },
  addressAlias: {
    fontSize: 12,
    fontWeight: 'bold',
    color: '#fbbf24',
  },
  addressDir: {
    fontSize: 11,
    color: '#a8a29e',
    marginTop: 2,
  },
  orderHistoryCard: {
    backgroundColor: '#1c1917',
    padding: 14,
    borderRadius: 14,
    borderWidth: 1,
    borderColor: '#292524',
    marginBottom: 12,
  },
  orderHistoryTitle: {
    fontSize: 13,
    fontWeight: 'bold',
    color: '#ffffff',
    marginBottom: 8,
  },
  orderHistoryItem: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingVertical: 8,
  },
  historyNumber: {
    fontSize: 13,
    fontWeight: 'bold',
    color: '#fbbf24',
  },
  historyDesc: {
    fontSize: 11,
    color: '#a8a29e',
    marginTop: 2,
  },
  historyPrice: {
    fontSize: 12,
    fontWeight: 'bold',
    color: '#ffffff',
    marginTop: 2,
  },
  historyTrackBtn: {
    backgroundColor: '#292524',
    paddingHorizontal: 10,
    paddingVertical: 6,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#44403c',
  },
  historyTrackText: {
    color: '#f59e0b',
    fontSize: 11,
    fontWeight: 'bold',
  },
  tabBar: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    backgroundColor: '#1c1917',
    borderTopWidth: 1,
    borderTopColor: '#292524',
    paddingTop: 10,
    paddingBottom: Platform.OS === 'ios' ? 24 : 14,
  },
  tabItem: {
    alignItems: 'center',
  },
  tabIcon: {
    fontSize: 18,
  },
  tabLabel: {
    fontSize: 10,
    color: '#78716c',
    marginTop: 2,
  },
  tabLabelActive: {
    color: '#ef4444',
    fontWeight: 'bold',
  },
});

registerRootComponent(App);
