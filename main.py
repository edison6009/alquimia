from pathlib import Path
from app.controllers.client_controller import ClientController
import sys

BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

from settings import *
# from app.controllers.user_controller import get_users, add_user

if __name__ == "__main__":
    
    # object_client = ClientController
    # object_client.crear_cliente()
    
    try:
        with engine.connect() as conn:
            print("Conexión exitosa con la base de datos")
    except Exception as e:
        print(f"Error al conectar: {e}")