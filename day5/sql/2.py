# sqlite
# connecting, creating cursor
# getting a table (employees)
# close the connection

import sqlite3

con = sqlite3.connect('chinook.db')
cur = con.cursor()

query = 'SELECT * FROM employees'

cur.execute(query)

lista = cur.fetchall()

for record in lista:
    print(record)
    print("---------")

con.close()
