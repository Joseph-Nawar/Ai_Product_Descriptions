import React, { useState, useRef, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import { SUPPORTED_LANGUAGES, getLanguageByCode } from '../constants/languages';

const LANGUAGE_FLAGS = {
  'en': '🇺🇸',
  'es': '🇪🇸',
  'fr': '🇫🇷',
  'de': '🇩🇪',
  'ja': '🇯🇵',
  'zh': '🇨🇳',
};

const LANGUAGE_COLORS = {
  'en': 'from-blue-500 to-red-600',
  'es': 'from-red-500 to-yellow-600',
  'fr': 'from-blue-500 to-red-600',
  'de': 'from-black to-red-600',
  'ja': 'from-red-500 to-white',
  'zh': 'from-red-500 to-yellow-600',
};

interface LanguageSelectorProps {
  value: string;
  onChange: (languageCode: string) => void;
  className?: string;
  showNativeNames?: boolean;
}

export default function LanguageSelector({ 
  value, 
  onChange, 
  className = "",
  showNativeNames = false 
}: LanguageSelectorProps) {
  const { t } = useTranslation();
  const [isOpen, setIsOpen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    }

    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const selectedLanguage = SUPPORTED_LANGUAGES.find(lang => lang.code === value) || SUPPORTED_LANGUAGES[0];

  return (
    <div className={`space-y-2 ${className}`}>
      <label className="text-sm font-medium text-gray-300">
        {t('forms.languageSelector.label')}
      </label>
      <div className="relative w-full z-[99998]" ref={dropdownRef}>
        <button
          type="button"
          onClick={() => setIsOpen(!isOpen)}
          className="w-full relative overflow-hidden rounded-2xl border-2 border-gray-600 bg-gradient-to-r from-gray-800 to-gray-900 px-6 py-4 text-left transition-all duration-300 hover:border-gray-500 hover:shadow-lg hover:shadow-gray-900/50 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 group"
        >
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <div className={`flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-to-r ${LANGUAGE_COLORS[selectedLanguage.code as keyof typeof LANGUAGE_COLORS]} text-white shadow-lg`}>
                <span className="text-lg">{LANGUAGE_FLAGS[selectedLanguage.code as keyof typeof LANGUAGE_FLAGS]}</span>
              </div>
              <div>
                <div className="text-lg font-semibold text-gray-100">
                  {showNativeNames ? selectedLanguage.nativeName : selectedLanguage.name}
                </div>
                <div className="text-sm text-gray-400">
                  {showNativeNames ? selectedLanguage.name : selectedLanguage.nativeName}
                </div>
              </div>
            </div>
            <div className="flex items-center space-x-2">
              <div className="h-2 w-2 rounded-full bg-green-400 animate-pulse"></div>
              <svg 
                className={`w-5 h-5 text-gray-300 transition-transform duration-200 ${isOpen ? 'rotate-180' : ''}`} 
                fill="none" 
                stroke="currentColor" 
                viewBox="0 0 24 24"
              >
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
              </svg>
            </div>
          </div>
          
          {/* Animated background gradient */}
          <div className="absolute inset-0 bg-gradient-to-r from-blue-600 to-purple-600 opacity-0 group-hover:opacity-20 transition-opacity duration-300"></div>
        </button>

        {isOpen && (
          <div className="absolute top-full left-0 right-0 mt-3 z-[99999]">
            <div className="bg-gray-900 border-2 border-gray-600 rounded-2xl shadow-2xl overflow-hidden">
              <div className="p-2">
                {SUPPORTED_LANGUAGES.map((language) => (
                  <button
                    key={language.code}
                    onClick={() => {
                      onChange(language.code);
                      setIsOpen(false);
                    }}
                    className={`w-full flex items-center space-x-4 px-4 py-4 rounded-xl transition-all duration-200 hover:bg-gray-800 hover:scale-[1.02] ${
                      value === language.code ? 'bg-gray-800 ring-2 ring-blue-500' : ''
                    }`}
                  >
                    <div className={`flex h-12 w-12 items-center justify-center rounded-xl bg-gradient-to-r ${LANGUAGE_COLORS[language.code as keyof typeof LANGUAGE_COLORS]} text-white shadow-lg`}>
                      <span className="text-xl">{LANGUAGE_FLAGS[language.code as keyof typeof LANGUAGE_FLAGS]}</span>
                    </div>
                    <div className="flex-1 text-left">
                      <div className="text-lg font-semibold text-gray-100">
                        {showNativeNames ? language.nativeName : language.name}
                      </div>
                      <div className="text-sm text-gray-400">
                        {showNativeNames ? language.name : language.nativeName}
                      </div>
                    </div>
                    {value === language.code && (
                      <div className="flex h-6 w-6 items-center justify-center rounded-full bg-blue-500">
                        <svg className="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 20 20">
                          <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                        </svg>
                      </div>
                    )}
                  </button>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>
      <p className="text-xs text-gray-400">
        {t('forms.languageSelector.description')}
      </p>
    </div>
  );
}