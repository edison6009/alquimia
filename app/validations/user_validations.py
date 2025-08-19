from pydantic import BaseModel, field_validator
from app.validations.schemas.exeptions.field_validation import MultiError
import re

class RegisterValidation(BaseModel):
    name: str
    last_name: str
    username: str
    email: str
    phone: int
    password: str

    @field_validator("email")
    def email_valid(cls, email):  # <-- este nombre debe coincidir
        email = email.strip()
        email_validations = []
        if not email:
            email_validations.append("El correo no puede estar vacío.")
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            email_validations.append("Formato de correo inválido.")
        if email_validations:
            raise MultiError("email", email_validations)
        return email

    @field_validator("phone")
    def phone_valid(cls, phone):
        phone = phone.strip()
        phone_validation = []
        if not phone.isdigit():
            phone_validation.append("Debe contener solo dígitos")
        if len(phone) < 10:
            phone_validation.append("Debe tener al menos 10 dígitos.")
        if phone_validation:
            raise MultiError("phone", phone_validation)
        return phone

    @field_validator("password")
    def password_valid(cls, v):
        password_validation = []
        if len(v) < 8:
            password_validation.append("Debe tener al menos 8 caracteres.")
        if not any(c.isdigit() for c in v):
            password_validation.append("Debe contener al menos un número.")
        if not any(c.isalpha() for c in v):
            password_validation.append("Debe contener al menos una letra.")
        if password_validation:
            raise MultiError("password", password_validation)
        return v
    
    @classmethod
    def validate_all_fields(cls, **kwargs):
        instance = cls.model_construct(**kwargs)  # evita validación automática
        errors = {}

        for field in cls.model_fields:
            validator = getattr(cls, f"{field}_valid", None)
            if validator:
                value = getattr(instance, field)
                try:
                    validated = validator(value)
                    setattr(instance, field, validated)
                except MultiError as e:
                    errors.setdefault(e.field, []).extend(e.messages)

        return errors if errors else instance
