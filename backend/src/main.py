# backend/src/main.py
import os
import sys
import logging
import asyncio
import time
from pathlib import Path
from typing import List, Dict, Any, Optional
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import pandas as pd
import json
import io
from dotenv import load_dotenv

# Add backend directory to path for imports
THIS_DIR = Path(__file__).resolve().parent
BACKEND_DIR = THIS_DIR.parent
sys.path.insert(0, str(BACKEND_DIR))

from utils.helpers import ensure_dir, timestamp, safe_extract_json
from src.ai_pipeline import load_env, call_gemini_generate, build_gemini_prompt, row_to_dict, CostTracker, SafetyFilter
from src.seo_check import seo_evaluate

# Load environment
load_dotenv(BACKEND_DIR / ".env")

# Initialize FastAPI app
app = FastAPI(
    title="AI Product Descriptions API",
    description="API for generating AI-powered product descriptions",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variables for model and components
model = None
cost_tracker = None
safety_filter = None

def find_column(columns, synonyms):
    """
    Find the best matching column for given synonyms.
    Normalizes column names and returns the first match.
    """
    normalized_columns = {}
    for col in columns:
        # Normalize: lowercase, remove spaces, hyphens, underscores
        normalized = col.lower().replace(' ', '').replace('-', '').replace('_', '')
        normalized_columns[normalized] = col
    
    for synonym in synonyms:
        normalized_synonym = synonym.lower().replace(' ', '').replace('-', '').replace('_', '')
        if normalized_synonym in normalized_columns:
            return normalized_columns[normalized_synonym]
    
    return None

def process_csv_row(row, target_audience, columns, language_code="en"):
    """
    Process a CSV row using automatic column mapping and dynamic feature generation.
    """
    # Define synonyms for automatic mapping
    product_name_synonyms = ['title', 'name', 'product', 'productname', 'item', 'model']
    category_synonyms = ['category', 'type', 'department', 'group', 'collection']
    
    # Blocklist for columns that shouldn't be used as features
    feature_blocklist = ['id', 'sku', 'price', 'cost', 'url', 'image', 'images']
    
    # Find mapped columns
    product_name_col = find_column(columns, product_name_synonyms)
    category_col = find_column(columns, category_synonyms)
    
    # Fallback logic
    if not product_name_col:
        product_name_col = columns[0] if columns else "Unknown"
    
    if not category_col:
        category_col = "General"
    
    # Extract values
    product_name = str(row.get(product_name_col, "")).strip()
    category = str(row.get(category_col, "")).strip() if category_col != "General" else "General"
    
    # Generate features from all other columns
    feature_parts = []
    for col in columns:
        if col not in [product_name_col, category_col] and col.lower() not in feature_blocklist:
            value = str(row.get(col, "")).strip()
            if value:  # Only include non-empty values
                feature_parts.append(f"{col}: {value}")
    
    features = ". ".join(feature_parts) if feature_parts else ""
    
    # Log mapping decisions for debugging
    logging.info(f"Mapped '{product_name_col}' to 'product_name', '{category_col}' to 'category'")
    
    return {
        "id": str(row.get("id", "")).strip(),
        "sku": str(row.get("sku", "")).strip(),
        "title": product_name,
        "category": category.lower(),
        "features": features,
        "primary_keyword": str(row.get("primary_keyword", "")).strip(),
        "tone": str(row.get("tone", "")).strip(),
        "price": row.get("price", ""),
        "images": str(row.get("images", "")).strip(),
        "audience": target_audience,
        "languageCode": language_code
    }

@app.on_event("startup")
async def startup_event():
    """Initialize the AI model and components on startup"""
    global model, cost_tracker, safety_filter
    
    try:
        # Load environment and initialize model
        conf = load_env(dry_run=False)  # Use real API key
        model = conf["model"]
        cost_tracker = CostTracker()
        safety_filter = SafetyFilter()
        
        # TEMPORARILY DISABLED FOR TESTING - Rate limiting for API calls
        # last_api_call_time = 0
        # MIN_API_INTERVAL = 2.0  # Minimum 2 seconds between API calls
        
        print("✅ AI Product Descriptions API started successfully")
        if model is not None:
            print(f"🤖 Model: {conf['model_name']} (Live mode)")
            print(f"🌡️  Temperature: {conf['temperature']}")
            print("✅ API key configured - ready for AI generation")
        else:
            print(f"🤖 Model: {conf['model_name']} (Dry-run mode)")
            print(f"🌡️  Temperature: {conf['temperature']}")
            print("⚠️  Running in dry-run mode - API key not configured")
        
    except Exception as e:
        print(f"❌ Failed to start API: {str(e)}")
        raise

# TEMPORARILY DISABLED FOR TESTING
def rate_limit_api_call():
    """Ensure minimum interval between API calls to avoid rate limiting"""
    # global last_api_call_time
    # current_time = time.time()
    # time_since_last_call = current_time - last_api_call_time
    # 
    # if time_since_last_call < MIN_API_INTERVAL:
    #     sleep_time = MIN_API_INTERVAL - time_since_last_call
    #     logging.info(f"Rate limiting: sleeping for {sleep_time:.2f} seconds")
    #     time.sleep(sleep_time)
    # 
    # last_api_call_time = time.time()
    pass

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "timestamp": timestamp()
    }


