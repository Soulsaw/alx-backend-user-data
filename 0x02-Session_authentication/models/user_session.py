#!/usr/bin/env python3
""" UserSession module
"""
import hashlib
from models.base import Base
"""Impor modules"""


class UserSession(Base):
    """Module doc"""
    def __init__(self, *args: list, **kwargs: dict):
        """Init method implementation"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
