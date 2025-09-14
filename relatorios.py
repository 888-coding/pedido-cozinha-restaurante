import os


def menu_relatorios():
    while True:
        os.system("cls")
        print("===============================")
        print(" > Relatorios ")
        print("===============================")
        print("1. Relatorio de vendas por dia")
        print("2. Relatorio de vendas por mês")
        print("3. Relatorio de vendas por periodo")
        print("0. Sair")

        print("===============================")
        opcao = input(" > Digite a opcao : ")
        if opcao == "0":
            break
        elif opcao == "1":
            pass
