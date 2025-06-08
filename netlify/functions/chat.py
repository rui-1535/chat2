from flask import Flask, request, jsonify
from chat_ai import ChatAI
import os
from dotenv import load_dotenv
import json

# 環境変数の読み込み
load_dotenv()

app = Flask(__name__)
chat_ai = ChatAI()

def handler(event, context):
    if event['httpMethod'] == 'POST':
        try:
            body = json.loads(event['body'])
            user_message = body.get('message', '')
            
            if not user_message:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': 'メッセージが空です'})
                }
            
            response = chat_ai.get_ai_response(user_message)
            return {
                'statusCode': 200,
                'body': json.dumps({'response': response})
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e)})
            }
    
    return {
        'statusCode': 405,
        'body': json.dumps({'error': 'Method not allowed'})
    } 