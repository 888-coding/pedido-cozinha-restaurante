import os 
from pedidos import menu_pedidos
from produtos import menu_produtos

def menu_principal():
    while True:
        os.system("cls")
        print("Sistema de 7PAM")
        print("1. Pedidos")
        print("2. Produtos")
        print("3. Relatorios")
        print("0. Sair")
        opcao = input("\n\n > Opcao: ")
        if opcao == "1":
            menu_pedidos()
        elif opcao == "2":
            menu_produtos()
        elif opcao == "3":
            print("Relatorios !")
        elif opcao == "0":
            break
        else:
            print("Opcao invalida!")
        

if __name__ == "__main__":
    menu_principal()
