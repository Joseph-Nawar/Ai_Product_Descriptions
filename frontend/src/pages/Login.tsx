// frontend/src/pages/Login.tsx
import React from "react";
import { useAuth } from "../auth/AuthProvider";
import LoginPage from "../components/LoginPage";

export default function Login() {
  const { loading, user } = useAuth();
  
  if (!loading && user) {
    // already logged in
    window.location.replace("/");
    return null;
  }

  return <LoginPage />;
}
