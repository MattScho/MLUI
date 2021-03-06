#Authors: Matthew Schofield
import tkinter as tk
from main.gui.Utilities.Settings import Settings

'''
A Tooltip to be bound to GUI widgets to supply extra information
'''
class ToolTip:

    '''
    Binds the tooltip to a given widget with supplied text

    :param tk_widget, widget to add tooltip to
    :param info, info to have on tooltip
    '''
    def __init__(self, tk_widget, info):
        self.tk_widget = tk_widget
        self.tk_widget.bind("<Enter>", self.show)
        self.tk_widget.bind("<Leave>", self.destroy)
        self.info = info

    '''
    Show the widget upon mosueover
    '''
    def show(self, event=None):
        x, y, _, __ = self.tk_widget.bbox("insert")
        x += self.tk_widget.winfo_rootx() + 25
        y += self.tk_widget.winfo_rooty() + 20
        self.tw = tk.Toplevel(self.tk_widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.info, font=Settings.REGULAR_FONT.value, background=Settings.TOOLTIP_COLOR.value)
        label.pack(ipadx=1)

    '''
    Cleans up after itself when mouse pointer leaves
    '''
    def destroy(self, event=None):
        if self.tw:
            self.tw.destroy()