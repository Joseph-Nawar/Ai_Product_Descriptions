import React from 'react';
import { useTranslation } from 'react-i18next';
import { SUPPORTED_LANGUAGES, getLanguageByCode } from '../constants/languages';

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

  return (
    <div className={`space-y-2 ${className}`}>
      <label className="text-sm font-medium text-gray-300">
        {t('forms.languageSelector.label')}
      </label>
      <select
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="w-full px-3 py-2 bg-gray-800 border border-glass-border rounded-lg text-gray-100 focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent"
      >
        {SUPPORTED_LANGUAGES.map((language) => (
          <option key={language.code} value={language.code}>
            {showNativeNames ? language.nativeName : language.name}
          </option>
        ))}
      </select>
      <p className="text-xs text-gray-400">
        {t('forms.languageSelector.description')}
      </p>
    </div>
  );
}
