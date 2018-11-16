from tkinter import *
from tkinter import ttk
from main.gui.Frames.ClassificationResultsFrame import ClassificationAlgorithmResultsFrame
from main.gui.Frames.RegressionResultsFrame import RegressionAlgorithmResultsFrame
from main.gui.Frames.ClusteringResultsFrame import ClusteringAlgorithmResultsFrame
from main.gui.Utilities.Settings import Settings
from main.AlgExecution.Executioner.AdvExecutioner import Executioner
import threading

'''
Takes orders and sends them to be trained, while training a progress bar is shown
When training for an order is complete adds a Frame based on the type of learning done
to this Frame
'''
class AdvResultFrame(Frame):
    '''
    Initializes the frame by starting the execution of orders
    '''
    def __init__(self, GUI, parent, orders, typeOfData, allData=None, trainingData=None, testingData=None, columnsDict=None):
        Frame.__init__(self, master=parent, bg=Settings.BACKGROUND_COLOR.value)
        self.GUI = GUI
        self.pack()
        for order in orders:
            progBar = ttk.Progressbar(self, mode='indeterminate')
            progBar.pack()
            self.start_submit_thread(order, typeOfData, allData, trainingData, testingData, progBar, columnsDict)


    '''
    Generates a Classification results frame
    '''
    def addClassificationInnerResultFrame(self, result):
        algResFrame = ClassificationAlgorithmResultsFrame(self, result)
        return algResFrame

    '''
    Generate a Regression results frame
    '''
    def addRegressionInnerResultFrame(self, result):
        algResFrame = RegressionAlgorithmResultsFrame(self, result)
        return algResFrame

    '''
    Generates a Clustering results frame
    '''
    def addClusteringInnerResultFrame(self, result):
        algResFrame = ClusteringAlgorithmResultsFrame(self, result)
        return algResFrame

    '''
    
    BEWARE BELOW, multi-threaded python to call Executioner to train the models
    needs documentation
    
    
    '''




    def run(self, orders, typeOfData, allData=None, trainingData=None, testingData=None, columnsDict=None):
        res = None
        if typeOfData == "All-n-One":
            res = Executioner(orders, typeOfData, columnsDict, allData=allData).execute()
        elif typeOfData == "1 Training 1 Testing":
            res = Executioner(orders, typeOfData, columnsDict, testingData=testingData, trainingData=trainingData).execute()
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


    def submit(self, orders, typeOfData, allData, trainingData, testingData, columnsDict):
        self.run(orders, typeOfData, allData, trainingData, testingData, columnsDict)

    def start_submit_thread(self, orders, typeOfData, allData, trainingData, testingData, progBar, columnsDict):
        submit_thread = threading.Thread(target=self.submit, args=(orders, typeOfData, allData, trainingData, testingData, columnsDict))
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