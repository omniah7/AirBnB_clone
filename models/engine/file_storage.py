#!/usr/bin/python3
"""File storage module  manages serialization and deserialization of User"""

import datetime
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

class FileStorage:
    """class for storing, retrieving and manipulating data"""
    __file_path = "file.json"
    __objects = {}

def all(self):
    """returns the dictionary __objects"""
    return FileStorage.__objects

def new(self, obj):
    """ sets in __objects the obj with key <obj class name>.id"""
    key = "{}.{}".format(type(obj).__name__,obj.id)
    FileStorage.__objects[key] = obj

def save(self):
    """serializes __objects to the JSON file (path: __file_path)"""
    dict_json = {}
    for key, value in self. __objects.items():
        dict_json[key] = value.to_dict()
    with open(FileStorage.__file_path, mode="w", encoding="utf-8")as my_file:
        my_file.write(json.dumps(dict_json))

def reload(self):
    """ deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; 
    otherwise, do nothing. If the file doesn’t exist, no exception should be raised
    """
    if not os.path.isfile(FileStorage.__file_path):
        return
    with open(FileStorage.__file_path, "r", encoding="utf=8")as my_file:
        
