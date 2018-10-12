from tkinter import Frame, Label
from main.AlgExecution.Executioner.Executioner import  Executioner

from main.gui.Utilities.Colors import Color
class WaitingFrame(Frame):
    def __init__(self, GUI, orders, typeOfData, data):
        Frame.__init__(self, bg=Color.BACKGROUND_COLOR.value)
        self.grid()
        waiting = Label(text="Executing")
        waiting.grid(row=0, column=0)
        res = Executioner(orders, data, typeOfData).execute()
        GUI.newResultFrame(res)