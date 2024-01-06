#!/usr/bin/python3
""" Database Storage Engine"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """ This is a databse storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializing the connections"""
        user = os.environ.get('HBNB_MYSQL_USER')
        pswd = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        db = os.environ.get('HBNB_MYSQL_DB')
        envi = os.environ.get('HBNB_ENV')
        path = f'mysql+mysqldb://{user}:{pswd}@{host}/{db}'
        self.__engine = create_engine(path, pool_pre_ping=True)
        if envi == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query all objects depending on class name"""
        classes = [User, State, City, Amenity, Place, Review]
        if cls:
            classes = [cls] if cls not in classes else [cls]

        results = {}
        for c in classes:
            query_res = self.__session.query(c).all()
            for obj in query_res:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                results[key] = obj

        return results

    def new(self, obj):
        """ Adds a new obj to the db"""
        self.__session.add(obj)

    def save(self):
        """ Saves the object to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes from the database"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """ Creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        self.Session = scoped_session(sessionmaker(bind=self.__engine))
        self.__session = self.Session()

    def close(self):
        """ This method removes items from db"""
        self.Session.remove()
        self.reload()
