from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from main.gui.Frames.AlgorithmFrame import AlgorithmFrame
from main.AlgExecution.Executioner.Executioner import  Executioner
import pandas as pd
from main.gui.Utilities.Colors import Color
import os
import time
from datetime import datetime
import shutil
import threading

class ModelCreationFrame(Frame):
    def __init__(self, GUI):
        Frame.__init__(self, bg=Color.BACKGROUND_COLOR.value)
        self.GUI = GUI
        self.pack()

        self.allData = None
        self.trainingData = None
        self.testingData = None

        self.CSV_label_cols = []
        self.CSV_feature_col = -1
        self.algFrames = []
        self.showSelTypeOfLearning()

    def showSelTypeOfLearning(self):
        selectTypeOfLearningBox = ttk.Combobox(self, state='readonly', values=['Classification', 'Regression', 'Clustering'])
        selectTypeOfLearningBox.pack()
        selectTypeOfLearningBox.bind("<<ComboboxSelected>>",
                                 lambda _: self.typeOfLearningSelected(selectTypeOfLearningBox.get()))

    def typeOfLearningSelected(self, selectedTypeOfLearning):
        self.showSelKindOfData()
        self.typeOfLearning = selectedTypeOfLearning

    def showSelKindOfData(self):
        selectkindOfDataBox = ttk.Combobox(self, state='readonly', values=['1 CSV Auto Split Training and Testing', '2 CSVs 1 Training 1 Testing'])
        selectkindOfDataBox.pack()
        selectkindOfDataBox.bind("<<ComboboxSelected>>", lambda _: self.showCorrectDataSelection(selectkindOfDataBox.selection_get()))

    def showCorrectDataSelection(self, type):
        if type == '1 CSV Auto Split Training and Testing':
            self.allData = filedialog.askopenfilename(title="Select Data")
            self.typeOfData = 'All-n-One'
        elif type == '2 CSVs 1 Training 1 Testing':
            self.trainingData = filedialog.askopenfilename(title="Select Training Data")
            self.testingData = filedialog.askopenfilename(title="Select Testing Data")
            self.typeOfData = "1 Training 1 Testing"
        self.addAnAlgBtn()


    def addAnAlgBtn(self):
        addAlgFrameBtn = Button(self, text='Add Algorithm', width= 15, bg=Color.GOOD_BUTTON_COLOR.value, command=lambda : self.addAlgFrame())
        self.addExecuteBtn()
        addAlgFrameBtn.pack()
        self.addAlgFrame()

    def addAlgFrame(self, alg=None):
        if alg == None:
            latestAlgFrame = AlgorithmFrame(self)
        else:
            latestAlgFrame = AlgorithmFrame(self, algor=alg)
        self.algFrames.append(latestAlgFrame)
        latestAlgFrame.pack()

    def addExecuteBtn(self):
        execBtn = Button(self, text="Execute", width= 15, bg=Color.GOOD_BUTTON_COLOR.value, command=lambda : self.execute())
        execBtn.pack()

    def execute(self):
        orders = []
        allData = trainingData = testData = None
        for algFrame in self.algFrames:
            orders.append(algFrame.packageForExecution())
        if self.typeOfData == "All-n-One":
            allData = pd.read_csv(self.allData)
        elif self.typeOfData == "1 Training 1 Testing":
            trainingData = pd.read_csv(self.trainingData)
            testData = pd.read_csv(self.trainingData)
        self.GUI.newResultFrame(orders, self.typeOfData, allData=allData, trainingData=trainingData, testingData=testData)

    def getSelectedTypeOfLearning(self):
        return self.typeOfLearning



