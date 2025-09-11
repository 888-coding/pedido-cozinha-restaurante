import os
import sqlite3
import time
from datetime import datetime
# Módulos
from pedidos import PedidosMenu
from pedidos import cadastrar
from pedidos import consultar

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
        opcao = input("Opção: ")

        if opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4":
            break
    
    if opcao == "1":
        PedidosMenu()

principal()
