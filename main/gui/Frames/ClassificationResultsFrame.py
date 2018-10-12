from tkinter import Frame, Entry, Label,Button
from tkinter import filedialog
import pickle
from main.gui.Utilities.Colors import Color

class ClassificationAlgorithmResultsFrame(Frame):
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
        if self.result.get("Algorithm") == "Decision Tree":
            model = self.result.get("Model")
            params = Label(master=self, bg=Color.BACKGROUND_COLOR.value,
                           text="Parameters:" +
                                "\nclass_weight=" + str(model.class_weight) +
                                "\ncriterion=" + str(model.criterion) +
                                "\nmax_depth=" + str(model.max_depth) +
                                "\nmax_features=" + str(model.max_features) +
                                "\nmax_leaf_nodes=" + str(model.max_leaf_nodes)
            )
            params.grid(row=self.curRow, column=0)
            self.curRow += 1

    def addStatistics(self):
        accuracyLabel = Label(master=self, bg=Color.BACKGROUND_COLOR.value, text="Accuracy: " + str(self.result.get("Statistics").get("Accuracy")))
        accuracyLabel.grid(row=self.curRow, column=0)
        self.curRow += 1

        if self.result.get("Statistics").get("Precision") != None:
            precLabel = Label(master=self, bg=Color.BACKGROUND_COLOR.value, text="Precision: " + str(self.result.get("Statistics").get("Precision")))
            precLabel.grid(row=self.curRow, column=0)
            self.curRow += 1

            recLabel = Label(master=self, bg=Color.BACKGROUND_COLOR.value, text="Recall: " + str(self.result.get("Statistics").get("Recall")))
            recLabel.grid(row=self.curRow, column=0)
            self.curRow += 1

            f1Label = Label(master=self, bg=Color.BACKGROUND_COLOR.value, text="F1: " + str(self.result.get("Statistics").get("F1")))
            f1Label.grid(row=self.curRow, column=0)
            self.curRow += 1

    def addPickleBtn(self):
        pickleModelBtn = Button(self, text='Pickle Model', width= 15, bg=Color.GOOD_BUTTON_COLOR.value, command=lambda : self.pickleModel())
        pickleModelBtn.grid(row=self.curRow, column=0)
        self.curRow += 1

    def pickleModel(self):
        fileToPickleTo = filedialog.asksaveasfile(mode='wb', defaultextension=".MLModel")
        if fileToPickleTo != None:
            pickle.dump(self.result.get("Model"), fileToPickleTo)
        fileToPickleTo.close()

