/**
 * SUITE DE PRUEBAS AUTOMATIZADAS - SOLUCIÓN DE SOFTWARE
 * PROYECTO: PIZZERÍA GOURMET BELLA ITALIA POPAYÁN
 * EVIDENCIA: GA9-220501096-AA1-EV01 - Taller sobre codificación de módulos del software
 * 
 * Aprendiz: Karen Yuliana Campo
 * Ficha: 3186681
 * Centro: Centro de Teleinformática y Producción Industrial (CTPI Popayán) - Regional Cauca
 * Framework: Node.js Test Runner (node:test) & Assert Strict
 */

import { test, describe, it, before, after } from 'node:test';
import assert from 'node:assert/strict';

// ==============================================================================
// 1. MÓDULO DE LÓGICA DE NEGOCIO: CALCULADORA DE PEDIDOS Y FACTURACIÓN
// ==============================================================================
export class OrderCalculator {
  static TAX_RATE_IMPOCONSUMO = 0.08; // 8% Impuesto Nacional al Consumo (Restaurantes Colombia)

  static calculateDeliveryCost(zone, subtotal) {
    if (subtotal >= 60000) return 0; // Envío gratis para compras superiores a $60.000 COP

    const rates = {
      'CENTRO': 3000,
      'NORTE': 4500,
      'SUR': 5000,
      'ORIENTE': 4500,
      'OCCIDENTE': 5000,
      'RURAL': 8000
    };

    const upperZone = (zone || 'CENTRO').toUpperCase();
    return rates[upperZone] ?? 4000;
  }

  static applyCoupon(subtotal, couponCode) {
    if (!couponCode) return { discount: 0, applied: false };
    const cleanCoupon = couponCode.trim().toUpperCase();

    if (cleanCoupon === 'BELLAITALIA10') {
      return { discount: Math.round(subtotal * 0.10), applied: true, name: 'Descuento Gourmet 10%' };
    }
    if (cleanCoupon === 'SENAPROGRAMADOR') {
      return { discount: Math.round(subtotal * 0.15), applied: true, name: 'Descuento ADSO SENA 15%' };
    }
    return { discount: 0, applied: false, error: 'Cupón no válido o vencido' };
  }

  static processOrder(items, deliveryZone, couponCode = null) {
    if (!Array.isArray(items) || items.length === 0) {
      throw new Error('El pedido debe contener al menos un producto');
    }

    let subtotal = 0;
    for (const item of items) {
      if (!item.price || item.price <= 0 || !item.quantity || item.quantity <= 0) {
        throw new Error('Precio o cantidad inválida en producto');
      }
      subtotal += item.price * item.quantity;
    }

    const couponResult = this.applyCoupon(subtotal, couponCode);
    const subtotalAfterDiscount = subtotal - couponResult.discount;
    const tax = Math.round(subtotalAfterDiscount * this.TAX_RATE_IMPOCONSUMO);
    const delivery = this.calculateDeliveryCost(deliveryZone, subtotalAfterDiscount);
    const total = subtotalAfterDiscount + tax + delivery;

    return {
      itemsCount: items.reduce((acc, curr) => acc + curr.quantity, 0),
      rawSubtotal: subtotal,
      discount: couponResult.discount,
      couponApplied: couponResult.applied,
      subtotalNet: subtotalAfterDiscount,
      taxImpoconsumo: tax,
      deliveryCost: delivery,
      totalToPay: total
    };
  }
}

// ==============================================================================
// 2. MÓDULO DE SEGURIDAD Y VALIDACIÓN DE AUTENTICACIÓN
// ==============================================================================
export class AuthValidator {
  static validatePassword(password) {
    if (!password || typeof password !== 'string') return false;
    // Mínimo 8 caracteres, al menos 1 mayúscula, 1 minúscula, 1 dígito y 1 símbolo
    const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$/;
    return regex.test(password);
  }

  static validateEmail(email) {
    if (!email || typeof email !== 'string') return false;
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email.trim());
  }

  static checkRoleAccess(userRole, requiredRole) {
    const roleHierarchy = {
      'CLIENTE': 1,
      'REPARTIDOR': 2,
      'COCINERO': 3,
      'ADMIN': 4
    };
    const userLevel = roleHierarchy[userRole] || 0;
    const requiredLevel = roleHierarchy[requiredRole] || 99;
    return userLevel >= requiredLevel;
  }
}

