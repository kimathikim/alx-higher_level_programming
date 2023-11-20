#!/usr/bin/python3
"""script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City
import sys

if __name__ == "__main__":
    """
    Script to create the State "California" with the City "San Francisco"
    in the hbtn_0e_100_usa database
    """

    # Establish the database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)

    # Create the necessary tables if they don't exist
    Base.metadata.create_all(engine)
    session = sessionmaker()(bind=engine)
    new_state = State(name="California", cities=[City(name="San Francisco")])
    session.add(new_state)
    session.commit()
    session.close()
