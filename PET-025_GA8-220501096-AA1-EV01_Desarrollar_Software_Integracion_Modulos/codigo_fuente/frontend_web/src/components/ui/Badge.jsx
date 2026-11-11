import React from 'react';

export function Badge({ children, variant = 'default', className = '' }) {
  const variants = {
    default: 'bg-stone-800 text-stone-300 border-stone-700',
    red: 'bg-red-950/80 text-red-300 border-red-800/60',
    gold: 'bg-amber-950/80 text-amber-300 border-amber-800/60',
    green: 'bg-emerald-950/80 text-emerald-300 border-emerald-800/60',
    blue: 'bg-sky-950/80 text-sky-300 border-sky-800/60',
  };

  return (
    <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium border ${variants[variant] || variants.default} ${className}`}>
      {children}
    </span>
  );
}

export function Card({ children, className = '', hoverEffect = false, ...props }) {
  return (
    <div
      className={`bg-stone-900/90 border border-stone-800/80 rounded-2xl p-5 backdrop-blur-sm ${
        hoverEffect ? 'hover:border-stone-700 hover:shadow-xl hover:shadow-black/50 transition-all duration-300' : ''
      } ${className}`}
      {...props}
    >
      {children}
    </div>
  );
}
