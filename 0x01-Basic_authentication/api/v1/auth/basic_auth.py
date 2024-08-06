#!/usr/bin/env python3
"""Doc of the module"""
from api.v1.auth.auth import Auth
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
