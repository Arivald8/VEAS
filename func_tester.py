from src.veas import VEAS

auth = VEAS()

auth.new_user(
    username="Arivald",
    password="Password",
    email="Arivald@Password.com",
    is_admin=True
)

session_id = auth.login("Arivald", "Password")

print(f"SESSION ID: {session_id}")

valid_session = auth.validate_session(session_id)

print(f"SESSION VALID? {valid_session}")





