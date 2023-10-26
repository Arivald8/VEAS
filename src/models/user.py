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


from datetime import datetime
from typing import Any
import re


class User:
    def _validate_username(username) -> None:
        if len(username) > 50:
            raise ValueError("Username must be no more than 50 characters.")

        if not re.match("^[a-zA-Z0-9_-]*$", username):
            raise ValueError(
                "Username can only contain alphanumeric characters, underscores, and hyphens.")
    

    def _validate_password(password) -> None:
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters.")

        if not re.match(
            "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+=-]).*$", password):
            raise ValueError(
                "Password must contain at least one uppercase, one lowercase, one number, and one symbol.")


    def _validate_email(email):
        if not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            raise ValueError("Email address is not valid.")

    def __init__(
        self, 
        username: str = "", 
        password: str = "", 
        email: str = "", 
        is_admin: bool = False,
        created: datetime = datetime.now()
    ):
        self.created = created
        self.username = username
        self.password = password
        self.email = email
        self.is_admin = is_admin
        self.created = created


    def __str__(self) -> str:
        return f"Username: {self.username} \nAdmin: {self.is_admin} \nCreated: {self.created}"

    
    def __setattr__(self, __name: str, __value: Any) -> None:
        attr_types = {
            "username": str,
            "password": str,
            "email": str,
            "is_admin": bool,
            "created": datetime
        }

        if not isinstance(__value, attr_types[__name]):
            raise ValueError(
                f"""
                Incorrect instance type {type(__value)} provided to attribute {__name}.
                Attribute {__name} should be of type {attr_types[__name]}
                """)
        else:
            super().__setattr__(__name, __value)



    def __getattribute__(self, __name: str) -> Any:
        """
        This method is called unconditionally when an attribute is accessed
        on an object. It takes the name of the attribute as an argument and
        returns the value of the attribute. 
    
        This will be used to implement custom attribute access behavior, but
        more specifically it will implement attribute access logging. Each
        attribute access will be logged to an external file for monitoring. 
        """
        return super().__getattribute__(__name)