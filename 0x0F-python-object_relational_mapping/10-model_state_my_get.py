#!/usr/bin/python3
"""Module for query"""
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys
from sqlalchemy import create_engine
if __name__ == "__main__":
    """
    prints the State object with the name
    passed as argument from the database hbtn_0e_6_usa
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State).all()

    value = 0
    for row in rows:
        if row.name == sys.argv[4]:
            value = row.id
    if value != 0:
        print(value)
    else:
        print("Not found")
