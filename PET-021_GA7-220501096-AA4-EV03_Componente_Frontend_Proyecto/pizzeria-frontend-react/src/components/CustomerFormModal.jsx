/**
 * CustomerFormModal - Modal de Datos del Cliente y Checkout
 * 
 * Organismo que captura y valida en tiempo real:
 * - Nombre completo del cliente (mínimo 3 caracteres)
 * - Celular colombiano (Regex: ^3[0-9]{9}$ - 10 dígitos iniciando en 3)
 * - Dirección de entrega (mínimo 5 caracteres)
 * - Método de pago y observaciones para la cocina
 * 
 * Aprendiz: Karen Yuliana Campo - SENA ADSO Ficha 228118
 */

import React, { useState, useRef, useEffect } from 'react';
import { useCart } from '../context/CartContext.jsx';

export const CustomerFormModal = ({ isOpen, onClose, onSubmitOrder }) => {
  const { totalCOP, items } = useCart();
  const nameInputRef = useRef(null);

  // Estado del formulario
  const [formData, setFormData] = useState({
    nombre: '',
    telefono: '',
    direccion: '',
    metodoPago: 'EFECTIVO',
    notas: ''
  });

  // Estado de errores de validación
  const [errors, setErrors] = useState({});
  const [submitting, setSubmitting] = useState(false);

  // Autofocus en el campo Nombre al abrir el modal
  useEffect(() => {
    if (isOpen && nameInputRef.current) {
      setTimeout(() => nameInputRef.current.focus(), 100);
    }
  }, [isOpen]);

  if (!isOpen) return null;

  // Validación síncrona de campos
  const validate = () => {
    const errs = {};

    // 1. Validación de Nombre
    if (!formData.nombre.trim()) {
      errs.nombre = 'El nombre completo es obligatorio.';
    } else if (formData.nombre.trim().length < 3) {
      errs.nombre = 'El nombre debe tener al menos 3 caracteres.';
    }

    // 2. Validación Regex de Teléfono Colombiano
    const phoneRegex = /^3[0-9]{9}$/;
    if (!formData.telefono.trim()) {
      errs.telefono = 'El número de teléfono es obligatorio.';
    } else if (!phoneRegex.test(formData.telefono.trim())) {
      errs.telefono = 'Ingrese un celular colombiano válido de 10 dígitos (ej: 3101234567).';
    }

    // 3. Validación de Dirección
    if (!formData.direccion.trim()) {
      errs.direccion = 'La dirección de domicilio es obligatoria.';
    } else if (formData.direccion.trim().length < 5) {
      errs.direccion = 'La dirección debe tener al menos 5 caracteres.';
    }

    setErrors(errs);
    return Object.keys(errs).length === 0;
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
    // Limpiar error al escribir
    if (errors[name]) {
      setErrors((prev) => ({ ...prev, [name]: undefined }));
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!validate()) return;

    setSubmitting(true);
    try {
      await onSubmitOrder({
        cliente: {
          nombre: formData.nombre.trim(),
          telefono: formData.telefono.trim(),
          direccion: formData.direccion.trim()
        },
        metodoPago: formData.metodoPago,
        notas: formData.notas.trim(),
        total: totalCOP,
        detalles: items.map((it) => ({
          idPizza: it.idPizza,
          cantidad: it.cantidad,
          precioUnitario: it.precioUnitario,
          subtotal: it.subtotal,
          tamano: it.tamano
        }))
      });
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="modal-overlay" onClick={onClose} role="presentation">
      <div
        className="modal-container"
        onClick={(e) => e.stopPropagation()}
        role="dialog"
        aria-modal="true"
        aria-labelledby="modal-checkout-title"
      >
        <div className="modal-header">
          <div className="modal-title-wrap">
            <span className="modal-icon">🛵</span>
            <h2 id="modal-checkout-title" className="modal-title">
              Finalizar Pedido a Domicilio
            </h2>
          </div>
          <button className="modal-close-btn" onClick={onClose} aria-label="Cerrar ventana">
            ✕
          </button>
        </div>

        <form onSubmit={handleSubmit} className="modal-form" noValidate>
          {/* Campo Nombre */}
          <div className="form-group">
            <label htmlFor="customer-name" className="form-label">
              Nombre Completo *
            </label>
            <input
              ref={nameInputRef}
              type="text"
              id="customer-name"
              name="nombre"
              className={`form-input ${errors.nombre ? 'invalid' : ''}`}
              placeholder="Ej: Karen Yuliana Campo"
              value={formData.nombre}
              onChange={handleChange}
              aria-invalid={!!errors.nombre}
              aria-describedby={errors.nombre ? 'error-name' : undefined}
            />
            {errors.nombre && (
              <span id="error-name" className="form-error" role="alert">
                ⚠️ {errors.nombre}
              </span>
            )}
          </div>

          {/* Campo Teléfono */}
          <div className="form-group">
            <label htmlFor="customer-phone" className="form-label">
              Celular de Contacto (Colombia) *
            </label>
            <input
              type="tel"
              id="customer-phone"
              name="telefono"
              maxLength="10"
              className={`form-input ${errors.telefono ? 'invalid' : ''}`}
              placeholder="Ej: 3123456789 (10 dígitos)"
              value={formData.telefono}
              onChange={handleChange}
              aria-invalid={!!errors.telefono}
              aria-describedby={errors.telefono ? 'error-phone' : undefined}
            />
            {errors.telefono && (
              <span id="error-phone" className="form-error" role="alert">
                ⚠️ {errors.telefono}
              </span>
            )}
          </div>

          {/* Campo Dirección */}
          <div className="form-group">
            <label htmlFor="customer-address" className="form-label">
              Dirección de Entrega *
            </label>
            <input
              type="text"
              id="customer-address"
              name="direccion"
              className={`form-input ${errors.direccion ? 'invalid' : ''}`}
              placeholder="Ej: Calle 5 # 12-45, Barrio Centro, Popayán"
              value={formData.direccion}
              onChange={handleChange}
              aria-invalid={!!errors.direccion}
              aria-describedby={errors.direccion ? 'error-address' : undefined}
            />
            {errors.direccion && (
              <span id="error-address" className="form-error" role="alert">
                ⚠️ {errors.direccion}
              </span>
            )}
          </div>

          {/* Método de Pago */}
          <div className="form-group">
            <label htmlFor="customer-payment" className="form-label">
              Método de Pago
            </label>
            <select
              id="customer-payment"
              name="metodoPago"
              className="form-select"
              value={formData.metodoPago}
              onChange={handleChange}
            >
              <option value="EFECTIVO">Efectivo contra entrega</option>
              <option value="NEQUI">Transferencia Nequi / Daviplata</option>
              <option value="DATAFONO">Datáfono contra entrega (Tarjeta)</option>
            </select>
          </div>

          {/* Notas Adicionales */}
          <div className="form-group">
            <label htmlFor="customer-notes" className="form-label">
              Instrucciones para Cocina / Repartidor
            </label>
            <textarea
              id="customer-notes"
              name="notas"
              rows="2"
              className="form-textarea"
              placeholder="Ej: Timbre 201, salsa de ajo extra por favor."
              value={formData.notas}
              onChange={handleChange}
            ></textarea>
          </div>

          {/* Resumen Final */}
          <div className="modal-summary-box">
            <span>Total a pagar al recibir:</span>
            <strong className="summary-amount">${totalCOP.toLocaleString('es-CO')}</strong>
          </div>

          {/* Botones de Acción */}
          <div className="modal-actions">
            <button type="button" className="btn-cancel" onClick={onClose} disabled={submitting}>
              Cancelar
            </button>
            <button type="submit" className="btn-submit-order" disabled={submitting}>
              {submitting ? 'Confirmando pedido...' : 'Confirmar Pedido Ahora 🍕'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};
