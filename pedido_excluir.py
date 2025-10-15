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
        print("\n\nAtencao: Este ação nao pode retornar . ")
        print("Precisa ter cuidado")

        senha = 89980

        opcao = input("> Tem certeza que quer continuar ? (S/N) : ").upper()

        if opcao == "N":
            break
        elif opcao == "S":
            # Primeiro digite a senha 
            input_senha = getpass.getpass("> Senha para excluir : ")

            time.sleep(1)

            if int(input_senha) == senha:
                print("Senha correta")
                time.sleep(1)
                os.system("cls")
                
                print("==================================")
                print(" > Excluir pedido")
                print("==================================")
                input_numero_pedido = int(input("Digite o numero do pedido : "))
                
                con = sqlite3.connect("database.db")
                cur = con.cursor()
                sql = "SELECT * FROM orders WHERE id = ?"
                cur.execute(sql, (input_numero_pedido,) )
                row = cur.fetchone()

                if row:
                    print("O numero de pedido existe. ")
                    opcao = input(f"Voce realmente quer excluir o pedido : {input_numero_pedido} ? (S/N) ").upper()
                    
                    if opcao == "S":
                        print(row)
                        
                        sql = "DELETE FROM orders WHERE id = ?"
                        cur.execute(sql, (input_numero_pedido,) )
                        con.commit()

                        sql = "DELETE FROM order_items WHERE order_id = ?"
                        cur.execute(sql, (input_numero_pedido,) )
                        con.commit()

                        print("Excluido o pedido.")
                        input("\nDigite algo para continuar ...")

                    #aqui
                else:
                    print("Erro: Nao foi encontrado o pedido. ")
                    time.sleep(2)

            else: 
                print("Senha incorreta...")
                time.sleep(0.8)
                print("Voltando ... ")
                time.sleep(1.5)
                break
        else:
            print("opcao invalida ...")
            time.sleep(0.8)



pedido_delete()