import sqlite3

try:
    import src.strings.queries as query
    import src.strings.errors as error
    from src.managers.auth import Auth

except ModuleNotFoundError:
    import strings.queries as query
    import strings.errors as error
    from managers.auth import Auth


class DB:
    def __init__(self, db_type="sqlite", db_name="database.db") -> None:
        self.db_type = db_type
        self.db_name = db_name
        self.auth = Auth()
        self.connection = None
        self.cursor = None
        self.connect()


    def connect(self):
        if self.db_type == "sqlite":
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
        else:
            raise ValueError("Unsupported database type")
        

    def close(self) -> None:
        if self.connection:
            self.connection.close()


    def initialize_database(self, name=None) -> None:
        if name:
            self.db_name = name
        self.connect()


    def table_exists(self, name=None) -> bool:
        self.cursor.execute(query.table_exists, (name, ))
        return self.cursor.fetchone() is not None


    def create_user_table(self) -> None:
        self.cursor.execute(query.create_user_table)
        self.connection.commit()


    def create_user(self, username, password, email, is_admin, created) -> None:
        pass_hash = self.auth.hash_password(password)
        
        try:
            self.cursor.execute(
                query.create_user, 
                (username,
                pass_hash, 
                email, 
                is_admin,
                created) 
            )
            self.connection.commit()
        except sqlite3.IntegrityError as e:
            if 'UNIQUE constraint failed' in str(e):
                print(error.username_taken)
            else:
                raise

    
    def create_session_table(self) -> None:
        self.cursor.execute(query.create_session_table)
        self.connection.commit()

    
    def create_session(self, session_id, username, expiration_time) -> None:
        try:
            self.cursor.execute(query.create_session, (session_id, username, expiration_time))
            self.connection.commit()
        except sqlite3.IntegrityError as e:
            if 'UNIQUE constraint failed' in str(e):
                raise ValueError(error.session_exists_for_user)
            else:
                raise


    def get_session(self, session_id) -> tuple:
        self.cursor.execute(query.get_session, (session_id,))
        return self.cursor.fetchone()
    

    def get_session_by_username(self, username):
        self.cursor.execute(query.get_session_by_username, (username,))
        session = self.cursor.fetchone()
        return session[0] if session else None
    

    def delete_session(self, session_id) -> None:
        self.cursor.execute(query.delete_session, (session_id,))
        self.connection.commit()

    
    def update_session_expiration(self, session_id, expiration_time):
        self.cursor.execute(query.update_session_expiration, (expiration_time, session_id))
        self.connection.commit()


    def read_user(self, user_id=None, username=None) -> tuple:
        if user_id:
            self.cursor.execute(query.read_user_where_id, (user_id,))

        elif username:
            self.cursor.execute(query.read_user_where_username, (username,))
        
        else:
            raise ValueError(error.invalid_read_user_args)

        return self.cursor.fetchone()


    def update_user(
            self, 
            user_id=None, 
            username=None, 
            password=None, 
            email=None, 
            is_admin=None
        ) -> None:
        
        query_str = query.update_user
        params = []

        if username:
            query_str += query.username
            params.append(username)

        if password:
            query_str += query.password
            params.append(password)

        if email:
            query_str += query.email
            params.append(email)

        if is_admin is not None:
            query_str += query.is_admin
            params.append(is_admin)

        query_str = query_str.rstrip(', ')
        query_str += query.where_id
        params.append(user_id)

        self.cursor.execute(query_str, tuple(params))
        self.connection.commit()

    