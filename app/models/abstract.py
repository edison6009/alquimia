import bcrypt
from sqlalchemy.orm import declared_attr, Mapped, mapped_column
from sqlalchemy import String, DateTime, func
from datetime import datetime

class PasswordMixin:
    _password: Mapped[str] = mapped_column("password", String(128), nullable=False)

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, plain_password: str) -> None:
        hashed = bcrypt.hashpw(plain_password.encode("utf-8"), bcrypt.gensalt())
        self._password = hashed.decode("utf-8")

    def verify_password(self, intentado: str) -> bool:
        return bcrypt.checkpw(intentado.encode("utf-8"), self._password.encode("utf-8"))

#---------------------------------------------------------------------------------------------------------------------------

class CreatedAtMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

class UpdateAtMixin:
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

class DateTimeMixin(CreatedAtMixin, UpdateAtMixin):
    pass

#---------------------------------------------------------------------------------------------------------------------------    

class SoftDeleteMixin:
    deleted_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=None, nullable=True)

    def soft_delete(self) -> None:
        self.deleted_at = datetime.now()

    def restore(self) -> None:
        self.deleted_at = None

