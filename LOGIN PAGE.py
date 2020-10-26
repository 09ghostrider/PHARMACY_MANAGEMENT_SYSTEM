from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
from PHARMACY_MANAGEMENT_SYSTEM import *
import sqlite3
from CREAT_ACCOUNT import *
from test import *

con = sqlite3.connect("Orders.db")
c = con.cursor()

name = []
username = []
password = []

c.execute("SELECT rowid, * FROM Accounts ")
all_items = c.fetchall()
for item in all_items:
    print(item)

for Id in all_items:
    name.append(Id[1])
    username.append(Id[2])
    password.append(Id[3])

print(name)
print(username)
print(password)

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("PHARMACY")
        self.root.geometry("1440x880+0+0")

        def Exit(): 
            self.root.destroy()

        def Cre():
            self.root.destroy()
            CR()

        def Login():
            User = username_entry.get()
            Pass = password_entry.get()

            if User == "" or Pass == "":
                messagebox.showinfo("ERROR", "ALL FIELDS ARE REQUIRED")
            
            elif User != "" and Pass != "":
                
                if User in username:
                    I = username.index(User)
                    
                    if password[I] == int(Pass):
                        messagebox.showinfo("WELCOME", "LOGIN SUCCESFULL")
                        self.root.destroy()
                        Restaurant(name[I])
                    
                    else:
                        messagebox.showinfo("ERROR", "INVALID USERNAME OR PASSWORD")

                else:
                    messagebox.showinfo("ERROR", "INVALID USERNAME OR PASSWORD")

            else:
                messagebox.showinfo("ERROR", "INVALID GMAIL OR PASSWORD")

        self.bg_img = ImageTk.PhotoImage(file = "/Users/saniha/Dropbox/My Mac (niha का MacBook Air)/Desktop/bg_img_4.jpg")

        bg = Label(self.root, image = self.bg_img)
        bg.pack()

        title = Label(self.root, text = "PHARMACY", font = ("times new roman", 100, "bold"), bg = "yellow", fg = "red", bd = 10, relief = GROOVE)
        title.place(x = 0, y = 0, relwidth = 1)

        Login_canvas = Canvas(self.root, width = 500, height = 350, bg = "#14a3df")
        Login_canvas.place(x = 470, y = 300)

        login_title = Label(Login_canvas, text = "LOGIN", font = ("times new roman", 50, "bold"), bg = "yellow", fg = "red", bd = 10, relief = GROOVE)
        login_title.place(x = 0, y = 0, relwidth = 1)

        username_title = Label(Login_canvas, text = "     GMAIL:    ", font = ("times new roman", 30, "bold"), fg = "black", bg = "white")
        username_title.place(x = 5, y = 150)

        password_title = Label(Login_canvas, text = "PASSWORD:", font = ("times new roman", 30, "bold"), fg = "black", bg = "white")
        password_title.place(x = 5, y = 210)

        username_entry = Entry(Login_canvas, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE)
        username_entry.place(x = 220, y = 150)

        password_entry = Entry(Login_canvas, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE, show = "*")
        password_entry.place(x = 220, y = 210)

        login_button = Button(Login_canvas, text = "  LOGIN  ", font = ("times new roman", 30, "bold"), relief = GROOVE, command = lambda:Login())
        login_button.place(x = 340, y = 300) # 130

        exit_button = Button(Login_canvas, text = "  EXIT  ", font = ("times new roman", 30, "bold"), relief = GROOVE, command = lambda:Exit())
        exit_button.place(x = 200, y = 300) # 110

        Creat_button = Button(Login_canvas, text = " SIGN UP ", font = ("times new roman", 30, "bold"), relief = GROOVE, command = lambda:Cre())
        Creat_button.place(x = 30, y = 300) # 140

log = Tk()
Login(log)

def Restaurant(Name):
    root = Tk()
    Pharmacy(root, Name)
    # pass

def CR():
    C = Tk()
    Creat_Acc(C)

con.commit()
con.close()

log.mainloop()