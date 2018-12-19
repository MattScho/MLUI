from tkinter import *
from main.gui.Widgets.BooleanToggle import BooleanToggle
from main.gui.Utilities.Settings import Settings

class CheckBoxFrame(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self,parent, bg=Settings.BACKGROUND_COLOR.value)
        self.btns = []
        for pick in picks:
            chk = BooleanToggle(self, text=pick)
            chk.pack(side=side, anchor=anchor, expand=YES)
            self.btns.append(chk)

    def get(self):
        res = []
        for btn in self.btns:
            res.append(btn.get())
        return res