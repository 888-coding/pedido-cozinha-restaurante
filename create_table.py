import sqlite3
import os 
from datetime import datetime, date
import time 

def create_tables():
    # Criação da tabela: orders 
    # Campos : id, date, time, total_value
    # id, autoincremento 
    # date, somente a data
    # time, somente HH:MM:SS
    # total_valeu, valor total do pedido.

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    sql = """
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            table_number TEXT NOT NULL,
            order_date TEXT NOT NULL,
            order_time TEXT NOT NULL,
            total_value INTEGER NOT NULL
        )
        """
    cur.execute(sql,())
    con.close()

    # Criação da tabela:  "products"
    # Campos : id, name_chinese, name_portuguese, price
    #
    #

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    sql = """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT NOT NULL,
                name_chinese TEXT NOT NULL, 
                name_portuguese TEXT NOT NULL, 
                price INTEGER
            ) 
    """
    cur.execute(sql, ())
    con.close()


    # Criação da tabela : order_items
    # id, order_id
    # product_id, product_qty, product_price
    #
    #
    #

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    sql = """
        CREATE TABLE IF NOT EXISTS order_items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL, 
        product_id INTEGER NOT NULL, 
        product_qty INTEGER NOT NULL, 
        product_price INTEGER NOT NULL
        )
    """
    cur.execute(sql, ())
    con.close()


create_tables()
