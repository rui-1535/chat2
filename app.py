from flask import Flask, render_template, request, jsonify
from chat_ai import ChatAI
import os
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()

app = Flask(__name__)
chat_ai = ChatAI()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({'error': 'メッセージが空です'}), 400
    
    response = chat_ai.get_ai_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True) 