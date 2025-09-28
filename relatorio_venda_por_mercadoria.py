import os 
import sqlite3
def relatorio_venda_por_mercadorias():
    os.system("cls")
    print("======================================")
    print(" > Relatorio Vendas por mercadorias")
    print("======================================")

    print("\nPeriodo Mensal ")
    ano = input("Digite ano: ")
    mes = input("Digite o mes: ")

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    sql =   """
            SELECT DISTINCT oi.product_id FROM orders AS o
            JOIN order_items AS oi 
            ON o.id = oi.order_id
            """
    cur.execute(sql,() )
    rows = cur.fetchall()
    cur.close()
    con.close()
    
    if rows:
        for row in rows:
            print(row)
    else:
        print("Não foi encontrado nenhum registro.")

relatorio_venda_por_mercadorias()