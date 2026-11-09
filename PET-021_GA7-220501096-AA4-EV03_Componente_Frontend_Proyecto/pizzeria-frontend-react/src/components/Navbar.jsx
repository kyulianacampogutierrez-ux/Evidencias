/**
 * Navbar - Barra de Navegación Principal y Control de Roles
 * 
 * Organismo que contiene:
 * - Identidad corporativa de la Pizzería Bella Italia
 * - Enlaces de navegación con scroll suave
 * - Selector interactivo de rol (CLIENTE vs ADMINISTRADOR)
 * - Botón de acceso al carrito con contador reactivo
 * 
 * Aprendiz: Karen Yuliana Campo - SENA ADSO Ficha 228118
 */

import React, { useState } from 'react';
import { useCart } from '../context/CartContext.jsx';
import { useAuth } from '../context/AuthContext.jsx';

export const Navbar = ({ brandName = 'Pizzería Bella Italia', activeSection = 'menu', onNavigate }) => {
  const { totalItems, setIsDrawerOpen } = useCart();
  const { role, toggleRole } = useAuth();
  const [isMobileOpen, setIsMobileOpen] = useState(false);

  return (
    <header className="navbar-header" role="banner">
      <div className="navbar-container">
        {/* Logotipo y Marca */}
        <div className="navbar-brand" onClick={() => onNavigate && onNavigate('menu')}>
          <span className="brand-icon" aria-hidden="true">🍕</span>
          <div className="brand-text">
            <span className="brand-title">{brandName}</span>
            <span className="brand-subtitle">Trattoria & Forno a Legna</span>
          </div>
        </div>

        {/* Botón de Menú Hamburguesa para Móviles */}
        <button
          className="mobile-toggle"
          onClick={() => setIsMobileOpen(!isMobileOpen)}
          aria-expanded={isMobileOpen}
          aria-label="Alternar navegación"
        >
          {isMobileOpen ? '✕' : '☰'}
        </button>

        {/* Navegación y Acciones */}
        <nav className={`navbar-nav ${isMobileOpen ? 'open' : ''}`} aria-label="Navegación principal">
          <button
            className={`nav-link ${activeSection === 'menu' ? 'active' : ''}`}
            onClick={() => {
              onNavigate && onNavigate('menu');
              setIsMobileOpen(false);
            }}
          >
            Menú Tradicional
          </button>

          <button
            className={`nav-link ${activeSection === 'cocina' ? 'active' : ''}`}
            onClick={() => {
              onNavigate && onNavigate('cocina');
              setIsMobileOpen(false);
            }}
          >
            Comandas & Cocina
          </button>

          <button
            className={`nav-link ${activeSection === 'kpis' ? 'active' : ''}`}
            onClick={() => {
              onNavigate && onNavigate('kpis');
              setIsMobileOpen(false);
            }}
          >
            Métricas KPI
          </button>

          {/* Selector de Rol */}
          <button
            className={`role-toggle-btn ${role === 'ADMIN' ? 'admin' : 'cliente'}`}
            onClick={toggleRole}
            title="Alternar entre modo Cliente y modo Administrador/Cocina"
          >
            Rol: <strong>{role}</strong>
          </button>

          {/* Botón de Carrito con Contador Reactivo */}
          <button
            className="cart-button"
            onClick={() => setIsDrawerOpen(true)}
            aria-label={`Ver carrito de compras con ${totalItems} productos`}
          >
            <span className="cart-icon" aria-hidden="true">🛒</span>
            <span className="cart-label">Carrito</span>
            {totalItems > 0 && <span className="cart-badge">{totalItems}</span>}
          </button>
        </nav>
      </div>
    </header>
  );
};
