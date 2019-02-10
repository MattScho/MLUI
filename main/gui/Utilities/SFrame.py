from tkinter import *
import tkinter as tk

from main.gui.Utilities.Settings import Settings
class ScrolledFrame(Frame):
    def __init__(self, parent,  *args, **kw):
        tk.Frame.__init__(self, parent,   *args, **kw)

        def _configureCanv(event):
            size = (self.canv.winfo_reqwidth(), self.canv.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if self.canv.winfo_reqwidth() != canvas.winfo_width():
                canvas.config(width=self.canv.winfo_reqwidth())

        def _configureCanvas(event):
            if self.canv.winfo_reqwidth() != canvas.winfo_width():
                canvas.itemconfigure(canv_id, width=canvas.winfo_width())

        vertscrollbar = Scrollbar(self, orient=VERTICAL)
        vertscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        
        canvas = Canvas(self, bg=Settings.BACKGROUND_COLOR.value, bd=0, yscrollcommand=vertscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        
        vertscrollbar.config(command=canvas.yview)

        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        self.canv = tk.Frame(canvas, bg=Settings.BACKGROUND_COLOR.value,width=768, height=576)
        canv_id = canvas.create_window(0, 0, window=self.canv, anchor=NW)


        self.canv.bind('<Configure>', _configureCanv)

        canvas.bind('<Configure>', _configureCanvas)