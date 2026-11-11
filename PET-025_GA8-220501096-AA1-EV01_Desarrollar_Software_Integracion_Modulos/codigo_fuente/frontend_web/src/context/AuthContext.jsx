import React, { createContext, useContext, useState, useEffect } from 'react';
import { api } from '../services/api';

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(() => {
    const saved = localStorage.getItem('sena_pizza_user');
    return saved ? JSON.parse(saved) : null;
  });
  const [token, setToken] = useState(() => localStorage.getItem('sena_pizza_jwt') || null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (token && !user) {
      api.getProfile()
        .then(res => {
          if (res.success && res.usuario) {
            setUser(res.usuario);
            localStorage.setItem('sena_pizza_user', JSON.stringify(res.usuario));
          } else {
            logout();
          }
        })
        .catch(() => logout());
    }
  }, [token]);

  const login = async (usuario, password) => {
    setLoading(true);
    try {
      const res = await api.login(usuario, password);
      if (res.success && res.token) {
        setToken(res.token);
        setUser(res.usuario);
        localStorage.setItem('sena_pizza_jwt', res.token);
        localStorage.setItem('sena_pizza_user', JSON.stringify(res.usuario));
        return { ok: true, mensaje: res.mensaje, user: res.usuario };
      }
      return { ok: false, mensaje: res.mensaje || 'Credenciales inválidas' };
    } catch (err) {
      return { ok: false, mensaje: err.message };
    } finally {
      setLoading(false);
    }
  };

  const register = async (datos) => {
    setLoading(true);
    try {
      const res = await api.register(datos);
      if (res.success && res.token) {
        setToken(res.token);
        setUser(res.usuario);
        localStorage.setItem('sena_pizza_jwt', res.token);
        localStorage.setItem('sena_pizza_user', JSON.stringify(res.usuario));
        return { ok: true, mensaje: res.mensaje, user: res.usuario };
      }
      return { ok: false, mensaje: res.mensaje || 'Error en el registro' };
    } catch (err) {
      return { ok: false, mensaje: err.message };
    } finally {
      setLoading(false);
    }
  };

  const logout = () => {
    setToken(null);
    setUser(null);
    localStorage.removeItem('sena_pizza_jwt');
    localStorage.removeItem('sena_pizza_user');
  };

  const isAuthenticated = !!token;
  const isAdmin = user?.rol === 'ADMIN';

  return (
    <AuthContext.Provider value={{ user, token, isAuthenticated, isAdmin, loading, login, register, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) throw new Error('useAuth debe usarse dentro de AuthProvider');
  return context;
}
