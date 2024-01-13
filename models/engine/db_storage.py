#!/usr/bin/python3



"""
creating a new engine

"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session
from models.state import State
#from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.base_model import Base
from models.place import Place
import os
from models.city import City

class_dict = {
    'User': User,
    'State': State,
    'Review': Review,
    'Place': Place,
    'Amenity': Amenity,
    'City': City
        }

class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        """creates the driver engine for our database"""
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, passwd, host, db), pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session (self.__session) all objects depending of the class name (argument cls)
        if cls=None, query all types of objects (User, State, City, Amenity, Place and Review)
        this method must return a dictionary: (like FileStorage)
        key = <class-name>.<object-id>
        value = object

        """

        objects = {}
        if cls:
            for obj in self.__session.query(cls):
                objects[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for cls in class_dict.values():
                for obj in self.__session.query(cls):
                    objects[obj.__class__.__name__ + '.' + obj.id] = obj
        return objects

    def new(self, obj):
        """
        add the object to the current database session (self.__session)

        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session (self.__session)

        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database (feature of SQLAlchemy) (WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine))
        create the current database session (self.__session) from the engine (self.__engine) by using a sessionmaker - the option expire_on_commit must be set to False ; and scoped_session - to make sure your Session is thread-safe

        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)
