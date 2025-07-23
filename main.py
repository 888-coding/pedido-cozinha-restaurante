# main.py 
import sqlite3


##### Banco de dados #####
# Criação do banco de dados 
def create_database():
	con = sqlite3.connect("database.db")
	con.close()

# Criação da tabela de produtos
def create_table_products():
	con = sqlite3.connect("database.db")
	sql = """
		CREATE TABLE IF NOT EXISTS products(
		id INTEGER PRIMARY KEY, 
		name TEXT, 
		price INTEGER
		)
	"""
	cur = con.cursor()
	cur.execute(sql)
	con.close()

# Criaçao da tabela de pedidos 
def create_table_orders():
	con = sqlite3.connect("database.db")
	sql = """
		CREATE TABLE IF NOT EXISTS orders(
		id INTERGER PRIMARY KEY,
		table_number TEXT, 
		order_date DATE, 
		total_value INTEGER 
		)
	"""
	cur = con.cursor()
	cur.execute(sql)
	con.close()

# Criação da tabela de Pedido_e_itens:
def create_table_order_items():
	con = sqlite3.connect("database.db")
	sql = """
		CREATE TABLE IF NOT EXISTS order_items(
			id INTERGER PRIMARY KEY,
			order_id INTERGER, 
			product_id INTERGER,
			product_qty INTERGER, 
			product_value INTERGER
		)
	"""
	cur = con.cursor()
	cur.execute(sql)
	con.close()

# Menu : Principal
def show_main_menu():
	print("================")
	print("7PAM MARKET LTDA")
	print("> MENU")
	print("================")
	print("1. Pedidos")
	print("2. Produtos")
	print("3. Relatorios")
	print("")
	while True: 
		selected_option = int(input("Digite escolha : "))
		if selected_option == 1 or selected_option == 2 or selected_option == 3:
			break
	if selected_option == 1:
		show_order_menu()
	elif selected_option == 2:
		show_product_menu()
	else:
		show_reports_menu()

# Menu : Pedidos 
def show_order_menu():
	pass

# Menu : Produtos 
def show_product_menu():
	pass

# Menu : Relatorios
def show_reports_menu():
	pass

# Procedimentos
create_database()
create_table_products()
create_table_orders()
create_table_order_items()
show_main_menu()