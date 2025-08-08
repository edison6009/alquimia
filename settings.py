import os
import logging
from dotenv import load_dotenv
from config.schemas.database_url import ConnectionData
from config.manager import init_database, init_session

load_dotenv()

# Defaults y aviso si faltan variables
DIALECT = os.getenv("DIALECT") or "sqlite"
DATABASE = os.getenv("DATABASE") or "Alquimia.db"
if not os.getenv("DIALECT") or not os.getenv("DATABASE"):
    logging.warning("Faltan variables de entorno DIALECT/DATABASE. Usando valores por defecto.")

# Config embebida (SQLite por defecto)
CONNECTION_DATA = ConnectionData(
    DATABASE=DATABASE,
    DIALECT=DIALECT,
)

engine = init_database(
    CONNECTION_DATA.url_embedded,  # para servidor usar: CONNECTION_DATA.url_server
    echo=False,
)

SessionLocal = init_session(engine, autoflush=False)