@app.get("/api/test-language/{language_code}")
async def test_language_generation(language_code: str):
    """Test endpoint to debug language generation issues"""
    if model is None:
        raise HTTPException(status_code=500, detail="AI model not initialized")
    
    # Validate language code
    SUPPORTED_LANGUAGES = ['en', 'es', 'fr', 'de', 'ja', 'zh']
    if language_code not in SUPPORTED_LANGUAGES:
        raise HTTPException(status_code=400, detail=f"Unsupported language code: {language_code}")
    
    try:
        # Create a simple test prompt
        language_names = {
            "en": "English",
            "es": "Spanish", 
            "fr": "French",
            "de": "German",
            "ja": "Japanese",
            "zh": "Chinese"
        }
        target_language = language_names.get(language_code, "English")
        
        test_prompt = f"""Write a simple product description in {target_language} for a wireless headphone.

Return JSON:
{{
  "title": "title in {target_language}",
  "description": "description in {target_language}",
  "bullets": ["benefit 1 in {target_language}", "benefit 2 in {target_language}", "benefit 3 in {target_language}"],
  "meta": "meta description in {target_language}"
}}"""
        
        logging.info(f"Testing language generation for: {language_code}")
        logging.info(f"Test prompt: {test_prompt}")
        
        # TEMPORARILY DISABLED FOR TESTING - rate_limit_api_call()  # Add rate limiting
        ai_text, tokens_used, response_time = call_gemini_generate(
            model=model,
            prompt=test_prompt,
            temperature=0.2,
            cost_tracker=cost_tracker
        )
        
        logging.info(f"AI response: {ai_text}")
        
        # Try to parse the response
        ai_text = safety_filter.sanitize_output(ai_text)
        parsed = safe_extract_json(ai_text)
        
        return {
            "success": True,
            "language_code": language_code,
            "target_language": target_language,
            "raw_response": ai_text,
            "parsed_response": parsed,
            "tokens_used": tokens_used,
            "response_time": response_time
        }
        
    except Exception as e:
        logging.error(f"Test generation failed for {language_code}: {str(e)}")
        return {
            "success": False,
            "language_code": language_code,
            "error": str(e),
            "error_type": type(e).__name__
        }

