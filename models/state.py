#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base, relationship

base = declarative_base()
class State(BaseModel, Base):
    """ State class """
    __tablename__ = "States"
    cities = relationship("City", back_populates="state")
