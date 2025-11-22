#!/usr/bin/env python
"""Test script to verify dataset searching works in chat_engine.py"""

import sys
import os

# Add the project root to path
sys.path.insert(0, os.path.dirname(__file__))

print("=" * 70)
print("DATASET SEARCH TEST - Chat Engine")
print("=" * 70)

# Test 1: Check if datasets exist
print("\n[TEST 1] Checking if dataset files exist...")
from pathlib import Path
data_dir = Path(__file__).parent / "data"
dataset_files = ['stress_management.txt', 'depression.txt', 'anxiety.txt', 'sleep.txt']

for filename in dataset_files:
    filepath = data_dir / filename
    if filepath.exists():
        size = filepath.stat().st_size
        print(f"✓ {filename}: {size} bytes")
    else:
        print(f"✗ {filename}: NOT FOUND")

# Test 2: Test search_datasets function
print("\n[TEST 2] Testing search_datasets() function...")
try:
    from chat_engine import search_datasets
    print("✓ Successfully imported search_datasets from chat_engine")
    
    # Test queries
    test_queries = [
        "I'm feeling stressed",
        "I have anxiety",
        "I'm depressed",
        "I can't sleep",
        "hello world"
    ]
    
    for query in test_queries:
        result = search_datasets(query)
        if result:
            print(f"\n✓ Query: '{query}'")
            print(f"  Match found: {result[:100]}...")
        else:
            print(f"\n✗ Query: '{query}' - No dataset match")
            
except Exception as e:
    print(f"✗ Error testing search_datasets: {e}")
    import traceback
    traceback.print_exc()

# Test 3: Test get_response function
print("\n[TEST 3] Testing get_response() with datasets...")
try:
    from chat_engine import get_response
    print("✓ Successfully imported get_response from chat_engine")
    
    # Test a simple query (won't call OpenAI if dataset matches)
    test_session = "test_dataset_search"
    test_query = "I'm feeling anxious and need help"
    
    response = get_response(test_session, test_query)
    print(f"\nQuery: '{test_query}'")
    print(f"Response preview: {response[:200]}...")
    
    if "[From" in response:
        print("✓ Response includes dataset label - dataset search is working!")
    elif "Error" in response:
        print("⚠ Response contains error - this might be an API issue")
    else:
        print("? Response is generic - dataset search may not have matched")
        
except Exception as e:
    print(f"✗ Error testing get_response: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 70)
print("TEST COMPLETE")
print("=" * 70)
print("\nNext steps:")
print("1. If all tests passed, the backend will now use datasets!")
print("2. Start the server: python -m uvicorn main:app --reload")
print("3. Test with /chat endpoint - it should return dataset content")
print("4. Try queries like: 'depression', 'anxiety', 'stress', 'sleep'")
print("\n" + "=" * 70)
