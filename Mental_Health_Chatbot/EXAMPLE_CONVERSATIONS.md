# 🗣️ Example Questions & Expected Answers

This file shows example questions you can ask your chatbot and what responses to expect.

---

## Test Question Set 1: Stress Management

### Question 1
**You:** "I'm feeling stressed"

**Expected Response:**
```
[From Stress Management]

1. What is Stress?
Stress is the body's natural reaction to challenges or demands. 
When faced with a challenge, your body releases chemicals that 
increase your heart rate and blood pressure. This is the 
"fight or flight" response.
```

---

### Question 2
**You:** "How do I manage my stress?"

**Expected Response:**
```
[From Stress Management]

Healthy Ways to Manage Stress:

• Exercise and Physical Activity
Regular physical activity helps reduce stress hormones and 
releases endorphins (feel-good chemicals).

• Meditation and Mindfulness
Focusing on the present moment can calm your mind...
```

---

### Question 3
**You:** "What relaxation techniques help?"

**Expected Response:**
```
[From Stress Management]

Stress-Relief Activities:

• Deep breathing exercises
• Progressive muscle relaxation
• Yoga or stretching
• Nature walks
• Creative hobbies
• Listening to music
```

---

## Test Question Set 2: Anxiety

### Question 4
**You:** "I have anxiety"

**Expected Response:**
```
[From Anxiety]

1. What is Anxiety?
Anxiety is your body's natural response to stress or fear. 
While it's a normal emotion, excessive anxiety can interfere 
with daily life.

Types of Anxiety Disorders:
• Generalized Anxiety Disorder (GAD)
• Panic Disorder
• Social Anxiety Disorder
• Specific Phobias
```

---

### Question 5
**You:** "I'm worried about everything"

**Expected Response:**
```
[From Anxiety]

Coping Strategies for Anxiety:

1. Breathing Techniques
• Practice deep breathing (4-7-8 technique)
• Slow, controlled breathing activates relaxation response

2. Grounding Techniques
• 5-4-3-2-1 method (identify 5 things you see, 4 you feel...)
```

---

### Question 6
**You:** "Panic attacks help"

**Expected Response:**
```
[From Anxiety]

9. When to Seek Help
Contact a healthcare provider if:
• Anxiety interferes with daily activities
• Anxiety lasts more than 2 weeks
• You avoid situations due to anxiety
• Anxiety causes physical symptoms
```

---

## Test Question Set 3: Depression

### Question 7
**You:** "I'm depressed"

**Expected Response:**
```
[From Depression]

1. What is Depression?
Depression is a serious mental health condition characterized 
by persistent feelings of sadness, hopelessness, and loss of 
interest in activities. It's more than just feeling sad - 
it's a medical condition that affects how you feel, think, 
and function.
```

---

### Question 8
**You:** "I feel sad all the time"

**Expected Response:**
```
[From Depression]

2. Common Signs of Depression
• Persistent sadness or empty feelings
• Loss of interest in hobbies and activities
• Changes in appetite or weight
• Sleep problems (insomnia or excessive sleeping)
• Fatigue and loss of energy
• Feelings of worthlessness or guilt
```

---

### Question 9
**You:** "Depression making me tired"

**Expected Response:**
```
[From Depression]

5. How to Help Yourself
• Reach out to trusted friends or family
• Maintain a regular sleep schedule
• Exercise regularly (even 20 minutes helps)
• Eat healthy, balanced meals
• Limit alcohol and avoid drugs
• Practice relaxation techniques
```

---

## Test Question Set 4: Sleep

### Question 10
**You:** "I can't sleep"

**Expected Response:**
```
[From Sleep]

1. Why Sleep is Important
Sleep is essential for physical and mental health. During sleep, 
your body repairs itself and your brain processes information. 
Chronic sleep deprivation can lead to serious health problems.
```

---

### Question 11
**You:** "Help with insomnia"

**Expected Response:**
```
[From Sleep]

Sleep Hygiene Tips:
• Keep a consistent sleep schedule (same time every day)
• Create a dark, cool, quiet bedroom
• Avoid screens 1 hour before bed
• Exercise regularly, but not close to bedtime
• Limit caffeine and alcohol
• Try relaxation techniques like deep breathing
```

---

### Question 12
**You:** "I'm always tired"

