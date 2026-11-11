import React from 'react';
import { useAuth } from '../context/AuthContext';
import { useCart } from '../context/CartContext';
import { Button } from './ui/Button';

export function Navbar({ activeTab, setActiveTab, onOpenAuthModal }) {
  const { user, isAuthenticated, isAdmin, logout } = useAuth();
  const { totalItemsCount, openCart } = useCart();

  return (
    <header className="sticky top-0 z-40 w-full border-b border-stone-800/80 bg-stone-950/90 backdrop-blur-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
        
        {/* LOGO */}
        <div 
          onClick={() => setActiveTab('inicio')}
          className="flex items-center gap-3 cursor-pointer group"
        >
          <div className="w-12 h-12 rounded-2xl bg-gradient-to-br from-red-600 to-amber-600 flex items-center justify-center text-2xl shadow-lg shadow-red-900/30 group-hover:scale-105 transition-transform">
            🍕
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="font-['Cinzel'] text-xl sm:text-2xl font-bold tracking-wider text-white">
                Bella <span className="text-red-500">Italia</span>
              </span>
              <span className="text-[10px] font-bold px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-400 border border-amber-500/40">
                SENA ADSO
              </span>
            </div>
            <p className="text-xs text-stone-400 font-light">Pizzería Artesanal • Popayán</p>
          </div>
        </div>

        {/* NAVEGACIÓN PRINCIPAL */}
        <nav className="hidden md:flex items-center gap-1 bg-stone-900/60 p-1.5 rounded-full border border-stone-800">
          <button
            onClick={() => setActiveTab('inicio')}
            className={`px-4 py-2 rounded-full text-sm font-medium transition-all ${
              activeTab === 'inicio' ? 'bg-red-600 text-white shadow-md' : 'text-stone-300 hover:text-white hover:bg-stone-800/60'
            }`}
          >
            Inicio
          </button>
          <button
            onClick={() => setActiveTab('carta')}
            className={`px-4 py-2 rounded-full text-sm font-medium transition-all ${
              activeTab === 'carta' ? 'bg-red-600 text-white shadow-md' : 'text-stone-300 hover:text-white hover:bg-stone-800/60'
            }`}
          >
            Carta & Menú
          </button>
          <button
            onClick={() => setActiveTab('estados')}
            className={`px-4 py-2 rounded-full text-sm font-medium transition-all ${
              activeTab === 'estados' ? 'bg-red-600 text-white shadow-md' : 'text-stone-300 hover:text-white hover:bg-stone-800/60'
            }`}
          >
            Seguimiento Pedido
          </button>
          <button
            onClick={() => setActiveTab('clientes')}
            className={`px-4 py-2 rounded-full text-sm font-medium transition-all ${
              activeTab === 'clientes' ? 'bg-red-600 text-white shadow-md' : 'text-stone-300 hover:text-white hover:bg-stone-800/60'
            }`}
          >
            Mi Cuenta
          </button>
          {isAdmin && (
            <button
              onClick={() => setActiveTab('admin')}
              className={`px-4 py-2 rounded-full text-sm font-semibold transition-all ${
                activeTab === 'admin' ? 'bg-amber-500 text-stone-950 shadow-md' : 'text-amber-400 hover:text-amber-300 hover:bg-amber-950/30'
              }`}
            >
              Panel Admin ⚙️
            </button>
          )}
        </nav>

        {/* ACCIONES DERECHA: CARRITO & SESIÓN */}
        <div className="flex items-center gap-3">
          {/* BOTÓN CARRITO */}
          <button
            onClick={openCart}
            className="relative p-2.5 rounded-xl bg-stone-900 hover:bg-stone-800 border border-stone-800 text-stone-200 hover:text-white transition-all active:scale-95"
            title="Ver carrito de compras"
          >
            <span className="text-xl">🛒</span>
            {totalItemsCount > 0 && (
              <span className="absolute -top-1.5 -right-1.5 bg-red-600 text-white text-xs font-bold w-5 h-5 rounded-full flex items-center justify-center animate-pulse">
                {totalItemsCount}
              </span>
            )}
          </button>

          {/* ESTADO USUARIO */}
          {isAuthenticated ? (
            <div className="flex items-center gap-2">
              <button
                onClick={() => setActiveTab('clientes')}
                className="flex items-center gap-2 p-1.5 pr-3 rounded-xl bg-stone-900 border border-stone-800 hover:border-stone-700 text-left"
              >
                <div className="w-8 h-8 rounded-lg bg-red-950 text-red-400 font-bold flex items-center justify-center text-sm border border-red-800/60">
                  {user?.nombre ? user.nombre.charAt(0).toUpperCase() : 'U'}
                </div>
                <div className="hidden lg:block">
                  <p className="text-xs font-semibold text-stone-200 leading-none">{user?.nombre?.split(' ')[0]}</p>
                  <span className="text-[10px] text-stone-400 uppercase">{user?.rol}</span>
                </div>
              </button>
              <Button size="sm" variant="ghost" onClick={logout} title="Cerrar sesión">
                Cerrar
              </Button>
            </div>
          ) : (
            <Button size="sm" variant="default" onClick={onOpenAuthModal}>
              Ingresar / Registro
            </Button>
          )}
        </div>

      </div>

      {/* Menú inferior responsive móvil */}
      <div className="md:hidden flex items-center justify-around bg-stone-900/90 border-t border-stone-800 py-2 px-1 text-xs">
        <button onClick={() => setActiveTab('inicio')} className={`px-2 py-1 rounded ${activeTab === 'inicio' ? 'text-red-400 font-bold' : 'text-stone-400'}`}>Inicio</button>
        <button onClick={() => setActiveTab('carta')} className={`px-2 py-1 rounded ${activeTab === 'carta' ? 'text-red-400 font-bold' : 'text-stone-400'}`}>Carta</button>
        <button onClick={() => setActiveTab('estados')} className={`px-2 py-1 rounded ${activeTab === 'estados' ? 'text-red-400 font-bold' : 'text-stone-400'}`}>Tracking</button>
        <button onClick={() => setActiveTab('clientes')} className={`px-2 py-1 rounded ${activeTab === 'clientes' ? 'text-red-400 font-bold' : 'text-stone-400'}`}>Cuenta</button>
        {isAdmin && <button onClick={() => setActiveTab('admin')} className={`px-2 py-1 rounded ${activeTab === 'admin' ? 'text-amber-400 font-bold' : 'text-stone-400'}`}>Admin</button>}
      </div>
    </header>
  );
}
