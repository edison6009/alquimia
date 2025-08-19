from settings import SessionLocal
from app.models.users import User
from pydantic import ValidationError
from app.validations.user_validations import *

class RegisterController:
    def register(self, **kwargs) -> User | dict:
        
        result = RegisterValidation.validate_all_fields(**kwargs)
        return result
        
        # try:
        #     return RegisterValidation(**kwargs)
        # except MultiError as e:
        #     return {e.field: e.messages}

        # with SessionLocal() as session:
        #     if session.query(User).filter(User.username == data.username).first():
        #         return {"username": "El nombre de usuario ya está registrado."}
        #     if session.query(User).filter(User.email == data.email).first():
        #         return {"email": "El correo ya está registrado."}

        #     user = User(
        #         name=data.name,
        #         last_name=data.last_name,
        #         username=data.username,
        #         email=data.email,
        #         phone=data.phone
        #     )
        #     user.password = data.password

        #     session.add(user)
        #     session.commit()
        #     session.refresh(user)

            # return user