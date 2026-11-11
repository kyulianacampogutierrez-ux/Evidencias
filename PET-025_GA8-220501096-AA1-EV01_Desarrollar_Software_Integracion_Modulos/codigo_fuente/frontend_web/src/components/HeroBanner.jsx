import React from 'react';
import { Button } from './ui/Button';
import { Badge } from './ui/Badge';

export function HeroBanner({ onGoToCarta, onOpenTracking }) {
  return (
    <div className="relative overflow-hidden pt-8 pb-16 lg:pt-14 lg:pb-24">
      {/* Glow de fondo decorativo */}
      <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[350px] bg-red-600/15 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute top-1/3 right-10 w-[300px] h-[300px] bg-amber-500/10 rounded-full blur-3xl pointer-events-none" />

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
          
          {/* COLUMNA IZQUIERDA: MENSAJE PRINCIPAL */}
          <div className="lg:col-span-7 space-y-6 text-center lg:text-left">
            <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-stone-900 border border-stone-800 text-xs font-medium text-amber-400">
              <span className="animate-pulse">🔥</span> Horno de Leña a 380°C • Sabor Napolitano en Popayán
            </div>

            <h1 className="font-['Cinzel'] text-4xl sm:text-5xl lg:text-6xl font-black tracking-tight text-white leading-tight">
              Auténtica Pasión Italiana en Cada <span className="text-transparent bg-clip-text bg-gradient-to-r from-red-500 via-amber-500 to-yellow-400">Porción</span>
            </h1>

            <p className="text-base sm:text-lg text-stone-300 max-w-2xl font-light leading-relaxed">
              Masa madre con 48 horas de fermentación lenta, salsa pomodoro San Marzano y queso mozzarella di bufala fundido a la perfección. Pide en línea y sigue tu entrega en tiempo real.
            </p>

            {/* BANNER CUPÓN PROMO */}
            <div className="p-4 rounded-xl bg-gradient-to-r from-red-950/60 via-stone-900 to-stone-900 border border-red-900/50 flex flex-col sm:flex-row items-center justify-between gap-3 text-left">
              <div>
                <p className="text-xs uppercase tracking-wider text-red-400 font-bold">Promoción Exclusiva</p>
                <p className="text-sm font-semibold text-white">15% de Descuento con el cupón <span className="text-amber-400 font-mono font-bold bg-stone-950 px-2 py-0.5 rounded border border-amber-500/30">SENA2026</span></p>
              </div>
              <Badge variant="gold">Válido en Popayán</Badge>
            </div>

            {/* BOTONES DE ACCIÓN */}
            <div className="flex flex-wrap items-center justify-center lg:justify-start gap-4 pt-2">
              <Button size="lg" variant="default" onClick={onGoToCarta} className="w-full sm:w-auto">
                Ver Carta y Pedir Ahora 🍕
              </Button>
              <Button size="lg" variant="outline" onClick={onOpenTracking} className="w-full sm:w-auto">
                Rastrear mi Pedido 📍
              </Button>
            </div>

            {/* BADGES METRICAS */}
            <div className="grid grid-cols-3 gap-4 pt-6 border-t border-stone-800/80">
              <div>
                <p className="font-['Cinzel'] text-2xl font-bold text-white">48h</p>
                <p className="text-xs text-stone-400">Fermentación natural</p>
              </div>
              <div>
                <p className="font-['Cinzel'] text-2xl font-bold text-amber-400">100%</p>
                <p className="text-xs text-stone-400">Mozzarella artesanal</p>
              </div>
              <div>
                <p className="font-['Cinzel'] text-2xl font-bold text-red-400">30-45m</p>
                <p className="text-xs text-stone-400">Entrega rápida Popayán</p>
              </div>
            </div>

          </div>

          {/* COLUMNA DERECHA: TARJETA HERO PIZZA DESTACADA */}
          <div className="lg:col-span-5 flex justify-center">
            <div className="relative w-full max-w-md p-6 rounded-3xl bg-gradient-to-b from-stone-900 to-stone-950 border border-stone-800 shadow-2xl shadow-red-950/40">
              
              <div className="relative aspect-square rounded-2xl bg-stone-950 flex items-center justify-center overflow-hidden border border-stone-800/60 group">
                <div className="text-9xl transition-transform duration-500 group-hover:scale-110 group-hover:rotate-6">
                  🍕
                </div>
                <div className="absolute top-3 left-3">
                  <Badge variant="red">Más Vendida</Badge>
                </div>
                <div className="absolute bottom-3 right-3 bg-stone-950/80 backdrop-blur-md px-3 py-1.5 rounded-xl border border-stone-800 text-xs text-amber-400 font-semibold flex items-center gap-1">
                  ⭐ 5.0 (215 reseñas)
                </div>
              </div>

              <div className="mt-5 space-y-2">
                <div className="flex justify-between items-baseline">
                  <h3 className="font-['Cinzel'] text-xl font-bold text-white">Pizza Cuatro Quesos Di Bufala</h3>
                  <span className="text-amber-400 font-bold text-lg">$48.000</span>
                </div>
                <p className="text-xs text-stone-400 line-clamp-2">
                  Mozzarella fresca, Gorgonzola DOP, Provolone ahumado, Parmesano Reggiano 24 meses y toque de miel de trufa negra.
                </p>
                <Button variant="gold" size="md" className="w-full mt-3" onClick={onGoToCarta}>
                  Personalizar y Agregar al Carrito
                </Button>
              </div>

            </div>
          </div>

        </div>
      </div>
    </div>
  );
}
