import os 
import sqlite3

def relatorio_vendas_periodo():
    os.system("cls")
    print("=====================================")
    print(" > Relatorio vendas por periodo")
    print("=====================================")

    print("\n\nInicio : ")
    inicio_ano = input("> Digite o ano : ")
    inicio_mes = input("> Digite o mes : ")
    inicio_dia = input("> Digite o dia : ")
    inicio_data = inicio_ano + inicio_mes.zfill(2) + inicio_dia.zfill(2)

    print("\n\nFim : ")
    fim_ano = input("> Digite o ano : ")
    fim_mes = input("> Digite o mes : ")
    fim_dia = input("> Digite o dia : ")
    fim_data = fim_ano + fim_mes.zfill(2) + fim_dia.zfill(2)

    print(f"\n\nVoce digitou inicio de : {inicio_data}   e o fim de : {fim_data}")



relatorio_vendas_periodo()