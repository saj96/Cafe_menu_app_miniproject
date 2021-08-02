import pymysql
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
    host,
    user,
    password,
    database
)

# A cursor is an object that represents a DB cursor,
# which is used to manage the context of a fetch operation.
cursor = connection.cursor()
# cursor.execute('SELECT * FROM products')
# rows = cursor.fetchall()
# column_names = [i[0] for i in cursor.description]
# print(column_names)
# print(rows)
# for row in rows:
#     print(row)
    
index = input('Enter id:')
cursor.execute("SELECT product_id, COUNT(*) FROM products WHERE product_id = %s", (index))
msg = cursor.fetchone()
print(msg[0])
if not msg[0]:
    print(msg)
#connection.commit()
#cursor.close()
# Closes the connection to the DB, make sure you ALWAYS do this
#connection.close()
