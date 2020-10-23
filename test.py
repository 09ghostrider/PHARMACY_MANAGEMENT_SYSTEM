import sqlite3
import re
import os

# con = sqlite3.connect("Orders.db")
# c = con.cursor()

def Print_Accounts_Table():
    con = sqlite3.connect("Orders.db")
    c = con.cursor()
    
    c.execute("SELECT rowid, * FROM Accounts ")
    all_items = c.fetchall()
    
    for item in all_items:
        print(item)
    
    con.commit()
    con.close()

def Print_Quantity_Table():
    con = sqlite3.connect("Orders.db")
    c = con.cursor()
    
    c.execute("SELECT rowid, * FROM Quantity ")
    all_items = c.fetchall()
    
    for item in all_items:
        print(item)
    
    con.commit()
    con.close()

def Clear():
    os.system("clear")

# Clear()
# Print_Accounts_Table()
Print_Quantity_Table()

'''
c.execute(""" CREATE TABLE Quantity (
    name text,
    item_1 int,
    item_2 int,
    item_3 int,
    item_4 int,
    item_5 int,
    item_6 int,
    item_7 int,
    item_8 int,
    item_9 int,
    item_10 int,
    item_11 int,
    item_12 int,
    item_13 int,
    item_14 int,
    item_15 int,
    item_delevered text
) """)
'''

# c.execute("INSERT INTO Accounts VALUES ('Niksh', 'niksh.hiremath@gmail.com', 4567)")

# c.execute("INSERT INTO Accounts VALUES (?, ?, ?)", (Nam, User, Pass))

# c.execute("UPDATE Accounts SET order_delevered = 'FALSE' WHERE rowid = 1")

# c.execute("DELETE from Accounts WHERE rowid = 1")

# c.execute("DROP TABLE Quantity")

# Print_Accounts_Table()
# Print_Quantity_Table()

# con.commit()
# con.close()

# Print_Accounts_Table()
# Print_Quantity_Table()

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def check_mail(email):
    if(re.search(regex,email)):
        return "VALID"
    return "INVALID"
    

# email = "niksh.hiremath@gmail.com"
# print(check_mail(email))