import json
import os
from chat_ai import ChatAI
from dotenv import load_dotenv
import logging

# ロギングの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 環境変数の読み込み
load_dotenv()

# ChatAIインスタンスの初期化
try:
    chat_ai = ChatAI()
except Exception as e:
    logger.error(f"ChatAI initialization error: {str(e)}")
    chat_ai = None

def handler(event, context):
    if not chat_ai:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'ChatAI initialization failed'})
        }

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
        except json.JSONDecodeError:
            logger.error("Invalid JSON in request body")
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Invalid JSON in request body'})
            }
        except Exception as e:
            logger.error(f"Error processing request: {str(e)}")
            return {
                'statusCode': 500,
                'body': json.dumps({'error': f'Internal server error: {str(e)}'})
            }
    
    return {
        'statusCode': 405,
        'body': json.dumps({'error': 'Method not allowed'})
    } 