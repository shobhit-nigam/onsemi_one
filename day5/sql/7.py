# sqlite
# connecting, creating cursor
# creating db, creating table
# inserting values as a list

import sqlite3

lista = [11, "michelle yeoh", "malaysia", 23400]

con = sqlite3.connect('movies.db')
cur = con.cursor()

query = """INSERT into actors(id, name, country, earning) values (?, ?, ?, ?)"""

cur.execute(query, lista)    
con.commit()

con.close()
