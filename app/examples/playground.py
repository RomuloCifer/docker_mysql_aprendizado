import os
import pymysql
import app.config as config
from app.db import get_connection


conn = get_connection()

def reset_customers_table():
    """Apaga todos os registros de customers (para testes)."""
    yes_or_no = input("Tem certeza que deseja resetar a tabela de clientes? (s/n): ")
    if yes_or_no.lower() != 's':
        print("Operação cancelada.")
        return
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

def get_name_age():
    """Pega o nome e idade do usuário através do input."""
    name = input("Digite o nome do cliente: ")
    age = int(input("Digite a idade do cliente: "))
    return name, age

def list_customers_above_age(min_age:int):
    """Lista clientes com idade acima de min_age."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """SELECT id, name, age FROM customers
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

def delete_customer_by_id():
    """Deleta um cliente pelo ID."""
    list_customers()
    customer_id = int(input("Digite o ID do cliente a ser deletado: "))
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM customers WHERE id = %s;", (customer_id,))
            conn.commit()
            print(f"Cliente com ID {customer_id} deletado.")
def update_customer():
    """Atualiza o nome e idade de um cliente pelo ID."""
    list_customers()
    customer_id = int(input("Digite o ID do cliente a ser atualizado: "))
    name, age = get_name_age()
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE customers SET name = %s, age = %s WHERE id = %s;",
                (name, age, customer_id)
            )
            conn.commit()
            print(f"Cliente com ID {customer_id} atualizado.")
def menu():
    """Menu interativo para testes."""
    escolhas = {
        "1" : ("Listar todos os clientes", list_customers),
        "2" : ("Listar clientes acima de uma idade", lambda: list_customers_above_age(int(input("Idade mínima: ")))),
        "3" : ("Mostrar estatísticas de idade", get_age_stats),
        "4" : ("inserir um cliente", insert_customer),
        "5" : ("Atualizar um cliente pelo ID", update_customer),
        "6" : ("Deletar um cliente pelo ID", delete_customer_by_id),
        "7" : ("resetar tabela de clientes", reset_customers_table),
        "0" : ("Sair", exit)
    }
    while True:
        print("\nMenu:")
        for key, (descricao, _) in escolhas.items():
            print(f"{key} - {descricao}")
        escolha = input("Escolha uma opção: ")
        if escolha in escolhas:
            _, acao = escolhas[escolha]
            acao()
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
