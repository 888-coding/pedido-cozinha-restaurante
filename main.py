# main.py 
import sqlite3
from datetime import datetime
import os 
import time 
# NOTE: BANCO- Criação do banco de dados 
def create_database():
	con = sqlite3.connect("database.db")
	con.close()

# NOTE: Criação da tabela de produtos
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

# NOTE: BANCO - Criaçao da tabela de pedidos 
def create_table_orders():
	con = sqlite3.connect("database.db")
	sql = """
		CREATE TABLE IF NOT EXISTS orders(
		id INTERGER PRIMARY KEY AUTOINCREMENT,
		table_number TEXT, 
		order_date DATE, 
		total_value INTEGER 
		)
	"""
	cur = con.cursor()
	cur.execute(sql)
	con.commit()
	con.close()

# NOTE: BANCO - Criação da tabela de Pedido_e_itens:
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

# NOTE: Menu : Principal
def show_main_menu():
	os.system("cls")
	print("================")
	print("7PAM MARKET LTDA")
	print("> MENU")
	print("================")
	print("1. Pedidos")
	print("2. Produtos")
	print("3. Relatorios")
	print("4. Sair")
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

# NOTE: Menu : Pedidos 
def show_order_menu():
	# TODO:  
	# Precisa dizer o numero da mesa 
	# Precisa adicionar os produtos desejados 
	# Cada vez que digita o codigo do produto, 
	# mostra o nome do produto 
	pass

# NOTE: Menu : Produtos 
def show_product_menu():
	# TODO: 
	# Cadastro de produto 
	# Consulta do produto 
	# Alterar nome do produto 
	# Alterar preco do produto

	print("")
	print("===========") 
	print("> Produtos")
	print("===========")
	print("1. Cadastrar produto")
	print("2. Consultar")
	print("3. Alterar nome do produto")
	print("4. Alterar preco do produto")
	print("")
	selected_option = int(input("Digite a opcao : ")) 
	if selected_option == 1:
		produto_cadastro()
	elif selected_option == 2:
		produtos_consultarTodo()
	elif selected_option == 3:
		pass
	else:
		produto_alterarPreco()
# NOTE: Menu : Relatorios
def show_reports_menu():
	pass

# NOTE: Produtos > Cadastro 
def produto_cadastro():
	print("\n ====================")
	print(" Cadastro de produto") 
	print(" ====================")
	numero_comida = int(input("Numero da comida : "))
	nome_comida = input("Nome da comida : ").upper()
	valor_comida = 	float(input("Valor da comida : R$ "))
	valor_comida = int(valor_comida * 100)

	# Conexao com banco de dados
	con = sqlite3.connect("database.db")
	sql = """
	INSERT INTO products(id, name, price) VALUES(?, ?, ?)
	"""
	cur = con.cursor()
	cur.execute(sql, (numero_comida, nome_comida, valor_comida))
	con.commit()
	con.close()
	print("\n\n Cadastrado com sucesso !!!")
	time.sleep(4)
	show_main_menu()

def produtos_consultarTodo():
	sql= "SELECT * FROM products ORDER BY id ASC"
	con = sqlite3.connect("database.db")
	cur = con.cursor()
	cur.execute(sql)
	rows = cur.fetchall()
	os.system("cls")
	for row in rows:
		print(f"{row}")

	con.close()
	input("\nDigite para continuar ... ")
	show_main_menu()

def produto_alterarPreco():
	os.system("cls")
	print("Alteracao de preco : ")
	codigo_comida = int(input("\nDigite o numero da comida : "))
	sql = "SELECT * FROM products WHERE id = ?"
	con = sqlite3.connect("database.db")
	cur = con.cursor()
	cur.execute(sql, (codigo_comida,))
	rows = cur.fetchall()
	con.close()

	for row in rows :
		print(row)
	input("Digite algo para voltar ao menu principal ...")
# NOTE: Procedimentos
create_database()
create_table_products()
create_table_orders()
create_table_order_items()
show_main_menu()