#!/usr/bin/env python3
'''This module defines a class to SLP Milestone categories'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Category(BaseModel, Base):
    '''This class represents a SLP Milestone category'''

    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, default='')

    child_milestones = relationship("ChildMilestone", back_populates="category", cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        '''Initializes an instance of the Category class'''
        super().__init__(*args, **kwargs)

    def __str__(self):
        '''Returns a string representation of an instance of Category'''
        return "[[{}] ({}) {}]".format(self.__class__.__name__,
                                    self.id, self.name)

    def to_dict(self):
        '''Returns a dictionary representation of an instance of Category'''
        return {'id': self.id,
                'name': self.name}
