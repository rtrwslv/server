from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/summ', methods=['POST'])
def summ():
    data = request.json
    result = sum(data['args'])
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
