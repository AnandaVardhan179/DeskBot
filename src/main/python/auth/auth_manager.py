from src.main.python.auth.user_model import UserModel

class AuthManager:
    def __init__(self):
        self.user_model = UserModel()

    def register(self, username, password):
        if self.user_model.create_user(username, password):
            return "User registered successfully."
        else:
            return "Username already exists. Please choose a different one."

    def login(self, username, password):
        if self.user_model.authenticate_user(username, password):
            return f"Welcome back, {username}!"
        else:
            return "Invalid username or password."

    def logout(self, username):
        # Placeholder logic for logout (if needed)
        return f"User {username} logged out successfully."

    def close(self):
        self.user_model.close()

# Example usage
if __name__ == "__main__":
    auth_manager = AuthManager()
    print(auth_manager.login("testuser", "password"))  # Should print "Welcome back, testuser!"
    auth_manager.close()
