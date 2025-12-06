import os
import pymysql
import app.config as config
from db import get_connection

conn = get_connection()

with conn:
    with conn.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS customers (
            id INT NOT NULL AUTO_INCREMENT, 
            name VARCHAR(50) NOT NULL, 
            age INT NOT NULL, 
            PRIMARY KEY(id))"""
        )
        conn.commit()
        