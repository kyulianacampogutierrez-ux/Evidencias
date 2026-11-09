/**
 * App - Componente Raíz de la Aplicación SPA Pizzería Bella Italia
 * 
 * Orquestador principal que integra:
 * - Proveedores de contexto global (CartProvider, AuthProvider)
 * - Barra de navegación responsive (Navbar)
 * - Hero banner promocional (HeroBanner)
 * - Métricas operativas (KPIStats)
 * - Filtrado y búsqueda reactiva (CategoryFilter)
 * - Rejilla del menú gastronómico (PizzaMenuGrid)
 * - Cajón lateral deslizante del pedido (CartDrawer)
 * - Modal accesible de checkout y validación de cliente (CustomerFormModal)
 * - Seguidor en vivo del estado del pedido (OrderStatusTracker)
 * - Panel de comandas de cocina (OrderHistoryTable)
 * 
 * Aprendiz: Karen Yuliana Campo
 * Ficha: 228118 - ADSO Modalidad Virtual
 * Centro de Teleinformática y Producción Industrial (CTPI) - Popayán, Cauca
 */

import React, { useState, useEffect, useMemo } from 'react';
import { CartProvider, useCart } from './context/CartContext.jsx';
import { AuthProvider, useAuth } from './context/AuthContext.jsx';
import { Navbar } from './components/Navbar.jsx';
import { HeroBanner } from './components/HeroBanner.jsx';
import { KPIStats } from './components/KPIStats.jsx';
import { CategoryFilter } from './components/CategoryFilter.jsx';
import { PizzaMenuGrid } from './components/PizzaMenuGrid.jsx';
import { CartDrawer } from './components/CartDrawer.jsx';
import { CustomerFormModal } from './components/CustomerFormModal.jsx';
import { OrderStatusTracker } from './components/OrderStatusTracker.jsx';
import { OrderHistoryTable } from './components/OrderHistoryTable.jsx';
import { getPizzas, getPedidos, createPedido, updateEstadoPedido } from './services/api.js';
import './styles/App.css';

