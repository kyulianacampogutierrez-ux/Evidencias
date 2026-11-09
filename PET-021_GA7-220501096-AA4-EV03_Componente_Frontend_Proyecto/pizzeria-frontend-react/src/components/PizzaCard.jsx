/**
 * PizzaCard - Tarjeta Individual de Producto en el Menú
 * 
 * Molécula que encapsula:
 * - Imagen y badge de categoría
 * - Nombre y descripción de ingredientes
 * - Selector interactivo de tamaño con ajuste dinámico de precio
 * - Control de cantidad unitaria
 * - Botón de adición al carrito con retroalimentación animada
 * 
 * Aprendiz: Karen Yuliana Campo - SENA ADSO Ficha 228118
 */

import React, { useState } from 'react';

export const PizzaCard = ({ pizza, onAddToCart }) => {
  const [tamano, setTamano] = useState('mediana');
  const [cantidad, setCantidad] = useState(1);
  const [justAdded, setJustAdded] = useState(false);

  // Multiplicador de precio según el tamaño
  const factor = tamano === 'familiar' ? 1.4 : tamano === 'personal' ? 0.7 : 1.0;
  const precioUnitario = Math.round(pizza.precio * factor);
  const subtotal = precioUnitario * cantidad;

  const handleAddToCart = () => {
    if (!onAddToCart) return;
    onAddToCart({
      idPizza: pizza.idPizza,
      nombre: pizza.nombre,
      categoria: pizza.categoria,
      imagen: pizza.imagen,
      tamano,
      cantidad,
      precioUnitario,
      subtotal
    });

    setJustAdded(true);
    setTimeout(() => setJustAdded(false), 1200);
  };

  return (
    <article className="pizza-card" aria-labelledby={`pizza-title-${pizza.idPizza}`}>
      {/* Contenedor de Imagen y Badge */}
      <div className="card-img-wrap">
        <img
          src={pizza.imagen}
          alt={`Pizza ${pizza.nombre}`}
          className="card-img"
          loading="lazy"
        />
        <span className="card-badge">{pizza.categoria}</span>
      </div>

      {/* Contenido de la Pizza */}
      <div className="card-body">
        <h3 id={`pizza-title-${pizza.idPizza}`} className="card-title">
          {pizza.nombre}
        </h3>
        <p className="card-desc">{pizza.descripcion}</p>

        {/* Selector de Tamaño */}
        <div className="size-selector">
          <label htmlFor={`size-${pizza.idPizza}`} className="selector-label">
            Tamaño:
          </label>
          <select
            id={`size-${pizza.idPizza}`}
            value={tamano}
            onChange={(e) => setTamano(e.target.value)}
            className="select-custom"
          >
            <option value="personal">Personal (4 porciones) - 30% desc.</option>
            <option value="mediana">Mediana (8 porciones) - Estándar</option>
            <option value="familiar">Familiar (12 porciones) + 40%</option>
          </select>
        </div>

        {/* Fila de Cantidad y Precio */}
        <div className="card-pricing-row">
          <div className="qty-control">
            <button
              type="button"
              className="qty-btn"
              onClick={() => setCantidad((prev) => Math.max(1, prev - 1))}
              aria-label="Restar una pizza"
            >
              -
            </button>
            <span className="qty-number" aria-label={`Cantidad ${cantidad}`}>
              {cantidad}
            </span>
            <button
              type="button"
              className="qty-btn"
              onClick={() => setCantidad((prev) => prev + 1)}
              aria-label="Sumar una pizza"
            >
              +
            </button>
          </div>

          <div className="price-display">
            <span className="price-unit">${precioUnitario.toLocaleString('es-CO')} c/u</span>
            <span className="price-total">${subtotal.toLocaleString('es-CO')}</span>
          </div>
        </div>

        {/* Botón de Agregar */}
        <button
          type="button"
          className={`btn-add-cart ${justAdded ? 'added' : ''}`}
          onClick={handleAddToCart}
          aria-label={`Agregar ${cantidad} ${pizza.nombre} tamaño ${tamano} al carrito`}
        >
          {justAdded ? '¡Agregada al Pedido! ✓' : 'Agregar al Carrito 🛒'}
        </button>
      </div>
    </article>
  );
};
