import os 

def menu_principal():
    while True:
        os.system("cls")
        print("Sistema de 7PAM")
        print("1. Pedidos")
        print("2. Produtos")
        print("3. Relatorios")
        print("0. Sair")

if __name__ == "__main__":
    menu_principal()
