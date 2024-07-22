from models.user import User
from managers.db import DB

class VEAS:
    def __init__(self):
        self.db = DB("sqlite")
        self.db.initialize_database()
        if not self.db.table_exists("User"):
            self.db.create_user_table()

    def new_user(self, username, password, email, is_admin):
        user = User(username, password, email, is_admin)
        


v = VEAS()

v.new_user("tester", "tester", "tester@tester.com", True)
