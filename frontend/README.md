# Frontend - AI Product Descriptions

This directory contains the frontend React application for the AI Product Descriptions tool.

## Structure

- `public/` - Static files (icons, logos, etc.)
- `src/` - React code (UI components, pages, etc.)

## Setup

1. Install dependencies:
   ```bash
   npm install
   ```

2. Start the development server:
   ```bash
   npm run dev
   ```

3. Build for production:
   ```bash
   npm run build
   ```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint
- `npm run lint:fix` - Fix ESLint issues

## Tech Stack

- React 18
- TypeScript
- Vite
- Axios for API calls
- React Router for navigation

## Configuration (.env)

Create `frontend/.env` with:

```
VITE_API_BASE_URL=http://localhost:8000
# Set to "true" to use the frontend mock generator until backend is live
VITE_USE_MOCK=true
```

- `VITE_API_BASE_URL` – Base URL of the backend API (no trailing slash).  
- `VITE_USE_MOCK` – When `"true"`, the app uses a local mock generator for `/generate` and `/download/:id`.

When `VITE_USE_MOCK="true"`, the app serves `/generate` and `/download/:id` from the local mock layer instead of the backend.
