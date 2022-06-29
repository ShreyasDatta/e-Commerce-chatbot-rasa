# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from multiprocessing import connection
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import sqlite3
from sqlite3 import Error
import random 


class QueryProductIinfo(Action):

    def name(self) -> Text:
        return "query_product_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = create_connection("chatb_db/sqlTemp.db")
        slot_value = tracker.get_slot("products")
        # slot_name = "Type"
        # pt = tracker.get_latest_entity_values(entity_type="product")
        get_query_result =select_by_slots(conn, slot_value)
        dispatcher.utter_message(text=get_query_result)
    
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


        rows = cur.fetchall()
    #if cursor is carrying Empty Val from query
        if len(list(rows)) < 1:
            return("There are no products matching your query in the database")
        
        else:
            for row in random.sample(rows, 1):
                return(f"Would you be interested in this product, we have {row}")

        conn.commit()
        conn.close()

        return []

