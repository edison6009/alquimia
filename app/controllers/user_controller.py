from pydantic import ValidationError

from settings import SessionLocal

from app.models.users import User
from app.models.rols import Rol

from app.validations.user_validations import UserValidation
from app.mixins.formats_validations import formats_validations

class UserController:

    def create(self, **kwargs) -> User | dict:
        try:
            data = UserValidation(**kwargs)
        except ValidationError as e:
            return formats_validations(e)

        session = SessionLocal()
        try:
            if session.query(User).filter(User.username == data.username).first():
                return {"username": ["El nombre de usuario ya está registrado."]}
            if session.query(User).filter(User.email == data.email).first():
                return {"email": ["El correo ya está registrado."]}

            new_user = User(
                name=data.name,
                last_name=data.last_name,
                username=data.username,
                email=data.email,
                phone=data.phone
            )
            new_user.password = data.password

            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            session.expunge(new_user)
            return new_user

        except Exception as e:
            try:
                session.rollback()
            except Exception:
                pass
            return {
                "error": [
                    str(e),
                    "user_controller.create: Error al crear el usuario."
                ]
            }

        finally:
            session.close()

    def register(self, **kwargs) -> User | dict:
        data = self.create(**kwargs)
        if isinstance(data, dict):
            return data

        session = SessionLocal()
        try:
            user = session.get(User, data.id)
            if not user: 
                raise Exception(f"Usuario con ID {data.id} no encontrado tras creación.")

            observer_rol = session.query(Rol).filter(Rol.name == "observer").first()
            if not observer_rol:
                session.delete(user)
                raise Exception("Rol 'observer' no existe en la base de datos.")
            
            user.rols.append(observer_rol)
            session.commit()
            session.refresh(user)
            session.expunge(user)
            return user

        except Exception as e:
            try:
                session.rollback()
            except Exception:
                pass
            return {
                "error": [
                    str(e),
                    f"user_controller.register: Error al registrar el usuario."
                ]
            }
        finally:
            session.close()


# class UserController:
#     # Controlador responsable de manejar la lógica de creación de usuarios

#     def create(self, **kwargs) -> User | dict:
#         # Método público que recibe datos arbitrarios para registrar un nuevo usuario

#         try:
#             data = UserValidation(**kwargs)
#             # Se valida la entrada usando un esquema definido (UserValidation).
#             # Si hay errores, se lanza ValidationError.
#         except ValidationError as e:
#             return formats_validations(e)
#             # Si falla la validación, se formatean los errores y se devuelven como dict.

#         session = SessionLocal()
#         # Se inicia una sesión de base de datos para realizar operaciones persistentes.

#         try:
#             # Verifica si el username ya existe en la base de datos
#             if session.query(User).filter(User.username == data.username).first():
#                 return {"username": ["El nombre de usuario ya está registrado."]}

#             # Verifica si el email ya está registrado
#             if session.query(User).filter(User.email == data.email).first():
#                 return {"email": ["El correo ya está registrado."]}

#             # Se construye el nuevo objeto User con los datos validados
#             new_user = User(
#                 name=data.name,
#                 last_name=data.last_name,
#                 username=data.username,
#                 email=data.email,
#                 phone=data.phone
#             )
#             new_user.password = data.password
#             # Se asigna la contraseña, lo que invoca el setter del PasswordMixin para hashearla

#             session.add(new_user)
#             session.commit()
#             # Se guarda el nuevo usuario en la base de datos

#             session.refresh(new_user)
#             # Se actualiza el objeto con los datos persistidos (ej. ID generado)

#             session.expunge(new_user)
#             # Se desacopla el objeto de la sesión para evitar errores de sesión cerrada

#             return new_user
#             # Se retorna el objeto User ya registrado

#         except Exception as e:
#             # Si ocurre cualquier excepción durante el proceso de persistencia

#             try:
#                 session.rollback()
#                 # Se revierte la transacción para evitar datos corruptos
#             except Exception:
#                 pass
#                 # Si el rollback falla, se ignora silenciosamente

#             return {
#                 "error": str(e),
#                 "description": "user_controller.register: Error al registrar el usuario."
#             }
#             # Se retorna un dict con el error capturado y una descripción contextual

#         finally:
#             session.close()
#             # Se cierra la sesión de base de datos para liberar recursos

            
