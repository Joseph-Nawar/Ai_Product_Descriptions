/** @type {import('tailwindcss').Config} */
import defaultTheme from 'tailwindcss/defaultTheme';

export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', ...defaultTheme.fontFamily.sans],
      },
      colors: {
        primary: {
          DEFAULT: '#2563eb', // blue-600 - matches ProductGenie blue
          dark: '#1d4ed8',   // blue-700
        },
        secondary: {
          DEFAULT: '#1e40af', // blue-800 - darker blue for contrast
          dark: '#1e3a8a',   // blue-900
        },
        accent: {
          cyan: '#0891b2',   // cyan-600 - light blue accent
          fuchsia: '#c026d3', // fuchsia-600 - red accent for tie
          emerald: '#059669', // emerald-600 - success green
          gold: '#d97706',   // amber-600 - gold accent
          lightblue: '#0ea5e9', // sky-500 - light blue for genie
        },
        'glass-border': 'rgba(255, 255, 255, 0.1)',
        'glass-bg': 'rgba(17, 24, 39, 0.6)', // gray-900 with opacity
      },
      animation: {
        'fade-in': 'fadeIn 0.6s ease-out forwards',
        'slide-in': 'slideIn 0.6s ease-out forwards',
        'shimmer': 'shimmer 2s linear infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideIn: {
          '0%': { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        shimmer: {
          '0%': { 'background-position': '200% 0' },
          '100%': { 'background-position': '-200% 0' },
        },
      },
      boxShadow: {
        'glow-primary': '0 0 20px 0 rgba(37, 99, 235, 0.4)',
        'glow-secondary': '0 0 20px 0 rgba(30, 64, 175, 0.4)',
      },
    },
  },
  plugins: [],
};