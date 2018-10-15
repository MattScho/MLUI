from tkinter import Frame, Entry, Label,Button
from tkinter import filedialog
import pickle
from main.gui.Utilities.Colors import Color

class ClassificationAlgorithmResultsFrame(Frame):
    def __init__(self, parent, res):
        Frame.__init__(self, master=parent, bg=Color.BACKGROUND_COLOR.value)
        print("HERE")
        self.pack()
        self.result = res
        self.addHeader()
        self.addParameters()
        self.addStatistics()
        self.addPickleBtn()

    def addHeader(self):
        algName = Label(master=self, bg=Color.BACKGROUND_COLOR.value, text=self.result.get("Algorithm"))
        algName.pack()

    def addParameters(self):
        model = self.result.get("Model")
        paramsOutput = ""
        paramsDict = model.get_params()
        for param in paramsDict.keys():
            paramsOutput += param + " = " + str(paramsDict[param]) + "\n"
        params = Label(master=self, bg=Color.BACKGROUND_COLOR.value,
                       text="Parameters:\n" + paramsOutput
        )
        params.pack()

    def addStatistics(self):
        accuracyLabel = Label(master=self, bg=Color.BACKGROUND_COLOR.value, text="Accuracy: " + str(self.result.get("Statistics").get("Accuracy")))
        accuracyLabel.pack()

        if self.result.get("Statistics").get("Precision") != None:
            precLabel = Label(master=self, bg=Color.BACKGROUND_COLOR.value, text="Precision: " + str(self.result.get("Statistics").get("Precision")))
            precLabel.pack()

            recLabel = Label(master=self, bg=Color.BACKGROUND_COLOR.value, text="Recall: " + str(self.result.get("Statistics").get("Recall")))
            recLabel.pack()

            f1Label = Label(master=self, bg=Color.BACKGROUND_COLOR.value, text="F1: " + str(self.result.get("Statistics").get("F1")))
            f1Label.pack()

    def addPickleBtn(self):
        pickleModelBtn = Button(self, text='Pickle Model', width= 15, bg=Color.GOOD_BUTTON_COLOR.value, command=lambda : self.pickleModel())
        pickleModelBtn.pack()

    def pickleModel(self):
        fileToPickleTo = filedialog.asksaveasfile(mode='wb', defaultextension=".MLModel")
        if fileToPickleTo != None:
            pickle.dump(self.result.get("Model"), fileToPickleTo)
        fileToPickleTo.close()

