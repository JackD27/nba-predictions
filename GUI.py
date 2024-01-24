import tkinter
import tkinter.messagebox
from settings import Settings

class App(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title(Settings.APP_NAME)
        self.resizable(True, True)
        self.minsize(Settings.WIDTH, Settings.HEIGHT)
        self.maxsize(Settings.MAX_WIDTH, Settings.MAX_HEIGHT)