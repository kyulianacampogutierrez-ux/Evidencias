import React from 'react';
import { Card, Badge } from './ui/Badge';
import { Button } from './ui/Button';

export function PizzaCard({ pizza, onSelectPizza }) {
  const precioBase = pizza.precios?.mediana || pizza.precios?.personal || 0;

  return (
    <Card hoverEffect className="flex flex-col justify-between h-full group bg-stone-900/90 border-stone-800/80">
      <div>
        {/* Cabecera / Imagen representativa */}
        <div className="relative aspect-video rounded-xl bg-gradient-to-br from-stone-950 to-stone-900 border border-stone-800/60 flex items-center justify-center overflow-hidden mb-4">
          <span className="text-6xl group-hover:scale-110 transition-transform duration-300">
            {pizza.categoria === 'BEBIDAS' ? '🥤' : pizza.categoria === 'POSTRES' ? '🍮' : '🍕'}
          </span>
          <div className="absolute top-2.5 left-2.5">
            <Badge variant={pizza.categoria === 'GOURMET' ? 'gold' : pizza.categoria === 'ESPECIALES' ? 'red' : 'default'}>
              {pizza.categoria}
            </Badge>
          </div>
          {pizza.destacada && (
            <div className="absolute top-2.5 right-2.5">
              <span className="bg-amber-500 text-stone-950 font-bold text-[10px] px-2 py-0.5 rounded-full uppercase tracking-wider">
                Chef Pick
              </span>
            </div>
          )}
        </div>

        {/* Título & Calificación */}
        <div className="flex items-start justify-between gap-2 mb-2">
          <h3 className="font-['Cinzel'] font-bold text-lg text-white group-hover:text-red-400 transition-colors">
            {pizza.nombre}
          </h3>
          <div className="flex items-center text-xs text-amber-400 font-semibold shrink-0">
            ⭐ {pizza.calificacionPromedio || 4.8}
          </div>
        </div>

        {/* Descripción */}
        <p className="text-xs text-stone-400 font-light leading-relaxed mb-4 line-clamp-2">
          {pizza.descripcion}
        </p>

        {/* Ingredientes clave */}
        {pizza.ingredientes && pizza.ingredientes.length > 0 && (
          <div className="flex flex-wrap gap-1 mb-4">
            {pizza.ingredientes.slice(0, 3).map((ing, idx) => (
              <span key={idx} className="text-[10px] bg-stone-950 text-stone-400 px-2 py-0.5 rounded border border-stone-800/80">
                {ing}
              </span>
            ))}
            {pizza.ingredientes.length > 3 && (
              <span className="text-[10px] text-stone-500 self-center">+{pizza.ingredientes.length - 3}</span>
            )}
          </div>
        )}
      </div>

      {/* Pie: Precios y Acción */}
      <div className="pt-3 border-t border-stone-800/80 flex items-center justify-between gap-3">
        <div>
          <span className="text-[10px] uppercase text-stone-400 block font-medium">Desde</span>
          <span className="text-lg font-bold text-amber-400">
            ${precioBase.toLocaleString('es-CO')}
          </span>
        </div>
        <Button size="sm" variant="default" onClick={() => onSelectPizza(pizza)}>
          Ordenar 🛒
        </Button>
      </div>
    </Card>
  );
}