// ==============================================================================
// 3. MÓDULO DE GESTIÓN Y VALIDACIÓN DE CLIENTES
// ==============================================================================
export class CustomerValidator {
  static validateColombianPhone(phone) {
    if (!phone || typeof phone !== 'string') return false;
    // Celular colombiano: 10 dígitos iniciando en 3
    const regex = /^3\d{9}$/;
    return regex.test(phone.trim());
  }

  static sanitizeInput(input) {
    if (typeof input !== 'string') return input;
    return input
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#x27;')
      .replace(/\$/g, '&#x24;');
  }
}

// ==============================================================================
// 4. MÓDULO DE INVENTARIO Y DISPONIBILIDAD DE INGREDIENTES
// ==============================================================================
export class PizzaInventoryManager {
  constructor() {
    this.ingredients = {
      'harina_00': 50000, // gramos
      'mozzarella_bufala': 30000, // gramos
      'pomodoro_san_marzano': 40000, // gramos
      'albahaca_fresca': 5000, // gramos
      'pepperoni_artesanal': 20000 // gramos
    };
  }

  checkAvailability(recipe) {
    for (const [ingredient, qtyNeeded] of Object.entries(recipe)) {
      if (!this.ingredients[ingredient] || this.ingredients[ingredient] < qtyNeeded) {
        return false;
      }
    }
    return true;
  }

  reserveIngredients(recipe) {
    if (!this.checkAvailability(recipe)) {
      throw new Error('Stock insuficiente para la receta seleccionada');
    }
    for (const [ingredient, qtyNeeded] of Object.entries(recipe)) {
      this.ingredients[ingredient] -= qtyNeeded;
    }
    return true;
  }
}

// ==============================================================================
// 5. EJECUCIÓN DE PRUEBAS UNITARIAS E INTEGRACIÓN (NODE.JS TEST RUNNER)
// ==============================================================================

