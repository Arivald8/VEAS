try:
    from models.user import User
    from managers.db import DB
    from managers.auth import Auth
    from managers.session import Session

except ModuleNotFoundError:
    from src.models.user import User
    from src.managers.db import DB
    from src.managers.auth import Auth
    from src.managers.session import Session


class VEAS:
    def __init__(self):
        self.session = Session()
        self.db = DB()
        self.db.initialize_database()
        if not self.db.table_exists("User"):
            self.db.create_user_table()
        if not self.db.table_exists("session"):
            self.db.create_session_table()


    def new_user(self, username, password, email, is_admin):
        user = User(username, password, email, is_admin)
        user.create(self.db)


    def get_user(self, username=None) -> tuple:
        return self.db.read_user(username=username)


    def authenticate(self, username, password) -> bool:
        auth = Auth(password=password)
        user_record = self.get_user(username=username)
        
        if user_record and auth.check_password(password=password):
            print("User authenticated successfully.")
            return True
        else:
            print("Wrong username or password.")
            return False
        

    def login(self, username, password) -> str:
        """
        -> str: uuid
        """
        if self.authenticate(username, password):
            session_id = self.session.create_session(username)
            expiration_time = self.session.sessions[session_id]['expiration_time']

            try:
                self.db.create_session(session_id, username, expiration_time)
                return session_id
            
            except ValueError as e:
                print(e)
                existing_session_id = self.db.get_session_by_username(username)
                self.db.update_session_expiration(existing_session_id, expiration_time)
                return existing_session_id
        
    
    def logout(self, session_id) -> None:
        self.session.delete_session(session_id)
        self.db.delete_session(session_id)
        print("Logged out successfully")
        

    def get_username_from_session(self, session_id) -> str:
        return self.session.get_username(session_id)
    

    def validate_session(self, session_id):
        session = self.session.sessions.get(session_id)
        if session and self.session._is_session_valid(session):
            return True
        return False



