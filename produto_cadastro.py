import os 
import sqlite3
import time 
from datetime import datetime

def produto_cadastro():
    
    # Cadastrar produto 
    # Tabela : id, code, name_chinese, name_portuguese, price
    # 
    # 

    os.system("cls")
    
    print("==========================")
    print(" >  Cadastro de produto ")
    print("==========================")

    code = input("\n > CODIGO DO PRODUTO : ")
    name_chinese = input("> NOME CHINES : ")
    name_portuguese = input("> NOME PORTUGUES : ")
    input_price = input("> PREÇO : R$ ")

    price = input_price * 100
    

produto_cadastro()