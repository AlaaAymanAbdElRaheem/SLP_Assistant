#!/usr/bin/env python3
'''This module defines a class representing a child's milestones table'''
from models.base_model import BaseModel, Base
from models.age_range import AgeRange
from models.category import Category
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class ChildMilestone(BaseModel, Base):
    '''This class represents a child's milestones table'''

    __tablename__ = 'child_milestones'
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    age_range_id = Column(Integer, ForeignKey('age_ranges.id'), nullable=False)
    value = Column(String(200), nullable=False, default='')

    category = relationship("Category",
                            back_populates="child_milestones",
                            cascade="all, delete-orphan",
                            single_parent=True)
    age_range = relationship("AgeRange",
                             back_populates="child_milestones",
                             cascade="all, delete-orphan",
                             single_parent=True)

    def __init__(self, *args, **kwargs):
        '''Initializes an instance of the ChildMilestone class'''
        super().__init__(*args, **kwargs)

    def __str__(self):
        '''Returns a string representation of an instance of ChildMilestone'''
        return "[[{}] ({}) {} from {} to {}: {}]".format(
            self.__class__.__name__,
            self.id,
            self.category.name,
            self.age_range.age_from,
            self.age_range.age_to,
            self.value
        )

    def to_dict(self):
        '''Returns a dictionary representation of ChildMilestone'''
        return {
            'id': self.child_milestone_id,
            'type': self.category.name,
            'age_from': self.age_range.age_from,
            'age_to': self.age_range.age_to,
            'value': self.value
        }
