// frontend/src/auth/AuthProvider.tsx
import React, { createContext, useContext, useEffect, useMemo, useState } from "react";
import { auth, googleProvider, isFirebaseEnabled } from "./firebase";
import { 
  onIdTokenChanged, 
  signInWithPopup, 
  signOut, 
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  User 
} from "firebase/auth";
import { setIdToken } from "./token";
import { usePaymentStore } from "../store/paymentStore";

type AuthCtx = {
  user: User | null;
  loading: boolean;
  signInWithGoogle: () => Promise<void>;
  signInWithEmail: (email: string, password: string) => Promise<void>;
  signUpWithEmail: (email: string, password: string) => Promise<void>;
  signOutUser: () => Promise<void>;
  isFirebaseEnabled: boolean;
};

const Ctx = createContext<AuthCtx | null>(null);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  
  // Payment store integration
  const {
    refreshAll,
    reset: resetPaymentStore,
    connectWebSocket,
    disconnectWebSocket
  } = usePaymentStore();

  useEffect(() => {
    if (!isFirebaseEnabled) {
      setLoading(false);
      return;
    }

    return onIdTokenChanged(auth, async (u: User | null) => {
      setUser(u);
      if (u) {
        try {
          const t = await u.getIdToken();
          setIdToken(t);
          
          // Wait a bit to ensure token is properly set before making API calls
          await new Promise(resolve => setTimeout(resolve, 200));
          
          // Initialize payment data when user signs in
          await refreshAll();
          connectWebSocket();
        } catch (error) {
          console.error('Failed to initialize payment data:', error);
        }
      } else {
        setIdToken(null);
        
        // Reset payment data when user signs out
        resetPaymentStore();
        disconnectWebSocket();
      }
      setLoading(false);
    });
  }, [refreshAll, resetPaymentStore, connectWebSocket, disconnectWebSocket]);

  const signInWithGoogle = async () => {
    if (!isFirebaseEnabled) {
      throw new Error('Firebase authentication is not configured');
    }
    await signInWithPopup(auth, googleProvider);
  };

  const signInWithEmail = async (email: string, password: string) => {
    if (!isFirebaseEnabled) {
      throw new Error('Firebase authentication is not configured');
    }
    await signInWithEmailAndPassword(auth, email, password);
  };

  const signUpWithEmail = async (email: string, password: string) => {
    if (!isFirebaseEnabled) {
      throw new Error('Firebase authentication is not configured');
    }
    await createUserWithEmailAndPassword(auth, email, password);
  };

  const signOutUser = async () => {
    if (!isFirebaseEnabled) {
      setIdToken(null);
      return;
    }
    await signOut(auth);
    setIdToken(null);
    
    // Clean up payment data and WebSocket connection
    resetPaymentStore();
    disconnectWebSocket();
  };

  const value = useMemo(() => ({ 
    user, 
    loading, 
    signInWithGoogle, 
    signInWithEmail,
    signUpWithEmail,
    signOutUser,
    isFirebaseEnabled: Boolean(isFirebaseEnabled)
  }), [user, loading]);
  return <Ctx.Provider value={value}>{children}</Ctx.Provider>;
};

export const useAuth = () => {
  const v = useContext(Ctx);
  if (!v) throw new Error("useAuth must be used within AuthProvider");
  return v;
};
