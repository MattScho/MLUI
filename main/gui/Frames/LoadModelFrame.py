from tkinter import Frame, Button, filedialog, Entry, Label
from main.gui.Utilities.Settings import Settings
import pickle
import pandas as pd
import numpy as np

class LoadModelFrame(Frame):
    def __init__(self, GUI, parent):
        Frame.__init__(self, master=parent, bg=Settings.BACKGROUND_COLOR.value)
        self.GUI = GUI
        self.pack()
        self.data = None
        self.addLoadModelBtn()
        self.addLoadDataBtn()
        self.addRunBtn()

    def addLoadModelBtn(self):
        loadModel = Button(master=self, font=Settings.REGULAR_FONT.value, height=3, width=16, bg=Settings.REGULAR_BUTTON2_COLOR.value, text="Load Model", command=lambda : self.importModel())
        loadModel.pack()

    def importModel(self):
        file = filedialog.askopenfilename()
        self.model = pickle.load(open(file, "rb"))

    def addLoadDataBtn(self):
        self.loadDataButton = Button(master=self, font=Settings.REGULAR_FONT.value, height=3, width=16, bg=Settings.REGULAR_BUTTON1_COLOR.value, text="Load Data", command=lambda : self.loadData())
        self.orLabel = Label(master=self, text="or")
        self.vectorEntry = Entry(master=self)
        self.orLabel.pack()
        self.vectorEntry.pack()
        self.loadDataButton.pack()

    def addRunBtn(self):
        self.runBtn = Button(self, font=Settings.REGULAR_FONT.value, height=3, width=16, bg=Settings.GOOD_BUTTON_COLOR.value, text="Run", command= lambda: self.run())
        self.runBtn.pack()

    def loadData(self):
        file = filedialog.askopenfilename()
        self.data = pd.read_csv(file)


    def run(self):
        if self.data != None:
            print(self.model.predict(self.data))
        else:
            print(self.model.predict([np.asarray(self.vectorEntry.get().split(","), dtype=float)]))
