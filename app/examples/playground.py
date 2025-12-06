import os
import pymysql
import app.config as config
from db import get_connection


conn = get_connection()

with conn:
    with conn.cursor() as cursor:
        cursor.execute("""TRUNCATE TABLE customers""")
        sql = """
            INSERT INTO customers
            (name, age) VALUES ('jorge', 20)""" # risco de injection

        cursor.execute(sql)

    
    with conn.cursor() as cursor2:
        sql = """ INSERT INTO customers
        (name, age) VALUES (%s, %s)""" #placeholders

        cursor2.execute(sql, ('teste2', 22)) 
    
    with conn.cursor() as cursor3:
        sql = """ INSERT INTO customers
        (name, age) VALUES (%(teste_nome)s, %(teste_idade)s)"""
        
        data = {
            'teste_idade': 77,
            'teste_nome': 'Jubiscleiton'
        }
        cursor3.execute(sql, data)

        sql = """SELECT * FROM customers"""
        cursor3.execute(sql)
        print(cursor3.fetchone())
        print(cursor3.fetchall())

