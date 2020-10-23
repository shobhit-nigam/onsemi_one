# sqlite
# connecting, creating cursor
# getting the list of tables
# close the connection

import sqlite3

con = sqlite3.connect('chinook.db')
cur = con.cursor()

query = 'SELECT name from sqlite_master where type="table"'

cur.execute(query)
lista = cur.fetchall()

print(lista)

con.close()
