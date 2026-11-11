import React, { useState, useEffect } from 'react';
import { api } from '../services/api';
import { PizzaCard } from './PizzaCard';
import { PizzaModal } from './PizzaModal';

export function CartaMenu() {
  const [categorias, setCategorias] = useState([]);
  const [pizzas, setPizzas] = useState([]);
  const [selectedCategoria, setSelectedCategoria] = useState('');
  const [searchTerm, setSearchTerm] = useState('');
  const [activePizzaModal, setActivePizzaModal] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    Promise.all([
      api.getCategorias(),
      api.getPizzas(selectedCategoria, searchTerm)
    ]).then(([catRes, pizRes]) => {
      if (catRes.success) setCategorias(catRes.categorias || []);
      if (pizRes.success) setPizzas(pizRes.pizzas || []);
    }).finally(() => setLoading(false));
  }, [selectedCategoria, searchTerm]);

  return (
    <section className="py-12 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      {/* Encabezado de la Carta */}
      <div className="text-center max-w-2xl mx-auto mb-10">
        <span className="text-xs font-bold uppercase tracking-widest text-red-500 bg-red-950/60 px-3 py-1 rounded-full border border-red-800/40">
          Nuestra Carta Artesanal
        </span>
        <h2 className="font-['Cinzel'] text-3xl sm:text-4xl font-black text-white mt-3">
          Elige tu Sabor Favorito
        </h2>
        <p className="text-sm text-stone-400 font-light mt-2">
          Ingredientes frescos de temporada, masa madre fermentada lentamente y horneadas a la leña en Popayán.
        </p>
      </div>

      {/* FILTROS Y BUSCADOR */}
      <div className="flex flex-col md:flex-row items-center justify-between gap-4 mb-8">
        
        {/* Pestañas de categorías */}
        <div className="flex flex-wrap gap-2 overflow-x-auto pb-2 w-full md:w-auto">
          <button
            onClick={() => setSelectedCategoria('')}
            className={`px-4 py-2 rounded-xl text-xs font-semibold transition-all ${
              selectedCategoria === ''
                ? 'bg-red-600 text-white shadow-lg shadow-red-900/40'
                : 'bg-stone-900 text-stone-300 hover:bg-stone-800 border border-stone-800'
            }`}
          >
            🍕 Todas ({pizzas.length})
          </button>
          {categorias.map(cat => (
            <button
              key={cat.codigo}
              onClick={() => setSelectedCategoria(cat.codigo)}
              className={`px-4 py-2 rounded-xl text-xs font-semibold transition-all ${
                selectedCategoria === cat.codigo
                  ? 'bg-red-600 text-white shadow-lg shadow-red-900/40'
                  : 'bg-stone-900 text-stone-300 hover:bg-stone-800 border border-stone-800'
              }`}
            >
              {cat.nombre}
            </button>
          ))}
        </div>

        {/* Buscador en tiempo real */}
        <div className="relative w-full md:w-72">
          <input
            type="text"
            placeholder="Buscar por ingrediente o pizza..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full bg-stone-900 border border-stone-800 rounded-xl px-4 py-2.5 text-xs text-white placeholder-stone-500 focus:outline-none focus:border-red-500 focus:ring-1 focus:ring-red-500"
          />
          {searchTerm && (
            <button
              onClick={() => setSearchTerm('')}
              className="absolute right-3 top-1/2 -translate-y-1/2 text-stone-400 hover:text-white text-xs font-bold"
            >
              ✕
            </button>
          )}
        </div>

      </div>

      {/* GRID DE PIZZAS */}
      {loading ? (
        <div className="text-center py-20 text-stone-400">
          <div className="inline-block animate-spin text-4xl mb-3">🍕</div>
          <p className="text-sm">Cargando la carta desde MongoDB...</p>
        </div>
      ) : pizzas.length === 0 ? (
        <div className="text-center py-20 bg-stone-900/40 rounded-3xl border border-stone-800 p-8">
          <span className="text-5xl block mb-3">🔍</span>
          <h3 className="font-['Cinzel'] text-xl font-bold text-white">No se encontraron productos</h3>
          <p className="text-xs text-stone-400 mt-1">Prueba seleccionando otra categoría o término de búsqueda.</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {pizzas.map(pizza => (
            <PizzaCard
              key={pizza.codigo}
              pizza={pizza}
              onSelectPizza={(p) => setActivePizzaModal(p)}
            />
          ))}
        </div>
      )}

      {/* MODAL DE PERSONALIZACIÓN Y COMPRA */}
      {activePizzaModal && (
        <PizzaModal
          pizza={activePizzaModal}
          onClose={() => setActivePizzaModal(null)}
        />
      )}
    </section>
  );
}
