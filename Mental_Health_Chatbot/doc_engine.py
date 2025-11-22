import os
from dotenv import load_dotenv
from typing import List
import pathlib
import difflib
from openai import OpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment (.env)")

client = OpenAI(api_key=OPENAI_API_KEY)


def _load_documents() -> List[str]:
    base = pathlib.Path(__file__).parent / "data"
    docs: List[str] = []
    if not base.exists():
        return docs
    for path in sorted(base.glob("**/*.txt")):
        try:
            docs.append(path.read_text(encoding="utf-8"))
        except Exception:
            continue
    return docs


def query_documents(user_query: str) -> str:
    docs = _load_documents()

    # build text lines for fuzzy search
    candidates = []
    for d in docs:
        for line in d.splitlines():
            line = line.strip()
            if line:
                candidates.append(line)

    matches = difflib.get_close_matches(user_query, candidates, n=3, cutoff=0.2)

    # --- SYSTEM PROMPT (mental health support style) ---
    system_prompt = (
        "You are a warm, empathetic mental-health support assistant. "
        "Respond in a safe, supportive, simple, and understanding tone. "
        "Do NOT give medical diagnosis. Encourage positive steps and listening. "
        "If context is provided, use it to help the user."
    )

    try:
        if matches:
            context = "\n".join(matches)
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "system", "content": f"Context:\n{context}"},
                {"role": "user", "content": user_query},
            ]
        else:
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query},
            ]

        resp = client.chat.completions.create(
            model="gpt-4o-mini",   # ⭐ Recommended Model
            messages=messages,
            temperature=0.4,
            max_tokens=500
        )
        return resp.choices[0].message.content.strip()

    except Exception as e:
        return f"Error contacting OpenAI API: {str(e)}"
