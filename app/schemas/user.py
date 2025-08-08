from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field, field_validator


class UserBase(BaseModel):
    nombre: str = Field(min_length=1, max_length=50)
    description: Optional[str] = Field(default=None, max_length=500)

    @field_validator("nombre")
    @classmethod
    def strip_nombre(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("El nombre no puede estar vacío")
        return cleaned


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=128)

    @field_validator("password")
    @classmethod
    def strong_password(cls, value: str) -> str:
        if value.strip() != value:
            raise ValueError("La contraseña no debe contener espacios al inicio o al final")
        return value