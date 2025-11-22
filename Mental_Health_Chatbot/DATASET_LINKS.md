# 📚 Dataset Links & Downloads

This file contains direct links to all available datasets for your Mental Health Chatbot.

## Available Datasets

### 1. Stress Management Dataset
**File:** `data/stress_management.txt`
**Size:** ~2 KB
**Topics Covered:**
- What is Stress?
- Common Signs of Stress
- Physical Manifestations
- Healthy Ways to Manage Stress
- Stress-Relief Activities
- Quick Tips for Daily Stress

**Use when user mentions:** stress, relax, meditation, exercise, breathing, pressure, overwhelmed

**Direct Link:** [stress_management.txt](./data/stress_management.txt)

---

### 2. Depression Dataset
**File:** `data/depression.txt`
**Size:** ~2.4 KB
**Topics Covered:**
- What is Depression?
- Common Signs of Depression
- Types of Depression
- Causes and Risk Factors
- How to Help Yourself
- When to Seek Professional Help

**Use when user mentions:** depression, depressed, sad, hopeless, mood, down, low

**Direct Link:** [depression.txt](./data/depression.txt)

---

### 3. Anxiety Dataset
**File:** `data/anxiety.txt`
**Size:** ~2.9 KB
**Topics Covered:**
- What is Anxiety?
- Types of Anxiety Disorders
- Physical Symptoms of Anxiety
- Causes of Anxiety
- Coping Strategies
- When to Seek Help

**Use when user mentions:** anxiety, anxious, panic, worried, afraid, nervous, fear

**Direct Link:** [anxiety.txt](./data/anxiety.txt)

---

### 4. Sleep Dataset
**File:** `data/sleep.txt`
**Size:** ~3.1 KB
**Topics Covered:**
- Why Sleep is Important
- Sleep Hygiene Tips
- Common Sleep Problems
- Natural Sleep Aids
- When Sleep Issues Require Help
- Creating a Sleep-Friendly Environment

**Use when user mentions:** sleep, insomnia, tired, fatigue, can't sleep, rest, bedtime

**Direct Link:** [sleep.txt](./data/sleep.txt)

---

## How to View Datasets

### Option 1: Online (Click Links Above)
Click any link above to view the dataset content directly in your browser.

### Option 2: In File Explorer
```
C:\Users\kala_\Downloads\Mental_Health_Chatbot\data\
```

Open any `.txt` file with a text editor (Notepad, VS Code, etc.)

### Option 3: In Terminal
```powershell
cd "C:\Users\kala_\Downloads\Mental_Health_Chatbot\data"
type stress_management.txt
type depression.txt
type anxiety.txt
type sleep.txt
```

### Option 4: Python
```python
# Read dataset content in Python
with open('data/stress_management.txt', 'r') as f:
    content = f.read()
    print(content)
```

---

## How to Search Datasets

### Search Query Examples

**Stress Questions:**
- "I'm feeling stressed"
- "How do I manage stress?"
- "Stress relief techniques"
- "Meditation and relaxation"
- "Breathing exercises"

**Anxiety Questions:**
- "I have anxiety"
- "Panic attack help"
- "I'm worried about..."
- "Anxiety symptoms"
- "How to cope with anxiety"

**Depression Questions:**
- "I'm depressed"
- "Feeling sad all the time"
- "Loss of interest in activities"
- "What is depression?"
- "Depression help"

**Sleep Questions:**
- "I can't sleep"
- "Insomnia tips"
- "Sleep hygiene"
- "I'm always tired"
- "Better sleep methods"

---

## Dataset Statistics

| Dataset | Keywords | Sections | Size | Status |
|---------|----------|----------|------|--------|
| Stress Management | stress, relax, meditation, exercise | 6 | 1.9 KB | ✓ Active |
| Depression | depress, sad, hopeless | 6 | 2.4 KB | ✓ Active |
| Anxiety | anxiety, panic, worried | 6 | 2.9 KB | ✓ Active |
| Sleep | sleep, insomnia, tired | 5 | 3.1 KB | ✓ Active |

**Total Dataset Size:** ~10.3 KB

---

## Editing Datasets

### To Edit a Dataset

1. Open the file in your text editor:
   ```
   C:\Users\kala_\Downloads\Mental_Health_Chatbot\data\stress_management.txt
   ```

2. Edit the content

3. Save the file (Ctrl+S)

