#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete-orphan')

    if os.environ.get("HBNB_TYPE_STORAGE") != "db":
        """ get cities for file storage"""
        @property
        def cities(self):
            """ getter method"""
            from models import storage
            all_cities = storage.all('City')
            return [city for city in all_cities.values()
                    if city.state_id == self.id]
