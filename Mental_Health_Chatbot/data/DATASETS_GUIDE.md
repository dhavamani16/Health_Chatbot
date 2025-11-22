# Mental Health Chatbot - Datasets Guide

## Overview

The chatbot is configured to search **local datasets** first before calling the OpenAI API. This means:

- **Faster responses** (no API call needed)
- **No API rate limits** (local text search only)
- **Customizable content** (add your own .txt files)

## Available Datasets

The following datasets are loaded and searchable:

1. **stress_management.txt** - Information about stress, coping strategies, and relaxation techniques
2. **depression.txt** - Information about depression, symptoms, and support resources
3. **anxiety.txt** - Information about anxiety disorders and coping methods
4. **sleep.txt** - Information about sleep hygiene, insomnia, and sleep improvement

## How to Use the Chatbot with Datasets

### Frontend (Browser Chat)
When you ask the chatbot a question using keywords from the datasets, it will:

1. **Search** all loaded datasets for matching content
2. **Extract** relevant paragraphs/sections
3. **Return** the dataset content with a label `[From dataset_name]`
4. **Example:**
   ```
   User: "I'm feeling stressed"
   Bot: "[From Stress Management]
   Stress is a normal reaction to life's demands. When faced with a challenge, 
   your body releases chemicals that increase your heart rate and blood pressure..."
   ```

### Backend API (`/chat` endpoint)
The backend also searches datasets before calling OpenAI:

```powershell
# Example API call:
$body = @{ session_id = "user1"; query = "How do I manage anxiety?" } | ConvertTo-Json
curl http://127.0.0.1:8000/chat -Method POST -H "Content-Type: application/json" -Body $body
```

## Search Keywords

The datasets are searchable using these keywords:

- **stress** → stress_management.txt
- **anxiety** → anxiety.txt
- **depression** → depression.txt
- **sleep** → sleep.txt
- **exercise, meditation, breath, relax, manage, cope, help, support** → searched across all datasets

## Adding Custom Datasets

To add your own dataset and have the chatbot use it:

1. **Create a new `.txt` file** in the `data/` folder:
   ```
   c:\Users\kala_\Downloads\Mental_Health_Chatbot\data\my_custom_topic.txt
   ```

2. **Add content** with clear sections separated by blank lines:
   ```
   # My Custom Topic

   ## Section 1: Overview
   This is helpful information about...

   ## Section 2: Tips
   Here are some practical tips...
   ```

3. **Restart the chatbot** or reload the page
   - The frontend will automatically load the new dataset
   - The backend will discover it on the next API call

4. **Test it:**
   - Ask a question containing keywords from your dataset
   - The chatbot should return content from your new file

## Example: Adding a Sleep Dataset

**File:** `c:\Users\kala_\Downloads\Mental_Health_Chatbot\data\sleep.txt`

**Content:**
```
# Sleep Management Guide

## What is Sleep Hygiene?

Sleep hygiene refers to habits and practices that help you achieve 
consistent, uninterrupted sleep. Good sleep is essential for mental health.

## Tips for Better Sleep

1. Maintain a consistent sleep schedule - go to bed and wake up at the same time
2. Create a dark, cool, quiet bedroom
3. Avoid screens 1 hour before bed
4. Exercise regularly, but not close to bedtime
5. Limit caffeine and alcohol
6. Try relaxation techniques like deep breathing or meditation

## If You Have Insomnia

Insomnia is difficulty falling or staying asleep. Common causes include:
- Stress and anxiety
- Irregular sleep schedules
- Poor sleep environment
- Medical conditions

Consider consulting a healthcare provider if insomnia persists for 2+ weeks.
```

Then ask the chatbot: **"I have trouble sleeping"** → It will return content from `sleep.txt`

## Dataset Search Priority

The chatbot searches datasets in this order:

1. **Keyword matching** - Does the user's question contain a keyword like "stress", "anxiety", etc.?
2. **Content matching** - Does the dataset file contain that keyword?
3. **Section extraction** - Extract the first relevant paragraph
4. **Return with label** - Return the content with `[From Dataset Name]`
5. **Fallback** - If no dataset matches, use OpenAI API or demo responses

## Linked Datasets (For User Reference)

Here are links to the dataset files:

- **Stress Management:** [stress_management.txt](./stress_management.txt)
- **Depression Info:** [depression.txt](./depression.txt)
- **Anxiety Support:** [anxiety.txt](./anxiety.txt)
- **Sleep Hygiene:** [sleep.txt](./sleep.txt)

## Testing Datasets

### Test 1: Frontend Dataset Search
1. Open `http://127.0.0.1:8001/index.html` (with HTTP server running)
2. Click "Chat with Us"
3. Type: **"stress"**
4. Expected: Response from `stress_management.txt`

### Test 2: Backend Dataset Search
```powershell
# In PowerShell, test the /chat endpoint with dataset queries:
$body = @{ session_id = "test1"; query = "anxiety" } | ConvertTo-Json
curl http://127.0.0.1:8000/chat -Method POST -H "Content-Type: application/json" -Body $body
```

### Test 3: Custom Dataset
1. Create `c:\Users\kala_\Downloads\Mental_Health_Chatbot\data\motivation.txt`
2. Add content about motivation
3. Ask the chatbot: **"motivate me"**
4. It should return content from your new file

## Troubleshooting

**Q: The chatbot is not returning dataset content**
- A: Check the browser console (F12) for errors like `⚠ Could not load dataset: file.txt`
- Make sure the HTTP server is running if testing the frontend
- Check that your dataset file contains the keywords you're searching for

**Q: I added a new dataset but it's not being used**
- A: Reload the browser page (Ctrl+F5) to refresh the dataset cache
- Or restart the backend server
- Make sure the `.txt` file is in `data/` folder

**Q: The response is from the API, not my dataset**
- A: Check that your query contains a keyword that exists in your dataset
- Add more keywords to `searchDatasets()` function in `chatbot.js`
- Expand keywords in `search_datasets()` function in `chat_engine.py`

## Next Steps

1. **Add more datasets** for topics you care about
2. **Test with keywords** to ensure search works
3. **Customize content** to match your audience
4. **Monitor the console** (F12) to see which datasets are being loaded and matched

Enjoy using datasets to power your chatbot! 🎯
