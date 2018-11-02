from tkinter import *
import pandas as pd

from tkinter import filedialog
from main.gui.Utilities.Settings import Settings

class SelectorFrame(Frame):

    def __init__(self, parent, data):
        Frame.__init__(self, master=parent, bg=Settings.BACKGROUND_COLOR.value)

        self.colors = ["Pink", "Light Green", "Yellow"]

        self.csv = pd.read_csv(open(data, 'r'))
        self.cols = {}
        self.buttons = []
        self.addSelectionButtons()


    def addSelectionButtons(self):
        for col in self.csv.columns[:-1]:
            self.cols[col] = 1
        self.cols[self.csv.columns[-1]] = 2
        self.paintButtons()

    def paintButtons(self):
        for i,k in enumerate(self.cols.keys()):
            btn = Button(master=self, text=k, bg=self.colors[self.cols[k]], command=lambda i=i: self.changeColor(i))
            btn.grid(column=i, row=1, padx=5)
            self.buttons.append(btn)

    def changeColor(self, i):
        btn = self.buttons[i]
        if btn.cget('bg') == "Pink":
            btn.config(bg = "Light Green")
        elif btn.cget('bg') == "Light Green":
            for b in self.buttons:
                if b.cget("bg") == "Yellow":
                    b.config(bg = "Light Green")
            btn.config(bg= "Yellow")
        elif btn.cget("bg") == "Yellow":
            btn.config(bg = "Pink")



    def get_cols(self):
        info = {}
        for b in self.buttons:
            use = None
            if b.cget("bg") == "Pink":
                use = 0
            elif b.cget("bg") == "Light Green":
                use = 1
            elif b.cget("bg") == "Yellow":
                use = 2
            info[b.cget("text")] = use
        return info




