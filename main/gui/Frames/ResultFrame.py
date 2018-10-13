from tkinter import Frame, Label
from main.gui.Frames.ClassificationResultsFrame import ClassificationAlgorithmResultsFrame
from main.gui.Frames.RegressionResultsFrame import RegressionAlgorithmResultsFrame
from main.gui.Frames.ClusteringResultsFrame import ClusteringAlgorithmResultsFrame
from main.gui.Utilities.Colors import Color
import matplotlib.pyplot as plt
from matplotlib.axes._axes import Axes
from matplotlib.figure import Figure

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
        accuracyStats = []
        f1Stats = []
        precisionStats = []
        recallStats = []
        names = []
        if self.type == "Classification":
            for result in res:
                self.addClassificationInnerResultFrame(result)
                accuracyStats.append(result.get("Statistics").get("Accuracy"))
                names.append(result.get("Algorithm"))
                if not result.get("Statistics").get("F1") == None:
                    f1Stats.append(result.get("Statistics").get("F1"))
                    precisionStats.append(result.get("Statistics").get("Precision"))
                    recallStats.append(result.get("Statistics").get("Recall"))

            f1 = plt.figure()
            ax1 = f1.add_subplot(111)
            ax1.plot(names, accuracyStats)

            if not len(f1Stats) == 0:
                f2 = plt.figure()
                ax2 = f2.add_subplot(111)
                ax2.plot(names, f1Stats, label="F1")
                f3 = plt.figure()
                ax3 = f3.add_subplot(111)
                ax3.plot(names, precisionStats, label="Precision")
                f4 = plt.figure()
                ax4 = f4.add_subplot(111)
                ax4.plot(names, recallStats, label="Recall")
            plt.show()
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