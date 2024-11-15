from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

METHODS = {
    'summ': lambda args: {"result": sum(args)},
    'multiply': lambda args: {"result": prod(args)}
}

def prod(args):
    result = 1
    for num in args:
        result *= num
    return result

@app.route('/rpc', methods=['POST'])
def rpc():
    try:
        if not request.is_json:
            raise ValueError("Request must be JSON")

        data = request.json

        if 'method' not in data or 'data' not in data or 'args' not in data['data']:
            raise KeyError("Missing 'method' or 'data' or 'args' fields")

        method = data['method']
        args = data['data']['args']

        if not isinstance(args, list) or not all(isinstance(x, (int, float)) for x in args):
            raise TypeError("'args' must be a list of numbers")

        if method in METHODS:
            return jsonify(METHODS[method](args))
        else:
            return jsonify({"error": f"Method '{method}' not found"}), 404

    except KeyError as e:
        return jsonify({"error": str(e)}), 400
    except TypeError as e:
        return jsonify({"error": str(e)}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        app.logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
