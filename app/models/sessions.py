from app.models import Base
from app.models.abstracts import CreatedAtMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import datetime

class Session(Base, CreatedAtMixin):
    __tablename__ = "sessions"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    expires_at: Mapped[datetime]
    is_active: Mapped[bool] = mapped_column(default=True)

    user: Mapped["User"] = relationship("User", back_populates="sessions")