#!/usr/bin/python3
"""a script that lists all State objects,
and corresponding City objects,
contained in the database hbtn_0e_101_usa
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
    for instance in session.query(State).order_by(State.id):
        print(f"{instance.id}: {instance.name}")
        for city in instance.cities:
            print(f"\t{city.id}: {city.name}")
