from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
import sqlite3
from test import *

class Creat_Acc:
    def __init__(self, root):
        self.root = root
        self.root.title("PHARMACY")
        self.root.geometry("1440x880+0+0")
        self.root.configure(bg = "black")

        def Exit(): 
            self.root.destroy()

        def Signup():
            con = sqlite3.connect("Orders.db")
            c = con.cursor()
            Nam = name_entry.get()
            User = username_entry.get()
            Pass = password_entry.get()
            print(f"NAME: {Nam}\nEMAIL: {User}\nPASSWORD: {Pass}")

            if Nam != "" and User != "" and Pass != "":
                if check_mail(User) == "VALID":
                    messagebox.showinfo("WELCOME", "ACCOUNT CREATED")
                    acc = [
                        (Nam, User, Pass)
                    ]
                    c.executemany("INSERT INTO Accounts VALUES (?, ?, ?)", acc)
                    Print_Accounts_Table()
                    con.commit()
                    con.close()
                    Exit()
                    # Clear()

                else:
                    messagebox.showinfo("ERROR", "INVALID GMAIL")
            else:
                messagebox.showinfo("ERROR", "ALL FIELDS ARE REQUIRED")

        self.bg_img = ImageTk.PhotoImage(file = "bg_img_4.jpg")
        bg = Label(self.root, image = self.bg_img)
        bg.place(x = -200, y = 0)

        title = Label(self.root, text = "PHARMACY", font = ("times new roman", 100, "bold"), bg = "yellow", fg = "red", bd = 10, relief = GROOVE)
        title.place(x = 0, y = 0, relwidth = 1)

        Login_canvas = Canvas(self.root, width = 500, height = 400, bg = "#14a3df")
        Login_canvas.place(x = 470, y = 300)

        signup_title = Label(Login_canvas, text = "SIGN UP", font = ("times new roman", 50, "bold"), bg = "yellow", fg = "red", bd = 10, relief = GROOVE)
        signup_title.place(x = 0, y = 0, relwidth = 1)

        name_title = Label(Login_canvas, text = "     NAME:     ", font = ("times new roman", 30, "bold"), fg = "black", bg = "white")
        name_title.place(x = 5, y = 140)

        username_title = Label(Login_canvas, text = "     GMAIL:    ", font = ("times new roman", 30, "bold"), fg = "black", bg = "white")
        username_title.place(x = 5, y = 200)

        password_title = Label(Login_canvas, text = "PASSWORD:", font = ("times new roman", 30, "bold"), fg = "black", bg = "white")
        password_title.place(x = 5, y = 260)

        name_entry = Entry(Login_canvas, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE )
        name_entry.place(x = 220, y = 140)

        username_entry = Entry(Login_canvas, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE)
        username_entry.place(x = 220, y = 200)

        password_entry = Entry(Login_canvas, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE, show = "*")
        password_entry.place(x = 220, y = 260)

        login_button = Button(Login_canvas, text = "   SIGN UP   ", font = ("times new roman", 30, "bold"), relief = GROOVE, command = lambda:Signup())
        login_button.place(x = 290, y = 350)

        exit_button = Button(Login_canvas, text = "    EXIT    ", font = ("times new roman", 30, "bold"), relief = GROOVE, command = lambda:Exit())
        exit_button.place(x = 40, y = 350)

# cre = Tk()
# Creat_Acc(cre)
# cre.mainloop()
