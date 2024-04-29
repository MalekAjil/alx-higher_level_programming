#!/usr/bin/python3
''' a python file that contains the class definition of a City
and an instance Base = declarative_base()
'''
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from model_state import State, Base


class City(Base):
    '''A class represents a City'''
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship("State", back_populates="cities")

    State.cities = relationship("City")
