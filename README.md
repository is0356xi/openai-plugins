# openai-plugins

- envファイルを用意

```sh:.env
AZURE_OPENAI_API_KEY="APIキー"
AZURE_OPENAI_ENDPOINT="エンドポイント"
AZURE_OPENAI_API_VERSION="2023-03-15-preview"
AZURE_OPENAI_DEPLOYMENT_NAME="gpt-35-turbo"
```

- プラグイン公開サーバの起動

```sh:
pip install -r ./requirements.txt
python app.py
```

- 実行テスト
    - ```plugin_call_test_langchain.ipynb```に従って実行

