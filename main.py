import os
import pymysql
import config


conn = pymysql.connect(
    host=config.MYSQL_HOST,
    user=config.MYSQL_USER,
    password=config.MYSQL_PASSWORD,
    database=config.MYSQL_DATABASE
)


# 2) Abre conexão usando as variáveis do .env


print("Conectado (:")

conn.close()