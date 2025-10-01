import os 
import sqlite3
from rich.console import Console
from rich.table import Table

def relatorio_vendas_periodo():
    os.system("cls")
    print("=====================================")
    print(" > Relatorio vendas por periodo")
    print("=====================================")

    print("\n\nInicio : ")
    inicio_ano = input("> Digite o ano : ")
    inicio_mes = input("> Digite o mes : ")
    inicio_dia = input("> Digite o dia : ")
    inicio_data = inicio_ano + "-" + inicio_mes.zfill(2) + "-" + inicio_dia.zfill(2)

    print("\n\nFim : ")
    fim_ano = input("> Digite o ano : ")
    fim_mes = input("> Digite o mes : ")
    fim_dia = input("> Digite o dia : ")
    fim_data = fim_ano + "-" + fim_mes.zfill(2) + "-" + fim_dia.zfill(2)

    print(f"\n\nVoce digitou inicio de : {inicio_data}   e o fim de : {fim_data}")

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    sql = "SELECT id, order_date, order_time, total_value FROM orders WHERE order_date >= ? AND order_date <= ? "
    cur.execute(sql, (inicio_data, fim_data, ) )
    rows = cur.fetchall()
    cur.close()
    con.close()

    console = Console()
    tabela = Table(title="Relatório de vendas por periodo")  
    tabela.add_column("No Pedido")
    tabela.add_column("Data")
    tabela.add_column("Horario", justify="right")
    tabela.add_column("Valor do pedido", justify="right", style="green")

    if rows:
        # Existe dados 
        valor_total_periodo = 0 
        for row in rows:
            valor_total_periodo = valor_total_periodo + row[3]
            
            pedido_id = row[0]
            pedido_data = row[1]
            pedido_horario = row[2]
            pedido_valor = float(row[3])/100
            
            valor_formatado = f"{pedido_valor:.2f}"
            
            tabela.add_row(str(pedido_id), pedido_data, pedido_horario, str(valor_formatado))
        valor_formatado = f"{float(valor_total_periodo)/100:.2f}"
        tabela.add_row(" ", " ", "Total: ", str(valor_formatado))
    else:
        # Não existe dados 
        tabela.add_row("n/d","n/d", "n/d", "n/d")
    console.print(tabela)
relatorio_vendas_periodo()