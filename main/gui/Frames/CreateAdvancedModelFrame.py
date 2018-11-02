from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from main.gui.Frames.AdvAlgorithmFrame import AdvAlgorithmFrame
import pandas as pd
from main.gui.Utilities.Settings import Settings
from main.gui.Frames.CSVSelectorFrame import SelectorFrame
'''
Frame for importing data and hosting sub frames for defining algorithms to be used
'''
class AdvancedModelCreationFrame(Frame):
    def __init__(self, GUI):
        Frame.__init__(self, bg=Settings.BACKGROUND_COLOR.value)
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
        self.selectTypeOfLearningBox = ttk.Combobox(self, state='readonly',font=Settings.REGULAR_FONT.value, values=['Classification', 'Regression', 'Clustering'])
        self.selectTypeOfLearningBox.pack()
        self.selectTypeOfLearningBox.bind("<<ComboboxSelected>>",
                                 lambda _: self.typeOfLearningSelected(self.selectTypeOfLearningBox.get()))

    def typeOfLearningSelected(self, selectedTypeOfLearning):
        self.selectTypeOfLearningBox.config(state="disabled")
        self.showSelKindOfData()
        self.typeOfLearning = selectedTypeOfLearning

    def showSelKindOfData(self):
        self.selectkindOfDataBox = ttk.Combobox(self, state='readonly',font=Settings.REGULAR_FONT.value, values=['1 CSV Auto Split Training and Testing', '2 CSVs 1 Training 1 Testing'])
        self.selectkindOfDataBox.pack()
        self.selectkindOfDataBox.bind("<<ComboboxSelected>>", lambda _: self.showCorrectDataSelection(self.selectkindOfDataBox.selection_get()))

    def showCorrectDataSelection(self, type):
        self.selectkindOfDataBox.config(state="disabled")
        if type == '1 CSV Auto Split Training and Testing':
            self.allData = filedialog.askopenfilename(title="Select Data")
            self.typeOfData = 'All-n-One'
            self.addSelectorFrame(self.allData)
        elif type == '2 CSVs 1 Training 1 Testing':
            self.trainingData = filedialog.askopenfilename(title="Select Training Data")
            self.testingData = filedialog.askopenfilename(title="Select Testing Data")
            self.typeOfData = "1 Training 1 Testing"
            self.addSelectorFrame(self.testingData)
        self.addAnAlgBtn()

    def addSelectorFrame(self, data):
        self.columnsSelectorFrame = SelectorFrame(self, data)
        self.columnsSelectorFrame.pack()

    def addAnAlgBtn(self):
        addAlgFrameBtn = Button(self, text='Add Algorithm',font=Settings.REGULAR_FONT.value, width= 15, bg=Settings.GOOD_BUTTON_COLOR.value, command=lambda : self.addAlgFrame())
        self.addExecuteBtn()
        addAlgFrameBtn.pack()
        self.addAlgFrame()

    def addAlgFrame(self, alg=None):
        if alg == None:
            latestAlgFrame = AdvAlgorithmFrame(self)
        else:
            latestAlgFrame = AdvAlgorithmFrame(self, algor=alg)
        self.algFrames.append(latestAlgFrame)
        latestAlgFrame.pack()

    def removeAlgFrame(self, frame):
        self.algFrames.remove(frame)
        frame.destroy()

    def addExecuteBtn(self):
        execBtn = Button(self, text="Execute",font=Settings.REGULAR_FONT.value, width= 15, bg=Settings.GOOD_BUTTON_COLOR.value, command=lambda : self.execute())
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
        self.GUI.newResultFrame(orders, self.typeOfData, allData=allData, trainingData=trainingData, testingData=testData, columnsDict=self.columnsSelectorFrame.get_cols())

    def getSelectedTypeOfLearning(self):
        return self.typeOfLearning



