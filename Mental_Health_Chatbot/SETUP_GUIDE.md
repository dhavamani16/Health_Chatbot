# Mental Health Chatbot - Complete Setup & Run Guide

## ✓ Server Status
- **Status**: ✓ ALL SYSTEMS READY
- **Backend**: Running on http://127.0.0.1:8000
- **API Key**: ✓ Loaded from .env

---

## 🚀 Step-by-Step to Run the Chatbot

### Step 1: Open Browser and Navigate to Chatbot UI

Your chatbot is ready at:
```
C:\Users\kala_\Downloads\Mental_Health_Chatbot\chatbot-ui\index.html
```

**Do this:**
1. Open **File Explorer**
2. Navigate to: `C:\Users\kala_\Downloads\Mental_Health_Chatbot\chatbot-ui\`
3. **Double-click on `index.html`**
4. Your browser will open with the chatbot interface

### Step 2: See the Chatbot Button

You should see:
- A beautiful purple gradient background
- A heading: "Mental Health Support Chatbot"
- A blue **"💬 Chat with Us"** button in the bottom-right corner

### Step 3: Start Chatting

1. **Click the "💬 Chat with Us" button**
2. A chat window will pop up
3. **Type your message**, for example:
   - "I am depressed"
   - "I'm feeling anxious"
   - "Help me with stress"
4. **Click "Send"** or press **Enter**
5. Wait 2-3 seconds for the AI response

---

## 📋 Quick Reference Commands

### **To Start the Server** (run in PowerShell):
```powershell
cd C:\Users\kala_\Downloads\Mental_Health_Chatbot
C:\Users\kala_\anaconda3\python.exe -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### **To Stop the Server**:
Press **Ctrl+C** in the PowerShell where the server is running

### **To View Server Logs**:
Watch the PowerShell window while chatting - you'll see logs like:
```
POST /chat HTTP/1.1 200 OK
```

---

## 🧪 Testing

### Test 1: Check if Server is Running
Open a new PowerShell and run:
```powershell
curl http://127.0.0.1:8000/
```
You should see:
```json
{"message":"Welcome to the Mental Health Support Chatbot"}
```

### Test 2: Test the Chat Endpoint
```powershell
$body = @{ session_id = "test1"; query = "hello" } | ConvertTo-Json
curl http://127.0.0.1:8000/chat -Method POST -H "Content-Type: application/json" -Body $body
```

### Test 3: Test Document Chat
```powershell
$body = @{ session_id = "test1"; query = "stress management" } | ConvertTo-Json
curl http://127.0.0.1:8000/doc-chat -Method POST -H "Content-Type: application/json" -Body $body
```

---

## 🔍 Troubleshooting

### Problem: Server Won't Start
1. Check that `.env` file exists with your API key
2. Run: `C:\Users\kala_\anaconda3\python.exe test_server.py` (should show all ✓)
3. Make sure port 8000 is not in use by another app

### Problem: Chatbot Button Doesn't Appear
1. Make sure you opened `chatbot-ui/index.html` (not the root `index.html`)
2. Open browser console: Press **F12** → **Console** tab
3. Check for errors like "Failed to load style.css" or "chatbot.js not found"
4. If files are missing, make sure you're in the correct folder

### Problem: "Error contacting OpenAI API"
1. Check your OpenAI API key in `.env`
2. Go to https://platform.openai.com to verify your key is valid
3. Check you have API credits available
4. Check your internet connection

### Problem: No Response from Bot
1. Check the server terminal for error messages
2. Make sure server is still running (didn't crash)
3. Try a simple message like "hello" first
4. Check browser console (F12) for network errors

---

## 📁 Project Structure

```
Mental_Health_Chatbot/
├── main.py                 # FastAPI server
├── chat_engine.py          # OpenAI chat logic
├── doc_engine.py           # Document search & chat
├── crisis.py               # Crisis keyword detection
├── loger.py                # Chat logging to CSV
├── models.py               # Pydantic models
├── test_server.py          # Diagnostic test script
├── .env                    # API key (create this)
├── chat_logs.csv           # Auto-created chat logs
├── requirements.txt        # Python dependencies
├── chatbot-ui/
│   ├── index.html          # Main webpage
│   ├── chatbot.js          # Frontend JavaScript
│   └── style.css           # Styling
└── data/                   # Optional: .txt files for document chat
```

---

## ✨ Features

✓ **Compassionate AI Chat** - Uses GPT-3.5-turbo with mental health system prompt
✓ **Session Memory** - Remembers conversation within a session
✓ **Crisis Detection** - Detects keywords and provides crisis hotline info
✓ **Document Chat** - Search and answer from local .txt files
✓ **Chat Logging** - Logs all conversations to `chat_logs.csv`
✓ **CORS Enabled** - Works from any origin (development-friendly)

---

## 📞 For Support

If you encounter issues:
1. Run `test_server.py` to diagnose problems
2. Check the PowerShell terminal running the server for error messages
3. Make sure all dependencies are installed
4. Verify `.env` file has your OpenAI API key

**Everything is ready. Enjoy chatting!** 💚
