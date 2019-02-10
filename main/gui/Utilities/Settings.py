from enum import Enum

# To store settings
settings = {}

# Read in settings from settings.txt file
with open("..\main\settings.txt", "r") as file:
    # Read contents of file in as a list
    individualSettings = file.read().split('\n')
    # closes file
    file.close()

# Turn settings into a dict
for setting in individualSettings:
    # This allows for blank lines and comment lines
    if not (setting == '' or setting[0] == '#'):
        # Turn entry into a len 2 list first being target and second being the value
        setting = setting.split(" = ")
        # Store setting in settings dict
        settings[setting[0]] = setting[1]

'''
Settings enumerations
'''
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
    FONT_COLOR = settings["FONT_COLOR"]
    VISUALIZATION_TOOL = settings["VISUALIZATION_TOOL"]
