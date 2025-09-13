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
    Try to extract JSON object from model output.
    Tries codeblocks first, then first {...} block.
    Returns Python object or raises ValueError.
    """
    if not text or not isinstance(text, str):
        raise ValueError("No text to parse")

    # codeblock JSON: ```json { ... } ```
    codeblock = re.search(r"```(?:json)?\s*({.*?})\s*```", text, re.S)
    if codeblock:
        payload = codeblock.group(1)
        return json.loads(payload)

    # fallback: first { ... } balanced braces (greedy)
    # Find first { and last } and attempt parse
    first = text.find("{")
    last = text.rfind("}")
    if first != -1 and last != -1 and last > first:
        payload = text[first:last+1]
        try:
            return json.loads(payload)
        except json.JSONDecodeError:
            # try to clean trailing commas
            cleaned = re.sub(r",\s*}", "}", payload)
            cleaned = re.sub(r",\s*\]", "]", cleaned)
            return json.loads(cleaned)
    raise ValueError("Could not extract JSON from text")

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
