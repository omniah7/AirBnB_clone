#!/usr/bin/python3
"""City module that contains attributes assigned to different cities
 and it inherits from BaseModel class
"""

from models.base_model import BaseModel

class City(BaseModel):
    """City class containing public attributes that are empty strings"""

    state_id = ""
    name = ""
