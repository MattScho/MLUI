from tkinter import Frame, Entry, Label,Button
from tkinter import filedialog
import pickle
from main.gui.Utilities.Settings import Settings

'''
Displays results of a classification algorithm
'''
class ClassificationAlgorithmResultsFrame(Frame):
    def __init__(self, parent, res):
        Frame.__init__(self, master=parent, bg=Settings.BACKGROUND_COLOR.value)
        self.pack()
        self.result = res
        self.addHeader()
        self.addParameters()
        self.addStatistics()
        self.addPickleBtn()

    def addHeader(self):
        algName = Label(master=self, fg=Settings.FONT_COLOR.value, bg=Settings.BACKGROUND_COLOR.value, font=Settings.REGULAR_FONT,text=self.result.get("Algorithm"))
        algName.pack()

    def addParameters(self):
        paramsOutput = ""
        paramsDict = self.result.get("Params")
        for param in paramsDict.keys():
            paramsOutput += param + " = " + str(paramsDict[param]) + "\n"
        params = Label(master=self,font=Settings.REGULAR_FONT.value, fg=Settings.FONT_COLOR.value, bg=Settings.BACKGROUND_COLOR.value,
                       text="Parameters:\n" + paramsOutput
        )
        params.pack()

    def addStatistics(self):
        accuracyLabel = Label(master=self, fg=Settings.FONT_COLOR.value, bg=Settings.BACKGROUND_COLOR.value,font=Settings.REGULAR_FONT, text="Accuracy: " + str(self.result.get("Statistics").get("Accuracy")))
        accuracyLabel.pack()

        precLabel = Label(master=self, fg=Settings.FONT_COLOR.value, bg=Settings.BACKGROUND_COLOR.value,font=Settings.REGULAR_FONT, text="Precision: " + str(self.result.get("Statistics").get("Precision")))
        precLabel.pack()

        recLabel = Label(master=self, fg=Settings.FONT_COLOR.value, bg=Settings.BACKGROUND_COLOR.value,font=Settings.REGULAR_FONT, text="Recall: " + str(self.result.get("Statistics").get("Recall")))
        recLabel.pack()

        f1Label = Label(master=self, fg=Settings.FONT_COLOR.value, bg=Settings.BACKGROUND_COLOR.value,font=Settings.REGULAR_FONT, text="F1: " + str(self.result.get("Statistics").get("F1")))
        f1Label.pack()

        trainTimeLabel = Label(master=self, fg=Settings.FONT_COLOR.value, font=Settings.REGULAR_FONT.value, bg=Settings.BACKGROUND_COLOR.value, text="Training Time: " + str(self.result.get("Statistics").get("Fit Time")) + " seconds")
        trainTimeLabel.pack()

    def addPickleBtn(self):
        pickleModelBtn = Button(self, text='Pickle Model', width= 15,font=Settings.REGULAR_FONT, bg=Settings.GOOD_BUTTON_COLOR.value, command=lambda : self.pickleModel())
        pickleModelBtn.pack()

        outputResultCSVBtn = Button(self, text="Results as CSV", width= 15,font=Settings.REGULAR_FONT, bg=Settings.GOOD_BUTTON_COLOR.value, command=lambda : self.pickleModel())
        outputResultCSVBtn.pack()

        if self.result.get("Algorithm") == "Perceptron":
            outputWeightsToCSVBtn = Button(self, text="Weights as CSV", width= 15,font=Settings.REGULAR_FONT, bg=Settings.GOOD_BUTTON_COLOR.value, command=lambda : self.pickleModel())
            outputWeightsToCSVBtn.pack()


    def pickleModel(self):
        fileToPickleTo = filedialog.asksaveasfile(mode='wb', defaultextension=".MLModel")
        if fileToPickleTo != None:
            pickle.dump(self.result.get("Model"), fileToPickleTo)
        fileToPickleTo.close()

