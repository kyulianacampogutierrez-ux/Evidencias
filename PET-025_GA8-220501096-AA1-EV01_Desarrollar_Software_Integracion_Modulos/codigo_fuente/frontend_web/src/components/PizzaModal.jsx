import React, { useState } from 'react';
import { Button } from './ui/Button';
import { Badge } from './ui/Badge';
import { useCart } from '../context/CartContext';

export function PizzaModal({ pizza, onClose }) {
  const { addItem } = useCart();
  const [tamano, setTamano] = useState('mediana');
  const [selectedAdiciones, setSelectedAdiciones] = useState([]);
  const [cantidad, setCantidad] = useState(1);

  if (!pizza) return null;

  const precios = pizza.precios || { personal: 25000, mediana: 35000, familiar: 45000 };
  const precioBase = precios[tamano] || precios.mediana;
  const precioAdiciones = selectedAdiciones.reduce((acc, ad) => acc + ad.precio, 0);
  const totalCalculado = (precioBase + precioAdiciones) * cantidad;

  const toggleAdicion = (adicion) => {
    setSelectedAdiciones(prev => {
      const exists = prev.some(a => a.nombre === adicion.nombre);
      if (exists) {
        return prev.filter(a => a.nombre !== adicion.nombre);
      } else {
        return [...prev, adicion];
      }
    });
  };

  const handleAddToCart = () => {
    addItem(pizza, tamano, selectedAdiciones, cantidad);
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm animate-fadeIn">
      <div className="relative w-full max-w-lg bg-stone-900 border border-stone-800 rounded-3xl p-6 shadow-2xl overflow-y-auto max-h-[90vh]">
        
        {/* Botón cerrar */}
        <button
          onClick={onClose}
          className="absolute top-4 right-4 w-9 h-9 rounded-full bg-stone-800 hover:bg-stone-700 text-stone-300 hover:text-white flex items-center justify-center text-sm font-bold transition-colors"
        >
          ✕
        </button>

        {/* Encabezado */}
        <div className="flex items-start gap-4 mb-5">
          <div className="w-16 h-16 rounded-2xl bg-stone-950 border border-stone-800 flex items-center justify-center text-4xl shrink-0">
            {pizza.categoria === 'BEBIDAS' ? '🥤' : pizza.categoria === 'POSTRES' ? '🍮' : '🍕'}
          </div>
          <div>
            <Badge variant="red" className="mb-1">{pizza.categoria}</Badge>
            <h2 className="font-['Cinzel'] text-xl font-bold text-white">{pizza.nombre}</h2>
            <p className="text-xs text-stone-400 mt-1">{pizza.descripcion}</p>
          </div>
        </div>

        {/* SELECCIÓN DE TAMAÑO (Solo si aplica) */}
        {pizza.categoria !== 'BEBIDAS' && pizza.categoria !== 'POSTRES' && (
          <div className="space-y-2 mb-6">
            <label className="text-xs font-bold uppercase tracking-wider text-stone-300 block">
              1. Selecciona el Tamaño:
            </label>
            <div className="grid grid-cols-3 gap-2">
              {[
                { id: 'personal', label: 'Personal', desc: '4 porciones (20cm)', precio: precios.personal },
                { id: 'mediana', label: 'Mediana', desc: '8 porciones (30cm)', precio: precios.mediana },
                { id: 'familiar', label: 'Familiar', desc: '12 porciones (40cm)', precio: precios.familiar },
              ].map(item => (
                <button
                  key={item.id}
                  onClick={() => setTamano(item.id)}
                  className={`p-3 rounded-xl border text-left transition-all ${
                    tamano === item.id
                      ? 'border-red-600 bg-red-950/40 text-white ring-1 ring-red-500'
                      : 'border-stone-800 bg-stone-950/60 text-stone-400 hover:border-stone-700'
                  }`}
                >
                  <p className="text-xs font-bold text-stone-200">{item.label}</p>
                  <p className="text-[10px] text-stone-400 mt-0.5">{item.desc}</p>
                  <p className="text-xs font-semibold text-amber-400 mt-1">${item.precio?.toLocaleString('es-CO')}</p>
                </button>
              ))}
            </div>
          </div>
        )}

        {/* ADICIONES Y BORDES ESPECIALES */}
        {pizza.adicionesDisponibles && pizza.adicionesDisponibles.length > 0 && (
          <div className="space-y-2 mb-6">
            <label className="text-xs font-bold uppercase tracking-wider text-stone-300 block">
              2. Adiciones e Ingredientes Extra (Opcional):
            </label>
            <div className="space-y-2">
              {pizza.adicionesDisponibles.map((adicion, idx) => {
                const isSelected = selectedAdiciones.some(a => a.nombre === adicion.nombre);
                return (
                  <label
                    key={idx}
                    className={`flex items-center justify-between p-3 rounded-xl border cursor-pointer transition-all ${
                      isSelected
                        ? 'border-amber-500/80 bg-amber-950/20 text-white'
                        : 'border-stone-800 bg-stone-950/40 text-stone-300 hover:border-stone-700'
                    }`}
                  >
                    <div className="flex items-center gap-3">
                      <input
                        type="checkbox"
                        checked={isSelected}
                        onChange={() => toggleAdicion(adicion)}
                        className="rounded border-stone-700 text-red-600 focus:ring-red-500 bg-stone-900 w-4 h-4"
                      />
                      <span className="text-xs font-medium">{adicion.nombre}</span>
                    </div>
                    <span className="text-xs font-bold text-amber-400">+${adicion.precio.toLocaleString('es-CO')}</span>
                  </label>
                );
              })}
            </div>
          </div>
        )}

        {/* CANTIDAD Y PRECIO FINAL */}
        <div className="pt-4 border-t border-stone-800/80 flex items-center justify-between gap-4">
          <div className="flex items-center gap-3 bg-stone-950 p-1.5 rounded-xl border border-stone-800">
            <button
              onClick={() => setCantidad(Math.max(1, cantidad - 1))}
              className="w-8 h-8 rounded-lg bg-stone-900 hover:bg-stone-800 text-stone-300 hover:text-white flex items-center justify-center font-bold text-base"
            >
              -
            </button>
            <span className="font-bold text-sm text-white w-6 text-center">{cantidad}</span>
            <button
              onClick={() => setCantidad(cantidad + 1)}
              className="w-8 h-8 rounded-lg bg-stone-900 hover:bg-stone-800 text-stone-300 hover:text-white flex items-center justify-center font-bold text-base"
            >
              +
            </button>
          </div>

          <div className="flex-1 text-right">
            <span className="text-[10px] uppercase text-stone-400 block font-medium">Total</span>
            <span className="text-xl font-black text-amber-400 font-['Cinzel']">
              ${totalCalculado.toLocaleString('es-CO')}
            </span>
          </div>
        </div>

        <Button size="lg" variant="default" className="w-full mt-5" onClick={handleAddToCart}>
          Agregar al Carrito 🛒
        </Button>

      </div>
    </div>
  );
}
