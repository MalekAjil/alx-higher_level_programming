#!/usr/bin/python3
"""a script that prints the first State object from
the database hbtn_0e_6_usa
"""
import sys
import sqlalchemy
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    state_name = sys.argv[4]
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).filter(State.name == state_name).first()
    if instance is None:
        print("Not<F12> found")
    else:
        print(instance.id)
