"""
User Model definition for the authentication system

This module defines the User class, represeting a user in the authentication system.
It icludes user attributes, methods for authentication, authorization and user data.

Attrs:
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

Author: Arivald8
Date: 25th Oct 2023
"""


from datetime import datetime
from typing import Any


class User:
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
            print(f"__value {__value} and attr {__name}")
            raise ValueError(
                f"""
                Incorrect instance type {type(__value)} provided to attribute {__name}.
                Attribute {__name} should be of type {attr_types[__name]}
                """
            )
            
        else:
            super().__setattr__(__name, __value)