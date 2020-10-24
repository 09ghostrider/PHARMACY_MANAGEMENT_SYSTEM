from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
from test import *

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

        def Order():
            Card = Card_entry.get()
            CVV = CVV_entry.get()
            Phone = Phone_entry.get()

            if len(Card) != 0 and len(CVV) != 0 and len(Phone) != 0:
                if len(Card) == 16:
                    if len(CVV) == 3:
                        if len(Phone) == 10:
                            messagebox.showinfo("THANK YOU", "YOUR ORDER WAS PLACED\n\n\t      THANK YOU\n\t      VISIT AGAIN")
                            Exit()
                        else:
                            messagebox.showinfo("ERROR", "INVALID PHONE NUMBER")
                    else:
                        messagebox.showinfo("ERROR", "INVALID CVV")
                else:
                    messagebox.showinfo("ERROR", "INVALID CARD NUMBER")
            else:
                messagebox.showinfo("ERROR", "PLEASE ENTER THE CORRECT DETAILS")

        Login_canvas = Canvas(self.root, width = 570, height = 400, bg = "#14a3df")
        Login_canvas.place(x = 420, y = 300)

        title = Label(self.root, text = "PHARMACY", font = ("times new roman", 100, "bold"), bg = "yellow", fg = "red", bd = 10, relief = GROOVE)
        title.place(x = 0, y = 0, relwidth = 1)

        place_order_title = Label(Login_canvas, text = "PLACE ORDER", font = ("times new roman", 50, "bold"), bg = "yellow", fg = "red", bd = 10, relief = GROOVE)
        place_order_title.place(x = 0, y = 0, relwidth = 1)

        order_button = Button(Login_canvas, text = "   ORDER   ", font = ("times new roman", 30, "bold"), relief = GROOVE, command = lambda:Order())
        order_button.place(x = 370, y = 350)

        exit_button = Button(Login_canvas, text = "    EXIT    ", font = ("times new roman", 30, "bold"), relief = GROOVE, command = lambda:Exit())
        exit_button.place(x = 50, y = 350)

        Card_Lable = Label(Login_canvas, text = " CARD NUMBER:  ", font = ("times new roman", 30, "bold"))
        Card_Lable.place(x = 15, y = 140)

        CVV_Lable = Label(Login_canvas, text = "   CVV NUMBER:   ", font = ("times new roman", 30, "bold"))
        CVV_Lable.place(x = 15, y = 200)

        Phone_Lable = Label(Login_canvas, text = "PHONE NUMBER:", font = ("times new roman", 30, "bold"))
        Phone_Lable.place(x = 15, y = 260)

        Card_entry = Entry(Login_canvas, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE )
        Card_entry.place(x = 290, y = 140)

        CVV_entry = Entry(Login_canvas, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE)
        CVV_entry.place(x = 290, y = 200)

        Phone_entry = Entry(Login_canvas, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE)
        Phone_entry.place(x = 290, y = 260)

# OP = Tk()
# Order_Page(OP)
# OP.mainloop()