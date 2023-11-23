#!/usr/bin/env python3
'''This module defines a class representing a child's milestones table'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer


class ChildMilestones(BaseModel, Base):
    '''This class represents a child's milestones table'''

    __tablename__ = 'child_milestones'
    id = Column(Integer, primary_key=True, autoincrement=True, default=0)
    type = Column(String(50), nullable=False, default='')
    age_from = Column(Integer, nullable=False)
    age_to = Column(Integer, nullable=False)
    value = Column(String(200), nullable=False, default='')

    def __init__(self, *args, **kwargs):
        '''Initializes an instance of the ChildMilestones class'''
        super().__init__(*args, **kwargs)

    def __str__(self):
        '''Returns a string representation of an instance of ChildMilestones'''
        return "({}) [{}] from {} to {}: {}".format(self.id,
                                       self.type,
                                       self.age_from,
                                       self.age_to,
                                       self.value)

    def to_dict(self):
        '''Returns a dictionary representation of an instance of ChildMilestones'''
        return {'id': self.id,
                'type': self.type,
                'age_from': self.age_from,
                'age_to': self.age_to,
                'value': self.value}
