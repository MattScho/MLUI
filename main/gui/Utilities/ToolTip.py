import tkinter as tk
from main.gui.Utilities.Colors import Color

class ToolTip():

    def __init__(self, tk_widget, info):
        self.tk_widget = tk_widget
        self.tk_widget.bind("<Enter>", self.show)
        self.tk_widget.bind("<Leave>", self.destroy)
        self.info = info

    def show(self, event=None):
        x, y, _, __ = self.tk_widget.bbox("insert")
        x += self.tk_widget.winfo_rootx() + 25
        y += self.tk_widget.winfo_rooty() + 20
        self.tw = tk.Toplevel(self.tk_widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.info, background=Color.TOOLTIP_COLOR.value)
        label.pack(ipadx=1)

    def destroy(self, event=None):
        if self.tw:
            self.tw.destroy()