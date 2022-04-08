from tkinter import NONE
import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host_name,
    user_name,user_payment,
    user_balance, user_discount):
    connection = NONE
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            payment=user_payment,
            balance=user_balance,
            discount=user_discount
        )
        print ("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
        
    return connection

connection = create_server_connection("localhost", "root", pw)

