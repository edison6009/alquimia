from app.seeders.sedeers import *
from app.views.app import MiVentana
from app.controllers.register_controller import RegisterController
from app.models.users import User
import wx


def init():
    register = RegisterController()
    data = register.register(name="Admin",
                      last_name="Admin",
                      username="admin",
                    #   email="admiSmail.com",
                      phone="16sadsad",
                      password="ad"
                      )
    print(data)

commands = {
    "init": init,
    "seeders": seeders,
    "seed_roles": seed_roles,
}