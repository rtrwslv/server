from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

@app.route('/rpc', methods=['POST'])
def rpc():
    data = request.json
    method = data['method']
    
    if method == 'summ':
        return jsonify(summ(data['data']['args']))
    else:
        return jsonify({"error": "Method not found"}), 404

def summ(args):
    return {"result": sum(args)}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
