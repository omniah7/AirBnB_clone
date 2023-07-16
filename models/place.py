#!/usr/bin/python3
"""Place module that contains attribues assigned to places 
and it inherits from BaseModel class"""

from models.base_model import BaseModel

class Place(BaseModel):
    """Place class containing its various public class atrributes"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
