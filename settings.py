import os
from dotenv import load_dotenv
from config.schemas.database_url import ConnectionData
from config.manager import *

load_dotenv()

CONNECTION_DATA = ConnectionData(
    USER=os.getenv("USER"),
    PASSWORD=os.getenv("PASSWORD"),
    HOST=os.getenv("HOST"),
    PORT=os.getenv("PORT"),
    DATABASE=os.getenv("DATABASE"),
    DIALECT=os.getenv("DIALECT"),
    DRIVER=os.getenv("DRIVER")
)

conn = ManagerDatabase(
    connection = CONNECTION_DATA.url,
    echo = False,
    autocommit = False,
    autoflush = False
)

engine = conn.engine
