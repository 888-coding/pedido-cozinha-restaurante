import os
from datetime import datetime
import time
import sqlite3

def menu_produtos():
    while True:
        os.system("cls")
        print("==================================")
        print(" > SISTEMA 7P > MENU DE PRODUTOS")
        print("==================================")
        print("1. Cadastrar")
        print("2. Consultar")
        print("3. Alterar preco")
        print("4. Alterar nome")
        print("0. Voltar")
        
        opcao = input("\n\n> Opcao: ")

        if opcao == "1":
            produto_cadastrar()
        elif opcao == "2":
            produtos_consultar()
        elif opcao == "3":
            alterar_preco()
        if opcao == "4":
            alterar_nome()
        elif opcao == "0":
            break
        else: 
            print("\n\nOpcao invalida")
            time.sleep(0.8)

def produto_cadastrar():
    
    # Cadastrar produto 
    # Tabela : id, code, name_chinese, name_portuguese, price
    # 
    # 

    os.system("cls")
    
    print("==========================")
    print(" >  Cadastro de produto ")
    print("==========================")

    code = input("\n> CODIGO DO PRODUTO : ").upper()
    name_chinese = input("> NOME CHINES : ")
    name_portuguese = input("> NOME PORTUGUES : ").upper()
    input_price = input("> PREÇO : R$ ")

    price = float(input_price) * 100
    
    # Inserir dados , code, name_chinese, name_portuguese, price
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    sql = """
        INSERT INTO products (code, name_chinese, name_portuguese, price)
        VALUES (?, ?, ?, ?)
    """
    cur.execute(sql, (code, name_chinese, name_portuguese, price) )
    con.commit()
    con.close()

    print("Cadastrado com sucesso ! ")
    time.sleep(1)

def produtos_consultar():
    os.system("cls")
    print("=================================")
    print(" > Consultar todos os produtos")
    print("=================================")

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    sql = "SELECT id, code, name_chinese, name_portuguese, price FROM products ORDER BY code ASC"
    cur.execute(sql, ())
    rows = cur.fetchall()
    cur.close()
    con.close()

    for row in rows:
        print(f"Codigo : {row[1]} - {row[2]} {row[3]} Preço: {float(row[4])/100:.2f}")

    print("\n\n Fim de linha .")
    input("Tecle para continuar ..")
    time.sleep(1.5)   


def alterar_preco():
    
    # Tabela products 
    # id, code, name_chinese, name_portuguese, price  
    # 
    # 
    # 

    while True:    
        # input do id para procurar 
        os.system("cls")
        print("====================")
        print("> Procurar produto  ")
        print("====================")

        code = str(input("\n> Digite o codigo : ").upper())
        
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        sql = "SELECT id, code, name_chinese, name_portuguese, price FROM products WHERE code = ? "
        cur.execute(sql, (code,) )
        row = cur.fetchone()
        con.close()
        if not row:
            input("Nao encontrado!")
        else:
            break

    time.sleep(0.5)

    id = row[0]
    code = row[1]
    name_chinese = row[2]
    name_portugues = row[3]
    old_price = row[4]

    old_price = float(old_price) / 100 

    print(f"Codigo : {code}")
    time.sleep(0.4)
    print(f"Nome : {name_chinese} - {name_portugues}")
    time.sleep(0.4)
    print(f"Preço: {old_price:.2f}")
    time.sleep(0.4)

    while True:
        deseja = input("Deseja alterar (s/n) ? : ").upper()
        if deseja == "S" or deseja == "N":
            break
    
    if deseja == "S":
        # Novo valor 
        new_price = input("Digite o novo valor : R$ ")
        new_price = float(new_price) * 100

        # Atualizar no banco de dados 
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        sql = "UPDATE products SET price = ? WHERE id = ? "
        cur.execute(sql, (new_price, id, ) )
        con.commit()
        con.close()

        print("Preço alterado com sucesso ! ")
    else:
        print("Ok. Não foi alterado o preço")

def alterar_nome():
    
    # Tabela : products 
    # id, code, name_chinese, name_portuguese, price
    # > id, code, name_chinese, name_portugues
    #
    #
    os.system("cls")
    print("============================")
    print(" > Alterar nome do produto")
    print("============================")

    # Consultar o codigo produto
    while True:
        code = input("\nDigite o codigo do produto : ")
    
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        sql = "SELECT id, code, name_chinese, name_portuguese FROM products WHERE code = ? "
        cur.execute( sql, (code, ) )
        row = cur.fetchone()
        con.close()

        if not row:
            print("Produto não encontrado!")
        else:
            break
    
    id = row[0]
    code = row[1]
    name_chinese = row[2]
    name_portuguese = row[3]
    
    print(f"Codigo : {code}")
    time.sleep(0.4)    
    print(f"Nome : {name_chinese} - {name_portuguese}")
    time.sleep(0.4)
    
    while True:
        deseja = input("Deseja alterar (s/n) ? ").upper()
        if deseja == "S" or deseja == "N":
            break
    
    time.sleep(0.4)

    # Novo nome 
    new_name_chinese = input("Novo nome em chinês : ").upper()
    new_name_portuguese = input("\nNovo nome em português : ").upper()

    # Alterar no banco de dados os nomes
    con = sqlite3.connect("database.db")    
    cur = con.cursor()
    sql = "UPDATE products SET name_chinese = ?, name_portuguese = ? WHERE id = ?"
    cur.execute(sql, (new_name_chinese,new_name_portuguese, id, ))
    con.commit()
    con.close()

    time.sleep(0.4)
    print("Atualizado com sucesso ")
