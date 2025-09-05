import os 
import sqlite3

def alterar():
    
    # Tabela : products 
    # id, code, name_chinese, name_portuguese, price
    # > id, code, name_chinese, name_portugues
    #
    #

    print("============================")
    print(" > Alterar nome do produto")
    print("============================")

    # Consultar o codigo produto
    code = input("\nDigite o codigo do produto : ")
    
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    sql = "SELECT id, code, name_chinese, name_portuguese FROM products WHERE code = ? "
    cur.execute( sql, (code, ) )
    row = cur.fetchone()
    con.close()

alterar()