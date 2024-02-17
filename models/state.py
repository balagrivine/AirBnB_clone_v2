#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base, relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates='state')

    @property
    def class(self):
        """public getter method cities to return the list of City objects from storage linked to the current State
        """

        form models import storage
        related_cities = []
        cities = storage..all(city)
        for city in cities.values():
            if city.state_id == self.id:
                related_cities.appent(city)
        return related_cities
