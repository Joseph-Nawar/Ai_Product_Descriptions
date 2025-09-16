// frontend/src/auth/AuthProvider.tsx
import React, { createContext, useContext, useEffect, useMemo, useState } from "react";
import { auth, googleProvider } from "./firebase";
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
};

const Ctx = createContext<AuthCtx | null>(null);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
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
    await signInWithPopup(auth, googleProvider);
  };

  const signInWithEmail = async (email: string, password: string) => {
    await signInWithEmailAndPassword(auth, email, password);
  };

  const signUpWithEmail = async (email: string, password: string) => {
    await createUserWithEmailAndPassword(auth, email, password);
  };

  const signOutUser = async () => {
    await signOut(auth);
    setIdToken(null);
  };

  const value = useMemo(() => ({ 
    user, 
    loading, 
    signInWithGoogle, 
    signInWithEmail,
    signUpWithEmail,
    signOutUser 
  }), [user, loading]);
  return <Ctx.Provider value={value}>{children}</Ctx.Provider>;
};

export const useAuth = () => {
  const v = useContext(Ctx);
  if (!v) throw new Error("useAuth must be used within AuthProvider");
  return v;
};
