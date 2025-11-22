# 💬 Questions to Ask Your Mental Health Chatbot

Use these example questions to test your chatbot and see dataset responses!

---

## 🧘 Stress Management Questions

Ask these to get responses from the **Stress Management dataset**:

```
1. "I'm feeling stressed"
2. "How do I manage stress?"
3. "What are stress relief techniques?"
4. "I'm feeling overwhelmed"
5. "How does meditation help with stress?"
6. "What are relaxation exercises?"
7. "I need to relax"
8. "How do I exercise for stress relief?"
9. "Help me cope with pressure"
10. "Stress management tips"
11. "I'm under a lot of stress"
12. "How to deal with daily stress?"
13. "Breathing exercises for stress"
14. "I need to manage my anxiety better"
15. "How do I stay calm?"
```

**Expected Response:** `[From Stress Management]` followed by stress-related content

---

## 😰 Anxiety Questions

Ask these to get responses from the **Anxiety dataset**:

```
1. "I have anxiety"
2. "I'm feeling anxious"
3. "Help with panic attacks"
4. "I'm worried about everything"
5. "What is anxiety?"
6. "How to cope with anxiety?"
7. "I'm afraid of things"
8. "Anxiety symptoms and help"
9. "I get panic attacks"
10. "How to calm down"
11. "I'm nervous and scared"
12. "Anxiety management strategies"
13. "What causes anxiety?"
14. "I feel anxious all the time"
15. "Help me with my fears"
```

**Expected Response:** `[From Anxiety]` followed by anxiety-related content

---

## 😔 Depression Questions

Ask these to get responses from the **Depression dataset**:

```
1. "I'm depressed"
2. "I feel depressed"
3. "I'm sad all the time"
4. "What is depression?"
5. "Depression help"
6. "I feel hopeless"
7. "I've lost interest in activities"
8. "Depression symptoms"
9. "How to help myself with depression?"
10. "I feel worthless"
11. "Depression is making me tired"
12. "When should I seek help for depression?"
13. "I'm feeling down"
14. "Depression and sleep problems"
15. "Can depression be treated?"
```

**Expected Response:** `[From Depression]` followed by depression-related content

---

## 😴 Sleep Questions

Ask these to get responses from the **Sleep dataset**:

```
1. "I can't sleep"
2. "I have insomnia"
3. "Help me sleep better"
4. "I'm always tired"
5. "Sleep hygiene tips"
6. "How to improve sleep?"
7. "Insomnia solutions"
8. "Why is sleep important?"
9. "I'm exhausted"
10. "Sleep problems"
11. "How to create a sleep routine?"
12. "Natural sleep aids"
13. "I can't fall asleep"
14. "Sleep and mental health"
15. "Bedroom setup for sleep"
```

**Expected Response:** `[From Sleep]` followed by sleep-related content

---

## 🎯 Mixed Topic Questions

These questions contain multiple keywords and will match one dataset:

```
1. "I'm stressed and can't sleep"          → [From Stress Management OR Sleep]
2. "My anxiety is causing insomnia"        → [From Anxiety OR Sleep]
3. "Depression makes me tired"             → [From Depression OR Sleep]
4. "Stressed and anxious"                  → [From Stress Management OR Anxiety]
5. "Depressed and hopeless"                → [From Depression]
6. "Worried and overwhelmed"               → [From Anxiety OR Stress Management]
7. "Can't concentrate due to stress"       → [From Stress Management]
8. "Anxiety and breathing problems"        → [From Anxiety]
9. "Sleep problems from depression"        → [From Sleep OR Depression]
10. "Panic attacks and stress"             → [From Anxiety OR Stress Management]
```

---

## ❓ Generic Questions (No Dataset Match)

These will use demo responses or OpenAI API fallback:

```
1. "Hello"
2. "How are you?"
3. "What's your name?"
4. "Tell me a joke"
5. "How can you help me?"
6. "What is this chatbot?"
7. "Can you help?"
8. "What do you do?"
9. "Hi there!"
10. "Thanks for helping"
```

**Expected Response:** Demo response or generic supportive message

---

## 🚨 Crisis Keywords (Special Handling)

These trigger crisis response with hotline numbers:

```
1. "I want to kill myself"
2. "I'm suicidal"
3. "I want to end my life"
4. "I'm going to hurt myself"
5. "I can't go on"
6. "I want to die"
```

**Expected Response:** Crisis safety message with hotline numbers:
- 🇮🇳 India: 9152987821 (iCall), 1800-599-0019 (Vandrevala Foundation)
- 🇺🇸 USA: 988 (National Suicide Prevention Lifeline)
- 🇬🇧 UK: 116 123 (Samaritans)

