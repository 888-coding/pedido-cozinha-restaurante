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

    numero_pedido = int(input("> Digite o numero do pedido (zero para sair): "))

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
            print("0. Voltar")
            opcao = input("> Digite a opcao : ")

            if opcao == "1":
                pedido_alterar_item_alterar(numero_pedido)
            elif opcao == "2":
                pedido_alterar_item_deletar(numero_pedido)
            elif opcao == "0":
                return
            else:
                print("Escolha errado!") 
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
        sql = """SELECT oi.product_id, oi.product_qty,oi.product_price, p.name_portuguese
        FROM order_items AS oi
        JOIN products AS p ON oi.product_id = p.id
        WHERE oi.id = ? AND oi.order_id = ? """
        cur.execute(sql, (numero_item, numero_pedido) )
        row = cur.fetchone()
        if row:
            break
        else:
            print("Não encontrado")
    numero_pedido = numero_pedido
    numero_item = numero_item
    old_product_id = row[0]
    old_product_qty = row[1]
    old_product_price = row[2]
    old_product_name = row[3]

    tabela = Table()
    console = Console()

    tabela.add_column("Numero Pedido")
    tabela.add_column("Numero Item")
    tabela.add_column("id do Produto")
    tabela.add_column("Quantidade")
    tabela.add_column("Preco")
    tabela.add_column("Nome")

    tabela.add_row(str(numero_pedido), str(numero_item), str(old_product_id), str(old_product_qty), str(old_product_price), old_product_name)
    console.print(tabela)    

    # Novo codigo do produto 
    while True:
        novo_codigo_comida = input("\n\n > Digite o novo codigo da comida : ")
        sql = "SELECT id, code, name_portuguese, price FROM products WHERE code = ? "
        cur.execute(sql, (novo_codigo_comida,) )
        row = cur.fetchone()
        if row:
            novo_id_comida = int(row[0])
            novo_preco_comida = int(row[3])
            break
        else: 
            print("Codigo nao encontrado !")
    
    # Novo codigo encontrado, e correto, portanto agora faço update na tabela de 'items de pedidos'
    sql = "UPDATE order_items SET product_id = ?, product_price = ? WHERE id = ? "
    cur.execute(sql, (novo_id_comida, novo_preco_comida,numero_item, ) )
    con.commit()

    print("Numero pedido : ")
    print(numero_pedido)
    time.sleep(0.4)
    
    # Fazendo update na tabela 'orders' com o valor total atualizado.
    sql = "SELECT product_price, product_qty FROM order_items WHERE order_id = ? "
    cur.execute(sql, (numero_pedido,) )
    rows = cur.fetchall()

    if rows:
        total_da_venda = 0
        for row in rows:
            preco = row[0]
            quantidade = row[1]
            preco_total_da_comida = preco * quantidade
            total_da_venda += preco_total_da_comida
            print(f"Preco total da comida (quantidade x valor unitario) : {float(preco_total_da_comida)/100:.2f} ")
        print(f"\nTotal da venda : {total_da_venda/100:.2f}")
        sql = "UPDATE orders SET total_value = ? WHERE id = ? "
        cur.execute(sql, (total_da_venda, numero_pedido, ))
        con.commit()
        time.sleep(0.4)
        print("\n\nAtualizado o valor do total da venda do pedido")
        #aqui
    else:
        print("Não existe")



    print("Atualizado com sucesso!")
    input("Pressione para continuar ..")
    
    cur.close()
    con.close()

def pedido_alterar_item_deletar(numero_pedido):
    tabela = Table()
    console = Console()
    numeracao_item = input("> Qual o numero de item deseja excluir ? :")
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    sql = "SELECT * FROM order_items WHERE order_id = ? AND id = ?"
    cur.execute(sql, (numero_pedido, numeracao_item,) )
    row = cur.fetchone()
    if row :
        print("achou")
    else:
        print("Erro, numeracao do item errado!")

pedido_alterar()