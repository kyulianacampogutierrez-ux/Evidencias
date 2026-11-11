import React, { useState } from 'react';
import { useCart } from '../context/CartContext';
import { useAuth } from '../context/AuthContext';
import { api } from '../services/api';
import { Button } from './ui/Button';
import { Badge } from './ui/Badge';

export function CheckoutModal({ isOpen, onClose, onOrderSuccess }) {
  const { items, subtotal, coupon, total, clearCart } = useCart();
  const { user, isAuthenticated } = useAuth();

  const [direccion, setDireccion] = useState(user?.direcciones?.[0]?.direccion || 'Calle 4 Norte # 18-24, Barrio Modelo, Popayán');
  const [telefono, setTelefono] = useState(user?.telefono || '+57 312 456 7890');
  const [nombre, setNombre] = useState(user?.nombre || 'Cliente Pizzería');
  const [medioPago, setMedioPago] = useState('TARJETA_CREDITO');
  const [numeroTarjeta, setNumeroTarjeta] = useState('4500 •••• •••• 1234');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [comprobante, setComprobante] = useState(null);
  const [pedidoCreado, setPedidoCreado] = useState(null);

  if (!isOpen) return null;

  const handleConfirmOrder = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);

    try {
      // 1. Crear el pedido en el Backend Go con Fiber y MongoDB
      const payloadPedido = {
        direccionEntrega: direccion,
        items,
        codigoCupon: coupon?.codigo || '',
        medioPago,
      };

      const resPedido = await api.crearPedido(payloadPedido);
      if (!resPedido.success) {
        alert(resPedido.mensaje || 'Error al crear el pedido');
        setIsSubmitting(false);
        return;
      }

      const pedido = resPedido.pedido;
      setPedidoCreado(pedido);

      // 2. Si es pago electrónico (Tarjeta o PSE/Nequi), procesar la pasarela
      if (medioPago !== 'EFECTIVO') {
        const resPago = await api.procesarPago({
          numeroPedido: pedido.numeroPedido,
          medioPago,
          titular: nombre,
          numeroDoc: '1061789234',
          monto: pedido.total,
        });

        if (resPago.success) {
          setComprobante(resPago.comprobante);
        }
      }

      clearCart();
    } catch (err) {
      alert('Error en el proceso de pago: ' + err.message);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm animate-fadeIn">
      <div className="relative w-full max-w-xl bg-stone-900 border border-stone-800 rounded-3xl p-6 shadow-2xl overflow-y-auto max-h-[92vh]">
        
        {/* Cabecera */}
        <div className="flex items-center justify-between pb-4 border-b border-stone-800">
          <div className="flex items-center gap-2">
            <span className="text-2xl">💳</span>
            <h2 className="font-['Cinzel'] text-xl font-bold text-white">Finalizar Compra y Pago</h2>
          </div>
          {!pedidoCreado && (
            <button
              onClick={onClose}
              className="w-8 h-8 rounded-full bg-stone-800 hover:bg-stone-700 text-stone-300 hover:text-white flex items-center justify-center text-xs font-bold"
            >
              ✕
            </button>
          )}
        </div>

        {/* SI EL PEDIDO YA FUE CREADO CON ÉXITO */}
        {pedidoCreado ? (
          <div className="py-6 text-center space-y-4">
            <div className="w-16 h-16 rounded-full bg-emerald-950/80 border border-emerald-600 text-emerald-400 text-3xl flex items-center justify-center mx-auto animate-bounce">
              ✓
            </div>
            <h3 className="font-['Cinzel'] text-2xl font-bold text-white">¡Pedido Confirmado con Éxito!</h3>
            <p className="text-xs text-stone-300 max-w-md mx-auto">
              Tu orden ha sido registrada en el sistema de Pizzería Bella Italia Popayán y cocina ha comenzado su preparación al horno de leña.
            </p>

            <div className="p-4 rounded-2xl bg-stone-950 border border-stone-800 text-left space-y-2 max-w-md mx-auto">
              <div className="flex justify-between text-xs">
                <span className="text-stone-400">Número de Pedido:</span>
                <span className="font-mono font-bold text-amber-400">{pedidoCreado.numeroPedido}</span>
              </div>
              <div className="flex justify-between text-xs">
                <span className="text-stone-400">Total Pagado:</span>
                <span className="font-bold text-white">${pedidoCreado.total.toLocaleString('es-CO')}</span>
              </div>
              <div className="flex justify-between text-xs">
                <span className="text-stone-400">Medio de Pago:</span>
                <Badge variant={medioPago === 'EFECTIVO' ? 'default' : 'green'}>{medioPago}</Badge>
              </div>
              {comprobante && (
                <div className="flex justify-between text-xs pt-1 border-t border-stone-800">
                  <span className="text-stone-400">Referencia Bancaria:</span>
                  <span className="font-mono text-emerald-400 text-[11px]">{comprobante.referencia}</span>
                </div>
              )}
              <div className="flex justify-between text-xs">
                <span className="text-stone-400">Dirección de Entrega:</span>
                <span className="text-stone-200 text-right truncate max-w-[220px]">{pedidoCreado.direccionEntrega}</span>
              </div>
            </div>

            <div className="flex flex-col sm:flex-row gap-3 pt-3">
              <Button
                variant="default"
                size="md"
                className="w-full"
                onClick={() => {
                  onClose();
                  onOrderSuccess(pedidoCreado.numeroPedido);
                }}
              >
                Ver Seguimiento en Tiempo Real 🛵
              </Button>
              <Button
                variant="outline"
                size="md"
                className="w-full"
                onClick={onClose}
              >
                Volver a la Carta
              </Button>
            </div>
          </div>
        ) : (
          /* FORMULARIO DE CHECKOUT */
          <form onSubmit={handleConfirmOrder} className="py-4 space-y-5">
            
            {/* SECCIÓN 1: DATOS DE ENVÍO */}
            <div className="space-y-3">
              <h3 className="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-1.5">
                <span>📍</span> 1. Dirección de Entrega en Popayán
              </h3>
              <div>
                <label className="text-[11px] text-stone-400 block mb-1">Dirección exacta / Barrio</label>
                <input
                  type="text"
                  required
                  value={direccion}
                  onChange={(e) => setDireccion(e.target.value)}
                  className="w-full bg-stone-950 border border-stone-800 rounded-xl px-3.5 py-2.5 text-xs text-white focus:outline-none focus:border-red-500"
                  placeholder="Ej: Carrera 9 # 15-40, Barrio Pandiguando"
                />
              </div>
              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="text-[11px] text-stone-400 block mb-1">Nombre quien recibe</label>
                  <input
                    type="text"
                    required
                    value={nombre}
                    onChange={(e) => setNombre(e.target.value)}
                    className="w-full bg-stone-950 border border-stone-800 rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-red-500"
                  />
                </div>
                <div>
                  <label className="text-[11px] text-stone-400 block mb-1">Teléfono de contacto</label>
                  <input
                    type="text"
                    required
                    value={telefono}
                    onChange={(e) => setTelefono(e.target.value)}
                    className="w-full bg-stone-950 border border-stone-800 rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-red-500"
                  />
                </div>
              </div>
            </div>

            {/* SECCIÓN 2: MEDIOS DE PAGO */}
            <div className="space-y-3">
              <h3 className="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-1.5">
                <span>💰</span> 2. Selecciona el Medio de Pago
              </h3>
              
              <div className="grid grid-cols-3 gap-2">
                {[
                  { id: 'TARJETA_CREDITO', label: 'Tarjeta', icon: '💳', desc: 'Crédito o Débito' },
                  { id: 'PSE_NEQUI', label: 'PSE / Nequi', icon: '📱', desc: 'Daviplata / Transferencia' },
                  { id: 'EFECTIVO', label: 'Efectivo', icon: '💵', desc: 'Contra Entrega' },
                ].map(opc => (
                  <button
                    key={opc.id}
                    type="button"
                    onClick={() => setMedioPago(opc.id)}
                    className={`p-3 rounded-xl border text-center transition-all ${
                      medioPago === opc.id
                        ? 'border-red-500 bg-red-950/40 text-white ring-1 ring-red-500'
                        : 'border-stone-800 bg-stone-950/60 text-stone-400 hover:border-stone-700'
                    }`}
                  >
                    <span className="text-xl block mb-1">{opc.icon}</span>
                    <p className="text-xs font-bold text-white">{opc.label}</p>
                    <p className="text-[10px] text-stone-400">{opc.desc}</p>
                  </button>
                ))}
              </div>

              {/* Campos condicionales según medio de pago */}
              {medioPago === 'TARJETA_CREDITO' && (
                <div className="p-3.5 rounded-xl bg-stone-950 border border-stone-800 space-y-2">
                  <div className="flex justify-between items-center text-xs text-stone-400">
                    <span>Pasarela de Pago Simulada Segura</span>
                    <Badge variant="blue">SSL 256-bit</Badge>
                  </div>
                  <input
                    type="text"
                    value={numeroTarjeta}
                    onChange={(e) => setNumeroTarjeta(e.target.value)}
                    className="w-full bg-stone-900 border border-stone-700 rounded-lg px-3 py-2 text-xs text-stone-200 font-mono"
                    placeholder="Número de tarjeta de crédito"
                  />
                  <div className="grid grid-cols-2 gap-2">
                    <input
                      type="text"
                      defaultValue="12/28"
                      className="w-full bg-stone-900 border border-stone-700 rounded-lg px-3 py-1.5 text-xs text-stone-300 font-mono"
                      placeholder="MM/AA"
                    />
                    <input
                      type="text"
                      defaultValue="890"
                      className="w-full bg-stone-900 border border-stone-700 rounded-lg px-3 py-1.5 text-xs text-stone-300 font-mono"
                      placeholder="CVC"
                    />
                  </div>
                </div>
              )}

              {medioPago === 'PSE_NEQUI' && (
                <div className="p-3.5 rounded-xl bg-stone-950 border border-stone-800 text-xs text-stone-300 space-y-2">
                  <p className="font-semibold text-white">Transferencia Inmediata Bancaria</p>
                  <p className="text-[11px] text-stone-400">
                    Se generará el enlace dinámico hacia tu billetera Nequi, Daviplata o PSE con validación instantánea en el backend Go.
                  </p>
                  <div className="flex items-center gap-2 text-emerald-400 font-mono text-xs">
                    <span>✓ Llave comercio verificada: 312-456-7890</span>
                  </div>
                </div>
              )}

              {medioPago === 'EFECTIVO' && (
                <div className="p-3.5 rounded-xl bg-stone-950 border border-stone-800 text-xs text-stone-300">
                  <p className="font-semibold text-white">Pago Contra Entrega</p>
                  <p className="text-[11px] text-stone-400 mt-0.5">
                    Pagas al repartidor en efectivo al momento de recibir tus pizzas calientes en tu domicilio.
                  </p>
                </div>
              )}
            </div>

            {/* RESUMEN FINAL Y CONFIRMAR */}
            <div className="pt-4 border-t border-stone-800 space-y-3">
              <div className="flex justify-between items-baseline">
                <span className="text-sm font-semibold text-stone-300">Total a Pagar:</span>
                <span className="font-['Cinzel'] text-2xl font-black text-amber-400">
                  ${total.toLocaleString('es-CO')}
                </span>
              </div>

              <Button
                type="submit"
                size="lg"
                variant="gold"
                disabled={isSubmitting}
                className="w-full font-bold"
              >
                {isSubmitting ? 'Procesando Transacción...' : `Confirmar y Pagar $${total.toLocaleString('es-CO')} 🚀`}
              </Button>
            </div>

          </form>
        )}

      </div>
    </div>
  );
}
