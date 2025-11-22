# Mental Health Chatbot - Dataset Integration Complete ✓

## Summary

Your chatbot now **properly answers questions from datasets**! Both the frontend (browser) and backend (API) have been updated to:

1. **Load all datasets** from the `data/` folder on startup
2. **Search datasets first** before calling the OpenAI API
3. **Return dataset content** with a clear `[From Dataset Name]` label
4. **Fall back to OpenAI** only if no dataset match is found

---

## How It Works

### Frontend (Browser Chat)

When you ask a question in the browser chat:

1. **Load phase** (on page load):
   - `loadAllDatasets()` fetches all `.txt` files from `data/`
   - Check browser console (F12) to see: `✓ Loaded dataset: anxiety`

2. **Chat phase** (when you send a message):
   - `getResponse()` is called with your message
   - `searchDatasets()` looks for keyword matches
   - If found → Returns dataset content with label
   - If not found → Uses demo responses

3. **Example**:
   ```
   User: "I'm feeling anxious"
   System: Searches for keyword "anxiety"
   Result: [From Anxiety]
           1. What is Anxiety? Anxiety is your body's natural response...
   ```

### Backend (API `/chat` endpoint)

When you call the API with a query:

1. **Search phase**:
   - `search_datasets()` checks if query contains keywords
   - Looks for matching dataset files
   - Extracts first relevant section

2. **Return phase**:
   - If dataset matches → Returns with `[From Dataset Name]`
   - If no match → Calls OpenAI API (or returns error if quota exceeded)

3. **Session memory**:
   - Saves all messages to `sessions/{session_id}.json`
   - Maintains conversation history for future queries

---

## Dataset Files & Keywords

### Available Datasets

| Dataset | File | Keywords |
|---------|------|----------|
| **Stress Management** | `stress_management.txt` | stress, relax, meditation, exercise, manage, coping |
| **Anxiety** | `anxiety.txt` | anxiety, panic, worried, afraid |
| **Depression** | `depression.txt` | depress, depressed, sad, hopeless |
| **Sleep** | `sleep.txt` | sleep, insomnia, tired |

### Testing Keywords

```
"I'm feeling stressed"      → [From Stress Management]
"I have anxiety"           → [From Anxiety]
"I am depressed"           → [From Depression]
"I can't sleep"            → [From Sleep]
"help with panic attacks"  → [From Anxiety]
"feeling sad"              → [From Depression]
```

---

## How to Run & Test

### Option 1: Frontend (Browser Chat)

1. **Serve the files** (from project root):
   ```powershell
   cd "C:\Users\kala_\Downloads\Mental_Health_Chatbot\chatbot-ui"
   python -m http.server 8001
   ```

2. **Open in browser**:
   ```
   http://127.0.0.1:8001/index.html
   ```

3. **Test with dataset questions**:
   - Click "Chat with Us"
   - Type: "I'm feeling stressed"
   - Expected: Response from stress_management.txt with `[From Stress Management]` label

4. **Check console logs** (F12 → Console):
   ```
   ✓ Loaded dataset: stress_management
   ✓ Loaded dataset: anxiety
   ✓ Loaded dataset: depression
   ✓ Loaded dataset: sleep
   Dataset matched for: I'm feeling stressed...
   ```

### Option 2: Backend (API)

1. **Start the server**:
   ```powershell
   cd "C:\Users\kala_\Downloads\Mental_Health_Chatbot"
   python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
   ```

2. **Test with dataset query**:
   ```powershell
   $body = @{ session_id = "user1"; query = "I'm anxious" } | ConvertTo-Json
   curl http://127.0.0.1:8000/chat -Method POST -H "Content-Type: application/json" -Body $body
   ```

3. **Expected response**:
   ```json
   {
     "response": "[From Anxiety]\n\n1. What is Anxiety? Anxiety is your body's natural response to stress or fear..."
   }
   ```

4. **Check server logs**:
   ```
   INFO: Dataset match found for query: I'm anxious...
   ```

### Option 3: Quick Test Script

```powershell
cd "C:\Users\kala_\Downloads\Mental_Health_Chatbot"
python test_datasets.py
```

This runs all tests and shows which datasets are loaded and searchable.

---

## Adding Custom Datasets

### Step 1: Create a Dataset File

Create a new `.txt` file in `data/` folder:

```
c:\Users\kala_\Downloads\Mental_Health_Chatbot\data\my_topic.txt
```

### Step 2: Add Content

```
MY TOPIC GUIDE

## What is My Topic?
Description here...

## Key Points
• Point 1
• Point 2
• Point 3

## How to Help Yourself
- Tip 1
- Tip 2
```

### Step 3: Add Keywords to Code

#### For Backend (Python)

Edit `chat_engine.py`, update the `keyword_map` dictionary:

```python
keyword_map = {
    # ... existing keywords ...
    'mytopic': 'my_topic.txt',
    'keyword1': 'my_topic.txt',
    'keyword2': 'my_topic.txt',
}
```

#### For Frontend (JavaScript)

Edit `chatbot-ui/chatbot.js`, update the `keywordMap` object:

```javascript
const keywordMap = {
    // ... existing keywords ...
    'mytopic': ['my_topic'],
    'keyword1': ['my_topic'],
    'keyword2': ['my_topic'],
};
```

### Step 4: Reload & Test

- **Frontend**: Reload page (Ctrl+F5)
- **Backend**: Restart server
- **Test**: Ask a question with your keyword

Example:
```
User: "I need help with my topic"
Bot: [From My Topic] ...content from my_topic.txt...
```

