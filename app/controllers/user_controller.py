from typing import Optional
from sqlalchemy import select
from app.models.user import User
from settings import SessionLocal


def get_users():
    with SessionLocal() as session:
        return session.execute(select(User)).scalars().all()


def add_user(name: str, email: Optional[str] = None):
    with SessionLocal() as session:
        new_user = User(name=name, email=email)
        try:
            session.add(new_user)
            session.commit()
        except Exception:
            session.rollback()
            raise