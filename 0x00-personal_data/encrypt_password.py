#!/usr/bin/env python3
"""This allow us to run the file like command"""
import bcrypt
"""Import the modules"""


def hash_password(password: str) -> bytes:
    """This function a hashed password"""
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """This function check if the password match"""
    return bcrypt.checkpw(password.encode(), hashed_password)
