from tkinter import Frame
from tkinter import Button

from main.gui.Utilities.Colors import Color
'''
The welcoming frame of the app

Inherits from Frame

Shows three buttons: create model, load model, and help

create - launch CreateModelFrame, walks user through creating a model
load - launch LoadModelFrame, allows a user to test model
help - launch TutorialFrame, show user how to use the application
'''
class HomeFrame(Frame):

    '''
    Creates the frame with three buttons

    :param GUI, the parent GUI (stage) object used to launch new frames
    '''
    def __init__(self, GUI):
        # Construct super class with orangish background
        Frame.__init__(self,   bg=Color.BACKGROUND_COLOR.value)
        # Lines things up
        self.pack()

        # The 'Create Model' button, onClick launches the CreateModelFrame
        createModelButton = Button(self, text="Create Model", height=8, width=32, bg=Color.GOOD_BUTTON_COLOR.value, command=lambda :GUI.newModelCreationFrame())
        createModelButton.pack()

        createAdvModelButton = Button(self, text="Create Advanced Model", height=8, width=32, bg=Color.REGULAR_BUTTON2_COLOR.value)
        createAdvModelButton.pack()

        # The 'Load Model' button onClick launches the LoadModelFrame
        loadModelButton = Button(self, text="Load Model", height=8, width=32, bg=Color.REGULAR_BUTTON1_COLOR.value)
        loadModelButton.pack()

        # The 'Help' button onClick launches the HelpFrame
        helpButton = Button(self, text="Help", height=8, width=32, bg=Color.GOOD_BUTTON_COLOR.value)
        helpButton.pack()