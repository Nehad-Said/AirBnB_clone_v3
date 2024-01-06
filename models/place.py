#!/usr/bin/python3
"""Place Module for HBNB project. Defines the place class"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

relationship_table = Table("place_amenity", Base.metadata,
                           Column('place_id', String(60),
                                  ForeignKey('places.id'),
                                  primary_key=True, nullable=False),
                           Column('amenity_id', String(60),
                                  ForeignKey('amenities.id'),
                                  primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """Represents a place for MSQL database.
    Inherits from the base and base model and links to the database.
    """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)

    user = relationship('User', back_populates='places')
    cities = relationship('City', back_populates='places')
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """Get a list of all linked Reviews."""
            from models.reviews import Review
            review_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """Get/set linked Amenities."""
            from models.amenity import Amenity
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)

    reviews = relationship("Review", back_populates="place",
                           cascade="all, delete-orphan")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False, overlaps="place_amenities")
