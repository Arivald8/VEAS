import builtins

def incorrect_type(type_lookup, *args):
    return f"""
            Incorrect instance type {type(args[0])} provided to attribute {args[1]}.
            Attribute {args[1]} should be of type ({type_lookup[args[1]]}
            """


def compose(error_name, error_string):
    raise getattr(builtins, error_name)(error_string)


username_length = "Username must be no more than 50 characters."
password_length = "Password must be at least 8 characters."
invalid_username =  "Username can only contain alphanumeric characters, underscores, and hyphens."
invalid_password = "Password must contain at least one uppercase, one lowercase, one number, and one symbol."
invalid_email = "Email address is not valid."