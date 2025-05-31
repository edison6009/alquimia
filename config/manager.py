from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def init_database(connection, echo):
    return create_engine(
        connection, 
        echo=echo,
    )

def init_session(engine, autocommit, autoflush):
    return sessionmaker(
        autocommit=autocommit, 
        autoflush=autoflush,
        bind=engine
    )

class ManagerDatabase:
    def __init__(self, connection, autocommit, autoflush, echo):
        self.connection = connection
        self.autocommit = autocommit
        self.autoflush = autoflush
        self.echo = echo
        self.engine = None
        self.SessionLocal = None

    def __repr__(self):
        self.engine = init_database(
            self.connection, 
            self.echo)
        
        self.SessionLocal = init_session(
            self.engine, 
            self.autocommit, 
            self.autoflush)
        
        with self.engine.connect() as conn: 
            return 'conexion completa'
