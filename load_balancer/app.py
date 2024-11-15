from flask import Flask, send_from_directory, jsonify

app = Flask(__name__)
STATIC_FOLDER = "./static_gateway/static"

@app.route('/rpc', methods=['POST'])
def rpc():
    data = request.json
    response = requests.post(rpc_gateway_url + "/rpc", json=data)
    return jsonify(response.json()), response.status_code

@app.route('/static', methods=['GET'])
def static_content():
    try:
        return send_from_directory(STATIC_FOLDER, "main.jpg")
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
