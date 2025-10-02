import os 
import sqlite3
import time
from rich.console import Console
from rich.table import Table


def produtos_consultar():
    os.system("cls")
    print("=================================")
    print(" > Consultar todos os produtos")
    print("=================================")


    console = Console()
    tabela = Table(title="Produtos ")
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    sql = "SELECT id, code, name_chinese, name_portuguese, price FROM products ORDER BY code ASC"
    cur.execute(sql, ())
    rows = cur.fetchall()
    cur.close()
    con.close()

    tabela.add_column("CODIGO", style="cyan")
    tabela.add_column("DESCRICAO", style="white")
    tabela.add_column("PRECO", style="green")

    for row in rows:
        valor_formatado = str(f"{float(row[4])/100:.2f}")
        code = str(row[1])
        descricao = row[2] + " - " + row[3]
        tabela.add_row(code, descricao, valor_formatado)

    console.print(tabela)
    print("\n\n Fim de linha .")
    input("Tecle para continuar ..")
    time.sleep(1.5)

produtos_consultar()