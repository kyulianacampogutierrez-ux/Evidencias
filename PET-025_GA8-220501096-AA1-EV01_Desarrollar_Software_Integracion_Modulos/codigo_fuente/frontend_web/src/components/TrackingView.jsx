import React, { useState, useEffect } from 'react';
import { api } from '../services/api';
import { Card, Badge } from './ui/Badge';
import { Button } from './ui/Button';

export function TrackingView({ initialOrderNumber }) {
  const [numeroPedido, setNumeroPedido] = useState(initialOrderNumber || 'PED-2026-002');
  const [pedido, setPedido] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchPedido = async (num) => {
    if (!num) return;
    setLoading(true);
    setError(null);
    try {
      const res = await api.getPedido(num);
      if (res.success && res.pedido) {
        setPedido(res.pedido);
      } else {
        setError(res.mensaje || 'Pedido no encontrado en MongoDB.');
        setPedido(null);
      }
    } catch (err) {
      setError(err.message);
      setPedido(null);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (numeroPedido) {
      fetchPedido(numeroPedido);
    }
  }, [numeroPedido]);

  const estadosOrden = [
    { key: 'RECIBIDO', label: 'Recibido', icon: '📝', desc: 'Confirmado por el sistema' },
    { key: 'EN_PREPARACION', label: 'En Preparación', icon: '👨‍🍳', desc: 'Masa e ingredientes frescos' },
    { key: 'EN_HORNO', label: 'En Horno', icon: '🔥', desc: 'Horno de leña a 380°C' },
    { key: 'EN_CAMINO', label: 'En Camino', icon: '🛵', desc: 'Repartidor rumbo a tu dirección' },
    { key: 'ENTREGADO', label: 'Entregado', icon: '🍕', desc: '¡Buen provecho!' },
  ];

  const getPasoActual = (estado) => {
    switch (estado) {
      case 'RECIBIDO': return 0;
      case 'EN_PREPARACION': return 1;
      case 'EN_HORNO': return 2;
      case 'EN_CAMINO': return 3;
      case 'ENTREGADO': return 4;
      case 'CANCELADO': return -1;
      default: return 0;
    }
  };

  const pasoActual = pedido ? getPasoActual(pedido.estado) : 0;

  return (
    <section className="py-12 max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      
      {/* Título y Buscador */}
      <div className="text-center max-w-xl mx-auto mb-10 space-y-3">
        <span className="text-xs font-bold uppercase tracking-widest text-amber-500 bg-amber-950/60 px-3 py-1 rounded-full border border-amber-800/40">
          Tracking en Tiempo Real
        </span>
        <h2 className="font-['Cinzel'] text-3xl sm:text-4xl font-black text-white">
          Seguimiento de tu Pedido
        </h2>
        <p className="text-xs text-stone-400">
          Consulta el estado de preparación, horneado y despacho conectado en vivo a nuestra base de datos MongoDB.
        </p>

        {/* Buscador de pedido */}
        <div className="flex gap-2 max-w-md mx-auto pt-2">
          <input
            type="text"
            placeholder="Número de orden (ej: PED-2026-002)"
            value={numeroPedido}
            onChange={(e) => setNumeroPedido(e.target.value.toUpperCase())}
            className="flex-1 bg-stone-900 border border-stone-800 rounded-xl px-4 py-2.5 text-xs text-white uppercase placeholder-stone-500 focus:outline-none focus:border-red-500 font-mono"
          />
          <Button size="sm" variant="default" onClick={() => fetchPedido(numeroPedido)}>
            Consultar 🔍
          </Button>
        </div>
      </div>

      {loading && (
        <div className="text-center py-16 text-stone-400">
          <div className="inline-block animate-spin text-4xl mb-2">🛵</div>
          <p className="text-xs">Sincronizando estado con el backend Go Fiber...</p>
        </div>
      )}

      {error && !loading && (
        <div className="p-6 rounded-2xl bg-rose-950/30 border border-rose-900/60 text-center max-w-md mx-auto space-y-2">
          <span className="text-3xl">⚠️</span>
          <p className="text-sm font-semibold text-rose-300">{error}</p>
          <p className="text-xs text-stone-400">Verifica el código ingresado o realiza un pedido nuevo.</p>
        </div>
      )}

      {pedido && !loading && (
        <div className="space-y-8 animate-fadeIn">
          
          {/* LÍNEA DE TIEMPO / STEPPER DE ESTADOS */}
          <Card className="p-6 bg-gradient-to-b from-stone-900 to-stone-950 border-stone-800">
            <div className="flex flex-col sm:flex-row items-center justify-between pb-6 mb-8 border-b border-stone-800/80 gap-4">
              <div>
                <span className="text-xs text-stone-400">Orden de Compra:</span>
                <h3 className="font-mono text-xl font-bold text-amber-400">{pedido.numeroPedido}</h3>
                <p className="text-xs text-stone-400 mt-0.5">Destino: {pedido.direccionEntrega}</p>
              </div>
              <div className="text-right">
                <span className="text-xs text-stone-400 block">Tiempo estimado:</span>
                <span className="text-lg font-bold text-white font-['Cinzel']">
                  ~{pedido.tiempoEstimadoMinutos || 35} minutos
                </span>
                <div className="mt-1">
                  <Badge variant={pedido.estado === 'ENTREGADO' ? 'green' : 'red'}>
                    Estado actual: {pedido.estado}
                  </Badge>
                </div>
              </div>
            </div>

            {/* Pasos Visuales */}
            <div className="grid grid-cols-5 gap-2 relative">
              {estadosOrden.map((step, idx) => {
                const isCompleted = pasoActual >= idx;
                const isCurrent = pasoActual === idx;

                return (
                  <div key={step.key} className="flex flex-col items-center text-center group">
                    <div
                      className={`w-12 h-12 rounded-2xl flex items-center justify-center text-xl transition-all duration-300 relative z-10 ${
                        isCurrent
                          ? 'bg-red-600 text-white shadow-xl shadow-red-900/60 scale-110 ring-4 ring-red-950 animate-pulse'
                          : isCompleted
                          ? 'bg-emerald-950 text-emerald-400 border border-emerald-600'
                          : 'bg-stone-900 text-stone-500 border border-stone-800'
                      }`}
                    >
                      {step.icon}
                    </div>
                    <span className={`text-[11px] font-bold mt-2.5 ${isCurrent ? 'text-red-400' : isCompleted ? 'text-white' : 'text-stone-500'}`}>
                      {step.label}
                    </span>
                    <span className="hidden sm:block text-[9px] text-stone-500 mt-0.5 max-w-[90px] leading-tight">
                      {step.desc}
                    </span>
                  </div>
                );
              })}
            </div>

            <div className="mt-6 flex justify-end">
              <Button size="sm" variant="outline" onClick={() => fetchPedido(numeroPedido)}>
                Actualizar Estado 🔄
              </Button>
            </div>
          </Card>

          {/* DETALLES DE LA ORDEN Y BITÁCORA */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            
            {/* Items del pedido */}
            <Card className="p-5">
              <h4 className="font-['Cinzel'] font-bold text-sm text-white mb-4 flex items-center gap-2">
                <span>📋</span> Resumen de Productos
              </h4>
              <div className="space-y-3">
                {pedido.items.map((it, idx) => (
                  <div key={idx} className="flex justify-between items-center text-xs pb-2 border-b border-stone-800/60 last:border-0">
                    <div>
                      <p className="font-semibold text-white">{it.cantidad}x {it.nombre}</p>
                      <span className="text-[10px] text-amber-400 capitalize">Tamaño: {it.tamano}</span>
                    </div>
                    <span className="font-mono font-bold text-stone-200">
                      ${it.totalItem?.toLocaleString('es-CO')}
                    </span>
                  </div>
                ))}
                <div className="pt-2 flex justify-between font-bold text-sm text-white border-t border-stone-800">
                  <span>Total Pedido:</span>
                  <span className="text-amber-400 font-['Cinzel'] text-base">${pedido.total?.toLocaleString('es-CO')}</span>
                </div>
              </div>
            </Card>

            {/* Bitácora de seguimiento / Historial de estados */}
            <Card className="p-5">
              <h4 className="font-['Cinzel'] font-bold text-sm text-white mb-4 flex items-center gap-2">
                <span>🕒</span> Bitácora Cronológica de Preparación
              </h4>
              <div className="space-y-3 relative pl-4 border-l-2 border-stone-800">
                {pedido.historialEstados && pedido.historialEstados.map((h, idx) => (
                  <div key={idx} className="relative">
                    <div className="absolute -left-[21px] top-1 w-2.5 h-2.5 rounded-full bg-red-500 ring-4 ring-stone-950" />
                    <p className="text-xs font-bold text-white">{h.estado}</p>
                    <p className="text-[11px] text-stone-400">{h.nota}</p>
                    <span className="text-[9px] text-stone-500 font-mono">
                      {new Date(h.fecha).toLocaleTimeString('es-CO')}
                    </span>
                  </div>
                ))}
              </div>
            </Card>

          </div>

        </div>
      )}

    </section>
  );
}
