from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
from ORDER_PAGE import *

class Pharmacy:
    def __init__(self, root, Order_Name):
        self.root = root
        self.root.title("PHARMACY")
        self.root.geometry("1440x880+0+0")

        self.bg_img = ImageTk.PhotoImage(file = "/Users/saniha/Dropbox/My Mac (niha का MacBook Air)/Desktop/bg_img_4.jpg")
        bg = Label(self.root, image = self.bg_img)
        bg.place(x = -200, y = 0)


        def Exit():
            self.root.destroy()

        def Total_calaculator():
            try:
                Item_1_Total_Cost = (int(Item_2_entry.get()) * 35)
                Item_2_Total_Cost = (int(Item_3_entry.get()) * 30)
                Item_3_Total_Cost = (int(Item_4_entry.get()) * 58)
                Item_4_Total_Cost = (int(Item_5_entry.get()) * 123)
                Item_5_Total_Cost = (int(Item_6_entry.get()) * 440)
                Item_6_Total_Cost = (int(Item_7_entry.get()) * 90)
                Item_7_Total_Cost = (int(Item_8_entry.get()) * 17)
                Item_8_Total_Cost = (int(Item_9_entry.get()) * 82)
                Item_9_Total_Cost = (int(Item_10_entry.get()) * 106)
                Item_10_Total_Cost = (int(Item_11_entry.get()) * 80)
                Item_11_Total_Cost = (int(Item_12_entry.get()) * 52)
                Item_12_Total_Cost = (int(Item_13_entry.get()) * 127)
                Item_13_Total_Cost = (int(Item_14_entry.get()) * 88)
                Item_14_Total_Cost = (int(Item_15_entry.get()) * 216)
                Item_15_Total_Cost = (int(Item_16_entry.get()) * 95)
                return (Item_1_Total_Cost + Item_2_Total_Cost + Item_3_Total_Cost + Item_4_Total_Cost + Item_5_Total_Cost + Item_6_Total_Cost + Item_7_Total_Cost + Item_8_Total_Cost + Item_9_Total_Cost + Item_10_Total_Cost + Item_11_Total_Cost + Item_12_Total_Cost + Item_13_Total_Cost + Item_14_Total_Cost + Item_15_Total_Cost)

            except:
                messagebox.showinfo("ERROR", "INVALID QUANTITY")

        def Total():
            Ans = Total_calaculator()
            Total_entry.delete(0, END)
            Total_entry.insert(0, Ans)

        def Place_Final_Order(name):
            Price = Total_calaculator()

            if Price > 0:
                con = sqlite3.connect("Orders.db")
                c = con.cursor()
                
                item_1 = int(Item_2_entry.get())
                item_2 = int(Item_3_entry.get())
                item_3 = int(Item_4_entry.get())
                item_4 = int(Item_5_entry.get())
                item_5 = int(Item_6_entry.get())
                item_6 = int(Item_7_entry.get())
                item_7 = int(Item_8_entry.get())
                item_8 = int(Item_9_entry.get())
                item_9 = int(Item_10_entry.get())
                item_10 = int(Item_11_entry.get())
                item_11 = int(Item_12_entry.get())
                item_12 = int(Item_13_entry.get())
                item_13 = int(Item_14_entry.get())
                item_14 = int(Item_15_entry.get())
                item_15 = int(Item_16_entry.get())

                item_delevered = "FALSE"

                c.execute("INSERT INTO Quantity VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11, item_12, item_13, item_14, item_15, item_delevered))

                con.commit()
                con.close()
                
                Exit()
                O_page()
            
            else:
                messagebox.showinfo("ERROR", "PLEASE ORDER ITEMS TO PLACE ORDER")
            

        dummy = Label(root, text = "\n\n\n\n\n\n\n\n\n\n", bg = "#50b9e9")
        dummy.grid(row = 0, column = 0)

        title = Label(self.root, text = "PHARMACY", font = ("times new roman", 70, "bold"), bg = "yellow", fg = "red", bd = 10, relief = GROOVE)
        title.place(x = 0, y = 0, relwidth = 1)

        timings_day = Label(self.root, text = "MONDAY - SATURDAY\n9 AM - 11 PM", font = ("times new roman", 20, "bold"), bg = "red", fg = "yellow", bd = 10, relief = GROOVE)
        timings_day.place(x = 0, y = 104, relwidth = 1)

        Item_Lable = Label(root, text = "   ITEMS   ", bg = "#65c0ed", fg = "yellow", font = ("times new roman", 30, "bold underline"))
        Item_Lable.grid(row = 1, column = 0)

        Item_2_Lable = Label(root, text = "  PARACETAMOL  ", bg = "#65c0ed", fg = "white", font = ("times new roman", 30))
        Item_2_Lable.grid(row = 2, column = 0)

        Item_3_Lable = Label(root, text = "  CALPOL  ", bg = "#65c0ed", fg = "white", font = ("times new roman", 30))
        Item_3_Lable.grid(row = 3, column = 0)

        Item_4_Lable = Label(root, text = "  CLOTRIMAZOLE  ", bg = "#65c0ed", fg = "white", font = ("times new roman", 30))
        Item_4_Lable.grid(row = 4, column = 0)

        Item_5_Lable = Label(root, text = "  CHOLECALCIFEROL  ", bg = "#65c0ed", fg = "white", font = ("times new roman", 30))
        Item_5_Lable.grid(row = 5, column = 0)

        Item_6_Lable = Label(root, text = "  RHUMAYOG GOLD  ", bg = "#65c0ed", fg = "white", font = ("times new roman", 30))
        Item_6_Lable.grid(row = 6, column = 0)

        Item_7_Lable = Label(root, text = "  DOLOLES  ", bg = "#65c0ed", fg = "white", font = ("times new roman", 30))
        Item_7_Lable.grid(row = 7, column = 0)

        Item_8_Lable = Label(root, text = "  CIPLOX - D  ", bg = "#65c0ed", fg = "white", font = ("times new roman", 30))
        Item_8_Lable.grid(row = 8, column = 0)

        Item_9_Lable = Label(root, text = "  DOLOGEL  ", bg = "#65c0ed", fg = "white", font = ("times new roman", 30))
        Item_9_Lable.grid(row = 9, column = 0)

        Item_10_Lable = Label(root, text = "  SENSUR RUB  ", bg = "#65c0ed", fg = "white", font = ("times new roman", 30))
        Item_10_Lable.grid(row = 10, column = 0)

        Item_11_Lable = Label(root, text = "  TUSQ.D  ", bg = "#65c0ed", fg = "white", font = ("times new roman", 30))
        Item_11_Lable.grid(row = 11, column = 0)

        Item_12_Lable = Label(root, text = "  COFTEX LS  ", bg = "#65c0ed", fg = "white", font = ("times new roman", 30))
        Item_12_Lable.grid(row = 12, column = 0)

        Item_13_Lable = Label(root, text = "  DUPHALAC  ", bg = "#65c0ed", fg = "white", font = ("times new roman", 30))
        Item_13_Lable.grid(row = 13, column = 0)

        Item_14_Lable = Label(root, text = "  BETADERM - Z  ", bg = "#65c0ed", fg = "white", font = ("times new roman", 30))
        Item_14_Lable.grid(row = 14, column = 0)

        Item_15_Lable = Label(root, text = "  SAVLON ANTISEPTIC  ", bg = "#65c0ed", fg = "white", font = ("times new roman", 30))
        Item_15_Lable.grid(row = 15, column = 0)

        Item_16_Lable = Label(root, text = "  ADGEL - O  ", bg = "#65c0ed", fg = "white", font = ("times new roman", 30))
        Item_16_Lable.grid(row = 16, column = 0)

        Item_entry = Label(root, text = "    QUANTITY    ", font = ("times new roman", 30, "bold underline"), bg = "#7ec7ef", fg = "yellow")
        Item_entry.grid(row = 1, column = 1)

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

        Item_Cost = Label(root, text = "     COST     ", bg = "#bee0fa", fg = "yellow", font = ("times new roman", 30, "bold underline"))
        Item_Cost.grid(row = 1, column = 2)

        Item_2_Cost = Label(root, text = "  ₹ 35 / SYRUP  ", bg = "#bee0fa", fg = "white", font = ("times new roman", 30))
        Item_2_Cost.grid(row = 2, column = 2)

        Item_3_Cost = Label(root, text = "  ₹ 30 / 10 TABLETS  ", bg = "#bee0fa", fg = "white", font = ("times new roman", 30))
        Item_3_Cost.grid(row = 3, column = 2)

        Item_4_Cost = Label(root, text = "  ₹ 58 / 75g POWDER  ", bg = "#bee0fa", fg = "white", font = ("times new roman", 30))
        Item_4_Cost.grid(row = 4, column = 2)

        Item_5_Cost = Label(root, text = "  ₹ 123 / 4 CAPSULES  ", bg = "#bee0fa", fg = "white", font = ("times new roman", 30))
        Item_5_Cost.grid(row = 5, column = 2)

        Item_6_Cost = Label(root, text = "  ₹ 440 / 30 TABLETS  ", bg = "#bee0fa", fg = "white", font = ("times new roman", 30))
        Item_6_Cost.grid(row = 6, column = 2)

        Item_7_Cost = Label(root, text = "  ₹ 90 / 10 TABLETS  ", bg = "#bee0fa", fg = "white", font = ("times new roman", 30))
        Item_7_Cost.grid(row = 7, column = 2)

        Item_8_Cost = Label(root, text = "  ₹ 17 / BOTTLE  ", bg = "#bee0fa", fg = "white", font = ("times new roman", 30))
        Item_8_Cost.grid(row = 8, column = 2)

        Item_9_Cost = Label(root, text = "  ₹ 82 / 15g GEL  ", bg = "#bee0fa", fg = "white", font = ("times new roman", 30))
        Item_9_Cost.grid(row = 9, column = 2)

        Item_10_Cost = Label(root, text = "  ₹ 106 / 30g GEL  ", bg = "#bee0fa", fg = "white", font = ("times new roman", 30))
        Item_10_Cost.grid(row = 10, column = 2)

        Item_11_Cost = Label(root, text = "  ₹ 80 / SYRUP  ", bg = "#bee0fa", fg = "white", font = ("times new roman", 30))
        Item_11_Cost.grid(row = 11, column = 2)

        Item_12_Cost = Label(root, text = "  ₹ 52 / SYRUP  ", bg = "#bee0fa", fg = "white", font = ("times new roman", 30))
        Item_12_Cost.grid(row = 12, column = 2)

        Item_13_Cost = Label(root, text = "  ₹ 127 / SYRUP  ", bg = "#bee0fa", fg = "white", font = ("times new roman", 30))
        Item_13_Cost.grid(row = 13, column = 2)

        Item_14_Cost = Label(root, text = "  ₹ 88 / 30g GEL  ", bg = "#bee0fa", fg = "white", font = ("times new roman", 30))
        Item_14_Cost.grid(row = 14, column = 2)

        Item_15_Cost = Label(root, text = "  ₹ 216 / BOTTLE ", bg = "#bee0fa", fg = "white", font = ("times new roman", 30))
        Item_15_Cost.grid(row = 15, column = 2)

        Item_16_Cost = Label(root, text = "  ₹ 95 / 30g GEL  ", bg = "#bee0fa", fg = "white", font = ("times new roman", 30))
        Item_16_Cost.grid(row = 16, column = 2)

        Order_Button = Button(root, text = "  PLACE ORDER  ", font = ("times new roman", 30, "bold"), relief = GROOVE, command = lambda:Place_Final_Order(Order_Name))
        Order_Button.place(x = 950, y = 820)

        Exit_Button = Button(root, text = "  EXIT  ", font = ("times new roman", 30, "bold"), relief = GROOVE, command = lambda:Exit())
        Exit_Button.place(x = 1250, y = 820)

        Total_Button = Button(root, text = "  TOTAL  ", font = ("times new roman", 30, "bold"), relief = GROOVE, command = lambda:Total())
        Total_Button.place(x = 1115, y = 200)

        Total_entry = Entry(root, font = ("times new roman", 25, "bold"), fg = "black", bg = "white", relief = GROOVE)
        Total_entry.place(x = 1050, y = 250)

def O_page():
    OP = Tk()
    Order_Page(OP)
    OP.mainloop()

# root = Tk()
# Pharmacy(root, "Niksh")
# root.mainloop()