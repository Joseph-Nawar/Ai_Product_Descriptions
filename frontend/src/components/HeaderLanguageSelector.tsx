import React, { useState, useRef, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import { SUPPORTED_LANGUAGES } from '../constants/languages';

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

interface HeaderLanguageSelectorProps {
  value: string;
  onChange: (languageCode: string) => void;
}

export default function HeaderLanguageSelector({ value, onChange }: HeaderLanguageSelectorProps) {
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
    <div className="relative z-[99998]" ref={dropdownRef}>
      <button
        type="button"
        onClick={() => setIsOpen(!isOpen)}
        className="flex items-center space-x-2 px-3 py-2 bg-gray-800/50 border border-gray-600 rounded-lg text-gray-100 text-sm transition-all duration-200 hover:bg-gray-700/50 hover:border-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
      >
        <span className="text-sm">{LANGUAGE_FLAGS[selectedLanguage.code as keyof typeof LANGUAGE_FLAGS]}</span>
        <span className="text-sm font-medium">{selectedLanguage.nativeName}</span>
        <svg 
          className={`w-4 h-4 text-gray-300 transition-transform duration-200 ${isOpen ? 'rotate-180' : ''}`} 
          fill="none" 
          stroke="currentColor" 
          viewBox="0 0 24 24"
        >
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
        </svg>
      </button>

      {isOpen && (
        <div className="absolute top-full right-0 mt-2 z-[99999] min-w-[200px]">
          <div className="bg-gray-900 border-2 border-gray-600 rounded-xl shadow-2xl overflow-hidden">
            <div className="p-1">
              {SUPPORTED_LANGUAGES.map((language) => (
                <button
                  key={language.code}
                  onClick={() => {
                    onChange(language.code);
                    setIsOpen(false);
                  }}
                  className={`w-full flex items-center space-x-3 px-3 py-2 rounded-lg transition-all duration-200 hover:bg-gray-800 ${
                    value === language.code ? 'bg-gray-800 ring-1 ring-blue-500' : ''
                  }`}
                >
                  <span className="text-sm">{LANGUAGE_FLAGS[language.code as keyof typeof LANGUAGE_FLAGS]}</span>
                  <div className="flex-1 text-left">
                    <div className="text-sm font-medium text-gray-100">{language.nativeName}</div>
                    <div className="text-xs text-gray-400">{language.name}</div>
                  </div>
                  {value === language.code && (
                    <div className="flex h-4 w-4 items-center justify-center rounded-full bg-blue-500">
                      <svg className="w-3 h-3 text-white" fill="currentColor" viewBox="0 0 20 20">
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
  );
}
