from tkinter import *
from main.gui.Frames.CreateModelFrame import ModelCreationFrame
from main.gui.Frames.HomeFrame import HomeFrame
from main.gui.Frames.LoadModelFrame import LoadModelFrame
from main.gui.Frames.ResultFrame import ResultFrame
from main.gui.Utilities.Settings import Settings
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


        # Set background color
        self.root.configure(background=Settings.BACKGROUND_COLOR.value)


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


    '''
    Sets the main frame of the GUI to the home frame
    '''
    def newHomeFrame(self):
        self.clearMainFrame()
        self.mainFrame = HomeFrame(self)

    '''
    Sets the main frame of the GUI to the Model Creation frame
    '''
    def newModelCreationFrame(self):
        self.clearMainFrame()
        self.mainFrame = ModelCreationFrame(self)

    '''
    Sets the main frame of the GUI to the Load Model frame
    '''

    def newLoadModelFrame(self):
        self.clearMainFrame()
        self.mainFrame = LoadModelFrame(self)

    '''
    Sets the main frame of the GUI to the Result frame
    '''
    def newResultFrame(self, orders, typeOfData, allData=None, trainingData=None, testingData=None):
        self.clearMainFrame()
        self.mainFrame = ResultFrame(self, orders, typeOfData, allData, trainingData, testingData)

    '''
    Gets the root of the tk GUI
    '''
    def getRoot(self):
        return self.root