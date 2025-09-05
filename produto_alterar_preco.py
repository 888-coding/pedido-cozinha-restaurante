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

    print(row)
    
    id = row[0]
    code = row[1]
    name_chinese = row[2]
    name_portugues = row[3]
    old_price = row[4]

    print(f"Codigo : {code} - {name_chinese}  {name_portugues}  Preco antigo: {old_price}")

alterar()