#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# System message for the chatbot
SYSTEM_MESSAGE = """Wisp is a compassionate mental health counselor offering support and guidance to [someone struggling with mental illness]. 
How would you encourage them to prioritize self-care, seek professional help, and stay positive during their journey towards healing and recovery?"""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    response = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0125:personal:wisp:91dhHss7",
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": user_message}
        ]
    )
    
    bot_response = response.choices[0].message.content
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)

