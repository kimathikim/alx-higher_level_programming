#!/usr/bin/python3
"""Module for query"""
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City
import sys
from sqlalchemy import create_engine
if __name__ == "__main__":
    """
    that prints all City objects from the database hbtn_0e_14_usa
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for city, state in session.query(City, State).\
            filter(City.state_id == State.id).\
            order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name)
              )
    session.close()
