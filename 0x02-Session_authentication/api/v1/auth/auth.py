#!/usr/bin/env python3
"""Doc of the auth module"""
from flask import request
from typing import List, TypeVar
import re
import os
"""All the import"""


class Auth:
    """DOc of the class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """This function permit to require auth"""
        if excluded_paths is None or not excluded_paths:
            return True
        elif path is None:
            return True
        n_path = path.rstrip('/') + '/'
        for ex_paths in excluded_paths:
            ex_path = ex_paths.rstrip('/') + '/'
            if ex_path == n_path:
                return False
        for ex_path in excluded_paths:
            expr = ex_path.rstrip('*') + '.*'
            if re.match(expr, path):
                return False
        return True

    def authorization_header(self, req=None) -> str:
        """This function permit to add an authorization header"""
        if req is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """Handle the current user"""
        return None

    def session_cookie(self, request=None):
        """This function return the cookie value"""
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        cookie_value = request.cookies.get(session_name, None)
        return cookie_value
