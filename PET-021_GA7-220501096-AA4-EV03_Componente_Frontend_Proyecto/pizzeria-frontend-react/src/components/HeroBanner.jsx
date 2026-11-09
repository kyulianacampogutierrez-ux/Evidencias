/**
 * HeroBanner - Banner Principal Promocional de la Pizzería
 * 
 * Presenta el llamado a la acción inicial, la propuesta de valor
 * de la masa madre horneada en piedra y la insignia de envío gratis.
 * 
 * Aprendiz: Karen Yuliana Campo - SENA ADSO Ficha 228118
 */

import React from 'react';

export const HeroBanner = ({ onExploreMenu }) => {
  return (
    <section className="hero-banner" aria-labelledby="hero-title">
      <div className="hero-overlay"></div>
      <div className="hero-content">
        <span className="hero-tag">🔥 AUTÉNTICA PIZZA NAPOLITANA &bull; POPAYÁN</span>
        <h1 id="hero-title" className="hero-title">
          Tradición Italiana Hecha con Pasión y Fuego
        </h1>
        <p className="hero-desc">
          Masa madre fermentada durante 48 horas, ingredientes importados con denominación de origen
          y horneada en piso refractario a 450°C.
        </p>

        <div className="hero-features">
          <div className="feature-pill">🚚 Domicilios Rápidos</div>
          <div className="feature-pill highlight">✨ Envío GRATIS sobre $50.000</div>
          <div className="feature-pill">🧀 100% Quesos Madurados</div>
        </div>

        <div className="hero-actions">
          <button className="btn-hero-primary" onClick={onExploreMenu}>
            Pedir en Línea Ahora 🍕
          </button>
          <a href="#promociones" className="btn-hero-secondary">
            Ver Ofertas del Día
          </a>
        </div>
      </div>
    </section>
  );
};
