#!/usr/bin/env python3
'''This module defines a class to SLP Milestone age ranges'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class AgeRange(BaseModel, Base):
    '''This class represents a SLP Milestone age range'''

    __tablename__ = 'age_ranges'
    id = Column(Integer, primary_key=True, autoincrement=True)
    age_from = Column(Integer, nullable=False, default=0)
    age_to = Column(Integer, nullable=False, default=0)

    child_milestones = relationship("ChildMilestone", back_populates="age_range", cascade="all, delete-orphan")


    def __init__(self, *args, **kwargs):
        '''Initializes an instance of the AgeRange class'''
        super().__init__(*args, **kwargs)

    def __str__(self):
        '''Returns a string representation of an instance of AgeRange'''
        return "[[{}] ({}) from {} to {}]".format(self.__class__.__name__,
                                        self.id, self.age_from, self.age_to)

    def to_dict(self):
        '''Returns a dictionary representation of an instance of AgeRange'''
        return {'id': self.id,
                'age_from': self.age_from,
                'age_to': self.age_to}
