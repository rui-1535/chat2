import os
import json
import datetime
from typing import List, Dict
import openai
from dotenv import load_dotenv
from serpapi import GoogleSearch

# 環境変数の読み込み
load_dotenv()

# APIキーの設定
openai.api_key = os.getenv("OPENAI_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

class ChatAI:
    def __init__(self):
        self.conversation_history: List[Dict] = []
        self.history_file = "conversation_history.json"
        self.load_history()

    def load_history(self):
        """会話履歴を読み込む"""
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    self.conversation_history = json.load(f)
        except Exception as e:
            print(f"履歴の読み込み中にエラーが発生しました: {e}")
            self.conversation_history = []

    def save_history(self):
        """会話履歴を保存する"""
        try:
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(self.conversation_history, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"履歴の保存中にエラーが発生しました: {e}")

    def search_web(self, query: str) -> str:
        """ウェブ検索を実行する"""
        try:
            search = GoogleSearch({
                "q": query,
                "api_key": SERPAPI_API_KEY
            })
            results = search.get_dict()
            
            if "organic_results" in results:
                return "\n".join([result.get("snippet", "") for result in results["organic_results"][:3]])
            return "検索結果が見つかりませんでした。"
        except Exception as e:
            return f"検索中にエラーが発生しました: {e}"

    def get_ai_response(self, user_input: str) -> str:
        """AIの応答を生成する"""
        try:
            # 会話履歴の準備
            messages = [
                {"role": "system", "content": "あなたは親切で役立つアシスタントです。"}
            ]
            
            # 過去の会話を追加
            for msg in self.conversation_history[-5:]:  # 直近5つの会話のみ使用
                messages.append(msg)

            # ユーザーの入力を追加
            messages.append({"role": "user", "content": user_input})

            # 検索が必要かどうかを判断
            if "検索" in user_input or "調べて" in user_input:
                search_query = user_input.replace("検索", "").replace("調べて", "").strip()
                search_results = self.search_web(search_query)
                messages.append({"role": "system", "content": f"検索結果: {search_results}"})

            # OpenAI APIを使用して応答を生成
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )

            ai_response = response.choices[0].message.content

            # 会話履歴に追加
            self.conversation_history.append({"role": "user", "content": user_input})
            self.conversation_history.append({"role": "assistant", "content": ai_response})
            
            # 履歴を保存
            self.save_history()

            return ai_response

        except Exception as e:
            return f"応答の生成中にエラーが発生しました: {e}"

def main():
    chat_ai = ChatAI()
    print("チャットAIが起動しました。'quit'と入力して終了できます。")
    
    while True:
        user_input = input("\nあなた: ").strip()
        
        if user_input.lower() == 'quit':
            print("チャットを終了します。")
            break
            
        response = chat_ai.get_ai_response(user_input)
        print(f"\nAI: {response}")

if __name__ == "__main__":
    main() 