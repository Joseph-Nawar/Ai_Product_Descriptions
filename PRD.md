📄 Product Requirements Document (PRD)

Project: AI-Powered Product Description Generator for E-commerce
Team:

Person 1 (Backend – AI Workflow Developer)

Person 2 (Frontend – UI/UX Engineer)

1. Project Overview

We are building a full-stack, production-ready AI product description generator for e-commerce stores.
The tool will:

Accept product details (title, category, features, audience).

Generate SEO-friendly product descriptions using AI.

Allow batch processing via CSV input.

Provide a user-friendly frontend where freelancers/clients can upload product data and download polished descriptions.

Primary Use Case: Freelancers and small e-commerce store owners who need fast, scalable product descriptions to boost SEO and sales.

2. Goals & Deliverables

Backend (Person 1):

Build pipeline: input → AI → output.

Implement prompt templates for multiple categories.

Ensure SEO optimization (keyword checks).

Provide clean API endpoints for frontend to call.

Frontend (Person 2):

Build UI for uploading CSVs or entering products manually.

Display generated descriptions in a table format with options to edit, copy, or export (CSV/JSON).

Ensure UX is simple and polished.

3. Directory Structure (Shared Standard)
repo-name/
├── backend/             
│   ├── src/             # main backend code (APIs, automation, scripts)
│   ├── models/          # saved AI prompt templates
│   ├── utils/           # helper functions (data cleaning, SEO check, etc.)
│   ├── requirements.txt # Python dependencies
│   └── README.md        # backend-specific documentation
│
├── frontend/            
│   ├── public/          # static files (icons, logos, etc.)
│   ├── src/             # React code (UI components, pages, etc.)
│   ├── package.json     # Node dependencies
│   └── README.md        # frontend-specific documentation
│
├── docs/                # shared documentation (API usage, workflows)
├── assets/              # design/UI/UX assets (screenshots, logos, images)
├── .gitignore
├── LICENSE
└── README.md            # root project overview

4. Detailed Role Responsibilities
👤 Person 1: AI Workflow Developer (Backend)

Tool Research & Setup

Test APIs: OpenAI GPT-4/ChatGPT, Jasper, Copy.ai.

Choose based on cost, reliability, and API availability.

Store API keys securely (e.g., .env).

Prompt Engineering

Create prompt templates and store in backend/models/.

Example template:

Write a 100-word SEO-friendly product description for a [product_name] in the [category].
Include features: [features].
Use persuasive but natural tone.
Target audience: [audience].


Design prompts for different categories (fashion, electronics, home goods).

Batch Generation Script

Input: CSV file (product_name, category, features, audience).

Output: JSON + CSV with unique IDs for each description.

Store in backend/src/outputs/.

SEO Enrichment

Implement lightweight SEO checks: keyword density, length, readability.

Store final enriched descriptions in separate folder.

API Development

Build REST API endpoints in backend/src/api.py (e.g., Flask/FastAPI):

POST /generate → generate descriptions for single/multiple products.

GET /download/<batch_id> → download generated outputs.

👤 Person 2: Frontend Engineer (UI/UX)

UI/UX Design

Pages:

Home: Upload CSV or input product manually.

Results Dashboard: Table of generated descriptions with edit/copy/export options.

Layout:

Clean, minimal white design.

Export buttons (CSV/JSON).

Status indicators (loading, success, error).

Frontend Development

Framework: React.js.

File Upload Component → POST to backend /generate.

Display results in a table (editable cells).

Integration

Call backend API to fetch generated descriptions.

Implement download feature.

Polish

Responsive design (mobile + desktop).

User feedback states (loading spinners, success banners).

5. Workflow & Collaboration (GitHub)

Branches

main: production only.

dev: integration branch.

feature/*: task-specific.

Process

Each person creates feature/ branches.

Commit often with clear messages.

Push → Open PR → Other person reviews → Merge to dev.

Merge dev → main only for production releases.

6. Tools & Dependencies

Backend:

Python (Flask or FastAPI).

OpenAI API / Jasper API.

Pandas (CSV handling).

SEO library (e.g., textstat).

Frontend:

React.js.

Axios (API calls).

TailwindCSS (styling).

React Table or Material UI (for displaying results).

7. Deliverables & Milestones

Week 1:

Backend: Prompt library + basic generation script.

Frontend: Skeleton UI (upload + results page).

Week 2:

Backend: Batch processing + SEO enrichment + REST API.

Frontend: Connect to API + display generated results.

Week 3:

Testing + polish + export features.

Final repo cleanup & documentation.