from app.seeders.sedeers import *
from app.views.app import MiVentana
import wx

def init():
    app = wx.App()
    frame = MiVentana(None, "Alquimia")
    frame.Show()
    app.MainLoop()

commands = {
    "init": init,
    "seeders": seeders,
    "seed_roles": seed_roles,
}