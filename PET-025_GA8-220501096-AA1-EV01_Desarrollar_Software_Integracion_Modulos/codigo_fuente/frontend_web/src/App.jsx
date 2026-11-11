import React, { useState } from 'react';
import { AuthProvider } from './context/AuthContext';
import { CartProvider } from './context/CartContext';
import { Navbar } from './components/Navbar';
import { HeroBanner } from './components/HeroBanner';
import { CartaMenu } from './components/CartaMenu';
import { TrackingView } from './components/TrackingView';
import { ClientProfile } from './components/ClientProfile';
import { AdminDashboard } from './components/AdminDashboard';
import { CartDrawer } from './components/CartDrawer';
import { CheckoutModal } from './components/CheckoutModal';
import { AuthModal } from './components/AuthModal';
import { Footer } from './components/Footer';

function PizzeriaApp() {
  const [activeTab, setActiveTab] = useState('inicio');
  const [isAuthModalOpen, setIsAuthModalOpen] = useState(false);
  const [isCheckoutOpen, setIsCheckoutOpen] = useState(false);
  const [trackedOrderNum, setTrackedOrderNum] = useState('PED-2026-002');

  const handleOrderSuccess = (numPedido) => {
    setTrackedOrderNum(numPedido);
    setActiveTab('estados');
  };

  return (
    <div className="min-h-screen bg-stone-950 text-stone-100 flex flex-col justify-between">
      <div>
        <Navbar
          activeTab={activeTab}
          setActiveTab={setActiveTab}
          onOpenAuthModal={() => setIsAuthModalOpen(true)}
        />

        <main>
          {activeTab === 'inicio' && (
            <>
              <HeroBanner
                onGoToCarta={() => setActiveTab('carta')}
                onOpenTracking={() => setActiveTab('estados')}
              />
              <CartaMenu />
            </>
          )}

          {activeTab === 'carta' && <CartaMenu />}

          {activeTab === 'estados' && (
            <TrackingView initialOrderNumber={trackedOrderNum} />
          )}

          {activeTab === 'clientes' && (
            <ClientProfile
              onTrackOrder={(num) => {
                setTrackedOrderNum(num);
                setActiveTab('estados');
              }}
              onOpenAuthModal={() => setIsAuthModalOpen(true)}
            />
          )}

          {activeTab === 'admin' && <AdminDashboard />}
        </main>
      </div>

      <Footer />

      {/* COMPONENTES GLOBALES FLOTANTES */}
      <CartDrawer onProceedToCheckout={() => setIsCheckoutOpen(true)} />
      
      <CheckoutModal
        isOpen={isCheckoutOpen}
        onClose={() => setIsCheckoutOpen(false)}
        onOrderSuccess={handleOrderSuccess}
      />

      <AuthModal
        isOpen={isAuthModalOpen}
        onClose={() => setIsAuthModalOpen(false)}
      />
    </div>
  );
}

export default function App() {
  return (
    <AuthProvider>
      <CartProvider>
        <PizzeriaApp />
      </CartProvider>
    </AuthProvider>
  );
}
