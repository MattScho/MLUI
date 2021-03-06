from tkinter import Frame, Entry, Label,Button
from tkinter import filedialog
import pickle
from main.gui.Utilities.Settings import Settings

'''
Displays results of a clustering algorithm
'''
class ClusteringAlgorithmResultsFrame(Frame):
    def __init__(self, parent, res):
        Frame.__init__(self, master=parent, bg=Settings.BACKGROUND_COLOR.value)
        self.result = res
        self.addHeader()
        self.addParameters()
        self.addStatistics()
        self.addPickleBtn()

    def addHeader(self):
        algName = Label(master=self, bg=Settings.BACKGROUND_COLOR.value, text=self.result.get("Algorithm"))
        algName.pack()

    def addParameters(self):
        model = self.result.get("Model")
        paramsOutput = ""
        paramsDict = self.result.get("Params")
        for param in paramsDict.keys():
            paramsOutput += param + " = " + str(paramsDict[param]) + "\n"
        params = Label(master=self, bg=Settings.BACKGROUND_COLOR.value,
                       text="Parameters:\n" + paramsOutput
                       )
        params.pack()

    def addStatistics(self):
        accuracyLabel = Label(master=self, bg=Settings.BACKGROUND_COLOR.value,
                              text="Accuracy: " + str(self.result.get("Statistics").get("Accuracy")))
        accuracyLabel.pack()

    def addPickleBtn(self):
        pickleModelBtn = Button(self, text='Pickle Model', width= 15, bg=Settings.GOOD_BUTTON_COLOR.value, command=lambda : self.pickleModel())
        pickleModelBtn.pack()

    def pickleModel(self):
        fileToPickleTo = filedialog.asksaveasfile(mode='wb', defaultextension=".MLModel")
        if fileToPickleTo != None:
            pickle.dump(self.result.get("Model"), fileToPickleTo)
        fileToPickleTo.close()
