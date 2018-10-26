from tkinter import *
from tkinter import ttk
from main.gui.Frames.ClassificationResultsFrame import ClassificationAlgorithmResultsFrame
from main.gui.Frames.RegressionResultsFrame import RegressionAlgorithmResultsFrame
from main.gui.Frames.ClusteringResultsFrame import ClusteringAlgorithmResultsFrame
from main.gui.Utilities.Settings import Settings
from main.AlgExecution.Executioner.Executioner import Executioner
import threading

class ResultFrame(Frame):
    def __init__(self, GUI, orders, typeOfData, allData=None, trainingData=None, testingData=None):

        Frame.__init__(self, bg=Settings.BACKGROUND_COLOR.value)
        self.scrollbar = Scrollbar(self)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.GUI = GUI
        self.pack()
        print("Orders: " + str(orders))
        for order in orders:
            progBar = ttk.Progressbar(self, mode='indeterminate')
            progBar.pack()
            self.start_submit_thread(order, typeOfData, allData, trainingData, testingData, progBar)


    def addClassificationInnerResultFrame(self, result):
        algResFrame = ClassificationAlgorithmResultsFrame(self, result)
        return algResFrame

    def addRegressionInnerResultFrame(self, result):
        algResFrame = RegressionAlgorithmResultsFrame(self, result)
        return algResFrame

    def addClusteringInnerResultFrame(self, result):
        algResFrame = ClusteringAlgorithmResultsFrame(self, result)
        return algResFrame

    def run(self, orders, typeOfData, allData=None, trainingData=None, testingData=None):
        res = None
        if typeOfData == "All-n-One":
            res = Executioner(orders, typeOfData, allData=allData).execute()
        elif typeOfData == "1 Training 1 Testing":
            res = Executioner(orders, typeOfData, testingData=testingData, trainingData=trainingData).execute()
        typeOfLearning = res[0].get("Type")
        if typeOfLearning == "Classification":
            for result in res:
                self.addClassificationInnerResultFrame(result).pack()
        elif typeOfLearning == "Regression":
            for result in res:
                self.addRegressionInnerResultFrame(result).pack()
        elif typeOfLearning == "Clustering":
            for result in res:
                self.addClusteringInnerResultFrame(result).pack()


    def submit(self, orders, typeOfData, allData, trainingData, testingData):
        self.run(orders, typeOfData, allData, trainingData, testingData)

    def start_submit_thread(self, orders, typeOfData, allData, trainingData, testingData, progBar):
        submit_thread = threading.Thread(target=self.submit, args=(orders, typeOfData, allData, trainingData, testingData))
        submit_thread.daemon = True
        progBar.start()
        submit_thread.start()
        self.GUI.getRoot().after(20, self.check_submit_thread, progBar, submit_thread)

    def check_submit_thread(self, progBar, submit_thread):
        if submit_thread.is_alive():
            self.GUI.getRoot().after(20, self.check_submit_thread, progBar, submit_thread)
        else:
            progBar.stop()
            progBar.destroy()