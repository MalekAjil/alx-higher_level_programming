#!/usr/bin/python3
''' a python file that contains the class definition of a City
and an instance Base = declarative_base()
'''
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    '''A class represents a City'''
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, foreign_key('states.id'))
