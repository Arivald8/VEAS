"""
Defines a set of regular expression patterns designed to help validate 
and enforce constraints on usernames, passwords, and email addresses.

Regular Expression Patterns:

- username_chars: A regex pattern for validating usernames. 
                  It matches strings that consist of alphanumeric
                  characters, underscores, and hyphens.

- password_chars: A regex pattern for validating passwords.
                  It matches strings that contain at least one 
                  lowercase letter, one uppercase letter, one number,
                  and one of the specified symbols: !@#$%^&*()_+=-.
                  This pattern enforces strong password requirements.

- email_chars:    A regex pattern for validating email addresses. 
                  It matches strings that adhere to a typical email 
                  format, including local part and domain part, 
                  and ensures proper characters and structure.

These regular expression patterns are designed to help validate and enforce constraints on usernames, passwords, and email addresses in your application. They can be used in conjunction with Python's 're' module for attribute validation.

"""



username_chars = "^[a-zA-Z0-9_-]*$"
password_chars = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+=-]).*$"
email_chars = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
