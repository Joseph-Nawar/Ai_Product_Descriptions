# backend/src/main.py
import os
import sys
import logging
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

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "timestamp": timestamp()
    }


@app.post("/api/generate-description")
async def generate_description(
    title: str = Form(...),
    features: str = Form(...),
    category: str = Form("generic"),
    primary_keyword: str = Form(""),
    tone: str = Form("professional"),
    sku: str = Form("")
):
    """Generate a single product description"""
    if model is None:
        raise HTTPException(status_code=500, detail="AI model not initialized")
    
    try:
        # Create row dict
        row = {
            "id": sku or timestamp(),
            "sku": sku,
            "title": title,
            "category": category,
            "features": features,
            "primary_keyword": primary_keyword,
            "tone": tone
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
    else:
        # New format - batch request with tone and style
        products = request.get("products", [])
        batch_tone = request.get("batchTone", "professional")
        batch_style = request.get("batchStyle", "amazon")
    
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
                    "style_variation": batch_style  # Use batch-level style
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
                    "audience": row_dict.get("audience", "general consumers"),
                    "description": parsed.get("description", ""),
                    "keywords": row_dict.get("primary_keyword", ""),
                    "features": row_dict["features"],  # Include original features
                    "tone": batch_tone,  # Include batch-level tone
                    "style_variation": batch_style,  # Include batch-level style variation
                    "bullets": parsed.get("bullets", []),
                    "meta": parsed.get("meta", ""),
                    "seo_score": seo_evaluate(parsed.get("description", ""), row_dict.get("primary_keyword", "")),
                    "tokens_used": tokens_used,
                    "response_time": response_time
                }
                
                results.append(result)
                
                # Add delay between API calls to avoid rate limits
                if idx < len(products) - 1:  # Don't delay after the last item
                    import time
                    time.sleep(2)
                
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
async def generate_batch(file: UploadFile = File(...)):
    """Generate descriptions for multiple products from CSV"""
    if model is None:
        raise HTTPException(status_code=500, detail="AI model not initialized")
    
    try:
        # Read CSV file
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))
        
        results = []
        errors = []
        
        for idx, row in df.iterrows():
            try:
                row_dict = row_to_dict(row)
                
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
                    "audience": row_dict.get("audience", "general consumers"),
                    "description": parsed.get("description", ""),
                    "keywords": row_dict.get("primary_keyword", ""),
                    "features": row_dict["features"],  # Include original features
                    "tone": batch_tone,  # Include batch-level tone
                    "style_variation": batch_style,  # Include batch-level style variation
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
            "style_variation": item.get("style_variation", "amazon")
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
