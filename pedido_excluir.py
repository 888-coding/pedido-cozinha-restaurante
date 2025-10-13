import os
import sqlite3
from rich.console import Console
from rich.table import Table
import time
import getpass

def pedido_delete():
    while True:
        os.system("cls") 
        print("=====================================")
        print(" > Pedido - Apagar")
        print("=====================================")
        print("\n\nAtencao: Este nao pode ser deletado")
        print("Precisa ter cuidado")

        senha = 89980

        opcao = input("> Tem certeza que quer continuar ? (S/N) : ").upper()

        if opcao == "N":
            break
        elif opcao == "S":
            # Primeiro digite a senha 
            input_senha = getpass.getpass("> Senha para excluir : ")

            print(input_senha)
            time.sleep(1)

            if int(input_senha) == senha:
                print("Senha correta")
                time.sleep(1)
            else: 
                print("Senha incorreta...")
                time.sleep(0.8)
                print("Voltando ... ")
                time.sleep(1.5)
                break
        else:
            print("opcao invalida ...")
            time.sleep(0.6)



pedido_delete()