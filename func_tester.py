from src.veas import VEAS

v = VEAS()

session_id = v.login("Arivald", "Password")

print(f"SESSION ID: {session_id}")

valid_session = v.validate_session(session_id)

print(f"SESSION VALID? {valid_session}")





