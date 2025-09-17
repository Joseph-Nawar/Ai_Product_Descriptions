# AI Product Description Generator

A professional, production-ready AI pipeline that generates compelling e-commerce product descriptions using Google Gemini. This backend system provides enterprise-grade logging, cost control, and safety measures for scalable product description generation.

## Lemon Squeezy – Local Testing (Vite + Express)

This setup allows you to test Lemon Squeezy webhooks locally with your Vite/React frontend and a minimal Express webhook server.

### Quick Start

1. **Start both servers locally:**
   ```bash
   npm run dev:all
   ```
   - Frontend: [http://localhost:5173](http://localhost:5173)
   - Webhook server: [http://localhost:3001/api/webhook](http://localhost:3001/api/webhook)

2. **Expose the webhook server publicly for Lemon Squeezy with ngrok (or Cloudflare Tunnel):**
   ```bash
   ngrok http 3001
   ```
   Copy the **https** URL (e.g., `https://xyz.ngrok-free.app`).

3. **In the Lemon Squeezy dashboard (Test Mode ON):**
   - Create a webhook: **Settings → Webhooks → New**
   - **Callback URL**: `https://<your-ngrok-subdomain>/api/webhook`
   - **Signing Secret**: set a value and put it in `.env` as `LEMON_SQUEEZY_WEBHOOK_SECRET`
   - Select events (e.g., `order_created`, `subscription_created`)

4. **Send a test event (or do a test checkout) and watch the terminal / ngrok inspector.** Expect `200 OK` and log lines like `[LS WEBHOOK OK]`.

5. **Notes:**
   - This setup is **for testing Lemon Squeezy locally** only.
   - The Vite app stays on port **5173**; webhooks are received on **3001**.
   - The server requires **raw body** for signature verification—do not add JSON middleware to the webhook route.
   - Tunnel URLs change on every ngrok restart unless you use a reserved domain.

---

## 🚀 Features

- **AI-Powered Content Generation**: Uses Google Gemini 1.5 Flash for high-quality product descriptions
- **Enterprise-Grade Logging**: Structured logging with file persistence and detailed metrics
- **Cost Control**: Real-time cost tracking with daily/monthly limits and budget alerts
- **Safety & Security**: Multi-layer content filtering and input validation
- **SEO Optimization**: Built-in SEO evaluation and keyword optimization
- **Scalable Architecture**: Professional backend designed for production use
- **Dry-Run Mode**: Test prompts without API calls for development and debugging

## 📁 Project Structure

```
backend/
├── src/
│   ├── ai_pipeline.py          # Main AI pipeline with enhanced features
│   ├── prompt_templates.py     # Prompt building utilities
│   ├── seo_check.py           # SEO evaluation functions
│   ├── data/
│   │   └── test_products.csv  # Sample product data
│   └── outputs/               # Generated outputs (created at runtime)
├── models/
│   └── prompt_templates/      # Category-specific prompt templates
│       ├── electronics.md
│       ├── fashion.md
│       └── homegoods.md
├── utils/
│   └── helpers.py             # Utility functions
├── requirements.txt           # Python dependencies
└── .env.example              # Environment configuration template
```

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- Google Gemini API key

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Ai_Product_Descriptions
   ```

2. **Create virtual environment**
   ```bash
   cd backend
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env and add your GEMINI_API_KEY
   ```

## ⚙️ Configuration

Create a `.env` file in the `backend/` directory:

```bash
# Gemini Configuration
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-1.5-flash
DEFAULT_TEMPERATURE=0.2

# Cost Control
DAILY_COST_LIMIT=1.00
MONTHLY_COST_LIMIT=10.00

# Output Configuration
OUTPUT_BASE=src/outputs
```

### Getting Your Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add it to your `.env` file

## 🚀 Usage

### Basic Usage

```bash
# Dry run (no API calls)
python src/ai_pipeline.py --input src/data/test_products.csv --limit 5 --dry-run

# Production run
python src/ai_pipeline.py --input src/data/test_products.csv --limit 10
```

### Command Line Options

- `--input`: Path to input CSV file (default: `src/data/test_products.csv`)
- `--limit`: Number of rows to process (default: 0 = no limit)
- `--dry-run`: Test mode without API calls

### Input CSV Format

Your CSV file should contain these columns:

| Column | Description | Required |
|--------|-------------|----------|
| `id` | Product identifier | Yes |
| `sku` | Product SKU | No |
| `title` | Product title | Yes |
| `category` | Product category | No |
| `features` | Semicolon-separated features | Yes |
| `primary_keyword` | SEO keyword | No |
| `tone` | Content tone (casual/professional/luxury) | No |
| `price` | Product price | No |
| `images` | Image URLs | No |

## 📊 Output Structure

The pipeline generates three types of output:

### 1. Raw Data (`outputs/raw/`)
- API responses and prompts
- Processing logs and error details
- Token usage and cost information

### 2. Enriched Data (`outputs/enriched/`)
- Parsed JSON with SEO scores
- Structured product descriptions
- Metadata and timestamps

### 3. Exports (`outputs/exports/`)
- CSV files ready for frontend integration
- Cost reports with usage statistics
- Production-ready data

## 🛡️ Safety & Security

### Content Filtering
- Multi-layer input validation
- Pattern-based inappropriate content detection
- Output sanitization for security
- Gemini built-in safety settings

### Cost Control
- Real-time cost tracking
- Daily/monthly spending limits
- Pre-run cost estimation
- Automatic stopping at budget limits

### Logging & Monitoring
- Structured logging with timestamps
- Performance metrics tracking
- Complete audit trail
- Error handling and reporting

## 🔧 Development

### Running Tests

```bash
# Dry run test
python src/ai_pipeline.py --input src/data/test_products.csv --limit 1 --dry-run

# Check logs
ls backend/src/outputs/logs/
```

### Adding New Prompt Templates

1. Create a new `.md` file in `models/prompt_templates/`
2. Follow the existing template format
3. Update the category mapping in `ai_pipeline.py`

### Customizing Safety Filters

Edit the `INAPPROPRIATE_PATTERNS` list in `ai_pipeline.py` to add or modify content filters.

## 📈 Performance

### Cost Optimization
- Token usage tracking and optimization
- Efficient prompt engineering
- Batch processing capabilities
- Cost estimation before runs

### Scalability
- Professional logging for monitoring
- Error handling and recovery
- Configurable limits and timeouts
- Production-ready architecture

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For issues and questions:
1. Check the logs in `backend/src/outputs/logs/`
2. Review the cost reports in `backend/src/outputs/exports/`
3. Ensure your API key is correctly configured
4. Verify input CSV format matches requirements

## 🔄 Version History

- **v1.1**: Enhanced logging, cost control, and safety measures
- **v1.0**: Initial Gemini integration
- **v0.9**: OpenAI integration (deprecated)

---

**⚠️ Important**: Always test with `--dry-run` before processing large datasets. Monitor costs and set appropriate limits in your `.env` file.


**Running:
.\start_backend.ps1

.\start_frontend.ps1