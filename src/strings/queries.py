table_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name=?"

create_user_table = """
    CREATE TABLE IF NOT EXISTS User (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        is_admin BOOLEAN NOT NULL,
        created TEXT NOT NULL
    )"""

create_user = """
    INSERT INTO User (username, password, email, is_admin, created)
    VALUES (?, ?, ?, ?, ?)
    """

read_user_where_username = "SELECT * FROM User WHERE username = ?"
read_user_where_id = "SELECT * FROM User WHERE id = ?"

update_user = "UPDATE User SET "
username = "name = ?, "
password = "password = ?, "
email = "email = ?, "
is_admin = "is_admin = ?, "
where_id = " WHERE id = ?"

