import psycopg2
from psycopg2 import connect
import sys
import getopt


conn = connect(database="TCount", user="postgres", password = "pass", host="localhost")

low = str(sys.argv[1])
high = str(sys.argv[2])
cur = conn.cursor()
records = cur.fetchall()
for rec in records:
  if rec[1] <= high and rec[1] >= low:
     print (rec[0], ":", rec[1])

conn.commit()

conn.close()