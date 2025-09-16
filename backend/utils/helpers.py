# backend/utils/helpers.py
import os
import json
import re
from pathlib import Path
from datetime import datetime

def ensure_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)
    return Path(path)

def timestamp():
    return datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

def safe_extract_json(text):
    """
    Enhanced JSON extraction with robust fallback mechanisms and AI-powered repair.
    Tries multiple strategies to extract valid JSON from AI responses.
    """
    if not text or not isinstance(text, str):
        raise ValueError("No text to parse")

    # Strategy 1: Look for codeblock JSON: ```json { ... } ```
    codeblock = re.search(r"```(?:json)?\s*({.*?})\s*```", text, re.S)
    if codeblock:
        payload = codeblock.group(1)
        try:
            parsed = json.loads(payload)
            return validate_product_json(parsed)
        except json.JSONDecodeError as e:
            # Try to repair the JSON
            repaired = repair_json(payload)
            if repaired:
                return validate_product_json(repaired)

    # Strategy 2: Find first { ... } balanced braces
    first = text.find("{")
    last = text.rfind("}")
    if first != -1 and last != -1 and last > first:
        payload = text[first:last+1]
        try:
            parsed = json.loads(payload)
            return validate_product_json(parsed)
        except json.JSONDecodeError:
            # Try to repair the JSON
            repaired = repair_json(payload)
            if repaired:
                return validate_product_json(repaired)

    # Strategy 3: Look for any JSON-like structure in the text
    json_patterns = [
        r'\{[^{}]*"title"[^{}]*"description"[^{}]*"bullets"[^{}]*\}',
        r'\{[^{}]*"bullets"[^{}]*"title"[^{}]*"description"[^{}]*\}',
        r'\{[^{}]*"description"[^{}]*"title"[^{}]*"bullets"[^{}]*\}'
    ]
    
    for pattern in json_patterns:
        matches = re.findall(pattern, text, re.S)
        for match in matches:
            try:
                parsed = json.loads(match)
                return validate_product_json(parsed)
            except json.JSONDecodeError:
                repaired = repair_json(match)
                if repaired:
                    return validate_product_json(repaired)

    # Strategy 4: Extract structured data using regex patterns
    structured_data = extract_structured_data(text)
    if structured_data:
        return validate_product_json(structured_data)

    raise ValueError("Could not extract valid JSON from text")

def repair_json(json_str):
    """
    Attempt to repair common JSON issues using regex patterns.
    """
    try:
        # Remove trailing commas
        repaired = re.sub(r",\s*}", "}", json_str)
        repaired = re.sub(r",\s*\]", "]", repaired)
        repaired = re.sub(r",\s*$", "", repaired)
        
        # Fix unescaped quotes in strings
        repaired = re.sub(r'(?<!\\)"(?![,}\]:\s])', '\\"', repaired)
        
        # Try to parse the repaired JSON
        return json.loads(repaired)
    except json.JSONDecodeError:
        return None

def extract_structured_data(text):
    """
    Extract structured data using regex patterns when JSON parsing fails.
    """
    try:
        # Extract title
        title_match = re.search(r'"title"\s*:\s*"([^"]+)"', text)
        title = title_match.group(1) if title_match else ""
        
        # Extract description
        desc_match = re.search(r'"description"\s*:\s*"([^"]+)"', text)
        description = desc_match.group(1) if desc_match else ""
        
        # Extract bullets
        bullets_match = re.search(r'"bullets"\s*:\s*\[(.*?)\]', text, re.S)
        bullets = []
        if bullets_match:
            bullets_text = bullets_match.group(1)
            # Extract individual bullet points
            bullet_items = re.findall(r'"([^"]+)"', bullets_text)
            bullets = bullet_items
        
        # Extract meta
        meta_match = re.search(r'"meta"\s*:\s*"([^"]+)"', text)
        meta = meta_match.group(1) if meta_match else ""
        
        # If we have at least title and description, return structured data
        if title and description:
            return {
                "title": title,
                "description": description,
                "bullets": bullets,
                "meta": meta
            }
    except Exception:
        pass
    
    return None

