import os 
import sqlite3
import time

def produtos_consultar():
    os.system("cls")
    print("=================================")
    print(" > Consultar todos os produtos")
    print("=================================")

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    sql = "SELECT id, code, name_chinese, name_portuguese, price FROM products ORDER BY code ASC"
    cur.execute(sql, ())
    rows = cur.fetchall()
    cur.close()
    con.close()

    for row in rows:
        print(f"Codigo : {row[1]} - {row[2]} {row[3]} Preço: {float(row[4])/100:.2f}")

    print("\n\n Fim de linha .")
    input("Tecle para continuar ..")
    time.sleep(1.5)

produtos_consultar()