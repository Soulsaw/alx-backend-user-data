#!/usr/bin/env python3
"""Doc of the SessionExpAuth module"""
from api.v1.auth.session_auth import SessionAuth
import os
from datetime import datetime, timedelta
"""All the required import for the module"""
session_time = os.getenv('SESSION_DURATION')


class SessionExpAuth(SessionAuth):
    """The documentation for the class"""
    def __init__(self):
        """Documentation for the __init__ method"""
        super().__init__()
        try:
            self.session_duration = int(os.getenv('SESSION_DURATION', 0))
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Overload the create session"""
        session_id = super().create_session(user_id)
        session_dictionary = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Overload the user_id_for_session method"""
        if session_id is None:
            return None
        session_dictionary = self.user_id_by_session_id.get(session_id, None)
        if session_dictionary is None:
            return None
        if self.session_duration <= 0:
            return session_dictionary.get('user_id', None)
        created_at = session_dictionary.get('created_at', None)
        if created_at is None:
            return None
        expiration_time = created_at + timedelta(seconds=self.session_duration)
        if datetime.now() > expiration_time:
            return None
        return session_dictionary.get('user_id', None)
