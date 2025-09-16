# backend/src/ai_pipeline.py
import os
import sys
import logging
import time
import json
import csv
import pandas as pd
from pathlib import Path
import argparse
from datetime import datetime, timedelta
from dotenv import load_dotenv
from tenacity import retry, wait_exponential, stop_after_attempt
from tqdm import tqdm
import re

# Ensure backend/utils is importable
THIS_DIR = Path(__file__).resolve().parent
BACKEND_DIR = THIS_DIR.parent
sys.path.insert(0, str(BACKEND_DIR))

from utils.helpers import ensure_dir, timestamp, safe_extract_json, write_ndjson, write_json, read_text
# Import prompt builder and seo check (same folder)
sys.path.append(str(THIS_DIR))
from prompt_templates import build_prompt_from_row
from seo_check import seo_evaluate

# Gemini import
import google.generativeai as genai

class CostTracker:
    """Track API costs and usage"""
    def __init__(self):
        self.total_tokens = 0
        self.total_requests = 0
        self.cost_per_1k_tokens = 0.000075  # Gemini 1.5 Flash pricing
        self.daily_limit = 1000  # $1.00 daily limit
        self.monthly_limit = 10000  # $10.00 monthly limit
        
    def add_usage(self, tokens):
        """Add token usage and check limits"""
        self.total_tokens += tokens
        self.total_requests += 1
        
    def get_current_cost(self):
        """Calculate current cost"""
        return (self.total_tokens / 1000) * self.cost_per_1k_tokens
        
    def check_daily_limit(self):
        """Check if daily limit exceeded"""
        return self.get_current_cost() >= self.daily_limit
        
    def get_usage_stats(self):
        """Get usage statistics"""
        return {
            "total_tokens": self.total_tokens,
            "total_requests": self.total_requests,
            "current_cost": self.get_current_cost(),
            "cost_per_1k_tokens": self.cost_per_1k_tokens
        }

class SafetyFilter:
    """Content safety and input validation"""
    
    # Inappropriate content patterns
    INAPPROPRIATE_PATTERNS = [
        r'\b(illegal|unlawful|harmful|dangerous|toxic|poisonous)\b',
        r'\b(weapon|gun|knife|bomb|explosive)\b',
        r'\b(drug|narcotic|cocaine|heroin|marijuana)\b',
        r'\b(hate|racist|discriminatory|offensive)\b',
        r'\b(adult|porn|sex|explicit)\b'
    ]
    
    def __init__(self):
        self.compiled_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in self.INAPPROPRIATE_PATTERNS]
    
    def validate_input(self, text):
        """Validate input text for safety"""
        if not text or not isinstance(text, str):
            return False, "Empty or invalid input"
            
        # Check length
        if len(text) > 10000:
            return False, "Input too long (max 10,000 characters)"
            
        # Check for inappropriate content
        for pattern in self.compiled_patterns:
            if pattern.search(text):
                return False, f"Inappropriate content detected: {pattern.pattern}"
                
        return True, "Valid input"
    
    def sanitize_output(self, text):
        """Sanitize AI output"""
        if not text:
            return text
            
        # Remove potential security issues
        text = re.sub(r'<script.*?</script>', '', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'javascript:', '', text, flags=re.IGNORECASE)
        text = re.sub(r'on\w+\s*=', '', text, flags=re.IGNORECASE)
        
        return text.strip()

