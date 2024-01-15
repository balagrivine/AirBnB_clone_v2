#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    place_amenity = relationship('Place', secondary='place_amenities')
