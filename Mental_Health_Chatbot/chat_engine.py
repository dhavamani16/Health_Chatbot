import os
from dotenv import load_dotenv
from typing import List, Dict, Any, Optional
import pathlib
import difflib
from openai import OpenAI
import json

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


def search_datasets(user_query: str) -> Optional[str]:
    """Search all datasets for relevant information about the query.
    
    Returns the matched dataset content or None if no match found.
    """
    base = pathlib.Path(__file__).parent / "data"
    if not base.exists():
        return None
    
    query_lower = user_query.lower()
    
    # Define keyword-to-dataset mapping for better matching
    keyword_map = {
        'stress': 'stress_management.txt',
        'anxiety': 'anxiety.txt',
        'panic': 'anxiety.txt',
        'worried': 'anxiety.txt',
        'afraid': 'anxiety.txt',
        'depress': 'depression.txt',  # Matches both "depression" and "depressed"
        'sad': 'depression.txt',
        'hopeless': 'depression.txt',
        'sleep': 'sleep.txt',
        'insomnia': 'sleep.txt',
        'tired': 'sleep.txt',
        'relax': 'stress_management.txt',
        'meditation': 'stress_management.txt',
        'exercise': 'stress_management.txt',
        'manage': 'stress_management.txt',
        'coping': 'stress_management.txt',
    }
    
    # Try to find a dataset match based on keywords in the query
    for keyword, dataset_file in keyword_map.items():
        if keyword in query_lower:
            try:
                content_path = base / dataset_file
                if content_path.exists():
                    content = content_path.read_text(encoding="utf-8")
                    
                    # Extract relevant section that contains the keyword or dataset-specific keyword
                    # For depression, search for both "depress" and "depression"
                    search_keywords = [keyword]
                    if keyword == 'depress':
                        search_keywords = ['depression', 'depress']
                    
                    sections = content.split('\n\n')
                    for section in sections:
                        section_lower = section.lower()
                        if any(sk in section_lower for sk in search_keywords) and len(section.strip()) > 50:
                            cleaned = section.strip().replace('\n', ' ')[:400]
                            dataset_name = dataset_file.replace('_', ' ').replace('.txt', '').title()
                            return f"[From {dataset_name}]\n\n{cleaned}"
            except Exception:
                continue
    
    return None


def get_response(session_id: str, user_query: str) -> str:
    """Generate a chat response with simple session memory stored on disk.

    This function:
    1. Loads previous messages for `session_id` from `sessions/`
    2. First tries to find relevant dataset content
    3. If dataset matches, returns that with context
    4. Otherwise calls OpenAI API as fallback
    5. Saves the assistant reply back to the session file
    """
    # System prompt tuned for warm, supportive responses
    system_prompt = (
        "You are a warm, empathetic mental-health support assistant. "
        "Respond in a safe, supportive, simple, and understanding tone. "
        "Do NOT provide a medical diagnosis. Encourage positive steps and listening."
    )

    sessions_dir = pathlib.Path(__file__).parent / "sessions"
    sessions_dir.mkdir(exist_ok=True)
    session_file = sessions_dir / f"{session_id}.json"

    # Load existing messages or start with the system prompt
    messages: List[Dict[str, Any]] = []
    if session_file.exists():
        try:
            messages = json.loads(session_file.read_text(encoding="utf-8"))
        except Exception:
            messages = []

    if not messages:
        messages = [{"role": "system", "content": system_prompt}]

    # Append user message
    messages.append({"role": "user", "content": user_query})

    # Try to find dataset match first
    dataset_response = search_datasets(user_query)
    if dataset_response:
        print(f"INFO: Dataset match found for query: {user_query[:40]}...")
        # Append and save the dataset-based response
        messages.append({"role": "assistant", "content": dataset_response})
        try:
            session_file.write_text(json.dumps(messages, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception as e:
            print(f"Warning: could not save session file {session_file}: {e}")
        return dataset_response

    # Fallback to OpenAI API
    try:
        resp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.5,
            max_tokens=450
        )

        assistant_text = resp.choices[0].message.content.strip()

        # Append assistant reply and save session
        messages.append({"role": "assistant", "content": assistant_text})
        try:
            session_file.write_text(json.dumps(messages, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception as e:
            print(f"Warning: could not save session file {session_file}: {e}")

        return assistant_text

    except Exception as e:
        err = f"Error contacting OpenAI API for chat: {str(e)}"
        print(f"ERROR in get_response: {err}")
        return err