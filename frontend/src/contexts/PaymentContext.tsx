import React, { createContext, useContext, useEffect, ReactNode } from 'react';
import { usePayment } from '../hooks/usePayment';
import { websocketService } from '../services/websocketService';
import { useAuth } from '../auth/AuthProvider';

interface PaymentContextType {
  // All payment functionality from usePayment hook
  payment: ReturnType<typeof usePayment>;
  // WebSocket service
  ws: typeof websocketService;
}

const PaymentContext = createContext<PaymentContextType | null>(null);

interface PaymentProviderProps {
  children: ReactNode;
}

/**
 * Payment Context Provider
 * Provides payment functionality and WebSocket connection to child components
 */
export const PaymentProvider: React.FC<PaymentProviderProps> = ({ children }) => {
  const { user } = useAuth();
  const payment = usePayment();

  // Initialize WebSocket connection when user is authenticated
  useEffect(() => {
    if (user) {
      websocketService.connect();
    } else {
      websocketService.disconnect();
    }

    // Cleanup on unmount
    return () => {
      websocketService.disconnect();
    };
  }, [user]);

  // Handle online/offline status changes
  useEffect(() => {
    const handleOnline = () => {
      payment.refreshPaymentData();
      if (user) {
        websocketService.connect();
      }
    };

    const handleOffline = () => {
      websocketService.disconnect();
    };

    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);

    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, [user, payment.refreshPaymentData]);

  const contextValue: PaymentContextType = {
    payment,
    ws: websocketService
  };

  return (
    <PaymentContext.Provider value={contextValue}>
      {children}
    </PaymentContext.Provider>
  );
};

/**
 * Hook to use payment context
 * Must be used within PaymentProvider
 */
export const usePaymentContext = (): PaymentContextType => {
  const context = useContext(PaymentContext);
  
  if (!context) {
    throw new Error('usePaymentContext must be used within a PaymentProvider');
  }
  
  return context;
};

/**
 * Higher-order component to wrap components with payment context
 */
export const withPaymentContext = <P extends object>(
  Component: React.ComponentType<P>
): React.ComponentType<P> => {
  const WrappedComponent: React.FC<P> = (props) => (
    <PaymentProvider>
      <Component {...props} />
    </PaymentProvider>
  );
  
  WrappedComponent.displayName = `withPaymentContext(${Component.displayName || Component.name})`;
  
  return WrappedComponent;
};

// Export types
export type { PaymentContextType };