class StructuredLogger:
    """Enhanced logging with structured output"""
    
    def __init__(self, log_dir):
        self.log_dir = Path(log_dir)
        ensure_dir(self.log_dir)
        
        # Setup logging
        self.logger = logging.getLogger('ai_pipeline')
        self.logger.setLevel(logging.DEBUG)
        
        # File handler
        log_file = self.log_dir / f"pipeline_{timestamp()}.log"
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        
        self.logger.info(f"Logging initialized. Log file: {log_file}")
    
    def log_api_call(self, identifier, prompt_length, response_length, tokens_used, cost):
        """Log API call details"""
        self.logger.info(f"API_CALL - ID: {identifier}, Prompt: {prompt_length} chars, "
                        f"Response: {response_length} chars, Tokens: {tokens_used}, Cost: ${cost:.4f}")
    
    def log_error(self, identifier, error_type, error_message):
        """Log errors with context"""
        self.logger.error(f"ERROR - ID: {identifier}, Type: {error_type}, Message: {error_message}")
    
    def log_safety_check(self, identifier, check_type, result, details=""):
        """Log safety checks"""
        self.logger.info(f"SAFETY_CHECK - ID: {identifier}, Type: {check_type}, "
                        f"Result: {result}, Details: {details}")
    
    def log_cost_warning(self, current_cost, limit):
        """Log cost warnings"""
        self.logger.warning(f"COST_WARNING - Current cost: ${current_cost:.4f}, Limit: ${limit:.4f}")

def load_env(dry_run=False):
    """Load environment variables and initialize Gemini client"""
    env_path = BACKEND_DIR / ".env"
    
    # Load .env file if it exists
    if env_path.exists():
        print(f"Loading environment from: {env_path}")
        load_dotenv(env_path)
    else:
        print(f"No .env file found at: {env_path}")
        if not dry_run:
            print("Make sure to create a .env file with your GEMINI_API_KEY")
    
    # Get environment variables
    api_key = os.getenv("GEMINI_API_KEY")
    model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")
    temp = float(os.getenv("DEFAULT_TEMPERATURE", 0.8))
    output_base = os.getenv("OUTPUT_BASE", "src/outputs")
    
    # Cost control settings
    daily_limit = float(os.getenv("DAILY_COST_LIMIT", "1.00"))
    monthly_limit = float(os.getenv("MONTHLY_COST_LIMIT", "10.00"))
    
    # Validate API key (skip for dry run)
    if not api_key and not dry_run:
        raise RuntimeError("GEMINI_API_KEY not set in backend/.env file")
    
    if api_key:
        print(f"✅ Gemini API key loaded successfully")
        print(f"📊 Using model: {model_name}, temperature: {temp}")
        print(f"💰 Daily cost limit: ${daily_limit}, Monthly: ${monthly_limit}")
        
        # Configure Gemini
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)
    else:
        print(f"⚠️  No API key found - running in dry-run mode only")
        model = None
    
    return {
        "model": model,
        "model_name": model_name,
        "temperature": temp, 
        "output_base": output_base,
        "daily_limit": daily_limit,
        "monthly_limit": monthly_limit
    }

