/**
 * OrderHistoryTable - Panel de Comandas para Personal de Cocina
 * 
 * Organismo que despliega las órdenes activas, el desglose de pizzas
 * y botones para transicionar el estado operativo del pedido en tiempo real.
 * 
 * Aprendiz: Karen Yuliana Campo - SENA ADSO Ficha 228118
 */

import React, { useState } from 'react';

const STATUS_OPTIONS = ['TODOS', 'PENDIENTE', 'PREPARANDO', 'EN_CAMINO', 'ENTREGADO'];

export const OrderHistoryTable = ({ orders = [], onUpdateStatus, loading = false }) => {
  const [filter, setFilter] = useState('TODOS');

  const filteredOrders = orders.filter((ord) => {
    if (filter === 'TODOS') return true;
    return ord.estado === filter;
  });

  return (
    <section className="kitchen-panel-section" aria-label="Panel de comandas de cocina">
      <div className="kitchen-header">
        <div>
          <h2 className="kitchen-title">👨‍🍳 Comandas Operativas de Cocina</h2>
          <p className="kitchen-subtitle">
            Monitoreo en tiempo real de órdenes radicadas y despacho a domicilio.
          </p>
        </div>

        {/* Filtros de Estado */}
        <div className="kitchen-filter-pills">
          {STATUS_OPTIONS.map((st) => (
            <button
              key={st}
              className={`kitchen-pill ${filter === st ? 'active' : ''}`}
              onClick={() => setFilter(st)}
            >
              {st}
            </button>
          ))}
        </div>
      </div>

      {loading ? (
        <div className="kitchen-loading">Sincronizando comandas con Spring Boot...</div>
      ) : filteredOrders.length === 0 ? (
        <div className="kitchen-empty">
          <span>🍕</span>
          <p>No hay comandas registradas en estado <strong>{filter}</strong>.</p>
        </div>
      ) : (
        <div className="table-responsive">
          <table className="kitchen-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Cliente & Contacto</th>
                <th>Dirección</th>
                <th>Pizzas Solicitadas</th>
                <th>Total COP</th>
                <th>Estado Actual</th>
                <th>Acciones de Cocina</th>
              </tr>
            </thead>
            <tbody>
              {filteredOrders.map((ord) => (
                <tr key={ord.idPedido}>
                  <td className="col-id">#{ord.idPedido}</td>
                  <td>
                    <strong>{ord.cliente ? ord.cliente.nombre : 'Cliente General'}</strong>
                    <div className="cell-sub">{ord.cliente ? ord.cliente.telefono : 'N/A'}</div>
                  </td>
                  <td className="col-address">
                    {ord.cliente ? ord.cliente.direccion : 'Mostrador'}
                  </td>
                  <td className="col-details">
                    {ord.detalles && ord.detalles.length > 0 ? (
                      <ul className="details-list">
                        {ord.detalles.map((det, i) => (
                          <li key={i}>
                            <strong>{det.cantidad}x</strong> {det.pizza ? det.pizza.nombre : 'Pizza'} ({det.tamano || 'Mediana'})
                          </li>
                        ))}
                      </ul>
                    ) : (
                      <span>1x Orden Completa</span>
                    )}
                  </td>
                  <td className="col-price">
                    ${(ord.total || 0).toLocaleString('es-CO')}
                  </td>
                  <td>
                    <span className={`status-badge status-${(ord.estado || '').toLowerCase()}`}>
                      {ord.estado}
                    </span>
                  </td>
                  <td className="col-actions">
                    {ord.estado === 'PENDIENTE' && (
                      <button
                        className="btn-action-status bg-orange"
                        onClick={() => onUpdateStatus(ord.idPedido, 'PREPARANDO')}
                        title="Enviar al horno de leña"
                      >
                        🔥 Al Horno
                      </button>
                    )}
                    {ord.estado === 'PREPARANDO' && (
                      <button
                        className="btn-action-status bg-blue"
                        onClick={() => onUpdateStatus(ord.idPedido, 'EN_CAMINO')}
                        title="Despachar con repartidor"
                      >
                        🛵 Despachar
                      </button>
                    )}
                    {ord.estado === 'EN_CAMINO' && (
                      <button
                        className="btn-action-status bg-green"
                        onClick={() => onUpdateStatus(ord.idPedido, 'ENTREGADO')}
                        title="Confirmar entrega al cliente"
                      >
                        ✓ Entregar
                      </button>
                    )}
                    {ord.estado === 'ENTREGADO' && (
                      <span className="text-muted">✓ Completada</span>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </section>
  );
};