def validate_and_ensure_compliance(parsed_data, max_retries=2):
    """
    Validation gate that ensures bullet points compliance.
    Returns validated data or raises ValueError with specific compliance failure details.
    """
    try:
        validated = validate_product_json(parsed_data)
        return validated
    except ValueError as e:
        error_msg = str(e)
        if "BULLET POINTS COMPLIANCE FAILURE" in error_msg or "EXACTLY 3 bullet points are required" in error_msg:
            raise ValueError(f"COMPLIANCE VALIDATION FAILED: {error_msg}")
        else:
            raise ValueError(f"VALIDATION ERROR: {error_msg}")

def generate_fallback_bullets(title, description, features):
    """
    Generate fallback bullet points when AI fails to provide them.
    Focus on product features and specifications rather than abstract benefits.
    """
    bullets = []
    
    # Extract features from the input
    feature_list = [f.strip() for f in features.split(";") if f.strip()]
    
    # Generate 3 fallback bullets based on actual features
    if len(feature_list) >= 3:
        bullets = [
            f"{feature_list[0]} - provides reliable performance and durability",
            f"{feature_list[1]} - ensures optimal functionality and user experience", 
            f"{feature_list[2]} - delivers consistent results and long-lasting quality"
        ]
    elif len(feature_list) >= 2:
        bullets = [
            f"{feature_list[0]} - offers superior performance and reliability",
            f"{feature_list[1]} - provides enhanced functionality and efficiency",
            f"Professional-grade construction - built for durability and long-term use"
        ]
    elif len(feature_list) >= 1:
        bullets = [
            f"{feature_list[0]} - delivers reliable performance and quality",
            f"Advanced design features - optimized for functionality and efficiency",
            f"High-quality materials - ensures durability and professional results"
        ]
    else:
        bullets = [
            "High-quality materials - ensures durability and professional performance",
            "Advanced design features - optimized for functionality and efficiency", 
            "Professional construction - built for reliability and long-term use"
        ]
    
    return bullets[:3]  # Ensure exactly 3 bullets

def validate_product_json(data):
    """
    Validate and normalize the product description JSON structure.
    Ensures all required fields are present and properly formatted.
    Enforces strict compliance with bullet point requirements.
    """
    if not isinstance(data, dict):
        raise ValueError("JSON must be an object")
    
    # Required fields with defaults
    validated = {
        "title": data.get("title", "").strip(),
        "description": data.get("description", "").strip(),
        "bullets": data.get("bullets", []),
        "meta": data.get("meta", "").strip()
    }
    
    # Ensure bullets is a list
    if not isinstance(validated["bullets"], list):
        validated["bullets"] = []
    
    # Clean and validate bullets - STRICT REQUIREMENT
    validated["bullets"] = [str(bullet).strip() for bullet in validated["bullets"] if bullet and str(bullet).strip()]
    
    # Ensure minimum content quality
    if not validated["title"]:
        raise ValueError("Title is required and cannot be empty")
    
    if not validated["description"]:
        raise ValueError("Description is required and cannot be empty")
    
    # STRICT BULLET POINT VALIDATION - MUST HAVE EXACTLY 3
    if len(validated["bullets"]) < 3:
        raise ValueError(f"EXACTLY 3 bullet points are required. Found {len(validated['bullets'])}. This violates the STRUCTURE REQUIREMENTS.")
    
    # If more than 3 bullets, take only the first 3
    if len(validated["bullets"]) > 3:
        validated["bullets"] = validated["bullets"][:3]
    
    # Ensure each bullet point is meaningful (at least 10 characters)
    validated["bullets"] = [bullet for bullet in validated["bullets"] if len(bullet) >= 10]
    
    # If we still don't have 3 bullets after filtering, this is an error
    if len(validated["bullets"]) < 3:
        raise ValueError(f"BULLET POINTS COMPLIANCE FAILURE: Need exactly 3 meaningful bullet points. Found {len(validated['bullets'])} after validation.")
    
    # Truncate meta description if too long
    if len(validated["meta"]) > 160:
        validated["meta"] = validated["meta"][:157] + "..."
    
    return validated

def write_ndjson(path, records):
    path = Path(path)
    ensure_dir(path.parent)
    with open(path, "w", encoding="utf-8") as fh:
        for r in records:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

def write_json(path, obj):
    ensure_dir(Path(path).parent)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)

def read_text(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()
