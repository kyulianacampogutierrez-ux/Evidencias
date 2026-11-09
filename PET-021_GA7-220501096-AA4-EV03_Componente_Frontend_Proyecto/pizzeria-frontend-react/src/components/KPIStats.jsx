/**
 * KPIStats - Panel de Métricas Operativas en Tiempo Real
 * 
 * Calcula agregaciones automáticas a partir de los pedidos despachados
 * y pendientes del microservicio Spring Boot.
 * 
 * Aprendiz: Karen Yuliana Campo - SENA ADSO Ficha 228118
 */

import React, { useMemo } from 'react';

export const KPIStats = ({ orders = [], loading = false }) => {
  // Cálculo de estadísticas consolidadas mediante useMemo
  const stats = useMemo(() => {
    const totalOrders = orders.length;
    const totalRevenue = orders.reduce((acc, ord) => acc + (ord.total || 0), 0);
    const pendingOrders = orders.filter((ord) => ord.estado === 'PENDIENTE' || ord.estado === 'PREPARANDO').length;
    const deliveredOrders = orders.filter((ord) => ord.estado === 'ENTREGADO').length;

    return {
      totalOrders,
      totalRevenue,
      pendingOrders,
      deliveredOrders,
      promedioTicket: totalOrders > 0 ? Math.round(totalRevenue / totalOrders) : 0
    };
  }, [orders]);

  if (loading) {
    return <div className="kpi-loading">Cargando métricas operativas...</div>;
  }

  return (
    <section className="kpi-section" aria-label="Métricas e Indicadores Clave de Desempeño">
      <div className="kpi-grid">
        <div className="kpi-card">
          <div className="kpi-icon-wrap bg-blue">💰</div>
          <div className="kpi-info">
            <span className="kpi-label">Ingresos Totales (Hoy)</span>
            <span className="kpi-value">${stats.totalRevenue.toLocaleString('es-CO')}</span>
            <span className="kpi-sub">Facturación neta COP</span>
          </div>
        </div>

        <div className="kpi-card">
          <div className="kpi-icon-wrap bg-orange">📋</div>
          <div className="kpi-info">
            <span className="kpi-label">Comandas en Cocina</span>
            <span className="kpi-value">{stats.pendingOrders}</span>
            <span className="kpi-sub">Pendientes / En Horno</span>
          </div>
        </div>

        <div className="kpi-card">
          <div className="kpi-icon-wrap bg-green">✅</div>
          <div className="kpi-info">
            <span className="kpi-label">Pedidos Entregados</span>
            <span className="kpi-value">{stats.deliveredOrders}</span>
            <span className="kpi-sub">Completados con éxito</span>
          </div>
        </div>

        <div className="kpi-card">
          <div className="kpi-icon-wrap bg-purple">🎯</div>
          <div className="kpi-info">
            <span className="kpi-label">Ticket Promedio</span>
            <span className="kpi-value">${stats.promedioTicket.toLocaleString('es-CO')}</span>
            <span className="kpi-sub">Por orden despachada</span>
          </div>
        </div>
      </div>
    </section>
  );
};
