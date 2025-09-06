import os 
import sqlite3
import time 

def alterar():
    
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

    
alterar()