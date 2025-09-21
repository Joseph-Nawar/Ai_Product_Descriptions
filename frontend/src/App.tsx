import React, { Suspense } from "react";
import { Routes, Route, Link } from "react-router-dom";
import { useTranslation } from "react-i18next";
import { AuthProvider } from "./auth/AuthProvider";
import { PaymentProvider } from "./contexts/PaymentContext";
import RequireAuth from "./auth/RequireAuth";
import { Header } from "./components/Header";
import { SUPPORTED_LANGUAGES } from "./constants/languages";
import i18n from "./i18n";

// Lazy load route components for better performance
const Home = React.lazy(() => import("./pages/Home"));
const Results = React.lazy(() => import("./pages/Results"));
const Login = React.lazy(() => import("./pages/Login"));
const Pricing = React.lazy(() => import("./pages/Pricing"));
const Billing = React.lazy(() => import("./pages/Billing"));
const Profile = React.lazy(() => import("./pages/Profile"));

// Loading fallback component
const LoadingFallback = () => (
  <div className="flex items-center justify-center min-h-screen">
    <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary"></div>
  </div>
);

export default function App() {
  const { t } = useTranslation();

  const handleLanguageChange = (language: string) => {
    i18n.changeLanguage(language);
  };

  return (
    <AuthProvider>
      <PaymentProvider>
        <div className="aurora-background"></div>
        <div className="relative min-h-dvh z-10">
          <Header />
          <main className="relative mt-8">
            <Suspense fallback={<LoadingFallback />}>
              <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/results" element={<Results />} />
                <Route path="/login" element={<Login />} />
                <Route path="/profile" element={<RequireAuth><Profile /></RequireAuth>} />
                <Route path="/pricing" element={<RequireAuth><Pricing /></RequireAuth>} />
                <Route path="/billing" element={<RequireAuth><Billing /></RequireAuth>} />
              </Routes>
            </Suspense>
          </main>
          <footer className="mt-24 pb-8">
            <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 text-sm text-center text-gray-400">
              &copy; {new Date().getFullYear()} {t('footer.copyright')}
            </div>
          </footer>
        </div>
      </PaymentProvider>
    </AuthProvider>
  );
}