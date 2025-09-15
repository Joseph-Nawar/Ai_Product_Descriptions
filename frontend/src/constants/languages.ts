// ISO 639-1 codes are required for compatibility with i18n libraries and LLMs.
export const SUPPORTED_LANGUAGES = [
  { code: 'en', name: 'English', nativeName: 'English' },
  { code: 'es', name: 'Spanish', nativeName: 'Español' },
  { code: 'fr', name: 'French', nativeName: 'Français' },
  { code: 'de', name: 'German', nativeName: 'Deutsch' },
  { code: 'ja', name: 'Japanese', nativeName: '日本語' },
  { code: 'zh', name: 'Chinese', nativeName: '中文' }, // Focus on Simplified Chinese initially.
];

// Helper function to get language by code
export const getLanguageByCode = (code: string) => {
  return SUPPORTED_LANGUAGES.find(lang => lang.code === code);
};

// Helper function to get language name by code
export const getLanguageName = (code: string) => {
  const language = getLanguageByCode(code);
  return language ? language.name : code;
};

// Helper function to get native language name by code
export const getNativeLanguageName = (code: string) => {
  const language = getLanguageByCode(code);
  return language ? language.nativeName : code;
};

// Default language
export const DEFAULT_LANGUAGE = 'en';

// Check if a language code is supported
export const isLanguageSupported = (code: string): boolean => {
  return SUPPORTED_LANGUAGES.some(lang => lang.code === code);
};