@app.post("/api/generate-description")
async def generate_description(
    title: str = Form(...),
    features: str = Form(...),
    category: str = Form("generic"),
    primary_keyword: str = Form(""),
    tone: str = Form("professional"),
    sku: str = Form(""),
    languageCode: str = Form("en")
):
    """Generate a single product description"""
    if model is None:
        raise HTTPException(status_code=500, detail="AI model not initialized")
    
    # Validate language code
    SUPPORTED_LANGUAGES = ['en', 'es', 'fr', 'de', 'ja', 'zh']
    if languageCode not in SUPPORTED_LANGUAGES:
        raise HTTPException(status_code=400, detail=f"Unsupported language code: {languageCode}")
    
    try:
        # Create row dict
        row = {
            "id": sku or timestamp(),
            "sku": sku,
            "title": title,
            "category": category,
            "features": features,
            "primary_keyword": primary_keyword,
            "tone": tone,
            "languageCode": languageCode
        }
        
        # Validate input
        is_valid, validation_msg = safety_filter.validate_input(title + " " + features)
        if not is_valid:
            raise HTTPException(status_code=400, detail=f"Invalid input: {validation_msg}")
        
        # Build prompt
        prompt = build_gemini_prompt(row)
        
        # Call AI
        ai_text, tokens_used, response_time = call_gemini_generate(
            model=model,
            prompt=prompt,
            temperature=0.2,
            cost_tracker=cost_tracker
        )
        
        # Sanitize output
        ai_text = safety_filter.sanitize_output(ai_text)
        
        # Parse response
        parsed = safe_extract_json(ai_text)
        
        # Extract fields
        generated_title = parsed.get("title", title)
        description = parsed.get("description", "").strip()
        bullets = parsed.get("bullets", [])
        meta = parsed.get("meta", "")
        
        # SEO evaluation
        seo = seo_evaluate(description, primary_keyword)
        
        return {
            "success": True,
            "data": {
                "id": row["id"],
                "sku": sku,
                "title": generated_title,
                "original_title": title,
                "description": description,
                "bullets": bullets,
                "meta": meta,
                "seo_score": seo,
                "languageCode": languageCode,
                "tokens_used": tokens_used,
                "response_time": response_time,
                "cost": cost_tracker.get_current_cost()
            }
        }
        
    except Exception as e:
        logging.error(f"Error generating description: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Generation failed: {str(e)}")

