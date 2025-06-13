from sqlalchemy import Column, Integer, String
from app.models import Base  

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=False, nullable=True)
