# 🎯 Dataset Integration - Quick Start

## What Changed?

Your chatbot **now properly uses datasets**! Both frontend and backend have been updated.

---

## Quick Test (30 seconds)

### Frontend (Browser)
```
1. Open: http://127.0.0.1:8001/index.html
   (or serve from: python -m http.server 8001 in chatbot-ui/)

2. Click "Chat with Us"

3. Type: "I'm feeling anxious"

4. Expected: Response from anxiety.txt with [From Anxiety] label
```

### Backend (API)
```powershell
$body = @{ session_id = "user1"; query = "I'm depressed" } | ConvertTo-Json
curl http://127.0.0.1:8000/chat -Method POST -H "Content-Type: application/json" -Body $body
```

**Expected Response:**
```
[From Depression]
1. What is Depression? Depression is a serious mental health condition...
```

---

## What Works Now

| Query | Returns |
|-------|---------|
| "stress" | [From Stress Management] |
| "anxiety" | [From Anxiety] |
| "depressed" | [From Depression] |
| "can't sleep" | [From Sleep] |
| "meditation" | [From Stress Management] |
| "panic attack" | [From Anxiety] |
| "feeling sad" | [From Depression] |
| "insomnia" | [From Sleep] |

---

## Files Updated

✅ `chatbot-ui/chatbot.js` - Added dataset loading and searching
✅ `chat_engine.py` - Added dataset search with OpenAI fallback
✅ `test_datasets.py` - Test script to verify everything works
✅ `data/DATASETS_GUIDE.md` - Complete dataset guide
✅ `DATASET_INTEGRATION.md` - This comprehensive guide

---

## Key Features

1. **Instant dataset responses** - No API calls needed
2. **Clear labeling** - `[From Dataset Name]` shows where answer comes from
3. **Easy to add** - Create a new .txt file, add keywords, reload
4. **No API quota** - Datasets work even if OpenAI quota is exceeded
5. **Per-user sessions** - Backend saves conversation history

---

## Add a New Dataset (5 minutes)

### Step 1: Create file
```
data/my_topic.txt
```

### Step 2: Add content
```
MY TOPIC GUIDE

## Overview
Information about my topic...

## Tips
- Tip 1
- Tip 2
```

### Step 3: Add keywords

**Backend:** Edit `chat_engine.py`
```python
keyword_map = {
    'mytopic': 'my_topic.txt',
    'keyword1': 'my_topic.txt',
}
```

**Frontend:** Edit `chatbot-ui/chatbot.js`
```javascript
const keywordMap = {
    'mytopic': ['my_topic'],
    'keyword1': ['my_topic'],
};
```

### Step 4: Reload
- Browser: Ctrl+F5
- Backend: Restart server

### Step 5: Test
```
User: "I need help with mytopic"
Bot: [From My Topic] ...content from my_topic.txt...
```

---

## Test It

```powershell
cd "C:\Users\kala_\Downloads\Mental_Health_Chatbot"
python test_datasets.py
```

Expected output:
```
✓ stress_management.txt: 1908 bytes
✓ depression.txt: 2447 bytes
✓ anxiety.txt: 2891 bytes
✓ sleep.txt: 3091 bytes
✓ Query: 'I'm feeling stressed' - Match found: [From Stress Management]
✓ Query: 'I have anxiety' - Match found: [From Anxiety]
✓ Response includes dataset label - dataset search is working!
```

---

## How It Works (Diagram)

```
User Message
    ↓
[Frontend: searchDatasets() OR Backend: search_datasets()]
    ↓
Does query contain a keyword? (stress, anxiety, depress, sleep, etc.)
    ↓
YES → Extract content from matching dataset file
      Return with [From Dataset Name] label
    ↓
NO → (Backend only) Call OpenAI API as fallback
     (Frontend) Return demo response
```

---

## Browser Console Logs (F12 → Console)

When chatbot loads, you should see:

```
✓ Loaded dataset: stress_management
✓ Loaded dataset: depression
✓ Loaded dataset: anxiety
✓ Loaded dataset: sleep
```

When you send a message:

```
Dataset matched for: I'm feeling anxious...
```

---

## Full Documentation

- 📖 **Comprehensive Guide**: `DATASET_INTEGRATION.md`
- 📁 **Dataset Guide**: `data/DATASETS_GUIDE.md`
- 🧪 **Test Script**: `test_datasets.py`

---

## Troubleshooting

**Q: Getting no response?**
- A: Your query might not contain a keyword. Use "stress", "anxiety", "depressed", "sleep", etc.

**Q: Getting API error?**
- A: That's OK! Datasets don't need the API. If dataset matched, you'll get dataset response.

**Q: Added new dataset but it's not working?**
- A: Reload page (Ctrl+F5) and restart server. Make sure keyword is in keywordMap (JS) and keyword_map (Python).

**Q: How do I add a custom dataset?**
- A: Follow "Add a New Dataset" section above. Takes 5 minutes!

---

## That's It! 🎉

Your chatbot now **properly answers questions from datasets** and can be easily extended with custom datasets for your specific needs.

Happy chatting! 💬
