import hashlib
import uuid

class Auth:
    def __init__(self, user=None, password=""):
        self.user = user
        self.password_hash = self.hash_password(password)

    def hash_password(self, password):
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
    def check_password(self, password):
        password_hash, salt = self.password_hash.split(':')
        return password_hash == hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    