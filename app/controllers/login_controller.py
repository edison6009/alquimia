from settings import SessionLocal

class LoginController:
    def __init__(self):
        self.db = SessionLocal()
