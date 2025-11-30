<h1 style="font-family: 'Arial Black', sans-serif; color:#1F618D;"> Project: Mental Health Chatbot</h1>

<p style="font-family: 'Verdana', sans-serif; font-size:16px;">
The <b>Mental Health Chatbot</b> is an AI-powered system that provides supportive responses and guidance related to mental health queries. Users can ask questions or describe their feelings, and the chatbot responds using information from a curated dataset and OpenAI GPT models.
</p>

<img width="9000" height="500" alt="Chatbot Screenshot" src="https://github.com/user-attachments/assets/mental_health_screenshot.png" />

<p style="font-family: 'Verdana', sans-serif; font-size:16px;">
Imagine a user seeking mental health guidance. They can interact with the chatbot through a web interface or API. The system will:
</p>

<ul style="font-family: 'Verdana', sans-serif; font-size:16px;">
<li>Analyze the user's input.</li>
<li>Search the local dataset for relevant context.</li>
<li>Generate meaningful and empathetic responses using <b>OpenAI GPT</b>.</li>
</ul>

<h2 style="font-family: 'Arial Black', sans-serif; color:#1F618D;"> Technical Architecture</h2>

<ol style="font-family: 'Verdana', sans-serif; font-size:16px;">
<li><b>Stage 1: Query Processing & Dataset Matching</b>
<ul>
<li>Receive user input via web interface or API.</li>
<li>Perform fuzzy matching on local dataset to extract relevant context.</li>
<li>Prepare context for GPT-based response generation.</li>
</ul>
</li>
<li><b>Stage 2: Response Generation</b>
<ul>
<li>Send user query + context to <b>OpenAI GPT</b> using API.</li>
<li>Receive a contextual and empathetic response.</li>
<li>Return response to the user in real-time via the web interface.</li>
</ul>
</li>
</ol>

<h2 style="font-family: 'Arial Black', sans-serif; color:#1F618D;"> Setup Instructions</h2>

<ul style="font-family: 'Verdana', sans-serif; font-size:16px;">
<li><b>Get API Key:</b> Obtain your OpenAI API key and update <code>.env</code>:
<pre>OPENAI_API_KEY=your_api_key_here</pre></li>

<li><b>Install Dependencies:</b>
<pre>pip install -r requirements.txt</pre>
</li>

<li><b>Run FastAPI Backend:</b>
<pre>uvicorn main:app --reload --port 8000</pre>
</li>

<li><b>Test API:</b> Open in browser:
<pre>http://127.0.0.1:8000/docs</pre>
Use the Swagger UI to interact with the chatbot endpoints.</li>
</ul>

<h2 style="font-family: 'Arial Black', sans-serif; color:#1F618D;"> Features</h2>
<ul style="font-family: 'Verdana', sans-serif; font-size:16px;">
<li>AI-powered mental health guidance using OpenAI GPT models</li>
<li>Dataset-based context for more relevant responses</li>
<li>Interactive web/API interface via FastAPI</li>
<li>Real-time responses</li>
<li>Easy integration for frontend applications</li>
</ul>

<h2 style="font-family: 'Arial Black', sans-serif; color:#1F618D;"> License & Terms</h2>
<p style="font-family: 'Verdana', sans-serif; font-size:16px;">
Copyright (C) Dhavamani A.<br>
Licensed under the <b>MIT License</b>.<br>
Commercial use requires explicit permission.<br>
Attribution must be given in all copies or substantial portions of the software.
</p>
