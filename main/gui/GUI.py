from tkinter import *
from tkinter.tix import ScrolledWindow
from main.gui.Frames.CreateModelFrame import ModelCreationFrame
from main.gui.Frames.HomeFrame import HomeFrame
from main.gui.Frames.ResultFrame import ResultFrame
from main.gui.Utilities.Colors import Color
import threading
'''
The base/backend/persistent GUI object that will facilitate the application

Here is the stage on which scenes will come and go
'''
class GUI:
    '''
    Launch the application's window and begin with the 'Home' scene
    '''
    def __init__(self):

        # Base Window (really frame)
        self.root = Tk()

        # make the canvas expandable
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.configure(background=Color.BACKGROUND_COLOR.value)

        # The frame we will act on clearing and rebuilding for new scenes
        self.mainFrame = Frame(self.root)
        self.mainFrame.pack()# Fill

        # Set secondary characteristics of frame
        self.root.title("SciUI Learn")

        # Set first scene, the welcome
        self.newHomeFrame()

        # Begin
        self.root.mainloop()

    '''
    Clears out current widgets and resets GUI to accept new Frame
    
    Sweeps off the stage for the next scene to come in
    '''
    def clearMainFrame(self):
        # Destruction of current widgets
        self.mainFrame.destroy()

        # Reinitialization
        self.mainFrame = Frame(self.root)
        self.mainFrame.pack()


    def newHomeFrame(self):
        self.clearMainFrame()
        self.mainFrame = HomeFrame(self)

    def newModelCreationFrame(self):
        self.clearMainFrame()
        self.mainFrame = ModelCreationFrame(self)

    def newResultFrame(self, orders, typeOfData, allData=None, trainingData=None, testingData=None):
        self.clearMainFrame()
        self.mainFrame = ResultFrame(self, orders, typeOfData, allData, trainingData, testingData)

    def getRoot(self):
        return self.root