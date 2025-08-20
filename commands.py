from app.seeders.sedeers import *
from app.views.app import MiVentana
from app.controllers.user_controller import UserController
from app.models.users import User
import wx


def init():
    user_controller = UserController()
    data = user_controller.register(
        name="Admin",
        last_name="Admin",
        username="admin",
        email="admin@gmail.com",
        phone="04245451786",
        password="admin1234"
    )
    print(data)

commands = {
    "init": init,
    "seeders": seeders,
    "seed_roles": seed_roles,
}