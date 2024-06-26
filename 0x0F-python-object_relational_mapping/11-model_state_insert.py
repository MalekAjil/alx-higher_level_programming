#!/usr/bin/python3
"""a script that adds the State object “Louisiana” to
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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(State(name='Louisiana'))
    session.commit()
    state = session.query(State).filter_by(name='Louisiana').first()
    print(state.id)