---

## 📱 How to Test

### Test in Browser

1. Open: `http://127.0.0.1:8001/index.html` (if running HTTP server)
2. Click "Chat with Us"
3. Type a question from above
4. Press Enter or click Send
5. Look for `[From Dataset Name]` in the response

### Check Console Logs

Open browser console (F12 → Console) and look for:

```
✓ Loaded dataset: stress_management
✓ Loaded dataset: anxiety
✓ Loaded dataset: depression
✓ Loaded dataset: sleep
Dataset matched for: I'm feeling anxious...
```

### Test via API

```powershell
$body = @{ session_id = "test1"; query = "I'm feeling stressed" } | ConvertTo-Json
curl http://127.0.0.1:8000/chat -Method POST -H "Content-Type: application/json" -Body $body
```

Expected response:
```json
{
  "response": "[From Stress Management]\n\n1. What is Stress?..."
}
```

---

## 🎓 Learning Path

### Beginner Test (5 minutes)
Try these simple questions to see basic functionality:

```
1. "I'm stressed" → Should get Stress Management content
2. "I have anxiety" → Should get Anxiety content
3. "I'm depressed" → Should get Depression content
4. "I can't sleep" → Should get Sleep content
5. "Hello" → Should get generic response
```

### Intermediate Test (10 minutes)
Try questions with more context:

```
1. "How do I manage my stress better?"
2. "What are symptoms of anxiety?"
3. "Depression makes me tired all day"
4. "Can meditation help with sleep?"
5. "I'm worried and overwhelmed"
```

### Advanced Test (15 minutes)
Test edge cases and custom combinations:

```
1. "I'm both stressed and anxious"
2. "Depression and sleep problems together"
3. "Anxiety is keeping me awake"
4. "Stress relief and meditation"
5. Mixed topics from different datasets
```

---

## 📊 What to Expect

### Response Format with Dataset

```
[From Dataset Name]

1. Section Content
Content about the topic that matches your question...

2. More Information
Additional helpful information...
```

### Response Format without Dataset Match

```
Generic supportive response:
"Thank you for sharing. Your feelings are valid and important..."

OR

OpenAI API response (if configured)
```

---

## 🔍 Observation Checklist

When testing, look for:

- ✅ Does response start with `[From Dataset Name]`?
- ✅ Is the content relevant to your question?
- ✅ Does it come from the correct dataset?
- ✅ Are there any console errors (F12)?
- ✅ Does it respond quickly (<500ms)?
- ✅ Is the user message saved in history?
- ✅ Can you ask follow-up questions?

---

## 💡 Pro Tips

1. **Use specific keywords** - "stress" works better than "feeling bad"
2. **Check console** - Browser console shows which datasets loaded
3. **Mix and match** - Try questions with multiple keywords
4. **Test fallback** - Ask "hello" to see what happens without dataset match
5. **Monitor history** - Left sidebar shows all your conversations

---

## 📝 Example Conversation

```
You: "I'm feeling very stressed and can't sleep"

Bot: [From Stress Management]

1. What is Stress? 
Stress is the body's natural reaction to challenges or demands. 
When faced with a challenge, your body releases chemicals that 
increase your heart rate and blood pressure. This is the "fight 
or flight" response.

Common Stress Triggers:
• Work pressure and deadlines
• Relationship problems
• Financial worries
• Major life changes
• Health concerns

You: "What are some relaxation techniques?"

Bot: [From Stress Management]

Healthy Ways to Manage Stress:

1. Exercise and Physical Activity
Regular physical activity helps reduce stress hormones and 
releases endorphins (feel-good chemicals).

2. Meditation and Mindfulness
Focusing on the present moment can calm your mind and reduce 
anxiety...

[Response continues with more techniques]
```

---

## 🎯 Next Steps

1. **Pick a question** from above
2. **Ask your chatbot** via browser or API
3. **Check the response** - should have `[From Dataset Name]`
4. **Verify accuracy** - response should match your question
5. **Try more questions** - test different topics
6. **Add your own datasets** - customize for your needs

---

## 📞 Questions or Issues?

If a question doesn't return dataset content:

1. Check browser console for errors
2. Verify the keyword is in the keyword mapping
3. Try a different phrasing with dataset keywords
4. Check that datasets are loaded (console logs)
5. Restart server and reload page

---

**Happy chatting! 💬**

Use these questions to explore your Mental Health Chatbot's capabilities.

**Last Updated:** November 19, 2025
