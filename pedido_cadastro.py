import sqlite3
import os 
import time 
from datetime import datetime
from datetime import date

# Fazendo o pedido desde zero 

os.system("cls")

print("======================")
print("> Cadastro de pedido  ")
print("======================")
print("\n")
mesa = input("> Numero de mesa : ")

time.sleep(0.5)

os.system("cls")
print("======================")
print(f"> Mesa : {mesa}")
print("======================")

print("\nPedido - Digite o codigo da comida: ")


lista_comidas = [] 
lista_precos = []
while True:
    input_comida = input("> Numero da comida: ").upper()

    time.sleep(0.3)
    
    # Sair do adicionar comida
    if input_comida == "0":
        break
    # Acrescentar comida
    else:
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        sql = "SELECT id, name_chinese, name_portuguese, price FROM products WHERE id = ?"
        cur.execute(sql, (input_comida,))
        row = cur.fetchone()
        con.close()
        if row is None:
            # Se não encontrar o codigo, nao faz nada, somente mostra aviso que nao encontrou
            print("Não encontrado!")
        else:
            # Se encontrar o codigo, adiciona ele na lista de comidas de pedido
            lista_comidas.append(row[0])
            lista_precos.append(row[3])
            print(f"> {row[1]} - {row[2]}")


# imprimir lista de comida 
print(f"Lista dos codigos dos produtos : {lista_comidas}") 
print(f"Precos unitarios :{lista_precos}")

total_value = 0 
for item in lista_precos:
    total_value += int(item)
print(f"Valor total : {total_value}")
# achar o numero de pedido para adicionar. 
con = sqlite3.connect("database.db")
cur = con.cursor()
sql = "SELECT id FROM orders ORDER BY id DESC LIMIT 1"
cur.execute(sql, () )
row = cur.fetchone()
con.close()
print("================================================")
if not row:
    numero_pedido_novo = 1
    print("Não tinha cadastro de pedido")
else:
    print(f"Ultimo numero de pedido é: {row[0]}") 
    numero_pedido_novo = int(row[0]) + 1 

print("===============================================")
print(f"novo numero de pedido é : {numero_pedido_novo}")
print("===============================================")
# mesa
print(f"Mesa : {mesa}")
print("===============================================")
# data do pedido 
data_pedido = datetime.today().strftime("%Y-%m-%d")
hora_pedido = datetime.today().strftime("%H:%M:%S")
print(f"Data : {data_pedido}")
print(f"Horas: {hora_pedido}")
print("===============================================")

# Cadastrar no banco de dados 
# Tabela orders 
# table_number(mesa), data_pedido(data_pedido), hora_pedido(hora_pedido), total_value(total_value)
# Tabela order_items
# order_id(numero_pedido_novo), product_id, product_qty, product_price
# 
# 

