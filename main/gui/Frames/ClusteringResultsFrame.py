from tkinter import Frame, Entry, Label,Button
from tkinter import filedialog
import pickle
from main.gui.Utilities.Colors import Color

class ClusteringAlgorithmResultsFrame(Frame):
    def __init__(self, parent, res):
        Frame.__init__(self, master=parent, bg=Color.BACKGROUND_COLOR.value)
        self.result = res
        self.curRow = 0
        self.addHeader()
        self.addParameters()
        self.addStatistics()
        self.addPickleBtn()

    def addHeader(self):
        algName = Label(master=self, bg=Color.BACKGROUND_COLOR.value, text=self.result.get("Algorithm"))
        algName.grid(row=self.curRow, column=0)
        self.curRow += 1

    def addParameters(self):
        pass

    def addStatistics(self):
        accuracyLabel = Label(master=self, bg=Color.BACKGROUND_COLOR.value,
                              text="Accuracy: " + str(self.result.get("Statistics").get("Accuracy")))
        accuracyLabel.grid(row=self.curRow, column=0)
        self.curRow += 1

    def addPickleBtn(self):
        pickleModelBtn = Button(self, text='Pickle Model', width= 15, bg=Color.GOOD_BUTTON_COLOR.value, command=lambda : self.pickleModel())
        pickleModelBtn.grid(row=self.curRow, column=0)
        self.curRow += 1

    def pickleModel(self):
        fileToPickleTo = filedialog.askopenfilename()
        pickle.dump(self.result.get("Model"), open(fileToPickleTo, 'wb'))

