# sqlite
# connecting, creating cursor
# creating db, creating table
# inserting values as a list

import sqlite3

lista = [[12, "salma hayek", "mexico", 23400],
         [13, "mel gibson" , "america", 40890],
         [14, "hugh jackman", "australia", 34000],
         [15, "emma watson", "france", 25000],
         [16, "jackie chan", "hong kong", 28000],
         [17, "dave bautista", "filipino", 22000]]

con = sqlite3.connect('movies.db')
cur = con.cursor()

query = """UPDATE actors SET name = "Batista" where id = 17"""

cur.execute(query)

con.commit()

con.close()
