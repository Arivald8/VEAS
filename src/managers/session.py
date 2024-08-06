import uuid
from datetime import datetime, timedelta

class Session:
    def __init__(self, session_timeout_minutes=30):
        self.sessions = {}
        self.session_timeout_minutes = session_timeout_minutes

    
    def create_session(self, username):
        session_id = str(uuid.uuid4())
        expiration_time = datetime.now() + timedelta(minutes=self.session_timeout_minutes)
        
        self.sessions[session_id] = {
            'username': username,
            'expiration_time': expiration_time
        }

        return session_id
    

    def get_username(self, session_id):
        session = self.sessions.get(session_id)
        if session and self._is_session_valid(session):
            return session['username']
        return None
    

    def _is_session_valid(self, session):
        if datetime.now() > session['expiration_time']:
            self.sessions.pop(session['session_id'], None)
            return False
        return True
    

    def delete_session(self, session_id):
        if session_id in self.sessions:
            self.sessions.pop(session_id)
