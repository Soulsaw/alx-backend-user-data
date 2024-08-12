#!/usr/bin/env python3
"""Doc of the SessionDBAuth module"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
"""All the required import for the module"""


class SessionDBAuth(SessionExpAuth):
    """Module documentation"""
    def create_session(self, user_id=None):
        """Create and store the new instance of user_id"""
        if user_id is None:
            return None
        session_id = super().create_session(user_id)
        kwargs = {'user_id': user_id, 'session_id': session_id}
        user_session = UserSession(**kwargs)
        user_session.save()
        return user_session.session_id

    def user_id_for_session_id(self, session_id=None):
        """Retrieve the user_id"""
        UserSession.load_from_file()
        user_id = super().user_id_for_session_id(session_id)
        return user_id

    def destroy_session(self, request=None):
        """Delete the session"""
        super().destroy_session(request)
