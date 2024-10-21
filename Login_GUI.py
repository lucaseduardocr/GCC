from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
import Register_GUI


class Login_GUI:
    def __init__(self, master=None):
        #Containers
        self.first_container = Frame(master)
        self.first_container.pack()

        self.second_container = Frame(master)
        self.second_container.pack()

        self.third_container = Frame(master)
        self.third_container.pack()

        self.fourth_container = Frame(master)
        self.fourth_container.pack()

        #Containers

        #Text and other widgets

        #title
        self.login_title = Label(self.first_container, text="LOGIN", height=2, font=("Verdana", "30", "bold"))
        self.login_title.pack()
        
        #email part
        self.email_text = Label(self.second_container, text="EMAIL", width=12, font=("Verdana", "10", "bold"))
        self.email_text.pack(side=LEFT)

        self.email_box_entry = Entry(self.second_container, width= 40)
        self.email_box_entry.pack(side=RIGHT)

        #password part
        self.password_text = Label(self.third_container, text="PASSWORD", width=12, font=("Verdana", "10", "bold"))
        self.password_text.pack(side=LEFT)

        self.password_entry = Entry(self.third_container, width=40)
        self.password_entry.pack(side=RIGHT, pady=10)

        #bottons part
        def register():
            Register_GUI.Register_GUI()

        self.button_login = Button(self.fourth_container, width=20,height=2, text="LOGIN", font=("Verdana", "7", "bold"))
        self.button_login.pack(pady=5, padx=30)

        self.button_register = Button(self.fourth_container, width=20,height=2, text="REGISTER", font=("Verdana", "7", "bold"), command=register)
        self.button_register.pack(padx=30)


#FALTA CORREÇÃO DE ABERTURA PARA PARTE REGISTER


root = Tk()
width_screen = (root.winfo_screenwidth())
height_screen = (root.winfo_screenheight())
root.geometry("700x400")
root.maxsize(width=width_screen, height=height_screen)
root.minsize(width=800, height=500)
root.title("Login")
Login_GUI(root)
root.mainloop()