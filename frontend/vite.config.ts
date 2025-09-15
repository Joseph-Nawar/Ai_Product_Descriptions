import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { visualizer } from 'rollup-plugin-visualizer'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    react(),
    // Add bundle analyzer
    visualizer({
      filename: 'dist/stats.html',
      open: true,
      gzipSize: true,
      brotliSize: true,
    }),
  ],
  build: {
    // Use esbuild for faster minification
    minify: 'esbuild',
    // Disable sourcemaps in production for smaller bundle
    sourcemap: false,
    // Optimize chunk splitting
    rollupOptions: {
      output: {
        manualChunks: {
          // Core React libraries
          'react-vendor': ['react', 'react-dom'],
          // Router
          'router': ['react-router-dom'],
          // Heavy UI libraries
          'table': ['@tanstack/react-table'],
          // Utility libraries
          'utils': ['axios', 'papaparse'],
          // i18n libraries
          'i18n': ['i18next', 'i18next-browser-languagedetector', 'react-i18next'],
        },
        // Optimize chunk naming for better caching
        chunkFileNames: 'assets/[name]-[hash].js',
        entryFileNames: 'assets/[name]-[hash].js',
        assetFileNames: 'assets/[name]-[hash].[ext]',
      },
    },
    // Enable CSS code splitting
    cssCodeSplit: true,
    // Optimize asset handling
    assetsInlineLimit: 4096, // Inline assets smaller than 4kb
    // Target modern browsers for smaller bundles
    target: 'esnext',
  },
  // Optimize dev server
  server: {
    hmr: {
      overlay: false,
    },
  },
  // Enable compression
  preview: {
    port: 5173,
  },
})
