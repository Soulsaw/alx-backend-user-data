#!/usr/bin/env python3
"""Doc of the app module"""
from flask import Flask, jsonify, request
from auth import Auth
"""Required import"""
app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    """Doc of the home page"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """Handle the user post requests"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = AUTH.register_user(email, password)
            return jsonify({"email": user.email, "message": "user created"})
        except ValueError:
            return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    """Doc of the main function"""
    app.run(host="0.0.0.0", port="5000")
