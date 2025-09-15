import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import LanguageDetector from 'i18next-browser-languagedetector';
import { SUPPORTED_LANGUAGES, DEFAULT_LANGUAGE } from '../constants/languages';

// Import translation resources
import enTranslation from '../../public/locales/en/translation.json';
import esTranslation from '../../public/locales/es/translation.json';
import frTranslation from '../../public/locales/fr/translation.json';
import deTranslation from '../../public/locales/de/translation.json';
import jaTranslation from '../../public/locales/ja/translation.json';
import zhTranslation from '../../public/locales/zh/translation.json';

const resources = {
  en: { translation: enTranslation },
  es: { translation: esTranslation },
  fr: { translation: frTranslation },
  de: { translation: deTranslation },
  ja: { translation: jaTranslation },
  zh: { translation: zhTranslation },
};

i18n
  .use(LanguageDetector)
  .use(initReactI18next)
  .init({
    resources,
    fallbackLng: DEFAULT_LANGUAGE,
    supportedLngs: SUPPORTED_LANGUAGES.map(lang => lang.code),
    
    detection: {
      order: ['localStorage', 'navigator', 'htmlTag'],
      caches: ['localStorage'],
      lookupLocalStorage: 'i18nextLng',
    },
    
    interpolation: {
      escapeValue: false, // React already does escaping
    },
    
    react: {
      useSuspense: false, // Disable suspense for better error handling
    },
  });

export default i18n;
