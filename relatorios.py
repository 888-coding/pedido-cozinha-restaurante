import os
import sqlite3
from datetime import date
import time

def menu_relatorios():
    while True:
        os.system("cls")
        print("===============================")
        print(" > Relatorios ")
        print("===============================")
        print("1. Relatorio de vendas por dia")
        print("2. Relatorio de vendas por mês")
        print("3. Relatorio de vendas por periodo")
        print("0. Voltar")

        print("===============================")
        opcao = input(" > Digite a opcao : ")
        if opcao == "0":
            break
        elif opcao == "1":
            relatorio_vendas_dia()
        elif opcao == "2":
            relatorio_vendas_mes()


def relatorio_vendas_dia():
    os.system("cls")
    print("=================================")
    print(" > Relatório vendas por dia ")
    print("=================================")

    data = input("\n\n > Digite a data (aaaa-mm-dd): ")

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    sql = "SELECT id, order_date, order_time, total_value FROM orders WHERE order_date = ? ORDER BY id ASC"
    cur.execute(sql, (data,))
    rows = cur.fetchall()
    cur.close()
    con.close()
    if rows:
        valor_do_dia = 0
        for row in rows:
            n = len(row)
            print(f"{row[0]} - Horas: {row[2]} - Valor: R$ {float(row[3]) / 100:.2f}")
            valor_do_dia += row[3]
        print(f"\n\nValor vendido do dia : {float(valor_do_dia) / 100:.2f}")
        input("\nDigite algo para continuar...")
        time.sleep(0.4)
    else:
        os.system("cls")
        print("Não encontrado nenhum pedido na data.")
        input("Digite algo para continuar ...")

# Relatorio vendas mes 
def relatorio_vendas_mes():
    os.system("cls")
    print("==================================")
    print(" > Relatorio vendas por mes ")
    print("==================================")

    # [Entradas]
    ano = input("\n\n> Digite o ano : ")
    mes = input("> Digite o mes : ")

    # [Conexão]
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    sql =   """SELECT id FROM orders 
                WHERE strftime('%m', order_date) = ?
                AND strftime('%Y', order_date) = ?
            """
    cur.execute(sql)
    rows = cur.fetchall()
    cur.close()
    con.close()

    # [Mostrar resultados]
    if rows:
        for row in rows:
            print(row[0])
            input("digite para continuar")
    else:
        os.system("cls")
        print("Não foi encontrado nada neste periodo")
        time.sleep(2)

def relatorio_venda_por_mercadorias_mensal():
    os.system("cls")
    print("======================================")
    print(" > Relatorio Vendas por mercadorias")
    print("======================================")

    print("\nPeriodo Mensal ")
    ano = input("Digite ano: ")
    mes = input("Digite o mes: ")
    print("\n\n")
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    sql = """
            SELECT DISTINCT oi.product_id FROM orders AS o
            JOIN order_items AS oi 
            ON o.id = oi.order_id
            WHERE strftime('%m', order_date) = ? 
            AND strftime('%Y', order_date) = ?
            """
    cur.execute(sql,(mes.zfill(2),ano,))
    rows = cur.fetchall()

    if rows:
        for row in rows:
            # os id de produtos
            id_product = row[0]
            sql = """
                    SELECT sum(product_qty) AS soma FROM order_items AS oi
                    JOIN orders AS o ON  oi.order_id = o.id
                    WHERE oi.product_id = ? AND strftime('%m', o.order_date) = ? AND strftime('%Y', o.order_date) = ?
                    """
            cur.execute(sql, (id_product, mes.zfill(2), ano,))
            rows = cur.fetchone()
            print("Quantidade por produto")
            sql = ("SELECT code, name_chinese, name_portuguese FROM products WHERE id = ?")
            cur.execute(sql, (id_product,))
            row = cur.fetchone()

            print(f"> Codigo do produto : {row[0]}. Nome: {row[1]} - {row[2]}  Quantidade : {rows[0]}\n")
    else:
        print("Não foi encontrado nenhum registro.")

    cur.close()
    con.close()


