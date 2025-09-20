import os
import sqlite3
from datetime import date

def menu_relatorios():
    while True:
        os.system("cls")
        print("===============================")
        print(" > Relatorios ")
        print("===============================")
        print("1. Relatorio de vendas por dia")
        print("2. Relatorio de vendas por mês")
        print("3. Relatorio de vendas por periodo")
        print("0. Voltar")

        print("===============================")
        opcao = input(" > Digite a opcao : ")
        if opcao == "0":
            break
        elif opcao == "1":
            relatorio_vendas_dia()

def relatorio_vendas_dia():
    
    os.system("cls")
    print("=================================")
    print(" > Relatório vendas por dia ")
    print("=================================")
    
    data = input("\n\n > Digite a data (aaaa-mm-dd): ")

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    sql = "SELECT * FROM orders WHERE order_date = ?"
    cur.execute(sql, (data,))
    rows = cur.fetchall()
    cur.close()
    con.close()
    if rows:
        for row in rows:
            print(row[0])
            pass
        pass
    else:
        os.system("cls")
        print("Não encontrado nenhum pedido na data.")
        input("Digite algo para continuar ...")

    


    

