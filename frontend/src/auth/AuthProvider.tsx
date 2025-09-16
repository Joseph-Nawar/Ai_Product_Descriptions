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

  useEffect(() => {
    if (!isFirebaseEnabled) {
      setLoading(false);
      return;
    }

    return onIdTokenChanged(auth, async (u: User | null) => {
      setUser(u);
      if (u) {
        const t = await u.getIdToken();
        setIdToken(t);
      } else {
        setIdToken(null);
      }
      setLoading(false);
    });
  }, []);

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
