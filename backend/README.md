# Backend - AI Product Descriptions

This directory contains the backend services for the AI Product Descriptions application.

## Structure

- `src/` - Main backend code (APIs, automation, scripts)
- `models/` - Saved AI/ML models or prompt templates
- `utils/` - Helper functions (data cleaning, APIs, etc.)

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

3. Run the development server:
   ```bash
   uvicorn src.main:app --reload
   ```

## API Endpoints

- `POST /api/generate-description` - Generate product description
- `GET /api/health` - Health check endpoint

## Development

- Use `black` for code formatting
- Use `flake8` for linting
- Run tests with `pytest`
