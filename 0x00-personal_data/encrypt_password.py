#!/usr/bin/env python3
import bcrypt
"""Import the modules"""


def hash_password(password: str) -> str:
    """This function a hashed password"""
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed
