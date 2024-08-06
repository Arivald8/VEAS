"""
Function and variable definitions used for validation rules and error messages.

Funcs:
- incorrect_type(type_lookup, *args): 

This function takes a dictionary 'type_lookup' and two arguments, 
and it returns a formatted string describing an incorrect instance
type being provided to a specific attribute. It also indicates the
expected type for that attribute based on the 'type_lookup' dictionary.

Vars:
- username_length:  A string describing the validation rule for usernames, 
                    stating that they must be no more than 50 characters.

- password_length:  A string describing the validation rule for passwords,
                    indicating that they must be at least 8 characters.

- invalid_username: A string describing the validation rule for usernames, 
                    specifying that they can only contain alphanumeric 
                    characters, underscores, and hyphens.

- invalid_password: A string describing the validation rule for passwords, 
                    stating that they must contain at least one uppercase 
                    letter, one lowercase letter, one number, and one symbol.

- invalid_email:    A string describing the validation rule for email addresses,
                    indicating that they should be valid.

Author: Arivald8
Created: 31st Oct 2023
"""


def incorrect_type(type_lookup, *args):
    return f"""
            Incorrect instance type {type(args[0])} provided to attribute {args[1]}.
            Attribute {args[1]} should be of type ({type_lookup[args[1]]}
            """


username_length = "Username must be no more than 50 characters."
password_length = "Password must be at least 8 characters."
invalid_username =  "Username can only contain alphanumeric characters, underscores, and hyphens."
invalid_password = "Password must contain at least one uppercase, one lowercase, one number, and one symbol."
invalid_email = "Email address is not valid."

invalid_read_user_args = "You can provide either user id, or username, but not both."
no_read_user_args = "You must provide a username, or user id."

email_already_exists = "This email already exists. You must provide a unique email address."