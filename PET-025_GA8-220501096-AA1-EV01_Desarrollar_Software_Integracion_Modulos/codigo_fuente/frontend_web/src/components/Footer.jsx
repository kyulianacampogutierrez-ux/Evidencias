import React from 'react';

export function Footer() {
  return (
    <footer className="border-t border-stone-800 bg-stone-950 text-stone-400 py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 md:grid-cols-4 gap-8">
        
        {/* Columna 1: Pizzería */}
        <div className="space-y-3">
          <div className="flex items-center gap-2">
            <span className="text-2xl">🍕</span>
            <span className="font-['Cinzel'] text-lg font-bold text-white">Bella Italia</span>
          </div>
          <p className="text-xs text-stone-400 leading-relaxed">
            Tradición gastronómica italiana con horneado a la leña en Popayán, Cauca. Ingredientes naturales y masa madre.
          </p>
          <p className="text-xs text-amber-400 font-semibold">
            📍 Calle 4 Norte # 18-24, Popayán
          </p>
        </div>

        {/* Columna 2: Stack Tecnológico */}
        <div className="space-y-2">
          <h4 className="text-xs font-bold uppercase tracking-wider text-white">Stack Tecnológico</h4>
          <ul className="text-xs space-y-1.5 text-stone-400">
            <li>🍃 <span className="text-stone-300">Base de Datos:</span> MongoDB 6 (NoSQL)</li>
            <li>🐹 <span className="text-stone-300">Backend:</span> Go (Golang) + Fiber v2 + JWT</li>
            <li>⚛️ <span className="text-stone-300">Frontend:</span> Vite + React 18 + Tailwind</li>
            <li>📱 <span className="text-stone-300">Móvil:</span> React Native Multiplataforma</li>
            <li>🐳 <span className="text-stone-300">Docker:</span> Contenedores Compose Aislados</li>
          </ul>
        </div>

        {/* Columna 3: Horarios y Contacto */}
        <div className="space-y-2">
          <h4 className="text-xs font-bold uppercase tracking-wider text-white">Atención y Domicilios</h4>
          <ul className="text-xs space-y-1 text-stone-400">
            <li>Lunes a Domingo: 12:00 m - 11:00 pm</li>
            <li>Línea Domicilios: +57 (2) 824 5500</li>
            <li>WhatsApp Pedidos: +57 312 456 7890</li>
            <li>Popayán, Departamento del Cauca</li>
          </ul>
        </div>

        {/* Columna 4: SENA ADSO */}
        <div className="space-y-2">
          <h4 className="text-xs font-bold uppercase tracking-wider text-white">Información Formativa</h4>
          <p className="text-xs text-stone-300 font-semibold">Tecnología en Análisis y Desarrollo de Software (ADSO)</p>
          <p className="text-xs text-stone-400">Ficha: <span className="text-amber-400 font-mono font-bold">3186681</span></p>
          <p className="text-xs text-stone-400">Aprendiz: <span className="text-white font-medium">Karen Yuliana Campo</span></p>
          <p className="text-[11px] text-stone-500">Centro de Teleinformática y Producción Industrial (CTPI Popayán) - Regional Cauca</p>
        </div>

      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-8 pt-6 border-t border-stone-800/60 text-center text-xs text-stone-500">
        © 2026 Pizzería Bella Italia. Proyecto Formativo SENA ADSO Ficha 3186681. Todos los derechos reservados.
      </div>
    </footer>
  );
}
