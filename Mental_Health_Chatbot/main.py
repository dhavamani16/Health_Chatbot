import os
import traceback
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from models import ChatRequest
from chat_engine import get_response
from crisis import contains_crisis_keywords, SAFETY_MESSAGE
from loger import log_chat
from doc_engine import query_documents

load_dotenv()

app = FastAPI()

# Enable CORS for all origins (for development/testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    """Root endpoint - returns welcome message"""
    return {"message": "Welcome to the Mental Health Support Chatbot"}

@app.post("/chat")
def chat_with_memory(request: ChatRequest):
    """
    Handle chat requests with session memory.
    
    Expected request body:
    {
        "session_id": "user123",
        "query": "I am feeling sad"
    }
    """
    try:
        session_id = str(request.session_id).strip()
        user_query = str(request.query).strip()
        
        if not session_id or not user_query:
            return {"response": "Error: session_id and query are required"}

        # Check for crisis keywords
        if contains_crisis_keywords(user_query):
            try:
                log_chat(session_id, user_query, SAFETY_MESSAGE, is_crisis=True)
            except Exception as log_err:
                print(f"Warning: Could not log crisis: {log_err}")
            return {"response": SAFETY_MESSAGE}

        # Get response from chatbot
        response = get_response(session_id, user_query)
        if not response:
            response = "Sorry, I couldn't generate a response. Please try again."
        
        try:
            log_chat(session_id, user_query, response, is_crisis=False)
        except Exception as log_err:
            print(f"Warning: Could not log chat: {log_err}")
        
        return {"response": response}
        
    except Exception as e:
        print(f"ERROR in /chat endpoint: {str(e)}")
        traceback.print_exc()
        return {"response": f"Server error: {str(e)}"}

@app.post("/doc-chat")
def chat_with_documents(request: ChatRequest):
    """
    Handle document-based chat requests.
    
    Expected request body:
    {
        "session_id": "user123",
        "query": "Tell me about depression"
    }
    """
    try:
        user_query = str(request.query).strip()
        if not user_query:
            return {"response": "Error: query is required"}
        
        response = query_documents(user_query)
        return {"response": response}
    except Exception as e:
        print(f"ERROR in /doc-chat endpoint: {str(e)}")
        traceback.print_exc()
        return {"response": f"Server error: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
