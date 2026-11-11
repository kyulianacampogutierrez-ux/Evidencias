import React, { useState } from 'react';
import { useCart } from '../context/CartContext';
import { Button } from './ui/Button';

export function CartDrawer({ onProceedToCheckout }) {
  const {
    items,
    removeItem,
    updateQuantity,
    clearCart,
    isCartOpen,
    closeCart,
    subtotal,
    costoEnvio,
    coupon,
    descuentoValor,
    total,
    applyCoupon,
    removeCoupon,
  } = useCart();

  const [couponCode, setCouponCode] = useState('');
  const [couponMessage, setCouponMessage] = useState(null);

  if (!isCartOpen) return null;

  const handleApplyCoupon = async (e) => {
    e.preventDefault();
    if (!couponCode.trim()) return;
    const res = await applyCoupon(couponCode);
    setCouponMessage(res);
    if (res.ok) setCouponCode('');
  };

  return (
    <div className="fixed inset-0 z-50 overflow-hidden">
      {/* Fondo oscuro con clic para cerrar */}
      <div
        onClick={closeCart}
        className="absolute inset-0 bg-black/75 backdrop-blur-sm transition-opacity"
      />

      <div className="fixed inset-y-0 right-0 max-w-full flex pl-10">
        <div className="w-screen max-w-md bg-stone-900 border-l border-stone-800 flex flex-col shadow-2xl">
          
          {/* ENCABEZADO */}
          <div className="p-5 border-b border-stone-800/80 flex items-center justify-between">
            <div className="flex items-center gap-2">
              <span className="text-2xl">🛒</span>
              <h2 className="font-['Cinzel'] text-lg font-bold text-white">Tu Carrito de Compras</h2>
            </div>
            <button
              onClick={closeCart}
              className="w-8 h-8 rounded-full bg-stone-800 hover:bg-stone-700 text-stone-300 hover:text-white flex items-center justify-center text-xs font-bold"
            >
              ✕
            </button>
          </div>

          {/* LISTADO DE ITEMS */}
          <div className="flex-1 overflow-y-auto p-5 space-y-4">
            {items.length === 0 ? (
              <div className="text-center py-20 text-stone-400 space-y-3">
                <span className="text-6xl block">🍕</span>
                <p className="font-['Cinzel'] text-base font-bold text-stone-200">Tu carrito está vacío</p>
                <p className="text-xs text-stone-400">Descubre nuestra deliciosa carta y agrega tus pizzas favoritas.</p>
              </div>
            ) : (
              items.map((item, idx) => (
                <div
                  key={idx}
                  className="p-3.5 rounded-2xl bg-stone-950/70 border border-stone-800/80 flex items-start gap-3 relative group"
                >
                  <div className="w-12 h-12 rounded-xl bg-stone-900 flex items-center justify-center text-2xl shrink-0">
                    🍕
                  </div>
                  <div className="flex-1 min-w-0">
                    <div className="flex justify-between items-start gap-2">
                      <h4 className="font-semibold text-xs text-white truncate">{item.nombre}</h4>
                      <button
                        onClick={() => removeItem(idx)}
                        className="text-stone-500 hover:text-rose-400 text-xs transition-colors"
                        title="Eliminar producto"
                      >
                        ✕
                      </button>
                    </div>
                    <p className="text-[10px] text-amber-400 uppercase font-medium mt-0.5">
                      Tamaño: {item.tamano}
                    </p>
                    {item.adiciones && item.adiciones.length > 0 && (
                      <p className="text-[10px] text-stone-400 truncate mt-0.5">
                        +{item.adiciones.join(', ')}
                      </p>
                    )}

                    <div className="flex items-center justify-between mt-2.5">
                      <div className="flex items-center gap-2 bg-stone-900 px-2 py-1 rounded-lg border border-stone-800">
                        <button
                          onClick={() => updateQuantity(idx, -1)}
                          className="text-xs text-stone-400 hover:text-white font-bold w-4"
                        >
                          -
                        </button>
                        <span className="text-xs font-bold text-white px-1">{item.cantidad}</span>
                        <button
                          onClick={() => updateQuantity(idx, 1)}
                          className="text-xs text-stone-400 hover:text-white font-bold w-4"
                        >
                          +
                        </button>
                      </div>
                      <span className="font-bold text-xs text-white">
                        ${item.totalItem?.toLocaleString('es-CO')}
                      </span>
                    </div>
                  </div>
                </div>
              ))
            )}
          </div>

          {/* CUPÓN DE DESCUENTO Y RESUMEN DE PAGO */}
          {items.length > 0 && (
            <div className="p-5 border-t border-stone-800/80 bg-stone-950/60 space-y-4">
              
              {/* Formulario de Cupón */}
              <form onSubmit={handleApplyCoupon} className="space-y-1.5">
                <div className="flex gap-2">
                  <input
                    type="text"
                    placeholder="Código de Cupón (ej: SENA2026)"
                    value={couponCode}
                    onChange={(e) => setCouponCode(e.target.value)}
                    className="flex-1 bg-stone-900 border border-stone-800 rounded-xl px-3 py-2 text-xs text-white uppercase placeholder-stone-500 focus:outline-none focus:border-amber-500"
                  />
                  <Button type="submit" size="sm" variant="outline">
                    Aplicar
                  </Button>
                </div>
                {coupon && (
                  <div className="flex items-center justify-between text-[11px] text-emerald-400 bg-emerald-950/30 p-2 rounded-lg border border-emerald-900/40">
                    <span>Cupón {coupon.codigo} (-{coupon.porcentaje}%)</span>
                    <button type="button" onClick={removeCoupon} className="text-xs font-bold hover:underline">
                      Quitar
                    </button>
                  </div>
                )}
                {couponMessage && !coupon && (
                  <p className={`text-[10px] ${couponMessage.ok ? 'text-emerald-400' : 'text-rose-400'}`}>
                    {couponMessage.mensaje}
                  </p>
                )}
              </form>

              {/* Desglose de Precios */}
              <div className="space-y-1.5 text-xs text-stone-300">
                <div className="flex justify-between">
                  <span>Subtotal productos:</span>
                  <span className="font-semibold text-white">${subtotal.toLocaleString('es-CO')}</span>
                </div>
                {coupon && (
                  <div className="flex justify-between text-emerald-400">
                    <span>Descuento cupón:</span>
                    <span>-${descuentoValor.toLocaleString('es-CO')}</span>
                  </div>
                )}
                <div className="flex justify-between">
                  <span>Costo de envío (Popayán):</span>
                  <span>{costoEnvio === 0 ? <span className="text-emerald-400 font-bold">¡GRATIS!</span> : `$${costoEnvio.toLocaleString('es-CO')}`}</span>
                </div>
                <div className="flex justify-between text-base font-bold text-white pt-2 border-t border-stone-800">
                  <span className="font-['Cinzel']">Total a Pagar:</span>
                  <span className="text-amber-400 font-['Cinzel'] text-lg font-black">
                    ${total.toLocaleString('es-CO')}
                  </span>
                </div>
              </div>

              {/* Botón Ir a Checkout */}
              <Button
                size="lg"
                variant="default"
                className="w-full"
                onClick={() => {
                  closeCart();
                  onProceedToCheckout();
                }}
              >
                Continuar al Pago & Checkout 💳
              </Button>
            </div>
          )}

        </div>
      </div>
    </div>
  );
}
