from tkinter import Button, Frame
import os
from main.gui.Utilities.Settings import Settings
import subprocess

def launchVisualizationTool():
    os.system("calc")

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
    def __init__(self, GUI, parent):
        # Construct super class
        Frame.__init__(self, master=parent, bg=Settings.BACKGROUND_COLOR.value)
        # Lines things up
        self.pack()

        # The 'Create Model' button, onClick launches the CreateModelFrame
        createModelButton = Button(self, text="Create Model", height=8, width=32, font=Settings.REGULAR_FONT.value, bg=Settings.GOOD_BUTTON_COLOR.value, command=lambda :GUI.newModelCreationFrame())
        createModelButton.pack(padx=10, pady=10)

        createAdvModelButton = Button(self, text="Create Advanced Model", height=8, width=32, font=Settings.REGULAR_FONT.value, bg=Settings.GOOD_BUTTON_COLOR.value, command=lambda :GUI.newAdvModelCreationFrame())
        createAdvModelButton.pack(padx=10, pady=10)

        # The 'Load Model' button onClick launches the LoadModelFrame
        loadModelButton = Button(self, text="Load Model", height=8, width=32, font=Settings.REGULAR_FONT.value, bg=Settings.GOOD_BUTTON_COLOR.value, command=lambda :GUI.newLoadModelFrame())
        loadModelButton.pack(padx=10, pady=10)

        # The 'Visualization Tool' button onClick launches defined visualization software
        visualizationButton = Button(self, text="Visualization Tool", height=8, width=32, font=Settings.REGULAR_FONT.value, bg=Settings.GOOD_BUTTON_COLOR.value, command= lambda : launchVisualizationTool())
        visualizationButton.pack(padx=10, pady=10)

        # The 'Help' button onClick launches the HelpFrame
        helpButton = Button(self, text="Help", height=8, width=32, font=Settings.REGULAR_FONT.value, bg=Settings.GOOD_BUTTON_COLOR.value, command= lambda : subprocess.Popen(["../main/Resources/Help/Help.pdf"],shell=True))
        helpButton.pack(padx=10, pady=10)