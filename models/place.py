#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
#from models import storage

place_amenity = Table('place_amenity', Base.metadata, 
        Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False), 
        Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))
class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    user = relationship('User', back_populates='places')
    cities = relationship('City', back_populates='places')
    amenity_ids = []

    env = getenv("HBNB_TYPE_STORAGE")

    if env == "db":
        reviews = relationship('Review', back_populates='place')

        amenities = relationship('Amenity', back_populates='place_amenities', secondary=place_amenity, viewonly=False)

    else:
        @property
        def review(self):
            """
            Returns a list of reies instances
            """
            from models import storage
            review_inst = storage.all('Review').values()
            return [review for review in review_inst if review.place_id == self.id]

        @property
        def amenities(self):
            """
            Getter attribute amenities that returns the list of Amenity instances based on the attribute amenity_ids that contains all Amenity.id linked to the Place
            """
            from models import storage
            review_instances = storage.all('Review').values()
            return [review for review in review_instances if review.place_id == self.id]
        @amenities.setter
        def amenities(self, obj):
            """Setter attribute amenities that handles append method for adding an Amenity.id to the attribute amenity_ids. This method should accept only Amenity object, otherwise, do nothing.
            """
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)

