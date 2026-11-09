/**
 * CartItem - Fila de Producto dentro del Carrito de Compras
 * 
 * Molécula que permite:
 * - Visualizar la pizza, tamaño seleccionado y precio
 * - Incrementar o decrementar unidades
 * - Eliminar el producto del pedido
 * 
 * Aprendiz: Karen Yuliana Campo - SENA ADSO Ficha 228118
 */

import React from 'react';

export const CartItem = ({ item, onUpdateQuantity, onRemove }) => {
  return (
    <div className="cart-item-row" role="listitem">
      <div className="cart-item-img-wrap">
        <img src={item.imagen} alt={item.nombre} className="cart-item-img" />
      </div>

      <div className="cart-item-details">
        <h4 className="cart-item-name">{item.nombre}</h4>
        <div className="cart-item-meta">
          <span className="cart-item-size">Tamaño: <strong>{item.tamano}</strong></span>
          <span className="cart-item-unit">${item.precioUnitario.toLocaleString('es-CO')} c/u</span>
        </div>

        <div className="cart-item-actions">
          {/* Controles de Cantidad */}
          <div className="cart-qty-ctrl">
            <button
              className="qty-btn-sm"
              onClick={() => onUpdateQuantity(item.idPizza, item.tamano, -1)}
              aria-label="Restar una unidad"
            >
              -
            </button>
            <span className="qty-val">{item.cantidad}</span>
            <button
              className="qty-btn-sm"
              onClick={() => onUpdateQuantity(item.idPizza, item.tamano, 1)}
              aria-label="Sumar una unidad"
            >
              +
            </button>
          </div>

          <span className="cart-item-subtotal">
            ${item.subtotal.toLocaleString('es-CO')}
          </span>

          <button
            className="cart-remove-btn"
            onClick={() => onRemove(item.idPizza, item.tamano)}
            aria-label={`Eliminar ${item.nombre} del carrito`}
            title="Eliminar producto"
          >
            🗑️
          </button>
        </div>
      </div>
    </div>
  );
};
