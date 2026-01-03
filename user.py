from password_auth import hash_password

class User:
    def __init__(self, username, password,  secret):
        self.username = username
        self.password_hash = hash_password(password)
        self.secret = secret
