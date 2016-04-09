import psycopg2
from psycopg2 import connect
import sys
import getopt


conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()


if len(sys.argv) == 1:
     records = cur.fetchall()
     for rec in records:
       print "word = ", rec[0]
       print "count = ", rec[1]
     conn.commit()

else:
    uword = str(sys.arg1)
    cur.execute("SELECT word, count from Tweetwordcount" WHERE word = uword)
    print("Total number of occurences of %s : %d" %(word, count))

    conn.commit()
#
conn.close()
