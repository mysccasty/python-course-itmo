"""Сервер запускается на localhost на 5000 порту"""
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))

    result = a + b

    response = {
        "function": "add",
        "description": "adds two numbers",
        "parameters": {
            "a": a,
            "b": b
        },
        "result": result
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)