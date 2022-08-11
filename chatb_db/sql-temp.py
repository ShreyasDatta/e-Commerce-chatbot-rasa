
import sqlite3
import random
import string
import time

con = sqlite3.connect("sqlTemp.db")
cur = con.cursor()

#query
query = """CREATE TABLE `Order`(
        OrderId INTEGER PRIMARY KEY NOT NULL,
        OrderNumber VARCHAR(10) NOT NULL, 
        CustomerId INT,
        OrderDate DATE
        );"""

query2 = """DELETE FROM `Order`;"""

query3 = "INSERT INTO `Order`(OrderNumber, CustomerId, OrderDate) VALUES('124245', '002', '2022-01-01')"

x = time.strftime("%Y-%m-%d")
# print(x)
chars =  string.ascii_lowercase + string.digits
a = ''.join(random.choice(chars) for _ in range(10))
order_new_id = a
# print(order_new_id)

cur.execute(query3)
print(cur.fetchall())

con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()

