from app.models import Client
from settings import SessionLocal

class ClientController:

    def __init__(self):
        Client.set_session(SessionLocal)

    def crear_cliente(self):
        nuevo = Client.create(nombre="Nuevo")
        print("Cliente creado:", nuevo.to_dict())

