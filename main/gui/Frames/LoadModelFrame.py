from tkinter import Frame
from main.gui.Utilities.Settings import Settings

class LoadModelFrame(Frame):
    def __init__(self, GUI):
        Frame.__init__(self, bg=Settings.BACKGROUND_COLOR.value)
        self.GUI = GUI
        self.pack()
