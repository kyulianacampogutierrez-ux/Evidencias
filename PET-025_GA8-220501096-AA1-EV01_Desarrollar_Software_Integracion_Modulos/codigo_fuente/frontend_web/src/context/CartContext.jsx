import React, { createContext, useContext, useState, useEffect } from 'react';
import { api } from '../services/api';

const CartContext = createContext();

export function CartProvider({ children }) {
  const [items, setItems] = useState(() => {
    const saved = localStorage.getItem('sena_pizza_cart');
    return saved ? JSON.parse(saved) : [];
  });
  const [coupon, setCoupon] = useState(null);
  const [isCartOpen, setIsCartOpen] = useState(false);

  useEffect(() => {
    localStorage.setItem('sena_pizza_cart', JSON.stringify(items));
  }, [items]);

  const addItem = (pizza, tamano = 'mediana', adiciones = [], cantidad = 1) => {
    const precioBase = pizza.precios[tamano] || pizza.precios.mediana;
    const precioAdiciones = adiciones.reduce((acc, ad) => acc + (ad.precio || 0), 0);
    const precioUnitario = precioBase + precioAdiciones;
    const totalItem = precioUnitario * cantidad;

    const newItem = {
      codigo: pizza.codigo,
      nombre: pizza.nombre,
      imagenUrl: pizza.imagenUrl,
      tamano,
      precioUnitario,
      cantidad,
      adiciones: adiciones.map(a => a.nombre || a),
      totalItem,
    };

    setItems(prev => {
      // Si ya existe el mismo item con igual tamaño y adiciones, sumar cantidad
      const existingIdx = prev.findIndex(
        i => i.codigo === newItem.codigo && i.tamano === newItem.tamano && JSON.stringify(i.adiciones) === JSON.stringify(newItem.adiciones)
      );
      if (existingIdx > -1) {
        const updated = [...prev];
        updated[existingIdx].cantidad += cantidad;
        updated[existingIdx].totalItem = updated[existingIdx].cantidad * updated[existingIdx].precioUnitario;
        return updated;
      }
      return [...prev, newItem];
    });

    setIsCartOpen(true);
  };

  const removeItem = (index) => {
    setItems(prev => prev.filter((_, idx) => idx !== index));
  };

  const updateQuantity = (index, delta) => {
    setItems(prev => {
      const updated = [...prev];
      const newCant = updated[index].cantidad + delta;
      if (newCant <= 0) {
        return updated.filter((_, idx) => idx !== index);
      }
      updated[index].cantidad = newCant;
      updated[index].totalItem = updated[index].cantidad * updated[index].precioUnitario;
      return updated;
    });
  };

  const clearCart = () => {
    setItems([]);
    setCoupon(null);
    localStorage.removeItem('sena_pizza_cart');
  };

  const subtotal = items.reduce((acc, item) => acc + item.totalItem, 0);

  const applyCoupon = async (codigo) => {
    try {
      const res = await api.validarCupon(codigo, subtotal);
      if (res.valido) {
        setCoupon({
          codigo: res.codigo,
          porcentaje: res.porcentaje,
          descuentoCalculado: res.descuentoCalculado,
          mensaje: res.mensaje,
        });
        return { ok: true, mensaje: `¡Cupón ${res.codigo} aplicado! (-${res.porcentaje}%)` };
      }
      return { ok: false, mensaje: res.mensaje || 'Cupón inválido' };
    } catch (err) {
      return { ok: false, mensaje: err.message };
    }
  };

  const removeCoupon = () => setCoupon(null);

  const descuentoValor = coupon ? coupon.descuentoCalculado : 0;
  const costoEnvio = subtotal > 70000 || subtotal === 0 ? 0 : 4000;
  const total = Math.max(0, subtotal - descuentoValor + costoEnvio);
  const totalItemsCount = items.reduce((acc, i) => acc + i.cantidad, 0);

  return (
    <CartContext.Provider
      value={{
        items,
        addItem,
        removeItem,
        updateQuantity,
        clearCart,
        isCartOpen,
        openCart: () => setIsCartOpen(true),
        closeCart: () => setIsCartOpen(false),
        subtotal,
        costoEnvio,
        coupon,
        descuentoValor,
        total,
        applyCoupon,
        removeCoupon,
        totalItemsCount,
      }}
    >
      {children}
    </CartContext.Provider>
  );
}

export function useCart() {
  const context = useContext(CartContext);
  if (!context) throw new Error('useCart debe usarse dentro de CartProvider');
  return context;
}
