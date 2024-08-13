#!/usr/bin/env python3
"""Doc of the auth module"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid
"""Required import"""


class Auth:
    """Auth class to interact with the authentication database.
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a user in the database

        Args:
            email (str): The user email
            password (str): The user giving password

        Returns:
                User: Return the user object instance
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {email} already exists.")
        except NoResultFound:
            hashed = _hash_password(password)
            user = self._db.add_user(email=email, hashed_password=hashed)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """Valid the user login

        Args:
            email (str): The user email
            password (str): The user password

        Returns:
            bool: True or False
        """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode(), user.hashed_password):
                return True
            else:
                return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Return the session id with a giving email

        Args:
            email (str): The user email

        Returns:
                session_id (str): Return the user session id
        """
        try:
            user = self._db.find_user_by(email=email)
            session_token = _generate_uuid()
            self._db.update_user(user.id, session_id=session_token)
            return session_token
        except NoResultFound:
            return None


def _hash_password(password: str) -> bytes:
    """Take a password as argument in return a bytes

    Args:
        password (str): The password to hash
    Returns:
        bytes: The bytes representation of the password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Retturn the string representation of a uuid

    Return:
            str: uuid in a string format
    """
    return str(uuid.uuid4())
