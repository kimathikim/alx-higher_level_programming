#!/usr/bin/python3

import MySQLdb
from sys import argv


def select_s():
    """conect and query data from a database"""

    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2],
        db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for i in rows:
        print(i)
    cur.close()
    db.close()


select_s()
