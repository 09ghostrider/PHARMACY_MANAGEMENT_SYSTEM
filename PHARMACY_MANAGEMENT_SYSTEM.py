from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image

class Pharmacy:
    def __init__(self, root):
        self.root = root
        self.root.title("PHARMACY")
        self.root.geometry("1440x880+0+0")
        self.root.configure(bg = "black")

        dummy = Label(root, text = "\n\n\n\n\n\n\n\n\n\n", bg = "black")
        dummy.grid(row = 0, column = 0)

        title = Label(self.root, text = "PHARMACY", font = ("times new roman", 70, "bold"), bg = "yellow", fg = "red", bd = 10, relief = GROOVE)
        title.place(x = 0, y = 0, relwidth = 1)

        timings_day = Label(self.root, text = "MONDAY - FRIDAY\n9 AM - 10 PM", font = ("times new roman", 20, "bold"), bg = "red", fg = "yellow", bd = 10, relief = GROOVE)
        timings_day.place(x = 0, y = 104, relwidth = 1)

        Item_1_Lable = Label(root, text = "  ITEM 1  ", bg = "black", fg = "white", font = ("times new roman", 30))
        Item_1_Lable.grid(row = 1, column = 0)

        Item_2_Lable = Label(root, text = "  ITEM 2  ", bg = "black", fg = "white", font = ("times new roman", 30))
        Item_2_Lable.grid(row = 2, column = 0)

        Item_3_Lable = Label(root, text = "  ITEM 3  ", bg = "black", fg = "white", font = ("times new roman", 30))
        Item_3_Lable.grid(row = 3, column = 0)

        Item_4_Lable = Label(root, text = "  ITEM 4  ", bg = "black", fg = "white", font = ("times new roman", 30))
        Item_4_Lable.grid(row = 4, column = 0)

        Item_5_Lable = Label(root, text = "  ITEM 5  ", bg = "black", fg = "white", font = ("times new roman", 30))
        Item_5_Lable.grid(row = 5, column = 0)

        Item_6_Lable = Label(root, text = "  ITEM 6  ", bg = "black", fg = "white", font = ("times new roman", 30))
        Item_6_Lable.grid(row = 6, column = 0)

        Item_7_Lable = Label(root, text = "  ITEM 7  ", bg = "black", fg = "white", font = ("times new roman", 30))
        Item_7_Lable.grid(row = 7, column = 0)

        Item_8_Lable = Label(root, text = "  ITEM 8  ", bg = "black", fg = "white", font = ("times new roman", 30))
        Item_8_Lable.grid(row = 8, column = 0)

        Item_9_Lable = Label(root, text = "  ITEM 9  ", bg = "black", fg = "white", font = ("times new roman", 30))
        Item_9_Lable.grid(row = 9, column = 0)

        Item_10_Lable = Label(root, text = "  ITEM 10  ", bg = "black", fg = "white", font = ("times new roman", 30))
        Item_10_Lable.grid(row = 10, column = 0)

root = Tk()
Pharmacy(root)
root.mainloop()