---

## Example: Adding a Motivation Dataset

### Create `data/motivation.txt`:

```
MOTIVATION AND CONFIDENCE GUIDE

## Why Motivation Matters
Motivation is the driving force that helps you achieve your goals 
and overcome challenges. It comes from within and can be strengthened.

## Building Self-Confidence
• Set achievable goals and celebrate small wins
• Practice positive self-talk
• Challenge negative thoughts with facts
• Surround yourself with supportive people
• Learn from failures instead of fearing them

## Staying Motivated During Tough Times
• Break goals into smaller, manageable steps
• Remind yourself of past successes
• Find inspiration from others' journeys
• Take care of your physical health (sleep, exercise)
• Practice gratitude daily

## When Motivation Fades
If you're feeling unmotivated, it might be related to depression 
or anxiety. Don't hesitate to reach out for professional support.
```

### Update `chat_engine.py`:

```python
keyword_map = {
    # ... existing ...
    'motivat': 'motivation.txt',  # matches "motivation", "motivated", "motivate"
    'confiden': 'motivation.txt',  # matches "confidence", "confident"
}
```

### Update `chatbot-ui/chatbot.js`:

```javascript
const keywordMap = {
    // ... existing ...
    'motivat': ['motivation'],
    'confiden': ['motivation'],
};
```

### Test:

```
User: "I need motivation"
Bot: [From Motivation]
     Motivation is the driving force that helps you achieve...
```

---

## Files Modified

### Backend
- **`chat_engine.py`** - Added `search_datasets()` and improved `get_response()` to prioritize datasets
- **`main.py`** - Already imports `get_response` correctly

### Frontend
- **`chatbot-ui/chatbot.js`** - Added `loadAllDatasets()` and improved `searchDatasets()` with keyword mapping
- **`chatbot-ui/index.html`** - No changes (works as-is)
- **`chatbot-ui/style.css`** - No changes

### Data
- **`data/stress_management.txt`** - Existing dataset
- **`data/depression.txt`** - Existing dataset
- **`data/anxiety.txt`** - Existing dataset
- **`data/sleep.txt`** - Existing dataset
- **`data/DATASETS_GUIDE.md`** - Comprehensive guide for datasets

### Tests
- **`test_datasets.py`** - New test script to verify dataset loading and searching

---

## Troubleshooting

### Problem: Chatbot not returning dataset content

**Check 1:** Verify datasets are loaded
```powershell
# Frontend: Open browser console (F12) and check for:
# ✓ Loaded dataset: anxiety
# ✓ Loaded dataset: depression
# etc.

# Backend: Check server logs for:
# INFO: Dataset match found for query...
```

**Check 2:** Verify keyword exists
```powershell
# Your query must contain one of the defined keywords
# "I'm feeling stressed" ✓ (contains "stress")
# "Help me" ✗ (doesn't match any specific keyword)
```

**Check 3:** Make sure HTTP server is running (frontend)
```powershell
# If using file:// protocol, dataset fetches may be blocked
# Use http://127.0.0.1:8001/ instead of file://
```

### Problem: API returning error instead of dataset

**Check 1:** API Key quota
```
Error: "You exceeded your current quota"
→ This is expected if API key has no credits
→ But dataset queries should still work without API!
```

**Check 2:** Dataset file not found
```
→ Make sure .txt file is in data/ folder
→ Check spelling matches keyword_map
```

### Problem: Added new dataset but it's not working

**Step 1:** Reload browser (Ctrl+F5) to clear cache
**Step 2:** Restart backend server
**Step 3:** Make sure keyword is in keywordMap (JS) and keyword_map (Python)
**Step 4:** Check that .txt file is in `data/` folder

---

## Architecture Overview

```
User Query
    ↓
┌─────────────────────────────────────────┐
│ Frontend (chatbot.js)                   │
│ - loadAllDatasets()                     │
│ - searchDatasets(message)               │
│ - Returns [From Dataset] or demo        │
└─────────────────────────────────────────┘
    OR
┌─────────────────────────────────────────┐
│ Backend (chat_engine.py)                │
│ - search_datasets(query)                │
│ - Falls back to OpenAI API              │
│ - Saves to sessions/{session_id}.json   │
└─────────────────────────────────────────┘
    ↓
Response with [From Dataset Name] label
```

---

## Next Steps

1. **Test the current setup** with the keywords provided above
2. **Add custom datasets** for topics important to your users
3. **Update keywords** in both frontend and backend for each new dataset
4. **Monitor usage** through browser console (frontend) or server logs (backend)
5. **Iterate** based on user questions and feedback

---

## Support Resources

- 📖 **Dataset Guide**: [data/DATASETS_GUIDE.md](./data/DATASETS_GUIDE.md)
- 🧪 **Test Script**: [test_datasets.py](./test_datasets.py)
- 📁 **Data Folder**: [data/](./data/)
- 🎯 **Frontend Logic**: [chatbot-ui/chatbot.js](./chatbot-ui/chatbot.js)
- ⚙️ **Backend Logic**: [chat_engine.py](./chat_engine.py)

---

## Summary

✅ **Datasets are now fully integrated!**

- Frontend loads all datasets on page load
- Backend searches datasets before calling API
- Keyword mapping ensures correct dataset is returned
- Easy to add new datasets with minimal code changes
- Clear `[From Dataset Name]` labels help users understand responses

**Your chatbot will now provide relevant, fast, dataset-based answers to mental health questions!** 🎉
