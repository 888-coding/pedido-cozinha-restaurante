import os
import sqlite3


def relatorio_venda_por_mercadorias_mensal():
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
    sql = """
            SELECT DISTINCT oi.product_id FROM orders AS o
            JOIN order_items AS oi 
            ON o.id = oi.order_id
            WHERE strftime('%m', order_date) = ? 
            AND strftime('%Y', order_date) = ?
            """
    cur.execute(sql,(mes.zfill(2),ano,))
    rows = cur.fetchall()

    if rows:
        for row in rows:
            # os id de produtos
            id_product = row[0]
            sql = """
                    SELECT sum(product_qty) AS soma FROM order_items AS oi
                    JOIN orders AS o ON  oi.order_id = o.id
                    WHERE oi.product_id = ? AND strftime('%m', o.order_date) = ? AND strftime('%Y', o.order_date) = ?
                    """
            cur.execute(sql, (id_product, mes.zfill(2), ano,))
            rows = cur.fetchone()
            print("Quantidade por produto")
            sql = ("SELECT code, name_chinese, name_portuguese FROM products WHERE id = ?")
            cur.execute(sql, (id_product,))
            row = cur.fetchone()

            print(f"> Codigo do produto : {row[0]}. Nome: {row[1]} - {row[2]}  Quantidade : {rows[0]}\n")
    else:
        print("Não foi encontrado nenhum registro.")

    cur.close()
    con.close()


relatorio_venda_por_mercadorias_mensal()

