#!/usr/bin/python3
"""a script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
import sqlalchemy
from relationship_state import State
from relationship_city import City, Base

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(State(name='California'))
    session.add(City(name='San Francisco', state_id=1))
    session.commit()
