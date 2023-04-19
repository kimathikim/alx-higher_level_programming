#!/usr/bin/python3

import MySQLdb
from sys import argv


def state():
    """ lists all cities from the database hbtn_0e_4_usa"""

    try:
        db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1], passwd=argv[2],
            db=argv[3])
    except Exception:
        print("unable to connect to the database")
        return 0
    cur = db.cursor()
    cur.execute(
        "SELECT c.id, c.name, s.name FROM cities AS c JOIN states AS s\
        where c.state_id=s.id")
    rows = cur.fetchall()

    for i in rows:
        print(i)
    cur.close()
    db.close()


state()
