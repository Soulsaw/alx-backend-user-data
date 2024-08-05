#!/usr/bin/env python3
"""Doc of the auth module"""
from flask import request
from typing import List, TypeVar
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
        return True

    def authorization_header(self, request=None) -> str:
        """This function permit to add an authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Handle the current user"""
        return None
