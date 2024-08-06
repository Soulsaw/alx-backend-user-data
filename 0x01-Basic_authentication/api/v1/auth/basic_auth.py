#!/usr/bin/env python3
"""Doc of the module"""
from api.v1.auth.auth import Auth
import base64
from typing import Tuple
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
        return (credentials[0], credentials[1])
