# Script para alterar tabela de banco de dados.

import sqlite3

def alterar_tabela_pedidos():
    # Acrescentar 2 campos :
    # 1. Status 
    # 2. Valor recebido 

    # 1. Status: Precisa dizer se o pedido foi iniciado, concluido, cancelado.
    # 2. Valor recebido, porque tem descontos.
       
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    sql = "ALTER TABLE orders ADD COLUMN order_status TEXT;"
    cur.execute(sql)
    con.commit()
    
    print("\n> Adicionado coluna status a tabela de Pedidos.")

    sql = "ALTER TABLE orders ADD COLUMN received_value INT;"
    cur.execute(sql)
    con.commit()

    print("\n> Adicionado coluna de valor recebido a tabela de Pedidos.")
    cur.close()
    con.close()

alterar_tabela_pedidos()

