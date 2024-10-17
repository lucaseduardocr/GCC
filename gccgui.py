from tkinter import *
from tkinter import ttk


class Application:
    def __init__(self, master=None):
        self.widget_master = Frame(master)
        self.widget_master.pack()
        self.msg = Label(self.widget_master, text="Primeiro Widget")
        self.msg.pack()
root = Tk()
width_screen = (root.winfo_screenwidth())
height_screen = (root.winfo_screenheight())
root.geometry("700x400")
root.maxsize(width=width_screen, height=height_screen)
root.minsize(width=800, height=500)
Application(root)
root.mainloop()