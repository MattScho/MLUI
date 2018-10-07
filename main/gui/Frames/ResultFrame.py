from tkinter import Frame, Label
from main.gui.Frames.ClassificationResultsFrame import ClassificationAlgorithmResultsFrame
from main.gui.Frames.RegressionResultsFrame import RegressionAlgorithmResultsFrame
from main.gui.Frames.ClusteringResultsFrame import ClusteringAlgorithmResultsFrame
from main.gui.Utilities.Colors import Color
class ResultFrame(Frame):
    def __init__(self, GUI, res):
        Frame.__init__(self, bg=Color.BACKGROUND_COLOR.value)
        print(res)
        self.GUI = GUI
        self.grid()
        self.curRow = 0
        self.type = res[0].get("Type")
        self.typeOfFrame = Label(text=self.type, bg=Color.BACKGROUND_COLOR.value)
        self.typeOfFrame.grid(row=self.curRow, column=0)
        self.curRow += 1
        if self.type == "Classification":
            for result in res:
                self.addClassificationInnerResultFrame(result)
        elif self.type == "Regression":
            for result in res:
                self.addRegressionInnerResultFrame(result)
        elif self.type == "Clustering":
            for result in res:
                self.addClusteringInnerResultFrame(result)

    def addClassificationInnerResultFrame(self, result):
        algResFrame = ClassificationAlgorithmResultsFrame(self, result)
        algResFrame.grid(row=self.curRow, column=0)
        self.curRow += 1

    def addRegressionInnerResultFrame(self, result):
        algResFrame = RegressionAlgorithmResultsFrame(self, result)
        algResFrame.grid(row=self.curRow, column=0)
        self.curRow += 1

    def addClusteringInnerResultFrame(self, result):
        algResFrame = ClusteringAlgorithmResultsFrame(self, result)
        algResFrame.grid(row=self.curRow, column=0)
        self.curRow += 1