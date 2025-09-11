import os 
import time 
import sqlite3
import datetime

import principal

def PedidosMenu():
    
    time.sleep(1)
    os.system("cls")

    print("===============================")
    print(" > Pedidos")
    print("===============================")
    print("1. Cadastrar")
    print("2. Consultar")

    print("==============================")

    while True:
        opcao = input(" > Opção : ")
        if opcao == "1" or opcao == "2":
            break

    if opcao == "1":
        cadastrar()
    else:
        pedido_consulta()
    


def cadastrar():
    os.system("cls")

    print("======================")
    print("> Cadastro de pedido  ")
    print("======================")
    print("\n")
    mesa = input("> Numero de mesa : ")

    time.sleep(0.5)

    os.system("cls")
    print("======================")
    print(f"> Mesa : {mesa}")
    print("======================")

    print("\nPedido - Digite o codigo da comida: ")


    lista_comidas = [] 
    lista_precos = []
    while True:
        input_comida = input("> Numero da comida: ").upper()

        time.sleep(0.3)
        
        # Sair do adicionar comida
        if input_comida == "0":
            break
        # Acrescentar comida
        else:
            con = sqlite3.connect("database.db")
            cur = con.cursor()
            sql = "SELECT id, name_chinese, name_portuguese, price FROM products WHERE code = ?"
            cur.execute(sql, (input_comida,))
            row = cur.fetchone()
            con.close()
            if row is None:
                # Se não encontrar o codigo, nao faz nada, somente mostra aviso que nao encontrou
                print("Não encontrado!")
            else:
                # Se encontrar o codigo, adiciona ele na lista de comidas de pedido
                lista_comidas.append(row[0])
                lista_precos.append(row[3])
                print(f"> {row[1]} - {row[2]}")


    # imprimir lista de comida 
    print(f"Lista dos codigos dos produtos : {lista_comidas}") 
    print(f"Precos unitarios :{lista_precos}")

    total_value = 0 
    for item in lista_precos:
        total_value += int(item)
    print(f"Valor total : {total_value}")
    # achar o numero de pedido para adicionar. 
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    sql = "SELECT id FROM orders ORDER BY id DESC LIMIT 1"
    cur.execute(sql, () )
    row = cur.fetchone()
    con.close()
    print("================================================")
    if not row:
        numero_pedido_novo = 1
        print("Não tinha cadastro de pedido")
    else:
        print(f"Ultimo numero de pedido é: {row[0]}") 
        numero_pedido_novo = int(row[0]) + 1 

    print("===============================================")
    print(f"novo numero de pedido é : {numero_pedido_novo}")
    print("===============================================")
    # mesa
    print(f"Mesa : {mesa}")
    print("===============================================")
    # data do pedido 
    data_pedido = datetime.today().strftime("%Y-%m-%d")
    hora_pedido = datetime.today().strftime("%H:%M:%S")
    print(f"Data : {data_pedido}")
    print(f"Horas: {hora_pedido}")
    print("===============================================")

    # Cadastrar no banco de dados 
    # Tabela orders 
    # table_number(mesa), order_date(data_pedido), order_time(hora_pedido), total_value(total_value)
    # Tabela order_items
    # order_id(numero_pedido_novo), product_id, product_qty, product_price
    # 
    # 


    # Na Tabela "orders"
    # ------------------
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    sql = """INSERT INTO orders (table_number, order_date, order_time, total_value) 
                VALUES(?, ?, ?, ?)"""
    cur.execute(sql, ( mesa,data_pedido,hora_pedido, total_value, ))
    con.commit()
    con.close()

    # Na Tabela "order_items"
    # -----------------------
    n = len(lista_comidas)

    for i in range(n):
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        sql = """ INSERT INTO order_items(order_id, product_id, product_qty, product_price)
                VALUES (?, ?, ?, ?)
            """
        cur.execute(sql, (numero_pedido_novo, lista_comidas[i],1,lista_precos[i])) #aqui
        con.commit()
        con.close()

    print("Cadastrado com sucesso e todos os produtos cadastrados no pedido.")

def consultar():

    # Mostrar um Menu de qual opcao deseja consultar
    # 1- Listar pedido do dia 
    # 2- Outro periodo 
    # 
    # 
    #  

    os.system("cls")

    print("=====================================")
    print(" > Consulta de pedidos")
    print("=====================================")

    print("\n1 . Listar pedidos de hoje ")
    print("2 . Outro periodo")

    while True:
        opcao = input("Escolha a opção : ")
        if opcao == "1" or opcao == "2":
            break

    time.sleep(0.5)
    
    if opcao == "1":
        data_consulta = datetime.now().strftime("%Y-%m-%d")

        con = sqlite3.connect("database.db")
        cur = con.cursor()
        sql = "SELECT id, order_date, order_time, total_value FROM orders WHERE order_date = ? "
        cur.execute(sql, (data_consulta,))
        rows = cur.fetchall()
        cur.close()
        con.close()

        if not rows:
            print("Nao foi encontrado nada!")
        else:
            for row in rows:
               print(f"Número do pedido : {row[0]}") 
               time.sleep(0.4)
               print(f"   {row[2]}")
               time.sleep(0.4)
               print(f"   {float(row[3])/100:.2f}\n")
    else:
        print("=============================")
        print(" > Outro periodo : ")
        print("=============================")

        periodo_inicial = input("> Digite o periodo inicial : (aaaa-mm-dd)")
        periodo_final = input("> Digite o periodo inicial : (aaaa-mm-dd)")

        print("\n==============================================================")
        print(f"Periodo escolhido é : > {periodo_inicial} até {periodo_final}")
        print("==============================================================")

        con = sqlite3.connect("database.db")
        cur = con.cursor()
        sql = "SELECT id, order_date, total_value FROM orders WHERE order_date >= ? and order_date <= ? ORDER BY id ASC"
        cur.execute(sql, (periodo_inicial, periodo_final,))
        rows = cur.fetchall()
        cur.close()
        con.close()

        venda_total_periodo = 0 
        for row in rows:
            print(row)
            venda_total_periodo += int(row[2])
        print("==========================================")
        print(f"Valor total do periodo : {float(venda_total_periodo)/100:.2f}")
        print("==========================================")


