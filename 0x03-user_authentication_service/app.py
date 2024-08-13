#!/usr/bin/env python3
"""Doc of the app module"""
from flask import Flask, jsonify, request, abort, url_for, redirect
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


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """Handle the login function"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if AUTH.valid_login(email, password):
            session_id = AUTH.create_session(email)
            resp = jsonify({"email": email, "message": "logged in"})
            resp.set_cookie("session_id", session_id)
            return resp
        else:
            abort(401)


@app.route('/sessions', method='DELETE', strict_slashes=False)
def logout():
    """Implement the logout method"""
    if request.method == 'DELETE':
        session_id = request.cookies.get('Cookie', None)
        if session_id is None:
            abort(403)
        user = AUTH.get_user_from_session_id(session_id)
        if user is not None:
            AUTH.destroy_session(user.id)
            return redirect(url_for('home'))
        else:
            abort(403)


if __name__ == "__main__":
    """Doc of the main function"""
    app.run(host="0.0.0.0", port="5000")
