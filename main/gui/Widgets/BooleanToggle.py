from tkinter import Checkbutton, IntVar

from main.gui.Utilities.Settings import Settings


class BooleanToggle(Checkbutton):
    def __init__(self, parent, text=""):
        self.var = IntVar()
        Checkbutton.__init__(self, parent, text=text, var=self.var, bg=Settings.BACKGROUND_COLOR.value, fg=Settings.FONT_COLOR.value)


    def get(self):
        return self.var.get() == 1