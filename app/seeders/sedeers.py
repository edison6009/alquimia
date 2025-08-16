from settings import SessionLocal
from app.models.rols import Rol
from sqlalchemy.exc import IntegrityError

def seeders():
    seed_roles()

def seed_roles():
    role_names = ["observer", "employee", "admin"]

    with SessionLocal() as session:
        for name in role_names:
            exists = session.query(Rol).filter_by(name=name).first()
            if not exists:
                session.add(Rol(name=name))
        try:
            session.commit()
            print("Roles base sembrados correctamente.")
        except IntegrityError as e:
            session.rollback()
            print(f"Error al sembrar roles: {e}")