from tkinter import *
from main.gui.Frames.CreateModelFrame import ModelCreationFrame
from main.gui.Frames.CreateAdvancedModelFrame import AdvancedModelCreationFrame
from main.gui.Frames.HomeFrame import HomeFrame
from main.gui.Frames.LoadModelFrame import LoadModelFrame
from main.gui.Frames.ResultFrame import ResultFrame
from main.gui.Frames.AdvResultFrame import AdvResultFrame
from main.gui.Utilities.Settings import Settings
from main.gui.Utilities.SFrame import ScrolledFrame
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
        self.root.geometry("1200x900")

        # Set background color
        self.root.configure(background=Settings.BACKGROUND_COLOR.value)


        # The frame we will act on clearing and rebuilding for new scenes
        self.mainFrame = ScrolledFrame(self.root, bg=Settings.BACKGROUND_COLOR.value, width=700, height=700) # Don't allow the widgets inside to determine the frame's width / height

        self.mainFrame.pack()


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
        self.mainFrame = ScrolledFrame(self.root, bg=Settings.BACKGROUND_COLOR.value, width=1700, height=1700) # Don't allow the widgets inside to determine the frame's width / height

        self.mainFrame.pack_propagate(0)
        self.mainFrame.pack(fill=BOTH, expand=False)


    '''
    Sets the main frame of the GUI to the home frame
    '''
    def newHomeFrame(self):
        self.clearMainFrame()
        HomeFrame(self, self.mainFrame.canv)

    '''
    Sets the main frame of the GUI to the Model Creation frame
    '''
    def newModelCreationFrame(self):
        self.clearMainFrame()
        ModelCreationFrame(self, self.mainFrame.canv)

    '''
    Sets the main frame of the GUI to the Model Creation frame
    '''
    def newAdvModelCreationFrame(self):
        self.clearMainFrame()
        AdvancedModelCreationFrame(self, self.mainFrame.canv)

    '''
    Sets the main frame of the GUI to the Load Model frame
    '''

    def newLoadModelFrame(self):
        self.clearMainFrame()
        LoadModelFrame(self, self.mainFrame.canv)

    '''
    Sets the main frame of the GUI to the Result frame
    '''
    def newResultFrame(self, orders, typeOfData, allData=None, trainingData=None, testingData=None, columnsDict=None):
        self.clearMainFrame()
        ResultFrame(self, self.mainFrame.canv, orders, typeOfData, allData, trainingData, testingData, columnsDict)

    '''
   Sets the main frame of the GUI to the Result frame
   '''

    def newAdvResultFrame(self, orders, typeOfData, allData=None, trainingData=None, testingData=None, columnsDict=None):
        self.clearMainFrame()
        AdvResultFrame(self, self.mainFrame.canv, orders, typeOfData, allData, trainingData, testingData,
                                     columnsDict)
    '''
    Gets the root of the tk GUI
    '''
    def getRoot(self):
        return self.root

    def getMainFrame(self):
        return self.mainFrame