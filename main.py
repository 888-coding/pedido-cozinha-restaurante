# main.py 
import sqlite3

def create_database():
	con = sqlite3.connect("database.db")
	con.close()

def create_table_product():
	sql = ""
	con = sqlite3.connect("database.db")
	cur = con.cursor()
	
create_database()
