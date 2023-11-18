''' This module contains the BaseModel class
    This class is the base class for all other classes in this project
'''
import uuid
import sqlalchemy



class BaseModel:
    def __init__(self, age_from, age_to, value)
        self.id = str(uuid.uuid4())
        self.age_from = age_from
        self.age_to = age_to
        self.value = value

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
