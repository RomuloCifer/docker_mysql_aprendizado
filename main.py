import pymysql
from dotenv import load_dotenv



conn = pymysql.connect(
    host='localhost',
    user='usuario',
    password='senha',
    database='my_db'
)
print("FINALMENTE")
conn.close()