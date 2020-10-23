# sqlite
# connecting, creating cursor
# creating db, creating table
# inserting values

import sqlite3

con = sqlite3.connect('movies.db')
cur = con.cursor()

query = """INSERT into actors VALUES
        (10, "Keanu Reaves", "lebanon", 34590)
        """

cur.execute(query)    
con.commit()

con.close()
