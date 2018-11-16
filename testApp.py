import tkinter as tk
from SFrame import ScrolledFrame

def add(frame):
    l = tk.Label(frame.canv, text="Finally")
    l.grid()

root = tk.Tk()

frame = ScrolledFrame(root)
frame.grid()

btn = tk.Button(frame.canv, text="add", command=lambda : add(frame))
btn.grid()


root.mainloop()