@app.post("/api/generate-batch")
async def generate_batch_json(request: Dict[str, Any]):
    """Generate descriptions for multiple products from batch request"""
    if model is None:
        raise HTTPException(status_code=500, detail="AI model not initialized")
    
    # Handle both old format (array of products) and new format (batch request)
    if isinstance(request, list):
        # Legacy format - array of products
        products = request
        batch_tone = "professional"
        batch_style = "amazon"
        language_code = "en"
    else:
        # New format - batch request with tone and style
        products = request.get("products", [])
        batch_tone = request.get("batchTone", "professional")
        batch_style = request.get("batchStyle", "amazon")
        language_code = request.get("languageCode", "en")
    
    # Validate language code
    SUPPORTED_LANGUAGES = ['en', 'es', 'fr', 'de', 'ja', 'zh']
    if language_code not in SUPPORTED_LANGUAGES:
        raise HTTPException(status_code=400, detail=f"Unsupported language code: {language_code}")
    
    try:
        results = []
        errors = []
        
        for idx, product in enumerate(products):
            try:
                # Convert to row dict format
                row_dict = {
                    "id": product.get("id", f"product_{idx}"),
                    "sku": product.get("sku", ""),
                    "title": product.get("product_name", ""),  # Frontend sends product_name
                    "category": product.get("category", "generic"),
                    "features": product.get("features", ""),
                    "primary_keyword": product.get("keywords", ""),  # Frontend sends keywords
                    "audience": product.get("audience", "general consumers"),  # Frontend sends audience
                    "tone": batch_tone,  # Use batch-level tone
                    "style_variation": batch_style,  # Use batch-level style
                    "languageCode": language_code  # Use batch-level language
                }
                
                # Basic validation for required fields
                if not row_dict["title"] or not row_dict["features"]:
                    errors.append({
                        "row": idx,
                        "id": row_dict.get("id", ""),
                        "error": "Missing required fields: product_name and features are required"
                    })
                    continue
                
                # Validate input
                is_valid, validation_msg = safety_filter.validate_input(
                    row_dict["title"] + " " + row_dict["features"]
                )
                if not is_valid:
                    errors.append({
                        "row": idx,
                        "id": row_dict.get("id", ""),
                        "error": f"Invalid input: {validation_msg}"
                    })
                    continue
                
                # Build prompt and generate
                prompt = build_gemini_prompt(row_dict)
                parsed = None
                tokens_used = 0
                response_time = 0
                
                try:
                    logging.info(f"Generating content for language: {language_code}")
                    # TEMPORARILY DISABLED FOR TESTING - rate_limit_api_call()  # Add rate limiting
                    ai_text, tokens_used, response_time = call_gemini_generate(
                        model=model,
                        prompt=prompt,
                        temperature=0.2,
                        cost_tracker=cost_tracker
                    )
                    
                    logging.info(f"AI response received: {ai_text[:200]}...")
                    
                    # Parse and process
                    ai_text = safety_filter.sanitize_output(ai_text)
                    parsed = safe_extract_json(ai_text)
                    
                    logging.info(f"Parsed JSON: {parsed}")
                    
                    # Validate that the generated content is in the requested language
                    if language_code != "en" and parsed.get("description", ""):
                        # Basic check: if description contains mostly English words, flag as potential issue
                        english_words = ["the", "and", "for", "with", "this", "that", "product", "quality", "features"]
                        description_lower = parsed.get("description", "").lower()
                        english_word_count = sum(1 for word in english_words if word in description_lower)
                        if english_word_count > 3:  # If more than 3 common English words, might be in English
                            logging.warning(f"Generated content for language {language_code} may contain English text")
                    
                except Exception as gen_error:
                    logging.error(f"Generation error for language {language_code}: {str(gen_error)}")
                    logging.error(f"Error type: {type(gen_error).__name__}")
                    
                    # Try a fallback with English if non-English fails
                    if language_code != "en":
                        logging.info(f"Attempting fallback to English for product: {row_dict.get('title', 'Unknown')}")
                        try:
                            # Create a simple English fallback
                            fallback_row = row_dict.copy()
                            fallback_row["languageCode"] = "en"
                            fallback_prompt = build_gemini_prompt(fallback_row)
                            
                            # TEMPORARILY DISABLED FOR TESTING - rate_limit_api_call()  # Add rate limiting
                            ai_text, tokens_used, response_time = call_gemini_generate(
                                model=model,
                                prompt=fallback_prompt,
                                temperature=0.2,
                                cost_tracker=cost_tracker
                            )
                            
                            ai_text = safety_filter.sanitize_output(ai_text)
                            parsed = safe_extract_json(ai_text)
                            
                            logging.info(f"Fallback to English successful")
                            
                        except Exception as fallback_error:
                            logging.error(f"Fallback to English also failed: {str(fallback_error)}")
                            
                            # Try one more time with an even simpler approach
                            try:
                                logging.info(f"Attempting ultra-simple English generation")
                                simple_prompt = f"""Create a product description for: {row_dict.get('title', 'Product')}

Features: {row_dict.get('features', '')}
Audience: {row_dict.get('audience', 'general consumers')}

Return JSON:
{{
  "title": "Product title",
  "description": "Product description",
  "bullets": ["Benefit 1", "Benefit 2", "Benefit 3"],
  "meta": "Meta description"
}}"""
                                
                                # TEMPORARILY DISABLED FOR TESTING - rate_limit_api_call()  # Add rate limiting
                                ai_text, tokens_used, response_time = call_gemini_generate(
                                    model=model,
                                    prompt=simple_prompt,
                                    temperature=0.2,
                                    cost_tracker=cost_tracker
                                )
                                
                                ai_text = safety_filter.sanitize_output(ai_text)
                                parsed = safe_extract_json(ai_text)
                                
                                logging.info(f"Ultra-simple English generation successful")
                                
                            except Exception as simple_error:
                                logging.error(f"Ultra-simple generation also failed: {str(simple_error)}")
                                errors.append({
                                    "row": idx,
                                    "id": row_dict.get("id", ""),
                                    "error": f"All generation attempts failed for language {language_code}: {str(gen_error)}"
                                })
                                continue
                    else:
                        errors.append({
                            "row": idx,
                            "id": row_dict.get("id", ""),
                            "error": f"Generation failed for language {language_code}: {str(gen_error)}"
                        })
                        continue
                
                result = {
                    "id": row_dict["id"],
                    "product_name": parsed.get("title", row_dict["title"]),
                    "category": row_dict["category"],
                    "audience": row_dict.get("audience", "general consumers"),
                    "description": parsed.get("description", ""),
                    "keywords": row_dict.get("primary_keyword", ""),
                    "features": row_dict["features"],  # Include original features
                    "tone": batch_tone,  # Include batch-level tone
                    "style_variation": batch_style,  # Include batch-level style variation
                    "languageCode": language_code,  # Include batch-level language
                    "bullets": parsed.get("bullets", []),
                    "meta": parsed.get("meta", ""),
                    "seo_score": seo_evaluate(parsed.get("description", ""), row_dict.get("primary_keyword", "")),
                    "tokens_used": tokens_used,
                    "response_time": response_time
                }
                
                results.append(result)
                
                # TEMPORARILY DISABLED FOR TESTING - Add delay between API calls to avoid rate limits
                # if idx < len(products) - 1:  # Don't delay after the last item
                #     import time
                #     time.sleep(2)
                
            except Exception as e:
                errors.append({
                    "row": idx,
                    "id": product.get("id", ""),
                    "error": str(e)
                })
        
        return {
            "success": True,
            "batch_id": f"batch_{timestamp()}",
            "items": results,
            "errors": errors,
            "total_processed": len(results),
            "total_errors": len(errors),
            "total_cost": cost_tracker.get_current_cost()
        }
        
    except Exception as e:
        logging.error(f"Error processing JSON batch: {str(e)}")
        raise HTTPException(status_code=500, detail=f"JSON batch processing failed: {str(e)}")

