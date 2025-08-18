from settings import SessionLocal

class registerController:
    def __init__(self):
        self.db = SessionLocal()

    def register(self, username, password):
        # Logic for user registration
        pass

    def is_username_taken(self, username):
        # Logic to check if the username is already taken
        pass