/**
 * CartContext - Gestión de Estado Global para el Carrito de Compras
 * 
 * Implementa el patrón Context API de React con mutaciones inmutables,
 * cálculo de derivados con useMemo y persistencia en localStorage.
 * 
 * Aprendiz: Karen Yuliana Campo - SENA ADSO Ficha 228118
 */

import React, { createContext, useContext, useState, useMemo, useEffect } from 'react';

const CartContext = createContext();

// Clave para almacenamiento local de persistencia
const CART_STORAGE_KEY = 'bella_italia_cart_v1';
const FREE_SHIPPING_THRESHOLD = 50000; // $50.000 COP para envío gratis
const SHIPPING_COST = 6000; // $6.000 COP costo estándar de domicilio

export const CartProvider = ({ children }) => {
  // Estado local del carrito inicializado desde localStorage si existe
  const [items, setItems] = useState(() => {
    try {
      const saved = localStorage.getItem(CART_STORAGE_KEY);
      return saved ? JSON.parse(saved) : [];
    } catch {
      return [];
    }
  });

  // Estado del panel lateral
  const [isDrawerOpen, setIsDrawerOpen] = useState(false);

  // Sincronizar en localStorage ante cualquier mutación
  useEffect(() => {
    try {
      localStorage.setItem(CART_STORAGE_KEY, JSON.stringify(items));
    } catch (e) {
      console.warn('Error al guardar carrito en localStorage:', e);
    }
  }, [items]);

  // Función inmutable para agregar pizzas al carrito
  const addToCart = (product) => {
    setItems((prevItems) => {
      // Buscar si el ítem (misma pizza y mismo tamaño) ya existe
      const existingIndex = prevItems.findIndex(
        (it) => it.idPizza === product.idPizza && it.tamano === product.tamano
      );

      if (existingIndex > -1) {
        // Incrementar la cantidad del ítem existente
        const updated = [...prevItems];
        const current = updated[existingIndex];
        const newQty = current.cantidad + product.cantidad;
        updated[existingIndex] = {
          ...current,
          cantidad: newQty,
          subtotal: current.precioUnitario * newQty
        };
        return updated;
      }

      // Adición inmutable de nuevo ítem
      return [...prevItems, { ...product }];
    });
    // Abrir automáticamente el drawer para retroalimentación visual
    setIsDrawerOpen(true);
  };

  // Actualizar la cantidad de un ítem existente
  const updateQuantity = (idPizza, tamano, delta) => {
    setItems((prevItems) => {
      return prevItems
        .map((it) => {
          if (it.idPizza === idPizza && it.tamano === tamano) {
            const newQty = it.cantidad + delta;
            if (newQty <= 0) return null; // Marcar para eliminación
            return {
              ...it,
              cantidad: newQty,
              subtotal: it.precioUnitario * newQty
            };
          }
          return it;
        })
        .filter(Boolean);
    });
  };

  // Remover un producto del carrito
  const removeFromCart = (idPizza, tamano) => {
    setItems((prevItems) =>
      prevItems.filter((it) => !(it.idPizza === idPizza && it.tamano === tamano))
    );
  };

  // Vaciar completamente el carrito tras un checkout exitoso
  const clearCart = () => {
    setItems([]);
  };

  // Cálculos derivados y memorizados con useMemo para alto rendimiento
  const totalItems = useMemo(() => {
    return items.reduce((acc, it) => acc + it.cantidad, 0);
  }, [items]);

  const subtotalCOP = useMemo(() => {
    return items.reduce((acc, it) => acc + it.subtotal, 0);
  }, [items]);

  const freeShippingEligible = useMemo(() => {
    return subtotalCOP >= FREE_SHIPPING_THRESHOLD;
  }, [subtotalCOP]);

  const shippingCOP = useMemo(() => {
    if (subtotalCOP === 0) return 0;
    return freeShippingEligible ? 0 : SHIPPING_COST;
  }, [subtotalCOP, freeShippingEligible]);

  const totalCOP = useMemo(() => {
    return subtotalCOP + shippingCOP;
  }, [subtotalCOP, shippingCOP]);

  const value = {
    items,
    addToCart,
    updateQuantity,
    removeFromCart,
    clearCart,
    totalItems,
    subtotalCOP,
    shippingCOP,
    totalCOP,
    freeShippingEligible,
    freeShippingThreshold: FREE_SHIPPING_THRESHOLD,
    isDrawerOpen,
    setIsDrawerOpen
  };

  return <CartContext.Provider value={value}>{children}</CartContext.Provider>;
};

// Hook personalizado para consumir el contexto de forma segura
export const useCart = () => {
  const context = useContext(CartContext);
  if (!context) {
    throw new Error('useCart debe ser utilizado dentro de un CartProvider');
  }
  return context;
};
