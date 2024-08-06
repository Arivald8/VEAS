import sqlite3
from pathlib import Path

import src.strings.queries as query
import src.strings.errors as error


class DB:
    def __init__(self, db_type="sqlite", db_name="database.db"):
        self.db_type = db_type
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.connect()


    def connect(self):
        if self.db_type == "sqlite":
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
        else:
            raise ValueError("Unsupported database type")
        

    def close(self):
        if self.connection:
            self.connection.close()


    def initialize_database(self, name=None):
        if name:
            self.db_name = name
        self.connect()


    def table_exists(self, name=None) -> bool:
        self.cursor.execute(query.table_exists, (name, ))
        return self.cursor.fetchone() is not None


    def create_user_table(self):
        self.cursor.execute(query.create_user_table)
        self.connection.commit()

    
    def create_user(self, username, password, email, is_admin, created):
        self.cursor.execute(
            query.create_user, 
            (username,
            password, 
            email, 
            is_admin,
            created) 
        )
        self.connection.commit()


    def read_user(self, user_id=None, username=None):
        def wrong_args():
            raise ValueError(error.invalid_read_user_args)
        
        def no_args():
            raise ValueError(error.no_read_user_args)
        
        def id_provided():
            self.cursor.execute(query.read_user_where_id)

        def username_provided():
            self.cursor.execute(query.read_user_where_username)

        conditions = {
            (user_id is not None, username is not None): lambda: wrong_args,
            (user_id is not None, username is None): lambda: id_provided,
            (user_id is None, username is not None): lambda: username_provided,
            (user_id is None, username is None): no_args
        }

        conditions[(user_id is not None, username is not None)]()
        return self.cursor.fetchone()


    def update_user(self, user_id=None, username=None, password=None, email=None, is_admin=None):
        query_str = ""
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

        print(tuple(params))
        # self.cursor.execute(query_str, tuple(params))
        # self.connection.commit()

    