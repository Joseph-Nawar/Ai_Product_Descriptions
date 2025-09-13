# backend/src/seo_check.py
import re

def seo_evaluate(text, primary_keyword, min_words=60, max_words=140):
    txt = (text or "").lower()
    kw = (primary_keyword or "").lower().strip()
    words = len(re.findall(r"\w+", text or ""))
    keyword_count = txt.count(kw) if kw else 0
    passes = True
    notes = []

    if kw and keyword_count < 1:
        passes = False
        notes.append("primary keyword missing")
    if words < min_words:
        passes = False
        notes.append(f"too short ({words} words) - target {min_words}-{max_words}")
    if words > max_words:
        # not failing, but note
        notes.append(f"long ({words} words)")

    return {
        "keyword_count": keyword_count,
        "length_words": words,
        "passes": passes,
        "notes": "; ".join(notes)
    }
