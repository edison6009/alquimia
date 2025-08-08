from typing import Optional
from app.models.user import User
from settings import *
from app.schemas.user import UserCreate


def get_users():
    session = SessionLocal()
    users = session.query(User).all()
    session.close()
    return users


def add_user(name: str, email: Optional[str] = None) -> None:
    validated = UserCreate(name=name, email=email)
    session = SessionLocal()
    try:
        new_user = User(name=validated.name, email=validated.email)
        session.add(new_user)
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()