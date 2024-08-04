#!/usr/bin/env python3
"""This allow us to run the file like command"""
import bcrypt
"""Import the modules"""


def hash_password(password: str) -> bytes:
    """This function a hashed password"""
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed
