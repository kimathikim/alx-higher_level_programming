#!/usr/bin/python3

import MySQLdb
from sys import argv


def select_s():
    """conect and query data from a database"""

    user = argv[1]
    pas = argv[2]
    database = argv[3]
    db = MySQLdb.connect(
        host="localhost", port=3306, user=f"{user}", passwd=f"{pas}",
        db=f"{database}")
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for i in rows:
        print(i)
    cur.close()
    db.close()


select_s()
