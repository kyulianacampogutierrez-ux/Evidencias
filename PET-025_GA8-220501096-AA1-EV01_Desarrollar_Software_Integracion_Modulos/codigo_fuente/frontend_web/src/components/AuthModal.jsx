import React, { useState } from 'react';
import { useAuth } from '../context/AuthContext';
import { Button } from './ui/Button';

export function AuthModal({ isOpen, onClose }) {
  const { login, register, loading } = useAuth();
  const [isLoginTab, setIsLoginTab] = useState(true);
  const [errorMsg, setErrorMsg] = useState(null);

  // Campos de formulario
  const [usuario, setUsuario] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');
  const [nombre, setNombre] = useState('');
  const [telefono, setTelefono] = useState('');
  const [direccion, setDireccion] = useState('');

  if (!isOpen) return null;

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrorMsg(null);

    if (isLoginTab) {
      const res = await login(usuario, password);
      if (res.ok) {
        onClose();
      } else {
        setErrorMsg(res.mensaje);
      }
    } else {
      const res = await register({
        usuario,
        password,
        email,
        nombre,
        telefono,
        direccion,
        rol: 'CLIENTE',
      });
      if (res.ok) {
        onClose();
      } else {
        setErrorMsg(res.mensaje);
      }
    }
  };

  const handleQuickLogin = async (userDemo, passDemo) => {
    setUsuario(userDemo);
    setPassword(passDemo);
    const res = await login(userDemo, passDemo);
    if (res.ok) onClose();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm animate-fadeIn">
      <div className="relative w-full max-w-md bg-stone-900 border border-stone-800 rounded-3xl p-6 shadow-2xl">
        
        {/* Botón cerrar */}
        <button
          onClick={onClose}
          className="absolute top-4 right-4 w-8 h-8 rounded-full bg-stone-800 hover:bg-stone-700 text-stone-300 hover:text-white flex items-center justify-center text-xs font-bold"
        >
          ✕
        </button>

        {/* Encabezado */}
        <div className="text-center mb-6">
          <div className="w-12 h-12 rounded-2xl bg-red-600/20 text-red-500 text-2xl flex items-center justify-center mx-auto mb-2 border border-red-800/40">
            🍕
          </div>
          <h2 className="font-['Cinzel'] text-xl font-bold text-white">
            {isLoginTab ? 'Iniciar Sesión' : 'Crear Cuenta de Cliente'}
          </h2>
          <p className="text-xs text-stone-400 mt-0.5">
            Pizzería Bella Italia • Autenticación JWT con Go y MongoDB
          </p>
        </div>

        {/* PESTAÑAS LOGIN / REGISTRO */}
        <div className="grid grid-cols-2 p-1 bg-stone-950 rounded-xl mb-5 border border-stone-800">
          <button
            type="button"
            onClick={() => { setIsLoginTab(true); setErrorMsg(null); }}
            className={`py-2 text-xs font-bold rounded-lg transition-all ${
              isLoginTab ? 'bg-red-600 text-white shadow' : 'text-stone-400 hover:text-white'
            }`}
          >
            Ingresar
          </button>
          <button
            type="button"
            onClick={() => { setIsLoginTab(false); setErrorMsg(null); }}
            className={`py-2 text-xs font-bold rounded-lg transition-all ${
              !isLoginTab ? 'bg-red-600 text-white shadow' : 'text-stone-400 hover:text-white'
            }`}
          >
            Registrarse
          </button>
        </div>

        {errorMsg && (
          <div className="p-3 mb-4 rounded-xl bg-rose-950/40 border border-rose-800 text-rose-300 text-xs text-center font-medium">
            ⚠️ {errorMsg}
          </div>
        )}

        {/* FORMULARIO */}
        <form onSubmit={handleSubmit} className="space-y-3.5">
          <div>
            <label className="text-[11px] text-stone-400 block mb-1">Nombre de Usuario</label>
            <input
              type="text"
              required
              value={usuario}
              onChange={(e) => setUsuario(e.target.value)}
              placeholder="Ej: karencampo o carlos_cliente"
              className="w-full bg-stone-950 border border-stone-800 rounded-xl px-3.5 py-2 text-xs text-white focus:outline-none focus:border-red-500"
            />
          </div>

          {!isLoginTab && (
            <>
              <div>
                <label className="text-[11px] text-stone-400 block mb-1">Nombre Completo</label>
                <input
                  type="text"
                  required
                  value={nombre}
                  onChange={(e) => setNombre(e.target.value)}
                  placeholder="Tu nombre completo"
                  className="w-full bg-stone-950 border border-stone-800 rounded-xl px-3.5 py-2 text-xs text-white focus:outline-none focus:border-red-500"
                />
              </div>
              <div>
                <label className="text-[11px] text-stone-400 block mb-1">Correo Electrónico</label>
                <input
                  type="email"
                  required
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="correo@ejemplo.com"
                  className="w-full bg-stone-950 border border-stone-800 rounded-xl px-3.5 py-2 text-xs text-white focus:outline-none focus:border-red-500"
                />
              </div>
              <div className="grid grid-cols-2 gap-2">
                <div>
                  <label className="text-[11px] text-stone-400 block mb-1">Teléfono</label>
                  <input
                    type="text"
                    value={telefono}
                    onChange={(e) => setTelefono(e.target.value)}
                    placeholder="+57 312..."
                    className="w-full bg-stone-950 border border-stone-800 rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-red-500"
                  />
                </div>
                <div>
                  <label className="text-[11px] text-stone-400 block mb-1">Dirección Popayán</label>
                  <input
                    type="text"
                    value={direccion}
                    onChange={(e) => setDireccion(e.target.value)}
                    placeholder="Barrio / Calle"
                    className="w-full bg-stone-950 border border-stone-800 rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-red-500"
                  />
                </div>
              </div>
            </>
          )}

          <div>
            <label className="text-[11px] text-stone-400 block mb-1">Contraseña</label>
            <input
              type="password"
              required
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="••••••••"
              className="w-full bg-stone-950 border border-stone-800 rounded-xl px-3.5 py-2 text-xs text-white focus:outline-none focus:border-red-500"
            />
          </div>

          <Button type="submit" size="md" variant="default" disabled={loading} className="w-full mt-2">
            {loading ? 'Validando con JWT...' : isLoginTab ? 'Ingresar a mi Cuenta 🔐' : 'Crear Cuenta y Continuar ✨'}
          </Button>
        </form>

        {/* ACCESOS DEMO RÁPIDOS */}
        <div className="mt-5 pt-4 border-t border-stone-800">
          <p className="text-[10px] uppercase tracking-wider text-stone-500 font-bold text-center mb-2">
            Acceso Rápido de Prueba (Demo SENA)
          </p>
          <div className="grid grid-cols-2 gap-2">
            <button
              type="button"
              onClick={() => handleQuickLogin('karencampo', 'Admin123*')}
              className="p-2 rounded-xl bg-amber-950/30 hover:bg-amber-900/40 border border-amber-800/40 text-[11px] font-semibold text-amber-300 text-center"
            >
              👑 Karen (Admin)
            </button>
            <button
              type="button"
              onClick={() => handleQuickLogin('carlos_cliente', 'Cliente123*')}
              className="p-2 rounded-xl bg-stone-950 hover:bg-stone-800 border border-stone-800 text-[11px] font-semibold text-stone-300 text-center"
            >
              👤 Carlos (Cliente)
            </button>
          </div>
        </div>

      </div>
    </div>
  );
}
