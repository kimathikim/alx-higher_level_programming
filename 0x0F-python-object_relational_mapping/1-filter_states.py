#!/usr/bin/python3

import MySQLdb
from sys import argv


def state_id():
    """List all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa"""
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
        )
    except MySQLdb.Error as e:
        print(f"Unable to connect to the database: {e}")
        return

    with db.cursor() as cur:
        try:
            cur.execute("SELECT * FROM states")
            rows = cur.fetchall()
            for state in rows:
                if isinstance(state[1], str) and state[1].startswith("N"):
                    print(state)
        except MySQLdb.Error as e:
            print(f"Error executing the query: {e}")


state_id()
