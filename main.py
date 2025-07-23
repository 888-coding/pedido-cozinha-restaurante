# main.py 
import sqlite3

def create_database():
	con = sqlite3.connect("database.db")
	con.close()

def create_table_products():
	con = sqlite3.connect("database.db")
	sql = """
	CREATE TABLE products(
	id INTEGER PRIMARY KEY, 
	name TEXT, 
	price INTEGER
	)
	"""
	cur = con.cursor()
	cur.execute(sql)
	con.close()



create_database()
create_table_products()
