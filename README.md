# VEAS: Very Easy Authentication System

## Overview
VEAS is a straightforward authentication system designed for user authentication and session handling. It offers a Python-based implementation with core functionalities for user management, session management and password hashing. 

## Features
* User creation and management
* Password hashing and validation
* Session creation, validation and management
* Integration with SQLite for persistent storage

## Usage
### Initialization
To use VEAS, you need to initialize the main VEAS class. This will set up the database and create necessary tables if they do not exist.

```
from veas import VEAS

veas = VEAS()
```

### User Management
#### Creating a New User

```
veas.new_user("username", "password", "email@example.com", is_admin=False)
```

#### Fetching User Information

```
user_info = vead.get_user("username")
print(user_info)
```

### Authentication
#### Logging In

```
session_id = veas.login("username", "password")
print("Session ID:", session_id)
```

#### Logging Out

```
veas.logout(session_id)
> Logged out successfully
```

### Session Management
#### Validate Session

```
is_valid = veas.validate_session(session_id)
print(is_valid)
```

#### Get Username from Session

```
username = veas.get_username_from_session(session_id)
```

## Testing
The project uses 'unittest' for testing.
To run the tests, use:

```
python -m unittest
```

## Modules

### src.models.user.py
Defines the 'User' model, including validation for username, password and email attributes.

### src/managers/db.py
Handles database operations including creating user and session tables, and CRUD operations for users and sessions.

### src/managers/auth.py
Manages password hashing and validation.

### src/managers/session.py
Manages session creation, validation, and deletion. Sessions are stored in-memory and validated against expiration times.

### src/veas.py
The main entry point for VEAS, integrating user management, authentication, and session handling.

## Example

```
from veas import VEAS

veas = VEAS()

# Create a new user
veas.new_user("testuser", "Password123", "testuser@example.com", False)

# Log in the user and obtain a session ID
session_id = veas.login("testuser", "Password123")
print("Session ID:", session_id)

# Validate the session
is_valid = veas.validate_session(session_id)
print("Is session valid?", is_valid)

# Get the username from the session ID
username = veas.get_username_from_session(session_id)
print("Username:", username)

# Log out the user
veas.logout(session_id)
print("Logged out successfully")
```

## License
This project is licensed under the MIT License. See the 'LICENSE' file for details.





