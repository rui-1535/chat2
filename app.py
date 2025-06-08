print("########################################")
print("##### APP.PY IS BEING EXECUTED #####")
print("########################################")
from flask import Flask, render_template, request, jsonify
import sys
print(f"DEBUG: sys.path at app.py start: {sys.path}")

from chat_ai import ChatAI
print("DEBUG: chat_ai module imported.")

import os
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()
print(f"DEBUG: OPENAI_API_KEY loaded: {bool(os.getenv('OPENAI_API_KEY'))}")

app = Flask(__name__)
chat_ai = ChatAI()
print("DEBUG: ChatAI instance created.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    print("DEBUG: /chat endpoint hit.")
    user_message = request.json.get('message', '')
    if not user_message:
        print("DEBUG: Empty message received.")
        return jsonify({'error': 'メッセージが空です'}), 400
    
    response = chat_ai.get_ai_response(user_message)
    print(f"DEBUG: AI response generated: {response[:50]}...")
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True) 