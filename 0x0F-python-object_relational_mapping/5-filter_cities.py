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
        "SELECT c.name, s.name FROM cities AS c JOIN states AS s\
        where c.state_id=s.id")
    rows = cur.fetchall()
    cities = []

    for i in rows:
        if i[1] == argv[4]:
            cities.append(i[0])
    for city in cities:
        if city != cities[-1]:
            print(city, end=", ")
        else:
            print(city, end="")
    print()
    cur.close()
    db.close()


state()
