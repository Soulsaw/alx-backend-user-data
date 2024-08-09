#!/usr/bin/env python3
""" Module of Users views
"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models.user import User
import os
"""The require import"""


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login():
    """This function return"""
    email = request.form.get('email', None)
    pwd = request.form.get('password', None)
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    if pwd is None or pwd == "":
        return jsonify({"error": "password missing"}), 400
    user = User.search({"email": email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    if not user[0].is_valid_password(pwd):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    cookie_token = auth.create_session(user[0].id)
    output = jsonify(user[0].to_json())
    session_name = os.getenv("SESSION_NAME")
    output.set_cookie(session_name, cookie_token)
    return output


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def session_logout():
    """This method permit to logout the current user"""
    from api.v1.app import auth
    destroy_session = auth.destroy_session(request)
    if destroy_session is False:
        abort(404)
    else:
        return jsonify({}), 200
