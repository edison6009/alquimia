from pydantic import BaseModel, field_validator
from typing import Optional

from app.validations.schemas.exist import exist
from app.validations.schemas.auxiliares import *
from app.validations.schemas.emails_are_valid import emails_are_valid

class UserValidation(BaseModel):
    name: str
    last_name: str
    username: str
    email: str
    phone: Optional[str]
    password: str

    @field_validator("name")
    def name_valid(cls, name):
        errors = []
        if not name:
            errors.append("El nombre no puede estar en blanco")
        if has_spaces(name):
            errors.append("El nombre no debe contener espacios")
        if has_invalid_characters(name):
            errors.append("El nombre solo debe contener letras sin símbolos ni números")
        if errors:
            raise ValueError(", ".join(errors))
        return name

    @field_validator("last_name")
    def last_name_valid(cls, last_name):
        errors = []
        if not last_name:
            errors.append("El apellido no puede estar en blanco")
        if has_spaces(last_name):
            errors.append("El apellido no debe contener espacios")
        if has_invalid_characters(last_name):
            errors.append("El apellido solo debe contener letras sin símbolos ni números")
        if errors:
            raise ValueError(", ".join(errors))
        return last_name

    @field_validator("username")
    def username_valid(cls, username):
        errors = []
        if not username:
            errors.append("El nombre de usuario no puede estar en blanco")
        if has_spaces(username):
            errors.append("El nombre de usuario no debe contener espacios")
        if errors:
            raise ValueError(", ".join(errors))
        return username

    @field_validator("email")
    def email_valid(cls, email):
        email = email.strip()
        errors = []
        if not email:
            errors.append("El correo no puede estar en blanco")
        elif emails_are_valid(email):
            errors.append("El correo no tiene un formato válido")
        if has_spaces(email):
            errors.append("El email no debe contener espacios")
        if errors:
            raise ValueError(", ".join(errors))
        return email

    @field_validator("phone")
    def phone_valid(cls, phone):
        errors = []
        if exist(phone) is None:
            return None
        if not phone.isdigit():
            errors.append("Debe contener solo dígitos")
        if len(phone) < 10:
            errors.append("Debe tener al menos 10 dígitos")
        if errors:
            raise ValueError(", ".join(errors))
        return phone

    @field_validator("password")
    def password_valid(cls, password):
        errors = []
        if len(password) < 8:
            errors.append("Debe tener al menos 8 caracteres")
        if not any(c.isdigit() for c in password):
            errors.append("Debe contener al menos un número")
        if not any(c.isalpha() for c in password):
            errors.append("Debe contener al menos una letra")
        if errors:
            raise ValueError(", ".join(errors))
        return password
