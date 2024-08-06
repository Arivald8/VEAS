from models.user import User
from managers.db import DB

class VEAS:
    def __init__(self):
        self.db = DB( )
        self.db.initialize_database()
        if not self.db.table_exists("User"):
            self.db.create_user_table()


    def new_user(self, username, password, email, is_admin):
        user = User(username, password, email, is_admin)
        user.create(self.db)


    def get_user(self, user_id=None, username=None):
        user_data = self.db.read_user(username=username)
        print(type(user_data))
        print(user_data)




v = VEAS()
v.get_user("tester")
