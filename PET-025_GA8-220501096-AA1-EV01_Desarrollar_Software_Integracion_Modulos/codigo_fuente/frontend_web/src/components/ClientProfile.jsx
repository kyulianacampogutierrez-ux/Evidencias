import React, { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { api } from '../services/api';
import { Card, Badge } from './ui/Badge';
import { Button } from './ui/Button';

export function ClientProfile({ onTrackOrder, onOpenAuthModal }) {
  const { user, isAuthenticated, logout } = useAuth();
  const [pedidos, setPedidos] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (isAuthenticated) {
      setLoading(true);
      api.getMisPedidos()
        .then(res => {
          if (res.success) setPedidos(res.pedidos || []);
        })
        .finally(() => setLoading(false));
    }
  }, [isAuthenticated]);

  if (!isAuthenticated) {
    return (
      <div className="py-20 max-w-md mx-auto px-4 text-center space-y-4">
        <span className="text-6xl block">🔒</span>
        <h2 className="font-['Cinzel'] text-2xl font-bold text-white">Módulo de Clientes</h2>
        <p className="text-xs text-stone-400">
          Inicia sesión para consultar tus direcciones de entrega, puntos acumulados e historial de pedidos.
        </p>
        <Button variant="default" size="md" onClick={onOpenAuthModal} className="w-full">
          Iniciar Sesión o Registrarme
        </Button>
      </div>
    );
  }

  return (
    <section className="py-12 max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
      
      {/* TARJETA DATOS DEL CLIENTE */}
      <Card className="p-6 bg-gradient-to-r from-stone-900 to-stone-950">
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
          <div className="flex items-center gap-4">
            <div className="w-16 h-16 rounded-2xl bg-gradient-to-br from-red-600 to-amber-600 flex items-center justify-center text-3xl font-bold text-white shadow-xl shadow-red-950/50">
              {user.nombre?.charAt(0).toUpperCase() || 'C'}
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="font-['Cinzel'] text-xl font-bold text-white">{user.nombre}</h2>
                <Badge variant={user.rol === 'ADMIN' ? 'gold' : 'default'}>{user.rol}</Badge>
              </div>
              <p className="text-xs text-stone-400 mt-0.5">@{user.usuario} • {user.email}</p>
              <p className="text-xs text-stone-400 font-mono mt-0.5">{user.telefono || '+57 312 456 7890'}</p>
            </div>
          </div>

          <div className="flex gap-2">
            <Button size="sm" variant="outline" onClick={logout}>
              Cerrar Sesión 🚪
            </Button>
          </div>
        </div>

        {/* Direcciones registradas */}
        <div className="mt-6 pt-5 border-t border-stone-800">
          <h4 className="text-xs font-bold uppercase tracking-wider text-stone-400 mb-2">
            Direcciones de Entrega en Popayán:
          </h4>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {user.direcciones && user.direcciones.length > 0 ? (
              user.direcciones.map((dir, idx) => (
                <div key={idx} className="p-3 rounded-xl bg-stone-950/80 border border-stone-800 text-xs flex justify-between items-center">
                  <div>
                    <span className="font-semibold text-white block">{dir.alias}</span>
                    <span className="text-stone-400">{dir.direccion}</span>
                  </div>
                  {dir.principal && <Badge variant="green">Principal</Badge>}
                </div>
              ))
            ) : (
              <p className="text-xs text-stone-500">No hay direcciones registradas.</p>
            )}
          </div>
        </div>
      </Card>

      {/* HISTORIAL DE PEDIDOS */}
      <div>
        <div className="flex items-center justify-between mb-4">
          <h3 className="font-['Cinzel'] text-xl font-bold text-white">Historial de tus Pedidos</h3>
          <span className="text-xs text-stone-400">Total registrados: {pedidos.length}</span>
        </div>

        {loading ? (
          <div className="text-center py-12 text-stone-400">
            <div className="inline-block animate-spin text-3xl mb-2">🛵</div>
            <p className="text-xs">Cargando pedidos de MongoDB...</p>
          </div>
        ) : pedidos.length === 0 ? (
          <div className="text-center py-14 bg-stone-900/40 rounded-2xl border border-stone-800 p-6">
            <span className="text-4xl block mb-2">📦</span>
            <p className="text-sm font-semibold text-stone-300">Aún no has realizado pedidos</p>
            <p className="text-xs text-stone-500 mt-1">Explora nuestra carta y haz tu primera orden artesanal.</p>
          </div>
        ) : (
          <div className="space-y-4">
            {pedidos.map(ped => (
              <Card key={ped.numeroPedido} className="p-5 flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div className="space-y-1">
                  <div className="flex items-center gap-3">
                    <span className="font-mono text-sm font-bold text-amber-400">{ped.numeroPedido}</span>
                    <Badge variant={ped.estado === 'ENTREGADO' ? 'green' : 'red'}>{ped.estado}</Badge>
                    <span className="text-[11px] text-stone-500">
                      {new Date(ped.fechaCreacion).toLocaleDateString('es-CO')}
                    </span>
                  </div>
                  <p className="text-xs text-stone-300">
                    {ped.items?.map(it => `${it.cantidad}x ${it.nombre} (${it.tamano})`).join(', ')}
                  </p>
                  <p className="text-[11px] text-stone-500">
                    Pago: {ped.medioPago} ({ped.estadoPago}) • Destino: {ped.direccionEntrega}
                  </p>
                </div>

                <div className="flex items-center justify-between md:justify-end gap-4 shrink-0 pt-3 md:pt-0 border-t md:border-0 border-stone-800">
                  <div className="text-right">
                    <span className="text-[10px] text-stone-400 uppercase block">Total</span>
                    <span className="font-['Cinzel'] text-lg font-bold text-white">
                      ${ped.total?.toLocaleString('es-CO')}
                    </span>
                  </div>
                  <Button size="sm" variant="default" onClick={() => onTrackOrder(ped.numeroPedido)}>
                    Ver Tracking 📍
                  </Button>
                </div>
              </Card>
            ))}
          </div>
        )}
      </div>

    </section>
  );
}
