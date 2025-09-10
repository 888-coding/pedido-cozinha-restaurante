import os
import sqlite3
import time
from datetime import datetime

def principal():
    os.system("cls")
    print("====================================")
    print(" > Sistema de Pedidos ")
    print("====================================")

    print("1. Pediddos")
    print("2. Produtos")
    print("3. Relatórios")
    print("4. Sair\n\n")

    while True:
        opcao = input("Opção : ")
        if opcao == "1" or opcao == "2" or opcao =="3" or opcao == "4":
            break
    
    if opcao == "1":
        pedidos()
    elif opcao == "2":
        produtos()
    elif opcao == "3":
        relatorios()
    else:
        print("\n\n=================================")
        print(" > Obrigado !! ")
        print("=================================")
        time.sleep(3)
        os.system("cls")
        exit()


principal()