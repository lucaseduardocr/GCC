from tkinter import *
from tkinter import ttk

class Application:
    def __init__(self, master=None):
        #frm = frame
        frm = ttk.Frame(root, padding=100)
        frm.grid()
        ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
        ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root = Tk()
Application(root)
root.mainloop()