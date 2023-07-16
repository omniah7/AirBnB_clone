#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes"""

from datetime import datetime
from models import storage
import uuid

class BaseModel:
    """Subclass from which various classes inherit from and also
    it will be the first piece of the serialization/deserialization process
    """

#initialization of instances
def __init__(self, *args, **kwargs):
    """initializes instance attributes
    *Args: lists non-keyworded arguments
    **kwargs: lists keyworded arguments
    """
    self.id = str(uuid.uuid4())
    self.created_at = datetime.now()
    self.updated_at = datetime.now()
    ISO_format =  "%Y-%m-%dT%H:%M:%S.%f"

    if kwargs is not None and kwargs !={}:
        for key in kwargs:
            """loops through key and its values"""
            if key == "created_at" or key == "updated_at":
                """converting to dictionary key with the given value of the time string"""
                self.__dict__[key] = datetime.strptime(value, ISO_format)
            else:
            self.__dict__[key] = kwargs[key]
    else:
        stroge.new(self)

def __str__(self):
    """function that prints content of BaseModel with the following format
    [<class name>] (<self.id>) <self.__dict__>"""
    return "[{}] ({}) {}".\
        format.(type(self).__name__, self.id, self.__dict__)

def save(self):
    """updates the public instance attribute updated_at with the current datetime"""
    self.updated_at = datetime.now()
    storage.save()

def to_dict(self):
    """returns a dictionary containing all keys/values of __dict__ of the instance
    """
    dict_me = self.__dict__.copy()
    dict_me["__class__"] = self.__name__
    dict_me["created_at"] = self.created_at.isoformat()
    dict_me["updated_at"] = self.updated_at.isoformat()

return dict_me
