# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# TODO: 
# - query more than one field/column at a time
# - if nothing matches both fields return results that match
#   at least one
# - data validation for close but not exact matches


# multifield query process:
# - first match each slot to closest item in that column
# actual complex queries
# - look for either, find union, 
# if none inform not perfect match


from multiprocessing import connection
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker 
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import sqlite3
from sqlite3 import Error
import random, string, time
from fuzzywuzzy import process


class QueryOrderUpdate(Action):

    def name(self) -> Text:
        return "place_confirmed_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = dbQueryMethods.create_connection("chatb_db/sqlTemp.db")
        
        #get user_id from tracker
        user_id = tracker.current_state()['sender_id']
        print(f"user-id:{user_id}")

        #initiate query to update order table
        current_order_id = dbQueryMethods.order_update_insert_query(conn, user_id)
        #display order status to user
        return_text_for_order_update = dbQueryMethods.order_status_check(conn, current_order_id)
        print(return_text_for_order_update)
        dispatcher.utter_message(text=str(return_text_for_order_update))

class QueryOrderStatus(Action):

    def name(self) -> Text:
        return "check_confirmed_order_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = dbQueryMethods.create_connection("chatb_db/sqlTemp.db")

        var1 = QueryOrderUpdate.current_order_id
        print(f"var1:{var1}")
        #display order status to user
        return_text_for_order_update = dbQueryMethods.order_status_check(conn, var1)
        print(return_text_for_order_update)
        dispatcher.utter_message(text=str(return_text_for_order_update))

class collectProductInfo(Action):

    def name(self) -> Text:
        return "collect_product_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = dbQueryMethods.create_connection("chatb_db/sqlTemp.db")
        user_id = tracker.current_state()['sender_id']
        print(f"user-id:{user_id}")

        # get matching entries for category value
        category_value = tracker.get_slot("productCategory")
        #make sure we don't pass None to our fuzzy matcher
        if category_value == None:
            category_value = " "
        print(f"category_slot_1:{category_value}")  #for debugging
        category_name = "ProductCategory"

        category_value = dbQueryMethods.get_closest_value(conn, category_name, category_value)[0]
        print(f"category_fuzzy_slot_2:{category_value}")

        query_result_category = dbQueryMethods.select_by_category(conn, category_value)

        # get matching entries for role value
        role_value = tracker.get_slot("products")
        #make sure we don't pass None to our fuzzy matcher
        if role_value == None:
            role_value = " "
        role_name = "ProductRoles"
        print(f"role_slot_1:{role_value}")  #for debugging
        
        role_value = dbQueryMethods.get_closest_value(conn, role_name, role_value)[0]
        print(f"role_fuzzy_slot_2:{role_value}")

        query_result_roles = dbQueryMethods.select_by_slots(conn, role_value)

        # apology for not being able to find a match
        apology = "I'm sorry, I couldn't find exactly what you wanted, but you might like this."

        # intersection of two queries
        query_result_overlap = list(set(query_result_category) & set(query_result_roles))
        

        # return info for both, or category match or role match or nothing
        if len(query_result_overlap)>0:
            return_text_for_general_query = dbQueryMethods.rows_as_info_text(query_result_overlap)
            print(f"query_result_overlap:{query_result_overlap}")
        elif len(list(query_result_category))>0:
            return_text_for_general_query = apology + dbQueryMethods.rows_as_info_text(query_result_category)
            print(f"query_result_category:{query_result_category}")
        elif len(list(query_result_roles))>0:
            return_text_for_general_query = apology + dbQueryMethods.rows_as_info_text(query_result_roles)
            print(f"query_result_roles:{query_result_roles}")
        else:
            return_text_for_general_query = dbQueryMethods.rows_as_info_text(query_result_overlap)
        
        # look at intersect between two arrays
        # if empty && union is not
        # randomly select one item from list
        # otherwise get query results from one of the two arrays

        print(return_text_for_general_query)
        dispatcher.utter_message(text=str(return_text_for_general_query))

class dbQueryMethods:
    def create_connection(sqlTemp):
        """ create a database connection to the SQLite database      
            """
        conn = None
        try:
            conn = sqlite3.connect(sqlTemp)
            print(dbQueryMethods.create_connection)
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
                                FROM Product""")
        column_values = fuzzy_match_cur.fetchall()

        top_match = process.extractOne(slot_value, column_values)

        conn.commit()

        return(top_match[0])

    def select_by_category(conn, slot_value):
        """
        Given a database column & text input, find the 
        closest match for product category.
        """
        cur = conn.cursor()
        cur.execute(f"""SELECT ProductName 
            FROM Product
            WHERE ProductCategory = '{slot_value}'""")

        rows = cur.fetchall()
        conn.commit()

        return(rows)
    
    def select_by_slots(conn,slot_value):
            """
            Query all rows in the tasks table
            :param conn: the Connection object
            :return:
            """
            cur = conn.cursor()
            cur.execute(f"""SELECT ProductName 
                FROM Product
                WHERE ProductRoles = '{slot_value}'""")

            # return an array
            rows = cur.fetchall()
            conn.commit()
            
            return(rows)

    def order_update_insert_query(conn, user_id):
        """ Update the Order table with 
        randomly/uniquely generated user_id and order_id"""

        cur = conn.cursor()
        current_date = time.strftime("%Y-%m-%d")
        chars =  string.ascii_lowercase + string.digits
        order_new_id = ''.join(random.choice(chars) for _ in range(10))
        # insert a new row of data
        cur.execute(f"INSERT INTO `Order`(OrderNumber, CustomerId, OrderDate) VALUES('{order_new_id}','{user_id}','{current_date}')")
        return order_new_id

    def order_status_check(conn, order_new_id):

        cur = conn.cursor() 
        # display the last inserted row
        cur.execute(f"""SELECT * FROM `Order`
         WHERE OrderNumber = '{order_new_id}'""")
        # return an array
        rows = cur.fetchall()
        conn.commit()
        rows = list(rows)
        for row in range(len(rows)):
            return(f"Your order number is {(rows[row][1])} and your order date is {(rows[row][3])}")

    def rows_as_info_text(rows):    
        
            if len(list(rows)) < 1:     #if cursor is carrying Empty Val from query
                return("There are no products matching your query in the database")
            
            else:
                for row in random.sample(rows, 1):
                    return f"we have {row[0]} in stock."

            

