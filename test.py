import sqlite3
import re

con = sqlite3.connect("Orders.db")
c = con.cursor()

'''
c.execute(""" CREATE TABLE Accounts (
    name text,
    email text,
    password int
) """)
'''

# c.execute("INSERT INTO Accounts VALUES ('Shivanand', 'shivanand.hiremath@gmail.com', 4567)")

# c.execute("UPDATE Accounts SET order_delevered = 'FALSE' WHERE rowid = 1")

# c.execute("DELETE from Accounts WHERE rowid = 2")

# c.execute("DROP TABLE Accounts")

'''
c.execute("SELECT rowid, * FROM Accounts ")
all_items = c.fetchall()
for item in all_items:
    print(item)
'''

con.commit()
con.close()

# item_1 int,
# item_2 int,
# item_3 int,
# item_4 int,
# item_5 int,
# item_6 int,
# item_7 int,
# item_8 int,
# item_9 int,
# item_10 int,
# item_11 int,
# item_12 int,
# item_13 int,
# item_14 int,
# item_15 int

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def check_mail(email):
    if(re.search(regex,email)):
        return "VALID"
    return "INVALID"
    

# email = "niksh.hiremath@gmail.com"
# print(check_mail(email))