from app.seeders.sedeers import *

def init():
    print('aplicacion iniciada')

commands = {
    "init": init,
    "seeders": seeders,
    "seed_roles": seed_roles,
}