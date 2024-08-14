#!/usr/bin/env python3
"""
Main file
"""
import requests
"""Requiered import"""


def register_user(email: str, password: str) -> None:
    """Permit to register a user"""
    url = 'http://localhost:5000/users'
    data = {"email": email, "password": password}
    req = requests.post(url, data=data)
    assert req.status_code == 200, {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Try to log in with a wrong password"""
    url = 'http://localhost:5000/sessions'
    data = {"email": email, "password": password}
    req = requests.post(url, data=data)
    assert req.status_code == 401


def log_in(email: str, password: str) -> str:
    """Login a user with the rigth credentials"""
    url = 'http://localhost:5000/sessions'
    data = {"email": email, "password": password}
    req = requests.post(url, data=data)
    assert req.status_code == 200


def profile_unlogged() -> None:
    """Try the user unlogged profile"""
    url = 'http://localhost:5000/profile'
    req = requests.get(url, cookies=dict(session_id='fake_session_id'))
    assert req.status_code == 403


def profile_logged(session_id: str) -> None:
    """The logged user profile"""
    url = 'http://localhost:5000/profile'
    cookies = dict(session_id=session_id)
    req = requests.get(url, cookies=cookies)
    assert req.status_code == 200


def log_out(session_id: str) -> None:
    """Logout the log in user"""
    url = 'http://localhost:5000/sessions'
    cookies = dict(session_id=session_id)
    req = requests.delete(url, cookies=cookies)
    assert req.status_code == 200, {"message": "Bienvenue"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
