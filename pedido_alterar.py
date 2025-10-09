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
    print(" > Alterar pedido ")
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

        sql = """SELECT oi.id, oi.order_id, p.code, oi.product_qty, oi.product_price, p.name_portuguese
        FROM order_items AS oi
        JOIN products AS p ON oi.product_id = p.id 
        WHERE order_id = ?"""
        cur.execute(sql, (numero_pedido,))
        rows = cur.fetchall()
        cur.close()
        con.close()

        if rows:
            tabela.add_column("ID Item")
            tabela.add_column("Codigo Produto")
            tabela.add_column("Nome")
            tabela.add_column("Quantidade", style="cyan")
            tabela.add_column("Preco", style="green")
            i = 0
            for row in rows:

                item_id = str(row[0])
                order_id = row[1]
                product_id = str(row[2])
                product_qty = str(row[3])
                product_price = str(f"{float(row[4])/100:.2f}")
                product_name_portuguese = row[5]
                tabela.add_row(item_id,product_id, product_name_portuguese, product_qty, product_price)
            console.print(tabela)

            print("\nOpções: ")
            print("1. Alterar item")
            print("2. Excluir item")
            opcao = input("> Digite a opcao : ")

            if opcao == "1":
                pedido_alterar_item_alterar(numero_pedido)
            elif opcao == "2":
                pedido_alterar_item_deletar()
            else:
                return 
        else:
            print("Não encontrado itens ")


    else:
        print("Não encontrado ...")
        time.sleep(0.8)



def pedido_alterar_item_alterar(numero_pedido):
    while True:
        numero_item = int(input(f"No {numero_pedido}, informe o numero do item para alterar : "))
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        sql = "SELECT product_id, product_qty,product_price FROM order_items WHERE id = ? AND order_id = ? "
        cur.execute(sql, (numero_item, numero_pedido) )
        row = cur.fetchone()
        if row:
            break
        else:
            print("Não encontrado")
    print(row)
    numero_pedido = numero_pedido
    numero_item = numero_item
    old_product_id = row[0]
    old_prodcut_qty = row[1]
    old_product_price = row[2]

def pedido_alterar_item_deletar():
    print("Deletar item")
    time.sleep(1)

pedido_alterar()