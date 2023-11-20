#!/usr/bin/python3
"""Module for query"""
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys
from sqlalchemy import create_engine
if __name__ == "__main__":
    """
    delete all atrribute having 'a'
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    update_state = session.query(State).filter(State.name.ilike('%a%')).all()
    for row in update_state:
        session.delete(row)
    session.commit()
    session.close()
