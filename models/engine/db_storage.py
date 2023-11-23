#!/usr/bin/env python3
'''This module defines a class to manage db storage for SLP assistant'''

import models
from os import getenv
from models.base_model import BaseModel, Base
from models.child_milestone import ChildMilestone
from models.age_range import AgeRange
from models.category import Category
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


classes = {'ChildMilestone': ChildMilestone, 'AgeRange': AgeRange, 'Category': Category}


class DBStorage:
    '''This class manages storage of SLP assistant data in a database'''
    __engine = None
    __session = None

    def __init__(self):
        '''Initializes an instance of DBStorage'''
        SLP_MYSQL_USER = getenv('SLP_MYSQL_USER')
        SLP_MYSQL_PWD = getenv('SLP_MYSQL_PWD')
        SLP_MYSQL_HOST = getenv('SLP_MYSQL_HOST')
        SLP_MYSQL_DB = getenv('SLP_MYSQL_DB')
        SLP_ENV = getenv('SLP_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(SLP_MYSQL_USER,
                                             SLP_MYSQL_PWD,
                                             SLP_MYSQL_HOST,
                                             SLP_MYSQL_DB))
        # drop all data to ensure a clean state before each test
        if SLP_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def new(self, obj):
        '''Adds a new object to the database'''
        self.__session.add(obj)

    def save(self):
        '''Commits all changes to the database'''
        self.__session.commit()

    def delete(self, obj=None):
        '''Deletes an object from the database'''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        '''Reloads all tables from the database'''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def all(self, cls=None):
        '''Returns a dictionary of all objects in the database'''
        if cls:
            objects = self.__session.query(classes[cls]).all()
        else:
            objects = []
            for cls in classes:
                objects += self.__session.query(classes[cls]).all()
        return {'{}.{}'.format(type(obj).__name__, obj.id):
                obj for obj in objects}

    def close(self):
        '''Close the session'''
        self.__session.remove()
