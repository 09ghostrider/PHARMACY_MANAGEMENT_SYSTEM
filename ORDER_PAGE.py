from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
from test import *
from PHARMACY_MANAGEMENT_SYSTEM import *

class Order_Page:
    def __init__(self, root):
        self.root = root
        self.root.title("PHARMACY")
        self.root.geometry("1440x880+0+0")

        self.bg_img = ImageTk.PhotoImage(file = "/Users/saniha/Dropbox/My Mac (niha का MacBook Air)/Desktop/bg_img_4.jpg")
        bg = Label(self.root, image = self.bg_img)
        bg.place(x = -200, y = -10)

        def Exit():
            self.root.destroy()

        Login_canvas = Canvas(self.root, width = 500, height = 400, bg = "#14a3df")
        Login_canvas.place(x = 470, y = 300)

        title = Label(self.root, text = "PHARMACY", font = ("times new roman", 100, "bold"), bg = "yellow", fg = "red", bd = 10, relief = GROOVE)
        title.place(x = 0, y = 0, relwidth = 1)

        signup_title = Label(Login_canvas, text = "PLACE ORDER", font = ("times new roman", 50, "bold"), bg = "yellow", fg = "red", bd = 10, relief = GROOVE)
        signup_title.place(x = 0, y = 0, relwidth = 1)

        login_button = Button(Login_canvas, text = "   ORDER   ", font = ("times new roman", 30, "bold"), relief = GROOVE)
        login_button.place(x = 290, y = 350)

        exit_button = Button(Login_canvas, text = "    EXIT    ", font = ("times new roman", 30, "bold"), relief = GROOVE, command = lambda:Exit())
        exit_button.place(x = 50, y = 350)

OP = Tk()
Order_Page(OP)
OP.mainloop()