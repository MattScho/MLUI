from tkinter import Frame, Entry, Label,Button
from tkinter import filedialog
import pickle
from main.gui.Utilities.Settings import Settings

class RegressionAlgorithmResultsFrame(Frame):
    def __init__(self, parent, res):
        Frame.__init__(self, master=parent, bg=Settings.BACKGROUND_COLOR.value)
        self.result = res
        self.curRow = 0
        self.addHeader()
        self.addParameters()
        self.addStatistics()
        self.addPickleBtn()

    def addHeader(self):
        algName = Label(master=self, font=Settings.REGULAR_FONT.value,bg=Settings.BACKGROUND_COLOR.value, text=self.result.get("Algorithm"))
        algName.pack()

    def addParameters(self):
        paramsOutput = ""
        paramsDict = self.result.get("Params")
        for param in paramsDict.keys():
            paramsOutput += param + " = " + str(paramsDict[param]) + "\n"
        params = Label(master=self, font=Settings.REGULAR_FONT.value, bg=Settings.BACKGROUND_COLOR.value,
                       text="Parameters:\n" + paramsOutput
                       )
        params.pack()

    def addStatistics(self):
        meanSquaredErrorLabel = Label(master=self, font=Settings.REGULAR_FONT.value, bg=Settings.BACKGROUND_COLOR.value, text="Mean Squared Error: " + str(self.result.get("Statistics").get("Mean Squared Error")))
        meanSquaredErrorLabel.pack()
        trainTimeLabel = Label(master=self, font=Settings.REGULAR_FONT.value, bg=Settings.BACKGROUND_COLOR.value, text="Training Time: " + str(self.result.get("Statistics").get("Fit Time")) + " seconds")
        trainTimeLabel.pack()

    def addPickleBtn(self):
        pickleModelBtn = Button(self, text='Pickle Model', font=Settings.REGULAR_FONT.value, width= 15, bg=Settings.GOOD_BUTTON_COLOR.value, command=lambda : self.pickleModel())
        pickleModelBtn.pack()

    def pickleModel(self):
        fileToPickleTo = filedialog.asksaveasfile(mode='wb', defaultextension=".MLModel")
        if fileToPickleTo != None:
            pickle.dump(self.result.get("Model"), fileToPickleTo)
        fileToPickleTo.close()