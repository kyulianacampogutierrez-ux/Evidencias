/**
 * CategoryFilter - Selector de Categorías y Buscador en Tiempo Real
 * 
 * Molécula que permite al usuario filtrar las variedades de pizza
 * y buscar mediante un input de texto interactivo.
 * 
 * Aprendiz: Karen Yuliana Campo - SENA ADSO Ficha 228118
 */

import React from 'react';

export const CategoryFilter = ({
  categories = ['Todas', 'Tradicionales', 'Especiales', 'Gourmet'],
  selectedCategory = 'Todas',
  onSelectCategory,
  searchTerm = '',
  onSearchChange
}) => {
  return (
    <div className="filter-bar" role="search" aria-label="Filtrado y búsqueda de menú">
      {/* Pills de Categorías */}
      <div className="category-pills" role="tablist" aria-label="Categorías de pizza">
        {categories.map((cat) => {
          const isSelected = selectedCategory === cat;
          return (
            <button
              key={cat}
              role="tab"
              aria-selected={isSelected}
              className={`pill-btn ${isSelected ? 'active' : ''}`}
              onClick={() => onSelectCategory && onSelectCategory(cat)}
            >
              {cat === 'Todas' && '✨ '}
              {cat === 'Tradicionales' && '🍕 '}
              {cat === 'Especiales' && '🌶️ '}
              {cat === 'Gourmet' && '⭐ '}
              {cat}
            </button>
          );
        })}
      </div>

      {/* Input de Búsqueda Reactivo */}
      <div className="search-box">
        <span className="search-icon" aria-hidden="true">🔍</span>
        <input
          type="text"
          className="search-input"
          placeholder="Buscar pizza o ingrediente..."
          value={searchTerm}
          onChange={(e) => onSearchChange && onSearchChange(e.target.value)}
          aria-label="Buscar pizza por nombre o ingredientes"
        />
        {searchTerm && (
          <button
            className="clear-search-btn"
            onClick={() => onSearchChange && onSearchChange('')}
            aria-label="Limpiar búsqueda"
          >
            ✕
          </button>
        )}
      </div>
    </div>
  );
};
