import psycopg2
from psycopg2 import connect

con = None
con = connect(dbname='TCount', user='postgres', host='localhost', password='pass')

cur = con.cursor()
cur.execute('''CREATE TABLE Tweetwordcount
       (word TEXT PRIMARY KEY     NOT NULL,
       count INT     NOT NULL);''')
con.commit()


cur.close()
con.close()
