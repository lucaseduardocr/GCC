from tkinter import *
from tkinter import ttk
import tkinter as tk


class Register_GUI:
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

        self.fifth_container = Frame(master)
        self.fifth_container.pack()

        self.sixth_container = Frame(master)
        self.sixth_container.pack()
        #Containers

        #Text and other widgets
        self.login_title = Label(self.first_container, text="REGISTER", height=2, font=("Verdana", "30", "bold"))
        self.login_title.pack()

        #name
        self.name_text = Label(self.second_container, text="NAME", width=12, font=("Verdana", "10", "bold"))
        self.name_text.pack(side=LEFT)

        self.name_box_entry = Entry(self.second_container, width= 40)
        self.name_box_entry.pack(side=RIGHT)

        #email
        self.email_text = Label(self.third_container, text="EMAIL", width=12, font=("Verdana", "10", "bold"))
        self.email_text.pack(side=LEFT)

        self.email_box_entry = Entry(self.third_container, width= 40)
        self.email_box_entry.pack(side=RIGHT)

        #password
        self.password_text = Label(self.fourth_container, text="PASSWORD", width=12, font=("Verdana", "10", "bold"))
        self.password_text.pack(side=LEFT)

        self.password_entry = Entry(self.fourth_container, width=40)
        self.password_entry.pack(side=RIGHT)

        #confirm password
        self.confirm_password_text = Label(self.fifth_container, text="CONFIRM PASSWORD", width=20, font=("Verdana", "10", "bold"))
        self.confirm_password_text.pack(side=LEFT)

        self.confirm_password_entry = Entry(self.fifth_container, width=28)
        self.confirm_password_entry.pack(side=RIGHT)

        #button
        self.button_register = Button(self.sixth_container, width=20,height=2, text="REGISTER", font=("Verdana", "7", "bold"))
        self.button_register.pack(pady=30)