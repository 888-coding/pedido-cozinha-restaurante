# main.py 
import sqlite3
from datetime import datetime, date
import os 
import time 
import win32print
import win32ui

# NOTE: BANCO- Criação do banco de dados 
def create_database():
	con = sqlite3.connect("database.db")
	con.close()

# NOTE: Criação da tabela de produtos
def create_table_products():
	con = sqlite3.connect("database.db")
	sql = """
		CREATE TABLE IF NOT EXISTS products(
		id TEXT, 
		name_chinese TEXT,
		name_portuguese TEXT, 
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
			product_id TEXT,
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
		selected_option = input("Digite escolha : ")
		if selected_option == "1" or selected_option == "2" or selected_option == "3" or selected_option == "4" :
			break
	if selected_option == "1":
		show_order_menu()
	elif selected_option == "2":
		show_product_menu()
	elif selected_option == "3":
		show_reports_menu()
	else:
		exit()

# NOTE: Menu : Pedidos 
def show_order_menu():
	# TODO:  
	# Precisa dizer o numero da mesa 
	# Precisa adicionar os produtos desejados 
	# Cada vez que digita o codigo do produto, 
	# mostra o nome do produto 
	os.system("cls")
	print("===========") 
	print("> Pedido")
	print("===========")
	print("\n1. Novo Pedido")
	print("2. Consultar pedidos de hoje")
	print("3. Voltar para menu iniciar")

	while True:
		selected_option = input("\nEscolha a opcao : ")
		if selected_option == "1" or selected_option == "2" or selected_option == "3":
			break 

	if selected_option == "1":
		insert_order()
	elif selected_option == "2":
		orders_today()
	else :
		show_main_menu()

# NOTE: Inserir Pedido
def insert_order():
	os.system("cls")
	print("===========") 
	print("> Pedido")
	print("===========")
	numero_mesa = input("Digite o numero da mesa : ") 
	data_hora_pedido = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
	print(f"Data e hora : {data_hora_pedido}")
	print(data_hora_pedido)

	con = sqlite3.connect("database.db")
	cur = con.cursor()
	sql = "INSERT INTO orders(table_number, order_date) VALUES (?, ?)"
	cur.execute(sql, (numero_mesa, data_hora_pedido,))
	con.commit()
	id_order = cur.lastrowid
	print(f"Temporario :: ID do pedido é : {id_order}")

	con.close()

	# Looping de adicionar itens , Quando digitar 0 , não adiciona mais itens
	valor_total = 0 
	while True:
		print("\n Adicione item : ")
		numero_comida_inserir = input("Digite numero da comida : ")
		print("\n(Para sair digite comida como 0)")
		if numero_comida_inserir == "0":
			break
		else:
			con = sqlite3.connect("database.db")
			cur = con.cursor()
			sql = "SELECT * FROM products WHERE id = ?"
			cur.execute(sql, (numero_comida_inserir,))
			rows = cur.fetchone()
			con.close()
			if rows :
				# Comida encontrada
				con = sqlite3.connect("database.db")
				cur = con.cursor()
				valor_comida = int(rows[3])
				valor_total += valor_comida
				sql = "INSERT INTO order_items(order_id, product_id, product_qty, product_value) VALUES (?, ?, ?, ?)"
				cur.execute(sql,(id_order, numero_comida_inserir, 1,valor_comida,))
				con.commit()
				con.close()
			else:
				# Nao existe comida
				print("\nErro , numero da comida nao encontrada.") 
	# Fim do Looping  
	
	# Atualizar valor total na tabela de orders
	sql = "UPDATE orders SET total_value = ? WHERE ROWID = ? "
	con = sqlite3.connect("database.db")
	cur = con.cursor()
	cur.execute(sql, (valor_total, id_order,) )
	con.commit()
	con.close()

	# Mostrar Dados do pedido, adicionando linhas de impressao no variavel
	os.system("cls")
	print("\n\n   DADOS DO PEDIDO : ")
	print(f"NUMERO DO PEDIDO : {id_order}")
	impressao_linhas= []
	impressao_linha_data = str(data_hora_pedido)
	impressao_linhas.append(impressao_linha_data)
	impressao_linha_pedido = "No. : " + str(id_order)
	impressao_linha_mesa = "Mesa : " + str(numero_mesa)
	impressao_linhas.append(impressao_linha_pedido)
	impressao_linhas.append(impressao_linha_mesa)
	con = sqlite3.connect("database.db")
	cur = con.cursor()
	sql = "SELECT * FROM order_items WHERE order_id = ? "
	cur.execute(sql, (id_order,))
	rows = cur.fetchall()
	con.close()
	valor_total = 0
	
	for row in rows:
		# Mostrar todos os itens do pedido 
		con = sqlite3.connect("database.db")
		cur = con.cursor()
		sql = "SELECT name_chinese, name_portuguese FROM products WHERE id = ? "
		cur.execute(sql, (row[2],))
		nome_comida = cur.fetchone()
		nome_comida_chinese = nome_comida[0]
		nome_comida_portuguese = nome_comida[1]
		codigo_comida = row[2]
		preco_comida = row[4]
		impressao_linha_comida = f"{codigo_comida} - {nome_comida_chinese} {preco_comida/100:.2f}"
		impressao_linhas.append(impressao_linha_comida)
		impressao_linha_comida = f"{nome_comida_portuguese}"
		impressao_linhas.append(impressao_linha_comida)
		valor_total += int(preco_comida)
		cur.close()
		con.close()
		print(f"     Numero da comida : {codigo_comida}  - {nome_comida[0]} - Valor da comida :  {(preco_comida/100):.2f}")
	
	print(f"TOTAL : {(valor_total/100):.2f}")
	impressao_linha_branca = " "
	impressao_linhas.append(impressao_linha_branca)
	impressao_linha_valor_total = f"TOTAL : {valor_total/100:.2f}"
	impressao_linhas.append(impressao_linha_valor_total)
	impressao_linhas.append(impressao_linha_branca)
	impressao_linhas.append(impressao_linha_branca)
	
	input("\nDigite algo para continuar com impressao ..")
	
	for linha in impressao_linhas:
		print(linha)
	time.sleep(3)

	# Impressão em imprimessora térmica SWEDA
	printer_name = "Microsoft Print to PDF" # Nome da impressora 
	hprinter = win32print.OpenPrinter(printer_name) # Abrir impressora 
	printer_info = win32print.GetPrinter(hprinter, 2)
	hDC = win32ui.CreateDC() # Iniciar o trabalho de impressao
	hDC.CreatePrinterDC(printer_name)
	hDC.StartDoc("Teste Python")
	hDC.StartPage()
	font = win32ui.CreateFont({"name": "SimSum", "height": 40, "weight": 700}) # Fonte Chines
	hDC.SelectObject(font)
	left = 20
	top = 30
	for impressao_linha in impressao_linhas:
		hDC.TextOut(left,top,impressao_linha)
		top += 40
	
	hDC.EndPage()
	hDC.EndDoc()
	hDC.DeleteDC()
	
	show_main_menu()

#NOTE: Pedido do dia 
def orders_today():
	# TODO: Mostrar as vendas do dia 
	os.system("cls")
	print("Pedidos > Vendas do dia >")
	con = sqlite3.connect("database.db")
	cur = con.cursor()
	data_hoje = date.today()
	sql = "SELECT ROWID, table_number, total_value FROM orders WHERE DATE(order_date) = ? "
	cur.execute(sql, (data_hoje,))
	rows = cur.fetchall()
	cur.close()
	con.close()
	venda_do_dia = 0
	
	for row in rows:
		rowid = row[0]
		table_number = row[1]
		total_value = row[2]
		venda_do_dia += total_value
		print(f"Pedido : {rowid}  Mesa : {table_number}  .  Valor total : {(total_value/100):.2f}")
	print("\n\n")
	print(f"Valor total : {(venda_do_dia/100):.2f}")
	print("\n\n")
	input("Digite algo para continuar ...")
	show_main_menu()

# NOTE: Menu : Produtos 
def show_product_menu():
	# TODO: 
	os.system("cls")
	print("")
	print("===========") 
	print("> Produtos")
	print("===========")
	print("1. Cadastrar produto")
	print("2. Consultar")
	print("3. Alterar nome do produto")
	print("4. Alterar preco do produto")
	print("5. Voltar Menu principal")
	print("")
	while True: 
		selected_option = input("Digite a opcao : ")
		if selected_option == "1" or selected_option == "2" or selected_option == "3" or selected_option == "4" or selected_option == "5":
			break 
	if selected_option == "1":
		produto_cadastro()
	elif selected_option == "2":
		produtos_consultarTodo()
	elif selected_option == "3":
		produto_alterarNome()
	elif selected_option == "4":
		produto_alterarPreco()
	else:
		show_main_menu()

# NOTE: Menu : Relatorios
def show_reports_menu():
	os.system("cls")
	print("> Relatorios > ")
	print("===============")
	print("1. Vendas por periodo (todos produtos)")
	print("2. Vendas por periodo (um produto)")
	print("3. Voltar Menu principal")

	while True:
		selected_option = input("Digite o item desejado : ")
		if selected_option == "1" or selected_option == "2" or selected_option == "3":
			break

	if selected_option == "1":
		report_vendas_todos_produtos()
	elif selected_option == "2":
		pass
	else:
		show_main_menu()

# NOTE: Relatorio > Vendas todos os produtos 
def report_vendas_todos_produtos():

	# Relatorio Todos os produtos, Precisa mostra tudo que vendeu de produtos. exemplo: yakissoba : 10 un.
	os.system("cls")
	print("Relatorio de todos os produtos por periodo ")
	print("****************************************** ")

	data_inicio = input("Digite a data de inicio (aaaa-mm-dd) : ") 
	# data_inicio += " 00:00:01"

	data_fim = input("Digite a data de fim (aaaa-mm-dd)")
	# data_fim += " 23:59:59"

	# sql = "SELECT ROWID, order_date, total_value FROM orders WHERE date(order_date) >= ?  AND date(order_date) <= ? "
	sql = """
		SELECT ROWID, order_date, total_value 
		FROM orders 
		WHERE date(order_date) >= ? 
			AND date(order_date) <= ?
	"""
	con = sqlite3.connect("database.db")
	cur = con.cursor()
	cur.execute(sql, (data_inicio, data_fim, ))
	rows = cur.fetchall()
	con.close()
	
	# Mostrar as linhas dos pedidos
	valor_total_periodo = 0
	for row in rows:
		for i in range(3):
			if i == 0:
				linha = f"No Pedido : {row[i]} - "
			elif i == 1:
				linha += f"Data : {row[i]}"
			else:
				linha += f" Valor : {float(row[i]/100):.2f}"
				print(linha)
				valor_total_periodo += row[i]

	print(f"\n\nValor total do periodo : {float(valor_total_periodo/100):.2f}")
	print("\n\n")
	input("Digite algo para continuar ... ")
	show_main_menu()
		
	#aqui

# NOTE: Produtos > Cadastro 
def produto_cadastro():
	print("\n ====================")
	print(" Cadastro de produto") 
	print(" ====================")
	codigo_comida = input("Codigo da comida : ").upper()
	nome_comida_chinese = input("Nome da comida(chines) : ").upper()
	nome_comida_portuguese = input("Nome da comida(portugues) : ").upper()
	valor_comida = 	int(float(input("Valor da comida : R$ ")) * 100)

	con = sqlite3.connect("database.db")
	sql = """
	INSERT INTO products(id, name_chinese, name_portuguese, price) VALUES(?, ?, ?, ?)
	"""
	cur = con.cursor()
	cur.execute(sql, (codigo_comida, nome_comida_chinese, nome_comida_portuguese, valor_comida))
	con.commit()
	con.close()
	print("\n\n Cadastrado com sucesso !!!")
	input("Digite enter para continuar ... ")
	show_main_menu()

# NOTE: Mostra todos os produtos
def produtos_consultarTodo():
	sql= "SELECT id, name_chinese, name_portuguese, price FROM products ORDER BY id ASC"
	con = sqlite3.connect("database.db")
	cur = con.cursor()
	cur.execute(sql)
	rows = cur.fetchall()
	os.system("cls")
	for row in rows:
		preco = row[3] / 100
		print(f"{row[0]} - {row[1]} - {row[2]} : {preco:.2f}")

	con.close()
	input("\nDigite para continuar ... ")
	show_main_menu()

# NOTE: Alterar nome do produto 
def produto_alterarNome():
	os.system("cls")
	print("Alteracao de nome da comida : ")
	codigo_comida = input("\nDigite o numero da comida : ").upper()
	sql = "SELECT * FROM products WHERE id = ?"
	con = sqlite3.connect("database.db")
	cur = con.cursor()
	cur.execute(sql, (codigo_comida,) )
	rows = cur.fetchall()
	con.close()

	for row in rows : 
		i = 0 
		for i in range(3):
			if i == 0:
				id_product = row[0]
				print(f"Codigo da comida : {row[0]}")
			elif i == 1:
				print(f"Nome da comida (chines): {row[1]}")
			elif i == 2:
				print(f"Nome da comida (portugues): {row[2]}")
			else:
				print(f"Preco da comida : {row[2]}")
	print("Novo nome da comida ")
	novo_nome_comida_chinese = input("Digite o nome novo da comida (chines) : ").upper()
	novo_nome_comida_portugues = input("Digite o nome novo da comida (portugues) : ").upper()
	# Conexao banco de dados para alterar nome 
	sql = "UPDATE products SET name_chinese = ?, name_portuguese = ? WHERE ID = ? "
	con = sqlite3.connect("database.db")
	cur = con.cursor()
	cur.execute(sql, (novo_nome_comida_chinese, novo_nome_comida_portugues, id_product,))
	con.commit()
	con.close()

	print("Atualizacao feita com sucesso , nome alterado!")
	input("\nDigite algo para continuar ...")
	show_main_menu()

# NOTE: Alterar preco do produto
def produto_alterarPreco():
	os.system("cls")
	print("Alteracao de preco : ")
	codigo_comida = input("\nDigite o numero da comida : ").upper()
	sql = "SELECT * FROM products WHERE id = ?"
	con = sqlite3.connect("database.db")
	cur = con.cursor()
	cur.execute(sql, (codigo_comida,))
	rows = cur.fetchall()
	con.close()

	for row in rows:
		i = 0 
		for i in range(4):
			if i == 0 :
				id_product = row[0]
				print(f"Codigo da comida : {row[i]}")
			elif i == 1 :
				print(f"Nome da comida : {row[1]} {row[2]}")
			else : 
				print(f"Preco da comida : {row[3]}")
		
	print("/n/nQual valor novo vc deseja ?")
	novo_valor = int(float(input("Digite novo valor : R$ ")) * 100)

	sql = "UPDATE products SET price = ? WHERE ID = ? "
	con = sqlite3.connect("database.db")
	cur = con.cursor()
	cur.execute(sql, (novo_valor,id_product,))
	con.commit()
	con.close()
	print("\n\nAtualizacao feita .. ")

	input("\nDigite algo para voltar ao menu principal ...")
	show_main_menu()
	
# NOTE: Procedimentos
create_database()
create_table_products()
create_table_orders()
create_table_order_items()
show_main_menu()