from flask import jsonify


def get():
    return jsonify({"message": "Hello, teste controller "})
