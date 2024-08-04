#!/usr/bin/env python3
import bcrypt


def hash_password(password: str) -> str:
    """This function a hashed password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
