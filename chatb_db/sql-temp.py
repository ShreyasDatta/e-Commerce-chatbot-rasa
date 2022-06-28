
import sqlite3

con = sqlite3.connect("sqlTemp.db")
cur = con.cursor()

#query
query = """SELECT ProductName, ProductCategory, UnitPrice
FROM Product
WHERE ProductRoles = 'Oral Care'"""

query2 = "SELECT * FROM Product"

cur.execute(query2)
print(cur.fetchall())

con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()

