import os
import yaml
from flask import Flask, jsonify, request, Response
from flask_restful import Resource, Api
from flask_cors import CORS

# アプリケーション設定
app = Flask(__name__)
CORS(app)
api = Api(app)


# リクエスト・レスポンスのスキーマ定義
from schemas import (
    GetTodoResponse,
    PostTodoRequest,
    PostTodoResponse,
)


@app.route("/.well-known/ai-plugin.json")
def plugin_manifest():
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return Response(text, content_type="application/json")


@app.route('/openapi.yaml')
def serve_openapi_yaml():
    with open(os.path.join(os.path.dirname(__file__), 'openapi.yaml'), 'r') as f:
        yaml_data = f.read()
    yaml_data = yaml.load(yaml_data, Loader=yaml.FullLoader)
    return jsonify(yaml_data)



todos = ['todo1', 'todo2', 'todo3']


# エンドポイントの定義
class Todos(Resource):
    def get(self):
        return GetTodoResponse(todos=todos).dict()
    
    def post(self):
        req = request.get_json()
        data = PostTodoRequest(**req)
        todos.append(data.todo)

        return PostTodoResponse(todos=todos).dict()


# エンドポイントの追加
api.add_resource(Todos, '/todos')

# サーバー起動
if __name__ == '__main__':
    app.run(debug=True)