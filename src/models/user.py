"""
User Model definition for the authentication system

This module defines the User class, represeting a user in the authentication system.
It icludes user attributes, methods for authentication, authorization and user data.

Attributes:
    - Username (str): A unique username.
    - Password (str): The securely hashed password for user authentication.
    - Email (Optional) (str): The email address associate with the user.
    - is_admin (bool): Indicated whether the user has admin privileges.
    - created (datetime): The date and time when the user registered.

Methods:
    - authenticate(password): Verify the user's password for authentication. 
    - has_permission(permission): Check if the user has a specific permission.
    - update_profile(new_data): Update user profile information.
    - change_password(new_password): Change the user's password securely.
    - generate_reset_token(): Generate a token for password reset. 

Constraints:
    Username:
        - Maximum length: 50 characters
        - Must be unique
        - Can only contain alphanumeric characters, underscores and hyphens
    Password:
        - Minimum length: 8 characters
        - Must contain at least one uppercase, lowercase, number and symbol
    Email:
        - Must be a valid email address.
        - Must be unique.

Author: Arivald8
Created: 25th Oct 2023
Edited: 26th Oct 2023
"""

from strings import errors as error
from strings import re_patterns as match

from datetime import datetime
from typing import Any
import re


class User:
    ATTR_TYPES = {
            "username": str,
            "password": str,
            "email": str,
            "is_admin": bool,
            "created": datetime
        }
    

    def _validate_username(username) -> None:
        if len(username) > 50:
            raise ValueError(error.username_length)
        if not re.match(match.username_chars, username):
            raise ValueError(error.invalid_username)
    

    def _validate_password(password) -> None:
        if len(password) < 8:
            raise ValueError(error.password_length)
        if not re.match(
            match.password_chars, password):
            raise ValueError(error.invalid_password)


    def _validate_email(email):
        if not re.match(match.email_chars, email):
            raise ValueError(error.invalid_email)


    def __init__(
        self, 
        username: str = "", 
        password: str = "", 
        email: str = "", 
        is_admin: bool = False,
        created: datetime = datetime.now()
    ):
        self.username = username
        self.password = password
        self.email = email
        self.is_admin = is_admin
        self.created = created


    def __str__(self) -> str:
        return f"Username: {self.username} \nAdmin: {self.is_admin} \nCreated: {self.created}"
    

    def __repr__(self):
        return f"User(username={self.username!r}, is_admin={self.is_admin!r}, created={self.created!r})"

    
    def __setattr__(self, name: str, value: Any) -> None:
        """
        This method is called unconditionally when an attribute is set
        on an object of the User class.

        name: type str: Name of the attribute to set the value for.
        value: multiple types: Value to be set for the named attribute.

        Checks if value has the valid type to be assigned. Types are mapped
        in ATTR_TYPES.
        """
        if not isinstance(value, self.ATTR_TYPES[name]):
            raise TypeError(error.incorrect_type(self.ATTR_TYPES, value, name))
        else:
            super().__setattr__(name, value)


    def __getattribute__(self, name: str) -> Any:
        """
        This method is called unconditionally when an attribute is accessed
        on an object. It takes the name of the attribute as an argument and
        returns the value of the attribute. 
    
        This will be used to implement custom attribute access behavior, but
        more specifically it will implement attribute access logging. Each
        attribute access will be logged to an external file for monitoring. 
        """
        return super().__getattribute__(name)