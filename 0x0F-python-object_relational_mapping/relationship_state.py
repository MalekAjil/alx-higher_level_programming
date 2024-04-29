#!/usr/bin/python3
''' a python file that contains the class definition of a State
and an instance Base = declarative_base()
'''
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from relationship_city import City, Base


class State(Base):
    '''A class represents a state'''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))

    cities = relationship("City")

    City.state = relationship("State", back_populates="cities")
