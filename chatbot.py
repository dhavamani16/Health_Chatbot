import spacy
import random
nlp=spacy.load("en_core_web_sm")
user_profile={}
health_tips=[
"Remember to drink at least 8 glasses of water daily.",
"Try to get 30 minutes of exercise every day.",
"Aim for 7-8 hours of good quality sleep each night.",
"Take short breaks to stretch if you sit for long hours."
]
while True:
    if 'name' not in user_profile:
        print("Bot: Hello! What's your name?")
        name=input("You: ")
        user_profile['name']=name.capitalize()
        print(f"Bot: Nice to meet you, {user_profile['name']}!")
        continue
    user_input=input(f"{user_profile['name']}: ")
    doc=nlp(user_input.lower())
    if any(token.lemma_ in ['hi','hello','hey'] for token in doc):
        print(f"Bot: Hello, {user_profile['name']}! How can I help you today?")
    elif any(token.lemma_ in ['bye','exit','quit'] for token in doc):
        print(f"Bot: Goodbye, {user_profile['name']}! Have a nice day.")
        break
    elif any(token.lemma_ in ['how','be'] for token in doc) and 'you' in user_input.lower():
        print("Bot: I'm a bot, but I'm doing well! How can I help you?")
    elif 'tip' in user_input.lower() or 'advice' in user_input.lower():
        tip=random.choice(health_tips)
        print(f"Bot: Here's a health tip for you: {tip}")
    else:
        print("Bot: Sorry, I didn't understand that.")
