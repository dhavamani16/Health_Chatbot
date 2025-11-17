import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment (.env)")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Simple in-memory session conversation store
# Each session stores a list of messages in OpenAI Chat format
session_memory_map = {}

SYSTEM_PROMPT = (
    "You are a compassionate, empathetic mental health support assistant. "
    "Provide supportive, non-judgmental replies and, when appropriate, encourage seeking professional help. "
    "Keep responses concise and clear."
)

def _ensure_session(session_id: str) -> None:
    """Initialize session if it doesn't exist"""
    if session_id not in session_memory_map:
        session_memory_map[session_id] = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]

def get_response(session_id: str, user_query: str) -> str:
    """
    Get a reply from OpenAI ChatCompletion API using session memory.
    Stores conversation history in memory (process-local).
    """
    _ensure_session(session_id)
    
    # Append user message to session history
    session_memory_map[session_id].append({
        "role": "user",
        "content": user_query
    })
    
    try:
        # Call OpenAI API using modern client syntax
        resp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=session_memory_map[session_id],
            temperature=0.7,
            max_tokens=512,
        )
        assistant_msg = resp.choices[0].message.content.strip()
    except Exception as e:
        error_msg = f"Error contacting OpenAI API: {str(e)}"
        print(f"ERROR in get_response: {error_msg}")
        return error_msg
    
    # Append assistant reply to session history
    session_memory_map[session_id].append({
        "role": "assistant",
        "content": assistant_msg
    })
    
    return assistant_msg
