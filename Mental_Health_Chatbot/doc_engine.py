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

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)


def _load_documents() -> List[str]:
    """Load all .txt files from data/ directory"""
    base = pathlib.Path(__file__).parent / "data"
    docs: List[str] = []
    if not base.exists():
        return docs
    for path in sorted(base.glob("**/*.txt")):
        try:
            docs.append(path.read_text(encoding="utf-8"))
        except Exception:
            try:
                docs.append(path.read_text(encoding="latin-1"))
            except Exception:
                continue
    return docs


def query_documents(user_query: str) -> str:
    """Query documents using fuzzy matching and OpenAI for answer generation"""
    docs = _load_documents()
    if not docs:
        return "No documents found in data/. Please add .txt files to the data/ folder."

    # Build candidates from document lines
    candidates = []
    for d in docs:
        for line in d.splitlines():
            line = line.strip()
            if line:
                candidates.append(line)

    # Find close matches to user query
    matches = difflib.get_close_matches(user_query, candidates, n=3, cutoff=0.2)

    try:
        if matches:
            context = "\n\n".join(matches)
            messages = [
                {"role": "system", "content": "You are a helpful assistant. Use the following context from local documents to answer the user's question."},
                {"role": "system", "content": f"Context:\n{context}"},
                {"role": "user", "content": user_query},
            ]
        else:
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_query},
            ]

        # Call OpenAI API using modern client syntax
        resp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.2,
            max_tokens=512
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        error_msg = f"Error contacting OpenAI API for document query: {str(e)}"
        print(f"ERROR in query_documents: {error_msg}")
        return error_msg