@retry(wait=wait_exponential(min=1, max=20), stop=stop_after_attempt(5))
def call_gemini_generate(model, prompt, temperature=0.2, logger=None, cost_tracker=None):
    """Make Gemini API call with enhanced monitoring"""
    try:
        # Configure generation parameters for enhanced creativity and quality
        generation_config = genai.types.GenerationConfig(
            temperature=temperature,
            max_output_tokens=2000,  # Increased for more detailed descriptions
            top_p=0.9,  # Increased for more creative responses
            top_k=50,   # Increased for better vocabulary diversity
            candidate_count=1
        )
        
        # Add safety settings
        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH", 
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            }
        ]
        
        start_time = time.time()
        response = model.generate_content(
            prompt,
            generation_config=generation_config,
            safety_settings=safety_settings
        )
        end_time = time.time()
        
        if response.text:
            # Estimate token usage (rough approximation)
            estimated_tokens = len(prompt.split()) + len(response.text.split())
            
            # Track costs
            if cost_tracker:
                cost_tracker.add_usage(estimated_tokens)
                current_cost = cost_tracker.get_current_cost()
                
                # Log API call
                if logger:
                    logger.log_api_call(
                        "api_call", 
                        len(prompt), 
                        len(response.text), 
                        estimated_tokens, 
                        current_cost
                    )
                
                # Check cost limits
                if cost_tracker.check_daily_limit():
                    if logger:
                        logger.log_cost_warning(current_cost, cost_tracker.daily_limit)
                    raise Exception(f"Daily cost limit exceeded: ${current_cost:.4f}")
            
            return response.text, estimated_tokens, end_time - start_time
        else:
            raise Exception("Empty response from Gemini")
            
    except Exception as e:
        error_msg = str(e)
        
        # Enhanced error categorization and logging
        if "quota" in error_msg.lower() or "limit" in error_msg.lower():
            error_type = "QUOTA_EXCEEDED"
            detailed_msg = f"API quota exceeded: {error_msg}"
        elif "safety" in error_msg.lower() or "blocked" in error_msg.lower():
            error_type = "SAFETY_FILTER"
            detailed_msg = f"Content blocked by safety filters: {error_msg}"
        elif "timeout" in error_msg.lower() or "connection" in error_msg.lower():
            error_type = "NETWORK_ERROR"
            detailed_msg = f"Network/connection issue: {error_msg}"
        elif "invalid" in error_msg.lower() or "malformed" in error_msg.lower():
            error_type = "INVALID_REQUEST"
            detailed_msg = f"Invalid request format: {error_msg}"
        else:
            error_type = "UNKNOWN_ERROR"
            detailed_msg = f"Unexpected error: {error_msg}"
        
        # Log detailed error information
        if logger:
            logger.log_error("api_call", error_type, detailed_msg)
        
        # Re-raise with more context
        raise Exception(f"Gemini API Error ({error_type}): {detailed_msg}")

def get_style_instructions(style_variation):
    """Get platform-specific writing instructions"""
    style_map = {
        "amazon": {
            "objective": "Maximize conversions and visibility via A9 algorithm",
            "format": "Keyword-heavy, bullet-point list for key features and specifications",
            "tone": "Professional, direct, and benefit-oriented",
            "structure": "Start with a short, engaging paragraph (approx. 2-3 lines) incorporating primary keywords. Follow with a detailed bulleted list (5-7 points) focusing on specs, features, and user benefits. Conclude with any necessary warranty/guarantee information."
        },
        "etsy": {
            "objective": "Connect emotionally and highlight craftsmanship",
            "format": "Narrative, storytelling prose",
            "tone": "Warm, personal, authentic, and inspired",
            "structure": "Begin with a story behind the product, the maker's inspiration, or the process of creation. Weave in keywords naturally. Describe the sensory details (e.g., 'feel,' 'look,' 'scent'). Mention the care and love put into making it. Include details about materials and their origin if possible."
        },
        "shopify": {
            "objective": "Build brand identity and engage customers",
            "format": "Flexible, blending storytelling with modern SEO and branding",
            "tone": "Confident, aspirational, and clean",
            "structure": "A cohesive brand story. Can use a short headline. Combine persuasive, benefit-driven copy with natural keyword integration. Structure can be a few medium-length paragraphs or a mix of short paragraphs and bullet points. Focus on the problem the product solves and the lifestyle it enables."
        },
        "ebay": {
            "objective": "Provide clear, concise information for a comparison-shopping audience",
            "format": "Strict, dense, and specification-focused",
            "tone": "Factual, straightforward, and unbiased",
            "structure": "Prioritize completeness and clarity. Use a very short introductory sentence. The body must be a dense, detailed list of specifications, condition (if used), dimensions, included components, and compatibility. Keywords are critical. Avoid fluff and marketing hyperbole."
        }
    }
    
    style = style_map.get(style_variation, style_map["amazon"])
    return f"""
**{style_variation.upper()} STYLE REQUIREMENTS:**
- **Objective:** {style['objective']}
- **Format:** {style['format']}
- **Tone:** {style['tone']}
- **Structure:** {style['structure']}

**CRITICAL:** Write the product description in the {style_variation.upper()} style, strictly adhering to the defined rules for that format."""

