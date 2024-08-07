#!/usr/bin/env python3
"""Doc of the SessionAuth module"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid
"""All the required import for the module"""


class SessionAuth(Auth):
    """Implementation of the session_auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """This function create an user session"""
        if user_id is None or type(user_id) is not str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """This function return the user id for the giving session id"""
        if session_id is None or type(session_id) is not str:
            return None
        user_id = self.user_id_by_session_id.get(session_id, None)
        return user_id

    def current_user(self, request=None):
        """This function will overided the current_user parent function"""
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """This function permit to logout with the current user"""
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False
        del self.user_id_by_session_id[session_id]
        return True
