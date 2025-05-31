from app.models.user import User
from settings import *

def get_users():
    session = conn.SessionLocal()
    users = session.query(User).all()
    session.close()
    return users

def add_user(name):
    session = conn.SessionLocal()
    new_user = User(name=name)
    session.add(new_user)
    session.commit()
    session.close()
