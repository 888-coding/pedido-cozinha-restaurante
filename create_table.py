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

