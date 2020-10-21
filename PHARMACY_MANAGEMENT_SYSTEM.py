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

        # self.bg_img = ImageTk.PhotoImage(file = "/Users/saniha/Dropbox/My Mac (niha का MacBook Air)/Desktop/bg_img_4.jpg")
        # bg = Label(self.root, image = self.bg_img)
        # bg.place(x = 0, y = 0)


        def Exit():
            self.root.destroy()

        dummy = Label(root, text = "\n\n\n\n\n\n\n\n\n\n", bg = "black")
        dummy.grid(row = 0, column = 0)

        title = Label(self.root, text = "PHARMACY", font = ("times new roman", 70, "bold"), bg = "yellow", fg = "red", bd = 10, relief = GROOVE)
        title.place(x = 0, y = 0, relwidth = 1)

        timings_day = Label(self.root, text = "MONDAY - FRIDAY\n9 AM - 11 PM", font = ("times new roman", 20, "bold"), bg = "red", fg = "yellow", bd = 10, relief = GROOVE)
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

        Item_11_Lable = Label(root, text = "  ITEM 11  ", bg = "black", fg = "white", font = ("times new roman", 30))
        Item_11_Lable.grid(row = 11, column = 0)

        Item_12_Lable = Label(root, text = "  ITEM 12  ", bg = "black", fg = "white", font = ("times new roman", 30))
        Item_12_Lable.grid(row = 12, column = 0)

        Item_13_Lable = Label(root, text = "  ITEM 13  ", bg = "black", fg = "white", font = ("times new roman", 30))
        Item_13_Lable.grid(row = 13, column = 0)

        Item_14_Lable = Label(root, text = "  ITEM 14  ", bg = "black", fg = "white", font = ("times new roman", 30))
        Item_14_Lable.grid(row = 14, column = 0)

        Item_15_Lable = Label(root, text = "  ITEM 15  ", bg = "black", fg = "white", font = ("times new roman", 30))
        Item_15_Lable.grid(row = 15, column = 0)

        Item_16_Lable = Label(root, text = "  ITEM 16  ", bg = "black", fg = "white", font = ("times new roman", 30))
        Item_16_Lable.grid(row = 16, column = 0)

        Item_1_entry = Entry(root, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE)
        Item_1_entry.grid(row = 1, column = 1)

        Item_2_entry = Entry(root, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE)
        Item_2_entry.grid(row = 2, column = 1)

        Item_3_entry = Entry(root, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE)
        Item_3_entry.grid(row = 3, column = 1)

        Item_4_entry = Entry(root, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE)
        Item_4_entry.grid(row = 4, column = 1)

        Item_5_entry = Entry(root, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE)
        Item_5_entry.grid(row = 5, column = 1)

        Item_6_entry = Entry(root, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE)
        Item_6_entry.grid(row = 6, column = 1)

        Item_7_entry = Entry(root, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE)
        Item_7_entry.grid(row = 7, column = 1)

        Item_8_entry = Entry(root, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE)
        Item_8_entry.grid(row = 8, column = 1)

        Item_9_entry = Entry(root, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE)
        Item_9_entry.grid(row = 9, column = 1)

        Item_10_entry = Entry(root, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE)
        Item_10_entry.grid(row = 10, column = 1)

        Item_11_entry = Entry(root, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE)
        Item_11_entry.grid(row = 11, column = 1)

        Item_12_entry = Entry(root, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE)
        Item_12_entry.grid(row = 12, column = 1)

        Item_13_entry = Entry(root, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE)
        Item_13_entry.grid(row = 13, column = 1)

        Item_14_entry = Entry(root, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE)
        Item_14_entry.grid(row = 14, column = 1)

        Item_15_entry = Entry(root, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE)
        Item_15_entry.grid(row = 15, column = 1)

        Item_16_entry = Entry(root, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE)
        Item_16_entry.grid(row = 16, column = 1)

        dummy_2 = Label(text = "\t", bg = "black")
        dummy_2.grid(row = 16, column = 2)

        Total_Button = Button(root, text = "  TOTAL  ", font = ("times new roman", 25, "bold"), relief = GROOVE)
        Total_Button.grid(row = 16, column = 3)

        dummy_3 = Label(text = "      ", bg = "black")
        dummy_3.grid(row = 16, column = 4)

        Exit_Button = Button(root, text = "  EXIT  ", font = ("times new roman", 25, "bold"), relief = GROOVE, command = lambda:Exit())
        Exit_Button.grid(row = 16, column = 5)


# root = Tk()
# Pharmacy(root)
# root.mainloop()