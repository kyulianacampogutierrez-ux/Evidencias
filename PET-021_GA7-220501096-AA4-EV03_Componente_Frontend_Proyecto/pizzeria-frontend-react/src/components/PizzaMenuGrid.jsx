/**
 * PizzaMenuGrid - Rejilla Responsiva del Menú de Pizzas
 * 
 * Organismo que itera sobre la colección de pizzas filtradas y renderiza
 * componentes PizzaCard individuales asignando claves inmutables.
 * 
 * Aprendiz: Karen Yuliana Campo - SENA ADSO Ficha 228118
 */

import React from 'react';
import { PizzaCard } from './PizzaCard.jsx';

export const PizzaMenuGrid = ({ pizzas = [], loading = false, onAddToCart }) => {
  if (loading) {
    return (
      <div className="grid-loading" aria-live="polite">
        <div className="spinner"></div>
        <p>Horneando el catálogo de pizzas en vivo...</p>
      </div>
    );
  }

  if (pizzas.length === 0) {
    return (
      <div className="grid-empty" role="alert">
        <span className="empty-icon">🍕</span>
        <h3>No encontramos pizzas que coincidan con tu búsqueda</h3>
        <p>Prueba seleccionando otra categoría o limpiando los términos de búsqueda.</p>
      </div>
    );
  }

  return (
    <section className="menu-grid-section" aria-label="Catálogo de pizzas disponibles">
      <div className="menu-grid">
        {pizzas.map((pizza) => (
          <PizzaCard
            key={pizza.idPizza}
            pizza={pizza}
            onAddToCart={onAddToCart}
          />
        ))}
      </div>
    </section>
  );
};
