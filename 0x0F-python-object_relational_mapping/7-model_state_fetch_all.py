#!/usr/bin/python3

from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys
from sqlalchemy import create_engine
"""Module for query"""


if __name__ == "__main__":
    """This metod is used to get all the data from state table"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State).all()

    for row in rows:
        print("{}: {}".format(row.id, row.name))
    session.close()
