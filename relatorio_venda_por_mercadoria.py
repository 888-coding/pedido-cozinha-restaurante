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
    print("\n\n")

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
            # os id de produtos
            id_product = row[0]
            con = sqlite3.connect("database.db")
            cur = con.cursor()
            sql =   """
                    SELECT sum(product_qty) AS soma FROM order_items 
                    WHERE product_id = ?
                    """
            cur.execute(sql,(id_product,))
            rows = cur.fetchone()
            cur.close()
            con.close()
            print("Quantidade por produto")
            print(f"> id do produto : {id_product} .  Quantidade : {rows[0]}\n")
    else:
        print("Não foi encontrado nenhum registro.")

relatorio_venda_por_mercadorias()