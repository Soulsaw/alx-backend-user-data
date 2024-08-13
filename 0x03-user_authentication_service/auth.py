#!/usr/bin/env python3
"""Doc of the auth module"""
import bcrypt
"""Require import"""


def _hash_password(password: str) -> bytes:
    """Take a password as argument in return a bytes

    Args:
        password (str): The password to hash
    Returns:
        bytes: The bytes representation of the password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