@app.post("/api/generate-batch-csv")
async def generate_batch(file: UploadFile = File(...), audience: str = Form(...), languageCode: str = Form("en")):
    """Generate descriptions for multiple products from CSV with automatic column mapping"""
    if model is None:
        raise HTTPException(status_code=500, detail="AI model not initialized")
    
    # Validate language code
    SUPPORTED_LANGUAGES = ['en', 'es', 'fr', 'de', 'ja', 'zh']
    if languageCode not in SUPPORTED_LANGUAGES:
        raise HTTPException(status_code=400, detail=f"Unsupported language code: {languageCode}")
    
    try:
        # Read CSV file
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))
        
        # Get column names for mapping
        columns = df.columns.tolist()
        
        results = []
        errors = []
        
        for idx, row in df.iterrows():
            try:
                # Use new automatic mapping function
                row_dict = process_csv_row(row, audience, columns, languageCode)
                
                # Validate input
                is_valid, validation_msg = safety_filter.validate_input(
                    row_dict["title"] + " " + row_dict["features"]
                )
                if not is_valid:
                    errors.append({
                        "row": idx,
                        "id": row_dict.get("id", ""),
                        "error": f"Invalid input: {validation_msg}"
                    })
                    continue
                
                # Build prompt and generate
                prompt = build_gemini_prompt(row_dict)
                ai_text, tokens_used, response_time = call_gemini_generate(
                    model=model,
                    prompt=prompt,
                    temperature=0.2,
                    cost_tracker=cost_tracker
                )
                
                # Parse and process
                ai_text = safety_filter.sanitize_output(ai_text)
                parsed = safe_extract_json(ai_text)
                
                result = {
                    "id": row_dict["id"],
                    "product_name": parsed.get("title", row_dict["title"]),
                    "category": row_dict["category"],
                    "audience": row_dict["audience"],
                    "description": parsed.get("description", ""),
                    "keywords": row_dict.get("primary_keyword", ""),
                    "features": row_dict["features"],  # Include original features
                    "tone": "professional",  # Default tone for CSV batch
                    "style_variation": "standard",  # Default style for CSV batch
                    "languageCode": languageCode,  # Include language from CSV batch
                    "bullets": parsed.get("bullets", []),
                    "meta": parsed.get("meta", ""),
                    "seo_score": seo_evaluate(parsed.get("description", ""), row_dict.get("primary_keyword", "")),
                    "tokens_used": tokens_used,
                    "response_time": response_time
                }
                
                results.append(result)
                
            except Exception as e:
                errors.append({
                    "row": idx,
                    "id": row_dict.get("id", ""),
                    "error": str(e)
                })
        
        return {
            "success": True,
            "batch_id": f"batch_{timestamp()}",
            "items": results,
            "errors": errors,
            "total_processed": len(results),
            "total_errors": len(errors),
            "total_cost": cost_tracker.get_current_cost()
        }
        
    except Exception as e:
        logging.error(f"Error processing batch: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Batch processing failed: {str(e)}")

@app.get("/api/usage-stats")
async def get_usage_stats():
    """Get current usage statistics"""
    if cost_tracker is None:
        raise HTTPException(status_code=500, detail="Cost tracker not initialized")
    
    return {
        "success": True,
        "data": cost_tracker.get_usage_stats()
    }

@app.get("/batch/{batch_id}")
async def fetch_batch(batch_id: str):
    """Fetch a batch by ID (placeholder - in real implementation, store in database)"""
    # This is a placeholder. In a real implementation, you'd store batches in a database
    # and retrieve them by ID. For now, return a 404.
    raise HTTPException(status_code=404, detail="Batch not found. This is a placeholder endpoint.")

@app.get("/download/{batch_id}")
async def download_batch(batch_id: str):
    """Download a batch as a CSV file"""
    # For now, we'll return a simple CSV with the batch ID
    # In a real implementation, you'd store and retrieve the actual batch data
    
    csv_content = f"""id,sku,title,description,bullets,meta,status
{batch_id},,Generated Product,This is a placeholder download for batch {batch_id}.,"Placeholder bullet 1|Placeholder bullet 2",Placeholder meta description,completed"""
    
    from fastapi.responses import Response
    
    return Response(
        content=csv_content,
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=batch_{batch_id}.csv"}
    )

@app.post("/api/regenerate")
async def regenerate_description(item: Dict[str, Any]):
    """Regenerate a single product description"""
    if model is None:
        raise HTTPException(status_code=500, detail="AI model not initialized")
    
    if safety_filter is None or cost_tracker is None:
        raise HTTPException(status_code=500, detail="AI components not initialized")
    
    try:
        # Convert the item to row dict format
        row_dict = {
            "id": item.get("id", timestamp()),
            "sku": item.get("sku", ""),
            "title": item.get("product_name", ""),
            "category": item.get("category", "generic"),
            "features": item.get("features", ""),
            "primary_keyword": item.get("keywords", ""),
            "audience": item.get("audience", "general consumers"),
            "tone": item.get("tone", "professional"),
            "style_variation": item.get("style_variation", "amazon"),
            "languageCode": item.get("languageCode", "en")
        }
        
        # Basic validation
        if not row_dict["title"] or not row_dict["features"]:
            raise HTTPException(status_code=400, detail="Missing required fields: product_name and features are required")
        
        # Validate input
        is_valid, validation_msg = safety_filter.validate_input(
            row_dict["title"] + " " + row_dict["features"]
        )
        if not is_valid:
            raise HTTPException(status_code=400, detail=f"Invalid input: {validation_msg}")
        
        # Build prompt and generate
        prompt = build_gemini_prompt(row_dict)
        ai_text, tokens_used, response_time = call_gemini_generate(
            model=model,
            prompt=prompt,
            temperature=0.2,
            cost_tracker=cost_tracker
        )
        
        # Parse and process
        ai_text = safety_filter.sanitize_output(ai_text)
        parsed = safe_extract_json(ai_text)
        
        result = {
            "id": row_dict["id"],
            "product_name": parsed.get("title", row_dict["title"]),
            "category": row_dict["category"],
            "audience": row_dict["audience"],
            "description": parsed.get("description", ""),
            "keywords": row_dict["primary_keyword"],
            "features": row_dict["features"],  # Include original features
            "tone": row_dict["tone"],  # Include original tone
            "style_variation": row_dict["style_variation"],  # Include original style variation
            "languageCode": row_dict["languageCode"],  # Include original language
            "bullets": parsed.get("bullets", []),
            "meta": parsed.get("meta", ""),
            "seo_score": seo_evaluate(parsed.get("description", ""), row_dict["primary_keyword"]),
            "tokens_used": tokens_used,
            "response_time": response_time,
            "regenerating": False
        }
        
        return result
        
    except Exception as e:
        logging.error(f"Error regenerating description: {str(e)}")
        logging.error(f"Item data: {item}")
        logging.error(f"Model status: {model is not None}")
        logging.error(f"Safety filter status: {safety_filter is not None}")
        logging.error(f"Cost tracker status: {cost_tracker is not None}")
        raise HTTPException(status_code=500, detail=f"Regeneration failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
