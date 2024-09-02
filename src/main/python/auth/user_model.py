import sqlite3
from hashlib import sha256

class UserModel:
    def __init__(self, db_name="deskbot_users.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_users_table()

    def _create_users_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password_hash TEXT,
                oauth_provider TEXT,
                oauth_token TEXT
            )
        """)
        self.connection.commit()

    def create_user(self, username, password):
        password_hash = sha256(password.encode()).hexdigest()
        try:
            self.cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def authenticate_user(self, username, password):
        password_hash = sha256(password.encode()).hexdigest()
        self.cursor.execute("SELECT * FROM users WHERE username = ? AND password_hash = ?", (username, password_hash))
        return self.cursor.fetchone() is not None

    def save_oauth_token(self, username, provider, token):
        self.cursor.execute("UPDATE users SET oauth_provider = ?, oauth_token = ? WHERE username = ?", (provider, token, username))
        self.connection.commit()

    def close(self):
        self.connection.close()

# Add this to create the 'testuser' with password 'password'
if __name__ == "__main__":
    user_model = UserModel()
    if user_model.create_user("testuser", "password"):
        print("User 'testuser' created successfully.")
    else:
        print("User 'testuser' already exists.")
    user_model.close()
