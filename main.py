from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

from settings import *
from app.controllers.user_controller import get_users, add_user

if __name__ == "__main__":
    add_user("edison")

    # Obtener todos los usuarios registrados
    usuarios = get_users()

    # Mostrar los resultados
    print("Usuarios en la base de datos:")
    for usuario in usuarios:
        print(f"- {usuario.name}")