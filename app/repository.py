from app.db import get_connection
from typing import List, Tuple, Optional

def criar_tabela_clientes_se_nao_existir() -> None:
    """Cria a tabela de clientes se ela ainda não existir."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS customers (
                id INT NOT NULL AUTO_INCREMENT,
                name VARCHAR(50) NOT NULL,
                age INT NOT NULL,
                PRIMARY KEY(id))"""
            cursor.execute(sql,)
            conn.commit()
        
def resetar_tabela_clientes() -> None:
    """Reseta a tabela de clientes removendo e recriando ela."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            sql_drop = """DROP TABLE IF EXISTS customers"""
            cursor.execute(sql_drop,)
            
            sql_create = """CREATE TABLE customers (
                id INT NOT NULL AUTO_INCREMENT,
                name VARCHAR(50) NOT NULL,
                age INT NOT NULL,
                PRIMARY KEY(id))"""
            cursor.execute(sql_create,)
            conn.commit()

def inserir_cliente(nome: str, idade: int) -> None:
    """Insere um novo cliente na tabela de clientes."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            sql = """INSERT INTO customers (name, age) VALUES (%s, %s)"""
            cursor.execute(sql, (nome, idade))
            conn.commit()

def listar_clientes() -> List[Tuple[int, str, int]]:
    """Lista todos os clientes da tabela."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            sql = """SELECT * FROM customers"""
            cursor.execute(sql,)
            print("Buscando todos os clientes...")
            return cursor.fetchall() 


def listar_clientes_acima_idade(idade_minima):
    """Lista clientes acima de certa idade."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            sql = """SELECT * FROM customers WHERE age > %s"""
            cursor.execute(sql, (idade_minima,))
            return cursor.fetchall()

def informacoes_idade():
    """Retorna a contagem e média de idade dos clientes."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            sql = """SELECT COUNT(*), AVG(age) FROM customers"""
            cursor.execute(sql,)
            return cursor.fetchall()

def atualizar_idade_cliente(cliente_id: int, nova_idade: int) -> None:
    """Atualiza a idade de um cliente pelo ID."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            sql = """UPDATE customers SET age = %s WHERE id = %s"""
            cursor.execute(sql, (nova_idade, cliente_id))
            conn.commit()

def atualizar_nome_cliente(cliente_id: int, novo_nome: str) -> None:
    """Atualiza o nome de um cliente pelo ID."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            sql = """UPDATE customers SET name = %s WHERE id = %s"""
            cursor.execute(sql, (novo_nome, cliente_id))
            conn.commit()

def deletar_cliente_por_id(cliente_id: int) -> None:
    """Deleta um cliente pelo ID."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            sql = """DELETE FROM customers WHERE id = %s"""
            cursor.execute(sql, (cliente_id,))
            conn.commit()