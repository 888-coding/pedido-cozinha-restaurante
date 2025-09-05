import os 
import sqlite3
from datetime import datetime
import time 

def alterar():
    
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

alterar()