from tkinter import Frame, Button, filedialog, Entry
from main.gui.Utilities.Settings import Settings
import pickle
import pandas as pd
import numpy as np

class LoadModelFrame(Frame):
    def __init__(self, GUI):
        Frame.__init__(self, bg=Settings.BACKGROUND_COLOR.value)
        self.GUI = GUI
        self.pack()
        self.data = None
        self.addLoadModelBtn()
        self.addLoadDataBtn()
        self.addRunBtn()

    def addLoadModelBtn(self):
        loadModel = Button(master=self, text="Load Model", command=lambda : self.importModel())
        loadModel.pack()

    def importModel(self):
        file = filedialog.askopenfilename()
        self.model = pickle.load(open(file, "rb"))

    def addLoadDataBtn(self):
        self.loadDataButton = Button(master=self, text="Load Data", command=lambda : self.loadData())
        self.loadDataButton.pack()

    def addRunBtn(self):
        self.runBtn = Button(self, text="Run", command= lambda: self.run())
        self.runBtn.pack()

    def loadData(self):
        file = filedialog.askopenfilename()
        self.data = pd.read_csv(file)


    def run(self):
        print(self.data)
        print(self.model.predict(self.data))
