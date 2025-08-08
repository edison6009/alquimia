from __future__ import annotations

from typing import Any, Dict, Tuple, Callable

from pydantic import ValidationError

from app.schemas.user import UserCreate


class ClientController:
    def __init__(self, db_session_factory: Callable | None = None):
        self._db_session_factory = db_session_factory

    def validar_cliente(self, payload: Dict[str, Any]) -> Tuple[bool, Dict[str, str] | Dict[str, Any]]:
        try:
            data = UserCreate.model_validate(payload)
            return True, data.model_dump()
        except ValidationError as exc:
            errors: Dict[str, str] = {}
            for err in exc.errors():
                loc = err.get("loc", ())
                field = loc[-1] if loc else "__all__"
                errors[str(field)] = err.get("msg", "Dato inválido")
            return False, errors

    def crear_cliente(self, payload: Dict[str, Any]):
        if self._db_session_factory is None:
            raise RuntimeError("No hay fábrica de sesión configurada. Inyecta SessionLocal en el constructor.")
        # Importación diferida para evitar dependencias innecesarias en validación
        from app.models.user import User

        data = UserCreate.model_validate(payload)
        with self._db_session_factory() as db:
            user = User(
                nombre=data.nombre,
                description=data.description,
            )
            user.password = data.password

            db.add(user)
            db.commit()
            db.refresh(user)
            return user