def build_gemini_prompt(row):
    """Build a professional copywriter-optimized prompt with enhanced structure and emotional appeal"""
    features_list = row.get("features", "")
    features_formatted = "\n".join([f"- {x.strip()}" for x in features_list.split(";") if x.strip()])
    
    # Get language code and create localization directive
    language_code = row.get("languageCode", "en")
    language_names = {
        "en": "English",
        "es": "Spanish", 
        "fr": "French",
        "de": "German",
        "ja": "Japanese",
        "zh": "Chinese"
    }
    target_language = language_names.get(language_code, "English")
    
    # Extract target audience from tone or create a default
    tone = row.get("tone", "professional").lower()
    audience_map = {
        "casual": "everyday consumers looking for comfort and style",
        "professional": "business professionals and working adults",
        "luxury": "discerning customers who value premium quality",
        "sporty": "active individuals and fitness enthusiasts",
        "modern": "tech-savvy consumers who appreciate contemporary design",
        "playful": "fun-loving consumers who enjoy vibrant and engaging products"
    }
    audience = audience_map.get(tone, "general consumers")
    
    # Get style variation and define style-specific instructions
    style_variation = row.get("style_variation", "amazon").lower()
    style_instructions = get_style_instructions(style_variation)
    
    # Enhanced professional copywriter prompt with product focus
    if style_variation == "etsy":
        # Etsy style - keep storytelling approach
        prompt = f"""You are a world-class professional copywriter specializing in e-commerce product descriptions. Your expertise lies in creating compelling, persuasive content that drives conversions and builds emotional connections with customers.

**YOUR MISSION:** Transform this product into an irresistible offer that speaks directly to the customer's desires and solves their problems.

**PRODUCT INFORMATION:**
- **Product Name:** {row.get("title", "")}
- **Key Features:** {features_formatted}
- **Target Audience:** {audience}
- **Primary Keyword:** {row.get("primary_keyword", "")}
- **Language:** {target_language}

**COPYWRITING STRATEGY:**
1. **EMOTIONAL HOOK:** Start with a compelling title that creates desire and urgency
2. **PROBLEM-SOLUTION NARRATIVE:** Frame the product as the solution to customer pain points
3. **SENSORY DETAILS:** Use vivid, sensory language that helps customers imagine using the product
4. **SOCIAL PROOF:** Imply quality and desirability through confident, authoritative language
5. **CALL TO ACTION:** Create urgency and desire to purchase

**STRUCTURE REQUIREMENTS:**
- **Compelling Title:** 5-8 words that create immediate interest and include the primary keyword
- **Engaging Description:** 2-3 sentences that paint a picture of the customer's improved life
- **Key Benefits:** 3-4 bullet points focusing on emotional benefits and outcomes, not just features
- **SEO Meta Description:** 140 characters optimized for search engines

**TONE GUIDELINES:**
- **Professional yet Enthusiastic:** Confident and knowledgeable without being pushy
- **Customer-Centric:** Focus on "you" and "your" to make it personal
- **Benefit-Focused:** Always explain WHY the feature matters to the customer
- **Sensory Rich:** Use words that evoke sight, touch, feel, and experience

**CRITICAL REQUIREMENTS:**
- Write entirely in {target_language} (no English text)
- Include the primary keyword naturally 1-2 times
- Focus on emotional benefits and outcomes, not technical specifications
- Use power words that create desire: "transform," "enhance," "discover," "experience," "unlock"
- Create urgency with words like "now," "today," "immediate," "instant"
- Avoid generic phrases like "high quality" or "great product"
- **YOU MUST PROVIDE 3 BULLET POINTS IN THE 'bullets' ARRAY. FAILURE TO DO SO WILL RESULT IN AN INCOMPLETE LISTING.**
- **YOUR RESPONSE MUST BE VALID JSON ONLY - NO ADDITIONAL TEXT BEFORE OR AFTER THE JSON OBJECT.**
- **THE 'bullets' ARRAY MUST CONTAIN EXACTLY 3 STRINGS - NO MORE, NO LESS.**

**OUTPUT FORMAT (JSON ONLY):**
{{
  "title": "Compelling 5-8 word title with primary keyword in {target_language}",
  "description": "2-3 sentence engaging paragraph focusing on customer transformation and emotional benefits in {target_language}",
  "bullets": [
    "Benefit-focused bullet point 1 emphasizing customer outcome in {target_language}",
    "Benefit-focused bullet point 2 emphasizing customer outcome in {target_language}",
    "Benefit-focused bullet point 3 emphasizing customer outcome in {target_language}"
  ],
  "meta": "140-character SEO-optimized meta description with primary keyword in {target_language}"
}}

**REMEMBER:** You're not just describing a product - you're selling a dream, a solution, and a better version of the customer's life. Make them feel the transformation this product will bring."""
    else:
        # All other styles - focus on product features and specifications
        prompt = f"""You are a professional e-commerce copywriter specializing in clear, informative product descriptions that drive sales through accurate feature presentation and benefit communication.

**YOUR MISSION:** Create compelling product descriptions that clearly communicate what the product is, what it does, and why customers should buy it.

**PRODUCT INFORMATION:**
- **Product Name:** {row.get("title", "")}
- **Key Features:** {features_formatted}
- **Target Audience:** {audience}
- **Primary Keyword:** {row.get("primary_keyword", "")}
- **Language:** {target_language}

**DESCRIPTION STRATEGY:**
1. **PRODUCT-FOCUSED:** Describe the actual product, its materials, specifications, and functionality
2. **FEATURE-BENEFIT CONNECTION:** Explain how each feature benefits the customer
3. **CLEAR SPECIFICATIONS:** Include relevant technical details, dimensions, materials, etc.
4. **PRACTICAL BENEFITS:** Focus on real-world uses and advantages
5. **CONFIDENT PRESENTATION:** Present the product professionally without excessive hype

**STRUCTURE REQUIREMENTS:**
- **Clear Title:** 5-8 words that accurately describe the product and include the primary keyword
- **Informative Description:** 2-3 sentences that describe what the product is and what it does
- **Feature Benefits:** 3 bullet points explaining specific features and their practical benefits
- **SEO Meta Description:** 140 characters optimized for search engines

**TONE GUIDELINES:**
- **Professional and Informative:** Clear, confident, and knowledgeable
- **Product-Centric:** Focus on the product itself, not abstract concepts
- **Benefit-Oriented:** Explain practical advantages and uses
- **Specification-Rich:** Include relevant technical details when appropriate

**CRITICAL REQUIREMENTS:**
- Write entirely in {target_language} (no English text)
- Include the primary keyword naturally 1-2 times
- Focus on PRODUCT FEATURES and SPECIFICATIONS, not abstract transformation
- Describe what the product IS and what it DOES
- Use concrete, specific language about materials, performance, and functionality
- Avoid vague emotional language like "transform your life" or "unlock potential"
- **YOU MUST PROVIDE 3 BULLET POINTS IN THE 'bullets' ARRAY. FAILURE TO DO SO WILL RESULT IN AN INCOMPLETE LISTING.**
- **YOUR RESPONSE MUST BE VALID JSON ONLY - NO ADDITIONAL TEXT BEFORE OR AFTER THE JSON OBJECT.**
- **THE 'bullets' ARRAY MUST CONTAIN EXACTLY 3 STRINGS - NO MORE, NO LESS.**

**OUTPUT FORMAT (JSON ONLY):**
{{
  "title": "Clear 5-8 word product title with primary keyword in {target_language}",
  "description": "2-3 sentence informative paragraph describing the product and its functionality in {target_language}",
  "bullets": [
    "Specific feature with practical benefit explanation in {target_language}",
    "Specific feature with practical benefit explanation in {target_language}",
    "Specific feature with practical benefit explanation in {target_language}"
  ],
  "meta": "140-character SEO-optimized meta description with primary keyword in {target_language}"
}}

**REMEMBER:** Describe the actual product - its features, materials, specifications, and practical benefits. Focus on what it IS and what it DOES, not abstract emotional transformation."""
    
    return prompt

