import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")
llm = OpenAI(openai_api_key=OPENAI_API_KEY,temperature=0.7)

session_memory_map={}

def get_response(session_id: str, query: str) -> str:
    if session_id not in session_memory_map:
        memory = ConversationBufferMemory(memory_key="chat_history")
        conversation_chain = ConversationChain(llm=llm, memory=memory)
        session_memory_map[session_id] = conversation_chain
    else:
        conversation_chain = session_memory_map[session_id]
    
    response = conversation_chain.run(input=query)
    return response