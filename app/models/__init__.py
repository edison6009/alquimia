
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base() #alquemist declarative form 2.0 

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy_mixins import AllFeaturesMixin
class Base(DeclarativeBase, AllFeaturesMixin): #alquemist declarative form 2.0+
    pass

from app.models.client import Client

