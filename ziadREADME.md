# AI Product Descriptions

An intelligent application that generates compelling product descriptions using AI technology.

## Project Structure

```
├── backend/             # Backend services (Person 1)
│   ├── src/             # Main backend code (APIs, automation, scripts)
│   ├── models/          # Saved AI/ML models or prompt templates
│   ├── utils/           # Helper functions (data cleaning, APIs, etc.)
│   ├── requirements.txt # Python dependencies
│   └── README.md        # Backend-specific documentation
│
├── frontend/            # Frontend application (Person 2)
│   ├── public/          # Static files (icons, logos, etc.)
│   ├── src/             # React/Vue code (UI components, pages, etc.)
│   ├── package.json     # Node dependencies
│   └── README.md        # Frontend-specific documentation
│
├── docs/                # Shared documentation (API usage, workflows)
├── assets/              # Design/UI/UX assets (screenshots, logos, images)
├── .gitignore
├── LICENSE
└── README.md            # This file
```

## Features

- 🤖 AI-powered product description generation
- 🎨 Modern, responsive web interface
- ⚡ Fast API backend with FastAPI
- 🔧 Easy-to-use configuration
- 📱 Mobile-friendly design

## Quick Start

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
uvicorn src.main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## Development

This project is designed for collaborative development with clear separation of concerns:

- **Backend Developer**: Focus on `backend/` directory
- **Frontend Developer**: Focus on `frontend/` directory
- **Shared Resources**: Use `docs/` and `assets/` for collaboration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
