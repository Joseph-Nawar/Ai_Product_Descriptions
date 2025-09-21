import React from 'react';
import { Link } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { useAuth } from '../auth/AuthProvider';
import { usePaymentContext } from '../contexts/PaymentContext';
import ProductGenieLogo from './ProductGenieLogo';
import HeaderLanguageSelector from './HeaderLanguageSelector';
import { CreditBalance } from './CreditBalance';
import { Button } from './UI';
import { HeaderProfileDropdown } from './HeaderProfileDropdown';

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
        <div className="mx-auto max-w-7xl px-0">
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
                <a 
                  href="https://github.com" 
                  target="_blank" 
                  rel="noreferrer" 
                  className="hover:text-primary transition-colors duration-200"
                >
                  {t('navigation.documentation')}
                </a>
              </nav>

              {/* Credit Balance and Upgrade Button - Only show for authenticated users */}
              {user && (
                <div className="hidden lg:flex items-center space-x-3">
                  <CreditBalance 
                    compact={true}
                    showPurchaseButton={false}
                    className="min-w-[200px]"
                  />
                  <Link to="/pricing">
                    <Button
                      variant="secondary"
                      size="sm"
                      className="bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-600 hover:to-pink-600 text-white border-0 shadow-lg hover:shadow-xl transform hover:-translate-y-0.5 transition-all duration-300"
                    >
                      Upgrade
                    </Button>
                  </Link>
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
                {/* Upgrade Button for non-authenticated users */}
                {!user && (
                  <Link to="/pricing">
                    <Button
                      variant="secondary"
                      size="sm"
                      className="bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-600 hover:to-pink-600 text-white border-0 shadow-lg hover:shadow-xl transform hover:-translate-y-0.5 transition-all duration-300"
                    >
                      Upgrade
                    </Button>
                  </Link>
                )}

                {/* Mobile Credit Display and Upgrade Button */}
                {user && (
                  <div className="lg:hidden flex items-center space-x-2">
                    <CreditBalance 
                      compact={true}
                      showPurchaseButton={false}
                      className="min-w-[120px]"
                    />
                    <Link to="/pricing">
                      <Button
                        variant="secondary"
                        size="sm"
                        className="bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-600 hover:to-pink-600 text-white border-0 shadow-lg hover:shadow-xl transform hover:-translate-y-0.5 transition-all duration-300"
                      >
                        Upgrade
                      </Button>
                    </Link>
                  </div>
                )}

                {/* Profile Dropdown */}
                <HeaderProfileDropdown />

                {/* Upgrade Button - Show when credits are low */}
                {user && payment.shouldShowUpgradePrompt() && (
                  <Button
                    onClick={handleUpgrade}
                    variant="primary"
                    size="sm"
                    className="hidden sm:inline-flex"
                  >
                    {t('buttons.upgrade')}
                  </Button>
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



