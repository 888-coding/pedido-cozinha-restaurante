import os
import sqlite3
import time 
from datetime import datetime
from rich.console import Console
from rich.table import Table

def consultar():

    # Mostrar um Menu de qual opcao deseja consultar
    # 1- Listar pedido do dia 
    # 2- Outro periodo 
    # 
    # 
    #  

    os.system("cls")

    print("=====================================")
    print(" > Consulta de pedidos")
    print("=====================================")

    print("\n1 . Listar pedidos de hoje ")
    print("2 . Outro periodo")

    while True:
        opcao = input("Escolha a opção : ")
        if opcao == "1" or opcao == "2":
            break

    time.sleep(0.5)
    
    if opcao == "1":
        data_consulta = datetime.now().strftime("%Y-%m-%d")

        con = sqlite3.connect("database.db")
        cur = con.cursor()
        sql = "SELECT id, order_date, order_time, total_value FROM orders WHERE order_date = ? "
        cur.execute(sql, (data_consulta,))
        rows = cur.fetchall()
        cur.close()
        con.close()

        if not rows:
            print("Nao foi encontrado nada!")
        else:
            console = Console()
            tabela = Table(title="Pedido")
            tabela.add_column("Numero Pedido")
            tabela.add_column("Data")
            tabela.add_column("Hora")
            tabela.add_column("Valor")

            for row in rows:
                tabela_pedido = str(row[0])
                tabela_data = row[1]
                tabela_horas = row[2]
                tabela_valor = f"{float(row[3])/100:.2f}"
                tabela.add_row(tabela_pedido, tabela_data, tabela_horas, tabela_valor)
            console.print(tabela)            
    else:
        print("=============================")
        print(" > Outro periodo : ")
        print("=============================")

        periodo_inicial = input("> Digite o periodo inicial : (aaaa-mm-dd)")
        periodo_final = input("> Digite o periodo inicial : (aaaa-mm-dd)")

        print("\n==============================================================")
        print(f"Periodo escolhido é : > {periodo_inicial} até {periodo_final}")
        print("==============================================================")

        con = sqlite3.connect("database.db")
        cur = con.cursor()
        sql = "SELECT id, order_date, total_value FROM orders WHERE order_date >= ? and order_date <= ? ORDER BY id ASC"
        cur.execute(sql, (periodo_inicial, periodo_final,))
        rows = cur.fetchall()
        cur.close()
        con.close()

        if rows:
            venda_total_periodo = 0

            console = Console()
            tabela = Table() 
            tabela.add_column("Numero Pedido")
            tabela.add_column("Data")
            tabela.add_column("Valor", style="green")


            for row in rows:
                tabela_pedido = str(row[0])
                tabela_data = row[1]
                tabela_valor = f"{float(row[2])/100:.2f}"

                tabela.add_row(tabela_pedido, tabela_data, tabela_valor)
                venda_total_periodo += int(row[2])
            
            venda_total_periodo = f"{float(venda_total_periodo)/100:.2f}"
            tabela.add_row("","Total",str(venda_total_periodo))

            console.print(tabela)
        else:
            print("Não foi encontrado pedido nessa data!")
consultar()