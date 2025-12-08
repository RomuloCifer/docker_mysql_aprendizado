import os
import pymysql
import app.config as config
from app.db import get_connection


conn = get_connection()

def reset_customers_table():
    """Apaga todos os registros de customers (para testes)."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE customers;")
        conn.commit()

def insert_customer(name: str, age: int):
    """Insere um cliente e retorna o ID gerado."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            sql = "INSERT INTO customers (name, age) VALUES (%s, %s);"
            cursor.execute(sql, (name, age))
            conn.commit()
            return cursor.lastrowid
        
def list_customers():
    """Lista todos os clientes."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT id, name, age FROM customers ORDER BY id;"
            )
            for row in cursor.fetchall():
                print(row)

def list_customers_above_age(min_age:int):
    """Lista clientes com idade acima de min_age."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                f"""SELECT id, name, age FROM customers
                           WHERE age > %s ORDER BY age DESC;""", (min_age,))
            
            for row in cursor.fetchall():
                print(row)

def get_age_stats():
    """Mostra quantidade de clientes e média de idade."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*), AVG(age) FROM customers;")
            total, avg_age = cursor.fetchone()
            print(f"Total de clientes: {total}")
            print(f"Média de idade: {avg_age:.2f}" if avg_age is not None else "Sem clientes ainda.")


if __name__ == "__main__":
    reset_customers_table()
    c1 = insert_customer("Alicinha", 22)
    c2 = insert_customer("Brunilde", 35)
    c3 = insert_customer("Carla", 29)
    c4 = insert_customer("Jubete", 70)
    c5 = insert_customer("Claudinho", 38)
    c5 = insert_customer("Enzo", 8)
    c6 = insert_customer("Sofia", 17)

    print("\n--- TODOS OS CLIENTES ---")
    list_customers()
    above_input = int(input("Qual idade mínima para mostrar os cliente? \n"))
    print(f"\n--- CLIENTES COM MAIS DE {above_input} ANOS ---")
    list_customers_above_age(above_input)

    print("\n--- ESTATÍSTICAS DE IDADE ---")
    get_age_stats()
