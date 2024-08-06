table_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name=?"

create_user_table = """
    CREATE TABLE IF NOT EXISTS User (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        is_admin BOOLEAN NOT NULL,
        created TEXT NOT NULL
    )"""

create_session_table = """
    CREATE TABLE IF NOT EXISTS session (
        session_id TEXT PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        expiration_time TIMESTAMP NOT NULL,
        FOREIGN KEY (username) REFERENCES user(username)

    )"""

create_user = """
    INSERT INTO User (username, password, email, is_admin, created)
    VALUES (?, ?, ?, ?, ?)
    """

create_session = """
    INSERT INTO session (session_id, username, expiration_time)
    VALUES (?, ?, ?)
    """

get_session = """
    SELECT username, expiration_time
    FROM session
    WHERE session_id = ?
    """

get_session_by_username = """
    SELECT session_id
    FROM session
    WHERE username = ?
    """

delete_session = """
    DELETE FROM session
    WHERE session_id = ?
    """

update_session_expiration = """
    UPDATE session
    SET expiration_time = ?
    WHERE session_id = ?
    """

read_user_where_username = "SELECT * FROM User WHERE username = ?"
read_user_where_id = "SELECT * FROM User WHERE id = ?"

update_user = "UPDATE User SET "
username = "username = ?, "
password = "password = ?, "
email = "email = ?, "
is_admin = "is_admin = ?, "
where_id = " WHERE id = ?"

