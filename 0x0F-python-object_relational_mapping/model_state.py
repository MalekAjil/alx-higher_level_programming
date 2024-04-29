#!/usr/bin/python3
''' a python file that contains the class definition of a State
and an instance Base = declarative_base()
'''
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    '''A class represents a state'''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
