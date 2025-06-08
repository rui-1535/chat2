# チャットAI

このプロジェクトは、OpenAIのGPTモデルを使用したチャットAIを実装しています。ウェブ検索機能と会話履歴の保存機能を備えています。

## 機能

- 自然な会話が可能
- ウェブ検索機能
- 会話履歴の保存と参照
- ユーザーとの対話を通じた学習

## デモ

[デモサイト](https://your-netlify-url.netlify.app)で実際に試すことができます。

## セットアップ

### 前提条件

- Python 3.9以上
- OpenAI APIキー
- SerpAPI APIキー（オプション：ウェブ検索機能を使用する場合）

### インストール

1. リポジトリをクローン:
```bash
git clone https://github.com/rui-1535/chat1.git
cd chat1
```

2. 必要なパッケージのインストール:
```bash
pip install -r requirements.txt
```

3. 環境変数の設定:
`.env`ファイルを作成し、以下の変数を設定してください：
```
OPENAI_API_KEY=your_openai_api_key
SERPAPI_API_KEY=your_serpapi_api_key
```

### 使用方法

1. ローカルでの実行:
```bash
python app.py
```

2. ブラウザでアクセス:
```
http://localhost:5000
```

## Netlifyへのデプロイ

1. Netlifyアカウントを作成
2. このリポジトリをNetlifyに接続
3. 以下の環境変数を設定:
   - `OPENAI_API_KEY`
   - `SERPAPI_API_KEY`
4. デプロイを開始

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