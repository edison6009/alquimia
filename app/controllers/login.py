from __future__ import annotations

from typing import Any, Dict, Tuple

from pydantic import BaseModel, Field, ValidationError

from settings import SessionLocal


class LoginRequest(BaseModel):
    nombre: str = Field(min_length=1)
    password: str = Field(min_length=8)


class LoginController:
    def __init__(self, db_session_factory=SessionLocal):
        self._db_session_factory = db_session_factory

    def validar_login(self, payload: Dict[str, Any]) -> Tuple[bool, Dict[str, str] | Dict[str, Any]]:
        try:
            data = LoginRequest.model_validate(payload)
            return True, data.model_dump()
        except ValidationError as exc:
            errors: Dict[str, str] = {}
            for err in exc.errors():
                loc = err.get("loc", ())
                field = loc[-1] if loc else "__all__"
                errors[str(field)] = err.get("msg", "Dato inválido")
            return False, errors

    def login(self, payload: Dict[str, Any]):
        # Importación diferida para evitar dependencias innecesarias en validación
        from app.models.user import User

        data = LoginRequest.model_validate(payload)
        with self._db_session_factory() as db:
            user = db.query(User).filter(User.nombre == data.nombre).first()
            if user and user.verify_password(data.password):
                return user
            return None



