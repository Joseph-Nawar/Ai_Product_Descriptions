import React, { useState, useRef, useEffect } from 'react';

const STYLES = [
  { 
    key: 'amazon', 
    label: 'Amazon', 
    icon: '📦',
    color: 'from-orange-500 to-red-600',
    description: 'Keyword-optimized for A9 algorithm',
    badge: 'SEO'
  },
  { 
    key: 'etsy', 
    label: 'Etsy', 
    icon: '🎨',
    color: 'from-green-500 to-teal-600',
    description: 'Handcrafted storytelling approach',
    badge: 'ARTISAN'
  },
  { 
    key: 'shopify', 
    label: 'Shopify', 
    icon: '🛍️',
    color: 'from-purple-500 to-indigo-600',
    description: 'Brand-focused aspirational copy',
    badge: 'PREMIUM'
  },
  { 
    key: 'ebay', 
    label: 'eBay', 
    icon: '🔍',
    color: 'from-blue-500 to-cyan-600',
    description: 'Factual specification-focused',
    badge: 'DETAILED'
  },
];

type Props = {
  value: string;
  onChange: (value: string) => void;
};

export default function StyleSelector({ value, onChange }: Props) {
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

  const selectedStyle = STYLES.find(style => style.key === value) || STYLES[0];

  return (
    <div className="relative w-full z-[99998]" ref={dropdownRef}>
      <button
        type="button"
        onClick={() => setIsOpen(!isOpen)}
        className="w-full relative overflow-hidden rounded-2xl border-2 border-gray-600 bg-gradient-to-r from-gray-800 to-gray-900 px-6 py-4 text-left transition-all duration-300 hover:border-gray-500 hover:shadow-lg hover:shadow-gray-900/50 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 group"
      >
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <div className={`flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-to-r ${selectedStyle.color} text-white shadow-lg`}>
              <span className="text-lg">{selectedStyle.icon}</span>
            </div>
            <div>
              <div className="flex items-center space-x-2">
                <div className="text-lg font-semibold text-gray-100">{selectedStyle.label}</div>
                <div className={`px-2 py-1 rounded-full text-xs font-bold bg-gradient-to-r ${selectedStyle.color} text-white`}>
                  {selectedStyle.badge}
                </div>
              </div>
              <div className="text-sm text-gray-400">{selectedStyle.description}</div>
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
              {STYLES.map((style) => (
                <button
                  key={style.key}
                  onClick={() => {
                    onChange(style.key);
                    setIsOpen(false);
                  }}
                  className={`w-full flex items-center space-x-4 px-4 py-4 rounded-xl transition-all duration-200 hover:bg-gray-800 hover:scale-[1.02] ${
                    value === style.key ? 'bg-gray-800 ring-2 ring-blue-500' : ''
                  }`}
                >
                  <div className={`flex h-12 w-12 items-center justify-center rounded-xl bg-gradient-to-r ${style.color} text-white shadow-lg`}>
                    <span className="text-xl">{style.icon}</span>
                  </div>
                  <div className="flex-1 text-left">
                    <div className="flex items-center space-x-2 mb-1">
                      <div className="text-lg font-semibold text-gray-100">{style.label}</div>
                      <div className={`px-2 py-1 rounded-full text-xs font-bold bg-gradient-to-r ${style.color} text-white`}>
                        {style.badge}
                      </div>
                    </div>
                    <div className="text-sm text-gray-400">{style.description}</div>
                  </div>
                  {value === style.key && (
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
  );
}