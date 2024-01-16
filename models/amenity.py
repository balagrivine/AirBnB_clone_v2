#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
#rom models.place import place_amenity


class Amenity(BaseModel):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    #place = relationship('Place', back_populates='amenities')