describe('Pizzería Gourmet Bella Italia Popayán - Pruebas de Módulos (GA9-AA1-EV01)', () => {

  // SUITE 1: CÁLCULO DE PEDIDOS
  describe('Módulo 1: Calculadora de Pedidos y Facturación', () => {
    it('CP01: Debe calcular correctamente subtotal, impoconsumo del 8% y envío en Popayán Centro', () => {
      const items = [
        { name: 'Pizza Margherita Gourmet Familiar', price: 42000, quantity: 1 },
        { name: 'Gaseosa Italiana 400ml', price: 6000, quantity: 2 }
      ];
      // Subtotal = 42000 + 12000 = 54000
      // Impoconsumo (8%) = 54000 * 0.08 = 4320
      // Envío Centro = 3000
      // Total = 54000 + 4320 + 3000 = 61320
      const order = OrderCalculator.processOrder(items, 'CENTRO');

      assert.strictEqual(order.rawSubtotal, 54000, 'Subtotal debe ser 54000 COP');
      assert.strictEqual(order.taxImpoconsumo, 4320, 'Impoconsumo del 8% debe ser 4320 COP');
      assert.strictEqual(order.deliveryCost, 3000, 'Costo de envío a Centro debe ser 3000 COP');
      assert.strictEqual(order.totalToPay, 61320, 'Total a pagar debe ser 61320 COP');
    });

    it('CP02: Debe otorgar envío gratuito cuando el subtotal supera $60.000 COP', () => {
      const items = [
        { name: 'Pizza Prosciutto di Parma', price: 48000, quantity: 1 },
        { name: 'Pizza Cuatro Quesos Artesanal', price: 44000, quantity: 1 }
      ];
      // Subtotal = 92000 >= 60000 -> Delivery = 0
      const order = OrderCalculator.processOrder(items, 'NORTE');
      assert.strictEqual(order.deliveryCost, 0, 'El costo de envío debe ser 0 COP para compras > $60.000');
    });

    it('CP03: Debe aplicar correctamente el cupón de descuento BELLAITALIA10 (10%)', () => {
      const items = [{ name: 'Pizza Napolitana Tradicional', price: 40000, quantity: 1 }];
      const order = OrderCalculator.processOrder(items, 'SUR', 'BELLAITALIA10');

      assert.strictEqual(order.discount, 4000, 'El descuento del 10% debe ser 4000 COP');
      assert.strictEqual(order.subtotalNet, 36000, 'Subtotal neto debe ser 36000 COP');
      assert.strictEqual(order.taxImpoconsumo, 2880, 'Impoconsumo 8% de 36000 debe ser 2880 COP');
    });

    it('CP04: Debe rechazar pedidos con lista vacía de productos', () => {
      assert.throws(() => {
        OrderCalculator.processOrder([], 'CENTRO');
      }, /El pedido debe contener al menos un producto/);
    });
  });

  // SUITE 2: AUTENTICACIÓN Y SEGURIDAD
  describe('Módulo 2: Autenticación, Roles y Seguridad', () => {
    it('CP05: Debe validar contraseñas robustas (mayúscula, minúscula, dígito, símbolo, >=8 chars)', () => {
      assert.strictEqual(AuthValidator.validatePassword('BellaItalia2026!'), true);
      assert.strictEqual(AuthValidator.validatePassword('debil'), false);
      assert.strictEqual(AuthValidator.validatePassword('SoloLetrasMayusYMinus'), false);
      assert.strictEqual(AuthValidator.validatePassword('SinSimbolo123'), false);
    });

    it('CP06: Debe validar formato de correo electrónico', () => {
      assert.strictEqual(AuthValidator.validateEmail('karen.campo@pizzeriabellaitalia.co'), true);
      assert.strictEqual(AuthValidator.validateEmail('correo_invalido_sin_arroba.com'), false);
      assert.strictEqual(AuthValidator.validateEmail('@sindominio.com'), false);
    });

    it('CP07: Debe validar jerarquía de control de acceso basada en roles (RBAC)', () => {
      assert.strictEqual(AuthValidator.checkRoleAccess('ADMIN', 'COCINERO'), true, 'ADMIN tiene acceso a funciones de COCINERO');
      assert.strictEqual(AuthValidator.checkRoleAccess('CLIENTE', 'ADMIN'), false, 'CLIENTE NO debe tener acceso a funciones de ADMIN');
      assert.strictEqual(AuthValidator.checkRoleAccess('REPARTIDOR', 'REPARTIDOR'), true, 'REPARTIDOR accede a su propio rol');
    });
  });

  // SUITE 3: VALIDACIÓN DE CLIENTES Y SANEAMIENTO
  describe('Módulo 3: Clientes, Teléfonos y Saneamiento XSS', () => {
    it('CP08: Debe validar número celular colombiano de 10 dígitos iniciando en 3', () => {
      assert.strictEqual(CustomerValidator.validateColombianPhone('3127894561'), true);
      assert.strictEqual(CustomerValidator.validateColombianPhone('2127894561'), false, 'Fijo no es celular');
      assert.strictEqual(CustomerValidator.validateColombianPhone('312789456'), false, 'Menos de 10 dígitos');
      assert.strictEqual(CustomerValidator.validateColombianPhone('312789456100'), false, 'Más de 10 dígitos');
    });

    it('CP09: Debe sanear entradas para evitar inyecciones XSS y NoSQL', () => {
      const malicious = '<script>alert("hack")</script>';
      const sanitized = CustomerValidator.sanitizeInput(malicious);
      assert.strictEqual(sanitized, '&lt;script&gt;alert(&quot;hack&quot;)&lt;/script&gt;');
    });
  });

  // SUITE 4: INVENTARIO DE INGREDIENTES
  describe('Módulo 4: Gestión de Inventario y Disponibilidad', () => {
    it('CP10: Debe reservar ingredientes cuando hay stock disponible y descontar cantidad exacta', () => {
      const inv = new PizzaInventoryManager();
      const recipePizzaMargherita = {
        'harina_00': 300,
        'mozzarella_bufala': 250,
        'pomodoro_san_marzano': 200,
        'albahaca_fresca': 30
      };

      assert.strictEqual(inv.checkAvailability(recipePizzaMargherita), true);
      const reserved = inv.reserveIngredients(recipePizzaMargherita);
      assert.strictEqual(reserved, true);
      assert.strictEqual(inv.ingredients['harina_00'], 49700);
      assert.strictEqual(inv.ingredients['mozzarella_bufala'], 29750);
    });

    it('CP11: Debe lanzar excepción si se solicitan más ingredientes de los disponibles', () => {
      const inv = new PizzaInventoryManager();
      const recipeExcesiva = {
        'mozzarella_bufala': 999999
      };

      assert.throws(() => {
        inv.reserveIngredients(recipeExcesiva);
      }, /Stock insuficiente/);
    });
  });

});