def row_to_dict(row):
    """Convert pandas row to plain dict with expected keys"""
    return {
        "id": str(row.get("id","")).strip(),
        "sku": str(row.get("sku","")).strip(),
        "title": str(row.get("title","")).strip(),
        "category": str(row.get("category","")).strip().lower(),
        "features": str(row.get("features","")).strip(),
        "primary_keyword": str(row.get("primary_keyword","")).strip(),
        "tone": str(row.get("tone","")).strip(),
        "price": row.get("price", ""),
        "images": str(row.get("images","")).strip()
    }

def main(args):
    """Main pipeline function with enhanced logging, cost control, and safety"""
    print("🚀 Starting AI Product Description Pipeline (Gemini) - Enhanced")
    print(f"📁 Input file: {args.input}")
    print(f"🔢 Limit: {args.limit if args.limit > 0 else 'No limit'}")
    print(f"🧪 Dry run: {args.dry_run}")
    print("-" * 50)
    
    # Load environment and initialize components
    conf = load_env(dry_run=args.dry_run)
    model = conf["model"]
    model_name = conf["model_name"]
    temp = conf["temperature"]
    out_base = Path(BACKEND_DIR) / conf["output_base"]
    
    # Initialize enhanced components
    cost_tracker = CostTracker()
    safety_filter = SafetyFilter()
    
    # Create output directories
    run_ts = timestamp()
    run_raw_dir = out_base / "raw" / run_ts
    run_enriched_dir = out_base / "enriched" / run_ts
    run_exports_dir = out_base / "exports" / run_ts
    logs_dir = out_base / "logs" / run_ts
    
    ensure_dir(run_raw_dir)
    ensure_dir(run_enriched_dir)
    ensure_dir(run_exports_dir)
    ensure_dir(logs_dir)
    
    # Initialize structured logger
    logger = StructuredLogger(logs_dir)
    
    print(f"📂 Output directories created:")
    print(f"   Raw: {run_raw_dir}")
    print(f"   Enriched: {run_enriched_dir}")
    print(f"   Exports: {run_exports_dir}")
    print(f"   Logs: {logs_dir}")
    print("-" * 50)
    
    # Read input CSV
    print(f"📖 Reading input CSV: {args.input}")
    df = pd.read_csv(args.input)
    print(f"📊 Found {len(df)} rows in input file")
    
    if args.limit:
        df = df.head(int(args.limit))
        print(f"🔢 Limited to {len(df)} rows")
    
    # Estimate costs before processing
    estimated_cost = (len(df) * 500 / 1000) * cost_tracker.cost_per_1k_tokens  # Rough estimate
    print(f"💰 Estimated cost: ${estimated_cost:.4f}")
    
    if estimated_cost > conf["daily_limit"]:
        print(f"⚠️  WARNING: Estimated cost exceeds daily limit!")
        if not args.dry_run:
            response = input("Continue anyway? (y/N): ")
            if response.lower() != 'y':
                print("❌ Processing cancelled by user")
                return
    
    results_enriched = []
    raw_records = []
    
    print(f"🔄 Processing {len(df)} rows...")
    print("-" * 50)
    
    for idx, prow in tqdm(df.iterrows(), total=len(df), desc="Processing rows"):
        row = row_to_dict(prow)
        identifier = row["id"] or row["sku"] or row["title"][:30]
        
        print(f"📝 Processing row {idx + 1}/{len(df)}: {identifier}")
        
        # Enhanced input validation
        is_valid, validation_msg = safety_filter.validate_input(row["title"] + " " + row["features"])
        if not is_valid:
            print(f"⚠️  Skipping {identifier}: {validation_msg}")
            logger.log_safety_check(identifier, "INPUT_VALIDATION", "FAILED", validation_msg)
            raw_records.append({
                "id": identifier, 
                "status": "skipped_safety_check",
                "reason": validation_msg
            })
            continue
        
        # Basic validation
        if not row["title"] or not row["features"]:
            print(f"⚠️  Skipping {identifier}: Missing title or features")
            raw_records.append({
                "id": identifier, 
                "status": "skipped_missing_fields",
                "reason": "Missing title or features"
            })
            continue
        
        # Build Gemini-optimized prompt
        try:
            prompt = build_gemini_prompt(row)
            print(f"✅ Gemini prompt built for {identifier}")
            logger.log_safety_check(identifier, "PROMPT_BUILD", "SUCCESS")
        except Exception as e:
            print(f"❌ Failed to build prompt for {identifier}: {str(e)}")
            logger.log_error(identifier, "PROMPT_ERROR", str(e))
            raw_records.append({
                "id": identifier, 
                "status": "prompt_error", 
                "error": str(e)
            })
            continue
        
        # Dry-run mode: save prompt and continue
        if args.dry_run:
            pfile = run_raw_dir / f"{identifier}_prompt.txt"
            pfile.write_text(prompt, encoding="utf-8")
            print(f"💾 Dry run: Saved prompt for {identifier}")
            raw_records.append({
                "id": identifier, 
                "status": "dry_run_prompt_saved",
                "prompt_file": str(pfile)
            })
            continue
        
        # Call Gemini API with enhanced monitoring
        try:
            print(f"🤖 Calling Gemini API for {identifier}...")
            ai_text, tokens_used, response_time = call_gemini_generate(
                model=model, 
                prompt=prompt, 
                temperature=temp,
                logger=logger,
                cost_tracker=cost_tracker
            )
            
            # Sanitize output
            ai_text = safety_filter.sanitize_output(ai_text)
            
            print(f"✅ Gemini response received for {identifier}")
            print(f"📝 Response length: {len(ai_text)} characters")
            print(f"⏱️  Response time: {response_time:.2f}s")
            print(f"💰 Current cost: ${cost_tracker.get_current_cost():.4f}")
            
            # Write raw response
            raw_records.append({
                "id": identifier,
                "prompt": prompt,
                "ai_raw_text": ai_text,
                "status": "completed",
                "model": model_name,
                "tokens_used": tokens_used,
                "response_time": response_time,
                "cost": cost_tracker.get_current_cost()
            })
            
        except Exception as e:
            print(f"❌ Gemini API error for {identifier}: {str(e)}")
            logger.log_error(identifier, "API_ERROR", str(e))
            raw_records.append({
                "id": identifier, 
                "status": "api_error", 
                "error": str(e)
            })
            continue
        
        # Parse AI response
        try:
            print(f"🔍 Parsing JSON response for {identifier}...")
            parsed = safe_extract_json(ai_text)
            
            # Extract fields with fallbacks
            title = parsed.get("title", row.get("title", ""))
            description = parsed.get("description", "").strip()
            bullets = parsed.get("bullets", [])
            meta = parsed.get("meta", "")
            
            # Additional safety check on output
            is_safe, safety_msg = safety_filter.validate_input(description)
            if not is_safe:
                print(f"⚠️  Output safety check failed for {identifier}: {safety_msg}")
                logger.log_safety_check(identifier, "OUTPUT_VALIDATION", "FAILED", safety_msg)
                description = "Content filtered for safety"
            
            # SEO evaluation
            seo = seo_evaluate(description, row.get("primary_keyword",""))
            
            enriched = {
                "id": identifier,
                "sku": row.get("sku"),
                "title": title,
                "original_title": row.get("title"),
                "category": row.get("category"),
                "description": description,
                "bullets": bullets,
                "meta": meta,
                "seo_score": seo,
                "prompt_version": "gemini-v1.1-enhanced",
                "model": model_name,
                "tokens_used": tokens_used,
                "response_time": response_time,
                "cost": cost_tracker.get_current_cost(),
                "status": "final" if seo["passes"] else "needs_seo",
                "timestamp": run_ts
            }
            
            print(f"✅ Successfully parsed and enriched {identifier}")
            print(f"📝 Description length: {len(description)} chars")
            print(f"🔍 SEO passes: {seo['passes']}")
            
        except Exception as e:
            print(f"❌ Parse error for {identifier}: {str(e)}")
            logger.log_error(identifier, "PARSE_ERROR", str(e))
            enriched = {
                "id": identifier,
                "title": row.get("title"),
                "category": row.get("category"),
                "description_raw": ai_text,
                "parse_error": True,
                "parse_error_msg": str(e),
                "status": "parse_error",
                "timestamp": run_ts
            }
        
        results_enriched.append(enriched)
        print(f"✅ Completed processing {identifier}")
        print("-" * 30)
    
    # Write output files
    print("💾 Writing output files...")
    
    # Write raw records
    raw_file = run_raw_dir / "run_raw.ndjson"
    write_ndjson(raw_file, raw_records)
    print(f"📄 Raw records written: {raw_file}")
    
    # Write enriched records
    enriched_file = run_enriched_dir / "enriched.json"
    write_json(enriched_file, results_enriched)
    print(f"📄 Enriched records written: {enriched_file}")
    
    # Write CSV export
    export_csv = run_exports_dir / "export.csv"
    with open(export_csv, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id","sku","title","final_description","bullets","meta","status"])
        
        for item in results_enriched:
            writer.writerow([
                item.get("id",""),
                item.get("sku",""),
                item.get("title",""),
                item.get("description","") or item.get("description_raw",""),
                "|".join(item.get("bullets", [])) if item.get("bullets") else "",
                item.get("meta",""),
                item.get("status","")
            ])
    
    print(f"📄 CSV export written: {export_csv}")
    
    # Write cost report
    cost_report = run_exports_dir / "cost_report.json"
    usage_stats = cost_tracker.get_usage_stats()
    write_json(cost_report, usage_stats)
    print(f"💰 Cost report written: {cost_report}")
    
    # Summary
    print("=" * 50)
    print("🎉 PIPELINE COMPLETE!")
    print(f"📊 Processed: {len(df)} rows")
    print(f"✅ Successful: {len([r for r in raw_records if r['status'] == 'completed'])}")
    print(f"❌ Errors: {len([r for r in raw_records if r['status'] == 'api_error'])}")
    print(f"⚠️  Skipped: {len([r for r in raw_records if r['status'] == 'skipped_missing_fields'])}")
    print(f"🛡️  Safety filtered: {len([r for r in raw_records if r['status'] == 'skipped_safety_check'])}")
    print(f"🧪 Dry run: {len([r for r in raw_records if r['status'] == 'dry_run_prompt_saved'])}")
    print(f"💰 Total cost: ${cost_tracker.get_current_cost():.4f}")
    print(f"🔢 Total tokens: {cost_tracker.total_tokens:,}")
    print("=" * 50)
    print(f"📂 Output locations:")
    print(f"   Raw: {run_raw_dir}")
    print(f"   Enriched: {run_enriched_dir}")
    print(f"   Exports: {run_exports_dir}")
    print(f"   Logs: {logs_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Product Description Pipeline (Gemini) - Enhanced")
    parser.add_argument("--input", default=str(Path(__file__).parent / "data/test_products.csv"),
                       help="Input CSV file path")
    parser.add_argument("--limit", type=int, default=0,
                       help="Limit number of rows to process (0 = no limit)")
    parser.add_argument("--dry-run", action="store_true",
                       help="Dry run mode - only save prompts, don't call API")
    args = parser.parse_args()
    main(args)