import sqlite3
import re
import os

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

def Update_Order_Delvery(Order_Number):
    con = sqlite3.connect("Orders.db")
    c = con.cursor()

    c.execute("UPDATE Quantity SET item_delevered = 'TRUE' WHERE rowid = {}".format(Order_Number))

    con.commit()
    con.close()

    print("CHANGED SUCCESSFULLY !!")

Clear()



# con = sqlite3.connect("Orders.db")
# c = con.cursor()

# c.execute(""" CREATE TABLE table_name (
#     name type,
#     name type
# ) """)

# c.execute("INSERT INTO Accounts VALUES ('User', 'user@gmail.com', 4567)")

# c.execute("INSERT INTO Accounts VALUES (?, ?, ?)", (Nam, User, Pass))

# c.execute("UPDATE Quantity SET item_delevered = 'FALSE' WHERE rowid = 4")

# c.execute("DELETE from Accounts WHERE rowid = 7")

# c.execute("DROP TABLE Quantity")

# con.commit()
# con.close()




# Print_Accounts_Table()
# Update_Order_Delvery(1)
# Print_Quantity_Table()




regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def check_mail(email):
    if(re.search(regex,email)):
        return "VALID"
    return "INVALID"
    
# email = "niksh.hiremath@gmail.com"
# print(check_mail(email))
