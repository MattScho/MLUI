from tkinter import Frame, Entry, Label
from tkinter import ttk
from tkinter import *
from ..Utilities.ToolTip import ToolTip
from main.gui.Utilities.Colors import Color
from main.Algorithms.AlgorithmsEnum import Algorithm
class AlgorithmFrame(Frame):
    def __init__(self, parent, algor=None):
        Frame.__init__(self, master=parent, bg=Color.BACKGROUND_COLOR.value)
        self.readyToExec = False

        self.initializeParamsDict()
        self.paramFields = []

        self.algs = []
        for alg in self.listOfAlgorithms:
            if parent.getSelectedTypeOfLearning() == alg.get("Type"):
                self.algs.append(alg.get("AlgName"))
        self.selectAlgBox = ttk.Combobox(master=self, state='readonly', values=self.algs)
        self.selectAlgBox.grid(row=0, column=0, columnspan=2)
        print(self.algs)
        if algor != None:
            self.selectAlgBox.current(self.algs.index(algor))
            print("AlG" + str(algor))
            self.buildParameterInputs(algor)
        self.selectAlgBox.bind("<<ComboboxSelected>>", lambda _: self.buildParameterInputs(self.selectAlgBox.selection_get()))


    def buildParameterInputs(self, alg):
        print("Build Params " + str(alg))
        algToUse = {}
        for algor in self.listOfAlgorithms:
            if algor.get("AlgName") == alg:
                print("Found alg: " + alg)
                algToUse = algor
                break
        print("Alg to use: " + str(algToUse))
        curRow = 1
        for param in algToUse.get("Simple Parameters"):
            label = Label(master=self, text=param.get("ParamName"), bg=Color.BACKGROUND_COLOR.value)
            label.grid(row=curRow, column=0)
            ToolTip(label, param.get("Simple Description"))
            if param.get("Type") == "int" or param.get("Type") == "double" or param.get("Type") == "float":
                textWidget = Entry(master=self, bg=Color.TEXTFIELD_COLOR.value)
                textWidget.insert(END, param.get("Default"))
                textWidget.grid(row=curRow, column=1)
                self.paramFields.append(textWidget)
            elif param.get("Type") == "bool":
                selectorWidget = ttk.Combobox(master=self, state='readonly', values=[True, False])
                selectorWidget.current(0)
                selectorWidget.grid(row=curRow, column=1)
                self.paramFields.append(selectorWidget)
            elif param.get("Type") == "options":
                selectorWidget = ttk.Combobox(master=self, state='readonly', values=param.get("Default"))
                selectorWidget.current(0)
                selectorWidget.grid(row=curRow, column=1)
                self.paramFields.append(selectorWidget)

            curRow += 1

    def isReadyToExec(self):
        return self.readyToExec

    def packageForExecution(self):
        algName = self.selectAlgBox.get()
        print("Alg for exec: " + algName)
        paramsList = []
        paramsDict = {}
        for pf in self.paramFields:
            paramsList.append(pf.get())
        cur = 0
        params = []
        algDict = {}
        for alg in self.listOfAlgorithms:
            print("Alg in list: " + str(alg))
            if alg.get("AlgName") == algName:
                algDict = alg
                break
        for param in algDict.get("Simple Parameters"):
            paramsDict[param.get("ParamName")] = paramsList[cur]
            cur += 1
        return {"Algorithm":algName, "Type":algDict.get("Type"), "Params":paramsDict}

    def initializeParamsDict(self):

        self.listOfAlgorithms = []
        for alg in Algorithm:
            self.listOfAlgorithms.append(alg.value)
