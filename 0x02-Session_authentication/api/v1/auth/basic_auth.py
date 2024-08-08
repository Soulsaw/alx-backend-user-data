#!/usr/bin/env python3
"""Doc of the module"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User
"""Import the require modules"""


class BasicAuth(Auth):
    """Doc of the BasicAuth inherit from Auth"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        """Return the Base64 part of the Authorization"""
        if not authorization_header or type(authorization_header) is not str:
            return None
        if authorization_header[:6] != 'Basic ':
            return None
        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """Return the decode of Base64 part of the Authorization"""
        if not base64_authorization_header or\
            type(base64_authorization_header) is not\
                str:
            return None
        try:
            return base64.b64decode(base64_authorization_header).\
                decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """This function return the current user email and password"""
        if not decoded_base64_authorization_header or\
            type(decoded_base64_authorization_header) is not\
                str:
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        credentials = decoded_base64_authorization_header.split(':')
        return (''.join(credentials[:1]), ':'.join(credentials[1:]))

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """Return the user instance base on the email and password"""
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        users = User.search({'email': user_email})
        if not users:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """This method override the initial class method"""
        allow_head = self.authorization_header(req=request)
        if allow_head is None:
            return
        extract_head = self.extract_base64_authorization_header(allow_head)
        decode_head = self.decode_base64_authorization_header(extract_head)
        (email, pwd) = self.extract_user_credentials(decode_head)
        if email is None or pwd is None:
            return
        user = self.user_object_from_credentials(email, pwd)
        if user is None:
            return
        return user
