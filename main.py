from pathlib import Path
import sys
import logging

BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

from settings import engine
from app.controllers.user_controller import get_users, add_user


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        with engine.connect() as conn:
            logging.info("Conexión exitosa con la base de datos")
    except Exception:
        logging.exception("Error al conectar")