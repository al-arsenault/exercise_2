from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2
from psycopg2 import connect


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        self.redis = StrictRedis()
        conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")

#Create a Table
#The first step is to create a cursor.

        cur = conn.cursor()
        cur.execute('''CREATE TABLE Tweetwordcount
           (word TEXT PRIMARY KEY     NOT NULL,
           count INT     NOT NULL);''')
        conn.commit()
        conn.close()

    def process(self, tup):

 uword = tup.values[0]
        # Increment the local count
        self.counts[uword] += 1
        self.emit([uword, self.counts[uword]])

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount
        # Table name: Tweetwordcount
        # you need to create both the database and the table in advance.

        # If self.counts[uword] = 1 this is a new word that must be inserted
        # into the table
        if self.counts[uword] == 1:
            cur.execute("INSERT INTO Tweetwordcount (word, count) VALUES (uword, "1")");
            conn.commit ()

        #Else update the table by incrementing the count by 1
        else:
             cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s", (self.counts[uword], uword))
             conn.commit()


        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[uword]))
