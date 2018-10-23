from enum import Enum
from tkinter import font

settings = {}
with open("./settings.txt", "r") as file:
    individualSettings = file.read().split('\n')
for setting in individualSettings:
    if not (setting == '' or setting[0] == '#'):
        setting = setting.split(" = ")
        settings[setting[0]] = setting[1]

class Settings(Enum):
    BACKGROUND_COLOR = settings["BACKGROUND_COLOR"]
    GOOD_BUTTON_COLOR = settings["GOOD_BUTTON_COLOR"]
    BAD_BUTTON_COLOR = settings["BAD_BUTTON_COLOR"]
    FRAME_BORDER_COLOR = settings["FRAME_BORDER_COLOR"]
    TEXTFIELD_COLOR = settings["TEXTFIELD_COLOR"]
    TOOLTIP_COLOR = settings["TOOLTIP_COLOR"]
    REGULAR_BUTTON1_COLOR = settings["REGULAR_BUTTON1_COLOR"]
    REGULAR_BUTTON2_COLOR = settings["REGULAR_BUTTON2_COLOR"]
    REGULAR_FONT = (settings["REGULAR_FONT_FAMILY"],settings["REGULAR_FONT_SIZE"],settings["REGULAR_FONT_WEIGHT"])