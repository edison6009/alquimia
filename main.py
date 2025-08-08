from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

from settings import *
from app.controllers.user_controller import get_users, add_user
from app.models import Base

if __name__ == "__main__":
    try:
        # Ensure tables exist for quick local runs/tests
        Base.metadata.create_all(bind=engine)
        with engine.connect() as conn:
            print("Conexión exitosa con la base de datos")
    except Exception as e:
        print(f"Error al conectar: {e}")