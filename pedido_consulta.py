import os
import sqlite3
import time 
from datetime import datetime

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
    print("2. Outro periodo")

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
            print("Nao foi encontrado nada")
        else:
            for row in rows:
               print(f"Número do pedido : {row[0]}") 
consultar()