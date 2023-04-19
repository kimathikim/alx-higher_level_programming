#!/usr/bin/python3
"""Module for query"""
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys
from sqlalchemy import create_engine
if __name__ == "__main__":
    """
    adds the State object “Louisiana” to the database hbtn_0e_6_usa
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    update_state = session.query(State).all()
    for row in update_state:
        if row.id == 2:
            row.name = 'New Mexico'
    session.commit()
    session.close()
