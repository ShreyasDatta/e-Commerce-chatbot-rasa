import itertools
import sqlite3
from sqlite3 import Error
import random 
import string
import time
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

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

def get_closest_value(conn, slot_name, slot_value):
        """ Given a database column & text input, find the closest 
        match for the input in the column.
        """
        # get a list of all distinct values from our target column
        fuzzy_match_cur = conn.cursor()
        fuzzy_match_cur.execute(f"""SELECT DISTINCT {slot_name} 
                                FROM eduresources""")
        column_values = fuzzy_match_cur.fetchall()

        top_match = process.extractOne(slot_value, column_values)

        return(top_match[0])

def order_update_insert_query(conn, user_id):
        """ Update the Order table with 
        randomly/uniquely generated user_id and order_id"""

        cur = conn.cursor()
        current_date = time.strftime("%Y-%m-%d")
        chars =  string.ascii_lowercase + string.digits
        order_new_id = ''.join(random.choice(chars) for _ in range(10))
        cur.execute(f"INSERT INTO `Order`(OrderNumber, CustomerId, OrderDate) VALUES('{order_new_id}','{user_id}','{current_date}')")

        cur.execute(f"""SELECT * FROM `Order`
         WHERE OrderNumber = '{order_new_id}'""")
        # return an array
        rows = cur.fetchall()
        conn.commit()
        rows = list(rows)
        for row in range(len(rows)):
            print(f"Your order number is {(rows[row][1])} and your order date is {(rows[row][3])}")

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
            print(f"For {(row[6])} under our {(row[4].lower())}, we have {(row[1])} for Rs.{(row[3])}")

    conn.commit()
    conn.close()


if __name__ == '__main__':
    select_by_slots(create_connection(r"sqlTemp.db"), slot_value="Body Care")