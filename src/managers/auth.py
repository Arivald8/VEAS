import hashlib
import uuid

class Auth:
    def __init__(self, password_hash=None, password=""):
        self.password_hash = password_hash or self.hash_password(password)

    def hash_password(self, password):
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
    def check_password(self, stored_password_hash, password):
        password_hash, salt = stored_password_hash.split(':')
        return password_hash == hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    