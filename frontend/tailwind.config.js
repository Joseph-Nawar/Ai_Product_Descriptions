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
          DEFAULT: '#38bdf8', // sky-400
          dark: '#0ea5e9',   // sky-500
        },
        secondary: {
          DEFAULT: '#a78bfa', // violet-400
          dark: '#8b5cf6',   // violet-500
        },
        accent: {
          cyan: '#22d3ee',
          fuchsia: '#d946ef',
          emerald: '#34d399',
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
        'glow-primary': '0 0 20px 0 rgba(56, 189, 248, 0.4)',
        'glow-secondary': '0 0 20px 0 rgba(167, 139, 250, 0.4)',
      },
    },
  },
  plugins: [],
};