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

engine = init_database(CONNECTION_DATA.url, echo = False)

SessionLocal = init_session(engine, autocommit = False, autoflush = False)