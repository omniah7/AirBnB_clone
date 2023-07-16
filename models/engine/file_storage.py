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
    
