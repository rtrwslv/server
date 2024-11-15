from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Конфигурации сервисов
rpc_gateway_url = "http://rpc_gateway:5001"
static_gateway_url = "http://static_gateway:80"

@app.route('/rpc', methods=['POST'])
def rpc():
    data = request.json
    response = requests.post(rpc_gateway_url + "/rpc", json=data)
    return jsonify(response.json()), response.status_code

@app.route('/static', methods=['GET'])
def static_content():
    response = requests.get(static_gateway_url + "/static")
    return response.content, response.status_code

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
