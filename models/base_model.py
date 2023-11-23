#!/usr/bin/env python3
''' This module contains the BaseModel class
    This class is the base class for all other classes in this project
'''
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models


Base = declarative_base()

class BaseModel:
    '''This class defines the BaseModel class for all other classes'''

    def __init__(self, *args, **kwargs):
        '''This method initializes an instance of the BaseModel class'''
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

    def save(self):
        '''This method saves the instance to the database'''
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        '''This method deletes the instance from the database'''
        models.storage.delete(self)