4. **Reload the chatbot:**
   - **Frontend:** Press Ctrl+F5 in browser
   - **Backend:** Restart the uvicorn server

---

## Adding New Datasets

### Example: Adding a "Relationships" Dataset

1. **Create file:** `data/relationships.txt`

2. **Add content:**
```
RELATIONSHIPS AND COMMUNICATION GUIDE

## Healthy Relationships
A healthy relationship is built on mutual respect, trust, and open communication...

## Communication Tips
- Listen actively without interrupting
- Express your feelings using "I" statements
- Be honest and direct
- Respect boundaries
- Validate the other person's feelings

## Handling Conflicts
- Take time before responding to avoid saying hurtful things
- Focus on the issue, not the person
- Look for compromises
- Seek help if needed (couples therapy, mediation)
```

3. **Update keywords in `chat_engine.py`:**
```python
keyword_map = {
    # ... existing ...
    'relationship': 'relationships.txt',
    'communication': 'relationships.txt',
    'conflict': 'relationships.txt',
}
```

4. **Update keywords in `chatbot-ui/chatbot.js`:**
```javascript
const keywordMap = {
    // ... existing ...
    'relationship': ['relationships'],
    'communication': ['relationships'],
    'conflict': ['relationships'],
};
```

5. **Reload chatbot**
   - Browser: Ctrl+F5
   - Backend: Restart server

6. **Test:**
   ```
   User: "How do I improve my relationships?"
   Bot: [From Relationships] A healthy relationship is built on...
   ```

---

## Bulk Operations

### Export All Datasets
```powershell
# Windows PowerShell
$datasets = Get-Content data\*.txt
$datasets | Out-File all_datasets.txt -Encoding UTF8
```

### Search Within Datasets
```powershell
# Search for keyword in all datasets
Select-String -Path data\*.txt -Pattern "symptom"
```

### Count Total Words
```powershell
# Count total words across all datasets
(Get-Content data\*.txt | Measure-Object -Word).Words
```

---

## Best Practices

### When Adding Content to Datasets

✅ **Do:**
- Use clear, simple language
- Organize content into labeled sections
- Separate sections with blank lines
- Keep explanations concise (2-3 sentences per point)
- Include practical tips and strategies

❌ **Don't:**
- Use overly technical medical jargon
- Make content too long (datasets should be quick reads)
- Mix unrelated topics in one section
- Forget to update keywords when adding new content

### Keyword Best Practices

✅ **Good Keywords:**
- Single words: "stress", "anxiety", "sleep"
- Word stems: "depress" (matches depression, depressed, depressing)
- Related terms: "panic" → anxiety dataset

❌ **Bad Keywords:**
- Multiple words: "can't sleep" (use "sleep" instead)
- Too specific: "insomnia-with-anxiety" (just use "insomnia")
- Acronyms without spelling out: "PTSD" (spell it out or don't use)

---

## Maintenance & Updates

### Regular Reviews
- Monthly: Check if datasets are still relevant
- Quarterly: Add new topics based on user questions
- Yearly: Update outdated information

### Feedback Loop
1. Monitor which queries don't match datasets
2. Add new keywords or datasets for common questions
3. Improve existing content based on user needs
4. Test thoroughly before deploying

---

## Support & Resources

- 📖 **Full Documentation:** `DATASET_INTEGRATION.md`
- 🚀 **Quick Start:** `QUICK_START_DATASETS.md`
- 📂 **Datasets Directory:** `data/`
- 🧪 **Test Script:** `test_datasets.py`
- 🔍 **Search Guide:** `data/DATASETS_GUIDE.md`

---

## License & Attribution

All datasets are original content created for this Mental Health Chatbot project.

**Please note:** These datasets are for informational and supportive purposes only and should not be used as a substitute for professional medical or mental health advice.

---

## Quick Navigation

- **View Stress Management:** [stress_management.txt](./data/stress_management.txt)
- **View Depression Info:** [depression.txt](./data/depression.txt)
- **View Anxiety Support:** [anxiety.txt](./data/anxiety.txt)
- **View Sleep Guide:** [sleep.txt](./data/sleep.txt)
- **Full Integration Guide:** [DATASET_INTEGRATION.md](./DATASET_INTEGRATION.md)
- **Quick Start:** [QUICK_START_DATASETS.md](./QUICK_START_DATASETS.md)

---

**Last Updated:** November 19, 2025
**Status:** ✓ All datasets active and searchable