**Expected Response:**
```
[From Sleep]

Common Sleep Problems:
• Insomnia - difficulty falling or staying asleep
• Sleep Apnea - interrupted breathing during sleep
• Restless Leg Syndrome - uncomfortable sensations
• Narcolepsy - excessive daytime sleepiness

When Sleep Issues Require Help:
If insomnia persists for 2+ weeks, consider consulting...
```

---

## Test Question Set 5: Mixed Topics

### Question 13
**You:** "Stressed and can't sleep"

**Expected Response:**
```
[From Stress Management] OR [From Sleep]

(System returns content from one of the matching datasets)

1. What is Stress?
Stress is the body's natural reaction to challenges...
```

---

### Question 14
**You:** "Anxiety is keeping me awake"

**Expected Response:**
```
[From Anxiety] OR [From Sleep]

(System returns content from first matching dataset)

1. What is Anxiety?
Anxiety is your body's natural response to stress...
```

---

### Question 15
**You:** "Depressed and hopeless"

**Expected Response:**
```
[From Depression]

1. What is Depression?
Depression is a serious mental health condition characterized 
by persistent feelings of sadness, hopelessness...
```

---

## Test Question Set 6: Generic Questions (No Dataset Match)

### Question 16
**You:** "Hello"

**Expected Response:**
```
Your wellbeing matters. What can I help with?
```
(Or another generic supportive response from demo responses)

---

### Question 17
**You:** "How are you?"

**Expected Response:**
```
I'm here to listen. Tell me more about what you're experiencing.
```
(Generic supportive response)

---

### Question 18
**You:** "Can you help me?"

**Expected Response:**
```
Of course, I'm here to listen and support you. What do you need help with?
```
(Generic response since "help" alone doesn't match specific dataset)

---

## Test Question Set 7: Crisis Keywords

### Question 19
**You:** "I want to kill myself"

**Expected Response:**
```
It seems like you're going through a really tough time right now. 
Please remember that you're not alone, and there are people who 
care about you and want to help.

If you're feeling overwhelmed, consider reaching out to a mental 
health professional or a trusted person in your life.

In case of an emergency, please contact emergency services or a 
crisis hotline immediately:

🇮🇳 India: 9152987821 (iCall), 1800-599-0019 (Vandrevala Foundation)
🇺🇸 USA: 988 (National Suicide Prevention Lifeline)
🇬🇧 UK: 116 123 (Samaritans)

You matter.
```

---

## How to Use This Guide

1. **Copy a question** from above
2. **Ask your chatbot** in the browser or API
3. **Compare the response** to the expected output
4. **Check for `[From Dataset Name]` label**
5. **Verify accuracy** - does it match the topic?

---

## Response Patterns

All dataset responses follow this pattern:

```
[From Dataset Name]

Section Title
Content from the dataset...

More Content
Additional information...
```

---

## Tips for Best Results

✅ Use **specific keywords**: "stress", "anxiety", "depressed", "sleep"
✅ Ask in **natural language**: "I'm feeling stressed"
✅ Check **browser console** (F12) for load status
✅ Monitor **response time** - should be fast (<500ms)
✅ Notice **[From Dataset Name]** label in responses

---

## Troubleshooting

### Chatbot not returning dataset content?

**Check:**
1. Does your question contain a dataset keyword?
   - Stress: "stress", "relax", "meditation", "exercise"
   - Anxiety: "anxiety", "panic", "worried", "afraid"
   - Depression: "depress", "depressed", "sad", "hopeless"
   - Sleep: "sleep", "insomnia", "tired"

2. Is dataset loaded?
   - Open browser console (F12)
   - Look for: `✓ Loaded dataset: anxiety`

3. Is the HTTP server running?
   - Use: `python -m http.server 8001` from `chatbot-ui/`
   - Visit: `http://127.0.0.1:8001/index.html`

---

## Next Steps

1. ✅ Pick a question from above
2. ✅ Ask your chatbot
3. ✅ Check for `[From Dataset Name]` label
4. ✅ Compare to expected response
5. ✅ Try more questions to explore features
6. ✅ Add your own datasets when ready

---

**Remember:** The chatbot will respond fastest to questions with dataset keywords. Generic questions will use demo responses.

**Last Updated:** November 19, 2025
