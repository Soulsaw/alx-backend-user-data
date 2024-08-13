#!/usr/bin/env python3
"""Doc of the app module"""
from flask import Flask, jsonify
"""Required import"""
app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    """Doc of the home page"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    """Doc of the main function"""
    app.run(host="0.0.0.0", port="5000")
