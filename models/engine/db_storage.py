#!/usr/bin/python3
""" New engine DBStorage """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class DBStorage:
    """ Database storage engine """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializes database storage engine """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Queries on current database session (self.__session) """
        obj_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
        else:
            cls_list = [User, State, City, Amenity, Place, Review]
            objs = []
            for clss in cls_list:
                objs += self.__session.query(clss).all()
        for obj in objs:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """ Adds the object to current database session (self.__session) """
        if obj:
            self.__session.add(obj)

    def save(self):
        """ Commits all changes of the current database session (self.__session) """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes obj from current database session (self.__session) """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables and the current database session (self.__session) """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)()
