# sqlite
# connecting, creating cursor
# creating db, creating table

import sqlite3

con = sqlite3.connect('movies.db')
cur = con.cursor()

query = """CREATE TABLE actors
        (id integer PRIMARY KEY, name varchar, country varchar, earning real)
        """

cur.execute(query)    

con.close()
