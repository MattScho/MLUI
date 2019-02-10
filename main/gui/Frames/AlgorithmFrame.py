from tkinter import ttk
from tkinter import *
from main.gui.Utilities.ToolTip import ToolTip
from main.gui.Utilities.Settings import Settings
from main.Algorithms.AlgorithmsEnum import Algorithm

'''
Algorithm Frame for defining an order to send for training
'''
class AlgorithmFrame(Frame):
    def __init__(self, parent, algor=None):
        Frame.__init__(self, master=parent, bg=Settings.BACKGROUND_COLOR.value)
        self.readyToExec = False

        self.initializeParamsDict()
        self.paramFields = []

        self.algs = []
        for alg in self.listOfAlgorithms:
            if parent.getSelectedTypeOfLearning() == alg.get("Type"):
                self.algs.append(alg.get("AlgName"))
        self.selectAlgBox = ttk.Combobox(master=self, font=Settings.REGULAR_FONT.value,state='readonly', values=self.algs)
        self.selectAlgBox.pack(padx=5, pady=5)
        self.removeBtn = Button(master=self, font=Settings.REGULAR_FONT.value, text="Remove",bg=Settings.BAD_BUTTON_COLOR.value, command=lambda : parent.removeAlgFrame(self))
        self.removeBtn.pack(padx=5, pady=5)
        if algor != None:
            self.selectAlgBox.current(self.algs.index(algor))
            self.buildParameterInputs(algor)
        self.selectAlgBox.bind("<<ComboboxSelected>>", lambda _: self.buildParameterInputs(self.selectAlgBox.selection_get()))


    def buildParameterInputs(self, alg):
        self.selectAlgBox.config(state="disabled")
        algToUse = {}
        for algor in self.listOfAlgorithms:
            if algor.get("AlgName") == alg:
                algToUse = algor
                break
        for param in algToUse.get("Simple Parameters"):
            label = Label(master=self, text=param.get("ParamName"), fg=Settings.FONT_COLOR.value, font=Settings.REGULAR_FONT.value, bg=Settings.BACKGROUND_COLOR.value)
            label.pack(padx=5, pady=5)
            ToolTip(label, param.get("Simple Description"))
            if param.get("Type") == "int" or param.get("Type") == "double" or param.get("Type") == "float":
                textWidget = Entry(master=self,font=Settings.REGULAR_FONT.value, bg=Settings.TEXTFIELD_COLOR.value)
                textWidget.insert(END, param.get("Default"))
                textWidget.pack()
                self.paramFields.append(textWidget)
            elif param.get("Type") == "bool":
                selectorWidget = ttk.Combobox(master=self, state='readonly',font=Settings.REGULAR_FONT.value, values=[True, False])
                selectorWidget.current(0)
                selectorWidget.pack()
                self.paramFields.append(selectorWidget)
            elif param.get("Type") == "options":
                selectorWidget = ttk.Combobox(master=self, state='readonly',font=Settings.REGULAR_FONT.value, values=param.get("Default"))
                selectorWidget.current(0)
                selectorWidget.pack()
                self.paramFields.append(selectorWidget)


    def isReadyToExec(self):
        return self.readyToExec

    def packageForExecution(self):
        algName = self.selectAlgBox.get()
        paramsList = []
        paramsDict = {}
        for pf in self.paramFields:
            paramsList.append(pf.get())
        cur = 0
        params = []
        algDict = {}
        for alg in self.listOfAlgorithms:
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
