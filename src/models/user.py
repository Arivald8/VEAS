from datetime import datetime

class User:
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
    def __init__(
        self, 
        username=None, 
        password=None, 
        email=None, 
        is_admin=None,
        created=datetime.now()
    ):
        self.created = created
        self.username = username
        self.password = password
        self.email = email
        self.is_admin = is_admin
        self.created = created


    def __str__(self):
        return f"""Username: {self.username} \nAdmin: {self.is_admin} \nCreated: {self.created}"""

    