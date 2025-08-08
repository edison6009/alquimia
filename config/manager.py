from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def init_database(connection, echo):
    return create_engine(
        connection,
        echo=echo,
    )


def init_session(engine, autoflush):
    return sessionmaker(
        autoflush=autoflush,
        bind=engine,
    )
