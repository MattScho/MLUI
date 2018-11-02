from tkinter import Frame, Label
from main.AlgExecution.Executioner.Executioner import  Executioner

from main.gui.Utilities.Colors import Color
class WaitingFrame(Frame):
    def __init__(self, GUI, orders, typeOfData, allData=None, trainingData=None, testingData=None):
        Frame.__init__(self, bg=Color.BACKGROUND_COLOR.value)
        self.grid()
        waiting = Label(text="Executing")
        waiting.grid(row=0, column=0)
        res = None
        print("TYPE: " + typeOfData)
        if typeOfData == "All-n-One":
            res = Executioner(orders, typeOfData, allData=allData).execute()
        elif typeOfData == "1 Training 1 Testing":
            res = Executioner(orders, typeOfData, testingData=testingData, trainingData=trainingData).execute()
        GUI.newResultFrame(res)