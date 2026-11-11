import React from 'react';

export function Button({
  children,
  variant = 'default',
  size = 'md',
  className = '',
  disabled = false,
  onClick,
  type = 'button',
  ...props
}) {
  const baseStyles = 'inline-flex items-center justify-center font-medium transition-all duration-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed active:scale-[0.98]';

  const variants = {
    default: 'bg-red-600 hover:bg-red-700 text-white shadow-lg shadow-red-900/30 focus:ring-red-500',
    gold: 'bg-amber-500 hover:bg-amber-600 text-stone-950 font-semibold shadow-lg shadow-amber-900/30 focus:ring-amber-400',
    outline: 'border border-stone-700 hover:border-stone-500 bg-transparent text-stone-200 hover:bg-stone-800 focus:ring-stone-400',
    ghost: 'bg-transparent hover:bg-stone-800 text-stone-300 hover:text-white',
    destructive: 'bg-rose-700 hover:bg-rose-800 text-white focus:ring-rose-500',
    secondary: 'bg-stone-800 hover:bg-stone-700 text-stone-100 border border-stone-700'
  };

  const sizes = {
    sm: 'text-xs px-2.5 py-1.5 gap-1.5',
    md: 'text-sm px-4 py-2.5 gap-2',
    lg: 'text-base px-6 py-3 gap-2.5 font-semibold'
  };

  return (
    <button
      type={type}
      disabled={disabled}
      onClick={onClick}
      className={`${baseStyles} ${variants[variant] || variants.default} ${sizes[size] || sizes.md} ${className}`}
      {...props}
    >
      {children}
    </button>
  );
}
