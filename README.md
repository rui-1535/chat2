# AI Chatbot

This is a Python-based AI Chatbot that can engage in conversations and perform web searches using OpenAI's GPT models and SerpAPI.

## Features

- **Interactive Chat**: Engage in natural language conversations with the AI.
- **Web Search Integration**: Ask the AI to search the web for information using keywords like "検索" or "調べて".
- **Conversation History**: Automatically saves and loads conversation history.
- **Secure Password Generator**: A utility script to generate strong, random passwords.

## Setup

### Prerequisites

- Python 3.10 or higher
- OpenAI API Key
- SerpAPI Key

### Installation

1.  **Clone the repository (or download the files):**

    ```bash
    git clone https://github.com/Rui-1535/ai-chatbot.git
    cd ai-chatbot
    ```

2.  **Create a Python virtual environment and activate it:**

    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\Activate.ps1
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up API Keys:**

    Create a file named `.env` in the root directory of the project and add your API keys:

    ```
    OPENAI_API_KEY=YOUR_OPENAI_API_KEY
    SERPAPI_API_KEY=YOUR_SERPAPI_API_KEY
    ```

    You can get your OpenAI API key from [https://platform.openai.com/](https://platform.openai.com/).
    You can get your SerpAPI key from [https://serpapi.com/](https://serpapi.com/).

    *Do not share your `.env` file publicly as it contains sensitive information.*

## Usage

### Running the Chatbot

Make sure your virtual environment is activated, then run:

```bash
python chat_ai.py
```

Type your message at the `あなた:` prompt. Type `quit` to exit.

### Using the Password Generator

Make sure your virtual environment is activated, then run:

```bash
python password_generator.py
```

This will generate a random password with specific requirements (at least 8 characters, one uppercase, one lowercase, one number, one special character).

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## デモ

[デモサイト](https://ai-chatbot-rui.netlify.app)で実際に試すことができます。

## プロジェクト構造

```
chat1/
├── app.py              # メインアプリケーションファイル
├── chat_ai.py          # チャットAIの実装
├── requirements.txt    # 必要なパッケージ
├── runtime.txt         # Pythonバージョン指定
├── netlify.toml        # Netlify設定
├── public/            # 静的ファイル
│   └── index.html     # フロントエンド
└── netlify/
    └── functions/     # サーバーレス関数
        └── chat.py    # チャットAPI
```

## ライセンス

MITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルを参照してください。

## 貢献

1. このリポジトリをフォーク
2. 新しいブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add some amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

## 作者

- Rui-1535

## 謝辞

- OpenAI - GPTモデルの提供
- SerpAPI - ウェブ検索APIの提供
- Netlify - ホスティングプラットフォーム 