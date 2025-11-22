import os 
from rich.console import Console
from rich.table import Table
import msvcrt

from pedidos import menu_pedidos
from produtos import menu_produtos
from relatorios import menu_relatorios

def menu_principal():
    while True:
        os.system("cls")
        console = Console()
        tabela = Table()
        tabela.add_column("SISTEMA DE 7PAM", style="cyan", no_wrap=True)
        tabela.add_row("1. Pedidos")
        tabela.add_row("2. Produtos")
        tabela.add_row("3. Relatorios")
        tabela.add_row("0. Sair")
        console.print(tabela)
        
        #opcao = input("\n\n > Opcao: ")
        print("\n\n > Opcao: ", end="", flush=True)
        opcao = ""
        
        while len(opcao) < 1 :
            char = msvcrt.getwch()
            print(char, end="", flush=True)
            opcao += char

        if opcao == "1":
            menu_pedidos()
        elif opcao == "2":
            menu_produtos()
        elif opcao == "3":
            menu_relatorios()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida!")
        

if __name__ == "__main__":
    menu_principal()
