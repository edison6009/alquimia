from app.seeders.sedeers import seed_roles

def init():
    print('aplicacion iniciada')

commands = {
    "init": init,
    "seed_roles": seed_roles,
}
