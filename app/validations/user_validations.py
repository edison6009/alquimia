from pydantic import BaseModel, field_validator #, EmailStr, Field

from app.mixins.emails_are_valid import emails_are_valid

class UserValidation(BaseModel):
    # Modelo base de Pydantic para validar datos de usuario
    name: str  # Nombre del usuario, obligatorio
    last_name: str  # Apellido del usuario, obligatorio
    username: str  # Nombre de usuario único, obligatorio
    email: str  # Correo electrónico, se valida con lógica personalizada
    phone: str  # Número de teléfono, validado manualmente (mínimo 10 dígitos)
    password: str  # Contraseña, validada con reglas de seguridad

    @field_validator("email")
    def email_valid(cls, email: str) -> str:
        # Valida el formato del correo electrónico
        email = email.strip()  # Elimina espacios antes/después
        email_validators = []  # Lista de errores acumulados
        if email and not emails_are_valid(email):
            email_validators.append("El correo no tiene un formato válido")
        if email_validators:
            raise ValueError(",".join(email_validators))  # Lanza todos los errores juntos
        return email  # Retorna el correo limpio si es válido

    @field_validator("phone")
    def phone_valid(cls, phone):
        # Valida que el teléfono tenga solo dígitos y longitud mínima
        phone = phone.strip()  # Elimina espacios
        phone_validators = []  # Lista de errores acumulados
        if not phone.isdigit():
            phone_validators.append("Debe contener solo dígitos")
        if len(phone) < 10:
            phone_validators.append("Debe tener al menos 10 dígitos")
        if phone_validators:
            raise ValueError(",".join(phone_validators))  # Lanza todos los errores juntos
        return phone  # Retorna el teléfono limpio si es válido

    @field_validator("password")
    def password_valid(cls, password):
        # Valida que la contraseña cumpla requisitos mínimos de seguridad
        password_validators = []  # Lista de errores acumulados
        if len(password) < 8:
            password_validators.append("Debe tener al menos 8 caracteres")
        if not any(c.isdigit() for c in password):
            password_validators.append("Debe contener al menos un número")
        if not any(c.isalpha() for c in password):
            password_validators.append("Debe contener al menos una letra")
        if password_validators:
            raise ValueError(",".join(password_validators))  # Lanza todos los errores juntos
        return password  # Retorna la contraseña si es válida
