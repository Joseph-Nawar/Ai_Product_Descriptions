# backend/src/prompt_templates.py
import sys
from pathlib import Path

# Add backend directory to path for imports
THIS_DIR = Path(__file__).resolve().parent
BACKEND_DIR = THIS_DIR.parent
sys.path.insert(0, str(BACKEND_DIR))

from utils.helpers import read_text

TEMPLATES_DIR = Path(__file__).resolve().parents[1] / "models" / "prompt_templates"

def load_template(category):
    category = (category or "generic").lower()
    fpath = TEMPLATES_DIR / f"{category}.md"
    if not fpath.exists():
        # fallback to homegoods
        fpath = TEMPLATES_DIR / "homegoods.md"
    return read_text(fpath)

def build_prompt_from_row(row):
    """
    row: dict-like with keys: title, features, primary_keyword, tone
    features string is semicolon-separated
    """
    tpl = load_template(row.get("category", "").lower())
    features_list = row.get("features", "")
    features_formatted = "\n".join([f"- {x.strip()}" for x in features_list.split(";") if x.strip()])
    mapping = {
        "title": row.get("title","").strip(),
        "features_list": features_formatted,
        "primary_keyword": row.get("primary_keyword","").strip(),
        "tone": row.get("tone","").strip() or "professional"
    }
    # use Python format (templates use {title}, etc.)
    try:
        prompt = tpl.format(**mapping)
    except Exception:
        # naive replace as final fallback
        prompt = tpl.replace("{title}", mapping["title"])\
                    .replace("{features_list}", mapping["features_list"])\
                    .replace("{primary_keyword}", mapping["primary_keyword"])\
                    .replace("{tone}", mapping["tone"])
    return prompt
