import React, { useState, useEffect } from 'react';
import { api } from '../services/api';
import { Card, Badge } from './ui/Badge';
import { Button } from './ui/Button';

export function AdminDashboard() {
  const [stats, setStats] = useState(null);
  const [pedidos, setPedidos] = useState([]);
  const [pizzas, setPizzas] = useState([]);
  const [activeTab, setActiveTab] = useState('pedidos'); // 'pedidos' | 'carta'
  const [filterEstado, setFilterEstado] = useState('');
  const [loading, setLoading] = useState(true);

  // Formulario nueva pizza
  const [nuevaPizza, setNuevaPizza] = useState({
    codigo: '',
    nombre: '',
    categoria: 'ESPECIALES',
    descripcion: '',
    personal: 28000,
    mediana: 40000,
    familiar: 55000,
    ingredientes: '',
  });

  const loadData = () => {
    setLoading(true);
    Promise.all([
      api.getAdminStats(),
      api.getAdminPedidos(filterEstado),
      api.getPizzas()
    ]).then(([statsRes, pedRes, pizRes]) => {
      if (statsRes.success) setStats(statsRes);
      if (pedRes.success) setPedidos(pedRes.pedidos || []);
      if (pizRes.success) setPizzas(pizRes.pizzas || []);
    }).finally(() => setLoading(false));
  };

  useEffect(() => {
    loadData();
  }, [filterEstado]);

  const handleCambiarEstado = async (numeroPedido, nuevoEstado) => {
    const res = await api.actualizarEstadoPedido(
      numeroPedido,
      nuevoEstado,
      `Actualizado desde el panel de administración por Karen Yuliana Campo.`
    );
    if (res.success) {
      loadData();
    } else {
      alert(res.mensaje || 'Error al actualizar el estado');
    }
  };

  const handleCrearPizza = async (e) => {
    e.preventDefault();
    const payload = {
      codigo: nuevaPizza.codigo.toUpperCase(),
      nombre: nuevaPizza.nombre,
      categoria: nuevaPizza.categoria,
      descripcion: nuevaPizza.descripcion,
      imagenUrl: '/images/pizza-custom.jpg',
      precios: {
        personal: parseInt(nuevaPizza.personal),
        mediana: parseInt(nuevaPizza.mediana),
        familiar: parseInt(nuevaPizza.familiar),
      },
      ingredientes: nuevaPizza.ingredientes.split(',').map(s => s.trim()).filter(Boolean),
      adicionesDisponibles: [
        { nombre: 'Queso Extra', precio: 4000 },
        { nombre: 'Borde de Queso', precio: 5000 },
      ],
      destacada: true,
      disponible: true,
    };

    const res = await api.crearPizza(payload);
    if (res.success) {
      alert('¡Nueva pizza agregada a la base de datos MongoDB!');
      setNuevaPizza({
        codigo: '',
        nombre: '',
        categoria: 'ESPECIALES',
        descripcion: '',
        personal: 28000,
        mediana: 40000,
        familiar: 55000,
        ingredientes: '',
      });
      loadData();
    } else {
      alert(res.mensaje || 'Error al crear pizza');
    }
  };

  const handleEliminarPizza = async (codigo) => {
    if (!confirm(`¿Eliminar la pizza ${codigo} de la carta?`)) return;
    const res = await api.eliminarPizza(codigo);
    if (res.success) {
      loadData();
    } else {
      alert(res.mensaje || 'Error al eliminar');
    }
  };

  return (
    <section className="py-12 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
      
      {/* ENCABEZADO PANEL ADMIN */}
      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 pb-6 border-b border-stone-800">
        <div>
          <div className="flex items-center gap-2">
            <span className="text-2xl">👑</span>
            <h2 className="font-['Cinzel'] text-2xl font-bold text-white">Panel de Control Administrador</h2>
            <Badge variant="gold">ADMIN SENA</Badge>
          </div>
          <p className="text-xs text-stone-400 mt-1">
            Gestión operativa en vivo: MongoDB + Go Fiber v2 • Sucursal Popayán Centro
          </p>
        </div>

        <div className="flex gap-2">
          <Button
            size="sm"
            variant={activeTab === 'pedidos' ? 'default' : 'outline'}
            onClick={() => setActiveTab('pedidos')}
          >
            Órdenes & Despachos ({pedidos.length})
          </Button>
          <Button
            size="sm"
            variant={activeTab === 'carta' ? 'gold' : 'outline'}
            onClick={() => setActiveTab('carta')}
          >
            Gestión de Carta ({pizzas.length})
          </Button>
          <Button size="sm" variant="ghost" onClick={loadData}>
            🔄 Refrescar
          </Button>
        </div>
      </div>

      {/* MÉTRICAS COMERCIALES Y DE SERVICIO */}
      {stats && (
        <div className="grid grid-cols-2 lg:grid-cols-5 gap-4">
          <Card className="p-4 bg-stone-900 border-stone-800">
            <span className="text-[10px] uppercase font-bold text-stone-400 block">Ventas Aprobadas</span>
            <p className="font-['Cinzel'] text-xl font-black text-emerald-400 mt-1">
              ${stats.metricas?.totalVentasPesos?.toLocaleString('es-CO')}
            </p>
          </Card>
          <Card className="p-4 bg-stone-900 border-stone-800">
            <span className="text-[10px] uppercase font-bold text-stone-400 block">Total Órdenes</span>
            <p className="font-['Cinzel'] text-xl font-black text-white mt-1">
              {stats.metricas?.totalPedidos}
            </p>
          </Card>
          <Card className="p-4 bg-stone-900 border-stone-800">
            <span className="text-[10px] uppercase font-bold text-amber-400 block">Órdenes Activas</span>
            <p className="font-['Cinzel'] text-xl font-black text-amber-400 mt-1">
              {stats.metricas?.pedidosActivos}
            </p>
          </Card>
          <Card className="p-4 bg-stone-900 border-stone-800">
            <span className="text-[10px] uppercase font-bold text-stone-400 block">Entregadas</span>
            <p className="font-['Cinzel'] text-xl font-black text-stone-300 mt-1">
              {stats.metricas?.pedidosEntregados}
            </p>
          </Card>
          <Card className="p-4 bg-stone-900 border-stone-800 col-span-2 lg:col-span-1">
            <span className="text-[10px] uppercase font-bold text-stone-400 block">Clientes Registrados</span>
            <p className="font-['Cinzel'] text-xl font-black text-sky-400 mt-1">
              {stats.metricas?.clientesRegistrados}
            </p>
          </Card>
        </div>
      )}

      {/* PESTAÑA 1: GESTIÓN DE PEDIDOS Y CONTROL DE ESTADOS */}
      {activeTab === 'pedidos' && (
        <div className="space-y-6">
          <div className="flex flex-wrap items-center justify-between gap-3">
            <h3 className="font-['Cinzel'] text-lg font-bold text-white">Despacho y Cambio de Estados</h3>
            
            {/* Filtro por estado */}
            <div className="flex gap-1.5 overflow-x-auto text-xs">
              {['', 'RECIBIDO', 'EN_PREPARACION', 'EN_HORNO', 'EN_CAMINO', 'ENTREGADO'].map(st => (
                <button
                  key={st}
                  onClick={() => setFilterEstado(st)}
                  className={`px-3 py-1.5 rounded-lg font-medium transition-all ${
                    filterEstado === st ? 'bg-red-600 text-white' : 'bg-stone-900 text-stone-400 hover:text-white border border-stone-800'
                  }`}
                >
                  {st || 'Todos'}
                </button>
              ))}
            </div>
          </div>

          <div className="space-y-4">
            {pedidos.map(p => (
              <Card key={p.numeroPedido} className="p-5 space-y-4 bg-stone-900/90 border-stone-800">
                <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 pb-3 border-b border-stone-800">
                  <div className="flex items-center gap-3">
                    <span className="font-mono text-base font-bold text-amber-400">{p.numeroPedido}</span>
                    <Badge variant={p.estado === 'ENTREGADO' ? 'green' : 'red'}>{p.estado}</Badge>
                    <span className="text-xs text-stone-400">Cliente: {p.clienteNombre} ({p.clienteUsuario})</span>
                  </div>
                  <div className="text-right">
                    <span className="text-sm font-bold text-white">${p.total?.toLocaleString('es-CO')}</span>
                    <span className="text-[11px] text-stone-400 block">Pago: {p.medioPago} ({p.estadoPago})</span>
                  </div>
                </div>

                <div className="text-xs text-stone-300">
                  <p><span className="font-semibold text-stone-400">Dirección:</span> {p.direccionEntrega}</p>
                  <p className="mt-1"><span className="font-semibold text-stone-400">Items:</span> {p.items?.map(i => `${i.cantidad}x ${i.nombre} (${i.tamano})`).join(' • ')}</p>
                </div>

                {/* BOTONERA DE CAMBIO RÁPIDO DE ESTADO */}
                <div className="pt-2 border-t border-stone-800/80 flex flex-wrap items-center justify-between gap-2">
                  <span className="text-[11px] uppercase tracking-wider font-bold text-stone-400">
                    Avanzar Estado:
                  </span>
                  <div className="flex flex-wrap gap-1.5">
                    {p.estado !== 'EN_PREPARACION' && (
                      <Button size="sm" variant="secondary" onClick={() => handleCambiarEstado(p.numeroPedido, 'EN_PREPARACION')}>
                        👨‍🍳 Preparación
                      </Button>
                    )}
                    {p.estado !== 'EN_HORNO' && (
                      <Button size="sm" variant="secondary" onClick={() => handleCambiarEstado(p.numeroPedido, 'EN_HORNO')}>
                        🔥 Al Horno
                      </Button>
                    )}
                    {p.estado !== 'EN_CAMINO' && (
                      <Button size="sm" variant="secondary" onClick={() => handleCambiarEstado(p.numeroPedido, 'EN_CAMINO')}>
                        🛵 En Camino
                      </Button>
                    )}
                    {p.estado !== 'ENTREGADO' && (
                      <Button size="sm" variant="gold" onClick={() => handleCambiarEstado(p.numeroPedido, 'ENTREGADO')}>
                        ✓ Entregado
                      </Button>
                    )}
                  </div>
                </div>
              </Card>
            ))}
          </div>
        </div>
      )}

      {/* PESTAÑA 2: GESTIÓN DEL CATÁLOGO DE PIZZAS */}
      {activeTab === 'carta' && (
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
          
          {/* Formulario Crear Pizza */}
          <div className="lg:col-span-5">
            <Card className="p-6 sticky top-28 bg-stone-900 border-stone-800 space-y-4">
              <h3 className="font-['Cinzel'] text-lg font-bold text-white flex items-center gap-2">
                <span>➕</span> Agregar Nueva Pizza a MongoDB
              </h3>
              
              <form onSubmit={handleCrearPizza} className="space-y-3 text-xs">
                <div>
                  <label className="text-stone-400 block mb-1">Código Único (ej: PIZ-007)</label>
                  <input
                    type="text"
                    required
                    value={nuevaPizza.codigo}
                    onChange={(e) => setNuevaPizza({...nuevaPizza, codigo: e.target.value})}
                    placeholder="PIZ-007"
                    className="w-full bg-stone-950 border border-stone-800 rounded-lg px-3 py-2 text-white uppercase focus:border-red-500 font-mono"
                  />
                </div>
                <div>
                  <label className="text-stone-400 block mb-1">Nombre de la Pizza</label>
                  <input
                    type="text"
                    required
                    value={nuevaPizza.nombre}
                    onChange={(e) => setNuevaPizza({...nuevaPizza, nombre: e.target.value})}
                    placeholder="Ej: Pizza Rústica de la Casa"
                    className="w-full bg-stone-950 border border-stone-800 rounded-lg px-3 py-2 text-white focus:border-red-500"
                  />
                </div>
                <div>
                  <label className="text-stone-400 block mb-1">Categoría</label>
                  <select
                    value={nuevaPizza.categoria}
                    onChange={(e) => setNuevaPizza({...nuevaPizza, categoria: e.target.value})}
                    className="w-full bg-stone-950 border border-stone-800 rounded-lg px-3 py-2 text-white focus:border-red-500"
                  >
                    <option value="CLASICAS">Clásicas</option>
                    <option value="ESPECIALES">Especiales</option>
                    <option value="GOURMET">Gourmet</option>
                    <option value="BEBIDAS">Bebidas</option>
                    <option value="POSTRES">Postres</option>
                  </select>
                </div>
                <div className="grid grid-cols-3 gap-2">
                  <div>
                    <label className="text-stone-400 block mb-1">Personal ($)</label>
                    <input
                      type="number"
                      value={nuevaPizza.personal}
                      onChange={(e) => setNuevaPizza({...nuevaPizza, personal: e.target.value})}
                      className="w-full bg-stone-950 border border-stone-800 rounded-lg px-2.5 py-1.5 text-white"
                    />
                  </div>
                  <div>
                    <label className="text-stone-400 block mb-1">Mediana ($)</label>
                    <input
                      type="number"
                      value={nuevaPizza.mediana}
                      onChange={(e) => setNuevaPizza({...nuevaPizza, mediana: e.target.value})}
                      className="w-full bg-stone-950 border border-stone-800 rounded-lg px-2.5 py-1.5 text-white"
                    />
                  </div>
                  <div>
                    <label className="text-stone-400 block mb-1">Familiar ($)</label>
                    <input
                      type="number"
                      value={nuevaPizza.familiar}
                      onChange={(e) => setNuevaPizza({...nuevaPizza, familiar: e.target.value})}
                      className="w-full bg-stone-950 border border-stone-800 rounded-lg px-2.5 py-1.5 text-white"
                    />
                  </div>
                </div>
                <div>
                  <label className="text-stone-400 block mb-1">Ingredientes (separados por coma)</label>
                  <input
                    type="text"
                    value={nuevaPizza.ingredientes}
                    onChange={(e) => setNuevaPizza({...nuevaPizza, ingredientes: e.target.value})}
                    placeholder="Pomodoro, Queso Gouda, Champiñón..."
                    className="w-full bg-stone-950 border border-stone-800 rounded-lg px-3 py-2 text-white"
                  />
                </div>
                <div>
                  <label className="text-stone-400 block mb-1">Descripción</label>
                  <textarea
                    rows={2}
                    value={nuevaPizza.descripcion}
                    onChange={(e) => setNuevaPizza({...nuevaPizza, descripcion: e.target.value})}
                    placeholder="Breve reseña del plato y cocción..."
                    className="w-full bg-stone-950 border border-stone-800 rounded-lg px-3 py-2 text-white"
                  />
                </div>

                <Button type="submit" size="md" variant="default" className="w-full mt-2">
                  Guardar en MongoDB 💾
                </Button>
              </form>
            </Card>
          </div>

          {/* Listado de Pizzas Registradas */}
          <div className="lg:col-span-7 space-y-3">
            <h3 className="font-['Cinzel'] text-lg font-bold text-white mb-4">Catálogo de Productos ({pizzas.length})</h3>
            {pizzas.map(p => (
              <Card key={p.codigo} className="p-4 flex items-center justify-between gap-4 bg-stone-900 border-stone-800">
                <div className="flex items-center gap-3">
                  <span className="text-3xl">🍕</span>
                  <div>
                    <div className="flex items-center gap-2">
                      <span className="font-mono text-xs font-bold text-amber-400">{p.codigo}</span>
                      <h4 className="font-bold text-sm text-white">{p.nombre}</h4>
                      <Badge variant="default">{p.categoria}</Badge>
                    </div>
                    <p className="text-[11px] text-stone-400 mt-0.5">
                      Mediana: ${p.precios?.mediana?.toLocaleString('es-CO')} • Familiar: ${p.precios?.familiar?.toLocaleString('es-CO')}
                    </p>
                  </div>
                </div>

                <Button size="sm" variant="destructive" onClick={() => handleEliminarPizza(p.codigo)}>
                  Eliminar 🗑️
                </Button>
              </Card>
            ))}
          </div>

        </div>
      )}

    </section>
  );
}
