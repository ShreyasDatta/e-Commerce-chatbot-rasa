import itertools
import sqlite3
from sqlite3 import Error
import random 
# def peek(iterator):
#     """
#     Peek at the next item in the iterator.
#     """
#     try:
#         next(iterator)
#     except StopIteration:
#         return None
#     else:
#         return True


def create_connection(sqlTemp):
    """ create a database connection to the SQLite database
        
    """
    conn = None
    try:
        conn = sqlite3.connect(sqlTemp)
        print(create_connection)
    except Error as e:
        print(e)
    return conn

def select_by_slots(conn, slot_value):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM product
        WHERE ProductRoles = '{slot_value}'""")


    rows = cur.fetchall()
#if cursor is carrying Empty Val from query
    if len(list(rows)) < 1:
        print("There are no products matching your query in the database")
    
    else:
        for row in random.sample(rows, 1):
            print(row)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    select_by_slots(create_connection(r"sqlTemp.db"), slot_value = "Body Care")