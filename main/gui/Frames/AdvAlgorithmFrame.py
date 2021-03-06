from tkinter import ttk
from tkinter import *
from main.gui.Utilities.ToolTip import ToolTip
from main.gui.Widgets.BooleanToggle import BooleanToggle
from main.gui.Utilities.Settings import Settings
from main.Algorithms.AlgorithmsEnum import Algorithm
from main.gui.Frames.KerasFrame import KerasFrame

'''
Algorithm Frame for defining an order to send for training
'''
class AdvAlgorithmFrame(Frame):
    def __init__(self, parent, algor=None):
        Frame.__init__(self, master=parent, bg=Settings.BACKGROUND_COLOR.value)
        self.readyToExec = False

        self.initializeParamsDict()
        self.paramFields = []

        self.algs = []
        for alg in self.listOfAlgorithms:
            if parent.getSelectedTypeOfLearning() == alg.get("Type"):
                self.algs.append(alg.get("AlgName"))
        self.algs.append("Neural Network (Keras)")
        self.selectAlgBox = ttk.Combobox(master=self, font=Settings.REGULAR_FONT.value,state='readonly', values=self.algs)
        self.selectAlgBox.pack()
        self.removeBtn = Button(master=self, font=Settings.REGULAR_FONT.value, text="Remove",bg=Settings.BAD_BUTTON_COLOR.value, command=lambda : parent.removeAlgFrame(self))
        self.removeBtn.pack()
        if algor != None:
            self.selectAlgBox.current(self.algs.index(algor))
            self.buildParameterInputs(algor)
        self.selectAlgBox.bind("<<ComboboxSelected>>", lambda _: self.buildParameterInputs(self.selectAlgBox.selection_get()))


    def buildParameterInputs(self, alg):
        self.selectAlgBox.config(state="disabled")
        self.alg = alg
        if alg == "Neural Network (Keras)":
            networkFrame = KerasFrame(self)
            networkFrame.pack()
            self.paramFields.append(networkFrame)
        else:
            algToUse = {}
            for algor in self.listOfAlgorithms:
                if algor.get("AlgName") == alg:
                    algToUse = algor
                    break
            params = []
            for param in algToUse.get("Simple Parameters"):
                params.append(param)
            for param in algToUse.get("Advanced Parameters"):
                params.append(param)
            for param in params:
                label = Label(master=self, text=param.get("ParamName"), fg=Settings.FONT_COLOR.value, font=Settings.REGULAR_FONT, bg=Settings.BACKGROUND_COLOR.value)
                label.pack()
                ToolTip(label, param.get("Advanced Description"))
                if param.get("Type") == "int" or param.get("Type") == "double" or param.get("Type") == "float":
                    textWidget = Entry(master=self,font=Settings.REGULAR_FONT, bg=Settings.TEXTFIELD_COLOR.value)
                    textWidget.insert(END, param.get("Default"))
                    textWidget.pack(padx=10, pady=10)
                    self.paramFields.append(textWidget)
                elif param.get("Type") == "bool":
                    toggle =BooleanToggle(self)
                    toggle.pack(padx=10, pady=10)
                    self.paramFields.append(toggle)
                elif param.get("Type") == "options":
                    selectorWidget = ttk.Combobox(master=self, state='readonly',font=Settings.REGULAR_FONT, values=param.get("Default"))
                    selectorWidget.current(0)
                    selectorWidget.pack(padx=10, pady=10)
                    self.paramFields.append(selectorWidget)


    def isReadyToExec(self):
        return self.readyToExec

    def packageForExecution(self):
        algName = self.selectAlgBox.get()
        paramsList = []
        paramsDict = {}
        if self.alg == "Neural Network (Keras)":
            paramsDict["Network"] = self.paramFields[0].get()
            algType = "Classification"
        else:
            for pf in self.paramFields:
                paramsList.append(pf.get())
            cur = 0
            params = []
            algDict = {}
            for alg in self.listOfAlgorithms:
                if alg.get("AlgName") == algName:
                    algDict = alg
                    algType = algDict.get("Type")
                    break
            for param in algDict.get("Simple Parameters"):
                paramsDict[param.get("ParamName")] = paramsList[cur]
                cur += 1
            for param in algDict.get("Advanced Parameters"):
                paramsDict[param.get("ParamName")] = paramsList[cur]
                cur += 1
        print(paramsDict)
        return {"Algorithm":algName, "Type":algType, "Params":paramsDict}

    def initializeParamsDict(self):
        self.listOfAlgorithms = []
        for alg in Algorithm:
            self.listOfAlgorithms.append(alg.value)
