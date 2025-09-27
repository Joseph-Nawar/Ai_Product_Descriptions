# AI Product Descriptions

A full-stack SaaS application for generating AI-powered product descriptions using Google's Gemini AI.

## Features

- **AI-Powered Descriptions**: Generate high-quality product descriptions using Google Gemini AI
- **Multiple Templates**: Support for electronics, fashion, and home goods
- **Batch Processing**: Upload CSV files for bulk description generation
- **Subscription Plans**: Free, Pro, and Enterprise tiers with Lemon Squeezy payments
- **User Authentication**: Firebase-based authentication system
- **Credit System**: Usage tracking and credit management

## Tech Stack

### Backend
- **FastAPI**: Python web framework
- **PostgreSQL**: Database
- **Firebase**: Authentication
- **Lemon Squeezy**: Payment processing
- **Google Gemini AI**: AI description generation

### Frontend
- **React**: UI framework
- **TypeScript**: Type safety
- **Vite**: Build tool
- **Tailwind CSS**: Styling
- **React Query**: Data fetching

## Deployment

### Backend (Render)
1. Connect GitHub repository to Render
2. Create new Web Service
3. Set build command: `cd backend && pip install -r requirements.txt`
4. Set start command: `cd backend && uvicorn src.main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables (see render.yaml)

### Frontend (Vercel)
1. Connect GitHub repository to Vercel
2. Set build command: `npm run build`
3. Set output directory: `dist`
4. Add environment variables

## Environment Variables

### Backend
- `ENV`: production
- `DATABASE_URL`: PostgreSQL connection string
- `LEMON_SQUEEZY_API_KEY`: Lemon Squeezy API key
- `LEMON_SQUEEZY_STORE_ID`: Store ID (224253)
- `LEMON_SQUEEZY_WEBHOOK_SECRET`: Webhook secret
- `FIREBASE_PROJECT_ID`: Firebase project ID
- `FIREBASE_SERVICE_ACCOUNT_BASE64`: Base64 encoded service account
- `GEMINI_API_KEY`: Google Gemini API key

### Frontend
- `VITE_API_BASE_URL`: Backend API URL
- `VITE_FIREBASE_*`: Firebase configuration
- `VITE_ALLOWED_REDIRECT_ORIGINS`: Allowed redirect origins

## Development

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn src.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## License

MIT