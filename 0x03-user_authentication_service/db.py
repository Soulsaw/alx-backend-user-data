#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User
"""Requiered import"""


class DB:
    """DB class
    """
    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database and return the User object

        Args:
            email (str): The email of the user
            hashed_password (str): The hashed password of the user

        Returns:
            User: The created user object
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs: dict) -> User:
        """Find an existing user with a arbitrary keyword

        Args:
                kwargs (dict): A dictionary with the argument

        Returns:
                User: The match user or None
        """
        try:
            query = self._session.query(User)
            for key, value in kwargs.items():
                column = getattr(User, key, None)
                if column is None:
                    raise InvalidRequestError
                query = query.filter(column == value)
            result = query.one()
            return result
        except NoResultFound:
            raise NoResultFound
        except InvalidRequestError:
            raise InvalidRequestError

    def update_user(self, user_id: int, **kwargs: dict) -> None:
        """Update the giving user by his id

        Args:
            user_id (int): The user id
            kwargs (dict): The attribute to update

        Returns:
                None
        """
        user = self.find_user_by(id=user_id)
        if user is None:
            raise ValueError
        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError
            setattr(user, key, value)
        try:
            self._session.commit()
        except Exception:
            self._session.rollback()
