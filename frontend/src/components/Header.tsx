import React from 'react';
import { Link } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { useAuth } from '../auth/AuthProvider';
import { usePaymentContext } from '../contexts/PaymentContext';
import ProductGenieLogo from './ProductGenieLogo';
import HeaderLanguageSelector from './HeaderLanguageSelector';
import { CreditBalance } from './CreditBalance';
import { Button } from './UI';

interface HeaderProps {
  className?: string;
}

export function Header({ className = "" }: HeaderProps) {
  const { t, i18n } = useTranslation();
  const { user } = useAuth();
  const { payment } = usePaymentContext();

  const handleLanguageChange = (languageCode: string) => {
    i18n.changeLanguage(languageCode);
  };

  const handleUpgrade = () => {
    window.location.href = '/pricing';
  };

  return (
    <header className={`sticky top-4 z-50 mx-4 md:mx-8 ${className}`}>
      <div className="bg-glass-bg backdrop-blur-lg border border-glass-border rounded-2xl shadow-2xl shadow-black/20">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between">
            {/* Logo */}
            <Link to="/" className="flex items-center group">
              <div className="group-hover:scale-110 transition-transform duration-300">
                <ProductGenieLogo size="xl" />
              </div>
            </Link>

            {/* Navigation and User Actions */}
            <div className="flex items-center space-x-6">
              {/* Navigation Links */}
              <nav className="hidden md:flex items-center space-x-6 text-sm font-medium text-gray-300">
                <Link 
                  to="/" 
                  className="hover:text-primary transition-colors duration-200"
                >
                  {t('navigation.dashboard')}
                </Link>
                <Link 
                  to="/pricing" 
                  className="hover:text-primary transition-colors duration-200"
                >
                  {t('navigation.pricing')}
                </Link>
                <a 
                  href="https://github.com" 
                  target="_blank" 
                  rel="noreferrer" 
                  className="hover:text-primary transition-colors duration-200"
                >
                  {t('navigation.documentation')}
                </a>
              </nav>

              {/* Credit Balance - Only show for authenticated users */}
              {user && (
                <div className="hidden lg:block">
                  <CreditBalance 
                    compact={true}
                    showPurchaseButton={false}
                    className="min-w-[200px]"
                  />
                </div>
              )}

              {/* Language Selector */}
              <div className="flex items-center space-x-2">
                <span className="text-sm text-gray-400">Language:</span>
                <HeaderLanguageSelector
                  value={i18n.language}
                  onChange={handleLanguageChange}
                />
              </div>

              {/* User Actions */}
              <div className="flex items-center space-x-3">
                {user ? (
                  <>
                    {/* Mobile Credit Display */}
                    <div className="lg:hidden">
                      <CreditBalance 
                        compact={true}
                        showPurchaseButton={false}
                        className="min-w-[120px]"
                      />
                    </div>
                    
                    {/* Profile Link */}
                    <Link 
                      to="/profile" 
                      className="text-sm text-gray-300 hover:text-primary transition-colors duration-200"
                    >
                      {t('navigation.profile')}
                    </Link>

                    {/* Upgrade Button - Show when credits are low */}
                    {payment.shouldShowUpgradePrompt() && (
                      <Button
                        onClick={handleUpgrade}
                        variant="primary"
                        size="sm"
                        className="hidden sm:inline-flex"
                      >
                        {t('buttons.upgrade')}
                      </Button>
                    )}
                  </>
                ) : (
                  <Link 
                    to="/login" 
                    className="text-sm text-gray-300 hover:text-primary transition-colors duration-200"
                  >
                    {t('navigation.login')}
                  </Link>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}

export default Header;