// Componente interno consumidor de contextos
function PizzeriaAppContent() {
  const { isDrawerOpen, setIsDrawerOpen, clearCart } = useCart();
  const { role } = useAuth();

  // Estados de navegación y datos
  const [activeSection, setActiveSection] = useState('menu');
  const [pizzas, setPizzas] = useState([]);
  const [orders, setOrders] = useState([]);
  const [loadingPizzas, setLoadingPizzas] = useState(true);
  const [loadingOrders, setLoadingOrders] = useState(false);

  // Estados de filtrado y búsqueda
  const [selectedCategory, setSelectedCategory] = useState('Todas');
  const [searchTerm, setSearchTerm] = useState('');

  // Estados para modales y confirmación
  const [isCheckoutOpen, setIsCheckoutOpen] = useState(false);
  const [lastConfirmedOrder, setLastConfirmedOrder] = useState(null);

  // Carga inicial de catálogo de pizzas desde el microservicio Spring Boot
  useEffect(() => {
    let isMounted = true;
    const fetchCatalog = async () => {
      try {
        setLoadingPizzas(true);
        const data = await getPizzas();
        if (isMounted) setPizzas(data);
      } finally {
        if (isMounted) setLoadingPizzas(false);
      }
    };
    fetchCatalog();
    return () => {
      isMounted = false;
    };
  }, []);

  // Carga de comandas para vista de cocina / administrador
  const reloadOrders = async () => {
    try {
      setLoadingOrders(true);
      const data = await getPedidos();
      setOrders(data);
    } finally {
      setLoadingOrders(false);
    }
  };

  useEffect(() => {
    if (activeSection === 'cocina' || activeSection === 'kpis' || role === 'ADMIN') {
      reloadOrders();
    }
  }, [activeSection, role]);

  // Filtrado reactivo de pizzas en memoria con useMemo
  const filteredPizzas = useMemo(() => {
    return pizzas.filter((pizza) => {
      const matchCategory =
        selectedCategory === 'Todas' || pizza.categoria === selectedCategory;
      const matchSearch =
        searchTerm.trim() === '' ||
        pizza.nombre.toLowerCase().includes(searchTerm.toLowerCase()) ||
        pizza.descripcion.toLowerCase().includes(searchTerm.toLowerCase());
      return matchCategory && matchSearch;
    });
  }, [pizzas, selectedCategory, searchTerm]);

  // Manejador del checkout y confirmación de orden
  const handleConfirmOrder = async (orderPayload) => {
    try {
      const confirmed = await createPedido(orderPayload);
      setLastConfirmedOrder({
        orderId: confirmed.idPedido || Math.floor(100 + Math.random() * 900),
        status: 'PENDIENTE',
        clientName: orderPayload.cliente.nombre,
        total: orderPayload.total
      });

      // Limpiar carrito tras radicación exitosa
      clearCart();
      setIsCheckoutOpen(false);

      // Recargar lista de pedidos para actualizar métricas
      reloadOrders();

      // Scroll suave hacia la confirmación
      window.scrollTo({ top: 380, behavior: 'smooth' });
    } catch (err) {
      alert(`Error al procesar el pedido: ${err.message}`);
    }
  };

  // Manejador de transición de estados de cocina
  const handleUpdateOrderStatus = async (idPedido, nuevoEstado) => {
    await updateEstadoPedido(idPedido, nuevoEstado);
    // Actualización optimista del estado local
    setOrders((prev) =>
      prev.map((ord) => (ord.idPedido === idPedido ? { ...ord, estado: nuevoEstado } : ord))
    );
    // Sincronizar tracker si corresponde al pedido actual
    if (lastConfirmedOrder && lastConfirmedOrder.orderId === idPedido) {
      setLastConfirmedOrder((prev) => ({ ...prev, status: nuevoEstado }));
    }
  };

  return (
    <div className="app-layout">
      {/* 1. Barra de Navegación */}
      <Navbar
        brandName="Pizzería Bella Italia"
        activeSection={activeSection}
        onNavigate={setActiveSection}
      />

      {/* 2. Hero Banner Promocional */}
      <HeroBanner onExploreMenu={() => setActiveSection('menu')} />

      {/* Contenedor Principal */}
      <main className="main-content">
        {/* Banner de Confirmación / Tracker Activo */}
        {lastConfirmedOrder && (
          <section className="confirmed-order-wrapper">
            <OrderStatusTracker
              orderId={lastConfirmedOrder.orderId}
              status={lastConfirmedOrder.status}
              clientName={lastConfirmedOrder.clientName}
              total={lastConfirmedOrder.total}
            />
          </section>
        )}

        {/* Vista: Catálogo de Menú Tradicional */}
        {activeSection === 'menu' && (
          <>
            <div className="section-heading">
              <span className="section-tag">CATÁLOGO GASTRONÓMICO</span>
              <h2 className="section-title">Nuestras Pizzas de Autor</h2>
              <p className="section-desc">
                Elige tus favoritas, personaliza el tamaño y disfruta del verdadero sabor napolitano.
              </p>
            </div>

            {/* Filtros de Categorías y Búsqueda */}
            <CategoryFilter
              selectedCategory={selectedCategory}
              onSelectCategory={setSelectedCategory}
              searchTerm={searchTerm}
              onSearchChange={setSearchTerm}
            />

            {/* Rejilla de Pizzas */}
            <PizzaMenuGrid
              pizzas={filteredPizzas}
              loading={loadingPizzas}
            />
          </>
        )}

        {/* Vista: Comandas de Cocina */}
        {activeSection === 'cocina' && (
          <OrderHistoryTable
            orders={orders}
            onUpdateStatus={handleUpdateOrderStatus}
            loading={loadingOrders}
          />
        )}

        {/* Vista: Métricas KPI */}
        {activeSection === 'kpis' && (
          <>
            <div className="section-heading">
              <span className="section-tag">PANEL GERENCIAL</span>
              <h2 className="section-title">Indicadores Clave de Desempeño (KPIs)</h2>
              <p className="section-desc">
                Métricas operativas del día calculadas a partir de las comandas y despachos.
              </p>
            </div>
            <KPIStats orders={orders} loading={loadingOrders} />
          </>
        )}
      </main>

      {/* 3. Panel Lateral Deslizante (CartDrawer) */}
      <CartDrawer
        isOpen={isDrawerOpen}
        onClose={() => setIsDrawerOpen(false)}
        onProceedToCheckout={() => setIsCheckoutOpen(true)}
      />

      {/* 4. Modal Accesible de Checkout (CustomerFormModal) */}
      <CustomerFormModal
        isOpen={isCheckoutOpen}
        onClose={() => setIsCheckoutOpen(false)}
        onSubmitOrder={handleConfirmOrder}
      />

      {/* Pie de Página Institucional */}
      <footer className="app-footer">
        <div className="footer-container">
          <div className="footer-brand">
            <span className="footer-icon">🍕</span>
            <h3>Pizzería Bella Italia</h3>
            <p>Trattoria artesanal &bull; Horno de leña &bull; Popayán, Cauca</p>
          </div>
          <div className="footer-meta">
            <p><strong>SENA - Regional Cauca</strong> &bull; Centro de Teleinformática y Producción Industrial (CTPI)</p>
            <p>Tecnología en Análisis y Desarrollo de Software (ADSO) - Ficha 228118</p>
            <p>Aprendiz: <strong>Karen Yuliana Campo</strong> &bull; Evidencia: GA7-220501096-AA4-EV03</p>
          </div>
        </div>
      </footer>
    </div>
  );
}

// Exportación del componente raíz envuelto en proveedores
export default function App() {
  return (
    <AuthProvider>
      <CartProvider>
        <PizzeriaAppContent />
      </CartProvider>
    </AuthProvider>
  );
}
