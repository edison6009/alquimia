from app.models import Base  
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String

class Client(Base):
    __tablename__ = "clients"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))