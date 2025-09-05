import os 
import sqlite3

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
    print("produto encontrado ")


alterar()