/**
 * AuthContext - Gestión de Estado Global para Autenticación y Roles
 * 
 * Permite alternar y consultar el rol activo:
 * - 'CLIENTE': Vista pública para explorar catálogo y realizar pedidos.
 * - 'ADMIN': Vista administrativa y comanda operativa de cocina.
 * 
 * Aprendiz: Karen Yuliana Campo - SENA ADSO Ficha 228118
 */

import React, { createContext, useContext, useState } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  // Rol activo (CLIENTE o ADMIN)
  const [role, setRole] = useState('CLIENTE');

  // Datos simulados de la sesión activa
  const [currentUser, setCurrentUser] = useState({
    nombre: 'Karen Yuliana Campo',
    email: 'karen.campo@sena.edu.co',
    ficha: '228118',
    regional: 'Cauca (Popayán)'
  });

  const toggleRole = () => {
    setRole((prevRole) => (prevRole === 'CLIENTE' ? 'ADMIN' : 'CLIENTE'));
  };

  const value = {
    role,
    setRole,
    toggleRole,
    currentUser,
    isAdmin: role === 'ADMIN'
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth debe ser utilizado dentro de un AuthProvider');
  }
  return context;
};
