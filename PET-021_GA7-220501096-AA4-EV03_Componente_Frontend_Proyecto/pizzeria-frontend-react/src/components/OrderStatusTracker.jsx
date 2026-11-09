/**
 * OrderStatusTracker - Seguidor de Estado del Pedido en Tiempo Real
 * 
 * Molécula que visualiza el ciclo de vida del pedido en 4 etapas:
 * 1. PENDIENTE (Recibido en sistema)
 * 2. PREPARANDO (En horno de leña)
 * 3. EN_CAMINO (Repartidor en ruta)
 * 4. ENTREGADO (Completado con éxito)
 * 
 * Aprendiz: Karen Yuliana Campo - SENA ADSO Ficha 228118
 */

import React from 'react';

const STEPS = [
  { key: 'PENDIENTE', label: 'Recibido', icon: '📝', desc: 'Comanda registrada en el sistema' },
  { key: 'PREPARANDO', label: 'En Horno', icon: '🔥', desc: 'Horneando con masa madre a 450°C' },
  { key: 'EN_CAMINO', label: 'En Camino', icon: '🛵', desc: 'Repartidor en ruta a tu dirección' },
  { key: 'ENTREGADO', label: 'Entregado', icon: '🍕', desc: '¡Buen provecho! Pedido finalizado' }
];

export const OrderStatusTracker = ({ orderId, status = 'PENDIENTE', clientName, total }) => {
  const currentStepIndex = STEPS.findIndex((s) => s.key === status);
  const activeIndex = currentStepIndex >= 0 ? currentStepIndex : 0;
  const progressPercent = Math.round((activeIndex / (STEPS.length - 1)) * 100);

  return (
    <div className="tracker-card" aria-label="Seguimiento en vivo del pedido">
      <div className="tracker-header">
        <div>
          <span className="tracker-badge">ORDEN CONFIRMADA #{orderId}</span>
          <h3 className="tracker-title">¡Gracias por tu compra{clientName ? `, ${clientName}` : ''}!</h3>
        </div>
        {total && (
          <div className="tracker-total">
            <span>Total:</span>
            <strong>${total.toLocaleString('es-CO')}</strong>
          </div>
        )}
      </div>

      {/* Barra de Progreso */}
      <div className="tracker-progress-bg">
        <div
          className="tracker-progress-fill"
          style={{ width: `${progressPercent}%` }}
        ></div>
      </div>

      {/* Pasos */}
      <div className="tracker-steps">
        {STEPS.map((step, idx) => {
          const isDone = idx < activeIndex;
          const isCurrent = idx === activeIndex;
          return (
            <div
              key={step.key}
              className={`tracker-step ${isDone ? 'done' : ''} ${isCurrent ? 'current' : ''}`}
            >
              <div className="step-circle" aria-hidden="true">
                {isDone ? '✓' : step.icon}
              </div>
              <span className="step-label">{step.label}</span>
              <span className="step-desc">{step.desc}</span>
            </div>
          );
        })}
      </div>
    </div>
  );
};
