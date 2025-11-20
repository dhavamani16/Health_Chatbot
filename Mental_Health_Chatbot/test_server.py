#!/usr/bin/env python
"""Quick test script to verify server can start and basic functionality works"""

import sys
import os

print("=" * 60)
print("MENTAL HEALTH CHATBOT - SERVER TEST")
print("=" * 60)

# Test 1: Check .env file
print("\n[TEST 1] Checking .env file...")
if os.path.exists(".env"):
    print("✓ .env file exists")
    try:
        from dotenv import load_dotenv
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            print(f"✓ OPENAI_API_KEY found: {api_key[:10]}...")
        else:
            print("✗ OPENAI_API_KEY is empty in .env")
    except Exception as e:
        print(f"✗ Error loading .env: {e}")
else:
    print("✗ .env file NOT found in current directory")
    print("  Create it with: echo OPENAI_API_KEY=sk-... > .env")

# Test 2: Check Python imports
print("\n[TEST 2] Checking Python imports...")
imports_ok = True
try:
    import openai
    print("✓ openai module imported")
except ImportError as e:
    print(f"✗ openai import failed: {e}")
    imports_ok = False

try:
    import fastapi
    print("✓ fastapi module imported")
except ImportError as e:
    print(f"✗ fastapi import failed: {e}")
    imports_ok = False

try:
    import uvicorn
    print("✓ uvicorn module imported")
except ImportError as e:
    print(f"✗ uvicorn import failed: {e}")
    imports_ok = False

try:
    from dotenv import load_dotenv
    print("✓ dotenv module imported")
except ImportError as e:
    print(f"✗ dotenv import failed: {e}")
    imports_ok = False

# Test 3: Check local modules
print("\n[TEST 3] Checking local Python modules...")
try:
    from models import ChatRequest
    print("✓ models.ChatRequest imported")
except Exception as e:
    print(f"✗ models import failed: {e}")
    imports_ok = False

try:
    from chat_engine import get_response
    print("✓ chat_engine.get_response imported")
except Exception as e:
    print(f"✗ chat_engine import failed: {e}")
    imports_ok = False

try:
    from crisis import contains_crisis_keywords
    print("✓ crisis.contains_crisis_keywords imported")
except Exception as e:
    print(f"✗ crisis import failed: {e}")
    imports_ok = False

try:
    from loger import log_chat
    print("✓ loger.log_chat imported")
except Exception as e:
    print(f"✗ loger import failed: {e}")
    imports_ok = False

try:
    from doc_engine import query_documents
    print("✓ doc_engine.query_documents imported")
except Exception as e:
    print(f"✗ doc_engine import failed: {e}")
    imports_ok = False

# Test 4: Try to import main.app
print("\n[TEST 4] Checking FastAPI app...")
try:
    from main import app
    print("✓ main.app (FastAPI) imported successfully!")
except Exception as e:
    print(f"✗ main.app import failed: {e}")
    import traceback
    traceback.print_exc()
    imports_ok = False

# Summary
print("\n" + "=" * 60)
if imports_ok:
    print("✓ ALL TESTS PASSED - Server should start!")
    print("\nRun the server with:")
    print("  C:\\Users\\kala_\\anaconda3\\python.exe -m uvicorn main:app --reload --host 127.0.0.1 --port 8000")
else:
    print("✗ SOME TESTS FAILED - Fix errors above before running server")
print("=" * 60)
