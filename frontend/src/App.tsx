import React, { Suspense } from "react";
import { Routes, Route, Link } from "react-router-dom";
import { useTranslation } from "react-i18next";
import { AuthProvider } from "./auth/AuthProvider";
import RequireAuth from "./auth/RequireAuth";
import ProductGenieLogo from "./components/ProductGenieLogo";
import HeaderLanguageSelector from "./components/HeaderLanguageSelector";
import { HeaderProfileDropdown } from "./components/HeaderProfileDropdown";
import { SUPPORTED_LANGUAGES } from "./constants/languages";

// Lazy load route components for better performance
const Home = React.lazy(() => import("./pages/Home"));
const Results = React.lazy(() => import("./pages/Results"));
const Login = React.lazy(() => import("./pages/Login"));
const Profile = React.lazy(() => import("./pages/Profile"));

// Loading fallback component
const LoadingFallback = () => (
  <div className="flex items-center justify-center min-h-screen">
    <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary"></div>
  </div>
);

export default function App() {
  const { t, i18n } = useTranslation();

  const handleLanguageChange = (languageCode: string) => {
    i18n.changeLanguage(languageCode);
  };

  return (
    <AuthProvider>
      <div className="aurora-background"></div>
      <div className="relative min-h-dvh z-10">
        <header className="sticky top-4 z-50 mx-2 md:mx-4">
            <div className="bg-glass-bg backdrop-blur-lg border border-glass-border rounded-2xl shadow-2xl shadow-black/20">
              <div className="flex items-center justify-between px-3">
                  <Link to="/" className="flex items-center group">
                    <div className="group-hover:scale-110 transition-transform duration-300">
                      <ProductGenieLogo size="xl" />
                    </div>
                  </Link>
                  <div className="flex items-center space-x-2">
                    <nav className="text-sm font-medium text-gray-300">
                      <a href="https://github.com" target="_blank" rel="noreferrer" className="hover:text-primary transition-colors duration-200">
                        {t('navigation.documentation')}
                      </a>
                    </nav>
                    <div className="flex items-center space-x-2">
                      <span className="text-sm text-gray-400">Language:</span>
                      <HeaderLanguageSelector
                        value={i18n.language}
                        onChange={handleLanguageChange}
                      />
                    </div>
                    <div className="flex items-center space-x-2">
                      <HeaderProfileDropdown />
                    </div>
                  </div>
                </div>
              </div>
        </header>
        <main className="relative mt-8">
          <Suspense fallback={<LoadingFallback />}>
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/results" element={<Results />} />
              <Route path="/login" element={<Login />} />
              <Route path="/profile" element={<RequireAuth><Profile /></RequireAuth>} />
            </Routes>
          </Suspense>
        </main>
        <footer className="mt-24 pb-8">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 text-sm text-center text-gray-400">
            &copy; {new Date().getFullYear()} {t('footer.copyright')}
          </div>
        </footer>
      </div>
    </AuthProvider>
  );
}