from flask import Flask, request, render_template_string
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

app = Flask(__name__)

html = '''
<!doctype html>
<title>Chatbot</title>
<h3>Simple Chatbot</h3>
<form method=post>
  <input name=text type=text autofocus required placeholder="Type your message" style="width:70%%">
  <input type=submit value="Send">
</form>
{% if response %}
<p><b>Bot:</b> {{response}}</p>
{% endif %}
'''

@app.route("/", methods=["GET", "POST"])
def chat():
    response = ''
    if request.method == "POST":
        user_input = request.form.get("text","")
        if 'name' not in user_profile:
            user_profile['name'] = "User"
        doc = nlp(user_input.lower())
        if any(token.lemma_ in ['hi','hello','hey'] for token in doc):
            response = f"Hello, {user_profile['name']}! How can I help you today?"
        elif any(token.lemma_ in ['bye','exit','quit'] for token in doc):
            response = f"Goodbye, {user_profile['name']}! Have a nice day."
        elif any(token.lemma_ in ['how','be'] for token in doc) and 'you' in user_input.lower():
            response = "I'm a bot, but I'm doing well! How can I help you?"
        elif 'tip' in user_input.lower() or 'advice' in user_input.lower():
            tip = random.choice(health_tips)
            response = f"Here's a health tip for you: {tip}"
        else:
            response = "Sorry, I didn't understand that."
    return render_template_string(html, response=response)

if __name__ == "__main__":
    app.run(debug=True)
