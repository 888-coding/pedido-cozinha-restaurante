import os 
import sqlite3
from rich.console import Console
from rich.table import Table
import time


def pedido_alterar():
    os.system("cls")
    console = Console()
    tabela = Table()

    print("==================================")
    print("Alterar pedido ")
    print("==================================")

    numero_pedido = int(input("> Digite o numero do pedido : "))

    con = sqlite3.connect("database.db")
    cur = con.cursor()

    sql = "SELECT id, table_number, order_date, order_time, total_value FROM orders WHERE id = ?"
    cur.execute(sql,(numero_pedido,))
    row = cur.fetchone()

    if row:
        print("> Encontrado!")
        time.sleep(0.5)
        os.system("cls")

        print(f"No. {numero_pedido}")
        print(f"Data: {row[2]}")
        print(f"Horas: {row[3]}")
        print(f"Mesa: {row[1]}")
        print(f"Valor Total: {float(row[4])/100:.2f}")

        sql = "SELECT * FROM order_items WHERE order_id = ?"
        cur.execute(sql, (numero_pedido,))
        rows = cur.fetchall()

        if rows:
            tabela.add_column("Codigo Produto")
            tabela.add_column("Nome")
            tabela.add_column("Quantidade")
            tabela.add_column("Preco")

            for row in rows:
                item_id = row[0]
                order_id = row[1]
                product_id = str(row[2])
                product_qty = str(row[3])
                product_price = str(row[4])
                tabela.add_row(product_id, "", product_qty, product_price)
            console.print(tabela)
        else:
            print("Não encontrado itens ")


    else:
        print("Não encontrado ...")
        time.sleep(0.8)


    cur.close()
    con.close()


pedido_alterar()