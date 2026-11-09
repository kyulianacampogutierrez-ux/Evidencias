/**
 * CartDrawer - Panel Lateral Deslizante (Off-Canvas) del Carrito
 * 
 * Organismo que muestra:
 * - Listado de ítems acumulados
 * - Barra de progreso hacia el envío gratis ($50.000 COP)
 * - Cálculo de subtotal, costo de envío y total neto
 * - Botón de acceso al modal de Checkout
 * 
 * Aprendiz: Karen Yuliana Campo - SENA ADSO Ficha 228118
 */

import React, { useEffect } from 'react';
import { useCart } from '../context/CartContext.jsx';
import { CartItem } from './CartItem.jsx';

export const CartDrawer = ({ isOpen, onClose, onProceedToCheckout }) => {
  const {
    items,
    updateQuantity,
    removeFromCart,
    clearCart,
    subtotalCOP,
    shippingCOP,
    totalCOP,
    freeShippingEligible,
    freeShippingThreshold
  } = useCart();

  // Escuchar tecla ESC para cerrar el panel
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape' && isOpen) {
        onClose();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  const progressPercent = Math.min(100, Math.round((subtotalCOP / freeShippingThreshold) * 100));
  const missingForFreeShipping = Math.max(0, freeShippingThreshold - subtotalCOP);

  return (
    <div className="drawer-overlay" onClick={onClose} role="presentation">
      <div
        className="drawer-container"
        onClick={(e) => e.stopPropagation()}
        role="dialog"
        aria-modal="true"
        aria-labelledby="drawer-title"
      >
        {/* Cabecera del Drawer */}
        <div className="drawer-header">
          <div className="drawer-header-left">
            <span className="drawer-icon">🛒</span>
            <h2 id="drawer-title" className="drawer-title">
              Tu Pedido ({items.length} {items.length === 1 ? 'producto' : 'productos'})
            </h2>
          </div>
          <button
            className="drawer-close-btn"
            onClick={onClose}
            aria-label="Cerrar panel de pedido"
          >
            ✕
          </button>
        </div>

        {/* Barra de Envío Gratis */}
        <div className="shipping-bar-wrap">
          {freeShippingEligible ? (
            <div className="shipping-congrats">
              🎉 ¡Felicidades! Tienes <strong>ENVÍO GRATIS</strong> en este pedido.
            </div>
          ) : (
            <div className="shipping-missing">
              Agrega <strong>${missingForFreeShipping.toLocaleString('es-CO')}</strong> más para tener <strong>ENVÍO GRATIS</strong>.
            </div>
          )}
          <div className="shipping-progress-bg">
            <div
              className={`shipping-progress-fill ${freeShippingEligible ? 'complete' : ''}`}
              style={{ width: `${progressPercent}%` }}
            ></div>
          </div>
        </div>

        {/* Lista de Ítems */}
        <div className="drawer-body" role="list">
          {items.length === 0 ? (
            <div className="drawer-empty">
              <span className="empty-cart-icon">🍕</span>
              <p>Tu carrito está vacío todavía.</p>
              <span>¡Agrega deliciosas pizzas del menú para comenzar!</span>
            </div>
          ) : (
            items.map((it) => (
              <CartItem
                key={`${it.idPizza}-${it.tamano}`}
                item={it}
                onUpdateQuantity={updateQuantity}
                onRemove={removeFromCart}
              />
            ))
          )}
        </div>

        {/* Resumen de Costos y Checkout */}
        {items.length > 0 && (
          <div className="drawer-footer">
            <div className="price-breakdown">
              <div className="breakdown-row">
                <span>Subtotal Comida:</span>
                <span>${subtotalCOP.toLocaleString('es-CO')}</span>
              </div>
              <div className="breakdown-row">
                <span>Costo de Domicilio:</span>
                <span className={freeShippingEligible ? 'free-tag' : ''}>
                  {freeShippingEligible ? 'GRATIS' : `$${shippingCOP.toLocaleString('es-CO')}`}
                </span>
              </div>
              <div className="breakdown-total">
                <span>Total a Pagar:</span>
                <span className="total-amount">${totalCOP.toLocaleString('es-CO')}</span>
              </div>
            </div>

            <div className="drawer-actions">
              <button
                className="btn-checkout"
                onClick={() => {
                  onClose();
                  onProceedToCheckout();
                }}
              >
                Confirmar y Pedir Ahora 🛵
              </button>
              <button className="btn-clear-cart" onClick={clearCart}>
                Vaciar Carrito
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
